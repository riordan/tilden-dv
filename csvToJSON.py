import csv

reader = csv.reader(open("Tilden-Family.csv"))

for PARENT_STRUC_ID, PARENT_TITLE, TITLE, IMAGE_ID, IMAGE_PK, UUID, MSS_FILE_ID, MSS_FILE_ID, MSS_LOCATION in reader:
		print TITLE
