from flask_restx.reqparse import RequestParser

page_parser: RequestParser = RequestParser()
page_parser.add_argument('page', type=int, location='args', required=False)
status_parser: RequestParser = RequestParser()
status_parser.add_argument('status', type=int, location='args', required=False)
