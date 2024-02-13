import dataclasses
from enum import Enum


class Gender(Enum):
    Male = 'Male'
    Female = 'Female'
    Other = 'Other'


class Hobby(Enum):
    Sports = 'Sports'
    Reading = 'Reading'
    Music = 'Music'


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    mobile_num: str
    date_of_birth_year: str
    date_of_birth_month: str
    date_of_birth_day: str
    subjects: str
    hobbies: Hobby
    photo: str
    current_address: str
    state: str
    city: str


alex = User(
    first_name="Alex",
    last_name="Yanin",
    email="test@test.ru",
    gender=Gender.Male,
    mobile_num="7916896581",
    date_of_birth_year='1982',
    date_of_birth_month='April',
    date_of_birth_day='10',
    subjects="Computer Science",
    hobbies=Hobby.Sports,
    photo="photo.jpg",
    current_address="random residential address",
    state="NCR",
    city="Delhi",
)
