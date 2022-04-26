class NoneError(Exception):

	def __init__(self, message):
		super().__init__()
		self.message = message

	def __str__(self):
		return f"Presentation NoneError: {self.message}"