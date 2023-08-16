
# Results vs. 3.10.4

- fork: python
- ref: 3.12
- machine: linux-x86_64
- commit hash: d20d52b
- commit date: 2023-08-11
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-pythonperf2-x86_64-python-3.12-3.12.0rc1+-d20d52b |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 283 ms: 1.23x faster                                          |
| docutils       | 3.40 sec                                                     | 2.90 sec: 1.18x faster                                        |
| tornado_http   | 152 ms                                                       | 119 ms: 1.28x faster                                          |
| Geometric mean | (ref)                                                        | 1.23x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-pythonperf2-x86_64-python-3.12-3.12.0rc1+-d20d52b |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 89.7 ms: 1.53x faster                                         |
| float          | 110 ms                                                       | 78.1 ms: 1.41x faster                                         |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                          |
| Geometric mean | (ref)                                                        | 1.31x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-pythonperf2-x86_64-python-3.12-3.12.0rc1+-d20d52b |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 144 ms: 1.34x faster                                          |
| regex_v8       | 26.6 ms                                                      | 23.1 ms: 1.15x faster                                         |
| regex_dna      | 259 ms                                                       | 238 ms: 1.09x faster                                          |
| regex_effbot   | 2.99 ms                                                      | 3.63 ms: 1.21x slower                                         |
| Geometric mean | (ref)                                                        | 1.09x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-pythonperf2-x86_64-python-3.12-3.12.0rc1+-d20d52b |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 203 us: 1.58x faster                                          |
| pickle_pure_python   | 457 us                                                       | 318 us: 1.44x faster                                          |
| tomli_loads          | 2.97 sec                                                     | 2.15 sec: 1.38x faster                                        |
| json_dumps           | 14.2 ms                                                      | 10.4 ms: 1.37x faster                                         |
| xml_etree_process    | 76.0 ms                                                      | 57.9 ms: 1.31x faster                                         |
| json_loads           | 30.0 us                                                      | 24.2 us: 1.24x faster                                         |
| xml_etree_generate   | 94.6 ms                                                      | 84.6 ms: 1.12x faster                                         |
| xml_etree_parse      | 162 ms                                                       | 148 ms: 1.09x faster                                          |
| xml_etree_iterparse  | 110 ms                                                       | 106 ms: 1.04x faster                                          |
| pickle               | 9.94 us                                                      | 10.0 us: 1.01x slower                                         |
| unpickle_list        | 4.49 us                                                      | 4.68 us: 1.04x slower                                         |
| unpickle             | 14.2 us                                                      | 15.0 us: 1.06x slower                                         |
| pickle_dict          | 30.0 us                                                      | 31.9 us: 1.06x slower                                         |
| pickle_list          | 4.11 us                                                      | 4.41 us: 1.07x slower                                         |
| Geometric mean       | (ref)                                                        | 1.15x faster                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-pythonperf2-x86_64-python-3.12-3.12.0rc1+-d20d52b |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup_no_site | 7.32 ms                                                      | 8.50 ms: 1.16x slower                                         |
| Geometric mean         | (ref)                                                        | 1.08x slower                                                  |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-pythonperf2-x86_64-python-3.12-3.12.0rc1+-d20d52b |
|-----------|:------------------------------------------------------------:|:-------------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 9.95 ms: 1.48x faster                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-pythonperf2-x86_64-python-3.12-3.12.0rc1+-d20d52b |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 151 us: 3.47x faster                                          |
| deltablue                | 7.47 ms                                                      | 3.22 ms: 2.32x faster                                         |
| asyncio_tcp              | 782 ms                                                       | 380 ms: 2.06x faster                                          |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.57 sec: 1.96x faster                                        |
| logging_silent           | 166 ns                                                       | 92.6 ns: 1.79x faster                                         |
| go                       | 259 ms                                                       | 147 ms: 1.76x faster                                          |
| chaos                    | 107 ms                                                       | 62.3 ms: 1.72x faster                                         |
| richards_super           | 90.8 ms                                                      | 53.2 ms: 1.71x faster                                         |
| scimark_lu               | 164 ms                                                       | 98.4 ms: 1.66x faster                                         |
| richards                 | 74.1 ms                                                      | 44.7 ms: 1.66x faster                                         |
| raytrace                 | 488 ms                                                       | 295 ms: 1.65x faster                                          |
| hexiom                   | 9.52 ms                                                      | 5.80 ms: 1.64x faster                                         |
| sqlglot_parse            | 2.26 ms                                                      | 1.39 ms: 1.63x faster                                         |
| scimark_sor              | 177 ms                                                       | 109 ms: 1.62x faster                                          |
| scimark_monte_carlo      | 109 ms                                                       | 68.7 ms: 1.59x faster                                         |
| generators               | 58.0 ms                                                      | 36.4 ms: 1.59x faster                                         |
| pyflate                  | 697 ms                                                       | 442 ms: 1.58x faster                                          |
| unpickle_pure_python     | 321 us                                                       | 203 us: 1.58x faster                                          |
| async_tree_none          | 700 ms                                                       | 456 ms: 1.53x faster                                          |
| async_tree_io            | 1.61 sec                                                     | 1.05 sec: 1.53x faster                                        |
| nbody                    | 137 ms                                                       | 89.7 ms: 1.53x faster                                         |
| spectral_norm            | 136 ms                                                       | 90.2 ms: 1.51x faster                                         |
| sqlglot_transpile        | 2.71 ms                                                      | 1.79 ms: 1.51x faster                                         |
| async_tree_memoization   | 824 ms                                                       | 549 ms: 1.50x faster                                          |
| mako                     | 14.7 ms                                                      | 9.95 ms: 1.48x faster                                         |
| crypto_pyaes             | 118 ms                                                       | 81.6 ms: 1.45x faster                                         |
| pickle_pure_python       | 457 us                                                       | 318 us: 1.44x faster                                          |
| float                    | 110 ms                                                       | 78.1 ms: 1.41x faster                                         |
| tomli_loads              | 2.97 sec                                                     | 2.15 sec: 1.38x faster                                        |
| fannkuch                 | 496 ms                                                       | 360 ms: 1.38x faster                                          |
| json_dumps               | 14.2 ms                                                      | 10.4 ms: 1.37x faster                                         |
| deepcopy_memo            | 48.9 us                                                      | 36.0 us: 1.36x faster                                         |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 701 ms: 1.36x faster                                          |
| coroutines               | 30.4 ms                                                      | 22.5 ms: 1.35x faster                                         |
| regex_compile            | 194 ms                                                       | 144 ms: 1.34x faster                                          |
| logging_simple           | 8.90 us                                                      | 6.69 us: 1.33x faster                                         |
| pprint_pformat           | 2.15 sec                                                     | 1.63 sec: 1.32x faster                                        |
| xml_etree_process        | 76.0 ms                                                      | 57.9 ms: 1.31x faster                                         |
| pprint_safe_repr         | 1.05 sec                                                     | 803 ms: 1.31x faster                                          |
| pycparser                | 1.66 sec                                                     | 1.27 sec: 1.31x faster                                        |
| logging_format           | 9.57 us                                                      | 7.35 us: 1.30x faster                                         |
| tornado_http             | 152 ms                                                       | 119 ms: 1.28x faster                                          |
| nqueens                  | 112 ms                                                       | 88.3 ms: 1.27x faster                                         |
| mypy2                    | 466 ms                                                       | 367 ms: 1.27x faster                                          |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 4.14 ms: 1.26x faster                                         |
| comprehensions           | 26.9 us                                                      | 21.7 us: 1.24x faster                                         |
| json_loads               | 30.0 us                                                      | 24.2 us: 1.24x faster                                         |
| sqlglot_normalize        | 144 ms                                                       | 116 ms: 1.24x faster                                          |
| 2to3                     | 350 ms                                                       | 283 ms: 1.23x faster                                          |
| deepcopy                 | 454 us                                                       | 370 us: 1.23x faster                                          |
| sqlglot_optimize         | 70.3 ms                                                      | 57.6 ms: 1.22x faster                                         |
| dulwich_log              | 80.1 ms                                                      | 65.8 ms: 1.22x faster                                         |
| scimark_fft              | 359 ms                                                       | 297 ms: 1.21x faster                                          |
| mdp                      | 3.03 sec                                                     | 2.52 sec: 1.20x faster                                        |
| bench_thread_pool        | 1.14 ms                                                      | 947 us: 1.20x faster                                          |
| deepcopy_reduce          | 4.03 us                                                      | 3.41 us: 1.18x faster                                         |
| docutils                 | 3.40 sec                                                     | 2.90 sec: 1.18x faster                                        |
| json                     | 5.96 ms                                                      | 5.16 ms: 1.15x faster                                         |
| regex_v8                 | 26.6 ms                                                      | 23.1 ms: 1.15x faster                                         |
| unpack_sequence          | 59.5 ns                                                      | 52.2 ns: 1.14x faster                                         |
| pathlib                  | 21.7 ms                                                      | 19.2 ms: 1.13x faster                                         |
| xml_etree_generate       | 94.6 ms                                                      | 84.6 ms: 1.12x faster                                         |
| async_generators         | 422 ms                                                       | 383 ms: 1.10x faster                                          |
| create_gc_cycles         | 1.82 ms                                                      | 1.65 ms: 1.10x faster                                         |
| regex_dna                | 259 ms                                                       | 238 ms: 1.09x faster                                          |
| xml_etree_parse          | 162 ms                                                       | 148 ms: 1.09x faster                                          |
| meteor_contest           | 137 ms                                                       | 126 ms: 1.09x faster                                          |
| sqlite_synth             | 2.97 us                                                      | 2.74 us: 1.08x faster                                         |
| xml_etree_iterparse      | 110 ms                                                       | 106 ms: 1.04x faster                                          |
| pidigits                 | 271 ms                                                       | 260 ms: 1.04x faster                                          |
| telco                    | 7.14 ms                                                      | 7.07 ms: 1.01x faster                                         |
| pickle                   | 9.94 us                                                      | 10.0 us: 1.01x slower                                         |
| gc_traversal             | 3.45 ms                                                      | 3.57 ms: 1.04x slower                                         |
| unpickle_list            | 4.49 us                                                      | 4.68 us: 1.04x slower                                         |
| unpickle                 | 14.2 us                                                      | 15.0 us: 1.06x slower                                         |
| pickle_dict              | 30.0 us                                                      | 31.9 us: 1.06x slower                                         |
| pickle_list              | 4.11 us                                                      | 4.41 us: 1.07x slower                                         |
| python_startup_no_site   | 7.32 ms                                                      | 8.50 ms: 1.16x slower                                         |
| regex_effbot             | 2.99 ms                                                      | 3.63 ms: 1.21x slower                                         |
| dask                     | 463 ms                                                       | 564 ms: 1.22x slower                                          |
| coverage                 | 64.0 ms                                                      | 89.8 ms: 1.40x slower                                         |
| Geometric mean           | (ref)                                                        | 1.30x faster                                                  |

Benchmark hidden because not significant (2): bench_mp_pool, python_startup
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
