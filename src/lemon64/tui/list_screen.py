from textual import events
from textual.app import ComposeResult
from textual.screen import Screen
from textual.containers import Horizontal, Vertical, VerticalScroll, HorizontalScroll
from textual.widgets import Header, Footer, Static, Label, Button, Input, Rule, Switch
from textual.reactive import reactive
from lemon64.tui.messages import PersonStaticClicked

class PersonStatic(Static):
	def __init__(self, text:str, **kwargs):
		super().__init__(**kwargs)
		self.person_name = text

	def compose(self) -> ComposeResult:
		yield Label(self.person_name)
		yield Label("人格")

	def on_click(self, event:events.Click):
		self.post_message(PersonStaticClicked(self.person_name))

class XxxvStatic(Static):
	def __init__(self, text:str, **kwargs):
		super().__init__(**kwargs)
		self.xxxv_name = text

	def compose(self) -> ComposeResult:
		with Horizontal():
			yield Label("-", classes="bdem-xxxv-symbol")
			yield Label("阳爻", classes="bdem-xxxv-text")
			with Vertical(classes="xxxv-switch-panel"):
				yield Label(self.xxxv_name, classes="xxxv-switch-label")
				yield Switch(classes="xxxv-switch")
			yield Label("阴爻", classes="bayt-xxxv-text")
			yield Label("--", classes="bayt-xxxv-symbol")

class ListScreen(Screen):
	TITLE = "lemon64"
	SUB_TITLE = "list"
	CSS_PATH = "list_screen.tcss"

	def get_app_controller(self):
		return self.app.controller

	def on_mount(self):
		myself_name_static = self.query_one("#myself", PersonStatic)
		persno_name_label = self.query_one("#person-name-label", Label)
		persno_name_label.update(myself_name_static.person_name)
		pass #TODO 以上须修改为从model读取myself资料并显示
		
	def compose(self) -> ComposeResult:
		self.add_class("list-screen")
		yield Header()
		yield Footer()
		with Horizontal():
			yield HorizontalScroll(
				VerticalScroll(
					PersonStatic("本人", id="myself", classes="someone"),
					Rule.horizontal(),
					PersonStatic("他人1", classes="someone"),
					PersonStatic("他人2", classes="someone"),
					PersonStatic("他人3", classes="someone"),
					PersonStatic("他人4", classes="someone"),
					PersonStatic("他人5", classes="someone"),
					classes="left-panel"
				),
				Rule.vertical(),
				VerticalScroll(
					Label("person name", id="person-name-label"),
					XxxvStatic("上爻", classes="xxxv-static"),
					XxxvStatic("五爻", classes="xxxv-static"),
					XxxvStatic("四爻", classes="xxxv-static"),
					XxxvStatic("三爻", classes="xxxv-static"),
					XxxvStatic("二爻", classes="xxxv-static"),
					XxxvStatic("初爻", classes="xxxv-static"),
					Button("发布到地图", variant="primary", classes="publish-to-map"),
					classes="right-panel"
				)
			)

	def on_person_static_clicked(self, msg: PersonStaticClicked):
		persno_name_label = self.screen.query_one("#person-name-label", Label)
		persno_name_label.update(msg.person_name)
		self.get_app_controller().call_notify(self.app, f"mvc_c loads {msg.person_name}")
