In this example we will create a simple triangle. The same sample code can be used in any platform.

## File organization tree

## 1. Using C++

In Supernova file tree there is a ```main.cpp``` file located in ```project/``` folder. This file is used to start the game development in C++. As you can see, there is a call for ```supernova.h```, that will call ```init()``` function when game started.

Edit it with the code:

``` c++
#include "Supernova.h"

#include "Scene.h"
#include "Polygon.h"
#include "Camera.h"

using namespace Supernova;

Polygon triangle;
Scene scene;

void init(){
    Engine::setCanvasSize(1000, 480);

    triangle.addVertex(Vector3(0, -100, 0));
    triangle.addVertex(Vector3(-50, 50, 0));
    triangle.addVertex(Vector3(50, 50, 0));

    triangle.setPosition(Vector3(300, 300, 0));
    triangle.setColor(0.6, 0.2, 0.6, 1);
    scene.addObject(&triangle);

    Engine::setScene(&scene);
}
```
If you have both Lua and C++ calling Supernova static method ```setScene()```, the last call will be from Lua, so C++ code will not work.

## 2. Using Lua

In Supernova file tree there is a ```main.lua``` file located in ```assets/lua/``` folder. This file is used to start the game development in Lua. You can call any other Lua files by this.

Edit it with the code:

``` lua
Engine.setCanvasSize(1000, 480)

scene = Scene()
triangle = Polygon()

triangle:addVertex(0, -100, 0)
triangle:addVertex(-50, 50, 0)
triangle:addVertex(50, 50, 0)

triangle:setPosition(300, 300, 0)
triangle:setColor(0.6, 0.2, 0.6, 1)

scene:addObject(triangle)

Engine.setScene(scene)
```

Now you can **run** to see the result.
