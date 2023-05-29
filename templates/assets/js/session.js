function getSessionData() {
    $.ajax({
        url: '/get_session_data',
        type: 'GET',
        success: function(data) {
            $('#session-data').text(data);
        }
    });
}

function setSessionData() {
    $.ajax({
        url: '/set_session_data',
        type: 'POST',
        data: { session_data: 'Some session data' },
        success: function() {
            alert('Session data set successfully!');
        }
    });
}