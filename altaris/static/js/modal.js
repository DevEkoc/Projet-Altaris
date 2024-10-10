// Ajoutez cet événement à votre code JavaScript
$(document).on('click', '.btn-outline-danger', function() {
    var deleteUrl = $(this).attr('href'); // Récupérez l'URL de suppression
    $('#confirmDelete').attr('href', deleteUrl); // Mettez à jour l'URL dans le bouton de confirmation
});

