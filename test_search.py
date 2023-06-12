import pytest
from selene import browser
from selene import be, have






def test_search_success():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_search_fail():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('hgyfutydkfchgvjbhkj').press_enter()
    browser.element('[id="topstuff"]').should(have.text('По запросу hgyfutydkfchgvjbhkj ничего не найдено.'))