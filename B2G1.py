username = input("Please enter your name :")
print("Hello ", username)
cost1 = int(input("Please enter cost of product 1 :"))
cost2 = int(input("Please enter cost of product 2 :"))
cost3 = int(input("Please enter cost of product 3 :"))
total=cost1+cost2+cost3

if (cost1!=0) and (cost2!=0) and (cost3!=0):

    print("Your initial bill before discount was : INR",total)
    if (cost1<cost2) and (cost1<cost3):
        lowest = int(cost1)

    elif (cost2<cost1) and (cost2<cost3):
        lowest = int(cost2)
    else:
        lowest = int(cost3)

    bill = total-lowest

    print("Your total payable amount after discount is : INR" , bill)

else:
    print("You're not eligible for the discount :( Please add one more product to avail this offer")
    bill=total
    print("your billing amount is :",bill)




