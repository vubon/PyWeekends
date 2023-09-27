# PyWeekends: Weekend Dates Formatter

PyWeekends is a Python package that provides a convenient way to generate weekend dates based on the Calendar. 
It includes a class named `Weekend` to generate weekend dates and an `OutputFormatter` class to format 
the generated dates into JSON.

## Features

- Generate weekend dates for all months in a given year.
- Generate weekend dates for a specific month.
- Format the generated dates as JSON.

## Installation

To install the package, use pip:

```bash
pip install PyWeekends
```
## Usage
```python
from PyWeekends import Weekend, WeekendStart

# Generate weekend dates for a specific month and format as JSON
w = Weekend(year=2024)
january_weekends = w.month_weekends("January")
json_data = january_weekends.as_json()
print(json_data)
# Output
# ["6", "7", "13", "14", "20", "21", "27", "28"]
# Generate weekend dates for all months and format as JSON
all_month_weekends = w.all_weekends()
json_data_all_months = all_month_weekends.as_json()
print(json_data_all_months)

#Output
# {"1": ["6", "7", "13", "14", "20", "21", "27", "28"], "2": ["3", "4", "10", "11", "17", "18", "24", "25"], 
# "3": ["2", "3", "9", "10", "16", "17", "23", "24", "30", "31"], "4": ["6", "7", "13", "14", "20", "21", "27", "28"], 
# "5": ["4", "5", "11", "12", "18", "19", "25", "26"], "6": ["1", "2", "8", "9", "15", "16", "22", "23", "29", "30"],
# "7": ["6", "7", "13", "14", "20", "21", "27", "28"], "8": ["3", "4", "10", "11", "17", "18", "24", "25", "31"], 
# "9": ["1", "7", "8", "14", "15", "21", "22", "28", "29"], "10": ["5", "6", "12", "13", "19", "20", "26", "27"], 
# "11": ["2", "3", "9", "10", "16", "17", "23", "24", "30"], "12": ["1", "7", "8", "14", "15", "21", "22", "28", "29"]}

```

## Changelog
See [Changelog](CHANGELOG.md)

## License
[MIT](LICENSE)