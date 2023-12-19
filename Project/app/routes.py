from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import postnew1 as Post

@app.route('/')
def home():
    posts = Post.query.all()
    print(posts)
    return render_template('home.html', posts=posts)

@app.route('/post/<int:post_id>')
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post_detail.html', post=post)

@app.route('/admin')
def admin():
    posts = Post.query.all()
    return render_template('admin.html', posts=posts)

@app.route('/admin/add', methods=['POST'])
def add_post():
    title = request.form.get('title')
    content = request.form.get('content')

    if title and content:
        new_post = Post(title=title, content=content)
        db.session.add(new_post)
        db.session.commit()

    return redirect(url_for('admin'))

@app.route('/admin/delete/<int:post_id>')
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('admin'))
@app.route('/admin/update/<int:post_id>', methods=['POST'])
def update_post(post_id):
    post = Post.query.get_or_404(post_id)

    if request.method == 'POST':
        update_title = request.form.get('updateTitle')
        update_content = request.form.get('updateContent')

        if update_title and update_content:
            post.title = update_title
            post.content = update_content
            db.session.commit()

    return redirect(url_for('admin'))