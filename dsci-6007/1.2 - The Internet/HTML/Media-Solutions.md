## Embedding Media

### Video and Audio

* video and audio tags
* Used to need fallbacks
* .mp4 and .ogg/.webm for video
* .mp3 for audio
* Caption tracks
* Controls

```html
<video controls="controls">
    <source src="first-choice.mp4" type="video/mp4">
    <source src="second-choice.ogg" type="video/ogg">
    Some message for browsers that don't support the video tag
</video>

<audio controls="controls">
    <source src="first-choice.mp3" type="audio/mp3">
    <track kind="captions" src="first-choice.en.vtt" srclang="en" label="English">
    Some message for browsers that don't support the audio tag
</audio>
```

### Figures

* On top of the basic image tag, there are two additional things you can use
* Figures are for illustration, diagram, or photo

```html
<figure>
    <img src="image.jpg" alt="A picture of a bear" />
    <figcaption>This is me fighting a bear</figcaption>
</figure>
```

### Image Maps

* Image with clickable areas

```html
<img src="united-states.jpg" alt="USA" usemap="#usa-map" />
<map name="usa-map">
    <area shape="rect" coords="0,0,82,126" href="north-east.html" alt="Northeast" />
    <area shape="circle" coords="90,58,3" href="mid-west.html" alt="Midwest" />
    <area shape="poly" coords="124,58,8,12,7,52" href="south.html" alt="South" />
    <area shape="default" nohref="nohref" alt="Wild West" />
</map>
```

##### Exercise: Image Maps

Follow the instructions on the [image maps repo](https://github.com/gSchool/image-map-exercise).

### SVG

* Vectors vs. Rasters
* Syntax

```html
<svg version="1.1"
    baseProfile="full"
    width="300" height="200"
    xmlns="http://www.w3.org/2000/svg">
    <rect width="100%" height="100%" fill="red" />
    <circle cx="150" cy="100" r="80" fill="green" />
    <text x="150" y="125" font-size="60" text-anchor="middle" fill="white">SVG</text>
</svg>
```

* Small file size
* Perfect scaling
* Replacement for Flash
* Creating them is outside of scope, but we should know what they are

##### Exercise: SVG

Read through the [MDN guide to SVG](https://developer.mozilla.org/en-US/docs/Web/SVG) and be able to answer the following questions:

* What are some common use cases for SVG?
* How do vector images work?
* What are the advantages of using SVG over a raster image like a JPEG?
* What are the advantages of using a raster image over SVG?

For bonus points, add a set of social media icons to an HTML page using an SVG you find online.

### Canvas

* Also generated, but with JS

```
<canvas id="canvas"></canvas>
```

* Can manipulate the `<canvas>` element to react to user input, render 3d content, apply physics, more
* Good for games, graphics-intensive applications
* Need to know that it's a container for creating complex graphics in Javascript

Some Canvas demos:

* [Ball Drop Physics Demo](http://balldroppings.com/js/)
* [Reactive Light Streams](https://developer.mozilla.org/en-US/demos/detail/zen-photon-garden/launch)
* [Free Rider Game](http://www.freeriderhd.com/t/1016-layers)
