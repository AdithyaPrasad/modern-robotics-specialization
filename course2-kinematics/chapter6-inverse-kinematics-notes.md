# Chapter 6: Inverse Kinematics

## Problem Overview

This exercise considers a three-joint revolute (3R) planar robotic arm operating in the x-y plane.

The robot consists of:

- Three revolute joints: θ₁, θ₂, and θ₃
- Three links, each with a length of 1 meter
- A space frame {s} located at the base of the robot
- An end-effector frame {b} attached to the tip of the third link

All joint axes are parallel and point along the positive z-axis (out of the plane).

## Objective

Determine the joint angle vector

θ = [θ₁, θ₂, θ₃]

that places the end-effector at a specified target pose relative to the space frame.

The desired end-effector configuration is:

Tsd =
[[-0.585, -0.811, 0, 0.076],
 [ 0.811, -0.585, 0, 2.608],
 [ 0,      0,     1, 0    ],
 [ 0,      0,     0, 1    ]]

## Method

The inverse kinematics solution is obtained using the Modern Robotics library and the numerical solver:

```python
mr.IKinSpace()

## Objective

Use the `IKinSpace()` function from the Modern Robotics library to find joint angles that achieve a desired end-effector configuration.

## Concepts Used

- Screw axes in the space frame
- Home configuration matrix (M)
- Desired end-effector pose (T)
- Numerical inverse kinematics
- Error tolerances
