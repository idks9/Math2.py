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
            dm[i][e] = float((n_str_split[0]+"."+n_str_split[1])[:l]);
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

def return_stuff(a):
    return a;
# Concatenates two bi-dimensional arrays
def concatenate(a:list,b:list):
    for i in range(len(a)):
        for e in range(len(b[0])):
            a[i].append(b[i][e])
    return a;
# Finds the determinant of a matrix(only 2x2, 3x3 or 4x4)
def determinant(data, size):
    # I'm using the leibnz(sry i don't how to write lol) method for determinants, since the matrix has the form of a square
    # "v" is the value i want to return
    v = 0;
    # "l" is the current line
    l = 0;
    # "tl" stands for "times line", it means how many times i executed the for loop
    tl = 0;
    delta = np.array(data).tolist();
    for i in range(len(delta)):
        delta[i].pop();
    data = concatenate(data, delta);
    for t in range(size):
        # "vt" stands for "temporary value", i'll use this to multiply the diagonal and then sum it with "v"
        vt = 1;
        for i in range(len(data)):
            # "vt" stands for "temporary value", i'll use this to sum the diagonal and then multiplicate it with "v"
            vt *= data[i][l+t];
            l += 1;
        v += vt;
        vt = 0;
        l = 0;
        # First part done, now to the second one
    for t in range(size):
        # "vt" stands for "temporary value", i'll use this to multiply the diagonal and then sum it with "v"
        vt = 1;
        l = 1;
        for i in range(len(data)):
            # "vt" stands for "temporary value", i'll use this to sum the diagonal and then multiplicate it with "v"
            vt *= data[i][-(l+t)];
            l += 1;
        v -= vt;
        vt = 0;
        l = 0;
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
        indexes.append(random.randint(0, len(data[0])-1))
        # It doesn't work with only one loop, because i need to check the entire array every time "cycle" of this first loop
        for e in range(len(indexes)-1):
            for t in range(len(indexes)):
                if indexes[t] == indexes[-1]:
                    indexes[-1] = random.randint(0, len(data[0])-1);
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
    # Now that'll be a pretty meme
    # Exquisite!
    for c in range(len(delta_xyz)):
        for i in range(len(delta_xyz[0])):
            for e in range(len(delta_xyz[0][0])):
                # i use "e == c" here because the column that will recieve the "y" value needs to be according to the "variables"
                # on a equation system, to substitute just the right ones 
                if e == c: delta_xyz[c][i][e] = data[1][indexes[i]];
    return parameters;
