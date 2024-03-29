
import math
from spg import Molecule

# Rotation matrix function around the 3 main axis
def rotate_matrix_x (x, y, z, angle, atom, x_shift=0, y_shift=0, z_shift=0, units="DEGREES"):

    # Shift to origin (0,0)
    x = x - x_shift
    y = y - y_shift
    z = z - z_shift

    # Convert degrees to radians
    if units == "DEGREES":
        angle = math.radians(angle)

    # Rotation matrix multiplication to get rotated x, y & z
    xr = x + x_shift
    yr = (y * math.cos(angle)) - (z * math.sin(angle)) + y_shift
    zr = (y * math.sin(angle)) + (z * math.cos(angle)) + z_shift

    return float("{:.4f}".format(xr)), float("{:.4f}".format(yr)), float("{:.4f}".format(zr)), atom
def rotate_matrix_y (x, y, z, angle, atom, x_shift=0, y_shift=0, z_shift=0, units="DEGREES"):

    # Shift to origin (0,0)
    x = x - x_shift
    y = y - y_shift
    z = z - z_shift

    # Convert degrees to radians
    if units == "DEGREES":
        angle = math.radians(angle)

    # Rotation matrix multiplication to get rotated x, y & z
    xr = (x * math.cos(angle)) + (z * math.sin(angle)) + x_shift
    yr = y + y_shift
    zr = (-x * math.sin(angle)) + (z * math.cos(angle)) + z_shift

    return float("{:.4f}".format(xr)), float("{:.4f}".format(yr)), float("{:.4f}".format(zr)), atom
def rotate_matrix_z (x, y, z, angle, atom, x_shift=0, y_shift=0, z_shift=0, units="DEGREES"):

    # Shift to origin (0,0)
    x = x - x_shift
    y = y - y_shift
    z = z - z_shift

    # Convert degrees to radians
    if units == "DEGREES":
        angle = math.radians(angle)

    # Rotation matrix multiplication to get rotated x, y & z
    xr = (x * math.cos(angle)) - (y * math.sin(angle)) + x_shift
    yr = (x * math.sin(angle)) + (y * math.cos(angle)) + y_shift
    zr = z + z_shift

    return float("{:.4f}".format(xr)), float("{:.4f}".format(yr)), float("{:.4f}".format(zr)), atom

mol1 = Molecule([['H', [0.0, 0.0, 0.0]], 
   ['H', [0.0, 0.0, 1.0]],
   ['O', [0.0, 1.0, 0.0]]])

mol1.build()

def test_Cn(cd):

    angles=[360/1, 360/2, 360/3, 360/4, 360/5, 360/6, 360/7, 360/8]
    higher=1
    atm_flgx=[]
    atm_flgy=[]
    atm_flgz=[]
    atm=[]
    rtt_atmx=[]
    rtt_atmy=[]
    rtt_atmz=[]
    finalx=0
    finaly=0
    finalz=0

    for i in angles:
        atm_flg.insert(i,False)
        atm.append(cd.coordinates[i])
        atm.append(cd.atm_name[i])
        #even positions stand for coordinates
        #odd positions stand for atom name
        if i%2!=0:
            rtt_atmx.append(rotate_matrix_x(atm[i-1],angles[i], atm[i]))
            rtt_atmy.append(rotate_matrix_y(atm[i-1],angles[i], atm[i]))
            rtt_atmz.append(rotate_matrix_z(atm[i-1],angles[i], atm[i]))
    
    for j in range (0,len(rtt_atmx)):
        #check if it's possible to put j and k in the same for
        for k in range (0,len(rtt_atmx)):
            if k%2==0:
                if rtt_atmx[j][0:3]==atm[k].tolist() and rtt_atmx[j][3]==atm[k+1]:
                    atm_flgx[j]=True
                if rtt_atmy[j][0:3]==atm[k].tolist() and rtt_atmy[j][3]==atm[k+1]:
                    atm_flgy[j]=True
                if rtt_atmz[j][0:3]==atm[k].tolist() and rtt_atmz[j][3]==atm[k+1]:
                    atm_flgz[j]=True
    
    for l in range(0,len(atm_flgx)):
        if atm_flgx[l]==False:
            finalx=finalx+1
        if atm_flgy[l]==False:
            finaly=finaly+1
        if atm_flgz[l]==False:
            finalz=finalz+1
    
    for m in angles:
        if finalx==0:
            print(f"There is a C{int((m+1)*angles[m])} symmetry operation")
            #main_axis.append('x')
            rot_x.insert(m,int((m+1)*angles[m]))
        if finaly==0:
            print(f"There is a C{int((m+1)*angles[m])} symmetry operation")
            #main_axis.append('y')
            rot_y.insert(m,int((m+1)*angles[m]))
        if finalz==0:
            print(f"There is a C{int((m+1)*angles[m])} symmetry operation")
            #main_axis.append('z')
            rot_z.insert(m,int((m+1)*angles[m]))
            if int((m+1)*angles[m])>higher:
                higher=int((m+1)*angles[m])

    max_x=max(rot_x)
    max_y=max(rot_y)
    max_z=max(rot_z)
    if max_x>max_y and max_x>max_z:
        main_axis='x'
        higher=max_x
    elif max_y>max_x and max_y>max_z:
        main_axis='y'
        higher=max_y
    elif max_z>max_x and max_z>max_y:
        main_axis='z'
        higher=max_z
    
    if higher!=1:
        print(f"The higher rotation symmetry operation is C{higher} around {main_axis}")
    else:
        print("There is no rotation symmetry operation")
    
    return

test_Cn(mol1)

