# Create your views here.
from framework.view_decorators import view_defaults
from landing.forms import FeedbackForm

@view_defaults
def homepage(request):
    feedback_form = FeedbackForm()
    request.context['feedback_form'] = feedback_form