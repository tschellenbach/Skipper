# Create your views here.
from framework.view_decorators import view_defaults
from landing.forms import FeedbackForm

@view_defaults
def homepage(request):
    feedback_form = FeedbackForm()
    request.context['feedback_form'] = feedback_form
    from framework.tasks import add
    #This should work since celery always eager is true
    result = add.delay()
    print 