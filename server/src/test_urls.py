from flask import Flask, url_for
from main import app, test_requests


print(url_for('index'))
print(url_for('login'))
print(url_for('user', username='test'))
print(url_for('profile', post_id=1))