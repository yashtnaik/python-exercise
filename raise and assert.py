'''
******
*    *
*    *
*    *
*    *
*    *
******
'''
import os, traceback

def box(symbol, height, width):
    try:
        if len(symbol) != 1 :
            raise Exception('Invalid input, Symbol should be of 1 character only')
        if height < 2 and width < 2:
            raise Exception('Width and Height should be greater than 2')
        print(symbol * width)
        for i in range (height -2):
            print(symbol + (' ' * (width-2)) + symbol)
        print(symbol * width)
    except:
        errorfile=open('error.txt', 'w')
        errorfile.write(traceback.format_exc())
        errorfile.close()
        print('Traceback has been written in the error log file')
                
box('**', 5, 5)
print(os.getcwd())