import logging,json
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import send_codeblock_update
from drf_yasg.utils import swagger_auto_schema
from .models import *
from .serializers import *
from drf_yasg import openapi
from codeblocks.serializers import *




code_param = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'code': openapi.Schema(type=openapi.TYPE_STRING, description='Code to update the code block with')
    }
)

# Define possible responses
responses = {
    200: openapi.Response(description="Code block updated", examples={
        'application/json': {"success": "Code block updated"}
    }),
    404: openapi.Response(description="No CodeBlock found with the given ID", examples={
        'application/json': {"error": "No CodeBlock found with ID {code_block_id}."}
    }),
    500: openapi.Response(description="An error occurred", examples={
        'application/json': {"error": "An error occurred: {error_message}"}
    }),
}


# defined logger
codeblock_logger = logging.getLogger('code_block')
submission_logger = logging.getLogger('submission')



#  get all code blocks 
@swagger_auto_schema(method='get', responses={200: CodeBlockSerializer(many=True)})
@api_view(['GET'])
def get_code_blocks(request):
    try:
        codeBlocks = CodeBlock.objects.all()
        codeblock_logger .debug("All code blocks provided to the client.")
        all_code_blocks = [
            {'id': block.id, 'title': block.title, 'instructions': block.instructions, 'code': block.code} for block in
            codeBlocks]
        return Response({'codeBlocks': all_code_blocks}, status=200)

    except Exception as e:
        codeblock_logger .error(f"Error retrieving code blocks: {e}")
        return Response({'Error': 'Page not found'}, status=404)


#checking user code : bonus
@swagger_auto_schema(method='post', request_body=code_param, responses=responses)
@api_view(['POST'])
def check_user_code(request, code_block_id):
    try:
        data = request.data
        user_id = data.get('clientUUID')
        user_script = request.data.get('code')
        codeblock = get_object_or_404(CodeBlock, id=code_block_id)
        script_solution = codeblock.solution
        
        if not script_solution:
            codeblock_logger.error("No solution found for the given code block ID.")
            return Response({"error": "No solution found for the given code block ID."}, status=404)

        if user_script == script_solution:
            codeblock_logger.info("User script matches the solution.")
            send_codeblock_update(code_block_id, user_script)

            return Response({"success": "match"}, status=200)
        else:
            codeblock_logger.info("User script does not match the solution.")
            send_codeblock_update(code_block_id, user_script)
            return Response({"fail": "not match"}, status=200)

    except CodeBlock.DoesNotExist:
        codeblock_logger.error(f"No CodeBlock found with ID {code_block_id}.")
        return Response({"error": f"No CodeBlock found with ID {code_block_id}."}, status=404)

    except Exception as e:
        codeblock_logger.error(f"An error occurred: {e}")
        return Response({"error": f"An error occurred: {e}"}, status=500)

@api_view(['POST'])
def fetch_client_uuid_to_server(request):
    data = json.loads(request.body)
    user_id = data.get('clientUUID')

    if not user_id:
        submission_logger.debug("ClientUUID is missing")
        return Response({'error': 'ClientUUID is missing'}, status=400)
    else:
        submission_logger.debug(f"ClientUUID accepted,{user_id}")
        return Response({'success': f"ClientUUID accepted,{user_id}"}, status=200)


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------




def create_new_submission(code_block_id, user_id):
    codeblock = get_object_or_404(CodeBlock, id=code_block_id)
    new_submission_data = {
        'code_block': codeblock.id,
        'user_id': user_id,
        'user_code': codeblock.code,  # Initialize with the default value from CodeBlock
    }
    serializer = SubmissionSerializer(data=new_submission_data)
    if serializer.is_valid():
        new_submission = serializer.save()
        submission_logger.debug("submission created")
        return new_submission, None
    return None, serializer.errors






