from flask import jsonify, request
from flask_security import auth_required
from flask_restful import Resource
from models import db
from models.task import Task


class TaskResource(Resource):
    # @auth_required()
    # TODO: serialize data helper function
    def get(self, task_id=None):
        if task_id:
            task = Task.query.filter(Task.id == task_id).first()
            if not task:
                return jsonify({'message': 'Task not found'}), 404
            return jsonify(task)
        tasks = Task.query.all()
        return jsonify(tasks)

    def post(self):
        data = request.get_json()
        new_task = Task(name=data['name'])
        if data['description']:
            new_task.deadline = data['description']
        if data['deadline']:
            new_task.deadline = data['deadline']  # make datetime format same

        db.session.add(new_task)
        db.session.commit()

        return jsonify(new_task), 201

    def put(self, task_id):
        # TODO: check if id exists in db
        pass

    def delete(self, task_id):
        task = Task.query.get(task_id)
        if task:
            db.session.delete(task)
            db.session.commit()
            return jsonify({f'message': 'Task {task_id} deleted'})
        return jsonify({'message': 'Task not found'}), 404
