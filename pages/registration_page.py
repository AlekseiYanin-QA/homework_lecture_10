import os
from selene import browser, be, have, by


class RegistrationPage:
    def open(self):
        browser.open('automation-practice-form')
        browser.driver.execute_script("document.querySelector('#fixedban').remove();")
        browser.driver.execute_script("document.querySelector('footer').remove();")

    def fill_first_name(self, value):
        browser.element("#firstName").should(be.blank).send_keys(value)

    def fill_last_name(self, value):
        browser.element("#lastName").should(be.blank).send_keys(value)

    def fill_email(self, value):
        browser.element("#userEmail").should(be.blank).send_keys(value)

    def select_gender(self, value):
        browser.element("[for='gender-radio-1']").click()

    def fill_phone_number(self, value):
        browser.element("#userNumber").should(be.blank).send_keys(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element(".react-datepicker__year-select").send_keys(year)
        browser.element(".react-datepicker__month-select").send_keys(month)
        browser.element(f".react-datepicker__day--0{day}").click()

    def type_subjects(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def select_hobbies(self):
        browser.element('[for="hobbies-checkbox-1"]').click()
        browser.element('[for="hobbies-checkbox-2"]').click()
        browser.element('[for="hobbies-checkbox-3"]').click()
        return self

    def upload_picture(self, value, ):
        browser.element("#uploadPicture").send_keys(os.path.abspath(value))

    def type_current_address(self, value):
        browser.element('#currentAddress').should(be.blank).type(value)

    def fill_state(self, value):
        browser.element("#state").should(be.clickable).click()
        browser.element(by.text(value)).should(be.clickable).click()

    def fill_city(self, city):
        browser.element("#city").should(be.clickable).click()
        browser.element(by.text(city)).should(be.clickable).click()

    def submit(self):
        browser.element('#submit').should(be.clickable).click()

    def should_have_registered_user_with(self, first_name, last_name, email, gender, mobile, date_of_birth,\
                                         subjects, hobbies, picture, current_address, state_city):
        browser.element(".table").all("td").even.should(have.texts(
            f"{first_name} {last_name}",
            email,
            gender,
            mobile,
            date_of_birth,
            subjects,
            hobbies,
            picture,
            current_address,
            state_city))
