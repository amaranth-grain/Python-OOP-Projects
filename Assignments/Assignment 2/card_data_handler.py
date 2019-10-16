"""
Handles data and file inputs / outputs from app.
"""

from datetime import datetime


class DataHandler:
    """
    Handle app data.
    """
    @staticmethod
    def backup_data(manager):
        """
        Export card list in CardManager in JSON format to txt file.
        :param manager: CardManager
        :return: None
        """
        time = datetime.now().strftime("%m%d%Y_%H%M")
        path = f"./OnederCard_Export_{time}.txt"
        with open(path, mode="w", encoding="utf-8") as backup:
            backup.write(manager.card_list_json)
        print("Backed up data successfully.")