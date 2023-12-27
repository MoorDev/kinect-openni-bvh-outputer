import glob

path = "./*"
file_list = glob.glob(path)
bvh_list=([file for file in file_list if file.endswith('bvh')])

def striping(list):
    striped_list=[]
    for data in list:
        striped_list.append(data.strip('\n'))
    return(striped_list)

for bvh_origin in bvh_list:
    print (bvh_origin)
    print ("./cali"+bvh_origin[1:])
    fr = open(bvh_origin,"r")
    fw = open("./cali"+bvh_origin[1:],"w")
    lines=fr.readlines()
    lines=striping(lines)
    motion_index=lines.index("MOTION")+3 #readlines를 하면 \n이 붙기 때문
    print("motion index = "+str(motion_index))
    fw.write('\n'.join(lines[:motion_index])+'\n')

    origin_coordinate=str(lines[motion_index]).split()
    print(origin_coordinate)
    positionX=float(origin_coordinate[0])
    positionY=float(origin_coordinate[1])-0.7192 #default position T
    positionZ=float(origin_coordinate[2])
    rotationZ=float(origin_coordinate[3])
    rotationY=float(origin_coordinate[4])
    rotationX=float(origin_coordinate[5])
    for line in lines[motion_index:]:
        motion=line.split()
        motion[0]=str(float(motion[0])-positionX)
        motion[1]=str(float(motion[1])-positionY)
        motion[2]=str(float(motion[2])-positionZ)
        # motion[3]=str(float(motion[3])-rotationZ)
        # motion[4]=str(float(motion[4])-rotationY)
        motion[5]=str(float(motion[5])-rotationX)
        fw.write(' '.join(motion)+'\n')
    fr.close()
    fw.close()
