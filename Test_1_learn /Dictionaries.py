# Creating a dictionary

monthConversions = {
    "Jan": "January",               # The key is Jan the January is the Value
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions.get("Dec", "Not a valid key"))           # Or I could use open and closed bracket
