import pygame, sys

class Button:
	def __init__(self,text,width,height,pos,elevation):
		#Core attributes 
		self.pressed = False
		self.elevation = elevation
		self.dynamic_elecation = elevation
		self.original_y_pos = pos[1]

		# top rectangle 
		self.top_rect = pygame.Rect(pos,(width,height))
		self.top_color = '#475F77'

		# bottom rectangle 
		self.bottom_rect = pygame.Rect(pos,(width,height))
		self.bottom_color = '#354B5E'
		#text
		self.text_surf = gui_font.render(text,True,'#FFFFFF')
		self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

	def draw(self):
		# elevation logic 
		self.top_rect.y = self.original_y_pos - self.dynamic_elecation
		self.text_rect.center = self.top_rect.center 

		self.bottom_rect.midtop = self.top_rect.midtop
		self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

		pygame.draw.rect(screen,self.bottom_color, self.bottom_rect,border_radius = 12)
		pygame.draw.rect(screen,self.top_color, self.top_rect,border_radius = 12)
		screen.blit(self.text_surf, self.text_rect)
		self.check_click()

	def check_click(self):
		mouse_pos = pygame.mouse.get_pos()
		if self.top_rect.collidepoint(mouse_pos):
			self.top_color = '#D74B4B'
			if pygame.mouse.get_pressed()[0]:
				self.dynamic_elecation = 0
				self.pressed = True
			else:
				self.dynamic_elecation = self.elevation
				if self.pressed == True:
					print('click')
					self.pressed = False
		else:
			self.dynamic_elecation = self.elevation
			self.top_color = '#475F77'

pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('Gui Menu')
clock = pygame.time.Clock()
gui_font = pygame.font.Font(None,30)

button1 = Button('Click me',200,40,(200,250),5)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	screen.fill('#DCDDD8')
	button1.draw()

	pygame.display.update()
	clock.tick(60)