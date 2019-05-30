# -*- coding: utf-8 -*-

from aioli import Package
from aioli_guestbook import service
from .service import VisitService, VisitorService
from .database import VisitModel, VisitorModel
from .controller import HttpController

__version__ = '0.1.0'

export = Package(
    controllers=[HttpController],
    services=[VisitService, VisitorService],
    models=[VisitModel, VisitorModel],
    name='aioli-guestbook',
    description='Example guestbook package'
)
