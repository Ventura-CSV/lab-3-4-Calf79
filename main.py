def main():
    x = int(input('Enter your input: '))
    y = int(input('Enter your input: '))
    """
    ########################################
    Code Your Program here
    ########################################
    """
    if (x and y)>0:
     quadrant = 1
    if (x and y)<0:
        quadrant= 3
    if (x<0) and (y>0):
        quadrant=2 
    if (x>0) and (y<0):
        quadrant=4
    
    
    print(f'Quadrant: {quadrant}')
    ########################################
    # Do not delete the return statement
    ########################################
    return quadrant


if __name__ == '__main__':
    main()
