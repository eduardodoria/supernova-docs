It`s possible to animate any object. This page explains how to make the animation work in many ways and ease functions. Animations in Supernova are made by Actions. These Actions can be used in all Scene objects.

There are these types of actions:

* TimeAction
    * MoveAction
    * RotateAction
    * ScaleAction
    * ColorAction
    * AlphaAction
* ParticlesAnimation
* SpriteAnimation

Any kind of **action** can be controlled with these tree main controllers:

* ```run()```
* ```stop()```
* ```pause()```

Also, you can use actions with these callback events:

* ```onStart()```
* ```onRun()```
* ```onPause()```
* ```onStop()```
* ```onFinish()```
* ```onStep()```

## TimeAction

TimeAction is a generic type of action that has the values ```time``` and ```value```. Both values can range from 0 to 1. The ```time``` is always fixed by a pre-defined duration, but ```value``` is calculated by an ease function. It can be controlled by both pre-defined functions and user-defined functions.

``` c++
#include "Supernova.h"

#include "Scene.h"
#include "Polygon.h"
#include "Camera.h"
#include "TimeAction.h"
#include "MoveAction.h"

using namespace Supernova;

Polygon triangle;
Scene scene;
TimeAction* action;

void onActionOnStep(Object* object);
void onTouchPress(float x, float y);

void init(){
    Engine::setCanvasSize(1000, 480);

    triangle.addVertex(Vector3(0, -100, 0));
    triangle.addVertex(Vector3(-50, 50, 0));
    triangle.addVertex(Vector3(50, 50, 0));

    triangle.setPosition(Vector3(300, 300, 0));
    triangle.setColor(0.6, 0.2, 0.6, 1);

    scene.addObject(&triangle);

    //action = new MoveAction(triangle.getPosition(), Vector3(0,10,0), 2, true);
    action = new TimeAction(2, true);

    action->setFunctionType(S_LINEAR);
    triangle.addAction(action);
    //action->run();

    action->onStep(onActionOnStep);

    Engine::setScene(&scene);
    Events::onTouchPress(onTouchPress);
}

void onActionOnStep(Object* object){
    object->setPosition(object->getPosition().x,200);
}

void onTouchPress(float x, float y){
    if (action->isRunning())
        action->pause();
    else
        action->run();
}
```
``` lua
Engine.setCanvasSize(1000,480)

scene = Scene()
triangle = Polygon()

triangle:addVertex(0, -100, 0)
triangle:addVertex(-50, 50, 0)
triangle:addVertex(50, 50, 0)

triangle:setPosition(300,300,0)
triangle:setColor(0.6, 0.2, 0.6, 1)

scene:addObject(triangle)

action = TimeAction(2, false)

action:setFunctionType(TimeAction.EASE_ELASTIC_IN_OUT)
triangle:addAction(action)

Engine.setScene(scene)

function onActionOnStep(object)
    object:setPosition2D(100, 500);
end
action:onStep(onActionOnStep);

function onTouchPress(x, y)
    if (action:isRunning()) then
        action:pause()
    else
        action:run()
    end
end
Events:onTouchPress(onTouchPress);
```

This is an example of MoveAction from TimeAction:

``` c++
#include "Supernova.h"

#include "Scene.h"
#include "Polygon.h"
#include "Camera.h"
#include "MoveAction.h"

using namespace Supernova;

Polygon triangle;
Scene scene;
MoveAction* action;

void onTouchPress(float x, float y);

void init(){
    Engine::setCanvasSize(1000, 480);

    triangle.addVertex(Vector3(0, -100, 0));
    triangle.addVertex(Vector3(-50, 50, 0));
    triangle.addVertex(Vector3(50, 50, 0));

    triangle.setPosition(Vector3(300, 300, 0));
    triangle.setColor(0.6, 0.2, 0.6, 1);

    scene.addObject(&triangle);

    action = new MoveAction(triangle.getPosition(), Vector3(0,10,0), 2, true);

    action->setFunctionType(S_LINEAR);
    triangle.addAction(action);
    action->run();

    Engine::setScene(&scene);
    Events::onTouchPress(onTouchPress);
}

void onTouchPress(float x, float y){
    if (action->isRunning())
        action->pause();
    else
        action->run();
}
```
``` lua
Engine.setCanvasSize(1000,480)

scene = Scene()
triangle = Polygon()

triangle:addVertex(0, -100, 0)
triangle:addVertex(-50, 50, 0)
triangle:addVertex(50, 50, 0)

triangle:setPosition(300,300,0)
triangle:setColor(0.6, 0.2, 0.6, 1)

scene:addObject(triangle)

action = MoveAction(triangle.position, Vector3(500,700,0), 2, true)

action:setFunctionType(TimeAction.EASE_ELASTIC_IN_OUT)
triangle:addAction(action)
action:run()

Engine.setScene(scene)

function onTouchPress(x, y)
    if (action:isRunning()) then
        action:pause()
    else
        action:run()
    end
