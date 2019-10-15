# Complete project details at https://RandomNerdTutorials.com

def web_page():
  html = """
<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <style type="text/css">
        #submit {
         background-color: #bbb;
         padding: .5em;
         -moz-border-radius: 5px;
         -webkit-border-radius: 5px;
         border-radius: 6px;
         color: #fff;
         font-family: 'Oswald';
         font-size: 20px;
         text-decoration: none;
         border: none;
        }

        #submit:hover {
         border: none;
         background: orange;
         box-shadow: 0px 0px 1px #777;
        }
    </style>
    <body>
        <h1>
          ESP Web Server Prender/Apagar LED
        </h1>
        <a href=\"?led=on\">
            <button  id="submit">
                ON
            </button>
        </a>&nbsp;
        <a href=\"?led=off\">
            <button  id="submit">
              OFF
            </button>
        </a>
    </body>
</html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)
  led_on = request.find('/?led=on')
  led_off = request.find('/?led=off')
  if led_on == 6:
    print('LED ON')
    led.value(1)
  if led_off == 6:
    print('LED OFF')
    led.value(0)
  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()