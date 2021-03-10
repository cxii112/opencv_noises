# About
This application made for crearing or editing images using noise. Также есть версия на [русском][readme-rus].

## Usage
Make sure you have installed all [requirements][requirements]. 
More about usage you can find [here][full-usage], full effects list with examples  [here][full-effects].
To create image you just need to run this:
```shell
noizy.py gen grayscale lines /path/to/destination
```
Result:

![Resulting image](./examples/gen__grayscale__lines.png)

For editing:
```shell
noizy.py edit channels levels-rgb /path/to/source.image /path/to/destination
```
Result:

![Resulting image](./examples/edit__channels__levels-ymc.png)

All people images took from [here][images-source].

[images-source]: https://thispersondoesnotexist.com/ "Images source"
[full-usage]: ./USAGE.md
[full-effects]: ./EFFECTS.md
[requirements]: ./requirements.txt
[readme-rus]: ./README.md