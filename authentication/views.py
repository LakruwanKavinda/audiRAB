"""
Views for user authentication and related functionalities.
"""

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
# Import the PDFFile and Message models from the correct module
from .models import PDFFile, Message


def signup(request):
    """
    View for user signup.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        # Create user
        User.objects.create_user(
            username=username, password=password, email=email)
        return JsonResponse({'message': 'User created successfully'})
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)


def user_login(request):
    """
    View for user login.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'})
        else:
            return JsonResponse({'message': 'Invalid credentials'}, status=400)
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)


@csrf_exempt
def upload_pdf(request):
    """
    View for uploading PDF files.
    """
    if request.method == 'POST' and request.FILES.get('pdf'):
        pdf_file = request.FILES['pdf']
        new_pdf = PDFFile(file=pdf_file, name=pdf_file.name)
        new_pdf.save()
        return JsonResponse({'message': 'PDF file uploaded successfully'})
    else:
        return JsonResponse({'message': 'Invalid request'}, status=400)


def search_pdf(request):
    """
    View for searching PDF files.
    """
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            results = PDFFile.objects.filter(Q(name__icontains=query))
            # You can add additional search criteria here
            # For example, search by author, genre, etc.
            return JsonResponse({'results': [{'name': pdf.name, 'url': pdf.file.url} for pdf in results]})
        else:
            return JsonResponse({'message': 'Please provide a search query'}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request'}, status=400)


def generate_story(request):  # Remove the request argument
    """
    View for generating a story.
    """
    if request.method == 'POST':
        topic = request.POST.get('topic')
        if topic:
            # Assuming openai is properly defined elsewhere
            # response = openai.Completion.create(
            #     engine="text-davinci-003",  # Choose the GPT-3 model you prefer
            #     prompt=f"Generate a story about {topic}.",
            #     max_tokens=200  # Adjust the maximum length of the generated story
            # )
            # story = response.choices[0].text.strip()
            story = "Story generation is disabled temporarily."
            return JsonResponse({'story': story})
        else:
            return JsonResponse({'message': 'Please provide a topic'}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request'}, status=400)


def view_pdf(pdf_id):
    """
    View for viewing a PDF file.
    """
    pdf = get_object_or_404(PDFFile, pk=pdf_id)
    return JsonResponse({'url': pdf.file.url})


# chat
@login_required
def send_message(request):
    """
    View for sending a message.
    """

    if request.method == 'POST':
        receiver_id = request.POST.get('receiver_id')
        content = request.POST.get('content')
        receiver = User.objects.get(pk=receiver_id)
        message = Message.objects.create(
            sender=request.user, receiver=receiver, content=content)
        return JsonResponse({'message_id': message.pk})
    else:
        return JsonResponse({'message': 'Invalid request'}, status=400)


@login_required
def get_messages(request):
    """
    View for retrieving messages.
    """
    if request.method == 'GET':

        messages = Message.objects.filter(receiver=request.user)
        message_data = [{'sender': message.sender.username, 'content': message.content,
                         'timestamp': message.timestamp} for message in messages]
        return JsonResponse({'messages': message_data})
    else:
        return JsonResponse({'message': 'Invalid request'}, status=400)
