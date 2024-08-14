import pytest

from flaskr.db import get_db

#def test_update(client, auth, app):
#    auth.login()
#    assert client.get("/1/update").status_code == 200
#    client.post("/1/update", data={"title": "updated", "body": ""})

#    with app.app_context():
#        db = get_db()
#        post = db.execute("SELECT * FROM post WHERE id = 1").fetchone()
#        assert post["title"] == "updated"
