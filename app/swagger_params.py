from drf_yasg import openapi

person_params = [ 
	openapi.Parameter("skip", openapi.IN_QUERY, type=openapi.TYPE_INTEGER, default=0, required=True),
	openapi.Parameter("limit", openapi.IN_QUERY, type=openapi.TYPE_INTEGER, default=25, required=True),
]
