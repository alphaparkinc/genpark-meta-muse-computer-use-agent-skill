from client import MetaMuseComputerUseAgentClient
client = MetaMuseComputerUseAgentClient()
print(client.get_coordinates({"button_detected": True}))