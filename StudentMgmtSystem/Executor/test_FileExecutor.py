from LearningPytest.StudentMgmtSystem.LogicFile.LogicFile import *
import pytest

@pytest.mark.smoke
def test_method_executor():
    add_student()
    get_student_data()


@pytest.mark.sanity
def test_studentData_executor():
    get_student_data()


@pytest.mark.skip("not")
def test_addstudent_executor():
    add_student()



