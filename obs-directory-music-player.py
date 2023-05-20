import obsws_python as obs
import PySimpleGUI as sg
import glob

sg.theme("DarkBlue")

layout=[
  [sg.Text("OBS-Directory-Music-Player")],
  [sg.Text("port"),sg.InputText("4455",key="port")],
  [sg.Text("password"),sg.InputText("",key="password")],
  [sg.Button("OK",key="ok")],
  [sg.Button("test",key="test")]]
window=sg.Window("OBS-Directory-Music-Player",layout)#Guiの設定

cl = obs.ReqClient(host='localhost', port=4455)

while True:
  event,values=window.read()
  if event==sg.WIN_CLOSED:
    break
  if event=="ok":
    cl = obs.ReqClient(host='localhost', port=values["port"], password=values["password"])
  if event=="test":
    cl.set_input_settings("testtext",{"text": "にゃんこ"},True)