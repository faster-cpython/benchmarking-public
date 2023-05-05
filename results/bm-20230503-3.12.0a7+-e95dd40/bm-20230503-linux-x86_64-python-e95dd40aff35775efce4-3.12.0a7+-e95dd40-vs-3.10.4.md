
# Results vs. 3.10.4

- fork: python
- ref: e95dd40aff35775efce4
- machine: linux-x86_64
- commit hash: e95dd40
- commit date: 2023-05-03
- overall geometric mean: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230503-linux-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 271 ms: 1.24x faster                                                   |
| docutils       | 3.19 sec                                                            | 2.73 sec: 1.17x faster                                                 |
| tornado_http   | 129 ms                                                              | 99.5 ms: 1.30x faster                                                  |
| Geometric mean | (ref)                                                               | 1.23x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230503-linux-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 146 ms                                                              | 87.5 ms: 1.67x faster                                                  |
| float          | 110 ms                                                              | 83.2 ms: 1.32x faster                                                  |
| pidigits       | 190 ms                                                              | 197 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                               | 1.28x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230503-linux-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 145 ms: 1.22x faster                                                   |
| regex_v8       | 24.9 ms                                                             | 22.1 ms: 1.13x faster                                                  |
| regex_dna      | 213 ms                                                              | 200 ms: 1.07x faster                                                   |
| regex_effbot   | 3.22 ms                                                             | 3.69 ms: 1.15x slower                                                  |
| Geometric mean | (ref)                                                               | 1.06x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230503-linux-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 313 us: 1.46x faster                                                   |
| json_dumps           | 13.7 ms                                                             | 9.98 ms: 1.37x faster                                                  |
| unpickle_pure_python | 300 us                                                              | 219 us: 1.37x faster                                                   |
| xml_etree_process    | 74.8 ms                                                             | 59.2 ms: 1.26x faster                                                  |
| json_loads           | 29.3 us                                                             | 25.8 us: 1.14x faster                                                  |
| xml_etree_generate   | 94.9 ms                                                             | 84.7 ms: 1.12x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                              | 104 ms: 1.07x faster                                                   |
| xml_etree_parse      | 164 ms                                                              | 154 ms: 1.06x faster                                                   |
| pickle_list          | 4.73 us                                                             | 4.50 us: 1.05x faster                                                  |
| unpickle_list        | 4.94 us                                                             | 5.02 us: 1.02x slower                                                  |
| pickle               | 10.2 us                                                             | 10.5 us: 1.03x slower                                                  |
| pickle_dict          | 27.8 us                                                             | 30.7 us: 1.10x slower                                                  |
| Geometric mean       | (ref)                                                               | 1.12x faster                                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230503-linux-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 9.20 ms: 1.54x faster                                                  |
| python_startup_no_site | 5.80 ms                                                             | 6.73 ms: 1.16x slower                                                  |
| Geometric mean         | (ref)                                                               | 1.15x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230503-linux-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|-----------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako      | 14.7 ms                                                             | 10.7 ms: 1.38x faster                                                  |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230503-linux-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|-------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 75.7 ms                                                             | 31.4 ms: 2.41x faster                                                  |
| deltablue               | 7.30 ms                                                             | 3.52 ms: 2.07x faster                                                  |
| asyncio_tcp             | 922 ms                                                              | 506 ms: 1.82x faster                                                   |
| logging_silent          | 169 ns                                                              | 101 ns: 1.67x faster                                                   |
| nbody                   | 146 ms                                                              | 87.5 ms: 1.67x faster                                                  |
| go                      | 226 ms                                                              | 136 ms: 1.66x faster                                                   |
| richards                | 74.2 ms                                                             | 45.0 ms: 1.65x faster                                                  |
| scimark_sor             | 198 ms                                                              | 124 ms: 1.59x faster                                                   |
| raytrace                | 470 ms                                                              | 303 ms: 1.55x faster                                                   |
| hexiom                  | 9.50 ms                                                             | 6.18 ms: 1.54x faster                                                  |
| python_startup          | 14.1 ms                                                             | 9.20 ms: 1.54x faster                                                  |
| sqlglot_parse           | 2.07 ms                                                             | 1.35 ms: 1.53x faster                                                  |
| chaos                   | 106 ms                                                              | 70.4 ms: 1.50x faster                                                  |
| crypto_pyaes            | 117 ms                                                              | 78.0 ms: 1.50x faster                                                  |
| pyflate                 | 671 ms                                                              | 451 ms: 1.49x faster                                                   |
| scimark_monte_carlo     | 109 ms                                                              | 73.6 ms: 1.47x faster                                                  |
| async_tree_io           | 1.78 sec                                                            | 1.22 sec: 1.47x faster                                                 |
| sqlglot_transpile       | 2.45 ms                                                             | 1.68 ms: 1.46x faster                                                  |
| pickle_pure_python      | 457 us                                                              | 313 us: 1.46x faster                                                   |
| async_tree_none         | 713 ms                                                              | 497 ms: 1.43x faster                                                   |
| scimark_lu              | 160 ms                                                              | 113 ms: 1.41x faster                                                   |
| async_tree_memoization  | 853 ms                                                              | 604 ms: 1.41x faster                                                   |
| spectral_norm           | 150 ms                                                              | 108 ms: 1.39x faster                                                   |
| mako                    | 14.7 ms                                                             | 10.7 ms: 1.38x faster                                                  |
| json_dumps              | 13.7 ms                                                             | 9.98 ms: 1.37x faster                                                  |
| unpickle_pure_python    | 300 us                                                              | 219 us: 1.37x faster                                                   |
| pycparser               | 1.53 sec                                                            | 1.14 sec: 1.35x faster                                                 |
| deepcopy_memo           | 51.8 us                                                             | 38.5 us: 1.34x faster                                                  |
| coroutines              | 31.8 ms                                                             | 23.7 ms: 1.34x faster                                                  |
| pprint_pformat          | 1.98 sec                                                            | 1.49 sec: 1.33x faster                                                 |
| float                   | 110 ms                                                              | 83.2 ms: 1.32x faster                                                  |
| async_tree_cpu_io_mixed | 944 ms                                                              | 719 ms: 1.31x faster                                                   |
| pprint_safe_repr        | 953 ms                                                              | 732 ms: 1.30x faster                                                   |
| logging_simple          | 8.21 us                                                             | 6.34 us: 1.30x faster                                                  |
| tornado_http            | 129 ms                                                              | 99.5 ms: 1.30x faster                                                  |
| logging_format          | 9.07 us                                                             | 7.06 us: 1.28x faster                                                  |
| unpack_sequence         | 65.6 ns                                                             | 51.1 ns: 1.28x faster                                                  |
| fannkuch                | 485 ms                                                              | 380 ms: 1.28x faster                                                   |
| xml_etree_process       | 74.8 ms                                                             | 59.2 ms: 1.26x faster                                                  |
| 2to3                    | 336 ms                                                              | 271 ms: 1.24x faster                                                   |
| mypy2                   | 432 ms                                                              | 351 ms: 1.23x faster                                                   |
| nqueens                 | 98.8 ms                                                             | 80.9 ms: 1.22x faster                                                  |
| regex_compile           | 177 ms                                                              | 145 ms: 1.22x faster                                                   |
| deepcopy                | 438 us                                                              | 368 us: 1.19x faster                                                   |
| sqlglot_normalize       | 135 ms                                                              | 113 ms: 1.19x faster                                                   |
| deepcopy_reduce         | 3.80 us                                                             | 3.22 us: 1.18x faster                                                  |
| sqlglot_optimize        | 65.3 ms                                                             | 55.5 ms: 1.18x faster                                                  |
| comprehensions          | 27.3 us                                                             | 23.3 us: 1.17x faster                                                  |
| docutils                | 3.19 sec                                                            | 2.73 sec: 1.17x faster                                                 |
| scimark_fft             | 425 ms                                                              | 367 ms: 1.16x faster                                                   |
| bench_thread_pool       | 954 us                                                              | 838 us: 1.14x faster                                                   |
| json_loads              | 29.3 us                                                             | 25.8 us: 1.14x faster                                                  |
| sqlalchemy_declarative  | 166 ms                                                              | 147 ms: 1.13x faster                                                   |
| regex_v8                | 24.9 ms                                                             | 22.1 ms: 1.13x faster                                                  |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 5.01 ms: 1.12x faster                                                  |
| xml_etree_generate      | 94.9 ms                                                             | 84.7 ms: 1.12x faster                                                  |
| sqlalchemy_imperative   | 21.2 ms                                                             | 18.9 ms: 1.12x faster                                                  |
| dulwich_log             | 76.3 ms                                                             | 68.3 ms: 1.12x faster                                                  |
| create_gc_cycles        | 1.64 ms                                                             | 1.49 ms: 1.10x faster                                                  |
| sqlite_synth            | 2.97 us                                                             | 2.72 us: 1.09x faster                                                  |
| json                    | 5.41 ms                                                             | 5.01 ms: 1.08x faster                                                  |
| pathlib                 | 19.8 ms                                                             | 18.5 ms: 1.07x faster                                                  |
| regex_dna               | 213 ms                                                              | 200 ms: 1.07x faster                                                   |
| xml_etree_iterparse     | 111 ms                                                              | 104 ms: 1.07x faster                                                   |
| xml_etree_parse         | 164 ms                                                              | 154 ms: 1.06x faster                                                   |
| pickle_list             | 4.73 us                                                             | 4.50 us: 1.05x faster                                                  |
| meteor_contest          | 115 ms                                                              | 113 ms: 1.02x faster                                                   |
| unpickle_list           | 4.94 us                                                             | 5.02 us: 1.02x slower                                                  |
| pickle                  | 10.2 us                                                             | 10.5 us: 1.03x slower                                                  |
| pidigits                | 190 ms                                                              | 197 ms: 1.04x slower                                                   |
| async_generators        | 420 ms                                                              | 446 ms: 1.06x slower                                                   |
| pickle_dict             | 27.8 us                                                             | 30.7 us: 1.10x slower                                                  |
| gc_traversal            | 3.53 ms                                                             | 3.97 ms: 1.12x slower                                                  |
| regex_effbot            | 3.22 ms                                                             | 3.69 ms: 1.15x slower                                                  |
| python_startup_no_site  | 5.80 ms                                                             | 6.73 ms: 1.16x slower                                                  |
| dask                    | 437 ms                                                              | 540 ms: 1.24x slower                                                   |
| coverage                | 70.6 ms                                                             | 103 ms: 1.45x slower                                                   |
| Geometric mean          | (ref)                                                               | 1.24x faster                                                           |

Benchmark hidden because not significant (4): mdp, bench_mp_pool, unpickle, telco
Ignored benchmarks (15) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
