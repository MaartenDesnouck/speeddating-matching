# Speeddating Matching

Install the [SMS Gateway API](https://play.google.com/store/apps/details?id=networked.solutions.sms.gateway.api) app.<br>
Create an account on <https://smsgateway.me>.<br>
Add a phone to your account.<br>
Don't forget to fill in the values of **USERNAME**, **PASSWORD** and **DEVICE** in app.py

This app makes us of **requests** to communicate with smsgateway.me so you will need to install it by running:<br>
`pip install requests`

The app takes 2 files as input:

- ##### participants.csv

  **Content:** Details about each participant.<br>
  **e.g.** `Maarten,Desnouck,Man,Interesse,Association,Year,E-mailadres,+32478182969,0`<br>
  This is easily adaptable off course.

  We use a ',' as separator but this is easily adaptable. Pay attention to the phonenumber format; +12345678900 is best.

- ##### choices.csv

  **Inhoud:** Each id and his/her choices<br>
  **e.g.** `188,84,83,72,77,70` (id 188 likes 84,83,72,77 and 70)

  It is advised to use google sheets for putting in all the numbers from the paper slips, it allows for multiple people to work toghether putting all the choices and it allows you to export to csv very easily.

Run the application:<br>
`./app.py` or `python app.py`

-- Maarten Desnouck, 18 januari 2015
