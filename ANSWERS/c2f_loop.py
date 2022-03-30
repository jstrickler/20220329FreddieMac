#!/usr/bin/env python

while True:
    raw_celsius = input('Enter Celsius temp: ')
    if raw_celsius.lower().startswith('q'):
        break
    if raw_celsius.strip() == '':
        print("Please enter the Celsius temperature: ")
        continue
    celsius = float(raw_celsius)
    fahrenheit = ((9 * celsius) / 5) + 32
    print('{:.1f} C is {:.1f} F\n'.format(celsius, fahrenheit))

