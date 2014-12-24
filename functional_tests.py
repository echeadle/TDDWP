from selenium import webdriver

browser = webdriver.Firefox()

#Edith has heard about a new online to-do app.
#She goes to check out it's home page.
browser.get('http://localhost:8000')

# She notices the pathe title and header metin to-do lists.
assert 'To-Do' in browser.title

#She is invited  to enter a to-do item straight away.

# She types "Buy peacock feathers" into the text box

# When she hits enter, the page updates, and now the page lists
# "1: Buy peacock feathers" as an item in the list

# There is still a  text box inviting her to add another item.
# She enters "Use peacock feathers to make a fly"


# The page updates again, and now shows both items on her list.

# Edith wonders whether the site will remember her list. Then she
# sees that the site has generated a unique URL for her -- there is some
# explanatory text to that effect.

# She visits that URL - her to-do list is still there.

#Satisfied, she goes back to sleep.

browser.quit() 
