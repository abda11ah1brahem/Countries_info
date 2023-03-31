result={}
with open('country.txt','r') as country_data:
    country_data.readline()
    for i in country_data:
        data= i.strip().split("|")
        Country, Capital, CC, CC3, IAC, TimeZone, Currency = data
        countries = {
            "name":Country,
            "capital":Capital,
            "Time Zone":TimeZone
        }
        result[Country]=countries
while True:
    user_choice = input("plz enter user choice : ")
    if user_choice in result:
        country_info=result[user_choice]
        print(f"capital of {user_choice} is \"{country_info['capital']}\" and time zone is \"{country_info['Time Zone']}")
    else:
       print("Not Found")
       break