document.addEventListener("DOMContentLoaded", function() {
    var localiteField = document.getElementById('id_localite');
    var initialesField = document.getElementById('id_initiales');

    localiteField.addEventListener('input', function() {
        var localiteValue = localiteField.value;
        if (localiteValue.length > 0) {
            var suggestion = localiteValue.substring(0, 5).toUpperCase();
            initialesField.value = suggestion;
        } else {
            initialesField.value = '';
        }
    });
});
