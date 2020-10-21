from models.Question import QuestionDocument
import datetime


def add_reply_to_question(q_id: str, reply: str):
    the_q = QuestionDocument.objects(id=q_id).first()
    the_q.update(push__replies=reply, inc__num_replies=1)
    the_q.reload()
    return the_q


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
