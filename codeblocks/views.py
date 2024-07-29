import logging
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CodeBlockSerializer
from .models import CodeBlock
from django.core.exceptions import ObjectDoesNotExist

logger = logging.getLogger('codeBlocks')

@api_view(['GET'])
def get_code_blocks(request):
    try:
        codeBlocks = CodeBlock.objects.all()
        logger.debug("All code blocks provided to the client.")
        all_code_blocks = [{'id': block.id, 'title': block.title, 'code': block.code} for block in codeBlocks]
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