/*
 * poiyee.ho
 */
(function ($) {

    var keyboardLayout = {
        'layout': [
            // alphanumeric keyboard type
            // text displayed on keyboard button, keyboard value, keycode, column span, new row
            [
                [
                    ['1', '1', 1, 0, true], ['2', '2', 2, 0, false], ['3', '3', 3, 0, false], ['4', '4', 4, 0, false], ['5', '5', 5, 0, false], ['6', '6', 6, 0, false],
                    ['7', '7', 7, 0, false], ['8', '8', 8, 0, false], ['9', '9', 9, 0, false], ['0', '0', 10, 0, false], ['\u00dc', '\u00dc', 11, 0, false], ['<--', '111', 111, 3, false],
                    ['q', 'q', 13, 0, true], ['w', 'w', 14, 0, false], ['e', 'e', 15, 0, false], ['r', 'r', 16, 0, false], ['t', 't', 17, 0, false], ['z', 'z', 18, 0, false], ['u', 'u', 19, 0, false],
                    ['i', 'i', 20, 0, false], ['o', 'o', 21, 0, false], ['p', 'p', 22, 0, false], ['\u00fc', '\u00fc', 23, 0, false], ['+', '+', 24, 0, false],
                    ['a', 'a', 25, 0, true], ['s', 's', 26, 0, false], ['d', 'd', 27, 0, false], ['f', 'f', 28, 0, false], ['g', 'g', 29, 0, false], ['h', 'h', 30, 0, false], ['j', 'j', 31, 0, false],
                    ['k', 'k', 32, 0, false], ['l', 'l', 33, 0, false], ['\u00f6', '\u00f6', 34, 0, false], ['\u00e4', '\u00e4', 35, 0, false], ['#', '#', 36, 0, false], ['Enter', '222', 222, 3, false],
                    ['Shift', '333', 333, 2, true], ['<', '<', 997, 0, false], ['y', 'y', 39, 0, false], ['x', 'x', 40, 0, false], ['c', 'c', 41, 0, false], ['v', 'v', 42, 0, false], ['b', 'b', 43, 0, false], ['n', 'n', 44, 0, false],
                    ['m', 'm', 45, 0, false], [',', ',', 46, 0, false], ['.', '.', 47, 0, false], ['-', '-', 48, 0, false], ['Shift', '333', 333, 2, false],
                    ['Reset', '666', 666, 3, true], ['....', '555', 555, 12, false], ['Alt Gr', '888', 888, 3, false], ['Cancel', '444', 444, 3, false]
                ],
                [
                    ['!', '!', 54, 0, true], ['"', '"', 55, 0, false], ['\u00A7', '\u00A7', 56, 0, false], ['$', '$', 57, 0, false], ['%', '%', 58, 0, false], ['&', '&', 59, 0, false],
                    ['/', '/', 60, 0, false], ['(', '(', 61, 0, false], [')', ')', 62, 0, false], ['=', '=', 63, 0, false], ['?', '?', 64, 0, false], ['<--', '111', 111, 3, false],
                    ['Q', 'Q', 13, 0, true], ['W', 'W', 14, 0, false], ['E', 'E', 15, 0, false], ['R', 'R', 16, 0, false], ['T', 'T', 17, 0, false], ['Z', 'Z', 18, 0, false], ['U', 'U', 19, 0, false],
                    ['I', 'I', 20, 0, false], ['O', 'O', 21, 0, false], ['P', 'P', 22, 0, false], ['\u00dc', '\u00dc', 23, 0, false], ['*', '*', 65, 0, false],
                    ['A', 'A', 25, 0, true], ['S', 'S', 26, 0, false], ['D', 'D', 27, 0, false], ['F', 'F', 28, 0, false], ['G', 'G', 29, 0, false], ['H', 'H', 30, 0, false], ['J', 'J', 31, 0, false],
                    ['K', 'K', 32, 0, false], ['L', 'L', 33, 0, false], ['\u00d6', '\u00d6', 34, 0, false], ['\u00c4', '\u00c4', 35, 0, false], ["'", "'", 66, 0, false], ['Enter', '222', 222, 3, false],
                    ['Shift', '333', 333, 2, true], ['>', '>', 998, 0, false], ['Y', 'Y', 39, 0, false], ['X', 'X', 40, 0, false], ['C', 'C', 41, 0, false], ['V', 'V', 42, 0, false], ['B', 'B', 43, 0, false], ['N', 'N', 44, 0, false],
                    ['M', 'M', 45, 0, false], [';', ';', 67, 0, false], [':', ':', 68, 0, false], ['_', '_', 69, 0, false], ['Shift', '333', 333, 2, false],
                    ['Reset', '666', 666, 3, true], ['....', '555', 51, 12, false], ['Alt Gr', '888', 888, 3, false], ['Cancel', '444', 444, 3, false]
                ],
                [
                    ['1', '1', 1, 0, true], ['\u00B2', '\u00B2', 70, 0, false], ['\u00B3', '\u00B3', 71, 0, false], ['4', '4', 4, 0, false], ['5', '5', 5, 0, false], ['6', '6', 6, 0, false],
                    ['{', '{', 72, 0, false], ['[', '[', 73, 0, false], [']', ']', 74, 0, false], ['}', '}', 75, 0, false], ['&#92;', '\\', 76, 0, false], ['<--', '111', 111, 3, false],
                    ['@', '@', 77, 0, true], ['w', 'w', 14, 0, false], ['\u20ac', '\u20ac', 78, 0, false], ['r', 'r', 16, 0, false], ['t', 't', 17, 0, false], ['z', 'z', 18, 0, false], ['u', 'u', 19, 0, false],
                    ['i', 'i', 20, 0, false], ['o', 'o', 21, 0, false], ['p', 'p', 22, 0, false], ['\u00fc', '\u00fc', 23, 0, false], ['~', '~', 79, 0, false],
                    ['a', 'a', 25, 0, true], ['s', 's', 26, 0, false], ['d', 'd', 27, 0, false], ['f', 'f', 28, 0, false], ['g', 'g', 29, 0, false], ['h', 'h', 30, 0, false], ['j', 'j', 31, 0, false],
                    ['k', 'k', 32, 0, false], ['l', 'l', 33, 0, false], ['\u00f6', '\u00f6', 34, 0, false], ['\u00e4', '\u00e4', 35, 0, false], ['#', '#', 36, 0, false], ['Enter', '222', 222, 3, false],
                    ['Shift', '333', 333, 2, true], ['|', '|', 999, 0, false], ['y', 'y', 39, 0, false], ['x', 'x', 40, 0, false], ['c', 'c', 41, 0, false], ['v', 'v', 42, 0, false], ['b', 'b', 43, 0, false], ['n', 'n', 44, 0, false],
                    ['m', 'm', 45, 0, false], [',', ',', 46, 0, false], ['.', '.', 47, 0, false], ['-', '-', 48, 0, false], ['Shift', '333', 333, 2, false],
                    ['Reset', '666', 666, 3, true], ['....', '555', 555, 12, false], ['AltGr', '888', 888, 3, false], ['Cancel', '444', 444, 3, false]
                ]
            ]
        ]
    };

    var activeInput = {
        'htmlElem': '',
        'initValue': '',
        'keyboardLayout': keyboardLayout,
        'keyboardType': '0',
        'keyboardSet': 0,
        'dataType': 'string',
        'isMoney': false,
        'thousandsSep': ',',
        'disableKeyboardKey': false
    };

    /*
     * initialize keyboard
     * @param {type} settings
     */
    $.fn.initKeypad = function (settings) {
        //$.extend(activeInput, settings);

        $(".virtualKeyboard").click(function (e) {
            if ($('div.virtualKeyboardContainer').length != 0) {
                removeKeypad();
               // $(activeInput.htmlElem).blur();
            }
            activateKeypad(e.target);
        });
    };

    /*
     * create keyboard container and keyboard button
     * @param {DOM object} targetInput
     */
    function activateKeypad(targetInput) {
        if ($('div.virtualKeyboardContainer').length === 0) {
            activeInput.htmlElem = $(targetInput);
            activeInput.initValue = $(targetInput).val();


            $(activeInput.htmlElem).addClass('focus');
            createInvisibleBox();
            createKeypadContainer();
            createKeypad(0);
        }
    }



    // altgr help variable
    var altgr = false;
    /*
     * create keyboard container
     */
    function createKeypadContainer() {
        var container = document.createElement('div');
        container.setAttribute('class', 'virtualKeyboardContainer');
        container.setAttribute('id', 'virtualKeyboardContainer');
        container.setAttribute('name', 'keyboardContainer' + activeInput.keyboardType);

        $("body").append(container);
    }
    function createInvisibleBox() {
        var container = document.createElement('div');
        container.setAttribute('class', 'invisibleBox');
        container.setAttribute('id', 'invisibleBox');
        container.setAttribute('name', 'invisibleBox');

        $("body").append(container);
    }
    window.addEventListener('click', function (e) {
        if ($('div.virtualKeyboardContainer').length != 0) {
            if ((document.getElementById("invisibleBox").contains(e.target))) {
                removeKeypad();
               $(activeInput.htmlElem).blur();
            }
        }
    });

    /*
     * create keyboard
     * @param {Number} set
     */
    function createKeypad(set) {
        $('#virtualKeyboardContainer').empty();

        var layout = activeInput.keyboardLayout.layout[activeInput.keyboardType][set];

        for (var i = 0; i < layout.length; i++) {

            if (layout[i][4]) {
                var row = document.createElement('div');
                row.setAttribute('class', 'virtualKeyboardRow');
                row.setAttribute('name', 'virtualKeyboardRow');
                $('#virtualKeyboardContainer').append(row);
            }

            var button = document.createElement('button');
            button.setAttribute('type', 'button');
            button.setAttribute('name', 'key' + layout[i][2]);
            button.setAttribute('id', 'key' + layout[i][2]);
            button.setAttribute('class', 'virtualKeyboardBtn' + ' ui-button-colspan-' + layout[i][3]);
            button.setAttribute('data-text', layout[i][0]);
            button.setAttribute('data-value', layout[i][1]);
            button.innerHTML = layout[i][0];

            $(button).click(function (e) {
                getKeyPressedValue(e.target);
            });

            $(row).append(button);
        }
    }
    /*
     * remove keyboard from kepad container
     */
    function removeKeypad() {
        $('#virtualKeyboardContainer').remove();
        $(activeInput.htmlElem).removeClass('focus');
        $('#invisibleBox').remove();
    }

    /*
     * handle key pressed
     * @param {DOM object} clickedBtn
     */
    function getKeyPressedValue(clickedBtn) {
        var caretPos = getCaretPosition(activeInput.htmlElem);
        var keyCode = parseInt($(clickedBtn).attr('name').replace('key', ''));

        var currentValue = $(activeInput.htmlElem).val();
        var newVal = currentValue;
        var closeKeypad = false;

        /*
         * TODO
        if(activeInput.isMoney && activeInput.thousandsSep !== ''){
            stripMoney(currentValue, activeInput.thousandsSep);
        }
        */

        switch (keyCode) {
            case 111:     // backspace key
                newVal = onDeleteKeyPressed(currentValue, caretPos);
                caretPos--;
                break;
            case 222:    // enter key
                closeKeypad = onEnterKeyPressed();
                break;
            case 333:    // shift key
                onShiftKeyPressed();
                break;
            case 444:    // cancel key
                closeKeypad = true;
                newVal = onCancelKeyPressed(activeInput.initValue);
                break;
            case 555:    // space key
                newVal = onSpaceKeyPressed(currentValue, caretPos);
                caretPos++;
                break;
            case 666:    // clear key
                newVal = onClearKeyPressed();
                break;
            case 47:   // dot key
                newVal = onDotKeyPressed(currentValue, $(clickedBtn), caretPos);
                caretPos++;
                break;
            case 888:   // altgr key
                altgr = true;
                onAltGrKeyPressed();
                break;
            default:    // alpha or numeric key
                newVal = onAlphaNumericKeyPressed(currentValue, $(clickedBtn), caretPos);
                caretPos++;
                break;
        }

        // update new value and set caret position
        $(activeInput.htmlElem).val(newVal);
        setCaretPosition(activeInput.htmlElem, caretPos);

        if (closeKeypad) {
            removeKeypad();
            $(activeInput.htmlElem).blur();
        }

    }

    /*
     * handle delete key pressed
     * @param value 
     * @param inputType
     */
    function onDeleteKeyPressed(value, caretPos) {
        var result = value.split('');

        if (result.length > 1) {
            result.splice((caretPos - 1), 1);
            return result.join('');
        }
    }

    /*
     * handle shift key pressed
     * update keyboard layout and shift key color according to current keyboard set
     */
    function onShiftKeyPressed() {
        var keyboardSet = activeInput.keyboardSet === 0 ? 1 : 0;
        activeInput.keyboardSet = keyboardSet;

        createKeypad(keyboardSet);

        if (keyboardSet === 1) {
            $('button[name="key333"').addClass('shift-active');
        } else {
            $('button[name="key333"').removeClass('shift-active');
        }
    }
    /*
     * handle altgr key pressed
     * update keyboard layout and alt gr key color according to current keyboard set
     */
    function onAltGrKeyPressed() {
        var keyboardSet = activeInput.keyboardSet === 0 ? 2 : 0;
        activeInput.keyboardSet = keyboardSet;

        createKeypad(keyboardSet);

        if (keyboardSet === 2) {
            $('button[name="key888"').addClass('altgr-active');
        } else {
            $('button[name="key888"').removeClass('altgr-active');
        }
    }
    /*
     * handle space key pressed
     * add a space to current value
     * @param {String} curVal
     * @returns {String}
     */
    function onSpaceKeyPressed(currentValue, caretPos) {
        return insertValueToString(currentValue, ' ', caretPos);
    }

    /*
     * handle cancel key pressed
     * revert to original value and close key pad
     * @param {String} initValue
     * @returns {String}
     */
    function onCancelKeyPressed(initValue) {
        return initValue;
    }

    /*
     * handle enter key pressed value
     * TODO: need to check min max value
     * @returns {Boolean}
     */
    function onEnterKeyPressed() {
        return true;
    }

    /*
     * handle clear key pressed
     * clear text field value
     * @returns {String}
     */
    function onClearKeyPressed() {
        return '';
    }

    /*
     * handle dot key pressed
     * @param {String} currentVal
     * @param {DOM object} keyObj
     * @returns {String}
     */
    function onDotKeyPressed(currentValue, keyElement, caretPos) {
        return insertValueToString(currentValue, keyElement.attr('data-value'), caretPos);
    }

    /*
     * handle all alpha numeric keys pressed
     * @param {String} currentVal
     * @param {DOM object} keyObj
     * @returns {String}
     */
    function onAlphaNumericKeyPressed(currentValue, keyElement, caretPos) {
        return insertValueToString(currentValue, keyElement.attr('data-value'), caretPos);
    }

    /*
     * insert new value to a string at specified position
     * @param {String} currentValue
     * @param {String} newValue
     * @param {Number} pos
     * @returns {String}
     */
    function insertValueToString(currentValue, newValue, pos) {
        var result = currentValue.split('');
        result.splice(pos, 0, newValue);

        return result.join('');
    }

    /*
     * get caret position
     * @param {DOM object} elem
     * @return {Number}
     */
    function getCaretPosition(elem) {
        var input = $(elem).get(0);

        if ('selectionStart' in input) {    // Standard-compliant browsers
            return input.selectionStart;
        } else if (document.selection) {    // IE
            input.focus();

            var sel = document.selection.createRange();
            var selLen = document.selection.createRange().text.length;

            sel.moveStart('character', -input.value.length);
            return sel.text.length - selLen;
        }
    }

    /*
     * set caret position
     * @param {DOM object} elem
     * @param {Number} pos
     */
    function setCaretPosition(elem, pos) {
        var input = $(elem).get(0);

        if (input !== null) {
            if (input.createTextRange) {
                var range = elem.createTextRange();
                range.move('character', pos);
                range.select();
            } else {
                input.focus();
                input.setSelectionRange(pos, pos);
            }
        }
    }
})(jQuery);

