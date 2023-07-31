
# Results vs. 3.10.4

- fork: python
- ref: 3.12
- machine: linux-x86_64
- commit hash: e3b5ed7
- commit date: 2023-07-29
- overall geometric mean: 1.29x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-pythonperf2-x86_64-python-3.12-3.12.0b4+-e3b5ed7 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 284 ms: 1.23x faster                                         |
| docutils       | 3.40 sec                                                     | 2.90 sec: 1.17x faster                                       |
| tornado_http   | 152 ms                                                       | 122 ms: 1.25x faster                                         |
| Geometric mean | (ref)                                                        | 1.22x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-pythonperf2-x86_64-python-3.12-3.12.0b4+-e3b5ed7 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 89.4 ms: 1.54x faster                                        |
| float          | 110 ms                                                       | 78.6 ms: 1.40x faster                                        |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                         |
| Geometric mean | (ref)                                                        | 1.31x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-pythonperf2-x86_64-python-3.12-3.12.0b4+-e3b5ed7 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 144 ms: 1.35x faster                                         |
| regex_v8       | 26.6 ms                                                      | 23.2 ms: 1.15x faster                                        |
| regex_dna      | 259 ms                                                       | 247 ms: 1.05x faster                                         |
| regex_effbot   | 2.99 ms                                                      | 3.75 ms: 1.25x slower                                        |
| Geometric mean | (ref)                                                        | 1.07x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-pythonperf2-x86_64-python-3.12-3.12.0b4+-e3b5ed7 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 207 us: 1.55x faster                                         |
| pickle_pure_python   | 457 us                                                       | 321 us: 1.43x faster                                         |
| json_dumps           | 14.2 ms                                                      | 10.2 ms: 1.39x faster                                        |
| tomli_loads          | 2.97 sec                                                     | 2.18 sec: 1.36x faster                                       |
| xml_etree_process    | 76.0 ms                                                      | 57.8 ms: 1.31x faster                                        |
| json_loads           | 30.0 us                                                      | 25.6 us: 1.17x faster                                        |
| xml_etree_generate   | 94.6 ms                                                      | 85.1 ms: 1.11x faster                                        |
| xml_etree_parse      | 162 ms                                                       | 147 ms: 1.10x faster                                         |
| xml_etree_iterparse  | 110 ms                                                       | 105 ms: 1.05x faster                                         |
| pickle               | 9.94 us                                                      | 10.0 us: 1.01x slower                                        |
| unpickle             | 14.2 us                                                      | 14.7 us: 1.04x slower                                        |
| unpickle_list        | 4.49 us                                                      | 4.68 us: 1.04x slower                                        |
| pickle_list          | 4.11 us                                                      | 4.52 us: 1.10x slower                                        |
| pickle_dict          | 30.0 us                                                      | 33.2 us: 1.11x slower                                        |
| Geometric mean       | (ref)                                                        | 1.14x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-pythonperf2-x86_64-python-3.12-3.12.0b4+-e3b5ed7 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.5 ms: 1.00x faster                                        |
| python_startup_no_site | 7.32 ms                                                      | 8.47 ms: 1.16x slower                                        |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-pythonperf2-x86_64-python-3.12-3.12.0b4+-e3b5ed7 |
|-----------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 9.89 ms: 1.49x faster                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-pythonperf2-x86_64-python-3.12-3.12.0b4+-e3b5ed7 |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 152 us: 3.44x faster                                         |
| deltablue                | 7.47 ms                                                      | 3.27 ms: 2.28x faster                                        |
| asyncio_tcp              | 782 ms                                                       | 381 ms: 2.05x faster                                         |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.57 sec: 1.97x faster                                       |
| logging_silent           | 166 ns                                                       | 91.7 ns: 1.81x faster                                        |
| richards_super           | 90.8 ms                                                      | 53.8 ms: 1.69x faster                                        |
| go                       | 259 ms                                                       | 153 ms: 1.69x faster                                         |
| scimark_lu               | 164 ms                                                       | 97.4 ms: 1.68x faster                                        |
| chaos                    | 107 ms                                                       | 63.8 ms: 1.68x faster                                        |
| scimark_monte_carlo      | 109 ms                                                       | 66.9 ms: 1.64x faster                                        |
| scimark_sor              | 177 ms                                                       | 109 ms: 1.63x faster                                         |
| sqlglot_parse            | 2.26 ms                                                      | 1.39 ms: 1.62x faster                                        |
| generators               | 58.0 ms                                                      | 35.8 ms: 1.62x faster                                        |
| hexiom                   | 9.52 ms                                                      | 5.88 ms: 1.62x faster                                        |
| raytrace                 | 488 ms                                                       | 308 ms: 1.59x faster                                         |
| richards                 | 74.1 ms                                                      | 46.8 ms: 1.58x faster                                        |
| pyflate                  | 697 ms                                                       | 446 ms: 1.56x faster                                         |
| unpickle_pure_python     | 321 us                                                       | 207 us: 1.55x faster                                         |
| nbody                    | 137 ms                                                       | 89.4 ms: 1.54x faster                                        |
| async_tree_none          | 700 ms                                                       | 459 ms: 1.52x faster                                         |
| sqlglot_transpile        | 2.71 ms                                                      | 1.78 ms: 1.52x faster                                        |
| async_tree_io            | 1.61 sec                                                     | 1.06 sec: 1.52x faster                                       |
| spectral_norm            | 136 ms                                                       | 89.9 ms: 1.52x faster                                        |
| async_tree_memoization   | 824 ms                                                       | 551 ms: 1.50x faster                                         |
| mako                     | 14.7 ms                                                      | 9.89 ms: 1.49x faster                                        |
| crypto_pyaes             | 118 ms                                                       | 80.9 ms: 1.46x faster                                        |
| fannkuch                 | 496 ms                                                       | 342 ms: 1.45x faster                                         |
| pickle_pure_python       | 457 us                                                       | 321 us: 1.43x faster                                         |
| float                    | 110 ms                                                       | 78.6 ms: 1.40x faster                                        |
| json_dumps               | 14.2 ms                                                      | 10.2 ms: 1.39x faster                                        |
| tomli_loads              | 2.97 sec                                                     | 2.18 sec: 1.36x faster                                       |
| coroutines               | 30.4 ms                                                      | 22.4 ms: 1.36x faster                                        |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 705 ms: 1.35x faster                                         |
| logging_simple           | 8.90 us                                                      | 6.60 us: 1.35x faster                                        |
| regex_compile            | 194 ms                                                       | 144 ms: 1.35x faster                                         |
| pycparser                | 1.66 sec                                                     | 1.24 sec: 1.34x faster                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.62 sec: 1.33x faster                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 794 ms: 1.32x faster                                         |
| xml_etree_process        | 76.0 ms                                                      | 57.8 ms: 1.31x faster                                        |
| logging_format           | 9.57 us                                                      | 7.32 us: 1.31x faster                                        |
| deepcopy_memo            | 48.9 us                                                      | 37.5 us: 1.30x faster                                        |
| mypy2                    | 466 ms                                                       | 366 ms: 1.27x faster                                         |
| nqueens                  | 112 ms                                                       | 89.1 ms: 1.26x faster                                        |
| tornado_http             | 152 ms                                                       | 122 ms: 1.25x faster                                         |
| comprehensions           | 26.9 us                                                      | 21.8 us: 1.23x faster                                        |
| 2to3                     | 350 ms                                                       | 284 ms: 1.23x faster                                         |
| dulwich_log              | 80.1 ms                                                      | 65.8 ms: 1.22x faster                                        |
| sqlglot_normalize        | 144 ms                                                       | 119 ms: 1.21x faster                                         |
| deepcopy                 | 454 us                                                       | 375 us: 1.21x faster                                         |
| mdp                      | 3.03 sec                                                     | 2.52 sec: 1.20x faster                                       |
| sqlglot_optimize         | 70.3 ms                                                      | 58.3 ms: 1.20x faster                                        |
| scimark_fft              | 359 ms                                                       | 300 ms: 1.20x faster                                         |
| bench_thread_pool        | 1.14 ms                                                      | 964 us: 1.18x faster                                         |
| deepcopy_reduce          | 4.03 us                                                      | 3.44 us: 1.17x faster                                        |
| docutils                 | 3.40 sec                                                     | 2.90 sec: 1.17x faster                                       |
| json_loads               | 30.0 us                                                      | 25.6 us: 1.17x faster                                        |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 4.44 ms: 1.17x faster                                        |
| unpack_sequence          | 59.5 ns                                                      | 50.9 ns: 1.17x faster                                        |
| json                     | 5.96 ms                                                      | 5.18 ms: 1.15x faster                                        |
| regex_v8                 | 26.6 ms                                                      | 23.2 ms: 1.15x faster                                        |
| pathlib                  | 21.7 ms                                                      | 19.0 ms: 1.14x faster                                        |
| xml_etree_generate       | 94.6 ms                                                      | 85.1 ms: 1.11x faster                                        |
| xml_etree_parse          | 162 ms                                                       | 147 ms: 1.10x faster                                         |
| create_gc_cycles         | 1.82 ms                                                      | 1.66 ms: 1.10x faster                                        |
| async_generators         | 422 ms                                                       | 389 ms: 1.09x faster                                         |
| meteor_contest           | 137 ms                                                       | 126 ms: 1.08x faster                                         |
| sqlite_synth             | 2.97 us                                                      | 2.75 us: 1.08x faster                                        |
| regex_dna                | 259 ms                                                       | 247 ms: 1.05x faster                                         |
| xml_etree_iterparse      | 110 ms                                                       | 105 ms: 1.05x faster                                         |
| pidigits                 | 271 ms                                                       | 260 ms: 1.04x faster                                         |
| python_startup           | 11.5 ms                                                      | 11.5 ms: 1.00x faster                                        |
| pickle                   | 9.94 us                                                      | 10.0 us: 1.01x slower                                        |
| unpickle                 | 14.2 us                                                      | 14.7 us: 1.04x slower                                        |
| unpickle_list            | 4.49 us                                                      | 4.68 us: 1.04x slower                                        |
| gc_traversal             | 3.45 ms                                                      | 3.76 ms: 1.09x slower                                        |
| pickle_list              | 4.11 us                                                      | 4.52 us: 1.10x slower                                        |
| pickle_dict              | 30.0 us                                                      | 33.2 us: 1.11x slower                                        |
| python_startup_no_site   | 7.32 ms                                                      | 8.47 ms: 1.16x slower                                        |
| dask                     | 463 ms                                                       | 568 ms: 1.23x slower                                         |
| regex_effbot             | 2.99 ms                                                      | 3.75 ms: 1.25x slower                                        |
| coverage                 | 64.0 ms                                                      | 91.2 ms: 1.43x slower                                        |
| Geometric mean           | (ref)                                                        | 1.29x faster                                                 |

Benchmark hidden because not significant (2): bench_mp_pool, telco
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
