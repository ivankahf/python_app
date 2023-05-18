function openPhoto(element) {

  var src = element.src;


  var modal = new bootstrap.Modal(document.getElementById('photoModal'));
  var modalImage = document.getElementById('modalImage');
  modalImage.src = src;

  modal.show();
}
