# Define your functions
price = 0
def coffee_bot():
  print("Welcome to the cafe!")

def get_size():
  global price
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  res = res.lower()
  if res == "a":
      res="Small"
      price += 5
  elif res == "b":
      res = "Medium"
      price += 7
  elif res == "c":
      res = "Large"
      price += 10
  else:
      print_message()
      return get_size()
  return res
  
def print_message():
    print ("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")
    
def get_drink_type():
    global price
    res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')
    res = res.lower()
    if res == "a":
      res="Brewed Coffee"
      price = price - 1
    elif res == "b":
      res = "Mocha"
    elif res == "c":
      price += 1
      return order_latte()
    else:
      print_message()
      return get_drink_type()
    return res
    
def order_latte():
    res = input("And what kind of milk for your latte ? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n> ")
    res = res.lower()
    if res == "a":
      res="Latte"
    elif res == "b":
      res = "Non-fat latte"
    elif res == "c":
      res = "Soy latte"
    else:
      print_message()
      return order_latte()
    return res


# Call coffee_bot()
coffee_bot()
size = get_size()
drink_type = get_drink_type()
print ("Alright, that's a {size} {drink_type}. That would be ${price}".format(size = size, drink_type=drink_type, price=price))
name = input("Can i get your name please? \n> ")
print("Thanks, {name}! Your drink will be ready shortly.".format(name = name))