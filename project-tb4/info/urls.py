from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('student/<slug:class_id>/timetable/', views.timetable, name='timetable'),
    path('student/<slug:stud_id>/marks_list/', views.marks_list, name='marks_list'),
    path('student/<slug:stud_id>/marks_feedack/', views.marks_feedback, name='marks_feedback'),
    path('teacher/<slug:teacher_id>/<int:choice>/Classes/', views.t_clas, name='t_clas'),
    path('teacher/<int:assign_id>/ClassDates/', views.t_class_date, name='t_class_date'),
    path('teacher/<int:ass_c_id>/Cancel/', views.cancel_class, name='cancel_class'),
    path('teacher/<int:assign_id>/Report/', views.t_report, name='t_report'),
    path('teacher/<slug:teacher_id>/t_timetable/', views.t_timetable, name='t_timetable'),
    path('teacher/<int:asst_id>/Free_teachers/', views.free_teachers, name='free_teachers'),
    path('teacher/<int:assign_id>/marks_list/', views.t_marks_list, name='t_marks_list'),
    path('teacher/<int:assign_id>/Students/Marks/', views.student_marks, name='t_student_marks'),
    path('teacher/<int:marks_c_id>/marks_entry/', views.t_marks_entry, name='t_marks_entry'),
    path('teacher/<int:marks_c_id>/marks_entry/confirm/', views.marks_confirm, name='marks_confirm'),
    path('teacher/<int:marks_c_id>/Edit_marks/', views.edit_marks, name='edit_marks'),

]