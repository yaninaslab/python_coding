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


name = input('What is your name?: ')
distance_km = input('Enter distance in km: ')
distance_miles = float(distance_km)/1.609
print(
    f'Hello {name.title()}! {distance_km} km is equivalent to {round(distance_miles,1)} miles.')
