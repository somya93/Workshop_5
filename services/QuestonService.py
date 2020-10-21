from models.Question import QuestionDocument
import datetime

# def update_question_in_db(updated_question: QuestionDocument):
#     the_doc = QuestionDocument.objects(id=new_question.primary_key).first()
#     # objects returns a list, first() returns the first result
#
#     the_doc.replies = new_question.replies
#     the_doc.save()


def create_question_in_db(question_text: str) -> [QuestionDocument]:
    question_doc = QuestionDocument(question_text=question_text,
                                    replies=[],
                                    num_replies=0,
                                    date_created=datetime.datetime.utcnow()
                                    )
    question_doc.save()
    return question_doc


def get_all_questions():
    return QuestionDocument.objects


def get_question(q_id):
    return QuestionDocument.objects.filter(id=q_id).first()
