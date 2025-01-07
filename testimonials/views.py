from django.http import JsonResponse
from testimonials.models import Testimonial
import random

def random_testimonial(request):
    testimonials = Testimonial.objects.all()
    if testimonials.exists():
        testimonial = random.choice(testimonials)
        return JsonResponse({
            'name': testimonial.name,
            'company': testimonial.company,
            'text': testimonial.text,
        })
    else:
        return JsonResponse({'error': 'No testimonials available'}, status=404)
