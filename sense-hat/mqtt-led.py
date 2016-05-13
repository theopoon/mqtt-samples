import paho.mqtt.client as mqtt
import json, time
import socket, os
import struct
from sense_hat import SenseHat 


hostname = socket.gethostname()
random_client_id = hostname

server = '192.168.0.234'
port = '1883'
topic = hostname + "/#"

sense = SenseHat()

def rgb_str2list(str):
        return struct.unpack('BBB',str.decode('hex'))
def try_led(str):
        if str == "clear":
                sense.clear()
                return
        #TODO: should add other led functions
        #rotate
        #send text
        
        #try split the str
        arr = str.split(",")
        if len(arr) != 64:
            print "Incorrect length!!! (must be 64 currently ", len(arr) , ")."
            return
        pixels = []
        for pixel in arr:
            pixels.append(rgb_str2list(pixel))
        #print pixels
        sense.low_light = True
        sense.set_pixels(pixels)


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
        #print("Connected.")
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe(topic)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
        #print "Topic: ", msg.topic+ '\nMessage: ' +str(msg.payload)
        topic = str(msg.topic)
        #print topic
        if topic == hostname + "/led":
                #print "Do LED action"
                try_led(msg.payload)
        #print "on_message" , msg.topic+ '\nMessage: ' +str(msg.payload)
        #print "\n------------EOM--------------\n"

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(server, port, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
