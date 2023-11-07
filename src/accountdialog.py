from inspect import isfunction
from functools import partial
from wcwidth import wcswidth
from asciimatics.widgets.button import Button
from asciimatics.widgets.frame import Frame
from asciimatics.widgets.layout import Layout
from asciimatics.widgets.textbox import TextBox
from asciimatics.widgets.text import Text
from asciimatics.widgets.utilities import _split_text


class AccountPopUpDialog(Frame):
    def __init__(self, screen, text, buttons, on_close=None, has_shadow=False, theme="popupdialog"):
        # Remember parameters for cloning.
        self._text = text
        self._buttons = buttons
        self._on_close = on_close

        # Decide on optimum width of the dialog.  Limit to 2/3 the screen width.
        string_len = wcswidth if screen.unicode_aware else len
        width = max(string_len(x) for x in text.split("\n"))
        width = max(width + 2,
                    sum(string_len(x) + 4 for x in buttons) + len(buttons) + 5)
        width = min(width, screen.width * 2 // 3)

        # Figure out the necessary message and allow for buttons and borders
        # when deciding on height.
        delta_h = 6 if len(buttons) > 0 else 2
        self._message = _split_text(text, width - 2, screen.height - delta_h, screen.unicode_aware)
        height = len(self._message) + delta_h
        self._accountnumber=""

        # Construct the Frame
        self._data = {"message": self._message,"accountnumber": self._accountnumber}
        super().__init__(
            screen, height, width, self._data, has_shadow=has_shadow, is_modal=True, can_scroll=False, reduce_cpu=False)

        # Build up the message box
        layout = Layout([15,70,15], fill_frame=True)
        self.add_layout(layout)
        text_box = TextBox(len(self._message), name="message")
        text_box.disabled = True
        layout.add_widget(text_box,1)
        layout.add_widget(Text("", name="accountnumber", max_length=7, validator=r"^\d{4}-\d{2}"),1)
        layout2 = Layout([1 for _ in buttons])
        self.add_layout(layout2)
        for i, button in enumerate(buttons):
            func = partial(self._destroy, i)
            layout2.add_widget(Button(button, func), i)
        self.fix()

        # Ensure that we have the right palette in place
        self.set_theme(theme)

    def _destroy(self, selected):
        self.save()
        self._scene.remove_effect(self)
        if self._on_close:
            self._on_close(selected, self.data["accountnumber"])

    def clone(self, screen, scene):
        """
        Create a clone of this Dialog into a new Screen.

        :param screen: The new Screen object to clone into.
        :param scene: The new Scene object to clone into.
        """
        # Only clone the object if the function is safe to do so.
        if self._on_close is None or isfunction(self._on_close):
            scene.add_effect(AccountPopUpDialog(screen, self._text, self._buttons, self._on_close))
