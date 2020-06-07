import pyautogui
from PIL import Image, ImageGrab
import time

def hit(key):
	pyautogui.keyDown(key)

# def draw():
def isCollide(data):
	for i in range(220, 225):
		for j in range(330, 395):
			if data[i, j] < 100:
				hit("down")
				return True


	for i in range(235, 290):
		for j in range(420, 440):
			if data[i, j] < 100:
				hit("up")
				return True
	return False



if __name__ == "__main__":
	print("Hey ...Dino start at 3 sec")
	time.sleep(3)

	while True:
		image = ImageGrab.grab().convert('L')
		data = image.load()
		isCollide(data)
		
		# Draw a rectangle for cactus
'''
		for i in range(230, 300):
			for j in range(420, 440):
				data[i, j] = 0

	# 	# Draw a rectangle for birds

		for i in range(220, 225):
			for j in range(330, 395):
				data[i, j] = 171

		image.show()
		break
	# 
'''