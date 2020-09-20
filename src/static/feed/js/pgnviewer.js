var cfg = {
  showNotation: false,
  position: 'start'
};
var board = ChessBoard('board', cfg);
var chess = new Chess();
var newMove = $('#newmove');


$('#nextMoveBtn').on('click', function() {
    var moveItem = movesList.shift();
    chess.move(moveItem);
    var movesFen = chess.fen();
    board.position(movesFen);
    newMove.html(moveItem);
});


$('#previousMoveBtn').on('click', function() {
    var moveItem = chess.undo('san');
    var movesFen = chess.fen();
    board.position(movesFen);
    newMove.html(moveItem);
    if(moveItem) {
        movesList.unshift(moveItem);
    }        
});
