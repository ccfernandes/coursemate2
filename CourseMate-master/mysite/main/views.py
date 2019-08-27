from django.shortcuts import render #render is for templates
from django.http import HttpResponse 
from .models import Tutorial
from .models import School
from .models import Course  
from .models import SchoolCourse
from main.forms import CourseForm 
from main.forms import SchoolCourseForm
from main.forms import SchoolForm
 
from django.views.generic import TemplateView, ListView
from django.db.models import Q
import datetime


# Create your views here.
def homepage(request): #for any view, always pass request 
    school_list = School.objects.order_by('name')
    
    return render(request=request, #so u can reference things inside your template to do with the user
                    template_name="main/home.html", context = {'school_list' : school_list})

def review(request):
	my_form=CourseForm()
	# course_form=SchoolCourseForm()
	course_list = SchoolCourse.objects.all()
	if request.method == "POST":
		my_form = CourseForm(request.POST)
		if my_form.is_valid():
			# print(my_form.cleaned_data)
			# Course.objects.create(my_form.cleaned_data)
			my_form.save()
			return render(request=request, template_name="main/course.html", context={'my_form': my_form, 'course_list': course_list})
		else:
			print(my_form.errors)
					#once u make a review, it should direct u to the class page 
	return render(request=request, #so u can reference things inside your template to do with the user
                    template_name="main/review.html", context={"form": my_form,'course_list': course_list})

def SearchPage(request):
	# model = School
	# template_name = 'search.html'
	# queryset=School.objects.order_by('name')
	# context={"object_list": queryset}
	# def get_queryset(self):
	# 	query = self.request.GET.get('q')
	# 	object_list = School.objects.filter(
	# 		Q(name__icontains=query) | Q(abbrev__icontains=query)
	# 		)
	# 	# object_list=School.objects.exclude(name__isnull=True)
	# 	# return object_list
	# 	return render(request=request, template_name='search.html', context={"object_list": queryset})
 	query=request.GET.get('q', '')
 	if query:
 		result=School.objects.filter(name__icontains=query)
 	else:
 		result=[]	
 	# queryset=School.objects.order_by('name')
 	return render(request=request, template_name="main/search.html", context={"result": result})

# class SearchPage(ListView):
# 	model=School
# 	template_name='main/search.html'
# 	# queryset=School.objects.filter(name__icontains="Santa Clara University")
# 	def get_queryset(self):
# 	# 	return School.objects.filter(name__icontains="Santa Clara University")
# 		return School.objects.filter(Q(name__icontains='Boston') | Q(abbrev__icontains='UCSB'))

def course(request):
	def get(self, request):
		form=CourseForm()
		posts=Course.objects.all()
		print(posts)
		return render(request=request, template_name="main/course.html", context={'form': form})
	post=Course.objects.order_by("name")
	return render(request=request, template_name="main/course.html", context={})

def college(request):
	return render(request=request, template_name="main/uniBase.html", context={})

def addCourse(request):
	print("hello")
	my_form =SchoolCourseForm()
	if request.method=="POST":
	# print("post")
		my_form = SchoolCourseForm(request.POST)
		if my_form.is_valid():
			my_form.save()
			print("saved)")
			return render(request=request, #so u can reference things inside your template to do with the user
	                  template_name="main/course.html", context={"form": my_form})
				# print(my_form.cleaned_data)
				# SchoolCourse.objects.create(my_form.cleaned_data)
		else:
			my_form=SchoolCourseForm()
			print("error")
			print(my_form.errors)
	print("done")
	return render(request=request, #so u can reference things inside your template to do with the user
                    template_name="main/addCourse.html", context={"form": my_form})

def about(request):
	return render(request=request, #so u can reference things inside your template to do with the user
                    template_name="main/AboutUs.html")
def login(request):
	now=datetime.datetime.now()
	return render(request=request, template_name="main/login.html", context={'datetime_now':now})

# def search(request):
# 	course_list = SchoolCourse.objects.order_by('name')
# 	return render(request=request, template_name="main/search.html", context={"course_list": course_list})

# def SCU(request):
# 	return render(request=request, template_name="main/SCU.html", context={})

# def UCSB(request):
# 	return render(request=request, template_name="main/course.html", context={})

# def UCB(request):
# 	return render(request=request, template_name="main/course.html", context={})

def current_date_time(request):
	now=datetime.datetime.now()
	html = "<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)

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

 
