def moveTower(height, fromPole, toPole, sparePole):
    if height == 1:
        moveDisk(fromPole, toPole)
    else:
        moveTower(height - 1, fromPole, sparePole, toPole)
        moveTower(1, fromPole, toPole, sparePole)
        moveTower(height - 1, sparePole, toPole, fromPole)


def moveDisk(fp, tp):
    print(f"moving disk from {fp} to {tp}")


moveTower(5, "A", "B", "C")
