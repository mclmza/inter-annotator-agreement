import argparse
from argparse import RawTextHelpFormatter
import re
from nltk.metrics.agreement import AnnotationTask
import os.path
import sys

def operation(file1, file2, op, unify):
	lines1 = [x.split() for x in open(file1, "r")]
	lines2 = [x.split() for x in open(file2, "r")]

	if(op=="pos"):
		min = 0
		max = 6
		target = 3
	else:
		min = 0
		max = 10
		target = 6
	
	output = "output-" + op + ".txt"
	out_file = open(output,"w", 0)
	
	for i in range(len(lines1)):
		splitted_line1 = lines1[i]
		splitted_line2 = lines2[i]

		if len(splitted_line1) != len(splitted_line2):
			print "Alignment error on line " + str(i+1)
			exit()
		if len(splitted_line1) != max and len(splitted_line1) != min:
			print "Something is wrong at line " + str(i+1) + " in " + file1
			exit()
		if len(splitted_line2) != max and len(splitted_line2) != min:
			print "Something is wrong at line " + str(i+1) + " in " + file2
			exit()
		if len(splitted_line1) == max:
			if(splitted_line1[0] != splitted_line2[0]):
				print "Alignment error on line " + str(i+1)
				exit()
			target1 = splitted_line1[target]
			target2 = splitted_line2[target]					
			if(op=='dep'):
				target1 = target1 + "_" + splitted_line1[target + 1]
				target2 = target2 + "_" + splitted_line2[target + 1]
				
			out_file.write('a' + '\t' + str(i+1) + '\t' + target1 + '\n')
			out_file.write('b' + '\t' + str(i+1) + '\t' + target2 + '\n')
			if unify and splitted_line1[target] != splitted_line2[target]:
				print "Differences found at line " + str(i+1)
	out_file.close
	annotation(output)

def annotation(output):
	t = AnnotationTask(data=[x.split() for x in open(output)])
	print "\nAverage observed agreement: " + str(t.avg_Ao())
	print "\nKappa: " + str(t.kappa());
	

def main(argv):
	parser = argparse.ArgumentParser(description="Interannotator agreement", formatter_class=RawTextHelpFormatter)
	parser.add_argument("command", choices=('pos', 'dep'), help="pos for interannotator agreement on pos\ndep interannotator agreement on dependencies")
	parser.add_argument("-u", "--unify", action='store_true', help="helps the annotators to unify the files in a single one")
	parser.add_argument("input1", help="one of the two files")
	parser.add_argument("input2", help="the other file")
	args = parser.parse_args()

	operation(args.input1, args.input2, args.command, args.unify)

	
			
if __name__ == "__main__":
    main(sys.argv)
