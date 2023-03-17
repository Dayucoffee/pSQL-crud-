from django import forms
from agent.models import Agent
class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = "__all__"