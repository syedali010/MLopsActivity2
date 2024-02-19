from main import StudentsInMLOps

def test_enroll_students():
    classroom = StudentsInMLOps()
    classroom.enrollStudents(5)
    assert classroom.getTotalStrength() == 5

def test_drop_students():
    classroom = StudentsInMLOps()
    classroom.enrollStudents(5)
    classroom.dropStudents(3)
    assert classroom.getTotalStrength() == 2

def test_get_total_strength():
    classroom = StudentsInMLOps()
    classroom.enrollStudents(3)
    assert classroom.getTotalStrength() == 3

def test_get_class_name():
    classroom = StudentsInMLOps()
    assert classroom.getClassName() == "MLOps Basics"
