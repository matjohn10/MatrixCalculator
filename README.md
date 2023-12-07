# Matrix Calculator

Simple and usable in the terminal/command line.
<br/>
Build a matrix of any size row by row. <br/>
<br/>
More features will be added in the future.

## Easy start

After cloning the repository to your machine and moving to the directory, make sure that you install numpy.

```commandline
pip3 install numpy
```

Furthermore, use the terminal/commandline to start the app:

```commandline
python3 main.py
```

The following should appear:

```commandline
==========================================================
		Please enter your matrix row by row.
		Make sure each row has the same number of elements.
		Follow the following formats:
		Format 1:
			Enter row: 1, 2, 3, 4

		Format 2:
			Enter row: 1 2 3 4

		When done, input 'done'. (Not case sensitive)
==========================================================
Enter row (or 'done'):
```

Just enter one row after the other following the formats above and input done when you are finished building your matrix.

## Documentation

### Single matrix

With your matrix, you have multiple possibilities:

| Code    | Effect                                           |
| ------- | ------------------------------------------------ |
| det     | Gives the determinant of your matrix if possible |
| trans   | Gives the transpose of your matrix               |
| invert  | Gives the invert of your matrix if possible      |
| add     | Gives the possibility to add another matrix      |
| restart | Restart with a new matrix                        |
| exit    | Exit the application                             |

### Two matrices

After adding another matrix, using 'add' mentioned above, you have other possibilities:

| Code    | Effect                            |
| ------- | --------------------------------- |
| back    | Go back to your first matrix only |
| madd    | Matrix addition if possible       |
| sub     | Matrix subtraction if possible    |
| dot     | Dot product if possible           |
| cross   | Cross product if possible         |
| restart | Restart with a new matrix (both)  |
| exit    | Exit the application              |
