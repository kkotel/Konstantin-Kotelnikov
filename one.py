
print ("-= Start =-")
phones=["iPhone Xs","Samsung Galaxy S10","Xiaomi Mi8"]
product = {
    "name":"iPhone Xs", 
    "stock":5, 
    "price": 65000.0,
    "recomend": phones
}
print (product["recomend"])
print (product["recomend"][1])
product["recomend"].append("iPhone 6")
print (product)
