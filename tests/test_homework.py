from selene import browser, have, be, by
import os.path


def test_practice_from(browser_management):
    browser.open('/automation-practice-form')
    browser.element('#firstName').should(be.blank).type('Sergey')
    browser.element('#lastName').should(be.blank).type('Gavrilenko')
    browser.element('#userEmail').type('serezagavrilenko@gmail.com')
    browser.element('#gender-radio-3').double_click()
    browser.element('#userNumber').type(9920454526)

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element(by.text('June')).click()
    browser.element('.react-datepicker__year-select').click().element(by.text('2003')).click()
    browser.element('.react-datepicker__day--003').click()
    browser.element('#subjectsInput').set_value('Economics').press_enter()
    browser.element('[for=hobbies-checkbox-1]').click()

    browser.element('#uploadPicture').send_keys(os.path.abspath('photo/photo.jpg'))
    browser.element('#currentAddress').type('Artistic driveway 4, sq.1')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Noi').press_enter()
    browser.element('#submit').press_enter()
    browser.element('.modal-content').should(have.text('Thanks for submitting the form'))
    browser.all('tbody tr td:last-child').should(
        have.exact_texts('Sergey Gavrilenko',
                         'serezagavrilenko@gmail.com',
                         'Other',
                         '9920454526',
                         '03 June,2003',
                         'Economics',
                         'Sports',
                         'photo.jpg',
                         'Artistic driveway 4, sq.1',
                         'NCR Noida'))
