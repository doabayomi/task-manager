from flask import jsonify, request
from flask_security import auth_required
from flask_restful import Resource

from models import db
from models.task import Task

from marshmallow import ValidationError
from schemas import TaskSchema


class TaskResource(Resource):
    # TODO: add authentication decorator to resource.
    def get(self, task_id=None):
        if task_id:
            task = Task.query.filter(Task.id == task_id).first()
            if not task:
                return jsonify({'message': 'Task not found'}), 204
            schema = TaskSchema()
            return jsonify(schema.dump(task))

        tasks = Task.query.all()
        schema = TaskSchema(many=True)
        return jsonify(schema.dump(tasks))

    def post(self):
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form.to_dict()

        try:
            schema = TaskSchema()
            data = schema.load(data)
            new_task = Task(**data)
        except ValidationError as e:
            return {'errors': e.messages}, 400

        db.session.add(new_task)
        db.session.commit()

        return schema.dump(new_task), 201

    def put(self, task_id):
        # ? Do I even need a put function, no one should be
        # ? overwriting a task completely.
        pass

    def delete(self, task_id):
        task = Task.query.get(task_id)
        if task:
            db.session.delete(task)
            db.session.commit()
            return jsonify({f'message': 'Task {task_id} deleted'})
        return jsonify({'message': 'Task not found'}), 404
