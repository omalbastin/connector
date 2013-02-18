# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Guewen Baconnier
#    Copyright 2012 Camptocamp SA
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import orm


class connectors_installed(orm.AbstractModel):
    """Empty model used to know if the module is installed on the
    database.
    """
    _name = 'connectors.installed'


class ConnectorUnit(object):
    """Abstract class for each piece of the connector:

    * Binder
    * Mapper
    * Synchronizer
    * Backend Adapter

    Or basically any class intended to be registered in a
    :py:class:`base_external_referentials.reference.Reference`.
    """

    model_name = None

    @classmethod
    def match(cls, model):
        """ Find the class to use """
        if cls.model_name is None:
            raise NotImplementedError
        if hasattr(model, '_name'):  # model instance
            model_name = model._name
        else:
            model_name = model  # str
        return cls.model_name == model_name
