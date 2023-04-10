# caro-ai
AI Project for Caro Game
## Introduction

## JSON API
- Frontend
    ``` json
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
    ``` json
    {
        match_id: xxx,
        team_id: xxx,
        x: 1,
        y: 2
    }
    ```

## Requirements Knowledge
- [x] Machine Learning
- [x] Reinforcement Learning
- [x] Neural Network
- [x] Monte Carlo Tree Search
## References
- [1] [A Simple Alpha(Go) Zero Tutorial](https://web.stanford.edu/~surag/posts/alphazero.html)
- [2] [Monte Carlo Tree Search](https://web.archive.org/web/20180623055344/http://mcts.ai/about/index.html)