# About
<p>
Script generates an image with size you want. Under the hood there are different types of color masking. 
Also you can write your own. 
</p>

## Usage
<p>
<code>main.py [-h] [-t {jpg,png}] [--width WIDTH] [--height HEIGHT] -s STEPS out_path</code>

Argument `-t` defines type of output image. Now available `.jpg` and `.png`.
Arguments `--width` and `--height` defines output image width and height.
Argument `-s` defines noise matrix size.
However, you can run `main.py` with flag `-h` you'll see help.
</p>

### Smoothing
<p>Now available only cubic interpolation for noise.</p>

### Color masking
<p>Now available alpha masks, color masks, grayscale masks.</p>

#### Alpha
<p>

For now there is `simple` and `lines` masks.
</p>

##### simple
<p>

Multiply value in raw image by 256 and return 
</p>