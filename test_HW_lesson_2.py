from selene.support.shared import browser
from selene import be, have
import pytest


# passed_test
def test_passed_hw(size_window):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('Selene - User-oriented').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


# fails_test
def test_failed_hw(size_window):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('Selene - User-oriented').press_enter()
    browser.element('[id="search"]').should(have.no.text('Java или Python для QA?'))
