import c4d
from c4d import gui
from c4d import utils as u, Matrix as m, Vector as v
from c4d.modules import takesystem as ts


#Welcome to the world of Python


def main():
    td=doc.GetTakeData()
    mt=td.GetMainTake()
    take_list = td.GetTakeSelection(True)
    #cam = main.GetEffectiveCamera(td)
    #camname=c4d.BaseList2D.GetName(cam)
    c4d.StatusSetText("updating")
    print("status update")
    #print(cam.getType())
    #print(cam.getTypeName())
    #print(cam.GetObjectName())
    c4d.StatusSetBar(0)
    for i in take_list:
        if not i.IsMain():
            print(i)
            tempCam=i.GetEffectiveCamera(td)
            print(tempCam)
            cn=tempCam[0].GetName()
            print(cn)
            i.SetName(cn)
            #td.(i)
    c4d.StatusClear()
if __name__=='__main__':
    main()
