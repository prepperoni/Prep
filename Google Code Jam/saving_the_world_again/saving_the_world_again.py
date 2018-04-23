'''

CCSSS = 12
CSCSS = 10
224610
CSSCS = 8
22448
SCCSS = 9
12459
SCSCS = 7
12347
SSCCS = 6
12246
'''

def calcDmg(s):
  base = 1
  dmg = 0

  for c in s:
    if c == 'S':
      dmg += base
    elif c == 'C':
      base <<= 1

  return dmg

t = int(input())
for i in range(1, t + 1):
  line = input().split(' ')
  D = int(line[0])
  pat = line[1]

  print("Case #{}: ".format(i), end='')

  numS = 0
  for c in pat:
  	if c == 'S':
  		numS += 1
  		if numS > D:
  			print("IMPOSSIBLE")
  			break

  if numS > D:
  	continue

  hacks = 0
  curDmg = calcDmg(pat)
  while curDmg > D:
  	for i in range(len(pat) - 1, 0, -1):
  		if pat[i] == 'S' and pat[i - 1] == 'C':
  			pat = pat[:i - 1] + 'SC' + pat[i+1:]
  			hacks += 1
  			break

  	curDmg = calcDmg(pat)

  print(hacks)
