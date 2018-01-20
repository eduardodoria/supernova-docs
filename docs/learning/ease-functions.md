[TimeAction](object-animation#timeaction) can be controlled by both pre-defined functions and user-defined functions.

## Pre-defined functions

### Linear
![Linear](../images/ease/linear.png)
``` lua
--Lua
action:setFunctionType(TimeAction.LINEAR);
```
``` cpp
//C++
action.setFunctionType(S_LINEAR);
```
### Quad
![Quad](../images/ease/easeQuad.png)
``` lua
--Lua
action:setFunctionType(TimeAction.EASE_QUAD_IN);
action:setFunctionType(TimeAction.EASE_QUAD_OUT);
action:setFunctionType(TimeAction.EASE_QUAD_IN_OUT);
```
``` cpp
//C++
action.setFunctionType(S_EASE_QUAD_IN);
action.setFunctionType(S_EASE_QUAD_OUT);
action.setFunctionType(S_EASE_QUAD_IN_OUT);
```
### Cubic
![Cubic](../images/ease/easeCubic.png)
``` lua
--Lua
action:setFunctionType(TimeAction.EASE_CUBIC_IN);
action:setFunctionType(TimeAction.EASE_CUBIC_OUT);
action:setFunctionType(TimeAction.EASE_CUBIC_IN_OUT);
```
``` cpp
//C++
action.setFunctionType(S_EASE_CUBIC_IN);
action.setFunctionType(S_EASE_CUBIC_OUT);
action.setFunctionType(S_EASE_CUBIC_IN_OUT);
```
### Quart
![Quart](../images/ease/easeQuart.png)
``` lua
--Lua
action:setFunctionType(TimeAction.EASE_QUART_IN);
action:setFunctionType(TimeAction.EASE_QUART_OUT);
action:setFunctionType(TimeAction.EASE_QUART_IN_OUT);
```
``` cpp
//C++
action.setFunctionType(S_EASE_QUART_IN);
action.setFunctionType(S_EASE_QUART_OUT);
action.setFunctionType(S_EASE_QUART_IN_OUT);
```
### Quint
![Quint](../images/ease/easeQuint.png)
``` lua
--Lua
action:setFunctionType(TimeAction.EASE_QUINT_IN);
action:setFunctionType(TimeAction.EASE_QUINT_OUT);
action:setFunctionType(TimeAction.EASE_QUINT_IN_OUT);
```
``` cpp
//C++
action.setFunctionType(S_EASE_QUINT_IN);
action.setFunctionType(S_EASE_QUINT_OUT);
action.setFunctionType(S_EASE_QUINT_IN_OUT);
```
### Sine
![Sine](../images/ease/easeSine.png)
``` lua
--Lua
action:setFunctionType(TimeAction.EASE_SINE_IN);
action:setFunctionType(TimeAction.EASE_SINE_OUT);
action:setFunctionType(TimeAction.EASE_SINE_IN_OUT);
```
``` cpp
//C++
action.setFunctionType(S_EASE_SINE_IN);
action.setFunctionType(S_EASE_SINE_OUT);
action.setFunctionType(S_EASE_SINE_IN_OUT);
```
### Expo
![Expo](../images/ease/easeExpo.png)
``` lua
--Lua
action:setFunctionType(TimeAction.EASE_EXPO_IN);
action:setFunctionType(TimeAction.EASE_EXPO_OUT);
action:setFunctionType(TimeAction.EASE_EXPO_IN_OUT);
```
``` cpp
//C++
action.setFunctionType(S_EASE_EXPO_IN);
action.setFunctionType(S_EASE_EXPO_OUT);
action.setFunctionType(S_EASE_EXPO_IN_OUT);
```
### Circ
![Circ](../images/ease/easeCirc.png)
``` lua
--Lua
action:setFunctionType(TimeAction.EASE_CIRC_IN);
action:setFunctionType(TimeAction.EASE_CIRC_OUT);
action:setFunctionType(TimeAction.EASE_CIRC_IN_OUT);
```
``` cpp
//C++
action.setFunctionType(S_EASE_CIRC_IN);
action.setFunctionType(S_EASE_CIRC_OUT);
action.setFunctionType(S_EASE_CIRC_IN_OUT);
```
### Elastic
![Elastic](../images/ease/easeElastic.png)
``` lua
--Lua
action:setFunctionType(TimeAction.EASE_ELASTIC_IN);
action:setFunctionType(TimeAction.EASE_ELASTIC_OUT);
action:setFunctionType(TimeAction.EASE_ELASTIC_IN_OUT);
```
``` cpp
//C++
action.setFunctionType(S_EASE_ELASTIC_IN);
action.setFunctionType(S_EASE_ELASTIC_OUT);
action.setFunctionType(S_EASE_ELASTIC_IN_OUT);
```
### Back
![Back](../images/ease/easeBack.png)
``` lua
--Lua
action:setFunctionType(TimeAction.EASE_BACK_IN);
action:setFunctionType(TimeAction.EASE_BACK_OUT);
action:setFunctionType(TimeAction.EASE_BACK_IN_OUT);
```
``` cpp
//C++
action.setFunctionType(S_EASE_BACK_IN);
action.setFunctionType(S_EASE_BACK_OUT);
action.setFunctionType(S_EASE_BACK_IN_OUT);
```
### Bounce
![Bounce](../images/ease/easeBounce.png)
``` lua
--Lua
action:setFunctionType(TimeAction.EASE_BOUNCE_IN);
action:setFunctionType(TimeAction.EASE_BOUNCE_OUT);
action:setFunctionType(TimeAction.EASE_BOUNCE_IN_OUT);
```
``` cpp
//C++
action.setFunctionType(S_EASE_BOUNCE_IN);
action.setFunctionType(S_EASE_BOUNCE_OUT);
action.setFunctionType(S_EASE_BOUNCE_IN_OUT);
```


## User-defined functions
