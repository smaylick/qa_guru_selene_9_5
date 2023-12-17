from demoqa_tests.pages.registration_page import RegistrationPage


def test_practice_from():
    registration_page = RegistrationPage()
    registration_page.open_registration_page()

    registration_page.fill_first_name('Sergey')
    registration_page.fill_last_name('Gavrilenko')
    registration_page.fill_user_email('serezagavrilenko@gmail.com')
    registration_page.gender_selection('Male')
    registration_page.fill_user_phone_number(9920454526)
    registration_page.fill_date_of_birth('2003', 'June', '03')
    registration_page.select_user_subject('Economics')
    registration_page.user_hobby_checkbox('Sports')
    registration_page.user_picture('photo.jpg')
    registration_page.user_current_adress('Artistic driveway 4, sq.1')
    registration_page.user_state('NCR')
    registration_page.user_city('Noida')
    registration_page.submit_the_form()

    registration_page.should_registered_user_with(
        'Sergey Gavrilenko',
        'serezagavrilenko@gmail.com',
        'Male',
        '9920454526',
        '03 June,2003',
        'Economics',
        'Sports',
        'photo.jpg',
        'Artistic driveway 4, sq.1',
        'NCR Noida',
    )
