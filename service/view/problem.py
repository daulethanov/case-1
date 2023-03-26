from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user
from flask_swagger_ui import get_swaggerui_blueprint

from service.form.problem import ProblemForm, VoteForm
from service.model.model import Problem, db, ProblemRating

problem = Blueprint('problems', __name__, url_prefix='/')


@problem.route('', methods=['GET', 'POST'])
def home():
    return render_template('applications.html')
#
# @problem.route('/problem/<int:id>', methods=['GET', 'POST'])
# def problem(id):
#     problem = Problem.query.get_or_404(id)
#     form = VoteForm()
#
#     if form.validate_on_submit():
#         rating = ProblemRating(problem_id=form.problem_id.data,
#                                user_id=current_user.id,
#                                rating=form.rating.data)
#         db.session.add(rating)
#         db.session.commit()
#         return redirect(url_for('problem', id=id))
#
#     return render_template('problem.html', problem=problem, form=form)


@problem.route('/problem', methods=['GET', 'POST'])
def create_problem():
    form = ProblemForm(user=current_user)
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

#
