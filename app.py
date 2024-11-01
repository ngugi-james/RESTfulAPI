from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory storage for students with two initial students
students_db = {
    1: {
        "id": 1,
        "name": "John Doe",
        "grade": "A",
        "email": "johndoe@example.com"
    },
    2: {
        "id": 2,
        "name": "Alice Smith",
        "grade": "B",
        "email": "alicesmith@example.com"
    }
}

# Helper function to generate a new unique ID
def generate_new_id():
    if students_db:
        return max(students_db.keys()) + 1
    return 1

# GET /students: Retrieve a list of all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(list(students_db.values())), 200

# GET /students/<id>: Retrieve details of a student by ID
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = students_db.get(id)
    if not student:
        abort(404, description="Student not found")
    return jsonify(student), 200

# POST /students: Add a new student
@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    if not data or 'name' not in data or 'grade' not in data or 'email' not in data:
        abort(400, description="Missing required fields")

    # Generate a new ID
    new_id = generate_new_id()
    
    # Create the new student entry
    new_student = {
        "id": new_id,
        "name": data['name'],
        "grade": data['grade'],
        "email": data['email']
    }
    
    # Add the new student to the database
    students_db[new_id] = new_student
    return jsonify(new_student), 201

# PUT /students/<id>: Update an existing student by ID
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    if id not in students_db:
        abort(404, description="Student not found")

    data = request.get_json()
    if not data or 'name' not in data or 'grade' not in data or 'email' not in data:
        abort(400, description="Missing required fields")

    # Update the student entry
    students_db[id].update({
        "name": data['name'],
        "grade": data['grade'],
        "email": data['email']
    })
    return jsonify(students_db[id]), 200

# DELETE /students/<id>: Delete a student by ID
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    if id not in students_db:
        abort(404, description="Student not found")
    del students_db[id]
    return jsonify({"message": "Student deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
