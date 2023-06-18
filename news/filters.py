from django_filters import FilterSet # ����������� filterset, ���-�� ������������ �������� ���������
from .models import Post
 
 
# ������ ������
class NewsFilter(FilterSet):
    # ����� � ���� ������ ���� ������������ ������ � ������� ����, �� ������� ����� ������������� (�.�. �����������) ���������� � �������
    class Meta:
        model = Post

        fields = {
            'header':['icontains'],
            'authorArticle__account': ['exact'],
            'creationTime': ['gt'],
        }