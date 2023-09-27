import calendar
import datetime
from typing import List, AnyStr
from enum import Enum

from PyWeekends.output_formatter import OutputFormatter


class WeekendStart(Enum):
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


class Weekend:
    """
    The Weekend class generates weekend dates based on the Calendar.

    Attributes:
        year (int): The year for which to generate weekend dates. Defaults to the current year.
        weekend_start (WeekendStart): The day at which the weekend starts (Friday, Saturday, or Sunday).
            Defaults to Saturday.

    Methods:
        all_weekends(enable_month_name: bool = False) -> OutputFormatter:
            Generates weekend dates for all months in the given year.
            Args:
                enable_month_name (bool): True to return month names, False to return month numbers.
            Returns:
                OutputFormatter: An instance of OutputFormatter containing the weekend dates.

        Month_weekends(month_name: AnyStr) -> List[str]:
            Generates weekend dates for a specific month.
            Args:
                month_name (str): Name of the month (case-insensitive).
            Returns:
                OutputFormatter: An instance of OutputFormatter containing the weekend dates.

        __Weekend_dates(month: int) -> List[str]:
            Helper method to generate weekend dates for a specific month.
            Args:
                month (int): Month number.
            Returns:
                List[str]: List of weekend dates for the specified month.

    Examples:
        w = Weekend(year=2024, weekend_start=WeekendStart.FRIDAY)
        weekends = w.all_weekends().as_json()
        print(weekends) # Outputs the weekend dates for all months in JSON format
    """

    def __init__(self, year: int = None, weekend_start: WeekendStart = WeekendStart.SATURDAY):
        """
        Initializes a Weekend instance.
        Args:
            year (int): The year for which to generate weekend dates. Defaults to the current year.
            weekend_start (WeekendStart): The day at which the weekend starts (Friday, Saturday, or Sunday).
            Defaults to Saturday.
        """
        self.year = year or datetime.datetime.now().year
        self.weekend_start = weekend_start

    def all_weekends(self, enable_month_name: bool = False) -> OutputFormatter:
        """
        Returns weekend dates for all months.
        :param enable_month_name: bool: True for month names, False for month numbers.
        :return: {"1": [<weekend date>, <weekend date>] ...}
        :rtype: dict
        """
        return OutputFormatter(
            {str(calendar.month_name[month] if enable_month_name else month): self.__weekend_dates(month) for month
             in range(1, 13)})

    def month_weekends(self, month_name: AnyStr) -> OutputFormatter:
        """
        Returns weekend dates for a specific month.
        :param month_name: str: Name of the month (case-insensitive).
        :return: List of weekend dates.
        """
        month = next((k for k, v in enumerate(calendar.month_name) if v.lower() == month_name.lower()), None)
        if not month:
            raise ValueError(f"Invalid month name: {month_name}")
        return OutputFormatter(self.__weekend_dates(month))

    def __weekend_dates(self, month: int) -> List[str]:
        """
        Returns weekend dates for a specific month.
        :param month: int: Month number.
        :return: List of weekend dates.
        """
        date_range = range(1, calendar.monthrange(year=self.year, month=month)[1] + 1)
        if self.weekend_start == WeekendStart.FRIDAY:
            days = [str(day) for day in date_range if datetime.date(self.year, month, day).weekday() in (4, 5)]
        else:
            days = [str(day) for day in date_range if datetime.date(self.year, month, day).weekday() in (5, 6)]

        return days
