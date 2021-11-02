def reorder_data(products,searchWord):
    result = [] 
    products.sort() 
    for i,c in enumerate(searchWord):
         list1 = [j for j in products if len(j) > i and j[i] in c]
         result.append(list1[:3])

    return result


searchWord = "mouse"
products = ["mobile","mouse","moneypot","monitor","mousepad"]

print(reorder_data(products,searchWord))
