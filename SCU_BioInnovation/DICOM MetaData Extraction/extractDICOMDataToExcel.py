# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import xlwt 
from xlwt import Workbook 
import os.path
import sys
from datetime import datetime

import pydicom
from pydicom.data import get_testdata_files


def createWorkBook( ):
       
    # Workbook is created 
    wb = Workbook() 
    
    # Writing to an excel  
    # sheet using Python 
      
    # Workbook is created 
    wb = Workbook() 
      
    # add_sheet is used to create sheet. 
    newSheet = wb.add_sheet('Sheet 1') 
    
    excelHeader = ['Patient Name','Modality','Study Date','Series Date', 'Acquisition Date', 'Contrast', 'Patient Position', 'Anatomic metadata','Implant Name', 'Implant Part Number', 'File Location' ]
    
    for i in range(0,len(excelHeader) ):
        newSheet.write( 0, i, excelHeader[ i ] ) 

    return newSheet,wb

def writeToExcel( files, sheet, excelFile,wb ):
    print( 'Writing Metadata to Excel File' )
    noOfFiles = len( files )
    hashMap = {}
    i=0
    for j in range( noOfFiles ):
        
       # print( files[i] )
        directoryName = files[j].split('\\')
       # print( directoryName[ len(directoryName)-2 ] )
        
        try:
            ds = pydicom.filereader.dcmread(files[j])
        except :
            continue
            
        string = files[j]
        folderStructure = string[0:string.rindex('\\')]
        #print( folderStructure )
        if( folderStructure in hashMap ):
            continue
        
        hashMap[ folderStructure ] = True  
        
        try:
           # print( ds )
            sheet.write( i+1,0, str( ds[0x0010,0x0010].value ) )#PatientName
        except KeyError:
            pass
        
        try:
            sheet.write( i+1,1, str( ds[0x0008,0x0060].value ) )#Modality
        except KeyError:
            pass
        
        try:
            #print( datetime.strptime(str( ds[0x0008,0x0020].value ), '%Y%m%d').date().isoformat()  )
            sheet.write( i+1,2, float( ds[0x0008,0x0020].value ) )#Study Date
            #sheet.write( i+1,2, datetime.strptime(str( ds[0x0008,0x0020].value ), '%Y%m%d').date().isoformat() )#Study Date
        except KeyError:
            pass
    
        try:
            sheet.write( i+1,3, float( ds[0x0008,0x0021].value ) )#Series Date
        except KeyError:
            pass
        
        try:
            acquistionDate = ""
            if not acquistionDate:
                sheet.write( i+1,4, float( ds[0x0008,0x0022].value ) )#Acquisition Date
            else:
                sheet.write( i+1,4,-1 )
        except KeyError:
            pass
        
        try:
            flag = contrastPresent( ds )
            sheet.write( i+1,5, flag )#Contrast
        except KeyError:
            pass
         
        try:
            sheet.write( i+1,6, str( ds[0x0008,0x5100].value ) )#Patient Position	
        except KeyError:
            pass
             
        try:
            value = getAnatomicMetaData( ds )
            sheet.write( i+1,7, value )#Anatomic metadata
        except KeyError:
            pass
        
        try:
            sheet.write( i+1,8, str( ds[0x0022,0x1095].value ) )#Implant Name	
        except KeyError:
            pass
        
        try:
            sheet.write( i+1,9, str( ds[0x0022,0x1097].value ) )#Implant Part Number
        except KeyError:
            pass
        
        sheet.write( i+1,10, folderStructure )#folder structure
        
        i = i + 1
        
    wb.save(excelFile) 

        
def getFilesFromDiacomDirectory( directory ):
    print('Reading Files From Diacom Directory')
    filepath = pydicom.data.get_testdata_files(directory)
    return filepath

def getAnatomicMetaData( ds ):
    val = ''
    try:
        val = val + str( ds[0x0018,0x2218].value )
        val = val + str( ds[0x0018,0x2220].value )
        val = val + str( ds[0x0018,0x2228].value )
        val = val + str( ds[0x0018,0x2229].value )
        val = val + str( ds[0x0018,0x2230].value )
    except KeyError: 
        pass         
    return val

def contrastPresent( ds ):
    flag = False
    try:
        par1 = str( ds[0x0018,0x0010].value )#Contrast/Bolus Agent
        flag = True
        par2 = str( ds[0x0018,0x0012].value )#Contrast/Bolus Agent
        flag = True
        par3 = str( ds[0x0018,0x0013].value )#Contrast/Bolus Agent
        flag = True
        par4 = str( ds[0x0018,0x0014].value )#Contrast/Bolus Agent
        flag = True
    except KeyError: 
        pass
    return flag
                        
def validInputParameters( sys ):
    length = len(sys.argv)
    print( 'Argumements passed ', length )

    if length == 3:
        return True
    return False
    
sheet,wb = createWorkBook()

if validInputParameters( sys ) == False:
    print( 'Invalid Argumements' )
    sys.exit(0)

print ('Input Directory name :', str(sys.argv[1]))
print ('Output file path name :', (sys.argv[2]))

files = getFilesFromDiacomDirectory( str(sys.argv[1]) )

writeToExcel( files,sheet, (sys.argv[2]),wb )

print("***Metadata extraction completed***")
