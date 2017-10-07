#Age Verifier
a=int(input("Enter Your Age:"))
if(a>=18 and a<=50):
    print ("You Can Access The Server")
else:
    print("You Cannot Access The Server")
    raise SystemExit
#Email Verifier
p=(input("Enter Email:"))
if (p=="mohakchhabria@gmail.com"):
    print("Welcome Mohak")
elif (p=="mohakchhabriayt@gmail.com"):
     print("Welcome Mohak")
elif (p=="admin"):
     print("Welcome admin")
else:
     print("Wrong Email")
     raise SystemExit
#Password Verifier
p=(input("Enter Password .1 Tries Remaining.Enter 'forgotpassword' To Recover Your Account:"))
if p=="123456":
         print("Access Granted!!.Here Is The Link For Your Account-mohakchhabria@gmail.com:'www.linkredirect.com/mohakchhabria'")
         raise SystemExit
elif p=="00000":
    print("Access Granted!!.Here Is The Link For Your Account-mohakchhabriayt@gmail.com:'www.linkredirect.com/mohakchhabriayt'")
    raise SystemExit
elif p=="hellyeah":
    print("Access Granted With Administrative Privilages")
elif p=="forgotpassword":
    print("Go To This Link To Recover Your Account:  www.linkredirect.com/forgotpassword")
else:
    print("Wrong Password.Connection Terminated")
    raise SystemExit
