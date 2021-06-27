from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()
    if user_message in ("hello","hi"):
        return "Hello! How may I help you ?"
    if user_message in ("thank you"):
        return "Your welcome "
    if user_message in ("How can we update offers?"):
        return "First click on entrepreneur in the home page.Next login with valid username and password.\n If you don't have an account then register.\n After login you will be redirected to Update page there you can fill the details and click submit.\nFinally you can update the offers of your particular shop.  "
    if user_message in ("How to know about the offers available in the city?"):
        return "First click on customer in the home page.\nNext login with valid username and password.\n If you don't have an account then register.\n After login you will be redirected to Offers pool page there you can fill the details and click submit.\nFinally you can view the offers "
    if user_message in ("thank you"):
        return "Your welcome "    
    if user_message in ("What all category offers can be viewed here?"):
        return "The different category offers present are\n 1.clothing\n 2.Footware\n3.Electrical\n4.Furniture\n5.Cell Phones\n6.Food\n7.Medicine\n8.Toys\n9.Stationary\n10.Jewellery"
    if user_message in ("timing","at what time shops are opened?"):
        return "From 9AM to 10PM"
    return "Sorry, I didn't get the question"                