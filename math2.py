# NOTES AND OTHER STUFF
# "x_l" stands for "x list"

# IMPORTS
import math
import numpy as np
import random
# FUNCTIONS
# Finds the n-root of a x number
def nroot(x, n):
    return math.pow(x, 1/n);
# Finds the product between matrix "A" and "B"
def multiplicate_matrix(A:list, B:list):
    # Creates and feeds C with zeros
    C = [];
    for i in range(len(A)):
        C.append([]);
        for e in range(len(B[0])):
            C[i].append(0);    
    # Executes the multiplications, surprisingly works with every matrix i tested so far
    for i in range(len(A)):
        for e in range(len(B[0])):
            # The multiplication needs to be executed "len(A[0])" times
            # And this loop serves also to prevent an "IndexError"
            for i2 in range(len(A[0])):
                C[i][e] += A[i][i2]*B[i2][e];
    return C;
# Finds and return the main diagonal
def main_diagonal(data:list):
    # "d" stands for "diagonal"
    d = [];
    # "nd" stands for "number of the diagonal"
    nd = 0;
    # "td" stands for "temp diagonal"
    td = [];
    while True:
        try:
            for i in range(len(data)+1):
                td.append(data[i][i+nd]);
        except IndexError:
            if nd != len(data[0]):
                d.append(td)
                nd += 1;
                td = [];
            else:
                break
    # "bd" stands for "bigger diagonal"
    bd = [];
    # Gets the bigger diagonal
    # But what if there are two diagonals with the same size? Then it stays with the first of
    # both he encounters
    for i in d:
        if len(i) > len(bd):
            bd = i;
    return bd;
# Applies one of the 4 basic operation to a 1D array and another 1D array or a number
def do_stuff_to_line(A, B, o):
    C = [];
    if type(B) == int or type(B) == float:
        if o == "*":
            for i in range(len(A)):
                C.append(A[i] * B);
        if o == "-":
            for i in range(len(A)):
                C.append(A[i] - B);
        if o == "+":
            for i in range(len(A)):
                C.append(A[i] + B);
        if o == "/":
            for i in range(len(A)):
                C.append(A[i] / B);
        return C;
    else:
        if o == "*":
            for i in range(len(A)):
                C.append(A[i] * B[i]);
        if o == "-":
            for i in range(len(A)):
                C.append(A[i] - B[i]);
        if o == "+":
            for i in range(len(A)):
                C.append(A[i] + B[i]);
        if o == "/":
            for i in range(len(A)):
                C.append(A[i] / B[i]);
        return C;

# Transforms a number to a fraction with numerator x and denominator 10^x, respectively
def to_fraction(number):
    if number >= 1:
        # "ns" stands for "number to string length"
        nsl = len(str(number))-2;
    else:
        nsl = len(str(number))-1;
    # x / 10^nsl = number
    # Which means x = number * 10^nsl
    return (number * 10**nsl, 10**nsl);
# Doing this because 4 decimals are enough, and more than that is dangerous
def shorthen_decimal(dm):
    for i in range(len(dm)):
        for e in range(len(dm[i])):
            n_str_split = str(dm[i][e]).split(".");
            # Here i'm just adding the integers(inclunding the "-" signal)
            # to five(the dot and 4 decimals)
            l = len(n_str_split[0])+5;
            # This string is the sum of the integers, the dot and the decimals,
            # but only the indexes from 0 to l, then i transform it in float
            dm[i][e] = float((n_str_split[0]+"."+n_str_split[1])[:l]+"2");
    return dm
