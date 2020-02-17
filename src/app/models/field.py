"""
Field model
"""

from app import DB
from .abstract_model import AbstractModel


class Field(AbstractModel):
    """
    Field model class

    :param name: short field name
    :param owner_id: id of user that created this field
    :param field_type: field type
    """

    __tablename__ = 'fields'
    __table_args__ = (
        DB.UniqueConstraint('name', 'owner_id', name='unique_name_owner'),
    )

    name = DB.Column(DB.String, unique=False, nullable=False)
    owner_id = DB.Column(DB.Integer, DB.ForeignKey('users.id', ondelete='SET NULL'), nullable=True)
    field_type = DB.Column(DB.SmallInteger, unique=False, nullable=False)

    choice_options = DB.relationship('ChoiceOption', backref='field')