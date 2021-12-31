total_problems = input()
solutions = []
write_solution = 0
for n in range(int(total_problems)):
    solution = input().split()
    solutions.append(solution)

for m in range(int(total_problems)):
    count = solutions[m].count("1")
    if count>1:
        write_solution += 1
    
print(write_solution)
    