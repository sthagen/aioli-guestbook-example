# -*- coding: utf-8 -*-

from aioli.package.controller import BaseHttpController, ParamsSchema, RequestProp, Method, route, takes, returns

from .service import VisitService, VisitorService
from .schema import Visit, Visitor, VisitNew, VisitPath


class HttpController(BaseHttpController):
    def __init__(self):
        self.visit = VisitService()
        self.visitor = VisitorService()
        self.log.debug('Guestbook opening')

    async def on_ready(self):
        self.log.debug(f'Guestbook opened at {self.pkg.path}')

    async def on_request(self, request):
        self.log.debug(f'Request received: {request}')

    @route('/', Method.GET, 'List of entries')
    @takes(query=ParamsSchema)
    @returns(Visit, many=True)
    async def visits_get(self, query):
        return await self.visit.get_many(**query)

    @route('/', Method.POST, 'Create entry')
    @takes(body=VisitNew, props=[RequestProp.client_addr])
    @returns(Visit, status=201)
    async def visit_add(self, client_addr, body):
        return await self.visit.create(client_addr, body)

    @route('/{visit_id}', Method.GET, 'Visit details')
    @takes(path=VisitPath)
    @returns(Visit)
    async def visit_get(self, visit_id):
        return await self.visit.get_one(visit_id)

    @route('/{visit_id}', Method.PUT, 'Update entry')
    @takes(body=Visit, path=VisitPath, props=[RequestProp.client_addr])
    @returns(Visit)
    async def visit_update(self, client_addr, body, visit_id):
        return await self.visit.update(client_addr, visit_id, body)

    @route('/{visit_id}', Method.DELETE, 'Delete entry')
    @takes(path=VisitPath, props=[RequestProp.client_addr])
    @returns(status=204)
    async def visit_delete(self, client_addr, visit_id):
        await self.visit.delete(client_addr, visit_id)

    @route('/visitors', Method.GET, 'List of visitors')
    @takes(query=ParamsSchema)
    @returns(Visitor, many=True)
    async def visitors_get(self, query):
        return await self.visitor.get_many(**query)

    @route('/visitors/{visitor_id}', Method.GET, 'Visitor details')
    @returns(Visitor)
    async def visitor_get(self, visitor_id):
        return await self.visitor.get_one(visitor_id)

    @route('/visitors/{visitor_id}/visits', Method.GET, 'Visits by visitor')
    @takes(query=ParamsSchema)
    @returns(Visit)
    async def visitor_entries(self, visitor_id, query):
        query.update({'visitor': visitor_id})
        return await self.visit.get_many(**query)
