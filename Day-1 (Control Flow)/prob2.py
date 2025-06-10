m1 = int(input("Enter Maarks m1 :"))
m2 = int(input("Enter Maarks  m2:"))
m3 = int(input("Enter Maarks  m3:"))

#calculate percentage
total_percentage = (100*(m1+m2+m3))/300

if (total_percentage >= 40 and m1 >= 33 and m2 >= 33 and m3 >= 33):
    print("You have passed",total_percentage)
else:
    print("you have failed",total_percentage)