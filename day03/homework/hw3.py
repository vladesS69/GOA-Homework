#Debugging ნიშნავს შეცდომების პოვნასა და გამოსწორებას პროგრამაში.
#როდესაც პროგრამა არ მუშაობს ისე, როგორც ველით — ანუ გამოყოფს error-ს (შეცდომას) ან არასწორ შედეგს, ჩვენ ვიწყებთ მის “დებაგინგს”.
#სხვა სიტყვებით, debugging არის პროცესი, როდესაც ვცდილობთ გავიგოთ:

#რატომ არ მუშაობს კოდი სწორად,

#სად მოხდა შეცდომა,

#და როგორ უნდა გამოვასწოროთ ის.

#რისთვის ვიყენებთ Debugging-ს

#Debugging დაგვეხმარება:

#შევამჩნიოთ შეცდომები (syntax errors, logical errors და სხვ.)

#გავიგოთ პროგრამის მუშაობის ლოგიკა

#გავაუმჯობესოთ კოდი — უფრო სწორი და სტაბილური გავხადოთ

#დავზოგოთ დრო მომავალში, რადგან ვიცით როგორ ვიპოვოთ და გამოვასწოროთ შეცდომები


my_name = "Saba"
print(my_name)



x = 5.5
y = 10
z = x + y
print(z)


x = 6.7
y = 15
z = x + y
print(z)


x= 10.5 
y = 20
z = x + y
print(z)


x = 24.4
y = 231
z = x * y
print(z)



age = 15
print(age+5)






my_name = "Saba"
print(my_name)
age = 16
print(age)
city = "Tbilisi"
print(city)
height = 1.75
print(height)



total = 100
print(total)

#აქ გამოიტანს 100


total = 120
print(total)

people = 4
print(people)


amount_per_person = total / people  
print(amount_per_person)


price = 50
discount = 0.5 
print(price - discount)


#if else statement გამოიყენება იმისთვის, რომ პროგრამამ შეასრულოს გარკვეული მოქმედება მხოლოდ მაშინ, როცა პირობა ჭეშმარიტია (True).
#თუ პირობა არ არის ჭეშმარიტი (False) — მაშინ პროგრამა შეასრულებს else ბლოკში მოცემულ კოდს.



# ცვლადის შექმნა
number = 7

# ვამოწმებთ არის თუ არა რიცხვი ლუწი
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

#done


