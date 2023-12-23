from confluent_kafka import Producer

# Kafka bootstrap servers
bootstrap_servers = 'localhost:9093,localhost:9095,localhost:9097,localhost:9099,localhost:9101'

# Kafka topic to produce messages to
topic = 'test-topic'

# Configure the Kafka producer
conf = {
    'bootstrap.servers': bootstrap_servers,
}

# Create Kafka producer instance
producer = Producer(conf)

# Produce a message to the Kafka topic
message_value = 'Hello, Kafka!'
producer.produce(topic, value=message_value)

# Wait for any outstanding messages to be delivered and delivery reports received
producer.flush()

print(f"Produced message: '{message_value}' to topic: '{topic}'")
