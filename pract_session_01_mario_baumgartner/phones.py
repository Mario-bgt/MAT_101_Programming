import phonenumbers
from phonenumbers import geocoder

phone_number = phonenumbers.parse("+524421910474")
print(geocoder.description_for_number(phone_number, "en"))
