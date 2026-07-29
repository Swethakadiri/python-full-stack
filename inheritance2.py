
#multilevel inheritance
class Ani:
    def __init__(self, animal):
        print("Animal eats food")
class Ani1(Ani):
    def __init__(self, animal, bird):
        super().__init__(animal)
        print("Bird  can fly")
class Ani3(Ani1):
    def __init__(self, animal, bird, parrot):
        super().__init__(animal, bird)
        print("Parrot can speak")
s = Ani3("eat", "fly", "beautiful")
print("Animal:", s.animal)
print("Bird:", s.bird)
print("Parrot:", s.parrot)





#inheritance
class Camera:
    def __init__(self, camera):
        self.camera = camera
        print("Taking photo")

class MusicPlayer(Camera):
    def __init__(self, camera, musicplayer):
        super().__init__(camera)
        self.musicplayer = musicplayer
        print("Playing music")

class Smartphone(MusicPlayer):
    def __init__(self, camera, musicplayer, smartphone):
        super().__init__(camera, musicplayer)
        self.smartphone = smartphone
        print("Calling")

s = Smartphone("Canon", "Spotify", "Samsung")

print("Camera:", s.camera)
print("Music Player:", s.musicplayer)
print("Smartphone:", s.smartphone)








#example
class name:
    def __init__(self):
        self.name=name
class marks(name):
    def __init__(self,name,marks):
        super(). __init__(name)
        self.marks=marks
s1=marks("ravi","92")
print(s1.name)
print(s1.marks)

