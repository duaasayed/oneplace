from django import forms

class AddApplicationForm(forms.Form):
    title = forms.CharField(max_length=150, required=True, label='Job Title', widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'type':'text'}))
    company = forms.CharField(max_length=150, required=True, label='Company', widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'type':'text'}))
    medium = forms.CharField(max_length=150, required=True, label='Where do you find this job?', widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'type':'text'}))
    link = forms.URLField(max_length=500, required=True, label='Job Link', widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'type':'url'}))
    job_type = forms.CharField(max_length=150, required=False, label='Job Type', widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'type':'text'}))
    level = forms.CharField(max_length=150, required=False, label='Experience Level', widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'type':'text'}))
    posted_at = forms.DateField(label='Job Posted', required=False, widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'type':'date'}))
    applied_at = forms.DateField(label='Applied at', required=False, widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'type':'date'}))
