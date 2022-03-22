from flask import Blueprint, render_template, request, abort, redirect, url_for, flash
from flask_login import login_required, current_user

from models import Question, Answer
from qa.forms import WriteQuestionForm, WriteAnswerForm

qa = Blueprint('qa', __name__,
               template_folder='templates',
               static_folder='../assets')


@qa.route('/')
def index():
    """ 首页 回答列表 """
    per_page = 20  # 每页数据的大小
    page = int(request.args.get('page', 1))
    page_data = Answer.query.filter_by(is_valid=True).paginate(
        page=page, per_page=per_page)
    return render_template('index.html', page_data=page_data)


@qa.route('/follow')
def follow():
    """ 关注 问题列表 """
    per_page = 20  # 每页数据的大小
    page = int(request.args.get('page', 1))
    page_data = Question.query.filter_by(is_valid=True).paginate(
        page=page, per_page=per_page)
    return render_template('follow.html', page_data=page_data)


@qa.route('/qa/list')
def question_list():
    """ 查询问题数据列表
    // json
    {
        'code': 0,
        'data': ''
    }
    """
    try:
        per_page = 2  # 每页数据的大小
        page = int(request.args.get('page', 1))
        page_data = Question.query.filter_by(is_valid=True).paginate(
            page=page, per_page=per_page)
        data = render_template('qa_list.html', page_data=page_data)
        return {'code': 0, 'data': data}
    except Exception as e:
        print(e)
        data = ''
    return {'code': 1, 'data': ''}


@qa.route('/write', methods=['GET', 'POST'])
@login_required
def write():
    """ 写文章，提问 """
    form = WriteQuestionForm()
    if form.validate_on_submit():
        try:
            que_obj = form.save()
            if que_obj:
                flash('发布问题成功', 'success')
                return redirect(url_for('qa.index'))
        except Exception as e:
            print(e)
        flash('发布问题失败，请稍后重试', 'danger')
    return render_template('write.html', form=form)


@qa.route('/detail/<int:q_id>', methods=['GET', 'POST'])
def detail(q_id):
    """ 问题详情 """
    # 1. 查询问题信息
    question = Question.query.get(q_id)
    if not question.is_valid:
        abort(404)
    # 2. 展示第一条回答信息
    answer = question.answer_list.filter_by(is_valid=True).first()
    # 添加回答
    form = WriteAnswerForm()
    if form.validate_on_submit():
        try:
            if not current_user.is_authenticated:
                flash('请先登录', 'danger')
                return redirect(url_for('accounts.login'))
            form.save(question=question)
            flash('回答问题成功', 'success')
            return redirect(url_for('qa.detail', q_id=q_id))
        except Exception as e:
            print(e)
    return render_template('detail.html',
                           question=question,
                           answer=answer,
                           form=form)
