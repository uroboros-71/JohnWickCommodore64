from asciimatics.widgets import Frame, ListBox, Layout, Divider, Label, Button, Text, TextBox
from asciimatics.exceptions import NextScene
import datetime


class MemberListView(Frame):
    def __init__(self, screen, model):
        super(MemberListView, self).__init__(screen,
                                        screen.height,
                                        screen.width,
                                        on_load=self._reload_list,
                                        title="Member List",
                                        has_border=True,
                                        hover_focus=True,
                                        can_scroll=False,
                                        edit_account=True,
                                        border_end_y=5,
                                        reduce_cpu=False)
        # Theme
        self.set_theme("green")

        # Save off the model that accesses the contacts database.
        self._model = model

        # Create the form for displaying the list of contacts.
        self._list_view = ListBox(
            18,
            model.get_member_summary(),
            name="member",
            add_scroll_bar=True,
            on_select=self._edit)
        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(self._list_view)
        #layout.add_widget(Divider())
        layout2 = Layout([1, 1, 1])
        self.add_layout(layout2)
        layout2.add_widget(Button("ADD", self._add), 0)
        layout2.add_widget(Button("CANSEL", self._quit), 2)
        layout2.add_widget(Divider(height=2, draw_line=False), 1)
        layout2.add_widget(Label(datetime.datetime.now().strftime("%H:%M %p"), 1, align="^", name="currenttime"), 1)
        self.fix()

    def _reload_list(self, new_value=None):
        self._list_view.options = self._model.get_member_summary()
        self._list_view.value = new_value

    def update(self, frame_no):
        # Update Current Time
        dt = self._layouts[1].find_widget("currenttime")
        dt.text = datetime.datetime.now().strftime("%H:%M  %p")
        super().update(frame_no)

    def _add(self):
        self._model.current_id = None
        raise NextScene("Edit Member")

    def _edit(self):
        self.save()
        self._model.current_id = self.data["member"]
        raise NextScene("Edit Member")

    @staticmethod
    def _quit():
        raise NextScene("Main")

class MemberView(Frame):
    def __init__(self, screen, model):
        super(MemberView, self).__init__(screen,
                                        screen.height,
                                        screen.width,
                                        has_border=True,
                                        hover_focus=True,
                                        edit_account=True,
                                        can_scroll=False,
                                        border_start_x=2,
                                        border_end_y=4,
                                        reduce_cpu=False)
        # Theme
        self.set_theme("green")

        # Save off the model that accesses the contacts database.
        self._model = model

        # Create the form for displaying the list of contacts.
        layout = Layout([100], fill_frame=True, offset_max=True)
        self.add_layout(layout)
        layout.add_widget(Label("CATEGORY                   INFORMATION"))
        layout.add_widget(Divider(draw_line=True))
        layout.add_widget(Text("MEMBERCODE", "membercode"))
        layout.add_widget(Divider(draw_line=False), 0)
        layout.add_widget(Text("NAME", "name"))
        layout.add_widget(Divider(draw_line=False), 0)
        layout.add_widget(Text("NUMBER", "phone"))
        layout.add_widget(Divider(draw_line=False), 0)
        layout.add_widget(Text("BANK NAME", "bankname"))
        layout.add_widget(Divider(draw_line=False), 0)
        layout.add_widget(Text("BANK ACCOUNT ", "bankaccount"))
        layout.add_widget(Divider(draw_line=False), 0)
        layout.add_widget(TextBox(4, "NOTES", "notes", as_string=True, line_wrap=True, button_offset=-1))
        layout.add_widget(Divider(draw_line=False), 0)
        layout.add_widget(Text("STATUS", "status"))
        layout.add_widget(Divider(draw_line=False), 0)
        layout2 = Layout([1, 1, 1], fill_frame=False)
        self.add_layout(layout2)
        layout2.add_widget(Divider(height=2, draw_line=False), 0)
        layout2.add_widget(Divider(height=3, draw_line=False), 1)
        layout2.add_widget(Divider(height=2, draw_line=False), 2)
        layout2.add_widget(Button("OK", self._ok), 0)
        layout2.add_widget(Button("CANCEL", self._cancel), 2)
        layout2.add_widget(Label(datetime.datetime.now().strftime("%H:%M %p"), 1, align="^", name="currenttime"), 1)

        screen.refresh()
        self.fix()

    def update(self, frame_no):
        # Update Current Time
        dt = self._layouts[1].find_widget("currenttime")
        dt.text = datetime.datetime.now().strftime("%H:%M  %p")
        super().update(frame_no)

    def reset(self):
        super(MemberView, self).reset()
        self.data = self._model.get_current_member()

    def _ok(self):
        self.save()
        self._model.update_current_member(self.data)
        raise NextScene("Member List")

    @staticmethod
    def _cancel():
        raise NextScene("Member List")
