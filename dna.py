import re 
import csv
from sys import argv


# when we run the program in terminal with two arguments it will produce the list containing three fields name of python file,
# name of csv file, and name of txt file and we provide wrong input code will not execute
if len(argv) == 3:


	csv_name = argv[1]
	txt_file = argv[2]

	csv_header = None
	csv_data = []
	upper_case = "[ABCDEFGHIJKLMNOPQRSTUVWXYZ]"
	result = "No Match" # setting result to No Match

	#Reading CSV file DATA
	with open(csv_name, mode="r") as csv_file:

		csvreader = csv.reader(csv_file)
		csv_header = next(csvreader)

		for row in csvreader:
			if row: #eliminating any blank row
				csv_data.append(row)


	#Reading Text DATA
	with open(txt_file, "r") as t:
		txt = t.readline()


	#For Lrage CSV file
	if len(csv_header) > 4:

		#Counting AGATC
		ag = re.sub("AGATC", "9", txt)
		ag = re.split(upper_case, ag)
		AG = len(max(ag))

		#Counting TTTTTTCT
		tt = re.sub("TTTTTTCT", "9", txt)
		tt = re.split(upper_case, tt)
		TT = len(max(tt))

		#Counting AATG
		aa = re.sub("AATG", "9", txt)
		aa = re.split(upper_case, aa)
		AA = len(max(aa))


		#counting TCTAG
		tc = re.sub("TCTAG", "9", txt)
		tc = re.split(upper_case, tc)
		TC = len(max(tc))


		# counting GATA
		gt = re.sub("GATA", "9", txt)
		gt = re.split(upper_case, gt)
		GT = len(max(gt))


		#counting TATC
		ta = re.sub("TATC", "9", txt)
		ta = re.split(upper_case, ta)
		TA = len(max(ta))


		#counting GAAA
		ga = re.sub("GAAA", "9", txt)
		ga = re.split(upper_case, ga)
		GA = len(max(ga))


		# counting TCTG
		tg = re.sub("TCTG", "9", txt)
		tg = re.split(upper_case, tg)
		TG = len(max(tg))


		#Looping Over Large CSV data to find a match
		for row in csv_data:
			name, ag, tt, aa, tc, gt, ta, ga, tg = row

			if (int(ag) == AG) and (int(tt) == TT) and (int(aa) == AA) and (int(tc) == TC):
				if (int(gt) == GT) and (int(ta) == TA) and (int(ga) == GA) and (int(tg) == TG):
					result = name
					break

		print(result) #Output

	#for smallCSV file
	else:

		#counting AGATC
		ag = re.sub("AGATC", "9", txt)
		ag = re.split(upper_case, ag)
		AG = len(max(ag))

		#counting AATG
		aa = re.sub("AATG", "9", txt)
		aa = re.split(upper_case, aa)
		AA = len(max(aa))

		#counting TATC
		ta = re.sub("TATC", "9", txt)
		ta = re.split(upper_case, ta)
		TA = len(max(ta))


		#Looping Over Small CSV data to find a match
		for row in csv_data:
			name, ag, aa, ta = row

			if (int(ag) == AG) and (int(aa) == AA) and (int(ta) == TA):
				result = name
				break

		print(result) #Output


else:
	print("Invalid Input")