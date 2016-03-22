#!/usr/bin/python
import random, sys
from optparse import OptionParser


class comm:
	def __init__(self, ifile1, ifile2, istdset, suppress1, suppress2, suppress3, unsorted):
		self.file1 = ifile1
		self.file2 = ifile2
		self.stdset = istdset
		self.neg1 = suppress1
		self.neg2 = suppress2
		self.neg3 = suppress3
		self.negu = unsorted

	def compare(self):
		#following is for debugging uses
		"""print "file1 set to: " + str(self.file1)
		print "file2 set to: " + str(self.file2)
		print "stdset set to: " + str(self.stdset)
		print "suppression of line 1 set to: " + str(self.neg1)
		print "suppression of line 2 set to: " + str(self.neg2)
		print "suppression of line 3 set to: " + str(self.neg3)
		print "set for unsorted inputs = " + str(self.negu)"""
		
		#assign the proper string to each file
		if self.stdset == 0:
			f1 = open(self.file1,'r').read()
			f2 = open(self.file2,'r').read()
		elif self.stdset == 1:
			f1 = ""
			for line in sys.stdin:
				f1 += line
			f2 = open(self.file2,'r').read()
		elif self.stdset == 2:
			f1 = open(self.file1,'r').read()
			f2 = ""
			for line in sys.stdin:
				f2 += line

		#create a list of lines from file1(or stdin if applicable)
		buf = ""
		wc1 = 0
		list1 = []

		for i in range(0,len(f1)):
			if f1[i] == '\n':
				list1.append(buf)
				buf = ""
				wc1 += 1
			else:
				buf += f1[i]


		#create a list of lines from file2(or stdin if applicable)
		buf = ""
		wc2 = 0
		list2 = []

		for i in range(0,len(f2)):
			if f2[i] == '\n':
				list2.append(buf)
				buf = ""
				wc2 += 1
			else:
				buf += f2[i]
		"""
		print "contents of list1, size = " + str(wc1)
		for i in range(0,len(list1)):
			print str(i) + ' ' + str(list1[i])

		print "contents of list2, size = " + str(wc2)
		for i in range(0,len(list2)):
			print str(i) + ' ' + str(list2[i])
		"""
		if not self.negu:
			col1 = []
			col2 = []
			col3 = []
			list2c = list2
			#create a list of words that are common in both lists
			for line1 in list1:
				size2c = len(list2c)
				it2c = 0
				if size2c==0:
					col1.append(line1)
				for line2 in list2c:
					it2c += 1
					if line2 == line1:
						col3.append(line1)
						list2c.remove(line2)
						break
					elif it2c == size2c:
						col1.append(line1)




			col2 = list2c
			"""
			print "col3 list: "
			for item in col3:
				print item

			print "col2 list: "
			for item in col2:
				print item

			print "col1 list: "
			for item in col1:
				print item
			"""
			#final output
			output = ""
			size1 = len(col1)
			size2 = len(col2)
			size3 = len(col3)
			it1=0
			it2=0
			it3=0


			for x in range(0,(size1 + size2 + size3)):
				if (it1 < size1):
					temp1 = col1[it1]
				else:
					temp1 = None
				if (it2 < size2):
					temp2 = col2[it2]
				else:
					temp2 = None
				if (it3 < size3):
					temp3 = col3[it3]
				else:
					temp3 = None

				if temp1 == None:
					if temp2 == None:
						if not self.neg3:
							output += ('                ' + temp3 + '\n')
						it3 += 1
						continue
					elif temp3 == None:
						if not self.neg2:
							output += ('        ' + temp2 + '\n')
						it2 += 1
						continue
					if (temp2 < temp3):
						if not self.neg2:
							output += ('        ' + temp2 + '\n')
						it2 += 1
						continue
					else:
						if not self.neg3:
							output += ('                ' + temp3 + '\n')
						it3 += 1
						continue
				if temp2 == None:
					if temp1 == None:
						if not self.neg3:
							output += ('                ' + temp3 + '\n')
						it3 += 1
						continue
					elif temp3 == None:
						if not self.neg1:
							output += (temp1 + '\n')
						it1 += 1
						continue
					if (temp1 < temp3):
						if not self.neg1:
							output += (temp1 + '\n')
						it1 += 1
						continue
					else:
						if not self.neg3:
							output += ('                ' + temp3 + '\n')
						it3 += 1
						continue
				if temp3 == None:
					if temp2 == None:
						if not self.neg1:
							output += (temp1 + '\n')
						it1 += 1
						continue
					elif temp1 == None:
						if not self.neg2:
							output += ('        ' + temp2 + '\n')
						it2 += 1
						continue
					if (temp1 < temp2):
						if not self.neg1:
							output += (temp1 + '\n')
						it1 += 1
						continue
					else:
						if not self.neg2:
							output += ('        ' + temp2 + '\n')
						it2 += 1
						continue

				if temp1 < temp2:
					if temp1 < temp3:
						if not self.neg1:
							output += (temp1 + '\n')
						it1+=1
						continue
					else:
						if not self.neg3:
							output += ('                ' + temp3 + '\n')
						it3+=1
						continue
				elif temp2 < temp3:
					if not self.neg2:
						output += ('        ' + temp2 + '\n')
					it2+=1
					continue
				else:
					if not self.neg3:
						output += ('                ' + temp3 + '\n')
					it3+=1
					continue
 
		else:
			col1 = []
			col2 = []
			col3 = []
			list2c = list2
			#create a list of words that are common in both lists
			for line1 in list1:
				size2c = len(list2c)
				it2c = 0
				if size2c==0:
					col1.append(line1)
				for line2 in list2c:
					it2c += 1
					if line2 == line1:
						col1.append(('                ' + line1))
						list2c.remove(line2)
						break
					elif it2c == size2c:
						col1.append(line1)
			
			col2 = list2c

			output = ""

			for item in col1:
				num = 1
				try:
					if item[15] == ' ':
						num = 3
				except:
					num=1

				if num == 3:
					if not self.neg3:
						output += (item + '\n')
				else:

					if not self.neg1:
						output += (item + '\n')

			for item in col2:
				if not self.neg2:
					output += ('        ' + item + '\n')




		sys.stdout.write(output)


	

def main():
	version_msg = "%prog 2.0"
	usage_msg = """%prog [OPTION]... FILE1 [FILE2]"""

	parser = OptionParser(version=version_msg, usage=usage_msg)

	parser.add_option("-u",action="store_true",dest="unsorted",default=False,help="Specify if files are unsorted (Default False)")

	parser.add_option("-1",action="store_true",dest="suppress1",default=False,help="Choose to suppress column 1 from output (Default False)")

	parser.add_option("-2",action="store_true",dest="suppress2",default=False,help="Choose to suppress column 2 from output (Default False)")

	parser.add_option("-3",action="store_true",dest="suppress3",default=False,help="Choose to suppress column 3 from output (Default False)")

	options, args = parser.parse_args(sys.argv[1:])

	if len(args) != 2:
		sys.stderr.write("invalid number of inputs")
		sys.exit(1)

	file1 = args[0]
	file2 = args[1]

	if file1 == "-":
		if file2 == "-":
			sys.stderr.write("Undefined behavior, both files set to standard input")
			sys.exit(2)
		else:
			stdset = 1
	elif file2 == "-":
		stdset = 2
	else:
		stdset = 0

	generator = comm(file1,file2,stdset,options.suppress1,options.suppress2,options.suppress3,options.unsorted)
	generator.compare()



if __name__ == "__main__":
	main()
