def main():
	# write code here
	#get the item name
	name = input('Item (enter \"done\" when finished):  ')
	items = []
	#for loop to prepare items list contains list of dictionary each item have name price quantity
	while name != 'done':
		price = input('enter price:  ')
		quantity = input('enter quantity:  ')
		item = {'name':name, 'price':price,'quantity':quantity}
		items.append(item)
		name = input('Item (enter \"done\" when finished):  ')
	print(items)

	print("-------------")
	print("receipt")
	print("-------------")
	#calculate total receipt
	total_price = 0
	#loop in the items to get each item information
	for item in items:
		name = item['name']
		price = float(item['price'])
		quantity = int(item['quantity'])
		item_price = quantity * price
		#add each item total to the total receipt
		total_price += item_price
		total = '%.3f'%item_price
		print(f'{quantity} {name} {total}KD')

	print('-------------')
	total = '%.3f'%total_price
	print(f'Total Price {total}KD')










if __name__ == '__main__':
	main()
