"""
API views for AJAX functionality
Handles JSON responses for announcement viewing, search, and other interactive features
"""

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import json
from django.db.models import Q

# Import models (these would need to be defined in models.py)
# from .models import Announcement, Subject, StudentRecommendation, StudentProfile


@login_required
@require_http_methods(["GET"])
def get_announcement_details(request, announcement_id):
    """Get announcement details for modal display"""
    try:
        # Mock announcement data - replace with actual model query
        announcement_data = {
            'id': announcement_id,
            'title': 'Sample Announcement',
            'content': 'This is a sample announcement content that would be displayed in the modal.',
            'is_urgent': False,
            'target_audience': 'all',
            'target_audience_display': 'All Students',
            'target_course': '',
            'target_year': None,
            'target_section': '',
            'created_at': '2024-01-15T10:30:00Z',
            'posted_by_name': 'Admin User'
        }
        
        return JsonResponse(announcement_data)
    
    except Exception as e:
        return JsonResponse({
            'error': 'Failed to load announcement details',
            'message': str(e)
        }, status=400)


@login_required
@require_http_methods(["POST"])
def delete_announcement(request, announcement_id):
    """Delete announcement via AJAX"""
    try:
        # Mock deletion - replace with actual model deletion
        # announcement = get_object_or_404(Announcement, id=announcement_id)
        # announcement.delete()
        
        return JsonResponse({
            'success': True,
            'message': 'Announcement deleted successfully'
        })
    
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        }, status=400)


@login_required
@require_http_methods(["GET"])
def search_content(request):
    """Global search functionality"""
    try:
        query = request.GET.get('q', '').strip()
        
        if len(query) < 2:
            return JsonResponse({
                'subjects': [],
                'announcements': [],
                'message': 'Query too short'
            })
        
        # Mock search results - replace with actual database queries
        subjects = [
            {
                'id': 1,
                'name': 'Data Structures',
                'code': 'CS301'
            },
            {
                'id': 2,
                'name': 'Database Systems',
                'code': 'CS401'
            }
        ]
        
        announcements = [
            {
                'id': 1,
                'title': 'Exam Schedule Updated',
                'content_preview': 'Please check the updated exam schedule...'
            }
        ]
        
        # Filter based on query
        filtered_subjects = [s for s in subjects if query.lower() in s['name'].lower() or query.lower() in s['code'].lower()]
        filtered_announcements = [a for a in announcements if query.lower() in a['title'].lower()]
        
        return JsonResponse({
            'subjects': filtered_subjects,
            'announcements': filtered_announcements
        })
    
    except Exception as e:
        return JsonResponse({
            'error': 'Search failed',
            'message': str(e)
        }, status=400)


@login_required
@require_http_methods(["POST"])
def generate_recommendations(request):
    """Generate AI recommendations for student"""
    try:
        # Mock recommendation generation - replace with actual AI logic
        recommendations = [
            {
                'title': 'Study Schedule Recommendation',
                'description': 'Based on your recent performance, we recommend focusing on Data Structures this week.'
            },
            {
                'title': 'Assignment Reminder',
                'description': 'You have an upcoming assignment in Database Systems due next week.'
            }
        ]
        
        # Here you would actually create StudentRecommendation objects
        # for rec in recommendations:
        #     StudentRecommendation.objects.create(
        #         student=request.user.studentprofile,
        #         title=rec['title'],
        #         description=rec['description'],
        #         recommendation_type='study_plan'
        #     )
        
        return JsonResponse({
            'success': True,
            'recommendations': recommendations,
            'message': f'{len(recommendations)} recommendations generated'
        })
    
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        }, status=400)


@login_required
@require_http_methods(["POST"])
def dismiss_recommendation(request, recommendation_id):
    """Dismiss a specific recommendation"""
    try:
        # Mock dismissal - replace with actual model update
        # recommendation = get_object_or_404(StudentRecommendation, id=recommendation_id, student=request.user.studentprofile)
        # recommendation.is_dismissed = True
        # recommendation.save()
        
        return JsonResponse({
            'success': True,
            'message': 'Recommendation dismissed'
        })
    
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        }, status=400)


@login_required
@require_http_methods(["POST"])
def generate_attendance_report(request):
    """Generate attendance report as PDF"""
    try:
        from django.http import HttpResponse
        from reportlab.pdfgen import canvas
        from reportlab.lib.pagesizes import letter
        import io
        
        # Create a file-like buffer to receive PDF data
        buffer = io.BytesIO()
        
        # Create the PDF object, using the buffer as its "file"
        p = canvas.Canvas(buffer, pagesize=letter)
        
        # Draw some sample content
        p.drawString(100, 750, f"Attendance Report for {request.user.get_full_name()}")
        p.drawString(100, 700, "Subject: Data Structures")
        p.drawString(100, 680, "Total Classes: 45")
        p.drawString(100, 660, "Attended: 42")
        p.drawString(100, 640, "Percentage: 93.3%")
        
        # Close the PDF object cleanly
        p.showPage()
        p.save()
        
        # Get the value of the BytesIO buffer and create response
        pdf = buffer.getvalue()
        buffer.close()
        
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="attendance_report.pdf"'
        
        return response
    
    except Exception as e:
        return JsonResponse({
            'error': 'Failed to generate report',
            'message': str(e)
        }, status=400)


@login_required
@require_http_methods(["POST"])
def ai_chat_response(request):
    """Handle AI chat messages"""
    try:
        data = json.loads(request.body)
        message = data.get('message', '')
        session_id = data.get('session_id', '')
        
        if not message:
            return JsonResponse({
                'error': 'No message provided'
            }, status=400)
        
        # Mock AI response - replace with actual AI service
        ai_responses = [
            "I understand you're asking about study materials. Let me help you with that.",
            "Based on your course, I recommend focusing on the fundamental concepts first.",
            "Would you like me to create a study schedule for your upcoming exams?",
            "That's a great question! Let me break it down for you step by step.",
            "I can help you with that topic. Here's what you need to know..."
        ]
        
        # Simple mock response based on message content
        response = "I understand your question. "
        if 'study' in message.lower():
            response += "Here are some study recommendations for you."
        elif 'schedule' in message.lower():
            response += "I can help you plan your study schedule."
        elif 'exam' in message.lower():
            response += "Let me give you some exam preparation tips."
        else:
            response += "How else can I assist you with your academic needs?"
        
        # Here you would integrate with actual AI service
        # ai_response = ai_service.get_response(message, user_context=request.user.studentprofile)
        
        return JsonResponse({
            'response': response,
            'session_id': session_id
        })
    
    except Exception as e:
        return JsonResponse({
            'error': 'Failed to process AI request',
            'message': str(e)
        }, status=400)


@login_required
@require_http_methods(["GET"])
def get_student_context(request):
    """Get student context for AI chat"""
    try:
        # Mock student context - replace with actual profile data
        context = {
            'name': request.user.get_full_name(),
            'course': 'Computer Science',
            'year': '3',
            'section': 'A',
            'subjects': [
                {'name': 'Data Structures', 'code': 'CS301'},
                {'name': 'Database Systems', 'code': 'CS401'},
                {'name': 'Operating Systems', 'code': 'CS402'}
            ],
            'attendance_summary': {
                'overall_percentage': 85.5,
                'total_classes': 120,
                'attended': 102
            }
        }
        
        return JsonResponse(context)
    
    except Exception as e:
        return JsonResponse({
            'error': 'Failed to load student context',
            'message': str(e)
        }, status=400)
