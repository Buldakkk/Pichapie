# DICTIONARY  is a collection of {key:value} pairs, ordered and changeable. No dupes

companies = {"ECC": "Zamora St., Tarlac City, Tarlac",
             "Civil Service Commission": "Tarlac City",
             "Tarlac City Water District": " Maliwalo Tarlac City",
             "Wireless Access for Health": "Diwa ng Tarlac"}

print(companies.get("ECC"))  # this accessed the value of the key ECC
print(companies.get("AYO"))  # since it is not in the list, it printed "None"

'''
ask = input("Enter a Company: ")

if ask in companies:
    # {companies[ask]} will print the VALUE of the entered KEY
    print(f"It exists and it is located at {companies[ask]}")
else:
    print("ah wala")   
'''

companies.update({"LGU Capas": "Sto. Domingo 2nd, Capas, Tarlac"})
print(companies)

companies.pop("ECC")  # removes specific key:value
companies.popitem()  # removes latest key:value
print(companies)
