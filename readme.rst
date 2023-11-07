=================================================================
JOHN WICK Continental Administration Commodore64 TUI Application
=================================================================


I watched JOHN WICK Chapter 4 and suddenly wanted to recreate the Commodore terminal in the Administrator's office, so I made one.


Installation
============

From source
-----------
git clone https://github.com/
cd JohnWickCommodore64
python3 -m pip install .

This program supports Python version 3.9 or above is now required.
This is based on `peterbrittain's ASCIIMATICS. <https://github.com/peterbrittain/asciimatics>`_.
Since this application modifies the asciimatics code, do not overwrite it with a newer version of asciimatics.

* Windows users only

.. code-block:: bash

    $ pip install pywin32

* All os users

.. code-block:: bash

    $ pip install pyfiglet
    $ pip install wcwidth


How to use it?
==============

Terminal
--------

This Application use terminal and Commodore64 font.
You can get commodore64 font `here <https://www.dafont.com/commodore-64.font>`_.

This is the recommended terminal application.
* Windows:  Windows Terminal, cool-retro-term(Need WSL)
* MacOSX:   iTerm2, cool-retro-term

I don't check linux termial, use a terminal that can display non-equal fonts.

Setting Terminal
----------------


