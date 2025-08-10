"""
URL configuration for API endpoints
These URLs handle AJAX requests from the frontend JavaScript
"""

from django.urls import path
from . import api_views

app_name = 'api'

urlpatterns = [
    # Announcement API endpoints
    path('announcements/<int:announcement_id>/', api_views.get_announcement_details, name='announcement_details'),
    path('announcements/<int:announcement_id>/delete/', api_views.delete_announcement, name='delete_announcement'),
    
    # Search API endpoints
    path('search/', api_views.search_content, name='search_content'),
    
    # Recommendation API endpoints
    path('recommendations/generate/', api_views.generate_recommendations, name='generate_recommendations'),
    path('recommendations/<int:recommendation_id>/dismiss/', api_views.dismiss_recommendation, name='dismiss_recommendation'),
    
    # Attendance API endpoints
    path('attendance/report/', api_views.generate_attendance_report, name='attendance_report'),
    
    # AI Chat API endpoints
    path('ai/chat/', api_views.ai_chat_response, name='ai_chat_response'),
    path('student/context/', api_views.get_student_context, name='student_context'),
]
