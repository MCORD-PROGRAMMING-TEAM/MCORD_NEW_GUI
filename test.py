import notify2

def sendmessage(title, message):
    notify2.init("Test")
    notice = notify2.Notification(title, message)
    notice.show()
    return



sendmessage("Testowa wiadomość", "Kurwy pole moje jest ")