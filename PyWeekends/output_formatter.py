import json
from typing import List, Dict, Union


class OutputFormatter:
    """
    The OutputFormatter class formats data and provides methods to represent it as JSON or other formats.

    Attributes:
        data (Union[Dict[str, List[str]], List]): The data to be formatted.

    Methods:
        as_json() -> str:
            Formats the data as JSON and returns the JSON string.

        to_original -> Union[Dict[str, List[str]], List]:
            Formats the data as an original object.e.g dict or List

    Example usage:
        data = {'January': ['5', '6', '12', '13', '19', '20', '26', '27'],
        'February': ['2', '3', '9', '10', '16', '17', '23', '24']}
        formatter = OutputFormatter(data)
        json_data = formatter.as_json()
        print(json_data)  # Outputs the data in JSON format

    """

    def __init__(self, data: Union[Dict[str, List[str]], List]):
        """
        Initializes an OutputFormatter instance.

        Args:
            data (Union[Dict[str, List[str]], List]): The data to be formatted.
        """
        self.data = data

    def as_json(self) -> str:
        """
        Formats the data as JSON and returns the JSON string.

        Returns:
            str: The data in JSON format.
        """
        if not isinstance(self.data, (dict, list)):
            raise TypeError("Invalid data type. Expected dict or list.")
        return json.dumps(self.data)

    def to_original(self) -> Union[Dict[str, List[str]], List]:
        """
        Formats the data as Original of parent class.
        Returns:
            Union[Dict[str, List[str]], List]
        """
        return self.data
