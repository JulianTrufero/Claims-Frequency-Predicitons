#CATHEGORIZING FUNCTIONS
#Variable: Vehicle Power
def vehpower_gr(x):
    """
    ARG: A number
    Returns: If is different from 12, 13, 14 or 15, returns the number, 
    otherwise, returns 12
    """
    if x in [12, 13, 14, 15]:
        x_ = 12
        return x_
    else:
        return x

#Variable: Vehicle Age

def vehage_gr(x):
    """
    ARG: A number
    Returns: If x belongs to (0,1) -> 1
             If x belongs to (1,10) -> 2
             If x belongs to (10,100) -> 3
    """
    if x in range(2):
        x_ = 1
        return x_
    elif x in range(1,11):
        x_ = 2
        return x_
    else:
        return 3

#Variable: Driver Age

def drivage_gr(x):
    """
    ARG: A number
    Returns: Assings a class (from 1 to 8) if x belongs to the specified ranges
    """
    if x in range(18,21):
        x_ = 1
        return x_
    elif x in range(21,26):
        x_ = 2
        return x_
    elif x in range(26,31):
        x_ = 3
        return x_
    elif x in range(31,41):
        x_ = 4
        return x_
    elif x in range(41,51):
        x_ = 5
        return x_
    elif x in range(51,61):
        x_ = 6
        return x_
    elif x in range(61,71):
        x_ = 7
        return x_

    else:
        return 8

#Variable: Bonus Malus

def bonusmalus_gr(x):
    """
    ARG: A number
    Returns: Assings a class (from 1 to 7) if x belongs to the specified ranges
    """
    if x in range(50, 61):
        x_ = 1
        return x_
    elif x in range(61,71):
        x_ = 2
        return x_
    elif x in range(71,81):
        x_ = 3
        return x_
    elif x in range(81,91):
        x_ = 4
        return x_
    elif x in range(91,101):
        x_ = 5
        return x_
    elif x in range(101,151):
        x_ = 6
        return x_
    else:
        x_ = 7
        return x_
    
#CLAIMS

def claims_(x):
    """
    arg: A claim count
    returns:if x is bigger than four, returns a four, otherwise, returns the same value
    """
    if x > 4 :
        return 4
    else: 
        return x