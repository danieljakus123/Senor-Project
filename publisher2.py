import paho.mqtt.client as mqtt
import time

mqttc = mqtt.Client()
mqttc.connect( "iot.eclipse.org" ) # test broker
counter = 0

while True:
    file = open("results.txt")
    message = "Hello World {}!".format(counter)
    print( message )
    mqttc.publish( "mytest/counter", message )
    file.write("results.txt", "Danielnode/#")
    mqttc.loop()
    counter += 1
    time.sleep(2)
