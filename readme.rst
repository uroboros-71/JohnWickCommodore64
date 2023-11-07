####################################################################
**JOHN WICK Continental Administration Commodore64 TUI Application**
####################################################################


I watched JOHN WICK Chapter 4 and suddenly wanted to recreate the Commodore terminal in the Administrator's office, so I made one.

Description
***********

This program supports Python version 3.9 or above is now required.

This is based on `peterbrittain's ASCIIMATICS. <https://github.com/peterbrittain/asciimatics>`_.

Since this application modifies the asciimatics code, do not overwrite it with a newer version of asciimatics.

Installation
************

From source
===========

.. code-block:: bash

git clone https://github.com/uroboros-71/JohnWickCommodore64.git
cd JohnWickCommodore64
python3 -m pip install -e .


Preparation
***********

Terminal
========

This Application use terminal and Commodore64 font.
You can get commodore64 font `here <https://www.dafont.com/commodore-64.font>`_.

This is the recommended terminal application.
* Windows:  Windows Terminal, cool-retro-term(Need WSL)
* MacOSX:   iTerm2, cool-retro-term

I don't check linux termial, use a terminal that can display non-equal fonts.

Setting Terminal
----------------

Set the font to Commodore 64 Angled.

If the terminal allows you to specify the screen size, set Columns 40 and Rows 25.

If the terminal does not allow you to specify the screen size, display monitor.txt in the terminal and
adjust the screen size so that 40 columns and 25 rows can be displayed.
