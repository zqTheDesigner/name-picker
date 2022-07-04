from fastapi import FastAPI, APIRouter
import random

app = FastAPI(title='Name Picker', openapi_url='/openapi.json')

api_router = APIRouter()

PRODUCT_TEAM_NAMES = ['Wayne', 'Aalind', 'Joel', 'Sherealyn', 'Giang', 'Zhang Qiao']

@api_router.get('/prod-team-rand-name', status_code=200)
def get_random_name() -> list:
	'''
	Takes a list of names and return a random list
	'''
	return random.sample(PRODUCT_TEAM_NAMES,len(PRODUCT_TEAM_NAMES))

app.include_router(api_router)

if __name__ == '__main__':
	import uvicorn

	uvicorn.run(app, host='0.0.0.0', port=8001, log_level='debug')