import obsws_python as obs

host = "localhost"
port = 4455


cl = obs.ReqClient(host='localhost', port=4455)

cl.set_input_settings("testmedia",{"local_file": "D:\Music\Gomathrow.ogg"},True)
