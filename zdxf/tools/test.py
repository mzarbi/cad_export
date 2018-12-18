# Purpose: test tools
# Created: 27.03.2011
# Copyright (C) 2011, Manfred Moitzi
# License: MIT License
from __future__ import unicode_literals
__author__ = "mozman <mozman@gmx.at>"

from zdxf.tools.handle import HandleGenerator
from zdxf.dxffactory import dxffactory
from zdxf.lldxf.tags import Tags, DXFStructureError, DXFTag
from zdxf.lldxf.extendedtags import ExtendedTags
from zdxf.lldxf.attributes import DXFAttr, DXFAttributes, DefSubclass

from zdxf.drawing import Drawing
from zdxf.database import EntityDB
from zdxf.lldxf.tagger import internal_tag_compiler


class ModelSpace:
    layout_key = 'FFFF'


class DrawingProxy:
    """ a lightweight drawing proxy for testing

    TestDrawingProxy in test_tools.py checks if all none private! attributes
    exists in the Drawing() class, private means starts with '__'.
    """
    def __init__(self, version):
        self.dxfversion = version
        self.entitydb = EntityDB()
        self.dxffactory = dxffactory(self)

    def modelspace(self):
        return ModelSpace()

    def __does_not_exist_in_Drawing(self):
        """ ATTENTION: private attributes will not be checked in TestDrawingProxy! """


def compile_tags_without_handles(text):
    return (tag for tag in internal_tag_compiler(text) if tag.code not in (5, 105))


def normlines(text):
    lines = text.split('\n')
    return [line.strip() for line in lines]


def load_section(text, name, database=None, dxffactory=None):
    from zdxf.lldxf.loader import load_dxf_structure, fill_database
    dxf = load_dxf_structure(internal_tag_compiler(text), ignore_missing_eof=True)
    if database is not None:
        fill_database(database, dxf, dxffactory)
    return dxf[name]
