# INF 601 - Advanced Python
# Illia Ivanov
# Mini Project 4

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.utils import timezone
from django.http import JsonResponse
from datetime import datetime, timedelta
from .models import DailyEntry, DailyTask
from .forms import DailyEntryForm, DailyTaskForm, UserRegisterForm


def home(request):
    """Home page view - shows calendar and recent entries"""
    if request.user.is_authenticated:
        recent_entries = DailyEntry.objects.filter(user=request.user)[:5]
        context = {
            'recent_entries': recent_entries,
        }
        return render(request, 'journal/home.html', context)
    return render(request, 'journal/landing.html')


def register(request):
    """User registration view"""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Account created successfully! Welcome, {user.username}!')
            return redirect('journal:home')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def entry_list(request):
    """View all journal entries"""
    entries = DailyEntry.objects.filter(user=request.user)
    context = {
        'entries': entries,
    }
    return render(request, 'journal/entry_list.html', context)


@login_required
def entry_detail(request, pk):
    """View a specific journal entry with tasks"""
    entry = get_object_or_404(DailyEntry, pk=pk, user=request.user)
    tasks = entry.tasks.all()

    context = {
        'entry': entry,
        'tasks': tasks,
    }
    return render(request, 'journal/entry_detail.html', context)


@login_required
def entry_create(request):
    """Create a new journal entry"""
    if request.method == 'POST':
        form = DailyEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            messages.success(request, 'Entry created successfully!')
            return redirect('journal:entry_detail', pk=entry.pk)
    else:
        # Pre-fill with today's date
        form = DailyEntryForm(initial={'date': timezone.now().date()})

    return render(request, 'journal/entry_form.html', {'form': form, 'action': 'Create'})


@login_required
def entry_update(request, pk):
    """Update an existing journal entry"""
    entry = get_object_or_404(DailyEntry, pk=pk, user=request.user)

    if request.method == 'POST':
        form = DailyEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            messages.success(request, 'Entry updated successfully!')
            return redirect('journal:entry_detail', pk=entry.pk)
    else:
        form = DailyEntryForm(instance=entry)

    return render(request, 'journal/entry_form.html', {'form': form, 'action': 'Update'})


@login_required
def entry_delete(request, pk):
    """Delete a journal entry"""
    entry = get_object_or_404(DailyEntry, pk=pk, user=request.user)

    if request.method == 'POST':
        entry.delete()
        messages.success(request, 'Entry deleted successfully!')
        return redirect('journal:entry_list')

    return render(request, 'journal/entry_confirm_delete.html', {'entry': entry})


@login_required
def task_create(request, entry_pk):
    """Create a new task (modal form)"""
    entry = get_object_or_404(DailyEntry, pk=entry_pk, user=request.user)

    if request.method == 'POST':
        form = DailyTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.daily_entry = entry
            task.save()
            messages.success(request, 'Task added successfully!')
            return redirect('journal:entry_detail', pk=entry.pk)

    return redirect('journal:entry_detail', pk=entry.pk)


@login_required
def task_toggle(request, task_pk):
    """Toggle task completion status (AJAX)"""
    if request.method == 'POST':
        task = get_object_or_404(DailyTask, pk=task_pk, daily_entry__user=request.user)
        task.completed = not task.completed
        task.save()
        return JsonResponse({'success': True, 'completed': task.completed})
    return JsonResponse({'success': False})


@login_required
def profile(request):
    """User profile with statistics"""
    total_entries = DailyEntry.objects.filter(user=request.user).count()
    total_tasks = DailyTask.objects.filter(daily_entry__user=request.user).count()
    completed_tasks = DailyTask.objects.filter(daily_entry__user=request.user, completed=True).count()

    # Mood statistics
    mood_stats = {}
    for choice in DailyEntry.MOOD_CHOICES:
        count = DailyEntry.objects.filter(user=request.user, mood=choice[0]).count()
        mood_stats[choice[1]] = count

    context = {
        'total_entries': total_entries,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'mood_stats': mood_stats,
    }
    return render(request, 'journal/profile.html', context)


def about(request):
    """About page view"""
    return render(request, 'journal/about.html')