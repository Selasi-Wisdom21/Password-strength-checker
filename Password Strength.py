import re
print("Password Strength checker")
user_password = input("Enter your password: ")
print (user_password)
def password_strength(user_password):
 score = 0
 length = len(user_password)
    

 if  8 <= length <=10:
    score += 1
 elif 11 <= length <= 15:
    score += 2
 elif length >= 16:
    score += 3

 if re.search(r"(?=.*[A-Z]).*",user_password):
      score += 1
 if re.search(r"(?=.*[0-9]).*",user_password):
      score += 1
 if re.search(r"(?=.*[a-z]).*",user_password):
       score += 1 
 if re.search(r"(?=.*[!@#$%^&]).*",user_password):
       score += 1 
 return score


final_score = password_strength(user_password)
print(f"Password strength score: {final_score}/7")
if final_score <= 2:
     print("Strength: Weak ")
elif final_score <= 4:
     print("Strength: Medium")
elif final_score > 5:
     print("Strength: Strong")
print("A STRONG PASSWORD SHOULD BE AT LEAST 10 CHARACTERS LONG AND CONTAIN UPPERCASE, LOWERCASE, SPECIAL CHARACTERS AND NUMBERS")