# W8_6


# Menu-Driven SVG Drawing Program

This program allows users to interactively draw shapes and save them as SVG files. It uses the `svgwrite` library to create and manipulate SVG drawings.

## Features
- Draw a square (rectangle with equal sides)
- Draw a circle
- Save the SVG file with pretty formatting
- Exit the program

## Instructions
1. The program starts by initializing a `Drawing` object.
2. Users can choose to draw a square or a circle.
3. When saving, the program confirms the filename and asks for user confirmation before writing.
4. The SVG file is saved with 2-space indentation for readability.

## Code
```python


from svgwrite import Drawing, cm
from svgwrite.shapes import Rect, Circle, Polygon

def drawSquare(PDwg: Drawing) -> None:
    # ...
    PDwg.add(Rect(...)) # See https://svgwrite.readthedocs.io/en/latest/classes/shapes.html#rect
    return None

def drawCircle(PDwg: Drawing) -> None:
    # ...
    PDwg.add(Circle(...)) # See https://svgwrite.readthedocs.io/en/latest/classes/shapes.html#circle
    return None

def saveSvg(PDwg: Drawing) -> None:
    # See Drawing.save method https://svgwrite.readthedocs.io/en/latest/classes/drawing.html?highlight=save#svgwrite.drawing.Drawing.save
    return None

def main() -> None:
    # 1. Initialise
    Dwg = svgwrite.Drawing()
    # ...
        drawSquare(Dwg)
        drawCircle(Dwg)
    # 3. Cleanup
    return None
```
## Example program runs
```
Program starting.
Options:
1 - Draw square  
2 - Draw circle  
3 - Save svg  
0 - Exit  
Your choice: 1  
Insert square  
- Left edge position: 10  
- Top edge position: 10  
- Side length: 130  
- Fill color: blue  
- Stroke color: gray  

Options:  
1 - Draw square  
2 - Draw circle  
3 - Save svg  
0 - Exit  
Your choice: 3  
Insert filename: A8_T6_D1.svg  
Saving file to "A8_T6_D1.svg"  
Proceed (y/n)?: y  
Vector saved successfully!

Options:  
1 - Draw square  
2 - Draw circle  
3 - Save svg  
0 - Exit  
Your choice: 0  
Exiting program.

Program ending.
```
```
Program starting.
Options:
1 - Draw square
2 - Draw circle
3 - Save svg
0 - Exit
Your choice: 2
Insert circle
- Center X coord: 225
- Center Y coord: 75
- Radius: 65
- Fill color: red
- Stroke color: gray

Options:
1 - Draw square
2 - Draw circle
3 - Save svg
0 - Exit
Your choice: 3
Insert filename: A8_T6_D3.svg
Saving file to "A8_T6_D3.svg"
Proceed (y/n)?: y
Vector saved successfully!

Options:
1 - Draw square
2 - Draw circle
3 - Save svg
0 - Exit
Your choice: 0
Exiting program.

Program ending.
```
```
Program starting.
Options:
1 - Draw square
2 - Draw circle
3 - Save svg
0 - Exit
Your choice: 1
Insert square
- Left edge position: 10
- Top edge position: 10
- Side length: 130
- Fill color: blue
- Stroke color: gray

Options:
1 - Draw square
2 - Draw circle
3 - Save svg
0 - Exit
Your choice: 2
Insert circle
- Center X coord: 225
- Center Y coord: 75
- Radius: 65
- Fill color: red
- Stroke color: gray

Options:
1 - Draw square
2 - Draw circle
3 - Save svg
0 - Exit
Your choice: 3
Insert filename: A8_T6_D3.svg
Saving file to "A8_T6_D3.svg"
Proceed (y/n)?: y
Vector saved successfully!

Options:
1 - Draw square
2 - Draw circle
3 - Save svg
0 - Exit
Your choice: 0
Exiting program.

Program ending.
```
## Notes
- The `Drawing` object is passed by reference, so changes made in functions affect the original object.
- Ensure `svgwrite` is installed using `pip install svgwrite` before running the program.
