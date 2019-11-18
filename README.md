# server-allocation

This is a simulator for distributed server allocation problem solved with ILP, SUM algorithm and ESUM algorithm.

## Features

This simulator enables to

- choose multiple solving methods
- put parameters with command line
- increment parameters gradually
- get optimal solution and cpu solving time
- make graph for cpu time
- send results to slack

## Requirement

- solvers
  - CPLEX 12.7.1.0
  - SCIP 6.0.2
  - GLPK 4.65
- python libraries
  - numpy
  - pandas
  - pulp
  - itertools
  - slackweb
  - configparser
  - csv

## Usage

```bash
git clone https://github.com/adshidtadka/server-allocation.git
cd server-allocation/src
python Result.py
```

## Author

- Sawa Takaaki
- Oki laboratory Communication and Computer Engineering Graduate School of Informatics Kyoto University
- tsawa@icn.cce.i.kyoto-u.ac.jp

## License

This software is released under the MIT License, see [LICENSE](https://github.com/adshidtadka/server-allocation/blob/master/LICENSE).
