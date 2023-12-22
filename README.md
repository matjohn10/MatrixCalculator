# Matrix Calculator 
[![PyPI version](https://badge.fury.io/py/MatrixCalcs.svg)](https://badge.fury.io/py/MatrixCalcs)

Simple and usable in the terminal/command line.
<br/>
Build a matrix of any size row by row. <br/>
<br/>
More features will be added in the future.

## Easy start

Make sure you have at least Python 3.10 installed on your computer with pip.

```commandline
$ pip install MatrixCalcs
```

Furthermore, use the terminal/commandline to start the app:

```commandline
$ matcalc
```

The following should appear:

```commandline
Use <help> command to have more information.
Matrix Calc > [Command]
```
Use 'create' command to create your first and main matrix.

### Matrix Creation
```commandline
Matrix Calc > create
```
This should appear:
```commandline
==========================================================
Please enter your matrix row by row.
Make sure each row has the same number of elements.
Follow the following formats:
Format 1:
	Enter row: 1, 2, 3, 4
Format 2:
	Enter row: 1 2 3 4
	
When done, input 'done' or press Enter key. (Not case sensitive)
==========================================================
```
Just enter one row after the other following the formats above and input done when you are finished building your matrix.

## Documentation

The calculator can hold up to two different matrices at the same time, your main matrix and the 'other' matrix.
The main matrix is always on the left side of the equation.

### Single matrix

With your matrix, you have multiple possibilities:

| Code        | Effect                                           |
|-------------|--------------------------------------------------|
| create      | Create your main matrix.                         |
| det         | Gives the determinant of your matrix if possible |
| trans       | Gives the transpose of your matrix               |
| invert      | Gives the invert of your matrix if possible      |
| add         | Gives the possibility to add another matrix      |
| show [flag] | Show matrix -m (main)                            |
| use         | Use operation result and store it                |
| clear       | Clears the window.                               |
| restart     | Restart with a new matrix                        |
| help        | Gives the list of commands                       |
| exit        | Exit the application                             |

### Two matrices

After adding another matrix, using 'add' mentioned above, you have other possibilities:

| Code        | Effect                                        |
|-------------|-----------------------------------------------|
| back        | Go back to your first matrix only             |
| madd        | Matrix addition if possible                   |
| sub         | Matrix subtraction if possible                |
| dot         | Dot product if possible                       |
| cross       | Cross product if possible                     |
| switch      | Switches order of the main and 'other' matrix |
| show [flag] | Show matrix -m (main) -o (other) -b (both)    |
| use         | Use operation result and store it             |
| clear       | Clears the window.                            |
| help        | Gives the list of commands                    |
| restart     | Restart with a new matrix (both)              |
| exit        | Exit the application                          |
<br>

### Command 'use'
The use command needs two options, the operation and where to store it.

```commandline
Matrix Calc > use [operation] [location]
```
The possible operations are:
- transpose (trans)
- inversion (invert)
- addition (madd)
- subtraction (sub)
- dot product (dot)
- cross product (cross)

The possible locations are:
- Main matrix (m or -m)
- Other matrix (o or -o)
