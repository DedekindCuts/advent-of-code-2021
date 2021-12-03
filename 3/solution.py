def _mode(it, rev: bool = False, tied = None):
  ct = {}
  for x in it:
    ct[x] = ct.get(x, 0) + 1
  items = sorted(ct.items(), key=lambda x: x[0]==tied)
  items = sorted(items, key=lambda x: x[1], reverse=rev)
  m, _ = items[-1]
  return m

def _transpose(x):
  return [[j[i] for j in x] for i in range(len(x[0]))]

class DiagnosticReport():
  def __init__(self, input_file):
    with open(input_file, 'r') as reader:
      self.data = reader.read().splitlines()
      
  def gamma_rate(self):
    return ''.join([_mode(x) for x in _transpose(self.data)])
  
  def epsilon_rate(self):  
    return ''.join([_mode(x, rev=True) for x in _transpose(self.data)])
  
  def power_consumption(self):
    return int(self.gamma_rate(), 2) * int(self.epsilon_rate(), 2)
  
  def oxygen_generator_rating(self):
    numbers = self.data
    pos = 0
    while len(numbers) > 1 and pos < len(numbers[0]):
      mode = _mode([n[pos] for n in numbers], tied = '1')
      numbers = [n for n in numbers if n[pos] == mode]
      pos += 1
    result, = numbers
    return result
  
  def co2_scrubber_rating(self):
    numbers = self.data
    pos = 0
    while len(numbers) > 1 and pos < len(numbers[0]):
      mode = _mode([n[pos] for n in numbers], rev=True, tied = '0')
      numbers = [n for n in numbers if n[pos] == mode]
      pos += 1
    result, = numbers
    return result
  
  def life_support_rating(self):
    return int(self.oxygen_generator_rating(), 2) * int(self.co2_scrubber_rating(), 2)

if __name__ == "__main__":
  assert DiagnosticReport('test_input.txt').power_consumption() == 198
  print(DiagnosticReport('input.txt').power_consumption())
  assert DiagnosticReport('test_input.txt').life_support_rating() == 230
  print(DiagnosticReport('input.txt').life_support_rating())
