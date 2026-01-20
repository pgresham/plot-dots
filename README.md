## Plot Dots
A simple Python image analyzer with svg output.
---
### About the project.
The intended usage of this script is to generate svg files to output to a pen plotter. All variables are controlled from the command line to better facilitate integration into scripts.
**To use it, you will need the following packages installed:**
- [Pillow](https://pypi.org/project/pillow/) 
- [Numpy](https://pypi.org/project/numpy/)
- [Matplotlib](https://pypi.org/project/matplotlib/)
---
### How to use plot-dots.py
Once you have the required packages installed, plot-dots.py is fairly straightforward to use.
Executing the following will generate a result with the default values:

`python3 plot-dots.py image.png` 

Replacing *image.png* with the name of your image. Matplotlib will open up a screen with your output.

Other functions (including saving your image as an SVG) are available using the following arguments:

  - **&#8208;h, &#8208;&#8208;help** shows the help message and exits
  - **&#8208;r, &#8208;&#8208;resolution**  controls resolution. Higher numbers= fewer dots
  - **&#8208;t, &#8208;&#8208;threshold** Controls the threshold for adding a dot. Value between 0 and 765
  - **&#8208;d, &#8208;&#8208;dotsize** Controls the size of dots displayed.
  - **&#8208;b, &#8208;&#8208;black** Black & White rendering only. Useful for pen plotter output
  - **&#8208;n, &#8208;&#8208;novisual** No visual output. Combine with -s for scripting.
  - **&#8208;o, &#8208;&#8208;outfile** Defines a custom name for the output file. Default it OUTPUT.svg
  - **&#8208;s, &#8208;&#8208;save** Saves file as defined by -o or OUTPUT.svg if none is defined

## Example Usage
Consider the following code:

`python3 plot-dots.py my-image.jpg -r 100 -t 255 -d 2 -b -o my-output.svg -s`

This code would read in *my-image*
- sampling every 100th pixel in a grid
- rendering only the dots in which the **sum of the RGB value** is greater than 255
- with a dot size of 2pt
- black and white rendering only (discarding color for each dot rendered)
- outputting to my-output.svg
- and saving the result
Since &#8208;n is not selected, this would also open the Matplotlib display panel and show the output.

## Another Example

`python3 plot-dots.py opossum.jpg -t 500 -r 50`

![kurt-anderson-_BcaNBAl9oc-unsplash](https://github.com/user-attachments/assets/aa44ff9d-bc2e-4a98-b77b-9088d9b3ae18)

<sub>*Image credit: Kurt Anderson, Source: Unsplash.com*</sub>

<img width="640" height="480" alt="Figure_1" src="https://github.com/user-attachments/assets/f1f05ddd-955e-4961-8fe6-ac46dace3d53" />

