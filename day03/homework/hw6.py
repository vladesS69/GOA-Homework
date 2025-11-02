# ==  ->  ტოლია (შემოწმება, არის თუ არა ორი მნიშვნელობა ერთნაირი)
print(5 == 5)        # True
print(3 == 4)        # False
print('a' == 'a')    # True
print(10 == 10.0)    # True (რადგან მნიშვნელობა ტოლია)
print('dog' == 'cat')# False


# !=  ->  არ არის ტოლი (შემოწმება, განსხვავდება თუ არა მნიშვნელობები)
print(5 != 3)        # True
print(4 != 4)        # False
print('hi' != 'Hi')  # True (რადგან დიდობა განსხვავებულია)
print(True != False) # True
print(10 != 10.0)    # False


# >  ->  მეტია (პირველი მნიშვნელობა მეტია მეორეზე)
print(5 > 3)         # True
print(2 > 8)         # False
print(10 > 9.99)     # True
print(-1 > -2)       # True
print(100 > 100)     # False


# <  ->  ნაკლებია (პირველი მნიშვნელობა ნაკლებია მეორეზე)
print(3 < 5)         # True
print(7 < 2)         # False
print(9 < 9.1)       # True
print(-5 < 0)        # True
print(10 < 10)       # False


# >=  ->  მეტია ან ტოლია
print(5 >= 5)        # True
print(8 >= 6)        # True
print(4 >= 9)        # False
print(10 >= 10.0)    # True
print(-2 >= -3)      # True


# <=  ->  ნაკლებია ან ტოლია
print(5 <= 5)        # True
print(3 <= 7)        # True
print(9 <= 4)        # False
print(10 <= 10.0)    # True
print(-1 <= -1)      # True




# Logical operators (ლოგიკური ოპერატორები)
# გამოიყენება ორი ან მეტი პირობის შესადარებლად
# შედეგი ყოველთვის არის True ან False

# სამი ძირითადი ლოგიკური ოპერატორია:
#  and  -> აბრუნებს True-ს მხოლოდ მაშინ, როცა ორივე პირობა მართალია
#  or   -> აბრუნებს True-ს მაშინ, როცა სულ მცირე ერთი პირობა მართალია
#  not  -> აბრუნებს პირიქით მნიშვნელობას (True → False, False → True)

# --- მაგალითები ---

#  and ოპერატორი
print(True and True)     # True (ორივე პირობა მართალია)
print(True and False)    # False (მხოლოდ ერთი პირობაა მართალი)
print(False and True)    # False
print(False and False)   # False
print(5 > 3 and 2 < 4)   # True (ორივე შედარება მართალია)

#  or ოპერატორი
print(True or False)     # True (ერთი პირობა მაინც მართალია)
print(False or True)     # True
print(False or False)    # False (არაფერი არ არის მართალი)
print(10 > 5 or 1 > 9)   # True (პირველი პირობა მართალია)
print(3 == 2 or 2 == 2)  # True (მეორე პირობა მართალია)

#  not ოპერატორი
print(not True)          # False (აბრუნებს საპირისპიროს)
print(not False)         # True
print(not (5 > 3))       # False (რადგან 5 > 3 არის True, ხოლო not True → False)
print(not (2 == 4))      # True (რადგან 2 == 4 არის False)
print(not (True and False)) # True (რადგან True and False არის False → not False → True)



#  and ოპერატორი — აბრუნებს True მხოლოდ მაშინ, როცა ორივე პირობა მართალია
print(5 > 3 and 10 > 7)     # True (ორივე პირობა მართალია)
print(8 > 2 and 4 < 1)      # False (მეორე პირობა ცრუა)
print('a' == 'a' and 2 == 2)# True (ორივე პირობა მართალია)


#  or ოპერატორი — აბრუნებს True, თუ მინიმუმ ერთი პირობა მართალია
print(5 > 10 or 3 < 4)      # True (მეორე პირობა მართალია)
print(False or False)       # False (არც ერთი პირობა არ არის მართალი)
print(7 == 7 or 2 > 9)      # True (პირველი პირობა მართალია)


#  not ოპერატორი — აბრუნებს პირიქით მნიშვნელობას
print(not True)             # False (პირიქით აქცია)
print(not (5 < 3))          # True (რადგან 5 < 3 არის False → not False → True)
print(not (10 == 10))       # False (რადგან 10 == 10 არის True → not True → False)



num = int(input("შეიყვანე რიცხვი: "))
fixed_number = 10

if num > fixed_number:
    print("შეყვანილი რიცხვი მეტია 10-ზე.")
else:
    print("შეყვანილი რიცხვი არ არის მეტი 10-ზე.")



    age = int(input("შეიყვანე შენი ასაკი: "))

if age > 18:
    print("შენი ასაკი მეტია 18-ზე.")
else:
    print("შენი ასაკი 18-ზე ნაკლებია ან ტოლია.")