"""Dependencies"""

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
    """The home page for Learning Log."""
    return render(request, "learning_logs/index.html")


def topics(request):
    """Show all topics."""
    # Show all topics
    # topics = Topic.objects.order_by("date_added")
    # Show only topics that a user has created:
    if request.user.is_authenticated:
        topics = Topic.objects.filter(owner=request.user).order_by("date_added")
        # Get all public topics not owned by the current user
        public_topics = Topic.objects.filter(public=True).exclude(owner=request.user).order_by("date_added")

    else:
        # User is not authenticated; return all public topics
        topics = None
        public_topics = Topic.objects.filter(public=True).order_by("date_added")

    context = {"topics": topics, "public_topics": public_topics}
    return render(request, "learning_logs/topics.html", context)


def topic(request, topic_id):
    """Show a single topic and all its entries."""
    # topic and entries are shell queries
    topic = Topic.objects.get(id=topic_id)
    # We only want to show new_entry and edit_entry links if the current
    #   user owns this topic.
    is_owner = False
    if request.user == topic.owner:
        is_owner = True

    # If the topic belongs to someone else, and it is not public,
    #   show an error page.
    if (topic.owner != request.user) and (not topic.public):
        raise Http404

    entries = topic.entry_set.order_by("-date_added")
    context = {"topic": topic, "entries": entries, "is_owner": is_owner}
    return render(request, "learning_logs/topic.html", context)


@login_required
def new_topic(request):
    """Add a new topic"""
    if request.method != "POST":
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            # form.save()
            # Associate new topics with the current user:
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect("learning_logs:topics")

    # Display a blank or invalid form.
    context = {"form": form}
    return render(request, "learning_logs/new_topic.html", context)


@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)
    # Create new entry only to that user:
    check_topic_owner(topic=topic, user=request.user)

    if request.method != "POST":
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect("learning_logs:topic", topic_id=topic_id)
    # Display a blank or invalid form.
    context = {"topic": topic, "form": form}
    return render(request, "learning_logs/new_entry.html", context)


@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    # Edit only topics that a user has created:
    check_topic_owner(topic=topic, user=request.user)

    if request.method != "POST":
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)

    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("learning_logs:topic", topic_id=topic.id)
    context = {"entry": entry, "topic": topic, "form": form}
    return render(request, "learning_logs/edit_entry.html", context)


def check_topic_owner(topic, user):
    """
    Make sure the currently logged-in user owns the topic that's
    being requested.

    Raise Http404 error if the user does not own the topic.
    """
    if topic.owner != user:
        raise Http404
