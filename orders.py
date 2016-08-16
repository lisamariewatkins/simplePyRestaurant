from __future__ import print_function
import random
import requests

my_request = requests.get('http://go.codeschool.com/spamvanmenu')
menu_list = my_request.json()

print(menu_list)

print("Today's Menu:")
for item in menu_list:
	print(item['name'], ': ', item['desc'].title(), ', $', item['price'], sep='')

def print_menu(menu):
	for name, price in menu.items():
		print(name, ': ', format(price, '.2f'), sep='')

def get_order(menu):
	orders = []
	order = raw_input('What would you like to order?')
	while (True):
		#order = raw_input('What would you like to order?')
		#if order == 'Cheerio Spam':
			#print('Sorry, we are all out of that!')
			#continue
		if order == 'Q':
			break
		found = menu.get(order)
		if found:
			orders.append(order)
		else:
			print ("Menu item doesn't exist")
		order = raw_input("Anything else? (Q to Quit)")

	return orders

# def dollar_menu():
# 	file = open('dollar_menu.txt', 'r')
# 	for line in file:


def bill_total(orders, menu):
        total = 0

        for order in orders:
                total += menu[order]
        return total

def write_sales_log(order):
	file = open('sales.txt', 'a')

	total = 0

	for item in order:
		file.write(item + ' ' + '\n')
	
	file.close()

def main():
	slang = ['Knackered', 'Pip Pop', 'Squidgy', 'Smashing', 'Cheerio', 'Odd Duck']

	menu = []

	for word in slang:
		menu.append(word + ' Spam')

	menu_prices = {}

	price = 0.50
	for item in menu:
		menu_prices[item] = price
		price = price + 1

	print_menu(menu_prices)
	orders = get_order(menu_prices)
	total = bill_total(orders, menu_prices)
	write_sales_log(orders)
	file = open('sales.txt', 'a')
	file.write('Total: ' + str(total) + '\n' + '---------------')
	file.close()
	print("You ordered:", orders,
              "Your total is: $", format(total, '.2f'), sep='')
	

main()
