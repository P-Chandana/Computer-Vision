import matplotlib.image as img
import numpy as np
image=img.imread("3d.jpg")
w,h=image.shape[:2]
greyscale_image = image.mean(axis=2) 
new_image_size=np.array([1760,380])
xscale=new_image_size[0]/w
yscale=new_image_size[1]/h
max=216
interpolated_image=np.zeros([new_image_size[0],new_image_size[1]])
for i in range(new_image_size[0]-1): 
     for j in range(new_image_size[1]-1): 
        
                interpolated_image[i+1,j+1]= greyscale_image[1 + int(i / xscale), 1 + int(j / yscale)] 

            
plt.imshow(interpolated_image, cmap='gray') 
plt.show()
            