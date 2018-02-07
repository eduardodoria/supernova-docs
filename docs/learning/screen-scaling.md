To handle with the variety of resolutions and screen sizes of devices, Supernova have some options to choose the better scaling mode. All project code you must declare the size of canvas:

C++: ```Supernova::setCanvasSize(1000,480)```   
Lua: ```Supernova.setCanvasSize(1000,480)```

This is the base size you must use for design your project. For 3D projects this is used only for perspective view aspect, but for 2D projects this sizes are very important to positioning objects in screen.

It`s also important know Supernova uses the origin of coordinates at bottom-left of canvas. This image represents an abstract canvas:

![Canvas](../images/Canvas.png)

There are 5 types of scaling mode divided by 2 categories:

## Dynamic canvas size modes

### FitWidth

This is **default** mode. This keeps canvas width but floats height. Canvas can be changed from original format, but only height changes. Should be used ```getPreferedCanvasWidth()```and ```getPreferedCanvasHeight()``` to get original canvas size.

C++: ```Supernova::setScalingMode(S_SCALING_FITWIDTH)```    
Lua: ```Supernova.setScalingMode(Supernova.SCALING_FITWIDTH)```

![Fitwidth](../images/Fitwidth.png)

### FitHeight

It is similar to FitWidth. This keeps canvas height but floats width. Canvas can be changed from original format, but only width changes. Should be used ```getPreferedCanvasWidth()```and ```getPreferedCanvasHeight()``` to get original canvas size.

C++: ```Supernova::setScalingMode(S_SCALING_FITHEIGHT)```   
Lua: ```Supernova.setScalingMode(Supernova.SCALING_FITHEIGHT)```

![Fitheight](../images/Fitheight.png)

## Static canvas size modes

### Letterbox

This keeps canvas width and height but empty spaces can be show on screen.

C++: ```Supernova::setScalingMode(S_SCALING_LETTERBOX)```   
Lua: ```Supernova.setScalingMode(Supernova.SCALING_LETTERBOX)```

![Letterbox](../images/Letterbox.png)

### Crop

This keeps canvas width and height but part of canvas can be out of screen (not in visible area).

C++: ```Supernova::setScalingMode(S_SCALING_CROP)```    
Lua: ```Supernova.setScalingMode(Supernova.SCALING_CROP)```

![Crop](../images/Crop.png)

### Stretch

This keeps canvas width and height but scene objects can deform.

C++: ```Supernova::setScalingMode(S_SCALING_STRETCH)```     
Lua: ```Supernova.setScalingMode(Supernova.SCALING_STRETCH)```

![Stretch](../images/Stretch.png)