In this example we will create a simple triangle. The same sample code can be used in any platform.

## 1. Using Lua

In Supernova file tree there is a ```main.lua``` file located in ```assets/lua/``` folder. This file is used to start the game development in Lua. You can call any other Lua files by this.

Edit it with the code:

```Lua
Supernova.setCanvasSize(1000,480)

cena = Scene()
triangulo = Shape()

triangulo:addVertex(0, 100, 0)
triangulo:addVertex(-50, -50, 0)
triangulo:addVertex(50, -50, 0)

triangulo:setPosition(300,300,0)
triangulo:setColor(0.6, 0.2, 0.6, 1)

cena:addObject(triangulo)

Supernova.setScene(cena)
```

Now you can **run** to see the result.

## 2. Using C++

In Supernova file tree there is a ```main.cpp``` file located in ```project/``` folder. This file is used to start the game development in C++. As you can see, there is a call for ```supernova.h```, that will call ```init()``` function when game started.

Edit it with the code:

```C++
#include "Supernova.h"

#include "Scene.h"
#include "Shape.h"
#include "Camera.h"

Shape triangulo;
Scene cena;

void init(){
    Supernova::setCanvasSize(1000,480);

    triangulo.addVertex(Vector3(0, 100, 0));
    triangulo.addVertex(Vector3(-50, -50, 0));
    triangulo.addVertex(Vector3(50, -50, 0));

    triangulo.setPosition(Vector3(300,300,0));
    triangulo.setColor(0.6, 0.2, 0.6, 1);
    cena.addObject(&triangulo);

    Supernova::setScene(&cena);
}
```
If you have both Lua and C++ calling Supernova static method ```setScene()```, the last call will be from Lua, so C++ code will not work.

## 3. Building project

To build, you first have to choose desired platform. The following links are instructions for each platform. The same project code can run in any of them:

[Compiling for Android](Compiling for Android)  
[Compiling for iOS](Compiling for iOS)  
[Compiling for HTML5 (Emscripten)](Compiling for HTML5 (Emscripten))
