from selene import browser, have, be
from selene.core import command
from selene.support.shared.jquery_style import s
import resource
from data.users import User


class RegistrationPage:
    def __init__(self):
        self.first_name = s('#firstName')
        self.last_name = s('#lastName')
        self.date_of_birth = s('#dateOfBirthInput')
        self.email = s('#userEmail')
        self.gender = browser.all('[for^=gender-radio]')
        self.mobile = s('#userNumber')
        self.subject = s('#subjectsInput')
        self.hobby = browser.all('[for^=hobbies-checkbox]')
        self.picture = s('#uploadPicture')
        self.current_address = s('#currentAddress')
        self.state_dropdown = browser.all('[id^=react-select][id*=option]')
        self.city_dropdown = browser.all('[id^=react-select][id*=option]')
        self.submit_button = s('#submit')

    def open(self):
        browser.open('automation-practice-form')
        browser.driver.execute_script("document.querySelector('#fixedban').remove();")
        browser.driver.execute_script("document.querySelector('footer').remove();")

    def fill_first_name(self, user: User):
        self.first_name.should(be.blank).type(user.first_name)
        return self

    def fill_last_name(self, user: User):
        self.last_name.should(be.blank).type(user.last_name)
        return self

    def fill_date_of_birth(self, user: User):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__year-select").send_keys(user.date_of_birth_year)
        browser.element(".react-datepicker__month-select").send_keys(user.date_of_birth_month)
        browser.element(f".react-datepicker__day--0{user.date_of_birth_day}").click()
        return self

    def fill_email(self, user: User):
        self.email.should(be.blank).type(user.email)
        return self

    def select_gender(self, user: User):
        self.gender.element_by(have.exact_text(user.gender.value)).click()
        return self

    def fill_mobile_number(self, user: User):
        self.mobile.type(user.mobile_num)
        return self

    def fill_subject(self, user: User):
        self.subject.type(user.subjects).press_enter()
        return self

    def select_hobby(self, user: User):
        self.hobby.element_by(have.exact_text(user.hobbies.value)).click()
        return self

    def upload_picture(self, user: User):
        self.picture.set_value(resource.path(user.photo))
        return self

    def fill_current_address(self, user: User):
        self.current_address.should(be.blank).perform((command.js.set_value(user.current_address)))
        return self

    def select_state(self, user: User):
        s('#state').click()
        self.state_dropdown.element_by(have.exact_text(user.state)).click()
        return self

    def select_city(self, user: User):
        s('#city').click()
        self.city_dropdown.element_by(have.exact_text(user.city)).click()
        return self

    def submit(self):
        self.submit_button.perform(command.js.click)

    def user_registration(self, user: User):
        self.fill_first_name(user) \
            .fill_last_name(user) \
            .fill_email(user) \
            .select_gender(user) \
            .fill_mobile_number(user) \
            .fill_date_of_birth(user) \
            .fill_subject(user) \
            .select_hobby(user) \
            .upload_picture(user) \
            .fill_current_address(user) \
            .select_state(user) \
            .select_city(user) \
            .submit()

    def should_have_registered_user_with(self, user: User):
        browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
        browser.element('.table').all('td').even.should(
            have.texts(
                f'{user.first_name} {user.last_name}',
                {user.email},
                {user.gender.value},
                {user.mobile_num},
                f'{user.date_of_birth_day} {user.date_of_birth_month},{user.date_of_birth_year}',
                {user.subjects},
                {user.hobbies.value},
                {user.photo},
                {user.current_address},
                f'{user.state} {user.city}'
            )
        )
