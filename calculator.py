while True :
 print("\n====Calculator====")
 print("\n1addition\n2.subraction\n3.multipication\n4.divison")
 ch=input("enter your choise:(1-4)")
 if ch=="1":
     a=int(input("enter first number:"))
     b=int(input("enter second number:"))
     print(a+b)
 elif ch=="2":
      a=int(input("enter first number:"))
      b=int(input("enter second number:"))
      print(a-b)
 elif ch=="3":
     a=int(input("enter first number:"))
     b=int(input("enter second number:"))
     print(a*b)      
 elif ch=="4":
     a=int(input("enter first number:"))
     b=int(input("enter second number:"))
     print(a/b)
 else:
      print("wrong choise slected!")       