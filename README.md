## Project Overview

* Computational software for single/multiple flow turbines
* Utilizes fictitious domain method for simulation
* Restricts movement of blades around rotational axis

## Notes

* Uses Python/Pyfoam for computational code
* GUI Development
  * Version 1 will use [Kivy](https://kivy.org/doc/stable/)
  * Version 2 can use Qt5 given enough income
    * Can be fully developed before Version 1 Release
    * Commercial license must be purchased before this version is released

## Code Structure

* Mesh creation from stl input (allow for saving of mesh)
* Class for inputs to fluid solver
  * Boundaries based on stl inputs
  * Need to allow user to select other parameters
* Fictitious domain class
* Fluid Simulation class

## Development Plan

* Find fast stl reader (or develop my own)
* Create classes for relevant objects
* Figure out how to set up and run Pyfoam cases
