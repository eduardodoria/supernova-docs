In Supernova to use particle system you have to create two kind of objects: Particle Initializers and Particle Modifiers.

* Particle Initializers
    * ParticleLifeInit
    * ParticlePositionInit
    * ParticleRotationInit
    * ParticleAccelerationInit
    * ParticleAlphaInit
    * ParticleColorInit
    * ParticleSizeInit
    * ParticleSpriteInit
    * ParticleVelocityInit
* Particle Modifiers
    * ParticleAlphaMod
    * ParticleColorMod
    * ParticlePositionMod
    * ParticleRotationMod
    * ParticleSizeMod
    * ParticleSpriteMod
    * ParticleVelocityMod

##Particle Initializers

###ParticleLifeInit

Every particle has its life and this life is regressive. When a particle starts, through this class you can set the lifetime of it. Throughout the life of the particle, when it reaches 0, the particle dies.

###ParticleAccelerationInit