import model
import view

def start():
    model.get_class(view.input_class())
    model.set_subject(view.input_subject())
    model.open_file()
    student = ''
    while True:
        journal=model.get_journal()
        view.list_of_child(journal)
        student=view.who_answer()
        view.student_check(student)
        if student=='exit':
            break
        mark = int(view.what_mark())
        view.mark_check(mark)
        model.student_mark(student, mark)
    model.save_file()