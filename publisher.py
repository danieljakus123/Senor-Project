import paho.mqtt.client as mqtt
import time

mqttc = mqtt.Client()
mqttc.connect( "iot.eclipse.org" ) # test broker
counter = 0

while True:
    message = "Hello World {}!".format(counter)
    print( message )
    mqttc.publish( "mytest/counter", message )
    mqttc
    mqttc.loop()
    counter += 1
    time.sleep(2)
