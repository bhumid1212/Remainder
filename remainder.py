import time
from plyer import notification

if __name__ == "__main__":
    notification.notify(
       title = "please drink water",
       message = "water is very beneficial for your health, you should drink at least 3 litre of water everyday.",
        app_icon = "D:\Python\PythonPracticeProgram\icon.ico",
        timeout = 5 
    )