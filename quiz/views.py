from django.shortcuts import render
from .models import Question, CustomerRequest
from django.core.mail import send_mail
from django.conf import settings

def quiz_view(request):
    if request.method == 'POST':
        # Check if this is a second-step POST with just email
        if 'email' in request.POST:
            email = request.POST.get('email')
            if email:
                try:
                    CustomerRequest.objects.create(email=email)
                    print(f"Email saved: {email}")  # Debug
                except Exception as e:
                    print(f"Error saving email: {e}")
                # Send notification email
                send_mail(
                    subject="New Customer Request",
                    message=f"A customer has requested help. Their email is: {email}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=["laresearchlabs@gmail.com"],
                    fail_silently=False,
                )
            return render(request, 'quiz/results.html', {'needs_help': False, 'email_saved': True})

        # First step: handling answers
        answers = [
            value
            for key, value in request.POST.items()
            if key.startswith('answers_')
        ]

        if len(answers) != Question.objects.count():
            return render(request, 'quiz/quiz.html', {
                'questions': Question.objects.all(),
                'error': 'Please answer all questions.'
            })

        needs_help = 'no' in answers
        return render(request, 'quiz/results.html', {'needs_help': needs_help})

    # GET request – show the quiz
    questions = Question.objects.all()
    return render(request, 'quiz/quiz.html', {'questions': questions})
