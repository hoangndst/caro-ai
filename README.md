# caro-ai
AI Project for Caro Game
## Introduction

## JSON API
- Frontend
    ``` js
    {
        match_id: xxx,
        status: None, (draw, teamID Win) (nếu khác None sẽ in ra draw hoặc xxx Win và kết thúc).
        size: n, 
        board: [[ ], [ ], [ ] …], (Kích thước nxn)
        time1: 100, (thời gian còn lại của đội 1)
        time2: 100, (thời gian còn lại của đội 2)
        team1_id: xxx, (id của team1)
        team2_id: xxx,	
        turn: xxx,  (id của team nào thì tới lượt của team đó, tới đội nào thì đội đó sẽ đếm ngược thời gian còn lại)
        score1: 0,
        score2: 1, (điểm của đội 2)

    }
    ```
- Backend
    ``` js
    {
        match_id: xxx,
        team_id: xxx,
        x: 1,
        y: 2
    }
    ```

## Requirements Knowledge
- [x] Minimax Algorithm
- [x] Alpha-Beta Pruning
- [x] Zobrist Hashing
## References
- [1] [](https://github.com/qwertyforce/gomoku_ai)
- [2] [](https://github.com/VictorHarri-Chal/Gomoku)
- [3] [](https://github.com/Giang-Dang/gomoku-AB-pruning)
- [4] [](https://paperswithcode.com/paper/alphagomoku-an-alphago-based-gomoku)
- [5] [](https://github.com/aaazyq/Gomoku)