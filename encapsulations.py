class  Car:
    def __init__(self, speed, color):

        self.__speed = speed
        self.__color = color

    def set_speed(self, value):
        self.speed =value

    def get_speed(self):
        return self.speed

    def get_color(self):
        return self.__color


toyota = Car(200, 'red')
honda = Car(250, 'blue')
nissan = Car(300, 'black')

toyota.set_speed(300)
print(toyota.get_speed())
print(toyota.get_color())


'''

toyota.set_speed(350)
toyota.set__speed(500)
toyota.set_speed(450)

#toyota.speed = 500
#nissan.speed = 'four hundred'

#print(toyota.speed)


print(toyota.get_speed())
print(honda.color)
print(nissan.get_color())

'''
