import os
import sys

import SimpleITK as sitk
from os import listdir
from os.path import isfile, join

# def resample(image, transform):
#     # Output image Origin, Spacing, Size, Direction are taken from the reference
#     # image in this call to Resample
#     reference_image = image
#     interpolator = sitk.sitkGaussian
#     default_value = 255.0
#     return sitk.Resample(image, reference_image, transform,
#                          interpolator, default_value)
# translation = sitk.TranslationTransform(3)
# translation.SetOffset((1.5, 1.5, 1.5))
# inputImage = sitk.ReadImage("C:/Users/Julia Scott/03 PreProcessing/IntensityNormalizationOutput/C3L-00599$$20030602$$1_IN.nii.gz")
# resampled = resample(inputImage, translation)
# sitk.WriteImage(resampled, "C:/Users/Julia Scott/03 PreProcessing/ReSampleOutput/output1.nii.gz")
# print( ' completed ')

# intensityImage =sitk.ReadImage('C:\\Users\\Julia Scott\\03 PreProcessing\\IntensityNormalizationOutput\\C3L-00599$$20030602$$1_IN.nii.gz')
#
# intensityImage =sitk.ReadImage('C:\\Users\\Julia Scott\\03 PreProcessing\\ReSampleOutput\\output1.nii.gz')
# print('Before Modification modification:')
# print('origin: ' + str(intensityImage.GetOrigin()))
# size = intensityImage.GetNumberOfComponentsPerPixel()
# print( "---------",intensityImage.GetWidth())
# print('size: ' + str(intensityImage.GetNumberOfComponentsPerPixel()) )
# print('spacing: ' + str(intensityImage.GetSpacing()))
# print('direction: ' + str(intensityImage.GetDirection()))
# print('pixel type: ' + str(intensityImage.GetPixelIDTypeAsString()))
# print('number of pixel components: ' + str(intensityImage.GetNumberOfComponentsPerPixel()))
# print('-----------------------------------------------------------------------------------------')
# selected_image =sitk.ReadImage('C:\\Users\\Julia Scott\\03 PreProcessing\\ReSampleOutput\\output1.nii.gz')
# print('After Modification modification:')
# print('origin: ' + str(selected_image.GetOrigin()))
# print('size: ' + str(selected_image.GetSize()))
# print('spacing: ' + str(selected_image.GetSpacing()))
# print('direction: ' + str(selected_image.GetDirection()))
# print('pixel type: ' + str(selected_image.GetPixelIDTypeAsString()))
# print('number of pixel components: ' + str(selected_image.GetNumberOfComponentsPerPixel()))

# center = ( intensityImage.GetWidth()//2, intensityImage.GetHeight()//2, intensityImage.GetDepth()//2)
mypath = "C:\\Users\\Julia Scott\\03 PreProcessing\\IntensityNormalizationOutput"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print( onlyfiles )