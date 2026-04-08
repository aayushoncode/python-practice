#ask he user for a temperature in celsius (string input). convert it to float ,
# then calculate and print temperature and print temperature in fahrenheit.

''' 
 conversion formula : fahrenheitTemp = (celciusTemp *( 9/5)) + 32


'''

celciusTemp = float(input("enter the temperature in celsius : "))

fehrenheitTemp = (celciusTemp * (9/5))+32

print(f"celcius : {celciusTemp}degree \nfehrenheit : {fehrenheitTemp}")