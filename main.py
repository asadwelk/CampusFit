import requests
from bs4 import BeautifulSoup

URL = "https://nutrition.sa.ucsc.edu/"
page = requests.get(URL)
html = page.text 

soup = BeautifulSoup(html, "html.parser")
links = soup.findAll("a")
colleges = []
for x in links:
    colleges.append(x.get("href"))
# for i in colleges:
#    print(i) 
#    print()

val = input("Which college would you like to eat at?")
val = val.capitalize()
# print(val)

match = ''
for i in colleges:
    if val in i:
        match = i
        # print(match)

url = URL + match 
# print(url)

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
#print(soup.get_text())

#Hardcoded solution after this point on:
Breakfast = {"Chocolate Chip Pancakes": ["Vegetarian", "Soy", "Eggs", "Dairy"], 
"Hard-boiled Cage Free Egg (1)": ["Vegetarian", "Eggs", "Gluten-Free"], 
"Organic Oatmeal Gluten-Free": ["Vegan", "Gluten-Free"],
"Potatoes O'Brien": ["Vegan", "Gluten-Free"],
"Thai Tofu Scramble": ["Vegan", "Soy"],
"Turkey Bacon": ["Gluten-Free"],
"Cage-Free Scrambled Eggs": ["Vegetarian", "Eggs", "Gluten-Free"],
"Steamed Rice": ["Vegan", "Gluten-Free"],
"Apple Walnut Muffin": ["Vegetarian", "Soy", "Eggs", "Dairy", "Tree Nuts"],
"Assorted Scones": ["Vegetarian","Soy", "Eggs", "Dairy"],
"Muffin Blueberry Oat Bran": ["Vegetarian","Soy", "Eggs", "Dairy"]}

Lunch = {"Chocolate Chip Pancakes": ["Vegetarian", "Soy", "Eggs", "Dairy"],
"Organic Oatmeal Gluten-Free": ["Vegan", "Gluten-Free"],
"Potatoes O'Brien": ["Vegan", "Gluten-Free"],
"Thai Tofu Scramble": ["Vegan", "Soy"], 
"Turkey Bacon": ["Gluten-Free"],
"Chicken Noodle Soup": ["Soy", "Eggs"],
"Falafels": ["Vegetarian"],
"Parsley Mint Sauce": ["Vegan", "Gluten-Free"],
"Steamed Basmati Rice": ["Vegan", "Gluten-Free"],
"Tahini Sauce": ["Vegan", "Gluten-Free"],
"Braised Toscano Potatoes": ["Vegan", "Gluten-Free"],
"Roast Pork Loin with Parsley and Shallot Sauce": ["Pork", "Gluten-Free"],
"Steamed Seasonal Vegetables": ["Vegan", "Gluten-Free"],
"Allergen Free Halal Chicken Thigh": ["Gluten-Free", "Halal"], 
"Tofu with Kosher Salt": ["Vegan", "Soy", "Gluten-Free"],
"Cheese Pizza": ["Vegetarian", "Soy", "Eggs", "Dairy"],
"Chipotle Chicken Pizza": ["Soy", "Eggs", "Dairy"],
"Steamed Rice": ["Vegan", "Gluten-Free"],
"Chocolate Chip Vegan Cookie Pacific": ["Vegan", "Soy"],
"Lemon Loaf": ["Vegetarian", "Soy", "Eggs", "Dairy"],
"Grilled Huli Huli Chicken": ["Soy", "Grilled Huli Huli Chicken"],
"Hawaiian Coleslaw": ["Vegan", "Gluten-Free"],
"Spam Fried Rice": ["Gluten-Free", "Eggs", "Pork", "Gluten-Free"],
"Sticky Rice": ["Vegan", "Gluten-Free"],
"Szechuan Sweet Chili Tofu": ["Vegan", "Soy", "Gluten-Free"]}

Dinner = {"Chicken Noodle Soup": ["Soy", "Eggs"], 
"Vegan Split Pea Soup": ["Vegan", "Gluten-Free"],
"Fried Plantains" : ["Vegan", "Gluten-Free"],
"Quinoa with Lemon and Thyme" : ["Vegan", "Gluten-Free"],
"Vegan Koshary, Egyptian Rice, and Chickpeas" : ["Vegan"],
"Vegan Tenders" : ["Vegan", "Soy"],
"Chipotle BBQ Beef Brisket": ["Soy", "Beef", "Fish"],
"Macaroni & Cheese": ["Soy", "Eggs", "Dairy", "Fish"],
"Steamed Seasonal Vegetables": ["Vegan", "Gluten-Free"],
"Allergen Free Halal Chicken Thigh": ["Gluten-Free", "Halal"],
"Tofu with Kosher Salt": ["Vegan", "Soy", "Gluten-Free"],
"Cheese Pizza": ["Vegetarian", "Soy", "Eggs", "Dairy"],
"Chipotle Chicken Pizza": ["Soy", "Eggs", "Dairy"],
"Steamed Rice": ["Vegan", "Gluten-Free"],
"Apple Pie": ["Vegan", "Soy"],
"Chocolate S'more Pie": ["Soy", "Dairy", "Pork"],
"Pork Carnitas": ["Pork", "Gluten-Free"],
"Refried Beans": ["Vegan", "Soy", "Gluten-Free"],
"Taqueria Chicken": ["Gluten-Free"],
"Tortilla Chips": ["Vegan", "Gluten-Free"]}

choose = input("\nHide specific options (1)\nNo restrictions (2)")
b = []
l = [] 
d = []
restrict = False

if choose == "1":
  hide = input("\nChoose items to hide (Dairy, Eggs, Fish, Shellfish, Tree Nuts, Peanuts, Soy, Pork, Beef):")
  restrictions = hide.split(", ")
  for key, value in Breakfast.items():
    for food in restrictions: 
      if food in value:
        restrict = True
    if restrict is not True: 
      b.append(key)
    restrict = False
  for key, value in Lunch.items():
    for food in restrictions: 
      if food in value:
        restrict = True
    if restrict is not True: 
      l.append(key)
    restrict = False
  for key, value in Dinner.items():
    for food in restrictions: 
      if food in value:
        restrict = True
    if restrict is not True: 
      d.append(key)
    restrict = False
  print("\nBreakfast:")
  for i in b: 
    print(i)
  print("\nLunch:")
  for i in l: 
    print(i)
  print("\nDinner:")
  for i in d: 
    print(i)
  
# elif choose == "2":
#   show = input("\nChoose items to show (Vegan, Vegetarian, Gluten-free, Eggs, Fish, Dairy, Peanuts, Soy, Pork, Beef, Halal, Shellfish, Tree Nuts):")
#   allow = show.split(", ")
#   for key, value in Breakfast.items():
#     for food in allow: 
#       if food in value:
#         b.append(key)
#     # if restrict is False: 
#     #   b.append(key)
#     # allow = True
#   print("\nb", b)
#   print("\nl", l)
#   print("\nd", d)

else:
  b = list(Breakfast.keys())
  l = list(Lunch.keys())
  d = list(Dinner.keys())
  print("\nBreakfast:")
  for i in b: 
    print(i)
  print("\nLunch:")
  for i in l: 
    print(i)
  print("\nDinner:")
  for i in d: 
    print(i) 