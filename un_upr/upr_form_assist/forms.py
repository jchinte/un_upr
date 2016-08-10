from django import forms
from django.forms import inlineformset_factory
from models import UPR_submission
from upr_form_assist.models import UPR_question
from django.forms.models import ModelForm


class QuestionForm(ModelForm):
     
    class Meta:
        model = UPR_question
        fields = '__all__'
        widgets={
                 'question': forms.HiddenInput()
                 }
    def __init__(self, question="question", *args, **kwargs):
        super(QuestionForm, self).__init__(args, kwargs)
        self.question = forms.CharField(
                    max_length=100,
                    widget=forms.HiddenInput(),initial = question
                    )
        
        
questionDictionary = [
        ('Part 1: Victim Information', [
                "q1",
                "q2", 
                "q3",
                ]),
        ('Part 2: Information regarding the incident',[
            "a. Detailed description of the human rights violation:",
            "b. Date:",
            "c. Time:",
            "d. Location/Country:",
            "e. Number of assailants:",
            "f. Are the assailant(s) known or related to the victim? If so, how?",
            "g. Name or nickname of assailant(s) (if unknown, description, scars or body marks such as tattoos, clothes/uniform worn, title/status, vehicle used):",
            "h. Does the victim believe he/she was targeted specifically because of her identity, classified by gender, race, religion, or other subgroups? If yes, why?",
            "i. Has the incident been reported to the relevant state/national authorities? If so, which authorities and when?",
            "j. Have the authorities taken any action after the incident? If so, which authorities, what action, when?",
            "k. If the violation was committed by private individuals or groups (rather than government officials), include any information which might indicate that the Government failed to exercise due diligence to prevent, investigate, punish, and ensure compensation for the violations.",
            "l. Has the victim seen a doctor after the incident took place? Are there any medical certificates/notes relating to the incident concerned?",
                ]),
        ('Part 3: Laws or policies',[
            "If your submission concerns a law or policy, please summarize it and the effects of its implementation on human rights. Provide concrete examples, when available.",
            
            ]),
        ]


class SubmitForm(ModelForm):
    """
    Form for individual user links
    """
    class Meta:
        model = UPR_submission
        fields = '__all__'
        

    formset = []
    
    #formset_factory(QuestionForm, extra=len(questionList1))()
    
    def __init__(self, *args, **kwargs):
        super(SubmitForm, self).__init__(args, kwargs)
        self.questionFactoryList = []
        
        for qnum, (t, questionList) in enumerate(questionDictionary):
            i = 0   
            self.questionFactoryList.append(inlineformset_factory(UPR_submission, UPR_question, fields='__all__', extra=len(questionList)))
            self.formset.append((t, self.questionFactoryList[-1](prefix="fs"+str(qnum))))
            for f in self.formset[-1][1]:
                f.initial['question'] = questionList[i]
                f.data['question'] = questionList[i]
                f['answer'].label = questionList[i]
                i += 1
            #qnum += 1
    def getFactory(self, num=0):
        if len(self.questionFactoryList)>0:
            return self.questionFactoryList[num]
        return None
    def save(self):
        inst = UPR_submission.objects.create(title="ph")
        for title, res in self.formset:
            #cd = res.cleaned_data()
            
            
            newQ = UPR_question(question = title, submission = inst, answer = "placeholder")
            newQ.save()
        
        return inst

