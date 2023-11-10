####################################################################
**JOHN WICK Continental Administration Commodore64 TUI Application**
####################################################################


I watched JOHN WICK Chapter 4 and suddenly wanted to recreate the Commodore terminal in the Administrator's office, so I made one.

===========

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

    $ git clone https://github.com/uroboros-71/JohnWickCommodore64.git
    $ cd JohnWickCommodore64
    $ python3 -m pip install -e .


Preparation
***********

Terminal
========

This Application use terminal and Commodore64 font.

You can get commodore64 font from the button below.

.. image:: https://user-images.githubusercontent.com/70955882/282057356-1dad0255-edb9-4952-81c7-3dde0ee281b7.gif
    :target: https://www.dafont.com/commodore-64.font


This is the recommended terminal application.

* Windows:  Windows Terminal, cool-retro-term(Need WSL)
* MacOSX:   iTerm2, cool-retro-term
* Linux:    cool-retro-term

I don't check other linux termial, use a terminal that can display non-equal fonts.

Setting Terminal
----------------

Set the font to Commodore 64 Angled.

If the terminal allows you to specify the screen size, set Columns 40 and Rows 25.

If the terminal does not allow you to specify the screen size, display monitor.txt in the terminal and
adjust the screen size so that 40 columns and 25 rows can be displayed.


iTerm2
^^^^^^
iTerm2 Setting Text Tab

.. image:: https://user-images.githubusercontent.com/70955882/282056564-f6fc44a3-0049-4297-a953-69953187dd77.jpg
    :height: 613px
    :width: 1200px
    :scale: 70 %
    :alt: iTerm2 Setting Image Text Tab

iTerm2 Setting Window Tab

.. image:: https://user-images.githubusercontent.com/70955882/282056578-e091a6f6-5e5e-4eaf-99ce-e200dbbe4b3b.jpg
    :height: 757px
    :width: 1200px
    :scale: 70%
    :alt: iTerm2 Setting Image Window Tab

Windows Terminal
^^^^^^^^^^^^^^^^
Please check ”Show all fonts" checkbox ON, Commodore64 fonts are not displayed in "Font face".
　I would suggest turning on the retro terminal effect.

.. image:: https://user-images.githubusercontent.com/70955882/282056899-e1eeca93-ff06-4581-86c9-3668da474939.jpg
    :height: 958px
    :width: 1200px
    :scale: 70%
    :alt: Windows Terminal Appearance


If you cannot set up a table, such as in a Windows Terminal, display monitor.txt on the screen and resize the window so that the entire table can be displayed.

.. image:: https://user-images.githubusercontent.com/70955882/282057065-4a330d10-f831-4d6c-996a-9fb823bdb45b.jpg
    :height: 1010px
    :width: 1200px
    :scale: 70%
    :alt: monitor.txt

Usage
-----

.. code-block:: bash

    usage: continental [-h] [-d] [-m]

    options:
    -h, --help    show this help message and exit
    -d, --dbfile  The database file to be opened
    -m, --memory  The database might be stored in memory

Youtube
*******

.. image:: https://i9.ytimg.com/vi/mQAHIwYoNZ4/mq1.jpg?sqp=CLiouKoG&rs=AOn4CLBX0HolhaqfhnbLmuor3FigR1VbyQ
    :target: https://youtu.be/mQAHIwYoNZ4
    :height: 720px
    :width: 1080px
    :scale: 70%


Uninstalle
************

.. code-block:: bash

    $ python3 -m pip uninstall JohnWickCommodore64
    $ rm -rf JohnWickCommodore64


More examples
*************

**Example of cool-retro-terminal display.**

.. image:: https://user-images.githubusercontent.com/70955882/282057095-b32454f8-1c09-4c01-b9e6-0986421c46e0.jpg
    :height: 1057px
    :width: 1200px
    :scale: 70%
    :alt: monitor.txt
