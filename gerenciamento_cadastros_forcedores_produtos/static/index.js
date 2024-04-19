function deleteTask(taskId) {
    fetch("/delete-task", {
        method: "POST",
        body: JSON.stringify({ taskId: taskId}),
    }).then((_res) => {
        window.location.href = "/";
    });
}

$('#modalEditTask').on('show.bs.modal', function (event) {
    
    const button = $(event.relatedTarget);
    data = button.data();
    const idTask = data.idtask;
    const nameTask = data.nametask;
    $('#taskId').val(idTask);
    $('#taskName').val(nameTask);
  });