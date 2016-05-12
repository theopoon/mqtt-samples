import paho.mqtt.client as mqtt

server = '192.168.0.209'
port = '1883'
#topic = '$SYS/broker/clients/connected'
topic = '#'

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
        print("Connected.")

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe(topic)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
        #print "Topic: ", msg.topic+ '\nMessage: ' +str(msg.payload)
        print "on_message" , msg.topic+ '\nMessage: ' +str(msg.payload)
        print "\n------------EOM--------------\n"

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(server, port, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
