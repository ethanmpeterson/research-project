# Research Project

This repository contains several python files that contain physics simulations for my research project. Below is a description of each simulation.

## Universal Controls

- Press space to pause
- Press p to play
- Press r to restart
- Press esc to exit the simulation

## Basic Freefall

- Filename: freefall_basic.py

The basic freefall simulation is the simplest of the three. The simulation assumes perfect vaccum conditions where there is no air resistance and the object is subjected to gravitational acceleration. The simulation has customizable starting values such gravitational acceleration, initial velocity, initial position and ground position. These values can all be changed at the top of the file by changing the value of the concerned variable.

## Complex Freefall

- Filename: freefall_complex.py

Unlike the basic freefall simulation the complex freefall simulation assumes normal conditions of an object in freefall on earth. The object is given a mass and drag coefficient allowing the object to fall and reach terminal velocity since the upward drag force will eventually match the downward force applied by gravity. This simulation is perfect for demonstrating the concept of terminal velocity as the simulation's accompanying graphs show when the object hits terminal velocity. Users can change the object's mass and drag coefficient in addition to all the same values that can be changed in the basic freefall simulation.

## 2 Dimensional Motion

- Filename: 2D_Motion.py

The 2D motion simulation resembles the complex freefall simulation except it handles complex motion in two directions. The simulation demonstrates the idea of 2 dimensional motion by allowing the user to analyze graph data from each axis. Users can change the same values as they could in the complex freefall simulation except they can use two dimensions where applicable.
