from flask import Blueprint, render_template

from service.form.problem import ProblemForm
from service.model.model import Problem, db

problem = Blueprint('problems', __name__, url_prefix='/api')


@problem.route('/problem', methods=['GET', 'POST'])
def create_problem():
    form = ProblemForm()
    if form.validate_on_submit():
        message = form.message.data
        image_file = form.image.data
        problem = Problem(message=message)
        if image_file:
            problem.save_image(image_file)
        db.session.add(problem)
        db.session.commit()
        return 'Problem created successfully'
    return render_template('problem_form.html', form=form)