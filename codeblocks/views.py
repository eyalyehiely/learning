import logging
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CodeBlockSerializer
from .models import CodeBlock
from django.core.exceptions import ObjectDoesNotExist
from .utils import send_codeblock_update
from drf_yasg.utils import swagger_auto_schema
from .models import CodeBlock
from .serializers import CodeBlockSerializer
from drf_yasg import openapi

logger = logging.getLogger('codeBlocks')

# Define the code parameter in the request body
# Define the code parameter in the request body
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



@swagger_auto_schema(method='get', responses={200: CodeBlockSerializer(many=True)})
@api_view(['GET'])
def get_code_blocks(request):
    try:
        codeBlocks = CodeBlock.objects.all()
        logger.debug("All code blocks provided to the client.")
        all_code_blocks = [{'id': block.id, 'title': block.title, 'instructions': block.instructions, 'code': block.code} for block in codeBlocks]
        return Response({'codeBlocks': all_code_blocks}, status=200)
    
    except Exception as e:
        logger.error(f"Error retrieving code blocks: {e}")
        return Response({'Error': 'Page not found'}, status=404)




@api_view(['GET'])
def get_code_block(request, code_block_id):
    try:
        codeBlock = CodeBlock.objects.get(id=code_block_id)
        logger.debug(f"CodeBlock {codeBlock.title} provided to the client.")
        serializer = CodeBlockSerializer(codeBlock)

        return Response(serializer.data, status=200)
    
    except ObjectDoesNotExist:
        logger.error(f"CodeBlock with id {code_block_id} not found.")
        return Response({'Error': 'Code block not found'}, status=404)
    
    except Exception as e:
        logger.error(f"Error retrieving code block: {e}")
        return Response({'Error': 'An error occurred'}, status=500)






# edit code
@swagger_auto_schema(method='put', request_body=code_param, responses=responses)
@api_view(['PUT'])
def edit_code_block(request, code_block_id):
    try:
        codeBlock = CodeBlock.objects.get(id=code_block_id)
        code = request.data.get('code')
        codeBlock.code = code
        codeBlock.save()
        
        # Send update to the mentor group if the request is from a student
        if request.user.role == 'student':  # Assume you have a user role attribute
            send_codeblock_update(code_block_id, code)

        logger.info(f"CodeBlock {codeBlock.title} updated.")
        return Response({"success": "Code block updated"}, status=200)
    
    except CodeBlock.DoesNotExist:
        logger.error(f"No CodeBlock found with ID {code_block_id}.")
        return Response({"error": f"No CodeBlock found with ID {code_block_id}."}, status=404)
    
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return Response({"error": f"An error occurred: {e}"}, status=500)
    

    
@api_view(['POST'])
def check_user_code(request, code_block_id):
    try:
        user_script = request.data.get('code')
        script_solution = CodeBlock.objects.get(id=code_block_id).solution
        if not script_solution:
            logger.error("No solution found for the given script ID.")
            return Response({"error": "No solution found for the given script ID."}, status=404)
        
        if user_script == script_solution:
            logger.info("User script matches the solution.")
            send_codeblock_update(code_block_id, user_script)
            return Response({"success": "match"}, status=200)
        
        else:
            logger.info("User script does not match the solution.")
            send_codeblock_update(code_block_id, user_script)
            return Response({"fail": "not match"}, status=200)
        
    except CodeBlock.DoesNotExist:
        logger.error(f"No CodeBlock found with ID {code_block_id}.")
        return Response({"error": f"No CodeBlock found with ID {code_block_id}."}, status=404)
    
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return Response({"error": f"An error occurred: {e}"}, status=500)