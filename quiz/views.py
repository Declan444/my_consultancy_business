from django.shortcuts import render
from .models import Question, CustomerRequest
from django.core.mail import send_mail
from django.conf import settings


def quiz_view(request):
    if request.method == "POST":
        # Check if this is a second-step POST with just email
        if "email" in request.POST:
            email = request.POST.get("email")
            no_questions = request.session.get("no_questions", [])
            if email:
                try:
                    CustomerRequest.objects.create(email=email)
                    print(f"Email saved: {email}")  # Debug
                except Exception as e:
                    print(f"Error saving email: {e}")
                # Prepare HTML email for user
                ul_list = "".join(f"<li>{q}</li>" for q in no_questions)
                html_message = f"""
                <html>
                <body style='font-family: Arial, sans-serif; background: #f9f9f9; padding: 20px;'>
                    <div style='max-width: 600px; margin: auto; background: #fff; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.05); padding: 30px;'>
                        <h2 style='color: #445261; text-align: center;'>Business Assessment Quiz Results</h2>
                        <p>Hi,</p>
                        <p>Thank you for taking the quiz. Your results indicate you may need help in the following areas:</p>
                        <ul>{ul_list}</ul>
                        <p>I will be in touch soon to discuss how I can help you improve in these areas.</p>
                        <hr style='border: none; border-top: 1px solid #eee;'>
                        <p style='font-size: 0.95em; color: #888;'>Declan Lenahan<br>DL | Business and Digital Consultant<br><a href='mailto:laresearchlabs@gmail.com' style='color: #445261;'>laresearchlabs@gmail.com</a><br><a href='tel:+353868934130' style='color: #445261;'>+353 868934130</a></p>
                    </div>
                </body>
                </html>
                """
                send_mail(
                    subject="Your Business Assessment Quiz Results",
                    message="Thank you for taking the quiz. Your results indicate you may need help in some areas. I will be in touch soon.",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[email],
                    fail_silently=False,
                    html_message=html_message,
                )
                # Send admin email
                admin_message = (
                    f"A customer ({email}) took the quiz and needs help in the following areas:\n\n"
                    + "\n".join(no_questions)
                )
                send_mail(
                    subject="Quiz Follow-up Needed",
                    message=admin_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=["laresearchlabs@gmail.com"],
                    fail_silently=False,
                )
            # Clear session
            if "no_questions" in request.session:
                del request.session["no_questions"]
            return render(
                request, "quiz/results.html", {"needs_help": False, "email_saved": True}
            )

        # First step: handling answers
        answers = [
            value for key, value in request.POST.items() if key.startswith("answers_")
        ]
        questions = list(Question.objects.all())
        if len(answers) != len(questions):
            return render(
                request,
                "quiz/quiz.html",
                {"questions": questions, "error": "Please answer all questions."},
            )
        # Find questions answered 'no'
        no_questions = [
            q.question_text for q, a in zip(questions, answers) if a == "no"
        ]
        needs_help = bool(no_questions)
        # Store in session for next step
        request.session["no_questions"] = no_questions
        return render(request, "quiz/results.html", {"needs_help": needs_help})

    # GET request – show the quiz
    questions = Question.objects.all()
    return render(request, "quiz/quiz.html", {"questions": questions})
