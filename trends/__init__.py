class Base(type):
	def __new__(cls, clsname, bases, attrs):
		if 'trends' not in attrs:
			raise AttributeError("Please provide at least on trend.")
		super().__new__(cls, clsname, bases, attrs)


class Derived(metaclass=Base):
	def __init__(self, trends)
		self.trends = trends

	def run(self):
		return "Running in {self}"

trader = Derived('mavgs')
trader.run()