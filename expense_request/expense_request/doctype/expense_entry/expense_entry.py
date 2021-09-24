# -*- coding: utf-8 -*-
# Copyright (c) 2020, Bantoo and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from erpnext.accounts.report.account_balance.account_balance import get_data
from erpnext.accounts.utils import get_balance_on


class ExpenseEntry(Document):
    pass

@frappe.whitelist()
def get_closing_balance(mode_of_payment):
    account = frappe.db.get_value('Mode of Payment Account', {
                                  'parent': mode_of_payment}, 'default_account')
    if account:
        balance = get_balance_on(account)
        return balance
    else:
        frappe.msgprint("<b>No default account</b> is associated with this mode of payment")
        return False