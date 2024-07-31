# swagger.py
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from codeblocks.serializers import *

schema_view = get_schema_view(
    openapi.Info(
        title="Your API Title",
        default_version='v1',
        description="API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


code_param = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'code': openapi.Schema(type=openapi.TYPE_STRING, description='Code to update the code block with')
    }
)

# Define possible responses for check_user_code
check_user_code_responses = {
    200: openapi.Response(description="User code checked", examples={
        'application/json': {"success": "match"},
        'application/json': {"fail": "not match"}
    }),
    404: openapi.Response(description="No CodeBlock found with the given ID", examples={
        'application/json': {"error": "No CodeBlock found with ID {code_block_id}."}
    }),
    500: openapi.Response(description="An error occurred", examples={
        'application/json': {"error": "An error occurred: {error_message}"}
    }),
}

# Define possible responses for codeblock_submission
codeblock_submission_responses = {
    201: SubmissionSerializer,
    400: openapi.Response(description="Bad Request")
}

# Define possible responses for codeblock_submission_detail
codeblock_submission_detail_responses = {
    200: SubmissionSerializer(many=True),
    400: openapi.Response(description="Bad Request"),
    404: openapi.Response(description="Not Found"),
    204: openapi.Response(description="No Content")
}
