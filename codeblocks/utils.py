# utils.py
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def send_codeblock_update(code_block_id, code):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f"codeblock_{code_block_id}",
        {
            "type": "code_update",
            "code": code,
        }
    )