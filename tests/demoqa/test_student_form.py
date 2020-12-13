"""Test Demo Form"""
import os
import pytest
from common.webdriver_factory import create_driver_instance, ROOT_DIR
from pages.demoqa.practice_form import PracticeForm


STUDENTS_DATA = [
   ('Luis', 'Rivas', 'luis@gmail.com', 'Male','018201820182','Dec 15 2000'),
   ('Sofia', 'Valenzuela', 'sofia@gmail.com', 'Male','0101010101','Jan 15 1994'),
   ('Miguel', 'Perez', 'miguel@gmail.com', 'Female','00123','Mar 15 1987')
]


@pytest.mark.parametrize("first_name, last_name, email, gender, mobile, date_of_birth", STUDENTS_DATA)
def test_one(first_name, last_name, email, gender, mobile, date_of_birth):
   """Test form"""
   driver = create_driver_instance('chrome')
   page = PracticeForm(driver, 2)
   page.open()
   page.wait_until_loaded()
   page.set_first_name(first_name)
   page.set_last_name(last_name)
   page.set_email(email)
   page.set_gender(gender)
   page.set_mobile(mobile)
   page.set_date_of_birth(date_of_birth)
   page.set_subject('Maths')
   page.set_subject('Computer Science')
   page.set_hobbies('Sports')
   file_path = os.path.join(ROOT_DIR, '.gitignore')
   page.set_file(file_path)
   page.set_current_address('TEST ADDRESS')
   page.set_state('NCR')
   page.set_city('Delhi')
   confirmation_form = page.submit()
   confirmation_form.wait_until_loaded()
   info = confirmation_form.get_table_info()
   assert info['Student Name'] == f'{first_name} {last_name}', 'Confirmation name is not valid'
   confirmation_form.close()
   page.close()

