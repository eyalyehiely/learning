import logging
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import send_codeblock_update
from drf_yasg.utils import swagger_auto_schema
from .models import *
from .serializers import *
from backend.swagger import code_param,check_user_code_responses,codeblock_submission_responses,codeblock_submission_detail_responses

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
@swagger_auto_schema(method='post', request_body=code_param, responses=check_user_code_responses)
@api_view(['POST'])
def check_user_code(request, code_block_id):
    try:
        user_script = request.data.get('code')
        script_solution = CodeBlock.objects.get(id=code_block_id).solution
        if not script_solution:
            codeblock_logger .error("No solution found for the given script ID.")
            return Response({"error": "No solution found for the given script ID."}, status=404)

        if user_script == script_solution:
            codeblock_logger .info("User script matches the solution.")
            send_codeblock_update(code_block_id, user_script)
            return Response({"success": "match"}, status=200)

        else:
            codeblock_logger .info("User script does not match the solution.")
            send_codeblock_update(code_block_id, user_script)
            return Response({"fail": "not match"}, status=200)

    except CodeBlock.DoesNotExist:
        codeblock_logger .error(f"No CodeBlock found with ID {code_block_id}.")
        return Response({"error": f"No CodeBlock found with ID {code_block_id}."}, status=404)

    except Exception as e:
        codeblock_logger .error(f"An error occurred: {e}")
        return Response({"error": f"An error occurred: {e}"}, status=500)






# codeblock submission
@swagger_auto_schema(method='post', request_body=SubmissionSerializer, responses=codeblock_submission_responses)
@api_view(['POST'])
def codeblock_submission(request, user_id):
    if request.method == 'POST':
        codeblock_id = request.data.get('code_block_id')

        codeblock = get_object_or_404(CodeBlock, id=codeblock_id)

        check_submission = Submission.objects.filter(code_block=codeblock, user_id=user_id)
        if check_submission.exists():
            return Response({'error': 'Submission already exists'}, status=400)
        
        # create submission if not exist
        else:
            serializer = SubmissionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)

            return Response(serializer.errors, status=400)





# codeblock_submission data
@swagger_auto_schema(method='get', responses=codeblock_submission_detail_responses)
@swagger_auto_schema(method='put', request_body=SubmissionSerializer, responses=codeblock_submission_detail_responses)
@swagger_auto_schema(method='delete', responses=codeblock_submission_detail_responses)
@api_view(['GET', 'PUT', 'DELETE'])
def codeblock_submission_detail(request,code_block_id):

    # check if code block exist
    codeblock = get_object_or_404(CodeBlock, id=code_block_id)


    if request.method == "GET":
        user_id =  request.data.get('user_id')
        submission = Submission.objects.filter(code_block_id=codeblock.id, user_id=user_id)

        #check if there is already submission exist
        if submission.exists():
            serializer = SubmissionSerializer(submission, many=True)
            submission_logger("submission exist")
            return Response(serializer.data, status=200)

        else:
            return Response({'error': 'No submission found'}, status=400)

    # saving the new submission
    elif request.method == "PUT":
        user_id =  request.data.get('user_id')
        submission = Submission.objects.filter(code_block_id=codeblock.id, user_id=user_id)
        if submission.exists():
            serializer = SubmissionSerializer(submission, data=request.data)
            if serializer.is_valid():
                new_sub = serializer.save()
                submission_logger("submission saved")
                send_codeblock_update(code_block_id,new_sub.user_code)
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=400)
        else:
            codeblock_submission(request, user_id)
