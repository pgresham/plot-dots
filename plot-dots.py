#!usr/bin/python3

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import argparse


def imagePlotter(inFile,outFile,resolution,cutoff,dotsize,black,novisual,save):
    try:
        print("(+) Opening "+inFile)
        img=Image.open(inFile)

    except:
        print("(-) Error opening file!")
        exit(0)
    w,h=img.size
    print("(+) Image size: "+str(w)+" "+str(h))
    img_array=np.array(img)
    img_list=img_array.tolist()


    def  colorHexify(arrayName,hIndex,wIndex):
    #Takes in an RGB array and returns a hex code as a string
    
        r = str(hex(arrayName[hIndex][wIndex][0])[2:])
        r = r if len(r)>1 else '0'+r

        g = str(hex(arrayName[hIndex][wIndex][1])[2:])
        g = g if len(g)>1 else '0'+g

        b = str(hex(arrayName[hIndex][wIndex][2])[2:])
        b = b if len(b)>1 else '0'+b
        return '#'+r+g+b
    for height_ in range(0,h-1%resolution,resolution):
        for width_ in range(0,w-1%resolution,resolution):
            if sum(img_list[height_][width_])<cutoff:
                if black:
                    plt.plot(width_,height_,'o',c='black',ms=dotsize)
                else:
                    plt.plot(width_,height_,'o',c=colorHexify(img_list,height_,width_),ms=dotsize)
            else:
                pass


    plt.axis('off')
    if save:
        plt.savefig(outFile,format='svg',transparent=True)
    if novisual==False:
        plt.show()



def main():
    parser=argparse.ArgumentParser(description='Plots an array of dots from an image', epilog='Example usage python3 plot-dots.py my-image.jpg -r 100 -t 255 -d 2 -o my-output.svg -s')
    parser.add_argument('image',type=str, help="Name of the image to be converted")
    parser.add_argument('-r','--resolution', type=int, default=100 ,help='controls resolution. Higher numbers= fewer dots')
    parser.add_argument('-t','--threshold',type=int,default=128,help='Controls the threshold for adding a dot. Value between 0 and 765')
    parser.add_argument('-d','--dotsize',type=int,default=1,help='Controls the size of dots displayed.')
    parser.add_argument('-b','--black', action='store_true',help='Black & White rendering only. Useful for pen plotter output')
    parser.add_argument('-n','--novisual',action='store_true',help='No visual output. Combine with -s for scripting.')
    parser.add_argument('-o','--outfile',type=str,default='OUTPUT.svg',help='Defines a custom name for the output file. Default it OUTPUT.svg')
    parser.add_argument('-s','--save',action='store_true',help='saves file as defined by -o or OUTPUT.svg if none is defined')
    args=parser.parse_args()


    imagePlotter(args.image,args.outfile,args.resolution,args.threshold,args.dotsize,args.black,args.novisual,args.save)

if __name__=='__main__':
    main()



