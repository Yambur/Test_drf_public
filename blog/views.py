from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from blog.models import Article
from blog.serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.role == 'subscriber':
            return Article.objects.filter(is_public=True)
        return Article.objects.all()

    def perform_create(self, serializer):
        if self.request.user.role == 'author':
            serializer.save(author=self.request.user)
        else:
            return Response({"Только автор может создавать публикацию"}, status=status.HTTP_403_FORBIDDEN)

    def perform_destroy(self, instance):
        if instance.author == self.request.user:
            instance.delete()
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def perform_update(self, serializer):
        if serializer.instance.author == self.request.user:
            serializer.save()
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
