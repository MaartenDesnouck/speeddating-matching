# SpeedDating

Installeer de [SMS Gateway API](https://play.google.com/store/apps/details?id=networked.solutions.sms.gateway.api) app vanuit de Play Store.   
Maak vervolgens een account aan op [https://smsgateway.me](https://smsgateway.me).   
Je voegt natuurlijk ook je gsmtoestel toe.   
Vergeet de waardes van **USERNAME**, **PASSWORD** en **DEVICE** niet in te vullen in app.py  

Het pythonprogramma maakt ook gebruik van **requests** om met smsgateway.me te kunnen praten dus moet je vooraf requests nog installeren:   
`pip install requests`   

Het programma neemt als input 2 bestanden:
- ##### deelnemers.csv   
   **Inhoud:** de deelnemers met hun nummer en telefoonnummer e.d   
**vb.** `Maarten,Desnouck,Man,Interesse,Kring,Jaar,E-mailadres,+32478182969,0`  
    Dit is eenvoudig aan te passen als je bestand er anders uitziet natuurlijk.   

	De separator moet een ',' zijn. Ook dit kan je makkelijk aanpassen als je wil.
	Let vooral op het telefoonnrformaat; +32 is het best omdat dit overal goed herkend wordt.

- ##### keuzes.csv   
	**Inhoud:** het nr en zijn/haar keuzes 	
    **vb.** `188,84,83,72,77,70` (nr 188 kiest 84,83,72,77 en 70)

	Om deze keuzes over te typen van de blaadjes werken we samen in een google spreadsheet, die kan je dan mooi naar csv exporteren.

Het programma laten lopen kan zeer eenvoudig met:   
`./app.py` of `python app.py`

-- Maarten Desnouck, 18 januari 2015   
