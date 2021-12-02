import math

def move_sub_old(input, horizontal: int = 0, depth: int = 0):
  with open(input, 'r') as reader:
    instructions = reader.readlines()
  for inst in instructions:
    dir, amount = inst.split(' ')
    if dir == 'forward':
      horizontal += int(amount)
    elif dir == 'up':
      depth -= int(amount)
    elif dir == 'down':
      depth += int(amount)
  return horizontal, depth

def move_sub(input, horizontal: int = 0, depth: int = 0, aim: int = 0):
  with open(input, 'r') as reader:
    instructions = reader.readlines()
  for inst in instructions:
    dir, amount = inst.split(' ')
    if dir == 'forward':
      horizontal += int(amount)
      depth += aim*int(amount)
    elif dir == 'up':
      aim -= int(amount)
    elif dir == 'down':
      aim += int(amount)
  return horizontal, depth

if __name__ == "__main__":
  assert math.prod(move_sub_old('test_input.txt')) == 150, 'Expected 150'
  print(f"Part 1: {math.prod(move_sub_old('input.txt'))}")
  assert math.prod(move_sub('test_input.txt')) == 900, 'Expected 900'
  print(f"Part 2: {math.prod(move_sub('input.txt'))}")
  