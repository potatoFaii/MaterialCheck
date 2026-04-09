# -*- coding: utf-8 -*-
import maya.cmds as cmds
import maya.mel as mel
from PySide2 import QtWidgets, QtGui
import re
import sys
import os

class MaterialCheck_Func(object):
    def __init__(self, *args):
        self.windowMaterialCheck(self, *args)

    def windowMaterialCheck(self, *args):
        checkWindows = "MaterialListCHECK"
        if (cmds.window(checkWindows ,q=True, exists = True)):
            cmds.deleteUI(checkWindows,window=True)
        cmds.window(checkWindows,t="Material_List_CHECK",menuBar=True,tlb=False,rtf=True,mnb=False,mxb=False,widthHeight=(350,630))
        cmds.menu(l='File')
        cmds.menuItem(divider=True)
        cmds.menuItem(l='VideoTutorial',en=True,c=lambda x:self.tutorial())
        cmds.menu(l='Reload')
        cmds.menuItem(l='Reload UI',c=lambda x:self.MaterialCheckReloadSub())
        #
        OrigMainForm = cmds.formLayout(numberOfDivisions = 100)

        # FirstLayout #
        fMainForm = cmds.formLayout(p=OrigMainForm)
        cmds.formLayout(OrigMainForm, edit=True, attachForm=[(fMainForm, "top", 10),(fMainForm, "left",15),(fMainForm, "right",15)])
        
        # FrameLayout
        importTutorialText = cmds.text(l='1. Select .ma/.py/.txt to FUNCTION',en=True)
        importTutorialTextUnderline = cmds.text(l='______________________________________________',align="center",en=True,fn='smallPlainLabelFont')
        textFieldImport = cmds.textFieldButtonGrp(l="ImportPath :",w=2,adj=2,bl=" ... ",bc=lambda :self.textFieldImportF(textFieldImport))
        newImportBtn = cmds.button(l='< Import >',c=lambda x:self.ImportFile_script(textScrollLists1,ScrollList1,textFieldImport))
        inputBtn = cmds.button(l='< Input/Refresh >',c=lambda x:self.inputMaterialList(textScrollLists2,ScrollList2,unmatched2List,frame_layout2))
        topSep = cmds.separator(style='double')
        fPublish = cmds.frameLayout(l="Current", labelAlign="center",collapsable=False, marginWidth=1, marginHeight=1,bgc=(0.315,0.354,0.465))
        cmds.setParent('..')
        fCurrent = cmds.frameLayout(l="Source", labelAlign="center",collapsable=False, marginWidth=1, marginHeight=1,bgc=(0.315,0.354,0.465))
        cmds.setParent('..')
        fframeSep = cmds.separator(style="in")
        multSelect1 = cmds.checkBox(l="[ Multiple ]",v=True,bgc=(0.4,0.3,0.3),cc=lambda x:self.mselPublish(multSelect1,textScrollLists1,textScrollLists2))
        ScrollList1 = cmds.text(l='number: 0/0')
        ScrollList2 = cmds.text(l='number: 0/0')
        cmds.formLayout(fMainForm, edit=True,attachControl=[(textFieldImport,'top',5,importTutorialText),
                                                            (newImportBtn,'top',5,textFieldImport),
                                                            (inputBtn,'top',5,textFieldImport),
                                                            #
                                                            (topSep,'top',5,newImportBtn),
                                                            (fPublish,'top',0,topSep),
                                                            (fCurrent,'top',0,topSep),
                                                            (fframeSep,'top',0,fPublish),
                                                            #
                                                            (multSelect1,'top',2,fframeSep),
                                                            (ScrollList1,'top',5,fframeSep),
                                                            (ScrollList2,'top',5,fframeSep),],
                                              attachForm=[(importTutorialText,'top',0),(importTutorialText,'left',0),(importTutorialTextUnderline,'top',3),
                                                          (textFieldImport,'left',-75),(textFieldImport,'right',0),
                                                          (newImportBtn,'left',0),(newImportBtn,'right',0),
                                                          (inputBtn,'left',0),(inputBtn,'right',0),
                                                          #
                                                          (topSep,'left',0),(topSep,'right',0),
                                                          (fPublish,'left',0),(fPublish,'right',0),
                                                          (fCurrent,'left',0),(fCurrent,'right',0),
                                                          (fframeSep,'left',0),(fframeSep,'right',0),
                                                          #
                                                          (multSelect1, "left", 2),
                                                          (ScrollList2, "right", 15)],
                                          attachPosition=[(inputBtn, "left", 3, 50),(newImportBtn, "right", 3, 51),
                                                          (fPublish, "left", 3, 50),(fCurrent, "right", 3, 51),
                                                          (ScrollList1, "right", 3, 50)])
        cmds.setParent('..')

        #=========================================PaneLayout=========================================
        Orig1 = cmds.formLayout(p=OrigMainForm)
        cmds.formLayout(OrigMainForm, edit=True,attachControl=[(Orig1,'top',-2,fMainForm)], 
                                                   attachForm=[(Orig1,'left',5),(Orig1,'right',5)])
        SMainForm = cmds.formLayout(p=Orig1)
        paneLayouts1 = cmds.paneLayout(configuration='quad',api=10,st=10,p=SMainForm)
        textScrollLists1 = cmds.textScrollList(h=180,width=50,allowMultiSelection=True)
        textScrollLists2 = cmds.textScrollList(h=180,width=50,allowMultiSelection=True,dcc=lambda :self.getSelected(textScrollLists2))

        # Create the paneLayout
        put1 = cmds.paneLayout(configuration='vertical2', parent=paneLayouts1)
        # Create frame_layout1 and position it in p3
        frame_layout1 = cmds.frameLayout(label="unmatched", labelAlign="center", collapsable=True,cl=True,en=False, marginWidth=1, marginHeight=1, p=put1)
        unmatched1List = cmds.textScrollList(h=150,allowMultiSelection=True)
        frame_layout2 = cmds.frameLayout(label="unmatched", labelAlign="center", collapsable=True,cl=True,en=False, marginWidth=1, marginHeight=1, p=put1)
        unmatched2List = cmds.textScrollList(h=150,allowMultiSelection=True,dcc=lambda :self.getSelected(unmatched2List))
        cmds.paneLayout(paneLayouts1,edit=True,sp=[(textScrollLists1,1), (textScrollLists2, 2)])
        cmds.formLayout(Orig1, edit=True, attachForm=[(SMainForm, "top", 0),(SMainForm, "left", 5),(SMainForm, "right", 5)])
        cmds.formLayout(SMainForm, edit=True, attachForm=[(paneLayouts1, "top", 5),(paneLayouts1, "left", 5),(paneLayouts1, "right", 5)])
        cmds.setParent('..')
        cmds.setParent('..')
        cmds.setParent('..')
        cmds.setParent('..')

        #=========================================SecondLayout=========================================
        TMainForm = cmds.formLayout(p=Orig1)
        cmds.formLayout(Orig1, edit=True,attachControl=[(TMainForm,'top',0,SMainForm)],
                                            attachForm=[(TMainForm, "left", 5),(TMainForm, "right", 5)])
        TMainText = cmds.text(l="** Number of Differences Between Both Lists",en=False)
        TMainSep = cmds.separator(style='double')
        #
        clearPublish = cmds.button(l=' ^ Clear ',h=18,bgc=(0.3,0.4,0.4),c=lambda x:self.clearSelectionPublish(textScrollLists1,unmatched1List))
        clearCurrent = cmds.button(l=' ^ Clear ',h=18,bgc=(0.3,0.4,0.4),c=lambda x:self.clearSelectionCurrent(textScrollLists2,unmatched2List))
        clearSep = cmds.separator(style='double')
        #
        compareBtn = cmds.button(l='CLICK TO COMPARE',bgc=(0.5,0.3,0.3),h=30,c=lambda x:self.compareMaterial(textScrollLists1,textScrollLists2,ScrollList1,ScrollList2,frame_layout1,frame_layout2,unmatched1List,unmatched2List))
        TMainSep2 = cmds.separator(style='double')

        #Forth
        Ftitle = cmds.text(l='-EDIT-')
        Ftitle2 = cmds.text(l='-EDIT-')
        FtitleUnderLine = cmds.text(l='_____________',fn='smallPlainLabelFont')
        FchangeNButtonGuide = cmds.button(l='?',w=20,c=lambda x:self.guide_list())
        FchangeNButton = cmds.button(l='--> Transfer_Name',c=lambda x:self.NameChange(textScrollLists1,textScrollLists2,ScrollList1,ScrollList2,frame_layout1,frame_layout2,unmatched1List,unmatched2List))
        Fsep = cmds.separator(style='double')
        cmds.formLayout(TMainForm, edit=True,attachControl=[(TMainSep,'top',5,TMainText),
                                                            (clearPublish,'top',2,TMainSep),
                                                            (clearCurrent,'top',2,TMainSep),
                                                            (clearSep,'top',2,clearCurrent),
                                                            #
                                                            (compareBtn,'top',2,clearSep),
                                                            (TMainSep2,'top',2,compareBtn),
                                                            #
                                                            (Ftitle,'top',2,TMainSep2),
                                                            (Ftitle2,'top',3,TMainSep2),
                                                            (FtitleUnderLine,'top',-8,Ftitle2),
                                                            #
                                                            (FchangeNButton,'top',5,FtitleUnderLine),
                                                            (FchangeNButtonGuide,'top',5,FtitleUnderLine),
                                                            #
                                                            (FchangeNButtonGuide,'right',5,FchangeNButton),
                                                            (Fsep,'top',5,FchangeNButtonGuide),], 
                                                attachForm=[(TMainText, "top", 0),(TMainText, "right", 10),
                                                            (TMainSep, "left", 0),(TMainSep, "right", 0),
                                                            (clearPublish, "left", 5),(clearPublish, "right", 5),
                                                            (clearCurrent, "left", 5),(clearCurrent, "right", 5),
                                                            (clearSep, "left", 0),(clearSep, "right", 0),
                                                            (compareBtn, "left", 5),(compareBtn, "right", 5),
                                                            #
                                                            (TMainSep2, "left", 0),(TMainSep2, "right", 0),
                                                            (Ftitle, "left", 5),(Ftitle, "right", 5),
                                                            (Ftitle2, "left", 5),(Ftitle2, "right", 5.5),
                                                            (FtitleUnderLine, "left", 5),(FtitleUnderLine, "right", 5),
                                                            (FchangeNButton, "left", 50),(FchangeNButton, "right", 5),
                                                            (Fsep, "left", 5),(Fsep, "right", 5)],
                                            attachPosition=[(clearPublish, "right", 0, 50),(clearCurrent, "left", 0, 51)])

        newFLayout = cmds.frameLayout(l="Data_Import/Export", labelAlign="center", collapsable=True,cl=False,en=True, marginWidth=1, marginHeight=1,bgc=(0.35,0.35,0.35))
        cmds.formLayout(TMainForm, edit=True,attachControl=[(newFLayout,'top',5,Fsep)], 
                                                attachForm=[(newFLayout,"left", 5),(newFLayout, "right", 5)])
        IEForm = cmds.formLayout(bgc=(0.25,0.25,0.25))
        textFieldExport = cmds.textFieldButtonGrp(l="ExportPath :",w=1,adj=2,bl=" ... ",bc=lambda :self.textFieldExportF(textFieldExport))
        exportBtn = cmds.button(l='Export',bgc=(0.3,0.3,0.3),c=lambda x:self.ExportData_execute_script(textFieldExport))
        dataSepLeft = cmds.separator(style='double',hr=False,h=75)
        dataSepRight = cmds.separator(style='double',hr=False,h=75)
        dataSepBot = cmds.separator(style='double')
        cmds.formLayout(IEForm,edit=True,attachControl=[(exportBtn,'top',5,textFieldExport),
                                                        (dataSepBot,'top',10,exportBtn)],
                                            attachForm=[(textFieldExport,'top',10),(textFieldExport,'left',-65),(textFieldExport,'right',10),
                                                        (exportBtn, "left", 0),(exportBtn, "right", 15),
                                                        (dataSepLeft, "top", 0),(dataSepLeft, "left", 0),
                                                        (dataSepRight, "top", 0),(dataSepRight, "right", 0),
                                                        (dataSepBot, "left", 0),(dataSepBot, "right", 0)],
                                        attachPosition=[(exportBtn, "left", 0, 40)])

        last_sep = cmds.separator(style='none',p=TMainForm)
        cmds.formLayout(TMainForm, edit=True,attachControl=[(last_sep,'top',20,newFLayout)])
        
        cmds.showWindow(checkWindows)




