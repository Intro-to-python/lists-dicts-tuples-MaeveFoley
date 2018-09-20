#lists/dictionaries/tuples

#create a list and show how we can find certain items in list
#add item to list

animal_list = ["dog", "cat", "bird", "horse", "mouse"]
print("this is an example of a list", animal_list)

# tuples cannot be changed once created, no append or delete
# helpful because sometimes you want to create
# something that you know will never change
fibs = (0,1,1,2,3)
print("this is an example of a tuple", fibs)

#dictionaries aka dicts aka map
#key:value pairing

favoriteSports = {"Ralph Williams":"Football", "Michael Tippett":"Basketball", "Edward Elgar":"Baseball", "Rebecca Clarke":"Netball", "Ethel Smyth":"Badminton", "Frank Bridge":"Rugby"}
print(favoriteSports["Rebecca Clarke"])
del favoriteSports["Ethel Smyth"]
print(favoriteSports)
