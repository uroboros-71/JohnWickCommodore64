from asciimatics.widgets import Frame, Layout, Button, PopUpDialog, Label, Divider
from asciimatics.exceptions import StopApplication, NextScene
import datetime

class MainMenuView(Frame):
    def __init__(self, screen, model):
        super(MainMenuView, self).__init__(screen,
                                          screen.height,
                                          screen.width,
                                          has_border=True,
                                          hover_focus=False,
                                          can_scroll=False,
                                          has_shadow=False,
                                          reduce_cpu=True)
        # Theme
        self.set_theme("green")

        # Save off the model that accesses the contacts database.
        self._model = model

        # Create the form for displaying the list of contacts.
        layout = Layout([1,1,1], fill_frame=True, gutter=-5)
        self.add_layout(layout)
        layout.add_widget(Divider(height=3, draw_line=False), 0)
        layout.add_widget(Divider(height=3, draw_line=False), 2)
        layout.add_widget(Button("MEMBER", self._member, align=">"), 0)
        layout.add_widget(Button("SANCTUARY", self._dummy, align="<"), 2)
        layout.add_widget(Divider(height=2, draw_line=False), 0)
        layout.add_widget(Divider(height=2, draw_line=False), 2)
        layout.add_widget(Button("ACCOUNT", self._account, align=">"), 0)
        layout.add_widget(Button("THE HIGH TABLE", self._dummy, align="<"), 2)
        layout.add_widget(Divider(height=13, draw_line=False), 1)
        layout.add_widget(Button("QUIT", self._quit, align="^"), 1)
        layout.add_widget(Divider(draw_line=False, height=3),1)

        layout2 = Layout([100])
        self.add_layout(layout2)
        layout2.add_widget(Label(datetime.datetime.now().strftime("%H:%M %p"), 1, align="^", name="currenttime"))
        layout2.add_widget(Divider(draw_line=False))

        self.fix()

    def update(self, frame_no):
        # Update Current Time
        dt = self._layouts[1].find_widget("currenttime")
        dt.text = datetime.datetime.now().strftime("%H:%M  %p")
        super().update(frame_no)

    def _member(self):
        self._model.current_id = None
        raise NextScene("Member List")

    def _account(self):
        self._model.current_id = None
        raise NextScene("Account List")

    def _quit(self):
        self._scene.add_effect(
            PopUpDialog(self._screen,
                        "Are you sure?",
                        ["Yes", "No"],
                        has_shadow=True,
                        on_close=self._quit_on_yes,
                        theme="green"))

    def _dummy(self):
        pass

    @staticmethod
    def _quit_on_yes(selected):
        # Yes is the first button
        if selected == 0:
            raise StopApplication("User requested exit")
