from django.forms import ModelForm
from main.models import School
from main.models import Course
from main.models import SchoolCourse 
from django import forms   

# Create the form class.
class SchoolForm(forms.Form):
     name=forms.CharField(label="Your School: ", max_length=40)
     # class Meta:
     #    model = School
     #    fields = ['name']

class SchoolCourseForm(forms.ModelForm):
    courseNumber=forms.CharField(max_length=10, label="Course Number: ")
    name=forms.CharField(max_length=30, label="Course Name: ")

    class Meta:
        model = SchoolCourse
        fields = ['courseNumber', 'name']

# class CourseForm(forms.Form):
# 	#general info
# 	courseNumber=forms.CharField(max_length=10, null=True)
# 	name=forms.CharField(max_length=30, null=True, blank=True)
	
# 	#the review itself, not data 
# 	review_title=forms.CharField(max_length=30, null=True)
# 	review_content=forms.TextField(max_length=200, null=True)
# 	review_published=forms.DateTimeField("data published", default=datetime.now())

# 	professor_name=forms.CharField(max_length=20, null=True)

# 	gradeReceived=forms.CharField(max_length=2)

# 	#ratings, 1-10
# 	easyRating=forms.IntegerField(
# 		validators=[MaxValueValidator(5), MinValueValidator(1)],
# 		help_text='(1)= :D (5)= >:(', null=True, blank=True)
# 	InterestingRating=forms.IntegerField(
# 		validators=[MaxValueValidator(5), MinValueValidator(1)],
# 		help_text='(1)= :D (5)= >:(', null=True, blank=True)

# 	#amount of work
# 	homework=forms.BooleanField()
# 	pop_quizzes=forms.BooleanField(null=True)
# 	webcast=forms.BooleanField(null=True)
# 	numProjects=forms.IntegerField(
# 		validators=[MaxValueValidator(10), MinValueValidator(0)], null=True, blank=True)
# 	numTests=forms.IntegerField(
# 		validators=[MaxValueValidator(15), MinValueValidator(0)], null=True, blank=True)
# 	testDiff=forms.IntegerField(
# 		validators=[MaxValueValidator(5), MinValueValidator(1)],
# 		help_text='(1)= :D (5)= >:(', null=True, blank=True) #rated 1-10
# 	time_spent=forms.IntegerField(
# 		validators=[MaxValueValidator(15), MinValueValidator(0)],
# 		help_text='For classes that took more than 15 hours, just put 15', null=True, blank=True)

# from django import forms 

class CourseForm(forms.ModelForm):
    # courseNumber=forms.ModelChoiceField(queryset=SchoolCourse.objects.order_by('name'))
    professor_name = forms.CharField(max_length=20, label="Professor's Name:")
    
    #tuple where first is the actual value to be set on the model and second is the human readable name
    InterestingRating = forms.ChoiceField(label= "Interesting Material? (1-lowest, 5-highest):", 
    								choices=[('',''), ('1','1'), ('2','2'), ('3','3'), ('4','4'), ('5','5')])
    easyRating = forms.ChoiceField(label="Easy Class? (1-lowest, 5-highest):",
                                    choices=[('',''), ('1','1'), ('2','2'), ('3','3'), ('4','4'), ('5','5')])

    numProjects = forms.ChoiceField(label= "Number of Projects?:", 
    								choices=[('',''), ('0','0'), ('1','1'), ('2','2'), ('3','3'), ('4','4'), ('5','5'), 
                                            ('6','6'), ('7','7'), ('8','8'), ('9','9'), ('10','10')])
    numTests = forms.ChoiceField(label= "Number of Tests?:", 
    							choices=[('',''), ('0','0'), ('1','1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), 
                                ('6', '6'), ('7', '7'),('8', '8'),('9', '9'), ('10', '10'), ('11', '11'), 
                                ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15')])
    testDiff = forms.ChoiceField(label= "Test Difficulty?:", 
    									choices=[('',''), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    time_spent = forms.ChoiceField(label= "Time Spent on Class Per Week in Hours?:", 
    								choices=[('',''), ('1', '1-2'), ('2', '3-4'), ('3', '5-6'), ('4', '7-8'), ('5', '9-10'), 
    										('6', '10-12'), ('7', '12-14'),('8', '15-17'),('9', '18-20'), ('10', '20+')])
    homework = forms.ChoiceField(label= "Is there Homework?:", choices=[('',''), ('True', 'Yes'), ('False', 'No')])
    # attendance = forms.ChoiceField(label= "Attendance Mandatory?:", choices[(True, 'Yes'), (False, 'No')])
    webcast = forms.ChoiceField(label= "Webcast?:", choices=[('',''), ('True', 'Yes'), ('False', 'No')])
    pop_quizzes = forms.ChoiceField(label= "Pop Quizzes?:", choices=[('',''), ('True', 'Yes'), ('False', 'No')])
    gradeReceived = forms.ChoiceField(label= "Grade Recieved:", 
        choices=[('',''), ('A', 'A'), ('A-', 'A-'), ('B+', 'B+'), ('B', 'B'), ('B-', 'B-'), ('C+', 'C+'), 
                ('C', 'C'), ('C-', 'C-'), ('D+', 'D+'), ('D', 'D'), ('D-', 'D-'), ('F', 'F'), 
                ('NP', 'NP'), ('P', 'P'), ('N/A', 'N/A')]) 
    review_title = forms.CharField(label= "Review Title:", max_length=100)
    review_content = forms.CharField(label= "Review Content:",widget = forms.Textarea)

    class Meta:
        model = Course
        fields = ['courseNumber', 'name', 'professor_name', 'easyRating', 'InterestingRating',
                    'numProjects', 'numTests', 'testDiff', 'time_spent', 'homework', 'pop_quizzes',
                    'webcast', 'gradeReceived', 'review_title', 'review_content', 'review_published']
        help_texts = {

        }


# 	# Creating a form to add an article.
# # form = SchoolForm()

# 	# Creating a form to change an existing article.
# # school = School.objects.get(pk=1)
# # form = SchoolForm(instance=school)
