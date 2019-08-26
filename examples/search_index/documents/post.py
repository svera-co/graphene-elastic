import datetime
import os
from elasticsearch_dsl import connections
from elasticsearch_dsl import (
    analyzer,
    Boolean,
    Completion,
    Date,
    Document,
    InnerDoc,
    Keyword,
    Nested,
    Text,
)
from .settings import BLOG_POST_DOCUMENT_NAME

try:
    from elasticsearch import logger
except ImportError:
    import logging
    logger = logging.getLogger(__name__)

__all__ = (
    'Comment',
    'Post',
)

connections.create_connection(hosts=['localhost'], timeout=20)


html_strip = analyzer('html_strip',
    tokenizer="standard",
    filter=["lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)


class Comment(InnerDoc):
    author = Text(fields={'raw': Keyword()})
    content = Text(analyzer='snowball')
    created_at = Date()

    def age(self):
        return datetime.datetime.now() - self.created_at


class Post(Document):
    title = Text(
        analyzer=html_strip,
        fields={'raw': Keyword()}
    )
    # title_suggest = Completion()
    content = Text()
    created_at = Date()
    published = Boolean()
    category = Text(
        analyzer=html_strip,
        fields={'raw': Keyword()}
    )
    comments = Nested(Comment)

    class Index:
        name = BLOG_POST_DOCUMENT_NAME
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 1,
            'blocks': {'read_only_allow_delete': None},
        }

    def add_comment(self, author, content):
        self.comments.append(
            Comment(
                author=author,
                content=content,
                created_at=datetime.datetime.now()
            )
        )

    def save(self, ** kwargs):
        self.created_at = datetime.datetime.now()
        return super().save(** kwargs)


try:
    # Create the mappings in Elasticsearch
    Post.init()
except Exception as err:
    logger.error(err)
