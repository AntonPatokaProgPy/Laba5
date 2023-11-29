import temperature_conversion

celsius_temperature = 1
fahrenheit_temperature = 77

converted_fahrenheit = temperature_conversion.celsius_to_fahrenheit(celsius_temperature)
converted_celsius = temperature_conversion.fahrenheit_to_celsius(fahrenheit_temperature)

print("Температура в градусах Фаренгейта:", converted_fahrenheit)
print("Температура в градусах Цельсия:", converted_celsius)
