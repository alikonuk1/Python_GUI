from guizero import App, Combo, CheckBox, ButtonGroup, PushButton, info, Text

app = App(title="My second GUI app", width=300, height=200, layout="grid")

def do_booking():
    info("Booking", "Thank you for booking")
    print( film_choice.get() )
    print( vip_seat.get_value() )
    print( row_choice.get() )

book_seats = PushButton(app, command=do_booking, text="Book seat", grid=[1,2], align="left")

film_description = Text(app, text="Which film?", grid=[0,0], align="left")

film_choice = Combo(app, options=["Star Wars", "Indiana Jones", "Batman"], grid=[0,1], align="left")

vip_seat = CheckBox(app, text="VIP seat?", grid=[0,2], align="left")

row_choice = ButtonGroup(app, options=[ ["Front", "F"], ["Middle", "M"],["Back", "B"] ], selected="M", horizontal=True, grid=[1,1], align="left")


app.display()















