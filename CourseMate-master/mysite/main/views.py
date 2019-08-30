from django.shortcuts import render #render is for templates
from django.http import HttpResponse 
from .models import Tutorial
from .models import School
from .models import Course  
from .models import SchoolCourse
from main.forms import CourseForm 
from main.forms import SchoolCourseForm
from main.forms import SchoolForm
 
from django.views.generic import TemplateView
import datetime

# Create your views here.
def homepage(request): #for any view, always pass request 
    school_list = School.objects.order_by('name')
    
    return render(request=request, #so u can reference things inside your template to do with the user
                    template_name="main/home.html", context = {'school_list' : school_list})

def review(request):
	my_form=CourseForm()
	if request.method == "POST":
		my_form = CourseForm(request.POST)
		if my_form.is_valid():
			print(my_form.cleaned_data)
			Course.objects.create(my_form.cleaned_data)
			my_form.save()
		else:
			print(my_form.errors)
	return render(request=request, #so u can reference things inside your template to do with the user
                    template_name="main/review.html", context={"form": my_form})
					#once u make a review, it should direct u to the class page 

def classPage(request):
	return render(request=request, #so u can reference things inside your template to do with the user
                    template_name="main/course.html", context={"form": my_form})

def addCourse(request):
	my_form=SchoolForm()
	if request.method=="POST":
		my_form =SchoolForm(request.POST)
		if my_form.is_valid():
			print("Valid")
			my_form.save()
			print("saved)")
			return render(request=request, #so u can reference things inside your template to do with the user
                    template_name="main/course.html", context={"form": my_form})
		else:
			my_form=SchoolCourseForm()
			print("error")
			print(my_form.errors)
	print("done")
	return render(request=request, #so u can reference things inside your template to do with the user
                    template_name="main/addCourse.html", context={"form": my_form})

# def addCourse(request):
# 	print("hello")
# 	my_form =SchoolCourseForm()
# 	if 'courseNumber' in request.POST:
# 		print("post")
# 		my_form = SchoolCourseForm(request.POST)
# 		if my_form.is_valid():
# 			print("Valid")
# 			my_form.save()
# 			print("saved)")
# 			return render(request=request, #so u can reference things inside your template to do with the user
#                     template_name="main/course.html", context={"form": my_form})
# 			# print(my_form.cleaned_data)
# 			# SchoolCourse.objects.create(my_form.cleaned_data)
# 		else:
# 			my_form=SchoolCourseForm()
# 			print("error")
# 			print(my_form.errors)
# 	print("done")
# 	return render(request=request, #so u can reference things inside your template to do with the user
#                     template_name="main/addCourse.html", context={"form": my_form})

def about(request):
	return render(request=request, #so u can reference things inside your template to do with the user
                    template_name="main/AboutUs.html")
def login(request):
	now=datetime.datetime.now()
	return render(request=request, template_name="main/login.html", context={'datetime_now':now})

def search(request):
	course_list = SchoolCourse.objects.order_by('name')
	return render(request=request, template_name="main/search.html", context={"course_list": course_list})

def SCU(request):
	return render(request=request, template_name="main/SCU.html", context={})

def course(request):
	post=Course.objects.order_by("name")
	return render(request=request, template_name="main/course.html", context={})

def current_date_time(request):
	now=datetime.datetime.now()
	html = "<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)

# def CourseView(TemplateView):
# 	# template_name = "main/review.html"

# 	def get(self, request):
# 		form = CourseForm()
# 		return render(request=request, template_name="main/review.html", context={'form': form})
# 	def post(self, request):
# 		form = CourseForm(request.POST)
# 		if form.is_valid():
# 			text = form.cleaned_data['reviewTitle']

# 		args = {'form': form, 'text': text}
# 		return render(request=request, template_name="main/review.html", context=args)	

# def addCourse(request):
# 	my_form=SchoolCourse()
# 	courseNumber=request.POST.get('courseNumber')
# 	name=request.POST.get('name')
# 	course_info = SchoolCourse(courseNumber=courseNumber, name=name)
# 	course_info.save()
# 	print("Hello form is submitted.")
# 	return render(request=request, #so u can reference things inside your template to do with the user
#                     template_name="main/addCourse.html", context={'my_form': my_form})


def review_form_submission(request):
	courseNumber=request.POST.get('courseNumber', False)
	name=request.POST.get('name', False)

	review_title=request.POST.get('review_title', False)
	review_content=request.POST.get('review_content', False)
	review_published=request.POST.get('review_published', False)

	professor_name=request.POST.get('professor_name', False)

	gradeReceived=request.POST.get('gradeReceived', False)
	easyRating=request.POST.get('easyRating', False)
	InterestingRating=request.POST.get('InterestingRating', False)

	homework=request.POST.get('homework', False)
	pop_quizzes=request.POST.get('pop_quizzes', False)
	webcast=request.POST.get('webcast', False)
	numProjects=request.POST.get('numProjects', False)
	numTests=request.POST.get('numTests', False)
	testDiff=request.POST.get('testDiff', False)
	time_spent=request.POST.get('time_spent', False)
	
	course_info= Course(courseNumber=courseNumber, name=name, review_title=review_title, review_content=review_content, 
						review_published=review_published,professor_name=professor_name, gradeReceived=gradeReceived, 
						easyRating=easyRating, InterestingRating=InterestingRating,homework=homework, pop_quizzes=pop_quizzes,
						webcast=webcast, numProjects=numProjects, numTests=numTests, testDiff=testDiff, time_spent=time_spent)
	course_info.save()

	print("Hello form is submitted.")
	return render(request=request, template_name="main/review.html")

 
