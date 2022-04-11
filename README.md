# PROBLEMS

* MUST FIND CFD SOLVER TO USE. OPENFOAM IS LINUX ONLY.
* Maybe copy/edit solvers from OpenFoam source code?
  * Yeah that's what I'm going to have to do
  * Fuck me
  * That's going to add so much to this project
  * Am I going to have to learn C++ again just to read the code?
  * Yes
  * Ugh
  * Fuck me

# SOLUTIONS

Ok so here's the plan:
1. Learn OpenFOAM
   * I need to get a case running on OpenFOAM so that I know how to use it
   * Try fictitious domain GitHub repo linked from pdf in 'resources' directory
   * If this doesn't make any sense, start with a simple channel flow then fictitious domain
   * Solvers should just be incompressible, unsteady, NS flow
2. Implementation:
   * Once I know what solvers are being used, edit these libraries for this program
   * Probably keep them as C++ for speed
     * Learn about calling C++ functions from Python scripts
   * Need to change output formats
     * Create proprietary format?
     * Might need to do this to prevent possible license issues
     * Will need to create reader for formats as well to view results in program

# Back to our regularly scheduled program

## Project Overview

* Working name: **_SpinSim_**
* Computational software for single/multiple flow turbines
* Utilizes fictitious domain method for simulation
* Restricts movement of blades around rotational axis

## Notes

* Uses Python/C++ for computational code
* GUI Development
  * Version 1 will use [Kivy](https://kivy.org/doc/stable/)
  * Version 2 can use Qt5 given enough income
    * Can be fully developed before Version 1 Release
    * Commercial license must be purchased before this version is released

## Required Modules

* numpy
* numpy-stl
* kivy
* plyer
