class TempTracker:
	def __init__(self):
		self.data = {}
		self.min = None
		self.max = None
		self.modeCount = None
		self.modeVal = None
		self.count = 0
		self.total = 0
	
	def insert(temp):
		if not data:
			self.min = self.max = self.modeVal = self.total = temp
			self.count = self.modeCount = 1

		self.data[temp] = self.data.get(temp, 0) + 1
		self.min = min(self.min, temp)
		self.max = max(self.max, temp)
		if data[temp] > self.modeCount:
			self.modeCount = data[temp]
			self.modeVal = temp
		self.count += 1
		self.total += temp

	def get_max():
		return self.max

	def get_min():
		return self.min

	def get_mean():
		return total/float(count)

	def get_mode():
		return self.modeVal
