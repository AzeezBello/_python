# import library 
import math, random 
  
# function to generate OTP 
def generateOTP() : 
  
    # Declare a digits variable   
    # which stores all digits  
    digits = "0123456789"
    OTP = "" 
  
   # length of password can be chaged 
   # by changing value in range 
    for i in range(4) : 
        OTP += digits[math.floor(random.random() * 10)] 
  
    return OTP 
  
# Driver code 
if __name__ == "__main__" : 
      
    print("OTP of 4 digits:", generateOTP()) 



  
# # function to generate OTP 
# def generateOTP() : 
  
#     # Declare a string variable   
#     # which stores all string  
#     string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     OTP = "" 
#     length = len(string) 
#     for i in range(6) : 
#         OTP += string[math.floor(random.random() * length)] 
  
#     return OTP 
  
# # Driver code 
# if __name__ == "__main__" : 
      
#     print("OTP of length 6:", generateOTP()) 