$(function () {
    var keyboard = {
        'layout': [
            // alphanumeric keyboard type
            // text displayed on keyboard button, keyboard value, keycode, column span, new row
            [
                [
                    ['1', '1', 1, 0, true], ['2', '2', 2, 0, false], ['3', '3', 3, 0, false], ['4', '4', 4, 0, false], ['5', '5', 5, 0, false], ['6', '6', 6, 0, false],
                    ['7', '7', 7, 0, false], ['8', '8', 8, 0, false], ['9', '9', 9, 0, false], ['0', '0', 10, 0, false], ['\u00dc', '\u00dc', 11, 0, false], ['<--', '111', 111, 3, false],
                    ['q', 'q', 13, 0, true], ['w', 'w', 14, 0, false], ['e', 'e', 15, 0, false], ['r', 'r', 16, 0, false], ['t', 't', 17, 0, false], ['z', 'z', 18, 0, false], ['u', 'u', 19, 0, false],
                    ['i', 'i', 20, 0, false], ['o', 'o', 21, 0, false], ['p', 'p', 22, 0, false], ['\u00fc', '\u00fc', 23, 0, false], ['+', '+', 24, 0, false],
                    ['a', 'a', 25, 0, true], ['s', 's', 26, 0, false], ['d', 'd', 27, 0, false], ['f', 'f', 28, 0, false], ['g', 'g', 29, 0, false], ['h', 'h', 30, 0, false], ['j', 'j', 31, 0, false],
                    ['k', 'k', 32, 0, false], ['l', 'l', 33, 0, false], ['\u00f6', '\u00f6', 34, 0, false], ['\u00e4', '\u00e4', 35, 0, false], ['#', '#', 36, 0, false], ['Enter', '222', 222, 3, false],
                    ['Shift', '333', 333, 2, true], ['<', '<', 997, 0, false], ['y', 'y', 39, 0, false], ['x', 'x', 40, 0, false], ['c', 'c', 41, 0, false], ['v', 'v', 42, 0, false], ['b', 'b', 43, 0, false], ['n', 'n', 44, 0, false],
                    ['m', 'm', 45, 0, false], [',', ',', 46, 0, false], ['.', '.', 47, 0, false], ['-', '-', 48, 0, false], ['Shift', '333', 333, 2, false],
                    ['Reset', '666', 666, 3, true], ['....', '555', 555, 12, false], ['AltGr', '888', 888, 3, false], ['Cancel', '444', 444, 3, false]
                ]
            ]
        ]
    }
    $('input.virtualKeyboard').initKeypad({ 'keyboardLayout': keyboard });
});


