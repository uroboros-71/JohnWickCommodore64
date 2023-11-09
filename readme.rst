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

.. image:: https://private-user-images.githubusercontent.com/70955882/281436380-06ec5edb-60be-4848-89e3-527a711c53ac.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE2OTk0NTQ2MjQsIm5iZiI6MTY5OTQ1NDMyNCwicGF0aCI6Ii83MDk1NTg4Mi8yODE0MzYzODAtMDZlYzVlZGItNjBiZS00ODQ4LTg5ZTMtNTI3YTcxMWM1M2FjLmdpZj9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFJV05KWUFYNENTVkVINTNBJTJGMjAyMzExMDglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjMxMTA4VDE0Mzg0NFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWU2YTZkOTRkMTNhOGNmODhjNTc5ZmE5OWQ2MzRiNjI2NjliOTQ4ZjkwMjRhNjIwZTk4ODkwYzQxNDZiOTkxZTAmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.7KUR46tGJ39Oy26gYOmcr7XoJB0tzXU235PRGUiH7XU
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

.. image:: https://private-user-images.githubusercontent.com/70955882/281446011-2572a290-bae9-4baf-be3d-e78098939ef0.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE2OTk0NTU4NjMsIm5iZiI6MTY5OTQ1NTU2MywicGF0aCI6Ii83MDk1NTg4Mi8yODE0NDYwMTEtMjU3MmEyOTAtYmFlOS00YmFmLWJlM2QtZTc4MDk4OTM5ZWYwLmpwZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFJV05KWUFYNENTVkVINTNBJTJGMjAyMzExMDglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjMxMTA4VDE0NTkyM1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWIxYWJjMzFmNDdkYTA0ZThkYjU1MDFhOWIzNmMxYTcyYjQzNzcwZmE4NzU5ODY0ZTAwZDM5Y2VmM2U2MTM5NjcmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.p5v9qsx1y02AleXj4X1ugOLEcWw7zufao1RAKOAKhKA
    :height: 613px
    :width: 1200px
    :scale: 70 %
    :alt: iTerm2 Setting Image Text Tab

iTerm2 Setting Window Tab

.. image:: https://private-user-images.githubusercontent.com/70955882/281446027-da72419b-32a3-4662-a2ed-8fa71225b929.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE2OTk0NTU4NjMsIm5iZiI6MTY5OTQ1NTU2MywicGF0aCI6Ii83MDk1NTg4Mi8yODE0NDYwMjctZGE3MjQxOWItMzJhMy00NjYyLWEyZWQtOGZhNzEyMjViOTI5LmpwZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFJV05KWUFYNENTVkVINTNBJTJGMjAyMzExMDglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjMxMTA4VDE0NTkyM1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTkzMmNlZDBjOTJlYTUzMWI3MGE3OTUwNzhhNTExYWY3ZmZjM2M4OWYyNzA0MThkOTJjMzE4MGZmYjY0ODZkYzUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.xsRyb1jDbxjT9_iSqF5KTPg0ybempFMXdj5POFdyvE0
    :height: 757px
    :width: 1200px
    :scale: 70%
    :alt: iTerm2 Setting Image Window Tab

Windows Terminal
^^^^^^^^^^^^^^^^
Please check ”Show all fonts" checkbox ON, Commodore64 fonts are not displayed in "Font face".
　I would suggest turning on the retro terminal effect.

.. image:: https://private-user-images.githubusercontent.com/70955882/281705019-b0e33e9d-d9d5-40b1-9f7b-31011fc27858.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE2OTk1MjgwNDMsIm5iZiI6MTY5OTUyNzc0MywicGF0aCI6Ii83MDk1NTg4Mi8yODE3MDUwMTktYjBlMzNlOWQtZDlkNS00MGIxLTlmN2ItMzEwMTFmYzI3ODU4LmpwZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFJV05KWUFYNENTVkVINTNBJTJGMjAyMzExMDklMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjMxMTA5VDExMDIyM1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWU3NjYxM2UxZDdjYjBhNjY0YzU0NTgyNjVlOWRiZDJhMjA4MTMxYzFlYmIyZjY4NzIxNzBlYzllYmFiNmQ0MTkmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.ei8qBceLBTdNtUAggsTPxOSwyazmF0iHWCn-ccaIxdQ
    :height: 958px
    :width: 1200px
    :scale: 70%
    :alt: Windows Terminal Appearance


If you cannot set up a table, such as in a Windows Terminal, display monitor.txt on the screen and resize the window so that the entire table can be displayed.

.. image:: https://private-user-images.githubusercontent.com/70955882/281710941-d7d2b54b-2c0c-4208-b157-1f8fd4a9c217.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE2OTk1Mjg3NzgsIm5iZiI6MTY5OTUyODQ3OCwicGF0aCI6Ii83MDk1NTg4Mi8yODE3MTA5NDEtZDdkMmI1NGItMmMwYy00MjA4LWIxNTctMWY4ZmQ0YTljMjE3LmpwZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFJV05KWUFYNENTVkVINTNBJTJGMjAyMzExMDklMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjMxMTA5VDExMTQzOFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTgwMTYwOWJlYzFiZTdhZTNmYTRhYmZmMGYyY2VmOTE1OTU4YjAxOTI4ZDgxMzRiY2EzZWJiZmFhNDQwYTlkNzUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0._tAqovEVARN5KaBlvU7GTFRFEucv_CIyIMQZyrzqloc
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

.. image:: https://i9.ytimg.com/vi/oM6QopbFwxY/mqdefault.jpg?v=654cc491&sqp=CJCKs6oG&rs=AOn4CLD_LvhdnryW-QWgsjgb94YyGmt8CQ
    :target: https://youtu.be/oM6QopbFwxY
    :height: 480px
    :width: 720px


Uninstalle
************

.. code-block:: bash

    $ python3 -m pip uninstall JohnWickCommodore64
    $ rm -rf JohnWickCommodore64


More examples
*************

**Example of cool-retro-terminal display.**

.. image:: https://private-user-images.githubusercontent.com/70955882/281710965-12596eb7-b85e-4cff-820c-19650347b49f.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE2OTk1Mjg3NzgsIm5iZiI6MTY5OTUyODQ3OCwicGF0aCI6Ii83MDk1NTg4Mi8yODE3MTA5NjUtMTI1OTZlYjctYjg1ZS00Y2ZmLTgyMGMtMTk2NTAzNDdiNDlmLmpwZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFJV05KWUFYNENTVkVINTNBJTJGMjAyMzExMDklMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjMxMTA5VDExMTQzOFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWZjMTg5N2ZiYTJlMWU0MDhlODQ3NGYwZjgyNTdlOTc4ZTk3MGIzZGU4YWY2ZGIzNWVmZjAxMzI5N2JjZmMxMGQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0._mo9zYI6d8bk8cyQvc1OXlm9_D-XIgytbg1a3AVT7uw
    :height: 1057px
    :width: 1200px
    :scale: 70%
    :alt: monitor.txt
