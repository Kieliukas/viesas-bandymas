@staticmethod
def _otaUpdate():
    ulogging.info('Checking for Updates...')
    from .ota_updater import OTAUpdater
    otaUpdater = OTAUpdater('https://github.com/rdehuyss/chicken-shed-mgr', github_src_dir='src', main_dir='app', secrets_file="secrets.py")
    otaUpdater.install_update_if_available()
    del(otaUpdater)
from ota_update.main.ota_updater import OTAUpdater


def download_and_install_update_if_available():
     o = OTAUpdater('boot.py')
     o.install_update_if_available_after_boot('ViVa', 'Ropes314Makso')

def start():
    try:
     import usocket as socket        #importing socket
    except:
     import socket
    import network            #importing network
    import esp                 #importing ESP
    esp.osdebug(None)
    import gc
    gc.collect()

    ap = network.WLAN(network.STA_IF)

    ap.active(True)            #activating
    ap.connect('ViVa', 'Ropes314Makso')
    ap.ifconfig(('192.168.1.76', '255.255.255.0', '192.168.1.254', '8.8.8.8'))
    while ap.active() == False:
      pass
    print('Connection is successful')
    print(ap.ifconfig())
    def web_page():
      html = """<!DOCTYPE html>
    <html>
        <head> <title>ESP8266 Pins</title> </head>
        <body> <h1>Testas pakeistas</h1>
            <table border="1"> <tr><th>Pin</th><th>Value</th></tr> %s </table>
        </body>
    </html>
    """
      return html
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #creating socket object
    s.bind(('', 76))
    s.listen(5)
    while True:
      conn, addr = s.accept()
      print('Got a connection from %s' % str(addr))
      request = conn.recv(1024)
      print('Content = %s' % str(request))
      response = web_page()
      conn.send("HTTP/1.0 200 OK\r\n")
      conn.send("Content-type: text/html\r\n")
      conn.send("\r\n")
      conn.send(response)
      conn.close()

def boot():
    download_and_install_update_if_available()
    start()

boot()
