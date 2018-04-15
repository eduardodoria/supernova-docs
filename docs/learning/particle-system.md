In Supernova to use particle system you have to create two kind of objects: Particle Initializers and Particle Modifiers.

* Particle Initializers
    * ParticleLifeInit
    * ParticlePositionInit
    * ParticleRotationInit
    * ParticleAlphaInit
    * ParticleColorInit
    * ParticleSizeInit
    * ParticleSpriteInit
    * ParticleVelocityInit
    * ParticleAccelerationInit
* Particle Modifiers
    * ParticleAlphaMod
    * ParticleColorMod
    * ParticlePositionMod
    * ParticleRotationMod
    * ParticleSizeMod
    * ParticleSpriteMod
    * ParticleVelocityMod

Here is an example how Inittializers and Modifiers can be used to create particles animation.
``` c++
#include "Supernova.h"
#include "Scene.h"
#include "Particles.h"
#include "ParticlesAnimation.h"
#include "ParticleLifeInit.h"
#include "ParticleSizeInit.h"
#include "ParticleVelocityInit.h"
#include "ParticleColorMod.h"
#include "ParticleRotationMod.h"

using namespace Supernova;

Scene scene;
Particles *particles;
ParticlesAnimation* particlesanim;

void init(){
    Engine::setCanvasSize(1000, 480);
    
    particles = new Particles();
    particlesanim = new ParticlesAnimation();
    
    particles->setRate(10);
    particles->setMaxParticles(100);;
    particles->setTexture("f4.png");
    particles->setPosition(200, 200, 0);
    particles->addAction(particlesanim);
    
    particlesanim->addInit(new ParticleLifeInit(10, 10));
    particlesanim->addInit(new ParticleSizeInit(50, 100));
    particlesanim->addInit(new ParticleVelocityInit(Vector3(-15,-4, 0),Vector3(15,24, 0)));
    
    particlesanim->addMod(new ParticleColorMod(10, 0, 0, 1, 0, 1, 0, 0));
    particlesanim->addMod(new ParticleRotationMod(9, 1, 0, 180));
    
    particlesanim->run();
    
    scene.addObject(particles);
    
    Engine::setScene(&scene);
}
```     
``` lua
Engine.setCanvasSize(1000,480)

scene = Scene()

particles = Particles()
particlesanim = ParticlesAnimation()

particles:setRate(10)
particles:setMaxParticles(100)
particles:setTexture("f4.png")
particles:setPosition(200, 200, 0)
particles:addAction(particlesanim)

particlesanim:addInit(ParticleLifeInit(10, 10))
particlesanim:addInit(ParticleSizeInit(50, 100))
particlesanim:addInit(ParticleVelocityInit(Vector3(-15,-4, 0),Vector3(15,24, 0)))

particlesanim:addMod(ParticleColorMod(10, 0, 0, 1, 0, 1, 0, 0))
particlesanim:addMod(ParticleRotationMod(9, 1, 0, 180))

particlesanim:run()

scene:addObject(particles)

Engine.setScene(scene)
```

##Particle Initializers

###ParticleLifeInit

Every particle has its life and this life is regressive. When a particle starts, through this class you can set the lifetime of it. Throughout the life of the particle, when it reaches 0, the particle dies.

Class default constructor:  
**ParticleLifeInit(float minLife, float maxLife)**

``` c++
particlesanim->addInit(new ParticleLifeInit(10, 10));
```
``` lua
particlesanim:addInit(ParticleLifeInit(10, 10))
```

###ParticlePositionInit

The inittial position of particle is set with this class.

Class default constructor:  
**ParticlePositionInit(Vector3 minPosition, Vector3 maxPosition)**

``` c++
particlesanim->addInit(new ParticlePositionInit(Vector3(100, 0, 0), Vector3(100, 100, 0)));
```
``` lua
particlesanim:addInit(ParticlePositionInit(Vector3(100, 0, 0), Vector3(100, 100, 0)))
```

###ParticleRotationInit

The inittial rotation of particle is set with this class. The engine default is degress, but it can be changed.

Class default constructor:  
**ParticleRotationInit(float minRotation, float maxRotation)**

``` c++
particlesanim->addInit(new ParticleRotationInit(0, 180));
```
``` lua
particlesanim:addInit(ParticleRotationInit(0, 180))
```

###ParticleAlphaInit

It can be used to set particle transparency. When set 0 is total transparent particle, when set 1 is total opaque particle.

Class default constructor:  
**ParticleAlphaInit(float minAlpha, float maxAlpha)**

``` c++
particlesanim->addInit(new ParticleAlphaInit(0, 0.5))
```
``` lua
particlesanim:addInit(ParticleAlphaInit(0, 0.5))
```

###ParticleColorInit

Can be used to set inittial color of particle.

Class default constructor:  
**ParticleColorInit(float minRed, float minGreen, float minBlue, float maxRed, float maxGreen, float maxBlue)**

``` c++
particlesanim->addInit(new ParticleColorInit(0, 0, 0, 1, 1, 0))
```
``` lua
particlesanim:addInit(ParticleColorInit(0, 0, 0, 1, 1, 0))
```

###ParticleSizeInit

Every particle can have its size. This class is used to set inittial size of particle.

Class default constructor:  
**ParticleSizeInit(float minSize, float maxSize)**

``` c++
particlesanim->addInit(new ParticleSizeInit(50, 100))
```
``` lua
particlesanim:addInit(ParticleSizeInit(50, 100))
```

###ParticleSpriteInit

A particle can also have a sprite. The sprite of particle is set by an integer and during particle creation the inittial sprite is sorted.  
In Supernova we call sprite as a rect of sprite sheet. More details you can see in [sprite](sprites) section.

Class default constructor:  
**ParticleSpriteInit(std::vector<int> frames)**

``` c++
std::vector<int> sprites;
sprites.push_back(1);
sprites.push_back(0);
sprites.push_back(2);
particlesanim->addInit(new ParticleSpriteInit(sprites));
```
``` lua
particlesanim->addInit(ParticleSpriteInit({1, 0, 2}));
```

###ParticleVelocityInit

It's the inittial velocity of particle.

Class default constructor:  
**ParticleVelocityInit(Vector3 minVelocity, Vector3 maxVelocity)**

``` c++
particlesanim->addInit(new ParticleVelocityInit(Vector3(-15, -4, 0),Vector3(15, 24, 0)))
```
``` lua
particlesanim:addInit(ParticleVelocityInit(Vector3(-15, -4, 0),Vector3(15, 24, 0)))
```

###ParticleAccelerationInit

It's to set inittal acceleration of particle with this class.

Class default constructor:  
**ParticleAccelerationInit(Vector3 minAcceleration, Vector3 maxAcceleration)**

``` c++
particlesanim->addInit(new ParticleAccelerationInit(Vector3(0.0f, 9.81f * 5, 0.0f), Vector3(0.0f, 9.81f * 5, 0.0f)));
```
``` lua
particlesanim:addInit(ParticleAccelerationInit(Vector3(0.0f, 9.81f * 5, 0.0f), Vector3(0.0f, 9.81f * 5, 0.0f)))
```