@swagger_auto_schema(method='post', request_body=SubmissionSerializer)
@api_view(['POST'])
def codeblock_submission(request):
    data = request.data
    user_id = data.get('clientUUID')
    code_block_id = data.get('code_block_id')
    
    if not code_block_id:
        return Response({'error': 'CodeBlock ID is missing'}, status=400)
    
    if not user_id:
        return Response({'error': 'User ID is missing'}, status=400)

    codeblock = get_object_or_404(CodeBlock, id=code_block_id)
    check_submission = Submission.objects.filter(code_block=codeblock, user_id=user_id)
    if check_submission.exists():
        return Response({'error': 'Submission already exists'}, status=400)
    
    # Create the new Submission object directly
    submission = Submission.objects.create(
        code_block=codeblock,
        user_id=user_id,
        user_code=codeblock.code  # Initialize with the default value from CodeBlock
    )

    # Prepare the response data
    response_data = {
        'id': submission.id,
        'code_block_id': submission.code_block.id,
        'user_id': submission.user_id,
        'user_code': submission.user_code,
        'passed': submission.passed,
        'created_at': submission.created_at
    }

    return Response(response_data, status=201)



@api_view(['GET', 'DELETE'])
def codeblock_submission_detail(request, code_block_id):
    user_id = request.GET.get('user_id')
    code_block_id = int(code_block_id)
    if not user_id:
        return Response({'error': 'User ID is missing'}, status=400)
        
    codeblock = get_object_or_404(CodeBlock, id=code_block_id)

    if request.method == "GET":
        submission = Submission.objects.filter(code_block_id=code_block_id, user_id=user_id).first()
        if submission:
            serializer = SubmissionSerializer(submission)
            submission_logger.debug("submission exists")
            return Response(serializer.data, status=200)
        else:
            new_submission, errors = create_new_submission(code_block_id, user_id)
            if new_submission:
                serializer = SubmissionSerializer(new_submission)
                return Response(serializer.data, status=201)
            return Response({'error': 'Unable to create submission', 'details': errors}, status=400)

    elif request.method == "DELETE":
        submission = Submission.objects.filter(code_block_id=codeblock.id, user_id=user_id).first()
        if submission:
            submission.delete()
            return Response(status=204)
        else:
            return Response({'error': 'No submission found to delete'}, status=400)



@api_view(['PUT'])
def edit_submission(request, code_block_id):
    user_id = request.GET.get('user_id')
    if not user_id:
        return Response({'error': 'User ID is missing'}, status=400)
    
    codeblock = get_object_or_404(CodeBlock, id=code_block_id)
    submission = Submission.objects.filter(code_block_id=codeblock.id, user_id=user_id).first()

    if submission:
        data = request.data.copy()
        data['code_block_id'] = code_block_id  # Ensure code_block_id is included
        data['user_id'] = user_id  # Ensure user_id is included
        if 'user_code' not in data:
            data['user_code'] = submission.user_code  # Ensure user_code is included
        serializer = SubmissionSerializer(submission, data=data)
        if serializer.is_valid():
            new_sub = serializer.save()
            submission_logger.debug("submission saved")
            send_codeblock_update(codeblock.id, new_sub.user_code)
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    else:
        return Response({'error': 'Submission not found'}, status=404)




@api_view(['POST'])
def log_visitor(request):
    data = request.data
    client_uuid = data.get('clientUUID')
    url = data.get('url')

    if not client_uuid:
        return Response({'error': 'ClientUUID is missing'}, status=400)
    
    if not url:
        return Response({'error': 'URL is missing'}, status=400)

    # Log the visitor
    visitor = Visitor.objects.create(client_uuid=client_uuid, url=url,role='unknown')
    visitor.save()

    # Count the number of visitors to the same URL
    visitor_count = Visitor.objects.filter(url=url).count()

    # Determine role
    if visitor_count > 1:
        role = 'student'
        visitor.role = 'student'
        visitor.save()

    else:
        role = 'teacher'
        visitor.role = 'teacher'
        visitor.save()


    return Response({'clientUUID': client_uuid, 'url': url, 'role': role}, status=200)