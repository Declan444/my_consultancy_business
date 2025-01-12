from django.shortcuts import render
from .models import Question

def quiz_view(request):
    if request.method == 'POST':
        # Collect all answers
        answers = [
            value
            for key, value in request.POST.items()
            if key.startswith('answers_')
        ]

        # Ensure all questions are answered
        if len(answers) != Question.objects.count():
            return render(request, 'quiz/quiz.html', {
                'questions': Question.objects.all(),
                'error': 'Please answer all questions.'
            })

        # Check if any answer is "no"
        needs_help = 'no' in answers
        return render(request, 'quiz/results.html', {'needs_help': needs_help})

    # Fetch all questions to display in the quiz
    questions = Question.objects.all()
    return render(request, 'quiz/quiz.html', {'questions': questions})
