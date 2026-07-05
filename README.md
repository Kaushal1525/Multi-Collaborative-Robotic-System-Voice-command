
# Multi-Collaborative Robotic System (MCRS) with A* Path Planning

## Overview

This project presents a simulation of a Multi-Collaborative Robotic System (MCRS) developed using Python. The system demonstrates decentralized task planning, autonomous robot coordination, A* path planning, and voice-assisted event notifications within a structured grid environment.

Each robot independently plans collision-free paths to available tasks using the A* search algorithm. A decision engine allocates tasks based on the shortest computed path while considering robot availability and energy levels. During execution, robots navigate toward assigned goals, complete tasks autonomously, and provide spoken notifications using a text-to-speech engine.

The project illustrates important concepts in autonomous robotics, collaborative multi-agent systems, intelligent path planning, and industrial automation.

---

## Features

- Multi-robot collaboration
- Autonomous task allocation
- A* path planning
- Grid-based navigation
- Static obstacle avoidance
- Energy-aware task assignment
- Real-time decision cycles
- Autonomous task execution
- Voice-assisted status notifications
- Modular system architecture

---

## Technologies Used

- Python 3
- Heapq
- Math
- Random
- Time
- pyttsx3

---

## Project Structure

```text
MCRS-AStar-Path-Planning/
│
├── mcrs_astar.py
├── README.md
└── requirements.txt
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/Kaushal1525/MCRS-AStar-Path-Planning.git
```

### Navigate to the project directory

```bash
cd MCRS-AStar-Path-Planning
```

### Install the required dependency

```bash
pip install -r requirements.txt
```

or

```bash
pip install pyttsx3
```

---

## Running the Project

Execute the simulation using:

```bash
python mcrs_astar.py
```

The system will begin collaborative decision cycles and display:

- Robot status dashboard
- Path planning information
- Task allocation decisions
- Task completion events
- Voice announcements
- Remaining task count

The simulation terminates automatically after all tasks are completed.

---

## Working Principle

The system operates through repeated collaborative cycles.

Each cycle consists of:

1. Displaying the robot status dashboard.
2. Planning optimal paths using the A* algorithm.
3. Evaluating available tasks.
4. Assigning tasks to the most suitable robots.
5. Navigating robots toward their assigned goals.
6. Completing assigned tasks.
7. Announcing important events using voice feedback.
8. Repeating until all tasks are completed.

---

## System Architecture

```text
Robot Initialization
         │
         ▼
Task Generation
         │
         ▼
A* Path Planning
         │
         ▼
Decision Engine
         │
         ▼
Task Assignment
         │
         ▼
Robot Navigation
         │
         ▼
Task Completion
         │
         ▼
Voice Notification
         │
         ▼
Next Decision Cycle
```

---

## A* Path Planning

Each robot independently computes the shortest collision-free path to available tasks.

The planner considers:

- Robot position
- Task location
- Static obstacles
- Manhattan heuristic
- Grid boundaries

The robot selects the task with the minimum planned path length.

---

## Decision Engine

The collaborative decision engine:

- Evaluates available robots
- Evaluates available tasks
- Assigns ownership of tasks
- Prevents duplicate assignments
- Stores the generated navigation path

Task allocation is performed in a decentralized manner without requiring a permanent central controller.

---

## Robot Model

Each robot maintains:

- Robot ID
- Grid position
- Battery level
- Assigned task
- Planned path
- Local A* planner

---

## Task Model

Each task contains:

- Task ID
- Target location
- Priority information
- Ownership status
- Completion status

---

## Voice Notification System

The simulation integrates offline text-to-speech functionality using `pyttsx3`.

Voice notifications are generated when:

- A robot accepts a task.
- A robot completes a task.
- All tasks are completed successfully.

This demonstrates how collaborative robotic systems can communicate important operational events to human operators.

---

## Static Obstacles

The environment contains predefined obstacles that robots must avoid while planning routes.

The A* planner automatically computes alternate paths around these obstacles.

---

## Applications

- Multi-Collaborative Robotic Systems (MCRS)
- Warehouse Automation
- Smart Manufacturing
- Autonomous Mobile Robots
- Industrial Robotics
- Swarm Robotics
- Factory Automation
- Autonomous Fleet Coordination
- Robotics Education
- Artificial Intelligence Research

---

## Future Enhancements

- Conflict-Based Search (CBS)
- Dynamic obstacle avoidance
- Time-expanded A*
- Adaptive swarm intelligence
- Multi-robot collision avoidance
- Robot-to-robot communication
- Battery charging stations
- Reinforcement learning
- ROS 2 integration
- Gazebo simulation
- Digital twin visualization
- Real robotic hardware deployment
- Fleet management dashboard
- LiDAR-based localization
- Distributed consensus algorithms

---

## Requirements

- Python 3.8 or later
- pyttsx3

---

## Dependencies

- pyttsx3

All remaining modules are part of Python's standard library.

---

## Author

Kaushal Reddy

AI & Autonomous Systems Engineer

GitHub: https://github.com/Kaushal1525
````
