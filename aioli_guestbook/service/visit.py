# -*- coding: utf-8 -*-

from aioli.package.service import BaseService
from aioli.exceptions import AioliException, NoMatchFound

from .. import database

from .visitor import VisitorService


class VisitService(BaseService):
    __model__ = database.VisitModel
    VISITS_MAX = 10

    def __init__(self):
        self.visitor = VisitorService()

    async def get_authored(self, visit_id, remote_addr):
        visit = await self.get_one(visit_id)
        if visit.visitor.ip_addr != remote_addr:
            raise AioliException('Not allowed from your IP', 403)

        return visit

    async def get_many(self, visitor_id=None, **kwargs):
        if visitor_id:
            kwargs['visitor'] = visitor_id

        return await self.db.get_many(**kwargs)

    async def get_one(self, visit_id):
        return await self.db.get_one(id=visit_id)

    async def delete(self, remote_addr, visit_id):
        visit = await self.get_authored(visit_id, remote_addr)
        await visit.delete()

    async def update(self, remote_addr, visit_id, payload):
        visit = await self.get_authored(visit_id, remote_addr)
        return await self.db.update(visit, payload)

    async def create(self, remote_addr, body):
        visit = body
        visit_count = await self.db.count(visitor__ip_addr__iexact=remote_addr)
        if visit_count >= self.VISITS_MAX:
            raise AioliException(
                status=400,
                message=f'Max {self.VISITS_MAX} entries per IP. Try deleting some old ones.'
            )

        async with self.db_manager.database.transaction():
            city, country = await self.visitor.ipaddr_location(remote_addr)

            visitor = dict(
                name=visit.pop('visitor_name'),
                ip_addr=remote_addr,
                location=f'{city}, {country}'
            )

            try:
                visit['visitor'] = await self.visitor.db.get_one(**visitor)
            except NoMatchFound:
                visit['visitor'] = await self.visitor.db.create(**visitor)
                self.log.info(f"New visitor: {visit['visitor'].name}")

            visit_new = await self.db.create(**visit)
            self.log.info(f'New visit: {visit_new.id}')

        return await self.db.get_one(id=visit_new.id)
