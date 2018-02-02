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

Any kind of **action** can be controlled with these tree commands:

* ```run()```
* ```stop()```
* ```pause()```

## TimeAction

TimeAction is a generic type of action that has the values ```time``` and ```value```. Both values can range from 0 to 1. The ```time``` is always fixed by a pre-defined duration, but ```value``` is calculated by an ease function. It can be controlled by both pre-defined functions and user-defined functions.

``` lua
action = MoveAction(object.position, Vector3(500,700,0), 2, true)
action:setFunctionType(Action.ELASTIC_EASEINOUT)
[...]
object:addAction(acao)
[...]
action:run()
```
``` c++
#include "action/MoveAction.h"
using namespace Supernova;
[...]
MoveAction* action;
action = new MoveAction(Vector3(100,200,0), Vector3(0,10,0), 2, false);
action->setFunctionType(S_LINEAR);
[...]
object.addAction(action);
[...]
action->run();
```

### Pre-defined functions

#### Linear
![Linear](../images/ease/linear.png)
``` lua
action:setFunctionType(TimeAction.LINEAR);
```
``` c++
action.setFunctionType(S_LINEAR);
```
#### Quad
![Quad](../images/ease/easeQuad.png)
``` lua
action:setFunctionType(TimeAction.EASE_QUAD_IN);
action:setFunctionType(TimeAction.EASE_QUAD_OUT);
action:setFunctionType(TimeAction.EASE_QUAD_IN_OUT);
```
``` c++
action.setFunctionType(S_EASE_QUAD_IN);
action.setFunctionType(S_EASE_QUAD_OUT);
action.setFunctionType(S_EASE_QUAD_IN_OUT);
```
#### Cubic
![Cubic](../images/ease/easeCubic.png)
``` lua
action:setFunctionType(TimeAction.EASE_CUBIC_IN);
action:setFunctionType(TimeAction.EASE_CUBIC_OUT);
action:setFunctionType(TimeAction.EASE_CUBIC_IN_OUT);
```
``` c++
action.setFunctionType(S_EASE_CUBIC_IN);
action.setFunctionType(S_EASE_CUBIC_OUT);
action.setFunctionType(S_EASE_CUBIC_IN_OUT);
```
#### Quart
![Quart](../images/ease/easeQuart.png)
``` lua
action:setFunctionType(TimeAction.EASE_QUART_IN);
action:setFunctionType(TimeAction.EASE_QUART_OUT);
action:setFunctionType(TimeAction.EASE_QUART_IN_OUT);
```
``` c++
action.setFunctionType(S_EASE_QUART_IN);
action.setFunctionType(S_EASE_QUART_OUT);
action.setFunctionType(S_EASE_QUART_IN_OUT);
```
#### Quint
![Quint](../images/ease/easeQuint.png)
``` lua
action:setFunctionType(TimeAction.EASE_QUINT_IN);
action:setFunctionType(TimeAction.EASE_QUINT_OUT);
action:setFunctionType(TimeAction.EASE_QUINT_IN_OUT);
```
``` c++
action.setFunctionType(S_EASE_QUINT_IN);
action.setFunctionType(S_EASE_QUINT_OUT);
action.setFunctionType(S_EASE_QUINT_IN_OUT);
```
#### Sine
![Sine](../images/ease/easeSine.png)
``` lua
action:setFunctionType(TimeAction.EASE_SINE_IN);
action:setFunctionType(TimeAction.EASE_SINE_OUT);
action:setFunctionType(TimeAction.EASE_SINE_IN_OUT);
```
``` c++
action.setFunctionType(S_EASE_SINE_IN);
action.setFunctionType(S_EASE_SINE_OUT);
action.setFunctionType(S_EASE_SINE_IN_OUT);
```
#### Expo
![Expo](../images/ease/easeExpo.png)
``` lua
action:setFunctionType(TimeAction.EASE_EXPO_IN);
action:setFunctionType(TimeAction.EASE_EXPO_OUT);
action:setFunctionType(TimeAction.EASE_EXPO_IN_OUT);
```
``` c++
action.setFunctionType(S_EASE_EXPO_IN);
action.setFunctionType(S_EASE_EXPO_OUT);
action.setFunctionType(S_EASE_EXPO_IN_OUT);
```
#### Circ
![Circ](../images/ease/easeCirc.png)
``` lua
action:setFunctionType(TimeAction.EASE_CIRC_IN);
action:setFunctionType(TimeAction.EASE_CIRC_OUT);
action:setFunctionType(TimeAction.EASE_CIRC_IN_OUT);
```
``` c++
action.setFunctionType(S_EASE_CIRC_IN);
action.setFunctionType(S_EASE_CIRC_OUT);
action.setFunctionType(S_EASE_CIRC_IN_OUT);
```
#### Elastic
![Elastic](../images/ease/easeElastic.png)
``` lua
action:setFunctionType(TimeAction.EASE_ELASTIC_IN);
action:setFunctionType(TimeAction.EASE_ELASTIC_OUT);
action:setFunctionType(TimeAction.EASE_ELASTIC_IN_OUT);
```
``` c++
action.setFunctionType(S_EASE_ELASTIC_IN);
action.setFunctionType(S_EASE_ELASTIC_OUT);
action.setFunctionType(S_EASE_ELASTIC_IN_OUT);
```
#### Back
![Back](../images/ease/easeBack.png)
``` lua
action:setFunctionType(TimeAction.EASE_BACK_IN);
action:setFunctionType(TimeAction.EASE_BACK_OUT);
action:setFunctionType(TimeAction.EASE_BACK_IN_OUT);
```
``` c++
action.setFunctionType(S_EASE_BACK_IN);
action.setFunctionType(S_EASE_BACK_OUT);
action.setFunctionType(S_EASE_BACK_IN_OUT);
```
#### Bounce
![Bounce](../images/ease/easeBounce.png)
``` lua
action:setFunctionType(TimeAction.EASE_BOUNCE_IN);
action:setFunctionType(TimeAction.EASE_BOUNCE_OUT);
action:setFunctionType(TimeAction.EASE_BOUNCE_IN_OUT);
```
``` c++
action.setFunctionType(S_EASE_BOUNCE_IN);
action.setFunctionType(S_EASE_BOUNCE_OUT);
action.setFunctionType(S_EASE_BOUNCE_IN_OUT);
```

### User-defined functions

It's also possible to create new functions and attach it to a TimeAction.

``` lua
function newFunction(time)
    return time * 2
end

action:setFunction(newFunction);
```
``` c++
float newFunction(float time){
    return time * 2;
}

action.setFunction(newFunction);
```


## MoveAction

Is used to generate a movement in objects. The class parameter list is:

* **(start_position, end_position, time, loop)**

``` lua
action = MoveAction(Vector3(100,200,0), Vector3(0,10,0), 2, true)
```
``` c++
action = new MoveAction(Vector3(100,200,0), Vector3(0,10,0), 2, false);
```