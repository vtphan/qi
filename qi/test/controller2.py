from qi import app


class show( app ):
	def get(self, id):
		return 'this is show.get', id

	def put(self):
		return 'show.put'

if __name__ == '__main__':
	app.run(8001)