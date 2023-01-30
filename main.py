
import os
import hashlib
import string
import base64
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
import pyperclip

class MainApp(MDApp):
    def build(self):
        self.screen = Screen()
        self.generate_password_screen()
        return self.screen

    def generate_password_screen(self):
        self.screen.clear_widgets()
        if os.path.exists("key_part.txt"):
            with open('key_part.txt', 'r') as f:
                self.text_field = f.read()
            self.input_string = MDTextField(hint_text="Enter input string here", pos_hint={"center_x": 0.5, "center_y": 0.7}, size_hint=(0.6,1))
            self.output_length = MDTextField(hint_text="Enter output length here", pos_hint={"center_x": 0.5, "center_y": 0.6},size_hint=(0.6,1))
            self.generate_button = MDRectangleFlatButton(text="Generate", pos_hint={"center_x": 0.5, "center_y": 0.3},
                                                         on_press=self.generate_password)

            self.password = MDRectangleFlatButton(text="", font_style="H4", pos_hint={"center_x": 0.5, "center_y": 0.4},)
            self.screen.add_widget(MDRectangleFlatButton(text="Password Generation", font_style="H4",
                                           pos_hint={"center_x": 0.5, "center_y": 0.9}))
            self.screen.add_widget(self.input_string)
            self.screen.add_widget(self.output_length)
            self.screen.add_widget(self.generate_button)
            self.screen.add_widget(self.password)


        else:
            self.text_field = MDTextField(hint_text="Enter string here", pos_hint={"center_x": 0.5, "center_y": 0.7}, size_hint=(0.6,1))
            self.submit_button = MDRectangleFlatButton(text="Submit", pos_hint={"center_x": 0.5, "center_y": 0.5},
                                                       on_press=self.submit)
            self.screen.add_widget(self.text_field)
            self.screen.add_widget(self.submit_button)
    def submit(self, obj):
        with open("key_part.txt", "w") as file:
            file.write(self.text_field.text)
        self.generate_password_screen()

    def generate_password(self, instance):
        input_string = self.input_string.text
        output_length = int(self.output_length.text)
        input_string += str(output_length)
        input_string +=str(self.text_field)
        sha = hashlib.sha256()
        sha.update(input_string.encode())
        hash_bytes = sha.digest()
        hash_base64 = base64.b64encode(hash_bytes)
        hash_base64 = hash_base64.decode()
        hash_filtered = ''.join(c for c in hash_base64 if c in (string.ascii_letters + string.digits))
        hash_filtered = hash_filtered[:output_length]
        hashed_string = '-'.join(hash_filtered[i:i+4] for i in range(0, len(hash_filtered), 4))
        self.password.text = hashed_string
        pyperclip.copy(hashed_string)




MainApp().run()
