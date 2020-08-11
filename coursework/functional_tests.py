from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class WelcomePageTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_move_to_home_page(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('Saud Almbdal', self.browser.title)
        time.sleep(7)

        self.assertEqual(self.browser.current_url,'http://localhost:8000/home/')

        self.fail('Finish the Welcome page test!')

class ContactAppTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_valid_message(self):
        self.browser.get('http://localhost:8000/contact/')
        time.sleep(2)

        name = self.browser.find_element_by_id('name')
        self.assertEqual(
            name.get_attribute('placeholder'), 'Your Name *')

        name.send_keys('Saud Almbdal')

        email = self.browser.find_element_by_id('email')
        self.assertEqual(
            email.get_attribute('placeholder'), 'Your Email *')

        email.send_keys('s.almbdal@gmail.com')

        title = self.browser.find_element_by_id('subject')
        self.assertEqual(
            title.get_attribute('placeholder'), 'Message Title *')

        title.send_keys('Functional test for contact app')

        message = self.browser.find_element_by_id('message')
        self.assertEqual(
            message.get_attribute('placeholder'), 'Your Message *')

        message.send_keys('Hello, this message is just for testing the application')

        time.sleep(2)

        submit = self.browser.find_element_by_id('submitButton')

        submit.click()

        alert = self.browser.find_element_by_id('alert').text

        self.assertEqual(alert, 'Your message has been sent')
        time.sleep(3)

        self.fail('Finish Contact Test!')


    def test_invalid_message(self):
        self.browser.get('http://localhost:8000/contact/')
        time.sleep(2)

        name = self.browser.find_element_by_id('name')
        self.assertEqual(
            name.get_attribute('placeholder'), 'Your Name *')

        name.send_keys('Saud Almbdal')

        email = self.browser.find_element_by_id('email')
        self.assertEqual(
            email.get_attribute('placeholder'), 'Your Email *')

        email.send_keys('s.almbdalgmail.com')

        title = self.browser.find_element_by_id('subject')
        self.assertEqual(
            title.get_attribute('placeholder'), 'Message Title *')

        title.send_keys('Functional test for contact app')

        message = self.browser.find_element_by_id('message')
        self.assertEqual(
            message.get_attribute('placeholder'), 'Your Message *')

        message.send_keys('Hello, this message is just for testing the application')

        time.sleep(2)

        submit = self.browser.find_element_by_id('submitButton')

        submit.click()

        alert = self.browser.find_element_by_id('alert').text

        self.assertEqual(alert, 'Your message has not been sent. Make sure you entered the details correctly.')
        time.sleep(3)

        self.fail('Finish Contact Test!')

class cvAppTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        self.browser.get('http://localhost:8000/cv/')
        time.sleep(2)

        education = self.browser.find_element_by_id('education').text
        self.assertIn('University of Birmingham', education)

        proLang = self.browser.find_element_by_id('proLang').text
        self.assertIn('Java', proLang)

        self.fail('Finish the cv test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')

