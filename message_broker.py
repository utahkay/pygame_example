from pulsar import AuthenticationOauth2, Client, ConsumerType
import json


class Pulsar:
    def __init__(self, topic):
        self.client = self.pulsar_client()
        self.producer = self.client.create_producer(topic)

    def consumer(self, topic):
        return self.client.subscribe(topic, topic+"-subscription", consumer_type=ConsumerType.Exclusive)

    def auth_params(self):
        issuer_url = "https://auth.sncloud-stg.dev"
        private_key = "/Users/kayjohansen/service-account/sa-continuous-verification-staging.json"
        audience = "urn:sn:pulsar:cv-pulsar:test-2-10"
        return json.dumps({"issuer_url": issuer_url, "private_key": private_key, "audience": audience})

    def pulsar_client(self):
        service_url = "pulsar+ssl://test-2-10.cv-pulsar.sn3.dev:6651"
        return Client(service_url, authentication=AuthenticationOauth2(self.auth_params()))

    def send_message(self, msg):
        self.producer.send(msg.encode("utf-8"))

    def close(self):
        self.producer.close()
