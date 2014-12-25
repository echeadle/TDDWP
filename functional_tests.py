from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisiterTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
 
    def tearDown(self):
        self.browser.quit()
        
    def test_can_start_a_list_and_retrive_it_later(self):
        #Edith has heard about a new online to-do app.
        # She goes to check out it's home page.
        self.browser.get('http://localhost:8000')
        # She notices the the page title and header metions to-do lists.
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        #self.fail('Finish the test!')

        #She is invited  to enter a to-do item straight away.
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
        )

        # She types "Buy peacock feathers" into the text box
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in the list
        inputbox.send_keys(Keys.ENTER)
        # import time
        # time.sleep(10) 
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
               any(row.text == '1: Buy peacock feathers' for row in rows),
               "New to-do item did not appear in the table"
        )

        # There is still a  text box inviting her to add another item.
        # She enters "Use peacock feathers to make a fly"
        self.fail('Finish the test!')
        
       # The page updates again, and now shows both items on her list.
    
        # Edith wonders whether the site will remember her list. Then she
        # sees that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.

        # She visits that URL - her to-do list is still there.

        #Satisfied, she goes back to sleep.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
