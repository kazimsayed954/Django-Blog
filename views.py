from django.shortcuts import render

#Dummy Data
posts=[
{
	'author':'kazim',
	'title':'Blog Post 1',
	'content':'First Post content',
	'date_posted':'July 5,2021'
},
{
	'author':'Jane Doe',
	'title':'Blog Post 2',
	'content':'Second Post content',
	'date_posted':'July 4,2021'
},
]



# Create your views here.

def home(request):
	context={
	'posts':posts
	}
	return render(request,'blog/home.html', context)

def about(request):
	return render(request,'blog/about.html')