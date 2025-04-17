from BloomingDays import db, app
from BloomingDays.admin.models import User

adminAcc = User(email="admin@admin.com", username="admin", password="admin", is_admin=True),

with app.app_context():
    # Remove all existing
    User.query.delete()
    db.session.commit()
    # Then add new
    db.session.add(adminAcc)
    db.session.commit()