import motor.motor_asyncio
from config import REQ_CHANNEL

class JoinReqs:

    def __init__(self):
        from config import JOIN_REQS_DB
        if JOIN_REQS_DB:
            self.client = motor.motor_asyncio.AsyncIOMotorClient(JOIN_REQS_DB)
            self.db = self.client["JoinReqs"]
            self.col = self.db[str(REQ_CHANNEL)]
        else:
            self.client = None
            self.db = None
            self.col = None

    def isActive(self):
        if self.client is not None:
            return True
        else:
            return False

    async def add_user(self, user_id, first_name, username, date):
        try:
            await self.col.insert_one({"_id": (user_id),"user_id": (user_id), "first_name": first_name, "username": username, "date": date})
        except:
            pass
