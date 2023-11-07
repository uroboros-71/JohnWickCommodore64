from asciimatics.widgets import Frame, ListBox, Layout, Divider, Label, Button, Text, TextBox
from asciimatics.exceptions import NextScene
from asciimatics.screen import Screen
from asciimatics.event import KeyboardEvent
from accountdialog import AccountPopUpDialog
import datetime
import pickle


class AccountListView(Frame):
    def __init__(self, screen, model):
        super(AccountListView, self).__init__(screen,
                                        screen.height,
                                        screen.width,
                                        on_load=self._reload_list,
                                        title="Account List",
                                        has_border=True,
                                        hover_focus=True,
                                        edit_account=True,
                                        border_end_y=5,
                                        can_scroll=False,
                                        reduce_cpu=False)
        # Theme
        self.set_theme("green")

        # Save off the model that accesses the contacts database.
        self._model = model

        # Create the form for displaying the list of contacts.
        self._list_view = ListBox(
            18,
            model.get_member_summary(),
            name="account",
            add_scroll_bar=True,
            on_select=self._edit)
        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(self._list_view)
        layout2 = Layout([1, 1, 1])
        self.add_layout(layout2)
        layout2.add_widget(Button("ADD", self._input_account_no), 0)
        layout2.add_widget(Button("CANSEL", self._quit), 2)
        layout2.add_widget(Divider(height=2, draw_line=False), 1)
        layout2.add_widget(Label(datetime.datetime.now().strftime("%H:%M %p"), 1, align="^", name="currenttime"), 1)
        self.fix()

    def update(self, frame_no):
        dt = self._layouts[1].find_widget("currenttime")
        dt.text = datetime.datetime.now().strftime("%H:%M  %p")
        super().update(frame_no)

    def _reload_list(self, new_value=None):
        self._list_view.options = self._model.get_account_summary()
        self._list_view.value = new_value

    def _edit(self):
        self.save()
        self._model.current_id = self.data["account"]
        raise NextScene("Edit Account")

    def _quit_on_ok(self, selected, value):
        # Yes is the first button
         if selected == 0:
            # Insert new account data
            maxid = self._model.get_max_id()
            key = ["id", "accountnumber", "name", "bounty", "distribution", "status", "lastseen", "contractupd","authorization"]
            val = [maxid[0]+1, value, "", "", "", "", "", "", ""]
            newdata=dict(zip(key, val))
            self._model.update_current_account(newdata)

            # Open Add Account Scene
            self._model.current_id = maxid[0]+1
            raise NextScene("Add Account")

    def _input_account_no(self):
        self._scene.add_effect(
            AccountPopUpDialog(self._screen,
                                " ACCOUNT NO",
                                ["OK", "CANCEL"],
                                has_shadow=True,
                                on_close=self._quit_on_ok))

    @staticmethod
    def _quit():
        raise NextScene("Main")


class AccountAddView(Frame):
    def __init__(self, screen, model):
        super(AccountAddView, self).__init__(screen,
                                        screen.height,
                                        screen.width-2,
                                        has_border=False,
                                        hover_focus=True,
                                        edit_account=False,
                                        can_scroll=False,
                                        reduce_cpu=False)
        # Theme
        self.set_theme("green")

        # Save off the model that accesses the contacts database.
        self._model = model

        # Create the form for displaying the list of contacts.
        layout = Layout([100], fill_frame=True, label_offset=2)
        self.add_layout(layout)

        layout.add_widget(Divider(height=2, draw_line=False))
        textwiget= Text("Account NO.", name="accountnumber", force_x=8)
        textwiget.disabled = True
        layout.add_widget(textwiget)
        layout.add_widget(Divider(draw_line=True))
        layout.add_widget(Divider(height=2, draw_line=False))
        layout.add_widget(Text("AUTHORIZATION", "authorization"))
        layout.add_widget(Divider(draw_line=False))
        layout.add_widget(Text("STATUS", "status"))
        layout.add_widget(Divider(draw_line=False))
        layout.add_widget(Text("NAME", "name"))
        layout.add_widget(Divider(draw_line=False))
        layout.add_widget(Text("AMOUNT", "bounty"))
        layout.add_widget(Divider(draw_line=False))
        layout.add_widget(Text("LOCATION", "lastseen"))
        layout.add_widget(Divider(draw_line=False))
        layout.add_widget(TextBox(3, "UPDATE", "contractupd", as_string=True, line_wrap=True, button_offset=-1))
        layout.add_widget(Divider(draw_line=False))
        layout.add_widget(Text("DISTRIBUTION", "distribution"))
        layout2 = Layout([1, 1, 1], fill_frame=False)
        self.add_layout(layout2)
        layout2.add_widget(Divider(height=2, draw_line=False), 1)
        layout2.add_widget(Divider(height=1, draw_line=False), 2)
        layout2.add_widget(Button("TRANSMIT", self._trasmit), 2)
        layout2.add_widget(Label(datetime.datetime.now().strftime("%H:%M %p"), 1, align="^", name="currenttime"), 1)

        screen.refresh()
        self.fix()

    def update(self, frame_no):
        dt = self._layouts[1].find_widget("currenttime")
        dt.text = datetime.datetime.now().strftime("%H:%M  %p")
        super().update(frame_no)

    def reset(self):
        super(AccountAddView, self).reset()
        self.data = self._model.get_current_account()

    def _trasmit(self):
        self.save()
        self._model.update_current_account(self.data)
        self.save_transmit_data()
        raise NextScene("Transmit")

    def process_event(self, event):
        if isinstance(event, KeyboardEvent):
            if event.key_code == Screen.KEY_ESCAPE:
                self._model.delete_account(self._model.current_id)
                raise NextScene("Account List")

       # Pass any other event on to the Frame and contained widgets.
        return super(AccountAddView, self).process_event(event)

    def save_transmit_data(self):
        listdata=[]
        data = self._model.get_transmit_data()
        for i in range(len(data)):
            listdata.append(data[i][0])
        for i in range(0, len(listdata)*2, 2):
            listdata.insert(i+1, "]\n")
        file = open("transmit_data.dat", "wb")
        pickle.dump(listdata,file)
        file.close()


