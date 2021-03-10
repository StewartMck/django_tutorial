from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import DeleteView, CreateView
from .models import Question, Choice
from .forms import QuestionForm


# Without using generic views

# def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    context = {'latest_question_list':latest_question_list}
#    return render(request, 'polls/index.html', context)

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#         context = {'question':question}
#     except Question.DoesNotExist:
#         raise Http404("Question Does Not Exist!")
#     return render(request, 'polls/detail.html', context)

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question':question})


#Using generic Views
class IndexView(generic.ListView):
    form = QuestionForm
    template_name='polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

class QuestionDelete(DeleteView):
    model = Question
    template_name = 'polls/confirm_delete.html'
    success_url = reverse_lazy('polls:index')

    def get_context_data(self, **kwargs):
        context = super(QuestionDelete, self).get_context_data(**kwargs)
        print('context', context)
        id = self.kwargs.get('pk')
        votes = Choice.objects.filter(question_id=id).values('votes')
        totalVotes = 0
        for vote in votes:
            totalVotes += vote['votes']
        context['total_votes'] = totalVotes
        print('new context', context)
        return context


class QuestionCreate(CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'polls/add_question.html'
    success_url = reverse_lazy('polls:index')

    def filter_choices(self, form):
        choices =  {
            'choice1': form.cleaned_data['choice1'],
            'choice2': form.cleaned_data['choice2'],
            'choice3': form.cleaned_data['choice3'],
            'choice4': form.cleaned_data['choice4']
        }
        return  {key: value for key, value in choices.items() if value != ""}
        
    def form_valid(self, form):
        if form.is_valid:
            question = form.save()
            print('form', form)
            for choice in self.filter_choices(form).values():
               Choice(question=question, choice_text=choice).save()

        return super().form_valid(form)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You Didn't Select A Choice!",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))