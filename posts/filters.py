from django_filters import FilterSet, CharFilter, DateFilter
from .models import Post

class PostFilter(FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains', label='Optional. Post title contains.')
    content = CharFilter(field_name='content', lookup_expr='icontains', label='Optional. Post content contains')
    start_date = DateFilter(field_name='created_date', lookup_expr='gte', label='Optional. Post with date created greater than or equal to. format - mm/dd/yyyy')
    end_date = DateFilter(field_name='created_date', lookup_expr='lte', label='Optional. Post with date created lesser than or equal to. format - mm/dd/yyyy')

    class Meta:
        model = Post
        exclude = ['user', 'link', 'created_date', 'updated_date']
