# from flask import session
from flask_socketio import emit
from .. import socketio

@socketio.on("receive packet")
def send_packet_to_display(packet):
    emit("received packet", packet)

"""Example from Flask-SocketIO-Chat on GitHub"""
# @socketio.on('text', namespace='/chat')
# def text(message):
#     """Sent by a client when the user entered a new message.
#     The message is sent to all people in the room."""
#     room = session.get('room')
#     emit('message', {'msg': session.get('name') + ':' + message['msg']}, room=room)