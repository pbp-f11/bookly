from django.forms import ModelForm
from add_review.models import Review

class ProductForm(ModelForm):
    class Meta:
        model = Review
        fields = ["rating", "review"]