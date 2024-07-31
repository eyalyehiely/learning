from django.test import TestCase

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import CodeBlock, Submission

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def codeblock():
    return CodeBlock.objects.create(title="Test Code Block", instructions="Test Instructions", code="print('Hello World')", solution="print('Hello World')")

@pytest.mark.django_db
def test_get_code_blocks(api_client, codeblock):
    url = reverse('get_code_blocks')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['codeBlocks']) == 1
    assert response.data['codeBlocks'][0]['title'] == "Test Code Block"


@pytest.mark.django_db
def test_check_user_code(api_client, codeblock):
    url = reverse('check_user_code', args=[codeblock.id])
    data = {'code': "print('Hello World')"}
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['success'] == "match"

@pytest.mark.django_db
def test_codeblock_submission(api_client, codeblock):
    url = reverse('codeblock_submission', args=[1])
    data = {'code_block_id': codeblock.id, 'user_id': 1, 'code': "print('Hello World')"}
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db
def test_codeblock_submission_detail_get(api_client, codeblock):
    url = reverse('codeblock_submission_detail', args=[codeblock.id])
    data = {'user_id': 1}
    response = api_client.get(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK or response.status_code == status.HTTP_400_BAD_REQUEST

@pytest.mark.django_db
def test_codeblock_submission_detail_put(api_client, codeblock):
    url = reverse('codeblock_submission_detail', args=[codeblock.id])
    data = {'user_id': 1, 'code': "print('Hello World')"}
    response = api_client.put(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK or response.status_code == status.HTTP_400_BAD_REQUEST
