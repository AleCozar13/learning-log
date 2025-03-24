"""Dependencies"""

from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    """Simple Topic form"""

    class Meta:
        """Simple Topic form"""

        model = Topic
        fields = ["text", "public"]
        labels = {"text": ""}


class EntryForm(forms.ModelForm):
    """Simple Entry form"""

    class Meta:
        """Simple Entry form"""

        model = Entry
        fields = ["text"]
        labels = {"text": ""}
        widgets = {"text": forms.Textarea(attrs={"cols": 80})}
