p1 = "Make a lot of money"
p2 = "Buy Now"
p3 = "Subscribe Now"
p4 = "Click This"

message = input("Enter the message")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This message is spam")
else:
    print("This comment is not spam")