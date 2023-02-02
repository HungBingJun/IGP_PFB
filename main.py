from pathlib import Path
import cash_on_hand, overheads, profit_loss

creating a new text file and assigning it to the current working directory
home = Path.cwd()
file_path = home/"summary_report.txt"
file_path.touch()

#creating a summary list to store all the different functions
summary = [overheads.overheads(),
            "\n",cash_on_hand.cash_on_hand(),
            "\n",profit_loss.profit_loss()]

#writing mutiple lines in summary to a textfile
with file_path.open(mode = "w",encoding = "UTF-8") as file:
    file.writelines(summary)
