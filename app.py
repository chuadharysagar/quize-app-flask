from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Quiz questions stored in memory with categories
QUESTIONS = [
    {
        "id": 1,
        "category": "Geography",
        "question": "What is the capital of France?",
        "options": ["London", "Paris", "Berlin", "Madrid"],
        "correct_answer": "Paris"
    },
    {
        "id": 2,
        "category": "Programming",
        "question": "Which is not a Python data type?",
        "options": ["List", "Dictionary", "Table", "Tuple"],
        "correct_answer": "Table"
    },
    {
        "id": 3,
        "category": "Web Development",
        "question": "What does HTML stand for?",
        "options": ["Hyper Text Markup Language", "High Tech Modern Language", "Hyper Transfer Markup Language", "High Text Machine Language"],
        "correct_answer": "Hyper Text Markup Language"
    },
    {
        "id": 4,
        "category": "Mathematics",
        "question": "What is 2 + 2 * 2?",
        "options": ["6", "8", "4", "10"],
        "correct_answer": "6"
    },
    {
        "id": 5,
        "category": "Astronomy",
        "question": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "correct_answer": "Mars"
    },
    {
        "id": 6,
        "category": "Biology",
        "question": "What is the largest mammal?",
        "options": ["African Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
        "correct_answer": "Blue Whale"
    },
    {
        "id": 7,
        "category": "Art",
        "question": "Who painted the Mona Lisa?",
        "options": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo"],
        "correct_answer": "Leonardo da Vinci"
    },
    {
        "id": 8,
        "category": "Chemistry",
        "question": "What is the chemical symbol for gold?",
        "options": ["Ag", "Fe", "Au", "Cu"],
        "correct_answer": "Au"
    },
    {
        "id": 9,
        "category": "Language",
        "question": "Which language is most widely spoken in the world?",
        "options": ["English", "Spanish", "Mandarin", "Hindi"],
        "correct_answer": "Mandarin"
    },
    {
        "id": 10,
        "category": "Astronomy",
        "question": "What is the main component of the Sun?",
        "options": ["Helium", "Oxygen", "Hydrogen", "Nitrogen"],
        "correct_answer": "Hydrogen"
    }
]

@app.route('/api/questions', methods=['GET'])
def get_questions():
    return jsonify(QUESTIONS)

if __name__ == '__main__':
    app.run(debug=True)
