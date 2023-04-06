# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flet import *
import datetime

def main(page: Page):
 BG = '#041955'
 page_2 = Row()
 page_2 = Row()
 FWG = '#97b4ff'
 FG = '#3450a1'
 PINK = '#eb06ff'
 messstationenZahl = {
  "Ochsenhausen": "4",
  "Schwendi": "0",
  "Biberach": "0"
 }
 Warnungen = {
  "Ochsenhausen": "keine Warnung",
  "Schwendi": "keine Warnung",
  "Biberach": "keine Warnung"
 }



 user = 'bob'
 messorte_card = Row(
  scroll='auto'
 )
 messorte = ['Ochsenhausen','Schwendi','Biberach']
 for messort in messorte:
  messorte_card.controls.append(
   Container(
    bgcolor=BG,
    border_radius=20,
    height=110,
    width=170,
    padding=20,
    content=Column(
     controls=[
      Text(messort,size=18),
      Text("Messstationen: " + messstationenZahl[messort]),
      Text(Warnungen[messort],color="green600")
     ]
    )
   )
  )


 first_page_contents = Container(
  content=Column(
   controls=[
    Row(alignment='spaceBetween',
     controls=[
      Container(
       content=Icon(
        icons.MENU
       )
      ),
      Row(
       controls=[
        Icon(icons.SEARCH),
        Icon(icons.NOTIFICATIONS_OUTLINED)
       ]
      )
     ]
    ),
    Container(height=20),
    Text(
     value='Hallo ' + user, size=15,
    ),
    Text(
     value="heute ist der " +str(datetime.date.today())
  ),
    Container(
     padding=padding.only(top=10,bottom=20,),
     content=messorte_card
    )
   ]
  )
 )

 page_1 = Container()
 page_2 = Row(
  controls=[
   Container(
    width=400,
    height=850,
    bgcolor=FG,
    border_radius=35,
    padding=padding.only(
     top=50,left=20,
     right=20,bottom=5
    ),
    content=Column(
     controls=[
      first_page_contents
     ]
    )
   )
  ]
 )


 container = Container(
  width=500,
  height=500,
  bgcolor=BG,
  border_radius=35,
  content=Stack(
   controls=[
    page_1,
    page_2
   ]
  )
 )
 page.add(container)



app(target=main)
# app(target=main,view=WEB_BROWSER)