# Escalonates a matrix, in certain cases it may bug, but almost all times it will be fine
def escalonate(data:list):
     # Go to https://pt.planetcalc.com/8328/ and put some random matrix there to see the step by step
    # "md" stands for "main diagonal"
    md = main_diagonal(data);
    # "nnmd" stands for "number of number in main diagonal"
    nnmd = len(md);
    # "dm" stands for "data multiplied"
    dm = [];
    for x in data:
        dm.append(do_stuff_to_line(x, 1/x[0], "*"));
    if len(data) != 2:
        for i in range(len(dm)):
            if i != 0:
                dm[i] = do_stuff_to_line(dm[i], dm[0], "-");
                dm[i] = do_stuff_to_line(dm[i], to_fraction(dm[i][1])[1]/to_fraction(dm[i][1])[0], "*");
        dm = shorthen_decimal(dm);
        for i in range(len(dm)):
            if not i in [0,1]:
                dm[i] = do_stuff_to_line(dm[i], dm[1], "-")
        # "slmsef" may seen like i punched my keyboard, but it stands for 
        # "second line multiplicated by second element of first"
        slmsef = do_stuff_to_line(dm[1], dm[0][1], "*");
        dm[0] = do_stuff_to_line(dm[0], slmsef, "-");
        # Doing this because 4 decimals are enough, and more than that is dangerous
        dm = shorthen_decimal(dm);
    else:
        for i in range(len(dm)):
            if i != 0:
                dm[i] = do_stuff_to_line(dm[i], dm[0], "-");
    return dm;
# "Transposes" a matrix
def transpose(matrix:list):
    """ Our normal matrix
        A = [[1,2,3,4,5,6],
             [1,2,3,4,5,6]]
        When "transposed" the positions go like this:
            [0][0] -> [0][0]
            [0][1] -> [1][0]
            [1][0] -> [0][1]
            and so on"""
    # It surprisingly works for every matrix i've tested so far, except when they are simetrical
    # in that case we do this:
    if len(matrix) == len(matrix[0]):
        return matrix
    # But for every other case i've tested so far we can just do this:
    m2 = [];
    # Builds the matrix on the format we want and fill it with zeros
    for x in range(len(matrix[0])):
        m2.append([]);
        for y in range(len(matrix)):
            m2[x].append(0)
    # Loops to substitute zero by an actual value
    i = 0;
    while True:
        try:
            for x in range(len(m2[i])):
                m2[i][x] = matrix[x][i]
            i += 1;
        except IndexError:
            break
    return m2

# Finds the mean of x_l
def mean(x_l:list):
    a = 0;
    for x in x_l:
        a += x;
    return a / len(x_l);

# Finds the variance, that will be used to find the standart deviation
def variance(x_l):
    m = mean(x_l);
    # "x_lmm" stands for "x minus mean"
    x_lmm = [];
    # "v_lus" stands for "variance list unsquared"
    v_lus = [];
    for x in x_l:
        x_lmm.append(x - m);
    for x in x_lmm:
        v_lus.append(x**2);
    return mean(v_lus);

# Finds the standart deviation
def standart_deviation(x_l:list):
    return math.sqrt(variance(x_l));

# "Standartizes" values into something that we can compare, 'cause we cannot compare kg to cubic cm
# The "i" parameter is for the case you just need one element to be standartized
def standartization(x_l:list, i, std_all=False):
    # The formula is actually just "(x - m) / s", x being the actual value in whatever unit it was
    # to be, m being the mean and s being standart deviation
    m = mean(x_l);
    s = standart_deviation(x_l);
    if std_all:
        # "a_stdz" stands for "all standartized"
        a_stdz = [];
        for x in x_l:
            # As you can see you're just applying a formula on x to feed this array
            a_stdz.append((x - m) / s);
        return a_stdz;
    return (x_l[i] - m) / s;

# Finds the somatorie of a array
def somatory(dataX):
    r = 0;
    for x in dataX:
        r += x;
    return r;
#finds the diagonal of some position
def diagonal(pos, axis, data):
    d = [];
    i = 0;
    while True:
        try:
            d.append(data[i][pos]);
            i += 1;
            pos += axis;
        except IndexError: 
            return d;
# Concatenates two bi-dimensional arrays
def concatenate(a:list,b:list):
    for i in range(len(a)):
        for e in range(len(b[0])):
            a[i].append(b[i][e])
    return a;
