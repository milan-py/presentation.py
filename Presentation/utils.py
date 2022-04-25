class NoneError(Exception):

	def __init__(self, message):
		super().__init__()

	def __str__(self):
		return f"Presentation NoneError: {self.message}"