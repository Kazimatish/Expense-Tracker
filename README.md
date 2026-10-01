# Expense Tracker

A simple command-line expense tracker written in Python. Enter your expense for each day and quickly check your daily, weekly, and monthly totals.

## Features

- Add an expense for the day
- View the latest day's expense
- View the total of the last 7 days (weekly)
- View the total of the last 30 days (monthly)
- Input validation: non-numeric input is rejected instead of crashing the program
- Clean exit option

## Requirements

- Python 3.8 or newer
- No external libraries needed

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/Kazimatish/Expense-Tracker.git
   cd Expense-Tracker
   ```

2. Run the program:

   ```bash
   python expense_tracker.py
   ```

## Usage

When the program starts, you will see a menu:

```
=========================
Your Expense Tracker
=========================
0. Enter today's expense
1. Daily expense
2. Weekly expense (last 7 days)
3. Monthly expense (last 30 days)
4. Exit
Select your choice:
```

| Option | What it does |
| ------ | ------------ |
| `0` | Add an expense for the day |
| `1` | Show the most recent day's expense |
| `2` | Show the total of the last 7 entries |
| `3` | Show the total of the last 30 entries |
| `4` | Exit the program |

### Example

Entering 100, 200, and 300 as three separate days gives:

- Daily: `300`
- Weekly: `600`
- Monthly: `600`

## How It Works

Each entry is stored in a list, and one entry represents one day. Totals are calculated from that list using slicing:

- Daily: `expenses[-1]`
- Weekly: `sum(expenses[-7:])`
- Monthly: `sum(expenses[-30:])`

## Limitations

- Data is stored in memory only, so it is lost when the program closes.
- Each entry counts as one day; the program does not use real calendar dates.

## Future Improvements

- Save and load expenses from a file (JSON or CSV)
- Record real dates so multiple entries on the same day are combined
- Add expense categories (food, transport, etc.) with a category summary
- Edit or delete past entries

## Author

Abdul Kalam, Computer Science student at FUUAST, Islamabad
