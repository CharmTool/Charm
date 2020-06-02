import matplotlib.pyplot as plt
import sys

def plot1(aciertos, fallos, nPruebas):

	title = sys.argv[1][:-4]+'_graph.png'
	names = ['aciertos', 'fallos']
	values = [aciertos, fallos]
	if aciertos > fallos:
		explode = (0.06, 0)
	else:
		explode = (0, 0.06)

	fig1, ax1 = plt.subplots()
	ax1.pie(values, explode=explode, labels=names, autopct='%1.1f%%',
        shadow=True, startangle=90)
	ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
	plt.suptitle(title)
	plt.savefig(title)

	return 

if __name__ == "__main__":

	f =  open(sys.argv[1], "r")
	if f.mode == 'r':
		aciertos = int(f.readline())
		fallos = f.readline()
		if fallos == '\n':
			fallos = 0
		else:
			fallos = int(fallos)
		nPruebas = int(sys.argv[2])
		print(aciertos, fallos)
		plot1(aciertos, fallos, nPruebas)
	else:
		print("The file did not open")
