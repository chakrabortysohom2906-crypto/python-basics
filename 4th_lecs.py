# DICTIONARY IN PYTHON
# info = {
    # "key" : "value",
    # "name" : "sohom",
    # "learning" : "python",
    # "SUBJECTS" : ["math","english","python"],
    # "topics" : ("c","java","js"),
    # "marks" : [54,76,87,86,90],
# }
# we can print each elements of dictionary.
# print(info["name"])
# print(info["SUBJECTS"])
# we can asssing another value to the key.
# info["name"] = "mithu"
# we can add new key an value in the dictionary.
# info["surname"] = "chakraborty" 
# print(info)
# nested dictionary
# student = {
#     "name" : "sohom",
#     "subjects" : {
#         "physics" : "98",
#         "math" : "95",
#         "chemistry" : "85"
#     }
# }
# print(student["subjects"]["math"])

# Methods of dictionary
# Keys method(give us a list of keys presents in this dictionary.)
# print(info.keys())
# typecast into keys(changing in to list)
# print(list(info.keys()))
# Values method(it returns all the values of the dictionary.)
# print(info.values())
# typecast into all values(changing in to list)
# print(list(info.values()))
# Items method(it returns all value pair of the dictionary in tuple form.)
# print(info.items())
# typecast into all values(changing in to list)
# print(list(info.items()))
# Get method(return the value of the key that is mention.)
# print(info.get("learning")) [in this case if we give a wrong key then it will return 'NONE' value.] 
# print(info["name"]) [this is wrong method because if we enter a wrong key then it will give us a error.]
# Update method 
# info.update({"city":"kolkata"})
# print(info)


# SETS IN PYTHON
# num = {1,2,3,4,5,"hello","world"}
# print(num)
# empty sets
collection = set()

# Methods of sets
# Add method(it add any value in the set of my choice.)
collection.add(55)
collection.add("hello")
collection.add(7.86)
print(collection)

# remove method(it remove any value from the set of my choice.)
collection.remove(55)
print(collection)

# clear method(it clear the whole set.)
# collection.clear()
# print(len(collection))

# Pop method(it deleted any random value from the set.)
collection = {"hello","world","fuck","you",2.67,86}
print(collection.pop())

# union method(it combine two sets in a single set but it doesnot print same value more than once.and it arrange all the value.)
set1 = {1,2,2,4,3,5,6,6,7}
set2 = {6,7,8,9,10}
set = set1.union(set2)
print(set)

#Intersection method(it combine only common value in two set.)
print(set1.intersection(set2))

