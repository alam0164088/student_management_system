from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.db.models import Q
from .models import Student, Subject
from .forms import StudentForm
from django.urls import reverse_lazy
from django.contrib import messages

# Class-Based Views for Students
class StudentListView(ListView):
    model = Student
    template_name = 'students/student_list.html'
    context_object_name = 'students'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')  # সার্চ কোয়েরি পাওয়া
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) |
                Q(email__icontains=query) |
                Q(department__icontains=query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')  # সার্চ কোয়েরি টেমপ্লেটে পাঠানো
        return context

class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/student_detail.html'

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student_list')

    def form_valid(self, form):
        messages.success(self.request, "Student added successfully!")
        return super().form_valid(form)

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student_list')

    def form_valid(self, form):
        messages.success(self.request, "Student updated successfully!")
        return super().form_valid(form)

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/student_confirm_delete.html'
    success_url = reverse_lazy('student_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Student deleted successfully!")
        return super().delete(request, *args, **kwargs)

# Function-Based Views for Combined Lists
def student_subject_list(request):
    students = Student.objects.all()
    subjects = Subject.objects.all()
    return render(request, 'students/student_subject_list.html', {
        'students': students,
        'subjects': subjects,
    })

def engineering_faculty_list(request):
    query = request.GET.get('q', '')  # সার্চ কোয়েরি পাওয়া
    all_students = Student.objects.all()
    cse_students = Student.objects.filter(department='CSE')
    eee_students = Student.objects.filter(department='EEE')
    civil_students = Student.objects.filter(department='CIVIL')
    me_students = Student.objects.filter(department='ME')
    subjects = Subject.objects.all()

    if query:
        all_students = all_students.filter(
            Q(name__icontains=query) |
            Q(email__icontains=query) |
            Q(department__icontains=query)
        )
        cse_students = cse_students.filter(
            Q(name__icontains=query) |
            Q(email__icontains=query) |
            Q(department__icontains=query)
        )
        eee_students = eee_students.filter(
            Q(name__icontains=query) |
            Q(email__icontains=query) |
            Q(department__icontains=query)
        )
        civil_students = civil_students.filter(
            Q(name__icontains=query) |
            Q(email__icontains=query) |
            Q(department__icontains=query)
        )
        me_students = me_students.filter(
            Q(name__icontains=query) |
            Q(email__icontains=query) |
            Q(department__icontains=query)
        )

    return render(request, 'students/engineering_faculty_list.html', {
        'all_students': all_students,
        'cse_students': cse_students,
        'eee_students': eee_students,
        'civil_students': civil_students,
        'me_students': me_students,
        'subjects': subjects,
        'query': query,  # সার্চ কোয়েরি টেমপ্লেটে পাঠানো
    })