from django.shortcuts import render
from . models import Course,Category,Tag

def course_list(request):
   courses =Course.objects.all().order_by('-date')
   categories = categories = Category.objects.all()
   tags = Tag.objects.all()
   context = {

      'courses' :courses,
      'categories': categories,
      'tags': tags
   }
   
   return render(request, 'courses.html',context)


def course_detail(request, category_slug, course_id):
   
    course = Course.objects.get(category__slug=category_slug, id = course_id)
    courses = Course.objects.all().order_by('-date') 
    categories = categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {

      'course': course,
      'categories': categories,
      'tags': tags
        
    }

    return render(request, 'course.html', context)