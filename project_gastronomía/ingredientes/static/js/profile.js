function showPanel(panelId) {
    // Ocultar todos los paneles
    document.getElementById('profilePanel').style.display = 'none';
    document.getElementById('ordersPanel').style.display = 'none';
    document.getElementById('editProfilePanel').style.display = 'none';

    // Mostrar el panel específico
    document.getElementById(panelId).style.display = 'block';
}