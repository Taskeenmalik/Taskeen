import pyqrcode
print('Enter text: ')
text=input()
profile = pyqrcode.create(text)
profile.png('profile.png', scale=6)
