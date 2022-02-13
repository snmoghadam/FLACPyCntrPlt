#--------------------------------------------------------------------------------------------
#---Python Code for 2D Contour Plot of xy-u Based on FLAC Output
#--------------------------------------------------------------------------------------------

#---Importing Objects------------------------------------------------------------------------
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.cm as cm
import numpy as np

from matplotlib import *
from numpy import *

#---Reading Contour Data from infile and Storage in a Matrix---------------------------------
contrDAT_A1=np.loadtxt("A1_EXCVS3_NOD_Contour.dat", dtype='d', delimiter=' ')
cDAT_nrow_A1, cDAT_ncol_A1 = contrDAT_A1.shape

#---Defining FLAC Contour Grid---------------------------------------------------------------
nxGrid=1141    #FLAC igrid
nyGrid=119     #FLAC jgrid

#---Initializing Contour Matrix--------------------------------------------------------------
xcord = np.zeros((nyGrid,nxGrid),dtype='d')
ycord = np.zeros((nyGrid,nxGrid),dtype='d')
uvalu = np.zeros((nyGrid,nxGrid),dtype='d')

xLeft=0
yBott=100000
gridDx=1000000000
gridDy=1000000000
minUVal=-10000000000000000
SclUnit=1

for jyGrid in range(0,nyGrid):
  for ixGrid in range(0,nxGrid):
    xcord[jyGrid][ixGrid]=xLeft+gridDx*ixGrid
    ycord[jyGrid][ixGrid]=yBott+gridDy*jyGrid
    uvalu[jyGrid][ixGrid]=minUVal

#---Filling in Contour Matrix in A1 Area-----------------------------------------------------
for cDAT_irow_A1 in range (0,cDAT_nrow_A1):
  jyGrid=int(contrDAT_A1[cDAT_irow_A1][1]-1)
  ixGrid=int(contrDAT_A1[cDAT_irow_A1][0]-1)
  xcord[jyGrid][ixGrid]=contrDAT_A1[cDAT_irow_A1][2]
  ycord[jyGrid][ixGrid]=contrDAT_A1[cDAT_irow_A1][3]
  uvalu[jyGrid][ixGrid]=SclUnit*contrDAT_A1[cDAT_irow_A1][4]
  
#---Filling in Contour Matrix in A2 Area-----------------------------------------------------
#for cDAT_irow_A2 in range (0,cDAT_nrow_A2):
#  jyGrid=int(contrDAT_A2[cDAT_irow_A2][1]-1)
#  ixGrid=int(contrDAT_A2[cDAT_irow_A2][0]-1)
#  xcord[jyGrid][ixGrid]=contrDAT_A2[cDAT_irow_A2][2]
#  ycord[jyGrid][ixGrid]=contrDAT_A2[cDAT_irow_A2][3]
#  uvalu[jyGrid][ixGrid]=contrDAT_A2[cDAT_irow_A2][4]

#---Filling in Contour Matrix in A3 Area-----------------------------------------------------
#for cDAT_irow_A3 in range (0,cDAT_nrow_A3):
#  jyGrid=int(contrDAT_A3[cDAT_irow_A3][1]-1)
#  ixGrid=int(contrDAT_A3[cDAT_irow_A3][0]-1)
#  xcord[jyGrid][ixGrid]=contrDAT_A3[cDAT_irow_A3][2]
#  ycord[jyGrid][ixGrid]=contrDAT_A3[cDAT_irow_A3][3]
#  uvalu[jyGrid][ixGrid]=contrDAT_A3[cDAT_irow_A3][4]

#---Filling in Contour Matrix in A4 Area-----------------------------------------------------
#for cDAT_irow_A4 in range (0,cDAT_nrow_A4):
#  jyGrid=int(contrDAT_A4[cDAT_irow_A4][1]-1)
#  ixGrid=int(contrDAT_A4[cDAT_irow_A4][0]-1)
#  xcord[jyGrid][ixGrid]=contrDAT_A4[cDAT_irow_A4][2]
#  ycord[jyGrid][ixGrid]=contrDAT_A4[cDAT_irow_A4][3]
#  uvalu[jyGrid][ixGrid]=contrDAT_A4[cDAT_irow_A4][4]

#------------------------Contour Plot--------------------------------------------------------

dp = 600          #Figure resolution (dpi)
fl =11            #Figure Length (in)
fw =3           #Figure Width  (in)
xMin=150
xMax=900
xtN=16
yMin=175
yMax=355
ytN=10

fg = plt.figure(figsize=(fl, fw), dpi=dp)                               #Figure Size and Resolution Set-Up
ax1 = fg.add_subplot(111)
plt.tight_layout()
for axis in ['top','bottom','left','right']:                            #Setting Axes Width
  ax1.spines[axis].set_linewidth(0.5)

