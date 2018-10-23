from __future__ import print_function

import redis

print('Loading function')

apikey = "mxHDufXzNoqATQJT6xGEoxajC6fhHv7A"
pool = redis.ConnectionPool(host='13.211.204.107', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

## 鏀堕泦鎵�鏈夌殑棰勮淇℃伅
def connect_alerts():
    pass


## 鏌ヨ鍛婅骞跺彂閫佸埌
def query_alert(event,context):
    alert=r.get("alerts")
    from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

    # For certificate based connection
    myMQTTClient = AWSIoTMQTTClient("2cdb55218fee9178fc42b63cced485fe7899f82d4d1a3c5eb1c78b77f50654a7")
    # For Websocket connection
    # myMQTTClient = AWSIoTMQTTClient("myClientID", useWebsocket=True)
    # Configurations
    # For TLS mutual authentication
    myMQTTClient.configureEndpoint("awxgxd7z6nhhi.iot.ap-southeast-2.amazonaws.com", 8883)
    # For Websocket
    # myMQTTClient.configureEndpoint("YOUR.ENDPOINT", 443)
    # For TLS mutual authentication with TLS ALPN extension
    # myMQTTClient.configureEndpoint("YOUR.ENDPOINT", 443)
    myMQTTClient.configureCredentials("root-CA.crt", "2cdb55218f-private.pem.key", "2cdb55218f-certificate.pem.crt")
    # For Websocket, we only need to configure the root CA
    # myMQTTClient.configureCredentials("YOUR/ROOT/CA/PATH")
    myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
    myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
    myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
    myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

    myMQTTClient.connect()
    print("start")
    myMQTTClient.publish("myTopic", alert, 0)
    myMQTTClient.subscribe("myTopic", 1, connect_alerts)
    myMQTTClient.unsubscribe("myTopic")
    myMQTTClient.disconnect()
    print(alert)
    print("END")
    return alert




print("Function End ~~")

if __name__ == '__main__':
    # query_location()
    # event={"location":"31,121","query":{"city":"shanghai","period":"3hour"},"method":1}
    # query_weather(event,2)
    # # record_rds(1,6)
    # Import SDK packages
    query_alert()