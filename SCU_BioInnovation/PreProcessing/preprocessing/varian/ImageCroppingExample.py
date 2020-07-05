import SimpleITK as sitk
import SimpleITK as sitk
import sys

center = (256, 256, 97)


image =sitk.ReadImage('C:\\Users\\Julia Scott\\03 PreProcessing\\ReSampleOutput\\output1.nii.gz')
croppedImage = image[center[0]-63:center[0]+63, center[1]-57:center[1]+57, center[2]-71:center[2]+71]

sitk.WriteImage(croppedImage, "C:\\Users\\Julia Scott\\03 PreProcessing\\CroppedImage\\cropped.nii.gz")