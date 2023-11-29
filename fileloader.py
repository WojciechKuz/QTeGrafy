
# reads file where every row is in format: 'float, float, int'
# to list of tuples
def readFile(filepath: str) -> list:
	file = open(filepath, "r")
	pointlist = []
	for line in file:
		separatedline = line.split(',')
		row = (
			float(separatedline[0].rstrip('\n')),
			float(separatedline[1].rstrip('\n')),
		  	int(separatedline[2].rstrip('\n'))
		)			# tuple
		pointlist.append(row)
	file.close()
	return pointlist

from PySide6.QtWidgets import QFileDialog
def selectFile(parent) -> str:
	dialog = QFileDialog(parent)
	dialog.setFileMode(QFileDialog.ExistingFile)
	if dialog.exec_():
		filenames = dialog.selectedFiles()
		if len(filenames) > 1:
			print("Uwaga! Wybrano wiecej niz jeden plik, czytam tylko pierwszy.")
		return filenames[0]
	print("Uwaga! Pominieto dokonanie wyboru pliku.")
	return ""

# tylko usuwa duplikaty
def normalize(input: list):
	return list(set(input))

# uses sets to normalize
# sets are unordered (no indexes), unchangeable and without duplicates
# tuples are ordered, unchangeable, and allow duplicate values. Has indexes.

if __name__ == "__main__":
	print("TESTS:")
	print(normalize([(5, "sir"),(6, "ser"),(3, "sir"),(5, "sir"),(7, "stirr")]))
	lis = []
	lis.append((5, "sir"))
	lis.append((7, "stirr"))
	print(lis)

# list of tuples can be converted to set, but not list of lists