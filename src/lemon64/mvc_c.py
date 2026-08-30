from lemon64.mvc_m import Model

class Controller:
	
	def __init__(self):
		pass

	def call_notify(self, app, text):
		#演示 controller 修改资料 model
		#更新画面并非 controller工作
		app.notify(f"{text}")
