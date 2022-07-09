import datetime

from peewee import *

db = SqliteDatabase('influnc_plus/db/database.db')


class BaseModel(Model):
    class Meta:
        database = db


class Blog(BaseModel):
    domain = CharField(null=False)
    title = CharField(null=True)
    status = CharField(null=True)  # online-links, online-no-links, offline or unknown
    last_access_time = DateTimeField(null=True)


class Link(BaseModel):
    src_blog = ForeignKeyField(Blog, backref="links_out")
    dst_blog = ForeignKeyField(Blog, backref="links_in")


def create_tables():
    db.connect()
    db.create_tables([Blog, Link])


def prepare_initial_data():
    horo = Blog(domain="blog.yoitsu.moe", title="约伊兹的萌狼乡手札", status="unknown", last_access_time=datetime.datetime.now())
    horo.save()


if __name__ == '__main__':
    create_tables()
    prepare_initial_data()
