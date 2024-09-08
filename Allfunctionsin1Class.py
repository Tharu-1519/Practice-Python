class allfunctions:
    def subfields():
        subfields=[
            'Machine Learning',
            'Neural Netword',
            'Vision',
            'Robotics',
            'Speech Processing',
            'Natural Language Processing']
        print("Sub-fields in AI are:")
        for fields in subfields:
            print(fields)
            
     def oddeven():
        number=int(input("Enter a number:"))
        if(number%2 ==0):
            print(f"{number} is Even")
        else:
            print(f"{number} is Odd")

    def Eligiblityformarriage():
        Gender=input("Your Gender:")
        Age=int(input("your age:"))
        if((Gender=="Male" and Age>21) or (Gender=="Female" and Age >18)):
            message="Eligible"
        else:
            message="Not Eligible"
        return message

    def Calculate():
        sub1=int(input("Subject1:"))
        sub2=int(input("Subject2:"))
        sub3=int(input("Subject3:"))
        sub4=int(input("Subject4:"))
        sub5=int(input("Subject5:"))
        Total=(sub1+sub2+sub3+sub4+sub5)
        print("Total:",Total)
        Percentage=float(Total/5)
        print("Percentage:",Percentage)

    def triangle():
        Height=int(input("Height:"))
        Breadth=int(input("Breadth:"))
        Area=(Height*Breadth)/2
        print("Area Formula: Area=(Height*Breadth)/2")
        print("Area of Triangle:", Area)
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breadth=int(input("Breadth:"))
        Perimeter=Height1+Height2+Breadth
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle:",Perimeter)