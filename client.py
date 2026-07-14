class MetaMuseComputerUseAgentClient:
    def get_coordinates(self, screen_metadata: dict) -> dict:
        return {"next_action_coordinates": "click x=450 y=320"}