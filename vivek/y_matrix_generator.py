import os
import numpy as np

from readLabel import *
from NumpyMatrix import * 
        
# function to calculate number of images in each patient file.
def get_tot_images(file): 
    npy_file = np.load(file)
    dim = npy_file.shape
    return(dim[0])

def matrix_generator():
    
    # Get all files in current working directory
    files = os.listdir(os.getcwd())
    
    num_imgs = []
    labels = []
    # create a list containing the number of images in each patient file.
    for file in files:
        num_imgs.append(get_tot_images(file))
    
    # create a list xthat contains the label(0 or 1) repeated n number of times (for each patient) 
    # where n is the number of images for each patient. And convert this list into a numpy array 
    # (there is a significant performance gain by doing it this way).
    for file, num in zip(files, num_imgs):    
        file_name, file_ext = file.split('.')
        labels.append(get_label(file_name)*num)
    # Combine all the elements of the list into one giant string    
    single_label_string = ''.join(map(str, labels))
    # Cast the string into a list before assigning it to a numpy array.
    np_matrix = np.array(list(single_label_string)) 
    saveNumpy(np_matrix, 'sample_images.npy')
    return np_matrix         

def main():
    my_path = r'fully qualified path of directory containing all .npy files'
    # Set it as the current working directory
    os.chdir(my_path)

    # Get the numpy matrix by calling the matrix_generator function        
    np_matrix = matrix_generator()
    print(np_matrix)
    print(np_matrix.shape)
    
if __name__ == '__main__':
    main()
