import asyncio

import redis
from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

import config as cfg

from sql.database import AlchemySqlDb
from sql.models import Base
from utils.repositories import Repository
from utils.schemas import User, UserRequest, Price, Way

sql_db = AlchemySqlDb(cfg.SQLALCHEMY_DATABASE_URL, Base)
redis_db = redis.Redis(host=cfg.REDIS_HOST, port=cfg.REDIS_HOST, db=cfg.REDIS_DB)
repo = Repository(redis_db, sql_db)

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# repo.sql_db.prepare()
# repo.load_users_from_db()
# repo.load_requests_from_db()


"""
PREPARING
"""


# async def main():
#     # user = User.create(2, '323', '654', '321654')
#     await repo.load_requests_from_db()
#     await repo.load_users_from_db()
#     print(await repo.delete_user(2))
#     # req1 = UserRequest.create('btc', Price(target_price=231), Way.up_to)
#     # req2 = UserRequest.create('eth', Price(target_price=3124), Way.up_to)
#     # print(await repo.add_request(1, req1))
#     # print(await repo.add_request(2, req2))
#     # print(await repo.delete_request(1, 1723527122647188736))
#     print(await repo.to_list_unique_requests_for_server())
#     print(await repo.get_all_users())
#     print(await repo.get_all_users_from_db())
#
# if __name__ == '__main__':
#     asyncio.run(main())
