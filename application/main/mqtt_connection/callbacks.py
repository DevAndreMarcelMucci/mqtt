from application.configs.broker_configs import mqtt_broker_configs
# from app.models import MqttData


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f'Cliente conectado com sucesso: {client}')
        client.subscribe(mqtt_broker_configs ["TOPIC"])
    else:
        print(f'Erro ao me conectar! codigo={rc}')

def on_subscribe(client, userdata, mid, granted_qos):    
    print(f'Client Subscribed at {mqtt_broker_configs["TOPIC"]}')
    print(f'QOS: {granted_qos}')

def on_message(client, userdata, message):
    print('Menssagem recebida!')
    print(client)
    print(message.payload)
    
# Função de callback para quando a conexão for perdida
def on_disconnect(client, userdata, flags, rc):
    if rc != 0:
        print("Desconexão inesperada. Tentando reconectar...")
        client.reconnect()