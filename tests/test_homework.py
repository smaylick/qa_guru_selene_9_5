from demoqa_tests.pages.registration_page import RegistrationPage
from demoqa_tests.data.users import test_user


def test_registration():
    registration_page = RegistrationPage()
    registration_page.open_registration_page()
    registration_page.register(test_user)
    registration_page.should_registered_user_with(test_user)
