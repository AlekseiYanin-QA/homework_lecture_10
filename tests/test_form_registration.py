from data import users
from pages.resource import RegistrationPage


def test_student_registration_form_2():
    registration_page = RegistrationPage()
    student = users.alex
    registration_page.open()
    # WHEN
    registration_page.user_registration(student)
    # THEN
    registration_page.should_have_registered_user_with(student)
