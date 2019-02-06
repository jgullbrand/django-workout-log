from django import forms

from .models import GymEntry

class EntryForm(forms.ModelForm):
	class Meta:
		model = GymEntry
		fields = ["workout_name", "text"]
		widgets = {
			"workout_name": forms.TextInput(attrs={"placeholder": "Workout Name", 'size': 35,}),
			"text": forms.Textarea(attrs={"placeholder": "What exercises did you do?" , 'cols': 71, 'rows': 10})
		}