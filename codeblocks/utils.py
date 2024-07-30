from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def send_codeblock_update(codeblock_id, code):
    channel_layer = get_channel_layer()
    group_name = f'codeblock_{codeblock_id}'

    # Send code to room group
    async_to_sync(channel_layer.group_send)(
        group_name,
        {
            'type': 'code_update',
            'code': code
        }
    )