end
Events:onTouchPress(onTouchPress);
```

### Pre-defined functions

#### Linear
![Linear](../images/ease/linear.png)
``` c++
action.setFunctionType(S_LINEAR);
```
``` lua
action:setFunctionType(TimeAction.LINEAR);
```
#### Quad
![Quad](../images/ease/easeQuad.png)
``` c++
action.setFunctionType(S_EASE_QUAD_IN);
action.setFunctionType(S_EASE_QUAD_OUT);
action.setFunctionType(S_EASE_QUAD_IN_OUT);
```
``` lua
action:setFunctionType(TimeAction.EASE_QUAD_IN);
action:setFunctionType(TimeAction.EASE_QUAD_OUT);
action:setFunctionType(TimeAction.EASE_QUAD_IN_OUT);
```
#### Cubic
![Cubic](../images/ease/easeCubic.png)
``` c++
action.setFunctionType(S_EASE_CUBIC_IN);
action.setFunctionType(S_EASE_CUBIC_OUT);
action.setFunctionType(S_EASE_CUBIC_IN_OUT);
```
``` lua
action:setFunctionType(TimeAction.EASE_CUBIC_IN);
action:setFunctionType(TimeAction.EASE_CUBIC_OUT);
action:setFunctionType(TimeAction.EASE_CUBIC_IN_OUT);
```
#### Quart
![Quart](../images/ease/easeQuart.png)
``` c++
action.setFunctionType(S_EASE_QUART_IN);
action.setFunctionType(S_EASE_QUART_OUT);
action.setFunctionType(S_EASE_QUART_IN_OUT);
```
``` lua
action:setFunctionType(TimeAction.EASE_QUART_IN);
action:setFunctionType(TimeAction.EASE_QUART_OUT);
action:setFunctionType(TimeAction.EASE_QUART_IN_OUT);
```
#### Quint
![Quint](../images/ease/easeQuint.png)
``` c++
action.setFunctionType(S_EASE_QUINT_IN);
action.setFunctionType(S_EASE_QUINT_OUT);
action.setFunctionType(S_EASE_QUINT_IN_OUT);
```
``` lua
action:setFunctionType(TimeAction.EASE_QUINT_IN);
action:setFunctionType(TimeAction.EASE_QUINT_OUT);
action:setFunctionType(TimeAction.EASE_QUINT_IN_OUT);
```
#### Sine
![Sine](../images/ease/easeSine.png)
``` c++
action.setFunctionType(S_EASE_SINE_IN);
action.setFunctionType(S_EASE_SINE_OUT);
action.setFunctionType(S_EASE_SINE_IN_OUT);
```
``` lua
action:setFunctionType(TimeAction.EASE_SINE_IN);
action:setFunctionType(TimeAction.EASE_SINE_OUT);
action:setFunctionType(TimeAction.EASE_SINE_IN_OUT);
```
#### Expo
![Expo](../images/ease/easeExpo.png)
``` c++
action.setFunctionType(S_EASE_EXPO_IN);
action.setFunctionType(S_EASE_EXPO_OUT);
action.setFunctionType(S_EASE_EXPO_IN_OUT);
```
``` lua
action:setFunctionType(TimeAction.EASE_EXPO_IN);
action:setFunctionType(TimeAction.EASE_EXPO_OUT);
action:setFunctionType(TimeAction.EASE_EXPO_IN_OUT);
```
#### Circ
![Circ](../images/ease/easeCirc.png)
``` c++
action.setFunctionType(S_EASE_CIRC_IN);
action.setFunctionType(S_EASE_CIRC_OUT);
action.setFunctionType(S_EASE_CIRC_IN_OUT);
```
``` lua
action:setFunctionType(TimeAction.EASE_CIRC_IN);
action:setFunctionType(TimeAction.EASE_CIRC_OUT);
action:setFunctionType(TimeAction.EASE_CIRC_IN_OUT);
```
#### Elastic
![Elastic](../images/ease/easeElastic.png)
``` c++
action.setFunctionType(S_EASE_ELASTIC_IN);
action.setFunctionType(S_EASE_ELASTIC_OUT);
action.setFunctionType(S_EASE_ELASTIC_IN_OUT);
```
``` lua
action:setFunctionType(TimeAction.EASE_ELASTIC_IN);
action:setFunctionType(TimeAction.EASE_ELASTIC_OUT);
action:setFunctionType(TimeAction.EASE_ELASTIC_IN_OUT);
```
#### Back
![Back](../images/ease/easeBack.png)
``` c++
action.setFunctionType(S_EASE_BACK_IN);
action.setFunctionType(S_EASE_BACK_OUT);
action.setFunctionType(S_EASE_BACK_IN_OUT);
```
``` lua
action:setFunctionType(TimeAction.EASE_BACK_IN);
action:setFunctionType(TimeAction.EASE_BACK_OUT);
action:setFunctionType(TimeAction.EASE_BACK_IN_OUT);
```
#### Bounce
![Bounce](../images/ease/easeBounce.png)
``` c++
action.setFunctionType(S_EASE_BOUNCE_IN);
action.setFunctionType(S_EASE_BOUNCE_OUT);
action.setFunctionType(S_EASE_BOUNCE_IN_OUT);
```
``` lua
action:setFunctionType(TimeAction.EASE_BOUNCE_IN);
action:setFunctionType(TimeAction.EASE_BOUNCE_OUT);
action:setFunctionType(TimeAction.EASE_BOUNCE_IN_OUT);
```

### User-defined functions

It's also possible to create new functions and attach it to a TimeAction.

``` c++
float newFunction(float time){
    return time * 2;
}

action.setFunction(newFunction);
```
``` lua
function newFunction(time)
    return time * 2
end

action:setFunction(newFunction);
```


## MoveAction

Is used to generate a movement in objects. The class parameter list is:

* **(start_position, end_position, time, loop)**

``` c++
action = new MoveAction(Vector3(100,200,0), Vector3(0,10,0), 2, false);
```
``` lua
action = MoveAction(Vector3(100,200,0), Vector3(0,10,0), 2, true)
```