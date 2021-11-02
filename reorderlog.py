def reorder_data(nums):
    digit = []
    letter = []

    for i in nums:
        if(i.split()[1].isdigit()):
            digit.append(i)
        else:
            letter.append(i)  

    letter.sort(key=lambda i: i.split()[0])
    letter.sort(key=lambda i: i.split()[1:])  
    result = letter + digit
    return result


nums = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

print(reorder_data(nums))
