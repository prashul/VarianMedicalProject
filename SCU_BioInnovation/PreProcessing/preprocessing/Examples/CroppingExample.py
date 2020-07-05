import os
import sys
from os import listdir
from os.path import isfile, join
import SimpleITK as sitk


def croppingImages(inputFilePath, outputFilePath):
    sitkImage = sitk.ReadImage(inputFilePath)
    center = ( sitkImage.GetWidth()//2, sitkImage.GetHeight()//2, sitkImage.GetDepth()//2)
    image = sitk.ReadImage(inputFilePath)
    #10 TO 20 IN HEIGHT - 85 , FOR THE WIDTH IT WILL BE 120 .FOR THE Y AXIS MAKE IT 70
    croppedImage = image[center[0] - 63:center[0] + 63, center[1] - 57:center[1] + 57, center[2] - 71:center[2] + 71]
    sitk.WriteImage(croppedImage, outputFilePath)
    print("Info--File ", inputFilePath, " cropped to ", outputFilePath)


def readAllNiftiFilesFromInputDirectory(inputDirectoryPath):
    niftiFilesPath = []
    niftiFilesPath = [f for f in listdir(inputDirectoryPath) if isfile(join(inputDirectoryPath, f))]
    print(niftiFilesPath)
    return niftiFilesPath


def validInputParameters( sys ):
    length = len(sys.argv)
    print( 'Argumements passed ', length )

    if length == 3:
        return True
    return False

if validInputParameters( sys ) == False:
    print( 'Invalid Argumements' )
    sys.exit(0)

print('Input File Path name :', str(sys.argv[1]))
print('Output file path name :', (sys.argv[2]))

inputDirectoryPath = str(sys.argv[1])
outputDirectory = (sys.argv[2])

print("Reading all the files from ", inputDirectoryPath)

niftiFilesPath = readAllNiftiFilesFromInputDirectory(inputDirectoryPath)
print("Info--Input files present in Input Directory", inputDirectoryPath, "is ", len(niftiFilesPath))
print( niftiFilesPath )
for niftiFile in niftiFilesPath:
    outputFileName = niftiFile.split(".")
    outputFileName = outputFileName[0] + "_CR.nii.gz"
    croppingImages(os.path.join(inputDirectoryPath, niftiFile),os.path.join(outputDirectory, outputFileName))

print("Normalization Of Intensities Completed")