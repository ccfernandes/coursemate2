from django.db import models
from datetime import datetime 
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms import ModelForm

# Create your models here.

class Tutorial(models.Model): 
    tutorial_title=models.CharField(max_length=200)
    tutorial_content=models.TextField()
    tutorial_published=models.DateTimeField("data published", default=datetime.now())

    def __str__(self):
        return self.tutorial_title



class School(models.Model):
    #fields 
    name=models.CharField(max_length=40)
    # location=models.CharField(max_length=30)

    def __str__(self):
    	return self.name

class SchoolForm(ModelForm):
	class Meta: 
		model = School
		fields = ['name']


# class Department(models.Model):
# 	name=models.CharField(max_length=30)
# 	school=models.ManyToManyField(School) #connects DepartmentName to School (i think)
# 	#many departments belong to one school 
	
# 	def __str__(self):
# 		return self.name

#the course itself
class SchoolCourse(models.Model):
	school=models.ForeignKey(School, blank=True, null=True, on_delete=models.DO_NOTHING)

	courseNumber=models.CharField(max_length=10, null=True, blank=True)
	name=models.CharField(max_length=30, null=True, blank=True)

	def __str__(self):
		return self.courseNumber

#the reviews for each course 
class Course(models.Model):
	#general info
	# courseNum=models.ForeignKey(SchoolCourse, blank=True, null=True, on_delete=models.DO_NOTHING)

	courseNumber=models.CharField(max_length=10, null=True, blank=True)
	name=models.CharField(max_length=30, null=True, blank=True)
	
	professor_name=models.CharField(max_length=20, null=True, blank=True, default='')
	#ratings, 1-10
	easyRating=models.IntegerField(
                                    choices=[('',''), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
	InterestingRating=models.IntegerField(
    								choices=[('',''), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])

	numProjects=models.IntegerField(choices=[('',''), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), 
    									  ('6', '6'), ('7', '7'),('8', '8'),('9', '9'), ('10', '10')])

	# department=models.ForeignKey('Department', on_delete=models.DO_NOTHING) #connects Course to DepartmentName
	#a class only belongs to a single department(usually)
	#the review itself, not data 

	numTests=models.IntegerField(
    							choices=[('',''), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), 
    							('6', '6'), ('7', '7'),('8', '8'),('9', '9'), ('10', '10'), ('11', '11'), 
    							('12', '12'), ('13', '13'), ('14', '14'), ('15', '15')])
	testDiff=models.IntegerField(
    							choices=[('',''), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])

	#amount of work
	time_spent=models.CharField(max_length=5,
    							choices=[('',''), ('1', '1-2'), ('2', '3-4'), ('3', '5-6'), ('4', '7-8'), ('5', '9-10'), 
    										('6', '10-12'), ('7', '12-14'),('8', '15-17'),('9', '18-20'), ('10', '20+')])

	homework=models.BooleanField(choices=[('',''), (True, 'Yes'), (False, 'No')])
	pop_quizzes=models.BooleanField(choices=[('',''), (True, 'Yes'), (False, 'No')])
	webcast=models.BooleanField(choices=[('',''), (True, 'Yes'), (False, 'No')])

	gradeReceived=models.CharField(max_length=3, 
        choices=[('',''), ('A', 'A'), ('A-', 'A-'), ('B+', 'B+'), ('B', 'B'), ('B-', 'B-'), ('C+', 'C+'), 
                ('C', 'C'), ('C-', 'C-'), ('D+', 'D+'), ('D', 'D'), ('D-', 'D-'), ('F', 'F'), 
                ('NP', 'NP'), ('P', 'P'), ('N/A', 'N/A')]) 

	review_title=models.CharField("Review Title: ", max_length=100)
	review_content=models.CharField("Review Content: ", max_length=200, null=True, blank=True)
	review_published=models.DateTimeField("data published", default=datetime.now())


# 	def __str__(self):
# 		return self.courseNumber

# class CourseForm(ModelForm):
# 	class Meta: 
# 		model=Course 
# 		fields=['courseNumber', 'review_title', 'name', 'review_title', 'review_content', 'review_published'
# 				'professor_name', 'gradeReceived', 'easyRating', 'InterestingRating', 'homework'
# 				'pop_quizzes', 'webcast', 'numProjects', 'numTests', 'testDiff', 'time_spent']
				
