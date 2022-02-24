from rest_framework import viewsets, generics, permissions
from django_filters import rest_framework as filters

from office.models import Project
from office.serializers.project_serializer import ProjectSerializer
from office.pagination import StandardResultsSetPagination
from utils.employee_info import Evolution


class ProjectFilter(filters.FilterSet):
    client_name = filters.CharFilter(field_name='client_name')
    client_phn_num = filters.CharFilter(field_name='client_phn_num')
    date_line = filters.DateFilter(field_name='date_line')
    is_active = filters.BooleanFilter(field_name='is_active')
    budget = filters.NumericRangeFilter(field_name='budget')
    status = filters.ChoiceFilter(field_name='pay_purpose', choices=Evolution.task_status())

    class Meta:
        model = Project
        fields = ['client_name', 'client_phn_num', 'date_line', 'status', 'budget']


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAdminUser]
    pagination_class = StandardResultsSetPagination


class ProjectFilterView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProjectFilter