from guizero import App, Text, TextBox, PushButton, Slider

def say_my_text():
    welcome_message.set( my_text.get() )
    
def change_text_size(slider_value):
    welcome_message.font_size(slider_value)    

app = App(title="Test App")

welcome_message = Text(app, text="Test Message.", size=40, font="Times New Roman", color="lightblue")

my_text = TextBox(app, width=10)

update_text = PushButton(app, command=say_my_text, text="Display my text")

text_size = Slider(app, command=change_text_size, start=10, end=80)

app.display()

