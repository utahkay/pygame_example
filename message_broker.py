from pulsar import AuthenticationOauth2, Client, ConsumerType
import json


class Pulsar:
    def __init__(self, topic):
        self.client = self.pulsar_client()
        self.producer = self.client.create_producer(topic)

    def consumer(self, topic):
        return self.client.subscribe(topic, topic+"-subscription", consumer_type=ConsumerType.Exclusive)

    def consumer_with_callback(self, topic, callback):
        return self.client.subscribe(topic, topic+"-subscription", consumer_type=ConsumerType.Exclusive,
                                     message_listener=callback)

    def auth_params(self):
        issuer_url = "https://auth.streamnative.cloud/"
        private_key = "/Users/kayjohansen/sndev-kjtest.json"
        audience = "urn:sn:pulsar:sndev:kj-game"
        return json.dumps({"issuer_url": issuer_url, "private_key": private_key, "audience": audience})

    def pulsar_client(self):
        service_url = "pulsar+ssl://kj-game.sndev.snio.cloud:6651"
        return Client(service_url, authentication=AuthenticationOauth2(self.auth_params()))

    def send_message(self, msg):
        self.producer.send(msg.encode("utf-8"))

    def close(self):
        self.producer.close()
