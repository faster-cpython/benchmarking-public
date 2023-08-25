
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 18b1fde
- commit date: 2023-07-01
- overall geometric mean: 1.26x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-pythonperf2-x86_64-python-main-3.13.0a0-18b1fde |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| docutils       | 3.40 sec                                                     | 2.93 sec: 1.16x faster                                      |
| tornado_http   | 152 ms                                                       | 122 ms: 1.24x faster                                        |
| Geometric mean | (ref)                                                        | 1.20x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-pythonperf2-x86_64-python-main-3.13.0a0-18b1fde |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| nbody          | 137 ms                                                       | 89.7 ms: 1.53x faster                                       |
| float          | 110 ms                                                       | 80.8 ms: 1.37x faster                                       |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                        |
| Geometric mean | (ref)                                                        | 1.30x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-pythonperf2-x86_64-python-main-3.13.0a0-18b1fde |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 152 ms: 1.27x faster                                        |
| regex_v8       | 26.6 ms                                                      | 22.9 ms: 1.16x faster                                       |
| regex_dna      | 259 ms                                                       | 245 ms: 1.06x faster                                        |
| regex_effbot   | 2.99 ms                                                      | 3.57 ms: 1.19x slower                                       |
| Geometric mean | (ref)                                                        | 1.07x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-pythonperf2-x86_64-python-main-3.13.0a0-18b1fde |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 224 us: 1.43x faster                                        |
| pickle_pure_python   | 457 us                                                       | 321 us: 1.42x faster                                        |
| json_dumps           | 14.2 ms                                                      | 10.3 ms: 1.38x faster                                       |
| xml_etree_process    | 76.0 ms                                                      | 60.6 ms: 1.25x faster                                       |
| tomli_loads          | 2.97 sec                                                     | 2.42 sec: 1.23x faster                                      |
| json_loads           | 30.0 us                                                      | 25.6 us: 1.17x faster                                       |
| xml_etree_parse      | 162 ms                                                       | 148 ms: 1.09x faster                                        |
| xml_etree_generate   | 94.6 ms                                                      | 88.4 ms: 1.07x faster                                       |
| xml_etree_iterparse  | 110 ms                                                       | 106 ms: 1.04x faster                                        |
| pickle               | 9.94 us                                                      | 10.1 us: 1.02x slower                                       |
| unpickle             | 14.2 us                                                      | 14.6 us: 1.03x slower                                       |
| unpickle_list        | 4.49 us                                                      | 4.71 us: 1.05x slower                                       |
| pickle_list          | 4.11 us                                                      | 4.31 us: 1.05x slower                                       |
| pickle_dict          | 30.0 us                                                      | 33.2 us: 1.11x slower                                       |
| Geometric mean       | (ref)                                                        | 1.12x faster                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-pythonperf2-x86_64-python-main-3.13.0a0-18b1fde |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.3 ms: 1.02x faster                                       |
| python_startup_no_site | 7.32 ms                                                      | 8.38 ms: 1.14x slower                                       |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-pythonperf2-x86_64-python-main-3.13.0a0-18b1fde |
|-----------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 10.2 ms: 1.44x faster                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-pythonperf2-x86_64-python-main-3.13.0a0-18b1fde |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 157 us: 3.34x faster                                        |
| deltablue                | 7.47 ms                                                      | 3.55 ms: 2.11x faster                                       |
| asyncio_tcp              | 782 ms                                                       | 385 ms: 2.03x faster                                        |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.57 sec: 1.97x faster                                      |
| raytrace                 | 488 ms                                                       | 274 ms: 1.78x faster                                        |
| chaos                    | 107 ms                                                       | 61.8 ms: 1.73x faster                                       |
| logging_silent           | 166 ns                                                       | 98.3 ns: 1.69x faster                                       |
| scimark_lu               | 164 ms                                                       | 100 ms: 1.63x faster                                        |
| generators               | 58.0 ms                                                      | 37.5 ms: 1.55x faster                                       |
| richards_super           | 90.8 ms                                                      | 59.3 ms: 1.53x faster                                       |
| nbody                    | 137 ms                                                       | 89.7 ms: 1.53x faster                                       |
| sqlglot_parse            | 2.26 ms                                                      | 1.49 ms: 1.52x faster                                       |
| go                       | 259 ms                                                       | 171 ms: 1.51x faster                                        |
| async_tree_none          | 700 ms                                                       | 470 ms: 1.49x faster                                        |
| async_tree_io            | 1.61 sec                                                     | 1.08 sec: 1.49x faster                                      |
| scimark_monte_carlo      | 109 ms                                                       | 75.1 ms: 1.46x faster                                       |
| async_tree_memoization   | 824 ms                                                       | 566 ms: 1.46x faster                                        |
| hexiom                   | 9.52 ms                                                      | 6.56 ms: 1.45x faster                                       |
| crypto_pyaes             | 118 ms                                                       | 81.7 ms: 1.45x faster                                       |
| mako                     | 14.7 ms                                                      | 10.2 ms: 1.44x faster                                       |
| unpickle_pure_python     | 321 us                                                       | 224 us: 1.43x faster                                        |
| sqlglot_transpile        | 2.71 ms                                                      | 1.89 ms: 1.43x faster                                       |
| pickle_pure_python       | 457 us                                                       | 321 us: 1.42x faster                                        |
| richards                 | 74.1 ms                                                      | 52.7 ms: 1.40x faster                                       |
| spectral_norm            | 136 ms                                                       | 97.5 ms: 1.40x faster                                       |
| json_dumps               | 14.2 ms                                                      | 10.3 ms: 1.38x faster                                       |
| float                    | 110 ms                                                       | 80.8 ms: 1.37x faster                                       |
| pyflate                  | 697 ms                                                       | 511 ms: 1.36x faster                                        |
| bench_mp_pool            | 7.18 ms                                                      | 5.33 ms: 1.35x faster                                       |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 715 ms: 1.33x faster                                        |
| coroutines               | 30.4 ms                                                      | 23.2 ms: 1.31x faster                                       |
| logging_simple           | 8.90 us                                                      | 6.89 us: 1.29x faster                                       |
| deepcopy_memo            | 48.9 us                                                      | 38.3 us: 1.28x faster                                       |
| regex_compile            | 194 ms                                                       | 152 ms: 1.27x faster                                        |
| logging_format           | 9.57 us                                                      | 7.51 us: 1.27x faster                                       |
| pycparser                | 1.66 sec                                                     | 1.31 sec: 1.27x faster                                      |
| pprint_pformat           | 2.15 sec                                                     | 1.70 sec: 1.27x faster                                      |
| pprint_safe_repr         | 1.05 sec                                                     | 829 ms: 1.27x faster                                        |
| xml_etree_process        | 76.0 ms                                                      | 60.6 ms: 1.25x faster                                       |
| mypy2                    | 466 ms                                                       | 375 ms: 1.24x faster                                        |
| tornado_http             | 152 ms                                                       | 122 ms: 1.24x faster                                        |
| tomli_loads              | 2.97 sec                                                     | 2.42 sec: 1.23x faster                                      |
| nqueens                  | 112 ms                                                       | 92.0 ms: 1.22x faster                                       |
| fannkuch                 | 496 ms                                                       | 407 ms: 1.22x faster                                        |
| scimark_sor              | 177 ms                                                       | 146 ms: 1.21x faster                                        |
| comprehensions           | 26.9 us                                                      | 22.4 us: 1.20x faster                                       |
| sqlglot_normalize        | 144 ms                                                       | 120 ms: 1.20x faster                                        |
| bench_thread_pool        | 1.14 ms                                                      | 952 us: 1.19x faster                                        |
| mdp                      | 3.03 sec                                                     | 2.54 sec: 1.19x faster                                      |
| dulwich_log              | 80.1 ms                                                      | 67.8 ms: 1.18x faster                                       |
| sqlglot_optimize         | 70.3 ms                                                      | 59.7 ms: 1.18x faster                                       |
| json_loads               | 30.0 us                                                      | 25.6 us: 1.17x faster                                       |
| deepcopy_reduce          | 4.03 us                                                      | 3.44 us: 1.17x faster                                       |
| deepcopy                 | 454 us                                                       | 388 us: 1.17x faster                                        |
| regex_v8                 | 26.6 ms                                                      | 22.9 ms: 1.16x faster                                       |
| docutils                 | 3.40 sec                                                     | 2.93 sec: 1.16x faster                                      |
| json                     | 5.96 ms                                                      | 5.23 ms: 1.14x faster                                       |
| unpack_sequence          | 59.5 ns                                                      | 53.2 ns: 1.12x faster                                       |
| scimark_fft              | 359 ms                                                       | 323 ms: 1.11x faster                                        |
| pathlib                  | 21.7 ms                                                      | 19.5 ms: 1.11x faster                                       |
| create_gc_cycles         | 1.82 ms                                                      | 1.65 ms: 1.10x faster                                       |
| xml_etree_parse          | 162 ms                                                       | 148 ms: 1.09x faster                                        |
| sqlite_synth             | 2.97 us                                                      | 2.74 us: 1.08x faster                                       |
| xml_etree_generate       | 94.6 ms                                                      | 88.4 ms: 1.07x faster                                       |
| async_generators         | 422 ms                                                       | 397 ms: 1.06x faster                                        |
| regex_dna                | 259 ms                                                       | 245 ms: 1.06x faster                                        |
| meteor_contest           | 137 ms                                                       | 130 ms: 1.05x faster                                        |
| pidigits                 | 271 ms                                                       | 260 ms: 1.04x faster                                        |
| xml_etree_iterparse      | 110 ms                                                       | 106 ms: 1.04x faster                                        |
| python_startup           | 11.5 ms                                                      | 11.3 ms: 1.02x faster                                       |
| pickle                   | 9.94 us                                                      | 10.1 us: 1.02x slower                                       |
| unpickle                 | 14.2 us                                                      | 14.6 us: 1.03x slower                                       |
| unpickle_list            | 4.49 us                                                      | 4.71 us: 1.05x slower                                       |
| pickle_list              | 4.11 us                                                      | 4.31 us: 1.05x slower                                       |
| telco                    | 7.14 ms                                                      | 7.80 ms: 1.09x slower                                       |
| pickle_dict              | 30.0 us                                                      | 33.2 us: 1.11x slower                                       |
| python_startup_no_site   | 7.32 ms                                                      | 8.38 ms: 1.14x slower                                       |
| gc_traversal             | 3.45 ms                                                      | 4.09 ms: 1.18x slower                                       |
| regex_effbot             | 2.99 ms                                                      | 3.57 ms: 1.19x slower                                       |
| coverage                 | 64.0 ms                                                      | 88.1 ms: 1.38x slower                                       |
| Geometric mean           | (ref)                                                        | 1.26x faster                                                |

Benchmark hidden because not significant (1): scimark_sparse_mat_mult
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, dask, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.20x
