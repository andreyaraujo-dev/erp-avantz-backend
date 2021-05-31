from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all, name='get_all_groups'),
    path('create', views.create_group, name='create_group'),
    path('subgroup/1/create/<int:id_group>', views.create_subgroup_level1,
         name='create_subgroup_level1'),
    path('subgroup/2/create/<int:id_subgroup>', views.create_subgroup_level2,
         name='create_subgroup_level2'),
    path('delete/<int:id>', views.delete, name='delete_group'),
    path('update/<int:id>', views.update, name='update_group'),
    path('details/<int:id>', views.details, name='details_group'),
    path('sections', views.get_sections, name='select_sections'),
    path('groups', views.get_groups, name='get_distinct_groups'),
]
