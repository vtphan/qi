from ..qi import app

##------------------------------------------------------------
class index( app ):
	route = '/'

	def get(self):
		return 'this is index'

if __name__ == '__main__':
	app.run(8000)