# This is a dictionary it is an example of key value pairs. We can give the dictionary a name and use it to keep values
firstDictionary = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
}
# here we are telling the computer to get the key using a get method. You can put in a default value if the key is
# not found.
print(firstDictionary.get("Feb", "Not a valid key"))