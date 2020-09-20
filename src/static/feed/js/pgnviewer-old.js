var chess = new Chess();

var board = ChessBoard('board');

var movePly = 0;


$('#setStartBtn').on('click', board.start);


$('#setRuyLopezBtn').on('click', function() {
    board.position('r1bqkbnr/pppp1ppp/2n5/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R');
});


$('#previousMoveBtn').on('click', function() {
    board.position(movesfen);
});


$('#nextMoveBtn').on('click', function() {
//    chess.move('e4');
    chess.move(movesList[0]);    
    var movesfen = chess.fen();
    board.position(movesfen);
});


$('#nextNextMoveBtn').on('click', function() {
    var moveItem = movesList.shift();
    chess.move(moveItem);
    var movesfen = chess.fen();
    board.position(movesfen);
});