#levels = np.linspace(0,0.3,30)
#levels=[0,0.00.05,0.1,0.15,0.2,0.25,0.3]
levels=np.arange(start=-0.01, stop=0.33, step=0.01)
cp = plt.contourf(xcord,ycord,uvalu,levels)                             #Contour Plot
cm = plt.hsv()                                                          #Contour Color Map

ax = plt.axis([xMin,xMax,yMin,yMax])                                    #Axis Range
tx = plt.xticks(linspace(xMin,xMax,xtN),fontsize=7)                     #Setting Ticks on X Axis / fontweight='bold'
ty = plt.yticks(linspace(yMin,yMax,ytN),fontsize=7)                     #Setting Ticks on Y Axis
plt.tick_params(axis='both',which='major',length=3, width=0.5)





cb = plt.colorbar(cp,orientation='vertical')                            #Legend (Color Bar)
cb.set_label('Horizontal Displacement (m)',
             rotation=90,fontsize=9,weight="bold",
             labelpad=-40,y=0.5)
cb.outline.set_linewidth(0.5)                                          #Setting Color Bar Outline Width
cb.ax.tick_params(length=2, width=0.5)                                 #Settig Ticks on Color Bar
for t in cb.ax.get_yticklabels():
     t.set_fontsize(7)
     #t.set_fontweight('bold')
     
xl = plt.xlabel('Distance (m)',fontsize=9,weight="bold")                 #X Label
yl = plt.ylabel('Elevation (m)',fontsize=9,weight="bold")                #Y Label
#ct = plt.title("Displacement Contour (m)",fontsize=3)                   #Contour Title

#------------------------Geological Layers---------------------------------------------------
#---DW Top
DWX=np.array([0,1140])
DWY=np.array([199,199])
DWP = plt.plot(DWX,DWY,'k--',dashes=(5, 3),color='black',linewidth = 0.5)    #length of 5, space of 4
txt = plt.text(170,185,'Dw',color='black',fontsize=6)              #weight="bold"
#---Basal Clay Top
BCX=np.array([0,738.6])
BCY=np.array([206,206])
BCP = plt.plot(BCX,BCY,'k--',dashes=(5, 3),color='black',linewidth = 0.5)
txt = plt.text(170,200.5,'Basal Clay',color='black',fontsize=6)
#---Km Top
KMX=np.array([0,611])
KMY=np.array([260,260])
KMP = plt.plot(KMX,KMY,'k--',dashes=(5, 3),color='black',linewidth = 0.5)
txt = plt.text(170,231,'Km',color='black',fontsize=6)
#---Pgtc Top
PGTCX=np.array([0,605])
PGTCY=np.array([262,262])
PGTCP = plt.plot(PGTCX,PGTCY,'k--',dashes=(5, 3),color='black',linewidth = 0.5)
txt = plt.text(170,255,'Pgtc',color='black',fontsize=6)
#---Pg Top
PGX=np.array([0,542])
PGY=np.array([283,283])
#PGP = plt.plot(PGX,PGY,'k--',dashes=(5, 3),color='black',linewidth = 0.5)
txt = plt.text(170,270,'Pg',color='black',fontsize=6)
#Ground Surface
GSX=np.array([0,542,611,636,738.6,1140])
GSY=np.array([283,283,260,260,206,206])
PGP = plt.plot(GSX,GSY,'k-',color='black',linewidth = 1)
#---Annotations
#txt = plt.text(260,284,'Original Ground El. 283 m',fontsize=7,horizontalalignment='center')
#txt = plt.text(760,207,'Bottom of Pit El.206 m',fontsize=7)
pcs = plt.annotate('',xy=(542,283),xytext=(542,300),
                   arrowprops={'arrowstyle':'->','lw':0.5,'color':'black','shrinkA':0,'shrinkB':0},
                   fontsize=7,rotation=0,horizontalalignment='center',verticalalignment='bottom')
pcs = plt.annotate('',xy=(525,283),xytext=(525,300),
                   arrowprops={'arrowstyle':'->','lw':0.5,'color':'black','shrinkA':0,'shrinkB':0},
                   fontsize=7,rotation=0,horizontalalignment='center',verticalalignment='bottom')
pcs = plt.annotate('',xy=(400,283),xytext=(400,300),
                   arrowprops={'arrowstyle':'->','lw':0.5,'color':'black','shrinkA':0,'shrinkB':0},
                   fontsize=7,rotation=0,horizontalalignment='center',verticalalignment='bottom')

#------------------------Plots---------------------------------------------------------------

#plt.show()                                                              #Plot Contour
plt.savefig("XDispCnt.tif",format='tif',dpi=dp)







