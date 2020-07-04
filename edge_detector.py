import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img

def hor_conv(w,h,photo_matrix):
    
        size_kernel = 3 
        kernel = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
       
        no_of_square_matrices = ((w-size_kernel)+1)*((h-size_kernel)+1)
   
                     
        result = []
        r = (h-3)+1                                         
        c = (w-3)+1                                         
        for i in range((h-3)+1 ):
            for j in range((w-3)+1):
                sub_matrix = photo_matrix[i:i+3,j:j+3]  
                sum = 0
                for m in range(3):
                    for n in range(3):
                        sum += (sub_matrix[m,n] * kernel[m,n])
                result.append(sum)
        result_matrix = np.asarray(result).reshape(r,c)     
        return result_matrix

def vert_conv(w,h,photo_matrix):
    
        size_kernel = 3
        kernel = np.array([[1,0,-1],[1,0,-1],[1,0,-1]])
        
        no_of_square_matrices = ((w-size_kernel)+1)*((h-size_kernel)+1)
   
                     
        result = []
        r = (h-3)+1                                        
        c = (w-3)+1                                         
        for i in range((h-3)+1 ):
            for j in range((w-3)+1):
                sub_matrix = photo_matrix[i:i+3,j:j+3]  
                sum = 0
                for m in range(3):
                    for n in range(3):
                        sum += (sub_matrix[m,n] * kernel[m,n])
                result.append(sum)
        result_matrix = np.asarray(result).reshape(r,c)     
        return result_matrix


def main():
    import matplotlib.pyplot as plt
    import matplotlib.image as img
    
    image = img.imread('image.jpg')
    black_n_white = image.mean(axis=2)  
    h,w = black_n_white.shape         

    vertical = vert_conv(w,h,black_n_white)  
    horizontal = hor_conv(w,h,black_n_white) 
    image = np.sqrt((vertical**2) + (horizontal**2)) 
    plt.imshow(image, cmap='gray', interpolation='nearest') 
    plt.show() 
    
    


    
