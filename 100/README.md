# 100 - Introduction

Genesis is a physics platform designed for general-purpose *Robotics/Embodied AI/Physical AI* applications. It is simultaneously multiple things:

1. A **universal physics engine** re-built from the ground up, capable of simulating a wide range of materials and physical phenomena.
2. A **lightweight**, **ultra-fast**, **pythonic**, and **user-friendly** robotics simulation platform.
3. A powerful and fast **photo-realistic rendering system**.
4. A **generative data engine** that transforms user-prompted natural language description into various modalities of data.

Powered by a universal physics engine re-designed and re-built from the ground up, Genesis integrates various physics solvers and their coupling into a unified framework. This core physics engine is further enhanced by a generative agent framework that operates at an upper level, aiming towards fully automated data generation for robotics and beyond.

**Note**: Currently, we are open-sourcing the _underlying physics engine_ and the _simulation platform_. Our _generative framework_ is a modular system that incorporates many different generative modules, each handling a certain range of data modalities, routed by a high level agent. Some of the modules integrated existing papers and some are still under submission. Access to our generative feature will be gradually rolled out in the near future. If you are interested, feel free to explore more in the [paper list](#associated-papers) below.

Genesis aims to:

- **Lower the barrier** to using physics simulations, making robotics research accessible to everyone. See our [mission statement](https://genesis-world.readthedocs.io/en/latest/user_guide/overview/mission.html).
- **Unify diverse physics solvers** into a single framework to recreate the physical world with the highest fidelity.
- **Automate data generation**, reducing human effort and letting the data flywheel spin on its own.

Project Page: <https://genesis-embodied-ai.github.io/>

## Key Features

- **Speed**: Over 43 million FPS when simulating a Franka robotic arm with a single RTX 4090 (430,000 times faster than real-time).
- **Cross-platform**: Runs on Linux, macOS, Windows, and supports multiple compute backends (CPU, Nvidia/AMD GPUs, Apple Metal).
- **Integration of diverse physics solvers**: Rigid body, MPM, SPH, FEM, PBD, Stable Fluid.
- **Wide range of material models**: Simulation and coupling of rigid bodies, liquids, gases, deformable objects, thin-shell objects, and granular materials.
- **Compatibility with various robots**: Robotic arms, legged robots, drones, *soft robots*, and support for loading `MJCF (.xml)`, `URDF`, `.obj`, `.glb`, `.ply`, `.stl`, and more.
- **Photo-realistic rendering**: Native ray-tracing-based rendering.
- **Differentiability**: Genesis is designed to be fully differentiable. Currently, our MPM solver and Tool Solver support differentiability, with other solvers planned for future versions (starting with rigid & articulated body solver).
- **Physics-based tactile simulation**: Differentiable [tactile sensor simulation](https://github.com/Genesis-Embodied-AI/DiffTactile) coming soon (expected in version 0.3.0).
- **User-friendliness**: Designed for simplicity, with intuitive installation and APIs.