class AccountEditView(Frame):
    def __init__(self, screen, model):
        super(AccountEditView, self).__init__(screen,
                                        screen.height,
                                        screen.width,
                                        has_border=True,
                                        hover_focus=True,
                                        can_scroll=False,
                                        edit_account=True,
                                        reduce_cpu=False,
                                        border_start_x=2,
                                        border_end_y=6)

        # Theme
        self.set_theme("green")

        # Save off the model that accesses the contacts database.
        self._model = model

        layout = Layout([100], fill_frame=True, offset_max=True)
        self.add_layout(layout)
        layout.add_widget(Label("CATEGORY                   INFORMATION"), 0)
        layout.add_widget(Divider(draw_line=False), 0)
        layout.add_widget(Label("> SUBJECT ...........", name="name", attr=True), 0)
        layout.add_widget(Divider(draw_line=False), 0)
        layout.add_widget(Text("> BOUNTY ............", "bounty"), 0)
        layout.add_widget(Divider(draw_line=False), 0)
        layout.add_widget(Text("> DISTRIBUTION ......", "distribution"), 0)
        layout.add_widget(Divider(draw_line=False), 0)
        layout.add_widget(Text("> STATUS ............", "status"), 0)
        layout.add_widget(Divider(draw_line=False), 0)
        layout.add_widget(Text("> LAST SEEN .........", "lastseen"), 0)
        layout.add_widget(Divider(draw_line=False), 0)
        layout.add_widget(TextBox(4, "> UPDATE ............", "contractupd", as_string=True, line_wrap=True, button_offset=-1),0)

        layout2 = Layout([1, 1, 1], fill_frame=False)
        self.add_layout(layout2)
        layout2.add_widget(Divider(height=2, draw_line=False), 0)
        layout2.add_widget(Label("< NEXT >  LN"), 0)
        layout2.add_widget(Divider(height=2, draw_line=False), 1)
        layout2.add_widget(Label("02-0715"), 1)
        layout2.add_widget(Divider(height=4, draw_line=False), 2)
        layout2.add_widget(Button("TRANSMIT", self._trasmit, align=">"), 2)
        layout2.add_widget(Divider(height=2, draw_line=False), 1)
        layout2.add_widget(Label(datetime.datetime.now().strftime("%H:%M %p"), 1, align="^", name="currenttime"), 1)

        screen.refresh()
        self.fix()

    def update(self, frame_no):
        dt = self._layouts[1].find_widget("currenttime")
        dt.text = datetime.datetime.now().strftime("%H:%M  %p")
        super().update(frame_no)

    def reset(self):
        super(AccountEditView, self).reset()
        self.data = self._model.get_current_account()

    def _trasmit(self):
        self.save()
        self._model.update_current_account(self.data)
        self.save_transmit_data()
        raise NextScene("Transmit")

    def process_event(self, event):
        if isinstance(event, KeyboardEvent):
            if event.key_code == Screen.KEY_ESCAPE:
                raise NextScene("Account List")

       # Pass any other event on to the Frame and contained widgets.
        return super(AccountEditView, self).process_event(event)

    def save_transmit_data(self):
        listdata=[]
        data = self._model.get_transmit_data_orderby()
        for i in range(len(data)):
            listdata.append(data[i][0])
        for i in range(0, len(listdata)*2, 2):
            listdata.insert(i+1, "]\n")
        file = open("transmit_data.dat", "wb")
        pickle.dump(listdata,file)
        file.close()


class TransmitView(Frame):
    def __init__(self, screen, model):
        super(TransmitView, self).__init__(screen,
                                          screen.height,
                                          screen.width+1,
                                          has_border=False,
                                          hover_focus=False,
                                          can_scroll=False,
                                          has_shadow=False,
                                          reduce_cpu=False)
        # Theme
        self.set_theme("transmit_green")

        self._line = 0
        self._column = 0

        # Create the form for displaying the list of contacts.
        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)

        layout.add_widget(TextBox(screen.height,"", as_string=True, line_wrap=True, button_offset=0))

        screen.clear()
        screen.refresh()
        self.fix()

    def update(self, frame_no):
        if len(self._data) == 0:
            # Read Transmit Data File
            file=open("transmit_data.dat", "rb")
            self._data = pickle.load(file)
            file.close()
            self._layouts[0].focus(force_first=True)

        # Draw Trasmit Data Character By Character
        if len(self._data) > self._line:
            char = self._data[self._line][self._column]
            # Make Keyboard Event Handler
            event = KeyboardEvent(ord(char))
            self.scene.process_event(event)
            if ord(char) in [10, 13]:
                self._line += 1
                self._column = 0
            else:
                self._column += 1
        elif len(self._data) == self._line:
            self._line = 0
            self._column = 0
            current_widget = self._layouts[self._focus].get_current_widget()
            current_widget.value = None
            super(TransmitView, self).reset()
            raise NextScene("Main")

        # Call force_update() To Speed Up Display　
        self._screen.force_update()
        # Call Super Class Method
        super().update(frame_no)
