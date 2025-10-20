a = 5
b = "3"

sum = a + int(b)
print(sum)



#პითონში “converter”-ი ძირითადად ნიშნავს მატერიალურ/ინფორმაციულ მნიშვნელობით მონაცემთა ტიპების (data types) კონვერტაციას — ანუ ერთ ტიპშია მოცემული მნიშვნელობა გადაყვანილი სხვა ტიპში.



num1 = float(input("4.5 "))
num2 = float(input("3.2 "))

# მათი ჯამი
sum = num1 + num2

# შედეგის გამოტანა ეკრანზე
print("7.7", sum)



# მომხმარებლისგან ორი მთელი რიცხვის მიღება
num1 = int(input("4 "))
num2 = int(input("8 "))

# შემოწმება, ორივე რიცხვი ლუწია თუ არა
if num1 % 2 == 0 and num2 % 2 == 0:
    sum = num1 + num2
    print("12", sum)
else:
    print("The given numbers are not even so they will not be summed")



my_name = "saba" 
print("saba")
age = 16
print("16")
city = "tbilisi"
print("tbilisi")
height = 1.75
print("1.75")
country = "georgia"
print("georgia")


a = 10
b = 7

print(a > b)    # True
print(a < b)    # False
print(a == b)   # False



# მომხმარებლისგან ორი რიცხვის მიღება
num1 = float(input("10"))
num2 = float(input("5"))

# ყველა მათემატიკური ოპერაცია
print("15 (+):", num1 + num2)
print("5 (-):", num1 - num2)
print("50 (*):", num1 * num2)

# გაყოფისას ვამოწმებთ ნულზე გაყოფას
if num2 != 0:
    print("2 (/):", num1 / num2)
else:
    print("ნულზე გაყოფა შეუძლებელია!")


# ჩემი სახელი შევინახოთ ცვლადში
my_name = "Saba"

# მომხმარებლისგან სახელის მიღება
user_name = input("Giorgi ")

# შევამოწმოთ ემთხვევა თუ არა
if user_name == my_name:
    print("We have the same name")
else:
    print("Our names do not match")



    first_name = "Saba"
last_name = "Valishivli"
full_name = first_name + " " + last_name
print(full_name)  # → Saba Valishivli







number = 10 


if number % 5 == 0: 
     print("The number is even")
else:
    print("The number is odd")

    




#done


