import wx
import json

class FinalScoreDialog(wx.Dialog):
    def __init__(self, parent, score, total_questions):
        super().__init__(parent, title="Quiz Results", size=(400, 300))
        self.score = score
        self.total_questions = total_questions
        self.init_ui()
        
    def init_ui(self):
        panel = wx.Panel(self)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Score display
        percentage = (self.score / self.total_questions) * 100
        score_text = wx.StaticText(panel, 
            label=f"Quiz Completed!\n\nFinal Score: {self.score}/{self.total_questions}\nPercentage: {percentage:.1f}%")
        font = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        score_text.SetFont(font)
        main_sizer.Add(score_text, 0, wx.ALL | wx.ALIGN_CENTER, 20)
        
        # Buttons
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        try_again_btn = wx.Button(panel, label="Try Again")
        try_again_btn.Bind(wx.EVT_BUTTON, lambda evt: self.EndModal(wx.ID_OK))
        button_sizer.Add(try_again_btn, 0, wx.ALL, 5)
        
        quit_btn = wx.Button(panel, label="Quit")
        quit_btn.Bind(wx.EVT_BUTTON, lambda evt: self.EndModal(wx.ID_CANCEL))
        button_sizer.Add(quit_btn, 0, wx.ALL, 5)
        
        main_sizer.Add(button_sizer, 0, wx.ALIGN_CENTER | wx.TOP, 20)
        
        # Performance message
        performance_text = ""
        if percentage >= 90:
            performance_text = "Excellent! You're a programming expert!"
        elif percentage >= 70:
            performance_text = "Good job! Keep learning!"
        elif percentage >= 50:
            performance_text = "Not bad! More practice will help!"
        else:
            performance_text = "Keep studying! You'll improve!"
            
        performance_label = wx.StaticText(panel, label=performance_text)
        performance_label.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL))
        main_sizer.Add(performance_label, 0, wx.ALL | wx.ALIGN_CENTER, 20)
        
        panel.SetSizer(main_sizer)

class QuizFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Programming Quiz', size=(800, 500))
        self.panel = wx.Panel(self)
        
        # Quiz data
        self.questions = [
            # wxPython Questions
            {
                "question": "1. Which method is used to start the main event loop in wxPython?",
                "options": ["run()", "MainLoop()", "start()", "execute()"],
                "correct_answer": 1,
                "category": "wxPython"
            },
            {
                "question": "2. Which class is the base class for all visual widgets in wxPython?",
                "options": ["wxObject", "wxWidget", "wxWindow", "wxControl"],
                "correct_answer": 2,
                "category": "wxPython"
            },
            {
                "question": "3. Which sizer allows widgets to be arranged in rows and columns in wxPython?",
                "options": ["BoxSizer", "GridSizer", "FlexGridSizer", "StaticBoxSizer"],
                "correct_answer": 1,
                "category": "wxPython"
            },
            
            # Node.js Questions
            {
                "question": "4. Which module in Node.js is used to create a web server?",
                "options": ["web", "http", "server", "net"],
                "correct_answer": 1,
                "category": "Node.js"
            },
            {
                "question": "5. What is the default package manager for Node.js?",
                "options": ["yarn", "npm", "pip", "cargo"],
                "correct_answer": 1,
                "category": "Node.js"
            },
            {
                "question": "6. Which of these is NOT a Node.js framework?",
                "options": ["Express", "Koa", "Django", "Nest.js"],
                "correct_answer": 2,
                "category": "Node.js"
            },
            
            # DSA Questions
            {
                "question": "7. What is the time complexity of binary search?",
                "options": ["O(n)", "O(log n)", "O(n²)", "O(1)"],
                "correct_answer": 1,
                "category": "DSA"
            },
            {
                "question": "8. Which data structure follows LIFO principle?",
                "options": ["Queue", "Stack", "Array", "LinkedList"],
                "correct_answer": 1,
                "category": "DSA"
            },
            
            # Aptitude Questions
            {
                "question": "9. If 3x + 4y = 25 and 2x + 3y = 18, what is the value of x?",
                "options": ["5", "7", "3", "4"],
                "correct_answer": 2,
                "category": "Aptitude"
            },
            {
                "question": "10. A train traveling at 60 km/hr takes 15 minutes to cross a platform. If the length of train is 250m, what is the length of platform?",
                "options": ["500m", "750m", "250m", "1000m"],
                "correct_answer": 0,
                "category": "Aptitude"
            }
        ]
        
        self.current_question = 0
        self.score = 0
        self.answered = False
        self.init_ui()
        self.show_question()
        
    def init_ui(self):
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Category display
        self.category_text = wx.StaticText(self.panel, label="", style=wx.ALIGN_CENTER)
        font = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL)
        self.category_text.SetFont(font)
        main_sizer.Add(self.category_text, 0, wx.ALL | wx.ALIGN_CENTER, 10)
        
        # Question text
        self.question_text = wx.StaticText(self.panel, label="", style=wx.ALIGN_CENTER)
        font = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        self.question_text.SetFont(font)
        main_sizer.Add(self.question_text, 0, wx.ALL | wx.ALIGN_CENTER, 20)
        
        # Options
        self.option_buttons = []
        for i in range(4):
            btn = wx.Button(self.panel, label="", size=(500, 40))
            btn.Bind(wx.EVT_BUTTON, lambda evt, x=i: self.check_answer(evt, x))
            main_sizer.Add(btn, 0, wx.ALL | wx.ALIGN_CENTER, 5)
            self.option_buttons.append(btn)
        
        # Navigation buttons
        nav_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.prev_btn = wx.Button(self.panel, label="Previous")
        self.prev_btn.Bind(wx.EVT_BUTTON, self.previous_question)
        nav_sizer.Add(self.prev_btn, 0, wx.ALL, 5)
        
        self.next_btn = wx.Button(self.panel, label="Next")
        self.next_btn.Bind(wx.EVT_BUTTON, self.next_question)
        nav_sizer.Add(self.next_btn, 0, wx.ALL, 5)
        
        main_sizer.Add(nav_sizer, 0, wx.ALIGN_CENTER | wx.TOP, 20)
        
        # Score display
        self.score_text = wx.StaticText(self.panel, label=f"Score: {self.score}/{len(self.questions)}")
        main_sizer.Add(self.score_text, 0, wx.ALL | wx.ALIGN_CENTER, 10)
        
        self.panel.SetSizer(main_sizer)
        
    def show_question(self):
        question_data = self.questions[self.current_question]
        self.category_text.SetLabel(f"Category: {question_data['category']}")
        self.question_text.SetLabel(question_data["question"])
        
        for i, option in enumerate(question_data["options"]):
            self.option_buttons[i].SetLabel(option)
            self.option_buttons[i].SetBackgroundColour(wx.NullColour)
        
        self.answered = False
        self.update_navigation_buttons()
        
    def check_answer(self, event, selected_option):
        if self.answered:
            return
            
        question_data = self.questions[self.current_question]
        correct_answer = question_data["correct_answer"]
        
        if selected_option == correct_answer:
            self.score += 1
            self.option_buttons[selected_option].SetBackgroundColour(wx.Colour(144, 238, 144))  # Light green
        else:
            self.option_buttons[selected_option].SetBackgroundColour(wx.Colour(255, 182, 193))  # Light red
            self.option_buttons[correct_answer].SetBackgroundColour(wx.Colour(144, 238, 144))
            
        self.score_text.SetLabel(f"Score: {self.score}/{len(self.questions)}")
        self.answered = True
        
        # If this is the last question, show final score dialog
        if self.current_question == len(self.questions) - 1:
            self.show_final_score()
        
    def next_question(self, event):
        if self.current_question < len(self.questions) - 1:
            self.current_question += 1
            self.show_question()
            
    def previous_question(self, event):
        if self.current_question > 0:
            self.current_question -= 1
            self.show_question()
            
    def update_navigation_buttons(self):
        self.prev_btn.Enable(self.current_question > 0)
        self.next_btn.Enable(self.current_question < len(self.questions) - 1)
        
    def show_final_score(self):
        dialog = FinalScoreDialog(self, self.score, len(self.questions))
        result = dialog.ShowModal()
        
        if result == wx.ID_OK:
            # Reset the quiz
            self.current_question = 0
            self.score = 0
            self.answered = False
            self.score_text.SetLabel(f"Score: {self.score}/{len(self.questions)}")
            self.show_question()
        else:
            # Close the application
            self.Close()
        
        dialog.Destroy()

def main():
    app = wx.App()
    frame = QuizFrame()
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()