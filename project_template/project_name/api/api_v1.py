from django.core.handlers.wsgi import WSGIRequest
from ninja import NinjaAPI, Schema
from ninja.parser import Parser
from ninja.renderers import BaseRenderer
from orjson import orjson
from pydantic import BaseModel, validator


class ORJSONRenderer(BaseRenderer):
	media_type = "application/json"
	
	def render(self, request, data, *, response_status):
		if isinstance(data, BaseModel):
			return orjson.dumps(data.__dict__)
		return orjson.dumps(data)


class ORJSONParser(Parser):
	def parse_body(self, request):
		return orjson.loads(request.body)


api = NinjaAPI(version='1.0', csrf=True, parser=ORJSONParser(), renderer=ORJSONRenderer())
