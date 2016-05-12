import paho.mqtt.client as mqtt

server = '192.168.0.209'
port = '1883'
topic = 'foo/bar'


client = mqtt.Client()
#client.on_connect = on_connect
#client.on_message = on_message

client.connect(server, port, 60)

client.publish("foo/bar","msg coming thru.")

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
#client.loop_forever()

