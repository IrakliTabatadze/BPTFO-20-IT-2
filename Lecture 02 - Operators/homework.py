

# txt = input("Please input some text: ")
#
# if 'small' in txt:
#     print('small')
# elif 'tall' in txt:
#     print('tall')
# elif 'middle' in txt:
#     print('middle')
# else:
#     print('words not exists in txt')




# text=input(str("Enter text: "))
#
# found = False

# print(text.lower())
# print(text.upper())

# if "small" in text:
#     found = True
#     print ("small")
#
# if "tall" in text:
#     found = True
#     print ("tall")
#
# if "middle" in text:
#     found = True
#     print ("middle")
#
# if not found:
#     print("No such words as 'small', 'tall' or 'middle' were found in the text." )


num1 = int(input("ჩაწერე პირველი რიცხვი: "))
num2 = int(input("ჩაწერე მეორე რიცხვი: "))
action = input ("ჩაწერე მათემატიკური ოპერატორი: ")
if '+' in action:
    print (num1 + num2)
elif '-' in action:
    print (num1 - num2)
elif "გამრავლება" in action:
    print (num1 * num2)
elif "ახარისხება" in action:
    print (num1 ** num2)
elif '/' in action:
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        print (num1 / num2)
elif "ნაშთი" in action:
    print (num1 % num2)
else:
    print ("მათემატიკური ოპერატორი არ მოიძებნა. აუცილებლად უნდა აირჩიო შემდეგი მათეამატიკურ ოპერატორებიდან ერთ-ერთი: მიმატება, გამოკლება, გამრავლება, გაყოფა, ახარისხება, უნაშთოდ გაყოფა ან ნაშთი")










# text = input("Enter the text to find if it contains words: small, middle, tall: ")
# word ="small"
# word1 ="middle"
# word2 ="tall"
#
# word_bool = False
# word1_bool = False
# word2_bool = False
#
# if word in text and word1 in text and word2 in text:
#     print("Small, middle, as well as tall, are in the text.")
# elif word in text and word1 in text:
#     print("Small and middle are in the text.")
# elif word in text and word2 in text:
#     print("Small and tall are in the text.")
# elif word1 in text and word2 in text:
#     print("Middle and tall are in the text.")
# elif word in text:
#     print("Small is indeed in the text.")
# elif word1 in text:
#     print("Middle is indeed in the text.")
# elif word2 in text:
#     print("Tall is indeed in the text.")
# else:
#     print("None of the words were found.")


