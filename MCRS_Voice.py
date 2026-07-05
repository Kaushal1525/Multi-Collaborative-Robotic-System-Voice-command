import math
import random
import time
import heapq
import pyttsx3

# =====================================================
# VOICE SYSTEM (EVENT-DRIVEN)
# =====================================================
engine = pyttsx3.init()
engine.setProperty('rate', 165)
engine.setProperty('volume', 1.0)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# =====================================================
# CONFIGURATION
# =====================================================
NUM_ROBOTS = 8
NUM_TASKS = 4
GRID_SIZE = 30
MAX_CYCLES = 40

LOW_ENERGY = 25
CYCLE_DELAY = 2.0
STEP_DELAY = 1.0

# =====================================================
# A* PLANNER
# =====================================================
class AStar:
    def __init__(self):
        self.moves = [(1,0),(-1,0),(0,1),(0,-1)]

    def heuristic(self, a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])

    def plan(self, start, goal, obstacles):
        pq = [(0, start)]
        came = {}
        cost = {start: 0}

        while pq:
            _, cur = heapq.heappop(pq)
            if cur == goal:
                break

            for dx, dy in self.moves:
                nx, ny = cur[0]+dx, cur[1]+dy
                if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
                    if (nx, ny) in obstacles:
                        continue
                    new_cost = cost[cur] + 1
                    if (nx, ny) not in cost or new_cost < cost[(nx, ny)]:
                        cost[(nx, ny)] = new_cost
                        priority = new_cost + self.heuristic((nx, ny), goal)
                        heapq.heappush(pq, (priority, (nx, ny)))
                        came[(nx, ny)] = cur

        path = []
        cur = goal
        while cur != start and cur in came:
            path.append(cur)
            cur = came[cur]
        path.reverse()
        return path

# =====================================================
# TASK
# =====================================================
class Task:
    def __init__(self, tid):
        self.id = tid
        self.x = random.randint(5, GRID_SIZE-5)
        self.y = random.randint(5, GRID_SIZE-5)
        self.priority = random.randint(1,5)
        self.owner = None
        self.done = False

# =====================================================
# ROBOT
# =====================================================
class Robot:
    def __init__(self, rid):
        self.id = rid
        self.x = random.randint(0, GRID_SIZE-1)
        self.y = random.randint(0, GRID_SIZE-1)
        self.energy = random.randint(60, 100)
        self.task = None
        self.path = []
        self.planner = AStar()

    def dist(self, x, y):
        return math.hypot(self.x - x, self.y - y)

# =====================================================
# PLANNING PHASE (EXPLICIT A*)
# =====================================================
def planning_phase(robots, tasks, obstacles):
    print("\n📐 PLANNER VIEW (A* PATH COMPUTATION)")
    print("-"*60)

    plans = {}

    for r in robots:
        if r.task or r.energy < LOW_ENERGY:
            continue

        available = [t for t in tasks if not t.done and t.owner is None]
        if not available:
            continue

        best_task, best_path, best_cost = None, None, float("inf")

        for t in available:
            path = r.planner.plan((r.x, r.y), (t.x, t.y), obstacles)
            if path and len(path) < best_cost:
                best_task, best_path, best_cost = t, path, len(path)

        if best_task:
            plans[r.id] = (best_task, best_path)
            print(f"Robot {r.id:02d} planned path to Task {best_task.id} | Path length {len(best_path)}")
            time.sleep(0.6)

    return plans

# =====================================================
# DECISION PHASE
# =====================================================
def decision_phase(robots, plans):
    print("\n🧠 DECISION PHASE")
    print("-"*60)

    for r in robots:
        if r.id in plans:
            task, path = plans[r.id]
            if task.owner is None:
                task.owner = r.id
                r.task = task
                r.path = path
                msg = f"Robot {r.id} has accepted task {task.id}"
                print("🤖", msg)
                speak(msg)
                time.sleep(0.6)

# =====================================================
# EXECUTION PHASE
# =====================================================
def execute_phase(robots):
    for r in robots:
        if not r.task:
            continue

        if r.path:
            nx, ny = r.path.pop(0)
            r.x = nx
            r.y = ny
            r.energy -= 0.5

        if r.dist(r.task.x, r.task.y) < 1:
            msg = f"Robot {r.id} has completed task {r.task.id}"
            print("✅", msg)
            speak(msg)
            r.task.done = True
            r.task.owner = None
            r.task = None
            r.path = []
            time.sleep(0.8)

# =====================================================
# DASHBOARD
# =====================================================
def dashboard(cycle, robots, tasks):
    print(f"\n🏭 SYSTEM CYCLE {cycle}")
    print("-"*70)

    for r in robots:
        state = "IDLE" if not r.task else f"TASK-{r.task.id}"
        print(f"Robot {r.id:02d} | Pos({r.x:3d},{r.y:3d}) | Energy {r.energy:3.0f}% | {state}")

    remaining = len([t for t in tasks if not t.done])
    print(f"\nRemaining Tasks: {remaining}")

# =====================================================
# MAIN
# =====================================================
robots = [Robot(i) for i in range(NUM_ROBOTS)]
tasks = [Task(i) for i in range(NUM_TASKS)]

# Static factory obstacles
obstacles = {
    (12,12),(12,13),(12,14),
    (18,18),(19,18),(20,18)
}

for cycle in range(1, MAX_CYCLES + 1):
    dashboard(cycle, robots, tasks)
    time.sleep(CYCLE_DELAY)

    if all(t.done for t in tasks):
        msg = "All tasks have been completed successfully. System shutting down safely."
        print("\n🎉", msg)
        speak(msg)
        break

    plans = planning_phase(robots, tasks, obstacles)
    decision_phase(robots, plans)
    execute_phase(robots)

print("\n🛑 Simulation Ended")
