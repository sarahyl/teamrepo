nums = [1,2,3,4]

target = int(input("Please enter an integer: "))

for x in nums:
  for y in nums:
    if x + y == target:
      print("[", nums.index(x), ",", nums.index(y), "]")
      break
     else:
      continue
      
      
