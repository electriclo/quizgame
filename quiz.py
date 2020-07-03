q1 = "what color is the sky?  a.blue, b.red, c.green, d.yellow"
print (q1)
userchoice = input()
count = 0
q1answer = "a"
if userchoice == q1answer:
    print ("correct")
    count += 1
    print (count)
else:
    print ("incorrect")

q2 = "what is 1 + 1? a.1, b.5, c.2"
print (q2)
userchoice = input()
q2answer = "c"
if userchoice == q2answer:
    print ("correct")
    count += 1
    print (count)
else:
    print ("incorrect")
    count-=1
    print (count)

q3 = "what is july 1? a.canada day, b.christmas, c.halloween"
print (q3)
userchoice = input()
q3answer = "a"
if userchoice == q3answer:
    print ("correct")
    count += 1
    print (count)
else:
    print ("incorrect")
    count-=1
    print (count)

q4 = "is tomato a fruit? a.True, b. False"
print (q4)
userchoice = input()
q4answer = "a"
if userchoice == q4answer:
    print ("correct")
    count += 1
    print (count)
else:
    print ("incorrect")
    count-=1
    print (count)



