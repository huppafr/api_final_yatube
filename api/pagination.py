from rest_framework import pagination
from rest_framework.response import Response

from .models import Follow


class CustomFollowPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'user': self.request.user.username,
            'following': Follow.objects.all()
        })
