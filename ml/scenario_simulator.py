from digital_twin import CorrosionTwin

def simulate(ci0, velocity, days, plan):
    twin = CorrosionTwin(velocity, ci0)
    traj = []

    for d in range(days):
        if d in plan:
            twin.maintain(plan[d])
        traj.append(twin.step())
    return traj
