
# Results vs. 3.10.4

- fork: faster-cpython
- ref: no_local_eval_breake
- machine: linux-x86_64
- commit hash: 4d1b4d4
- commit date: 2023-05-12
- overall geometric mean: 1.31x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230512-pythonperf2-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a7+-4d1b4d4 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 283 ms: 1.24x faster                                                                   |
| docutils       | 3.40 sec                                                     | 2.87 sec: 1.19x faster                                                                 |
| tornado_http   | 152 ms                                                       | 113 ms: 1.34x faster                                                                   |
| Geometric mean | (ref)                                                        | 1.25x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230512-pythonperf2-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a7+-4d1b4d4 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 85.6 ms: 1.60x faster                                                                  |
| float          | 110 ms                                                       | 77.7 ms: 1.42x faster                                                                  |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                                                   |
| Geometric mean | (ref)                                                        | 1.33x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230512-pythonperf2-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a7+-4d1b4d4 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 143 ms: 1.35x faster                                                                   |
| regex_v8       | 26.6 ms                                                      | 23.5 ms: 1.13x faster                                                                  |
| regex_dna      | 259 ms                                                       | 230 ms: 1.13x faster                                                                   |
| regex_effbot   | 2.99 ms                                                      | 3.52 ms: 1.18x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.10x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230512-pythonperf2-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a7+-4d1b4d4 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 204 us: 1.57x faster                                                                   |
| pickle_pure_python   | 457 us                                                       | 321 us: 1.43x faster                                                                   |
| json_dumps           | 14.2 ms                                                      | 10.3 ms: 1.38x faster                                                                  |
| tomli_loads          | 2.97 sec                                                     | 2.16 sec: 1.37x faster                                                                 |
| xml_etree_process    | 76.0 ms                                                      | 58.7 ms: 1.29x faster                                                                  |
| json_loads           | 30.0 us                                                      | 24.0 us: 1.25x faster                                                                  |
| xml_etree_generate   | 94.6 ms                                                      | 85.3 ms: 1.11x faster                                                                  |
| xml_etree_parse      | 162 ms                                                       | 147 ms: 1.10x faster                                                                   |
| xml_etree_iterparse  | 110 ms                                                       | 105 ms: 1.05x faster                                                                   |
| unpickle             | 14.2 us                                                      | 14.3 us: 1.01x slower                                                                  |
| pickle               | 9.94 us                                                      | 10.1 us: 1.01x slower                                                                  |
| pickle_list          | 4.11 us                                                      | 4.32 us: 1.05x slower                                                                  |
| pickle_dict          | 30.0 us                                                      | 32.0 us: 1.07x slower                                                                  |
| unpickle_list        | 4.49 us                                                      | 4.88 us: 1.09x slower                                                                  |
| Geometric mean       | (ref)                                                        | 1.15x faster                                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230512-pythonperf2-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a7+-4d1b4d4 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.4 ms: 1.01x faster                                                                  |
| python_startup_no_site | 7.32 ms                                                      | 8.39 ms: 1.15x slower                                                                  |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230512-pythonperf2-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a7+-4d1b4d4 |
|-----------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 9.89 ms: 1.48x faster                                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230512-pythonperf2-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a7+-4d1b4d4 |
|--------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 151 us: 3.46x faster                                                                   |
| deltablue                | 7.47 ms                                                      | 3.20 ms: 2.34x faster                                                                  |
| asyncio_tcp              | 782 ms                                                       | 380 ms: 2.06x faster                                                                   |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.57 sec: 1.97x faster                                                                 |
| logging_silent           | 166 ns                                                       | 90.5 ns: 1.83x faster                                                                  |
| richards_super           | 90.8 ms                                                      | 50.1 ms: 1.81x faster                                                                  |
| go                       | 259 ms                                                       | 144 ms: 1.79x faster                                                                   |
| richards                 | 74.1 ms                                                      | 43.5 ms: 1.70x faster                                                                  |
| chaos                    | 107 ms                                                       | 63.6 ms: 1.68x faster                                                                  |
| scimark_lu               | 164 ms                                                       | 98.0 ms: 1.67x faster                                                                  |
| scimark_sor              | 177 ms                                                       | 107 ms: 1.65x faster                                                                   |
| hexiom                   | 9.52 ms                                                      | 5.79 ms: 1.65x faster                                                                  |
| sqlglot_parse            | 2.26 ms                                                      | 1.38 ms: 1.63x faster                                                                  |
| generators               | 58.0 ms                                                      | 35.7 ms: 1.62x faster                                                                  |
| raytrace                 | 488 ms                                                       | 302 ms: 1.62x faster                                                                   |
| nbody                    | 137 ms                                                       | 85.6 ms: 1.60x faster                                                                  |
| scimark_monte_carlo      | 109 ms                                                       | 68.5 ms: 1.60x faster                                                                  |
| pyflate                  | 697 ms                                                       | 441 ms: 1.58x faster                                                                   |
| unpickle_pure_python     | 321 us                                                       | 204 us: 1.57x faster                                                                   |
| async_tree_io            | 1.61 sec                                                     | 1.05 sec: 1.53x faster                                                                 |
| async_tree_none          | 700 ms                                                       | 458 ms: 1.53x faster                                                                   |
| spectral_norm            | 136 ms                                                       | 89.5 ms: 1.52x faster                                                                  |
| sqlglot_transpile        | 2.71 ms                                                      | 1.78 ms: 1.52x faster                                                                  |
| async_tree_memoization   | 824 ms                                                       | 550 ms: 1.50x faster                                                                   |
| crypto_pyaes             | 118 ms                                                       | 79.5 ms: 1.49x faster                                                                  |
| mako                     | 14.7 ms                                                      | 9.89 ms: 1.48x faster                                                                  |
| pickle_pure_python       | 457 us                                                       | 321 us: 1.43x faster                                                                   |
| float                    | 110 ms                                                       | 77.7 ms: 1.42x faster                                                                  |
| bench_mp_pool            | 7.18 ms                                                      | 5.15 ms: 1.39x faster                                                                  |
| fannkuch                 | 496 ms                                                       | 356 ms: 1.39x faster                                                                   |
| json_dumps               | 14.2 ms                                                      | 10.3 ms: 1.38x faster                                                                  |
| tomli_loads              | 2.97 sec                                                     | 2.16 sec: 1.37x faster                                                                 |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 698 ms: 1.36x faster                                                                   |
| deepcopy_memo            | 48.9 us                                                      | 35.9 us: 1.36x faster                                                                  |
| coroutines               | 30.4 ms                                                      | 22.4 ms: 1.36x faster                                                                  |
| regex_compile            | 194 ms                                                       | 143 ms: 1.35x faster                                                                   |
| pycparser                | 1.66 sec                                                     | 1.23 sec: 1.35x faster                                                                 |
| tornado_http             | 152 ms                                                       | 113 ms: 1.34x faster                                                                   |
| pprint_pformat           | 2.15 sec                                                     | 1.61 sec: 1.34x faster                                                                 |
| logging_simple           | 8.90 us                                                      | 6.67 us: 1.33x faster                                                                  |
| pprint_safe_repr         | 1.05 sec                                                     | 788 ms: 1.33x faster                                                                   |
| logging_format           | 9.57 us                                                      | 7.32 us: 1.31x faster                                                                  |
| xml_etree_process        | 76.0 ms                                                      | 58.7 ms: 1.29x faster                                                                  |
| json_loads               | 30.0 us                                                      | 24.0 us: 1.25x faster                                                                  |
| nqueens                  | 112 ms                                                       | 90.3 ms: 1.25x faster                                                                  |
| comprehensions           | 26.9 us                                                      | 21.7 us: 1.24x faster                                                                  |
| 2to3                     | 350 ms                                                       | 283 ms: 1.24x faster                                                                   |
| sqlglot_normalize        | 144 ms                                                       | 117 ms: 1.24x faster                                                                   |
| dulwich_log              | 80.1 ms                                                      | 65.3 ms: 1.23x faster                                                                  |
| deepcopy                 | 454 us                                                       | 373 us: 1.22x faster                                                                   |
| sqlglot_optimize         | 70.3 ms                                                      | 58.2 ms: 1.21x faster                                                                  |
| mdp                      | 3.03 sec                                                     | 2.52 sec: 1.20x faster                                                                 |
| scimark_fft              | 359 ms                                                       | 300 ms: 1.20x faster                                                                   |
| deepcopy_reduce          | 4.03 us                                                      | 3.39 us: 1.19x faster                                                                  |
| docutils                 | 3.40 sec                                                     | 2.87 sec: 1.19x faster                                                                 |
| bench_thread_pool        | 1.14 ms                                                      | 958 us: 1.19x faster                                                                   |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 4.40 ms: 1.18x faster                                                                  |
| unpack_sequence          | 59.5 ns                                                      | 51.6 ns: 1.15x faster                                                                  |
| json                     | 5.96 ms                                                      | 5.18 ms: 1.15x faster                                                                  |
| regex_v8                 | 26.6 ms                                                      | 23.5 ms: 1.13x faster                                                                  |
| regex_dna                | 259 ms                                                       | 230 ms: 1.13x faster                                                                   |
| sqlite_synth             | 2.97 us                                                      | 2.65 us: 1.12x faster                                                                  |
| pathlib                  | 21.7 ms                                                      | 19.4 ms: 1.12x faster                                                                  |
| create_gc_cycles         | 1.82 ms                                                      | 1.63 ms: 1.12x faster                                                                  |
| xml_etree_generate       | 94.6 ms                                                      | 85.3 ms: 1.11x faster                                                                  |
| xml_etree_parse          | 162 ms                                                       | 147 ms: 1.10x faster                                                                   |
| async_generators         | 422 ms                                                       | 386 ms: 1.09x faster                                                                   |
| meteor_contest           | 137 ms                                                       | 130 ms: 1.05x faster                                                                   |
| xml_etree_iterparse      | 110 ms                                                       | 105 ms: 1.05x faster                                                                   |
| pidigits                 | 271 ms                                                       | 260 ms: 1.04x faster                                                                   |
| python_startup           | 11.5 ms                                                      | 11.4 ms: 1.01x faster                                                                  |
| unpickle                 | 14.2 us                                                      | 14.3 us: 1.01x slower                                                                  |
| pickle                   | 9.94 us                                                      | 10.1 us: 1.01x slower                                                                  |
| pickle_list              | 4.11 us                                                      | 4.32 us: 1.05x slower                                                                  |
| pickle_dict              | 30.0 us                                                      | 32.0 us: 1.07x slower                                                                  |
| unpickle_list            | 4.49 us                                                      | 4.88 us: 1.09x slower                                                                  |
| gc_traversal             | 3.45 ms                                                      | 3.80 ms: 1.10x slower                                                                  |
| python_startup_no_site   | 7.32 ms                                                      | 8.39 ms: 1.15x slower                                                                  |
| regex_effbot             | 2.99 ms                                                      | 3.52 ms: 1.18x slower                                                                  |
| dask                     | 463 ms                                                       | 556 ms: 1.20x slower                                                                   |
| coverage                 | 64.0 ms                                                      | 90.5 ms: 1.42x slower                                                                  |
| Geometric mean           | (ref)                                                        | 1.31x faster                                                                           |

Benchmark hidden because not significant (2): mypy2, telco
Ignored benchmarks (16) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
