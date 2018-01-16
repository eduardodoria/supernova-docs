It`s possible to animate any object. This page explains how to make the animation work in many ways and ease functions. Animations in Supernova are made by Actions. These Actions can be used in all Scene objects.

There are these types of actions:

* TimeAction
    * MoveAction
    * RotationAction
    * ScaleAction
    * ColorAction
    * AlphaAction
* ParticlesAnimation
* SpriteAnimation

## TimeAction

TimeAction is a generic type of action that has the values ```time``` and ```value```. Both values can range from 0 to 1. The ```time``` is always fixed by duration, but ```value``` is calculated by an [**ease functions**](ease-functions).

## MoveAction

This type is used to generate a movement in objects. First thing you need to do is create an ```MoveAction``` object.

Lua: ```action = MoveAction()```  
C++: ```MoveAction action()```