# returns cofactor of a number in a matrix
# "l" = "line", "c" = "column"
def cofactor(data, l, c):
    matrix = np.array(data).tolist();
    for i in range(len(matrix)):
        matrix[i].pop(c);
    matrix.pop(l);
    D_ie = determinant(matrix, len(matrix));
    return ((-1)**(l+c)) * D_ie;
# Finds the determinant of a matrix(only NxN type)
def determinant(data, size):
    # "v" is the value i want to return
    if size == 2:
        return data[0][0]*data[1][1] - data[0][1]*data[1][0];
    # I'm using sarrus for matrixes with N = 3
    elif size == 3:
        v  = data[0][0]*data[1][1]*data[2][2];
        v -= data[0][0]*data[1][2]*data[2][1];
        v += data[0][1]*data[1][2]*data[2][0];
        v -= data[0][1]*data[1][0]*data[2][2];
        v += data[0][2]*data[1][0]*data[2][1];
        v -= data[0][2]*data[1][1]*data[2][0];
    # I'm using the laplace for matrix with N > 3
    else:
        v = 0;
        for e in range(len(data)):
            v += data[0][e]*cofactor(data, 0, e);
    return v;
# Finds the equation that forms a graphic
# Returning a,b,c and so on
def find_graphic_equation(data, exponential):
    #                      ^- a array with the x points in the 0 index and the y points on the 1
    parameters = [];
    indexes = [];
    # Feeding the indexes i'll use, i'm using the "exponential+1" here because i'll add extra number later and the matrix need to look like an
    # square
    for i in range(exponential+1):
        # Doesn't matter what the index is, if it fits on the "data[0]" and "data[1]" array i'll be able to use
        indexes.append(i);
    print(indexes)
    delta = [];
    # "ex" means "exponential", i need it that way because i'll decrease it's value later
    ex = exponential
    i = 0;
    l = [];
    # Feeding the "matrix"
    while True:
        # Remember that we're talking about a polynomial equation, that's why we need to elevate data to "ex"
        if ex != 1:
            l.append(data[0][indexes[i]]**ex);
            ex -= 1;
        else:
            l.append(data[0][indexes[i]]);
            l.append(1);
            delta.append(l);
            l = [];
            ex = exponential;
            i += 1;
            try: indexes[i];
            except IndexError: break
        if len(delta) == (exponential+1): break;
    delta_xyz = [];
    l = [];
    # Just feeding delta_xyz with enough delta copies
    for c in range(exponential+1):
        delta_xyz.append(np.array(delta).tolist());
    for c in range(len(delta_xyz)):
        for i in range(len(delta_xyz[0])):
            for e in range(len(delta_xyz[0][0])):
                # i use "e == c" here because the column that will recieve the "y" value needs to be according to the "variables"
                # on a equation system, to substitute just the right ones 
                if e == c: delta_xyz[c][i][e] = data[1][indexes[i]];
    delta_determinant = determinant(delta,exponential+1);
    for c in range(len(delta_xyz)):
        parameters.append(determinant(delta_xyz[c],exponential+1)/delta_determinant);
    return parameters;
#finds the r2 score of a regression
def r2(data, parameters):
    mean_y = mean(data[1]);
    squares1 = 0;
    squares2 = 0;
    e = 0;
    c = 0;
    while True:
        try:
            # builds the squares of the thing with and without regression
            squares1 += (mean_y)**2;
            ex = len(parameters)-1;
            # This is because i need to execute the equation that i dont know the size, so i'll just loop
            for i in range(len(parameters)):
                if ex != 0:
                    e += parameters[i]*((data[0][c])**ex);
                    ex -= 1;
                else: squares2 += parameters[i];
            squares2 = (e)**2;
            c += 1;
        except IndexError: break
    a = (squares1-squares2)/squares2;
    if a < 0:
        a *= -1;
    return a;