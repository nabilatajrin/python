import os

# Function to move files
def main():

    src = '/media/iit/R a i n/2019/ML/pythonprojects/crop_img/src/'
    dst = '/media/iit/R a i n/2019/ML/pythonprojects/crop_img/dst/'

    for filename in os.listdir(src):
        print(filename)

        srcFolder = src + '/' + filename
        dstFolder = dst + filename

        # move all the files
        os.rename(srcFolder, dstFolder)

# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()