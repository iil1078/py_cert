"""
Unit tests for module currency

When run as a script, this module invokes several procedures that test
the various functions in the module currency.

Author: I-Chia Liao
Date:   2023-08-03
"""

# import modules
import introcs
import currency


# test each function
def test_before_space():
    """Test procedure for before_space"""

    print('Testing before_space')
    
    result = currency.before_space('Hello World')
    introcs.assert_equals("Hello", result)

    result = currency.before_space('Hello  World')
    introcs.assert_equals("Hello", result)

    result = currency.before_space('Hello World ')
    introcs.assert_equals("Hello", result)

    result = currency.before_space(' HelloWorld')
    introcs.assert_equals("", result)


def test_after_space():
    """Test procedure for after_space"""

    print('Testing after_space')
        
    result = currency.after_space('Hello World')
    introcs.assert_equals("World", result)

    result = currency.after_space('Hello  World')
    introcs.assert_equals(" World", result)

    result = currency.after_space(' Hello World')
    introcs.assert_equals("Hello World", result)

    result = currency.after_space('HelloWorld ')
    introcs.assert_equals("", result)


def test_first_inside_quotes():
    """Test procedure for first_inside_quotes"""

    print('Testing first_inside_quotes')

    # one pair of double quotes
    result = currency.first_inside_quotes('A "B C" D')
    introcs.assert_equals('B C', result)

    # two pairs of double quotes
    result = currency.first_inside_quotes('A "B C" D "E F" G')
    introcs.assert_equals('B C', result)

    # nothing inside double quotes
    result = currency.first_inside_quotes('""')
    introcs.assert_equals('', result)

    # one pair of double quote with special character inside
    result = currency.first_inside_quotes('":"')
    introcs.assert_equals(':', result)


def test_get_src():
    """Test procedure for get_src"""

    print('Testing get_src')

    # one space after "src":
    result = currency.get_src('{"success": true, "src": "2 United States Dollars"'+
    ', "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('2 United States Dollars', result)

    # no space after "src":
    result = currency.get_src('{"success": true, "src":"2 United States Dollars"'+
    ', "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('2 United States Dollars', result)

    # no value for src (one space after "src":)
    result = currency.get_src('{"success":false,"src": "","dst":"","error":"Source'+
    ' currency code is invalid."}')
    introcs.assert_equals('', result)

    # no value for src (no space after "src":)
    result = currency.get_src('{"success":false,"src":"","dst":"","error":"Source'+
    ' currency code is invalid."}')
    introcs.assert_equals('', result)


def test_get_dst():
    """Test procedure for get_dst"""

    print('Testing get_dst')

    # one space after "dst":
    result = currency.get_dst('{"success": true, "src": "2 United States Dollars"'+
    ', "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('1.772814 Euros', result)

    # no space after "dst":
    result = currency.get_dst('{"success": true, "src": "2 United States Dollars"'+
    ', "dst":"1.772814 Euros", "error": ""}')
    introcs.assert_equals('1.772814 Euros', result)

    # no value for dst (one space after "dst":)
    result = currency.get_dst('{"success":false,"src": "","dst": "","error":"Source'+
    ' currency code is invalid."}')
    introcs.assert_equals('', result)

    # no value for dst (no space after "dst":)
    result = currency.get_dst('{"success":false,"src": "","dst":"","error":"Source'+
    ' currency code is invalid."}')
    introcs.assert_equals('', result)


def test_has_error():
    """Test procedure for has_error"""
    print('Testing has_error')

    # one space after "error":
    result = currency.has_error('{"success":false,"src": "","dst":"","error":"Source'+
    ' currency code is invalid."}')
    introcs.assert_true(result)

    # no space after "error":
    result = currency.has_error('{"success":false,"src": "","dst":"","error": "Source'+
    ' currency code is invalid."}')
    introcs.assert_true(result)

    # no value, one space after "error":
    result = currency.has_error('{"success": true, "src": "2 United States Dollars"'+
    ', "dst":"1.772814 Euros", "error": ""}')
    introcs.assert_false(result)

    # no value, no space after "error":
    result = currency.has_error('{"success": true, "src": "2 United States Dollars"'+
    ', "dst":"1.772814 Euros", "error":""}')
    introcs.assert_false(result)


def test_service_response():
    """Test procedure for service_response"""

    print('Testing service_response')

    # valid currency and non-negative amount
    result = currency.service_response('USD','EUR',2.5)
    introcs.assert_equals('{"success": true, "src": "2.5 United States Dollars", '+
    '"dst": "2.2160175 Euros", "error": ""}',result)

    # valid currency and negative amount
    result = currency.service_response('USD','EUR',-2.5)
    introcs.assert_equals('{"success": true, "src": "-2.5 United States Dollars", '+
    '"dst": "-2.2160175 Euros", "error": ""}',result)

    # invalid src currency and non-negative amount
    result = currency.service_response('US','EUR',2.5)
    introcs.assert_equals('{"success": false, "src": "", "dst": "", "error": "The rate '+
    'for currency US is not present."}',result)

    # invalid dst currency and non-negative amount
    result = currency.service_response('USD','EU',2.5)
    introcs.assert_equals('{"success": false, "src": "", "dst": "", "error": "The rate '+
    'for currency EU is not present."}',result)


def test_iscurrency():
    """Test procedure for iscurrency"""

    print('Testing iscurrency')

    # valid currency code
    result = currency.iscurrency("TWD")
    introcs.assert_true(result)

    # invalid currency code
    result = currency.iscurrency("T")
    introcs.assert_false(result)


def test_exchange():
    """Test procedure for exchange"""

    print('Testing exchange')

    # valid src, dst, and amt
    result = currency.exchange('USD','TWD',1)
    introcs.assert_floats_equal(31.0525,result)

    # negative amt
    result = currency.exchange('USD','TWD',-1)
    introcs.assert_floats_equal(-31.0525,result)


# run the test functions
test_before_space()
test_after_space()
test_first_inside_quotes()
test_get_src()
test_get_dst()
test_has_error()
test_service_response()
test_iscurrency()
test_exchange()
print('All tests completed successfully.')
