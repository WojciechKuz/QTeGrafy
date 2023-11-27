
# reads file where every row is in format: 'float, float, int'
# to list of lists
def readFile(filepath: str) -> list:
	file = open(filepath, "r")
	pointlist = []
	for line in file:
		separatedline = line.split(',')
		row = []
		row.append(float(separatedline[0].rstrip('\n')))
		row.append(float(separatedline[1].rstrip('\n')))
		row.append(  int(separatedline[2].rstrip('\n')))
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