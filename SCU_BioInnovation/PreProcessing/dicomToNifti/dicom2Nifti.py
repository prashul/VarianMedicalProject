import dicom2nifti.convert_dicom as convert_dicom
import os
import pydicom
import dicom2nifti
from dicom2nifti import settings


def getAllDCMFiles( inputDirectories ):
    dcmFiles=[]
    for inputDirectory in inputDirectories:
      #  print( inputDirectory )
        for currentpath, folders, files in os.walk(inputDirectory):
            for file in files:
                #print( file )
                if( file.endswith(".dcm") ):
                    dcmFiles.append(os.path.join(currentpath, file) )

    return dcmFiles

def extractMetaDataDetails( dcmFiles ):
    noOfFiles = len(dcmFiles)
    mapOfDetails = {}
    i = 0
    for j in range(noOfFiles):

        filePath = dcmFiles[j]
        folderPath = filePath[0:filePath.rindex('\\')]

        if (folderPath in mapOfDetails):
            continue

        try:
            ds = pydicom.filereader.dcmread(filePath)
        except:
            continue
      #  print( ds )
        paitentName = str( ds[0x0010,0x0010].value )
        studyDate = str(ds[0x0008, 0x0020].value)
        mapOfDetails[folderPath] = paitentName + "$$" + studyDate

    return mapOfDetails

def convertDicom2Nifti( inputFiles,outputDirectory ):
    mapOfFileNames = {}
    settings.disable_validate_orientation()
    settings.disable_validate_orthogonal()
    settings.disable_validate_slice_increment()
  //  settings.disable_validate_instance_number()
    settings.disable_validate_slicecount()
    for key in inputFiles:
        dicomFolderPath = key
        outputFileName = inputFiles[ key ];
        if (outputFileName in mapOfFileNames):
            fileNo = mapOfFileNames[ outputFileName]
            mapOfFileNames[outputFileName] = fileNo + 1
        else:
            mapOfFileNames.setdefault(outputFileName, 1)

        outputFileName = outputFileName + "$$" + str(mapOfFileNames[ outputFileName])
        print('***', dicomFolderPath)
        print('--', outputDirectory, outputFileName)
        outputFileName = outputFileName + ".nii.gz"
        try:
            convert_dicom.dicom_series_to_nifti(key, os.path.join(outputDirectory, outputFileName),
                                              False)
        except dicom2nifti.exceptions.ConversionValidationError:
            print( " Error for file outputFileName", outputFileName )

    print( 'completed' )

def readFromTextFile( inputFilePath):
    inputFilesList = []
    file1 = open(inputFilePath, 'r')
    lines = file1.readlines()
    count = 0
    # Strips the newline character
    for line in lines:
        inputFilesList.append( line.strip() )

    return inputFilesList

def validInputParameters( sys ):
    length = len(sys.argv)
    print( 'Argumements passed ', length )

    if length == 3:
        return True
    return False

if validInputParameters( sys ) == False:
    print( 'Invalid Argumements' )
    sys.exit(0)

print ('Input File Path name :', str(sys.argv[1]))
print ('Output file path name :', (sys.argv[2]))

inputFilePath = str(sys.argv[1])
outputDirectory = str(sys.argv[2])
inputDirectories = readFromTextFile( inputFilePath )
dcmFiles = getAllDCMFiles( inputDirectories )
print( dcmFiles )
mapOfDetails = extractMetaDataDetails( dcmFiles )
print( mapOfDetails )
convertDicom2Nifti(mapOfDetails,outputDirectory)

