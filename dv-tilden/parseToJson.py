import csv

class Folder:
	def __init__(self,name, image):
		self.name = name
		self.images = [image]

	def addImage(self, image):
		self.images.append(image)
		#print "Added %s" %self.images[-1]

	def allImages(self):
		return images

class Series:
	def __init__(self,name):
		self.name = name
		self.folders = dict()

	def addImage(self,folderName, image):
		try:
			self.folders[folderName].addImage(image)
		except KeyError:
			self.folders[folderName]=  Folder(folderName, image)



def parseMetaData(reader):
	series = dict()
	for row in reader:
		parent_struc_id,parent_title,struc_id,title,image_id,image_pk,uuid,mss_file_id,title_1,mss_location = row

		try:
			series[parent_title].addImage(title, uuid)
		except KeyError:
			series[parent_title] =  Series(title)
			series[parent_title].addImage(title, uuid)
	return series



def writeJSON(outfile, seriesName, folders):
   b = open('base.js', 'r')
   baseString = b.read()
   b.close()
   f = open('output/'+outfile+".js", 'w')
   vt = open('tildenTemplateViewer.html', 'r')
   viewerTemplate = vt.read()
   vt.close()
   viewer = open('../tildenviewers/'+outfile+'.html','w')
   print seriesName
   print outfile
   tilView = viewerTemplate %(seriesName,outfile)
   viewer.write(tilView)
   viewer.close()
   # Get Folder List
   uuidList = []
   sectionList = []
   for folderName, folderImages in folders.iteritems():
      for i in folderImages.images:
         uuidList.append(i)
      sectionList.append((folderName, len(folderImages.images)))

   
   #Let's generate some sections up in this JSON!

   printSections = ""

   page = 1
   for s in sectionList:
      sName, sLen = s
      printSections += '''
      {
         "title":"%s",
         "page":%d
      },''' %(sName, page)
      page += sLen

   print printSections


   #Output to js file. Filename must align with ID paramater otherwise it'll reject
   f.write(baseString %(outfile, outfile, uuidList, printSections))
   f.close
   



csvfile = open('Tilden.csv','rb')
dialect = csv.Sniffer().sniff(csvfile.read(1024))
csvfile.seek(0)
reader = csv.reader(csvfile,dialect)
allSeries = parseMetaData(reader)

for series, folders in allSeries.iteritems():
	#print series
	#print folders
	writeJSON(series, series, folders.folders)


		






