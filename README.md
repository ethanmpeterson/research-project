# Research Project

This repository contains several python files that contain physics simulations for my research project. Below is a description of each simulation.

## Universal Controls

- Press space to pause
- Press p to play
- Press r to restart
- Press esc to exit the simulation

## Basic Free Fall

- Filename: freefall_basic.py

The basic free fall simulation is the simplest of the three. The simulation assumes perfect vacuum conditions where there is no air resistance and the object is subjected to gravitational acceleration. The simulation has customizable starting values such as gravitational acceleration, initial velocity, initial position and ground position. These values can all be changed at the top of the file by changing the value of the concerned variable.

## Complex Free Fall

- Filename: freefall_complex.py

Unlike the basic free fall simulation, the complex free fall simulation assumes normal conditions of an object in free fall on earth. The object is given a mass and a drag coefficient, thus allowing the object to fall and reach terminal velocity as the upward drag force will eventually match the downward force applied by gravity. This simulation is perfect for demonstrating the concept of terminal velocity as shown by the simulation's accompanying graphs. Users can change the object's mass and drag coefficient in addition to all the same values that can be changed in the basic free fall simulation.

## 2 Dimensional Motion

- Filename: 2D_Motion.py

The 2D motion simulation resembles the complex free fall simulation, except that it handles complex motion in two directions. The simulation demonstrates the idea of 2 dimensional motion by allowing the user to analyze graph data from each axis. Users can change the same values as they could in the complex free fall simulation, with the exception that they can use two dimensions where applicable.

## Momentum: Newton's Cradle

- Filename: momentum.py

The momentum simulation uses ideas from our momentum unit to model Newton's cradle. It is assumed that there is no loss of momentum or energy in each collision so the device continues forever transfering momentum from ball on a pendulum to another. Relevant data is also graphed creating the expected sinusoidal pattern. Constants like the initial angle and which pendulum to start with can be adjusted at the top of the file.

## Energy

- Filename: energy.py

The energy simulation covers ideas from our grade 12 energy unit modelling a specific problem from the unit test. It consists of a block sliding down a frictionless incline and coming to a stop due to the frictional surface at the bottom. The various types of energy are graphed aptly demonstrating the concept of conservation of energy.

## Circular Motion

- Filename: circular_motion.py

The circular motion simulation covers ideas from the grade 12 circular motion unit. The simulation models the basic scenario of a mass attached to a string rotating in a circular motion. This is the same general scenerio students were asked to analyze in the project for that unit.
