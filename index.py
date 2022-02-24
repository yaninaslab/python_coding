msg = 'welcome to Python 101: Strings'

print(msg)
msg1 = msg[18]+' '+msg[:8]+msg[25:29]+msg[7:11] + \
    msg[13]+msg[12]+msg[2]+msg[1]+msg[-5]
print(msg1.title())

print(msg1[::-1].title())


msg2 = """Dear Terry,,
You must cut down the mightiest 
tree in the forest with…
a herring! <3"""
print(msg2)


name = 'TERRY'
color = 'RED'
msg = '[' + name + '] loves the color ' + color.lower() + '!'
msg1 = f'[{name.capitalize()}] loves the color {color.lower()}!'
print(msg)
print(msg1)


# name = input('What is your name?: ')
# distance_km = input('Enter distance in km: ')
# distance_miles = float(distance_km)/1.609
# print(
#     f'Hello {name.title()}! {distance_km} km is equivalent to {round(distance_miles,1)} miles.')

friends = ['John', 'Jane', 'Joe', 'Jessie']
cars = [1, 4, 7, 2, 9, 6]
cars.sort()
friends.reverse()
print(friends)
print(cars)


sales_w1 = [7, 3, 42, 19, 15, 35, 9]
sales_w2 = [12, 4, 26, 10, 7, 28]
sales = []

new_day = input('How many drinks did you sell on Sunday?: ')
sales_w2.append(int(new_day))

sales.extend(sales_w1)
sales.extend(sales_w2)
# sales = sales_w1 + sales_w2
# total_drinks = sum(sales)
# sales.sort()
# print(sales)
worst_day = min(sales) * 1.5
best_day = max(sales) * 1.5
# total_sales = total_drinks * 1.5
print(f'Worst day profit:$ {worst_day}')
print(f'Best day profit: $ {best_day}')
print(f'Combined profit:$ {worst_day + best_day}')