#=========================================Function=========================================#

    def MaterialCheckReloadSub(self):
        MaterialCheck_Func()

    def tutorial(self):
        script_dirP = os.path.dirname(os.path.abspath(__file__))
        script_dirP = script_dirP.replace("IndivPyMaterialCheck","Tutorial")
        os.startfile(script_dirP)

    def ExportData_execute_script(self,textFieldExport): #open scriptList
        #select .txt/.py file
        exportPath = cmds.textFieldButtonGrp(textFieldExport,q=True,tx=True)
        if exportPath:
            listExport = [] # append all data here for export
            default_extension = "py"
            singleFilter = "Python Files (*.%s);;All Files (*.*)" % default_extension
            script_file = cmds.fileDialog2(fileFilter=singleFilter,dialogStyle=2,fileMode=0,dir=exportPath)
            if script_file:
                script_file = script_file[0]
                # Ensure the file has the .py extension
                if not script_file.endswith(".%s" % default_extension):
                    script_file += ".%s" % default_extension
                # Create a Python script from the list
                # Organise 
                materials_set = set()
                # Add materials to the set
                materials = cmds.ls(mat=True)
                materials_set.update(materials)
                materialList = [str(mat) for mat in materials_set]
                materials_sorted = sorted(materialList) #sorted alphabet
                listExport.append(materials_sorted)
                script_content ='\n'.join(materials_sorted)
                # Save the script as a .py file
                try:
                    with open(script_file, 'w') as script_file:
                        script_file.write(script_content)
                    cmds.confirmDialog(title='Success', message='Script exported successfully!', button=['OK'])
                except IOError as e:
                    cmds.error("Error: Failed to export script - %s" % e)
                    return
        else:
            cmds.warning('No file path provided')
            return

    def ImportFile_script(self,textScrollLists1,ScrollList1,textFieldImport):
        # Open a file dialog to select a .ma file
        importPath = cmds.textFieldButtonGrp(textFieldImport,q=True,tx=True)
        cmds.textScrollList(textScrollLists1,e=True,ra=True)
        # Check the filePath whether .py/.txt or .ma
        if importPath:
            if importPath[-3:] == '.ma':
                materials_set = set()
                # Read the contents of the selected .ma file
                with open(importPath, 'r') as file:
                    importPath = file.read()
                # Find all materials in the file
                material_assignments = re.findall(r'createNode (\w+) -n "([^"]+)"', importPath)  # Use regular expressions to find material assignments
                
                #material_nodes = [node[1] for node in material_assignments if node[0] == "lambert" or node[0] == "blinn" or node[0] == "phong" or node[0] == "aiStandardSurface"] # Filter for material nodes
                valid_material_types = set([
                    # Maya
                    "lambert", "blinn", "phong", "phongE", "surfaceShader", "useBackground",

                    # Arnold
                    "aiStandardSurface", "aiStandardHair", "aiStandardVolume",
                    "aiToon", "aiSkin", "aiShadowMatte", "aiRaySwitch",

                    # Legacy
                    "layeredShader", "rampShader", "anisotropic"
                ])
                material_nodes = [node[1] for node in material_assignments if node[0] in valid_material_types]
                
                # Print the material names
                for material in material_nodes:
                    materials_set.add(material)
                if materials_set:
                    #manual add
                    materials_set.add("lambert1")
                    materials_set.add("standardSurface1")
                    materials_set.add("particleCloud1")
                    materials_sorted = sorted(list(materials_set))
                    for materials in materials_sorted:
                        cmds.textScrollList(textScrollLists1,e=True,append=materials)
                    checkNumP = cmds.textScrollList(textScrollLists1,q=True,ni=True)
                    cmds.text(ScrollList1,e=True,label='number: {}/{}'.format(checkNumP,checkNumP))
                    mel.eval( 'print ("Result : FILE data import <SUCCESS> ")')
                else:
                    print("No materials found in the selected .ma file.")
            else:
                QGuideText = ''  # Initialize with a default value
                if os.path.isfile(importPath):
                    try:
                        with open(importPath, 'r') as file:
                            QGuideText = file.read()
                    except IOError:
                        QGuideText = 'Error: Failed to load Q guide.'
                else:
                    cmds.error("Script file not found")
                    return
                my_list = None
                apple = None
                lines = QGuideText.split('\n')
                # Iterate through each line
                for a,line in enumerate(lines):
                    if len(lines[0]) == 0: #possible nothing
                        cmds.warning('.py no DATA')
                        None
                    else:
                        cmds.textScrollList(textScrollLists1,e=True,append=line)
                checkNumP = cmds.textScrollList(textScrollLists1,q=True,ni=True)
                cmds.text(ScrollList1,e=True,label='number: {}/{}'.format(checkNumP,checkNumP))
                mel.eval( 'print ("Result : data import <SUCCESS> ")')
        else:
            cmds.warning('No file path provided')
            return

    def mselPublish(self,multSelect1,textScrollLists1,textScrollLists2):
        cbValue = cmds.checkBox(multSelect1,q=True,v=True)
        cmds.textScrollList(textScrollLists1,e=True,allowMultiSelection=cbValue)
        cmds.textScrollList(textScrollLists2,e=True,allowMultiSelection=cbValue)

    def getSelected(self,textScroll):
        sel = cmds.textScrollList(textScroll,query=True,selectItem=True)
        cmds.select(sel)

    def clearSelectionPublish(self,textScrollLists1,unmatched1List):
        cmds.textScrollList(textScrollLists1,e=True,da=True)
        cmds.textScrollList(unmatched1List,e=True,da=True)
        
    def clearSelectionCurrent(self,textScrollLists2,unmatched2List):
        cmds.textScrollList(textScrollLists2,e=True,da=True)
        cmds.textScrollList(unmatched2List,e=True,da=True)

    def inputMaterialList(self,textScrollLists2,ScrollList2,unmatched2List,frame_layout2):
        cmds.frameLayout(frame_layout2,edit=True,cl=True,en=False,bgc=(0.4,0.4,0.4))
        cmds.textScrollList(textScrollLists2,e=True,ra=True) #clear all textScrollList
        cmds.textScrollList(unmatched2List,e=True,ra=True)
        # Organise 
        materials_set = set()
        # Add materials to the set
        materials = cmds.ls(mat=True)
        materials_set.update(materials)
        materialList = [str(mat) for mat in materials_set]
        materials_sorted = sorted(materialList) #sorted alphabet

        cmds.textScrollList(textScrollLists2,e=True,append=materials_sorted)
        checkNum = cmds.textScrollList(textScrollLists2,q=True,ni=True)
        cmds.text(ScrollList2,e=True,label='number: {}/{}'.format(checkNum,checkNum))

    def materialCheck(self,textList1,textList2,textNum,unmatchedFrameL,textListUnmatched,selNoExist=None):
        Publish = cmds.textScrollList(textList1,query=True,allItems=True)
        Current = cmds.textScrollList(textList2,query=True,allItems=True) #list item
        checkNum = cmds.textScrollList(textList1,q=True,ni=True)
        listExist = []
        listNoExist = []
        if selNoExist is None:
            selNoExist = []  # Initialize the list if it's not provided
        CurrentSel = cmds.textScrollList(textList2,q=True,si=True)
        if CurrentSel:
            for item in CurrentSel:
                if item in Publish:
                    cmds.textScrollList(textList1,e=True,si=item)
                else:
                    selNoExist.append(item)
        else:
            # Iterate through my_list
            for item in Publish:
                if item in Current:
                    listExist.append(item)
                else:
                    listNoExist.append(item)
        return listExist ,listNoExist ,checkNum ,selNoExist

    def compareMaterial(self,textScrollLists1,textScrollLists2,ScrollList1,ScrollList2,frame_layout1,frame_layout2,unmatched1List,unmatched2List):
        selNoExist1 = []
        resultPublish = self.materialCheck(textScrollLists1,textScrollLists2,ScrollList1,frame_layout1,unmatched1List,selNoExist1)
        selNoExist2 = []
        resultCurrent = self.materialCheck(textScrollLists2,textScrollLists1,ScrollList2,frame_layout2,unmatched2List,selNoExist2)
        #store the list first ,then assign the edit
        listPublishExist, listPublishNoExist, publishNum, publishSelNoExist = resultPublish #unpack ,separate variables
        listCurrentExist, listCurrentNoExist, currentNum, currentSelNoExist = resultCurrent

        unmatched1Num = cmds.textScrollList(unmatched1List,q=True,ni=True)
        unmatched2Num = cmds.textScrollList(unmatched2List,q=True,ni=True)
        totalP = publishNum + unmatched1Num
        totalC = currentNum + unmatched2Num
        publishSelCheck = cmds.textScrollList(textScrollLists1,q=True,si=True) #check selection
        currentSelCheck = cmds.textScrollList(textScrollLists2,q=True,si=True) #check selection
        if currentSelCheck: #if current got selection
            cmds.text(ScrollList1,e=True,bgc=(0.4,0,0),label='number: {}/{}'.format(len(publishSelCheck),totalP))
            cmds.text(ScrollList2,e=True,bgc=(0.4,0,0),label='number: {}/{}'.format(len(currentSelCheck),totalP))
            if len(publishSelCheck) == len(currentSelCheck):
                mel.eval( 'print ("Result : Selection <MATCH> ")')
            else:
                cmds.warning("Selection number <NO MATCH>")
        else: #no selection
            if listPublishNoExist:
                cmds.textScrollList(textScrollLists1,e=True,ra=True) #clear all textScrollList
                cmds.textScrollList(unmatched1List,e=True,ra=True)
                cmds.textScrollList(textScrollLists1,edit=True,append=listPublishExist) #exist
                cmds.textScrollList(unmatched1List,edit=True,append=listPublishNoExist) #noexist
                cmds.frameLayout(frame_layout1,edit=True,en=True,cl=False,bgc=(0.85,0.54,0.15))
                cmds.text(ScrollList1,e=True,bgc=(0.4,0,0),label='number: {}/{}'.format(len(listPublishExist),totalP))
            else:
                if len(listPublishExist)==totalP:
                    cmds.frameLayout(frame_layout1,edit=True,en=False,collapsable=True,cl=True,bgc=(0.4,0.4,0.4))
                    cmds.text(ScrollList1,e=True,bgc=(0,0.4,0),label='number: {}/{}'.format(len(listPublishExist),totalP))
                else:
                    cmds.text(ScrollList1,e=True,bgc=(0.4,0,0),label='number: {}/{}'.format(len(listPublishExist),totalP))
            if listCurrentNoExist:
                cmds.textScrollList(textScrollLists2,e=True,ra=True) #clear all textScrollList
                cmds.textScrollList(unmatched2List,e=True,ra=True)
                cmds.textScrollList(textScrollLists2,edit=True,append=listCurrentExist) #exist
                cmds.textScrollList(unmatched2List,edit=True,append=listCurrentNoExist) #noexist
                cmds.frameLayout(frame_layout2,edit=True,en=True,cl=False,bgc=(0.85,0.54,0.15))
                cmds.text(ScrollList2,e=True,bgc=(0.4,0,0),label='number: {}/{}'.format(len(listCurrentExist),totalC))
                cmds.warning("Material naming/number <DOESNT MATCH>")
            else:
                if len(listCurrentExist)==totalC:
                    cmds.frameLayout(frame_layout2,edit=True,en=False,collapsable=True,cl=True,bgc=(0.4,0.4,0.4))
                    cmds.text(ScrollList2,e=True,bgc=(0,0.4,0),label='number: {}/{}'.format(len(listCurrentExist),totalC))
                    mel.eval( 'print ("Result : everything <MATCH> ")')
                else:
                    cmds.text(ScrollList2,e=True,bgc=(0.4,0,0),label='number: {}/{}'.format(len(listCurrentExist),totalC))
                    cmds.warning("Material naming/number <DOESNT MATCH>")

    def NameChange(self,textScrollLists1,textScrollLists2,ScrollList1,ScrollList2,frame_layout1,frame_layout2,unmatched1List,unmatched2List):
        print1A = cmds.textScrollList(unmatched1List,q=True,si=True)
        print2A = cmds.textScrollList(unmatched2List,q=True,si=True)
        cmds.select(print2A)
        sel = cmds.ls(sl=True)
        cmds.rename(sel,print1A)
        #reshuffle
        cmds.textScrollList(unmatched1List, edit=True, removeItem=print1A) #Remove the selected item
        cmds.textScrollList(textScrollLists1,edit=True,append=print1A)
        self.inputMaterialList(textScrollLists2,ScrollList2,unmatched2List,frame_layout2)
        self.compareMaterial(textScrollLists1,textScrollLists2,ScrollList1,ScrollList2,frame_layout1,frame_layout2,unmatched1List,unmatched2List)
        #reorder
        publishList = cmds.textScrollList(textScrollLists1,q=True,allItems=True)
        publishList.sort()
        cmds.textScrollList(textScrollLists1, edit=True, ra=True)
        cmds.textScrollList(textScrollLists1, edit=True, append=publishList)

    def guideWindow(self, html_text):
        # Delete old window if needed
        try:
            if self.guide_win and self.guide_win.isVisible():
                self.guide_win.close()
                self.guide_win.deleteLater()
        except:
            pass

        self.guide_win = QtWidgets.QDialog()
        self.guide_win.setWindowTitle("Guide")
        self.guide_win.resize(490,640)

        layout = QtWidgets.QVBoxLayout(self.guide_win)

        browser = QtWidgets.QTextBrowser()
        browser.setReadOnly(True)
        browser.setOpenExternalLinks(True)
        browser.setHtml(html_text)

        layout.addWidget(browser)
        self.guide_win.show()

    def guide_list(self):
        txt = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>INPUT_NAME_REPLACE</title>
    <style>
        body {
            font-family: 'Segoe UI', Arial, sans-serif;
            background-color: #2b2b2b;
            color: #e8e8e8;
            margin: 16px;
        }

        h1 {
            color: #ff6a3d;
            font-size: 26px;
            margin-bottom: 18px;
        }

        .section {
            border: 1px solid #4a4a4a;
            background-color: #323232;
            padding: 12px;
            margin-bottom: 14px;
        }

        .section-title {
            color: #8ab4f8;
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 8px;
        }

        .desc {
            color: #cfcfcf;
            margin-bottom: 6px;
            font-size: 11pt;
            line-height: 1.5;
        }

        .good {
            color: #00d084;
            font-weight: bold;
        }

        .warn {
            color: #ffd166;
            font-weight: bold;
        }

        .note {
            color: #ff8a65;
            font-weight: bold;
            margin-top: 8px;
        }

        ul {
            margin-top: 4px;
            margin-bottom: 4px;
            padding-left: 18px;
        }

        li {
            margin-bottom: 4px;
            color: #cfcfcf;
        }

        .code {
            color: #f78c6c;
            font-family: Consolas, monospace;
        }
    </style>
