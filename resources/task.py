from flask import request
from flask_security import auth_required
from flask_restful import Resource

from models import db
from models.task import Task

from marshmallow import ValidationError
from schemas import TaskSchema

from .import api


class TaskResource(Resource):
    # TODO: Uncomment below to add authentication decorator to resource.
    # ? method_decorators vs decorators
    # method_decorators = [auth_required]
    def get(self, task_id=None):
        """
        GET /tasks
        GET /tasks/<task_id>
        """
        if task_id:
            task = Task.query.filter(Task.id == task_id).first()
            if not task:
                return {'message': 'Task not found'}, 404
            schema = TaskSchema()
            return schema.dump(task)

        tasks = Task.query.all()
        schema = TaskSchema(many=True)
        return schema.dump(tasks)

    def post(self):
        """POST /tasks"""
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form.to_dict()

        try:
            schema = TaskSchema()
            validated_data = schema.load(data)
            new_task = Task(**validated_data)
        except ValidationError as e:
            return {'errors': e.messages}, 400

        db.session.add(new_task)
        db.session.commit()

        return schema.dump(new_task), 201

    def put(self, task_id):
        """PUT /tasks/<task_id>"""
        task = Task.query.get(task_id)
        if not task:
            return {'message': 'Task does not exist'}, 404

        if request.is_json:
            data = request.get_json()
        else:
            data = request.form.to_dict()

        try:
            schema = TaskSchema()
            validated_data: dict = schema.load(data)
            for field, value in validated_data.items():
                setattr(task, field, value)
        except ValidationError as e:
            return {'errors': e.messages}, 400

        db.session.commit()
        return schema.dump(task), 200

    def delete(self, task_id):
        """DELETE /task/<task_id>"""
        task = Task.query.get(task_id)
        if task:
            db.session.delete(task)
            db.session.commit()
            return {'message': f'Task {task_id} deleted'}
        return {'message': 'Task not found'}, 404


api.add_resource(TaskResource, '/tasks', '/tasks/<int:task_id>')
