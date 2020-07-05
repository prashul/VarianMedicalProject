
import os
import sys

import SimpleITK as sitk

def intensityNormalization(inputFilePath, outputFilePath):
    sitkImage = sitk.ReadImage(inputFilePath)
    normalizationFilter = sitk.IntensityWindowingImageFilter()
    normalizationFilter.SetOutputMaximum(255)
    normalizationFilter.SetOutputMinimum(0)
    print(normalizationFilter)
    outNormalization = normalizationFilter.Execute(sitkImage)
    sitk.WriteImage(outNormalization, outputFilePath)
    print("Info--File ", inputFilePath, " normalized to ", outputFilePath)


def readAllNiftiFilesFromInputDirectory(inputDirectoryPath):
    niftiFilesPath = []
    for inputDirectory in inputDirectoryPath:
        for currentpath, folders, files in os.walk(inputDirectoryPath):
            for file in files:
                if (file.endswith("nii.gz")):
                    niftiFilesPath.append(os.path.join(currentpath, file))

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

for niftiFile in niftiFilesPath:
    outputFileName = os.path.basename(niftiFile)
    intensityNormalization(input, outputFileName, os.path.join(outputDirectory, outputFileName))

print("Normalization Of Intensities Completed")