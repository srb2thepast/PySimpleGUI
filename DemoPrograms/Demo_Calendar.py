#!/usr/bin/env python
import PySimpleGUI as sg

"""
    Simple test harness to demonstate how to use the CalendarButton and the get date popup
"""

layout = [[sg.Text('Date Chooser Test Harness', key='-TXT-')],
      [sg.Input(key='-IN-', size=(20,1)), sg.CalendarButton('Cal US No Buttons', close_when_date_chosen=True,  target='-IN-')],
      [sg.Input(key='-IN3-', size=(20,1)), sg.CalendarButton('Cal US Monday', close_when_date_chosen=False,  target='-IN3-', begin_at_sunday_plus=1)],
      [sg.Input(key='-IN2-', size=(20,1)), sg.CalendarButton('Cal German Feb 2020',  target='-IN2-',  default_date_m_d_y=(2,None,2020), locale='de_DE', begin_at_sunday_plus=1 )],
      [sg.Input(key='-IN4-', size=(20,1)), sg.CalendarButton('Cal Format %m-%d',  target='-IN4-', format='%m-%d', default_date_m_d_y=(2,None,2020), locale='de_DE', begin_at_sunday_plus=1 )],
      [sg.Button('Read'), sg.Button('Date Popup'), sg.Exit()]]

window = sg.Window('window', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    elif event == 'Date Popup':
        sg.popup('You chose:', sg.popup_get_date())
window.close()