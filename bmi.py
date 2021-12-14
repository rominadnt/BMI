w = int( input("vazn(kg) : "))
h = float( input("gad(m) : "))

bmi = ( w / (h*h) )
print("BMI:")
print(bmi)

status = ""
if bmi <= 18.5:
    status = "kambood vazn"
elif bmi < 24.9:
    status = "salem"   
elif bmi < 29.9:
    status = "ezafe vazn" 
else:
    status = "chagh"  

print(status)      
