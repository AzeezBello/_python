#Find the cube root of a perfect cube

x = int(input('Enter an integer: '))
step = 0


while step < x:
    multiple = step * step * step
    # print(step, multiple)
    if multiple - x <= 0.3 and multiple > x:
        print(f"""Approximate cube root of {x} is {step} because {step} cube is {step*step*step}""")
        break
    step += 0.01