</head>
<body>

    <h1>Input Name Replace</h1>

    <div class="section">
        <div class="section-title">Purpose</div>
        <div class="desc">
            This function allows you to replace the name of a target object using a selected source object.
        </div>
    </div>

    <div class="section">
        <div class="section-title">How to Use</div>
        <ul>
            <li>Select one <span class="good">source object</span> (reference name).</li>
            <li>Select one <span class="warn">unmatched target object</span> (object to be renamed).</li>
            <li>Click the <span class="code">InputName</span> button.</li>
        </ul>
    </div>

    <div class="section">
        <div class="section-title">Result</div>
        <div class="desc">
            The system will replace the target object's name using the source object's naming pattern.
        </div>
        <div class="desc">
            <span class="code">source(name) -> input(name)</span>
        </div>
    </div>

    <div class="section">
        <div class="section-title">Notes</div>
        <div class="desc">
            Ensure only one source and one target object are selected to avoid incorrect renaming.
        </div>
        <div class="note">
            This function is intended for fixing unmatched naming during validation or cleanup.
        </div>
    </div>

</body>
</html>'''
        self.guideWindow(txt)

    def textFieldImportF(self,textFieldImport):
        #select .txt or .py file
        singleFilter = "All Files (*.*)"
        script_file = cmds.fileDialog2(fileFilter=singleFilter, dialogStyle=1, fileMode=1)
        if script_file:
            script_file = script_file[0]
            cmds.textFieldButtonGrp(textFieldImport,e=True,tx=script_file)

    def textFieldExportF(self,textFieldExport):
        #select .txt or .py file  
        script_file = cmds.fileDialog2(dialogStyle=2, fileMode=3)
        if script_file:
            script_file = script_file[0]
            cmds.textFieldButtonGrp(textFieldExport,e=True,tx=script_file)

if __name__=='__main__':
    try:
        MaterialCheck_Func()
    except:
        pass