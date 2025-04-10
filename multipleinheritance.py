class Employee:
    def __init__(self,name):
        self.name = name

    def showinfo(self):
        return f"The name of Employee is {self.name}"
    
    def __str__(self):
        return f"{self.name}"
    

class Dancer:
    def __init__(self,dance):
        self.dance = dance

    def showinfo(self):
        return f"The name of dance is {self.dance}"
    
    def __str__(self):
        return f"{self.dance}"
    

class DancerEmployee(Employee,Dancer):
    def __init__(self,dance,name):
        self.dance = dance
        self.name = name

    def showinfo(self):
        return super().showinfo()
    
    def __str__(self):
        return super().__str__()
    
a = DancerEmployee("Bhangda","Nitesh")

print(DancerEmployee.mro())

print(a)
print(a.showinfo())


# ✅ Requirements:
# Create a base class WiFiEnabled:
# Method: connect_to_wifi(ssid) → prints: "Connected to {ssid}"
# Create another base class VoiceControlEnabled:
# Method: voice_command(command) → prints: "Executing voice command: {command}"
# Now create a class SmartSpeaker that inherits from both WiFiEnabled and VoiceControlEnabled.
# Add a method play_music() in SmartSpeaker that prints: "Playing music..."


class WifiEnabled:
    def __init__(self,ssid):
        self.ssid = ssid

    def connect_to_wifi(self):
        return f"Connected to {self.ssid}"
    
class VoiceControlEnabled:
    def __init__(self,command):
        self.command = command

    def voice_command(self):
        return f"Executing voice command: {self.command}"
    
class SmartSpeaker(WifiEnabled,VoiceControlEnabled):
    def __init__(self,ssid,command):
        self.ssid = ssid  
        self.command = command 

    def play_music(self):
        print(super().connect_to_wifi())
        print(super().voice_command())
        return f"Playing music...."

a = WifiEnabled("Home Network")
a.connect_to_wifi()

b = VoiceControlEnabled("Play Playlist")
b.voice_command()

c = SmartSpeaker("Home Network","Play Playlist")
print(c.play_music())
