# Flask app -hello world ap

from flask import Flask

app=Flask(__name__)

@app.route("/",methods=['GET'])
def home():
    return 'HELLO WORLD'


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5001)  #host="0.0.0.0" make the app accessible from any IP address, not just the local machine


    '''
    By default, Flask only binds to 127.0.0.1 (localhost), which means it is only accessible from the local machine.

    If you set the host to 0.0.0.0, your app will be accessible not only from your local machine but also from other devices on the same network or 
    even over the internet (if the machine's firewall and network allow it)

    #we gave ip address as 0.0.0.0 so it will run on http://127.0.0.1:5001/,  http://192.168.0.16:5001/  ,http://localhost:5001/

    #local address of mac  IPv4 add = 192.168.0.16  (run  ipconfig getifaddr en0 in terminal)
    '''