#program to track the location of mobile number by using python number.
import phonenumbers as ph
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier

number =input("Enter the phone number wiht country code \n :>>>>")

#Parsing String to the Phone number
phonenumber=ph.parse(number)

#printing the timezone using the timezone module.
timezone=timezone.time_zones_for_number(phonenumber)
print("timezone:"+str(timezone))

#printing the geolocation of the given number using the geocoder module.
geolocation=geocoder.description_for_number(phonenumber,"en")
print("location:"+geolocation)

#printing the service provider name using the carrier mocule 
service=carrier.name_for_number(phonenumber,"en")
print("service provide:"+service)

