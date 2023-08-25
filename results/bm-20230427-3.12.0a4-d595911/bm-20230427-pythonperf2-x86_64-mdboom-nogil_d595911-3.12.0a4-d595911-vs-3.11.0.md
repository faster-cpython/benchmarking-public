
# Results vs. 3.11.0

- fork: mdboom
- ref: nogil_d595911
- machine: linux-x86_64
- commit hash: d595911
- commit date: 2023-04-27
- overall geometric mean: 1.02x slower
- HPT reliability: 99.90%
- HPT 99th percentile: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230427-pythonperf2-x86_64-mdboom-nogil_d595911-3.12.0a4-d595911 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 303 ms: 1.05x slower                                                 |
| chameleon      | 7.67 ms                                                      | 8.37 ms: 1.09x slower                                                |
| docutils       | 2.86 sec                                                     | 2.99 sec: 1.05x slower                                               |
| Geometric mean | (ref)                                                        | 1.05x slower                                                         |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230427-pythonperf2-x86_64-mdboom-nogil_d595911-3.12.0a4-d595911 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 74.2 ms                                                      | 65.5 ms: 1.13x faster                                                |
| pidigits       | 251 ms                                                       | 246 ms: 1.02x faster                                                 |
| nbody          | 90.7 ms                                                      | 102 ms: 1.12x slower                                                 |
| Geometric mean | (ref)                                                        | 1.01x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230427-pythonperf2-x86_64-mdboom-nogil_d595911-3.12.0a4-d595911 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.50 ms                                                      | 3.30 ms: 1.06x faster                                                |
| regex_v8       | 23.9 ms                                                      | 23.1 ms: 1.04x faster                                                |
| regex_compile  | 158 ms                                                       | 157 ms: 1.01x faster                                                 |
| regex_dna      | 227 ms                                                       | 233 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                        | 1.02x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230427-pythonperf2-x86_64-mdboom-nogil_d595911-3.12.0a4-d595911 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 11.4 ms: 1.17x faster                                                |
| xml_etree_parse      | 158 ms                                                       | 137 ms: 1.15x faster                                                 |
| unpickle_pure_python | 241 us                                                       | 233 us: 1.03x faster                                                 |
| pickle_pure_python   | 319 us                                                       | 329 us: 1.03x slower                                                 |
| xml_etree_generate   | 80.5 ms                                                      | 85.4 ms: 1.06x slower                                                |
| pickle_dict          | 30.8 us                                                      | 32.7 us: 1.06x slower                                                |
| tomli_loads          | 2.26 sec                                                     | 2.49 sec: 1.10x slower                                               |
| unpickle_list        | 4.53 us                                                      | 5.01 us: 1.10x slower                                                |
| xml_etree_process    | 56.5 ms                                                      | 62.8 ms: 1.11x slower                                                |
| json_loads           | 28.7 us                                                      | 32.3 us: 1.13x slower                                                |
| pickle_list          | 3.83 us                                                      | 4.46 us: 1.16x slower                                                |
| unpickle             | 13.4 us                                                      | 15.8 us: 1.17x slower                                                |
| xml_etree_iterparse  | 104 ms                                                       | 126 ms: 1.21x slower                                                 |
| Geometric mean       | (ref)                                                        | 1.05x slower                                                         |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230427-pythonperf2-x86_64-mdboom-nogil_d595911-3.12.0a4-d595911 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.5 ms: 1.07x slower                                                |
| python_startup_no_site | 7.76 ms                                                      | 8.45 ms: 1.09x slower                                                |
| Geometric mean         | (ref)                                                        | 1.08x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230427-pythonperf2-x86_64-mdboom-nogil_d595911-3.12.0a4-d595911 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_xml     | 58.5 ms                                                      | 54.6 ms: 1.07x faster                                                |
| genshi_text    | 26.1 ms                                                      | 27.0 ms: 1.03x slower                                                |
| mako           | 11.0 ms                                                      | 14.9 ms: 1.36x slower                                                |
| Geometric mean | (ref)                                                        | 1.07x slower                                                         |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230427-pythonperf2-x86_64-mdboom-nogil_d595911-3.12.0a4-d595911 |
|--------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io            | 1.17 sec                                                     | 595 ms: 1.97x faster                                                 |
| asyncio_tcp              | 753 ms                                                       | 399 ms: 1.88x faster                                                 |
| asyncio_tcp_ssl          | 3.08 sec                                                     | 1.70 sec: 1.81x faster                                               |
| async_tree_memoization   | 630 ms                                                       | 361 ms: 1.74x faster                                                 |
| async_tree_none          | 519 ms                                                       | 304 ms: 1.71x faster                                                 |
| async_tree_cpu_io_mixed  | 749 ms                                                       | 529 ms: 1.42x faster                                                 |
| gc_traversal             | 3.85 ms                                                      | 3.08 ms: 1.25x faster                                                |
| json_dumps               | 13.4 ms                                                      | 11.4 ms: 1.17x faster                                                |
| xml_etree_parse          | 158 ms                                                       | 137 ms: 1.15x faster                                                 |
| float                    | 74.2 ms                                                      | 65.5 ms: 1.13x faster                                                |
| pycparser                | 1.32 sec                                                     | 1.22 sec: 1.08x faster                                               |
| genshi_xml               | 58.5 ms                                                      | 54.6 ms: 1.07x faster                                                |
| regex_effbot             | 3.50 ms                                                      | 3.30 ms: 1.06x faster                                                |
| scimark_lu               | 115 ms                                                       | 108 ms: 1.06x faster                                                 |
| chaos                    | 80.9 ms                                                      | 77.8 ms: 1.04x faster                                                |
| regex_v8                 | 23.9 ms                                                      | 23.1 ms: 1.04x faster                                                |
| unpickle_pure_python     | 241 us                                                       | 233 us: 1.03x faster                                                 |
| nqueens                  | 103 ms                                                       | 99.8 ms: 1.03x faster                                                |
| sqlglot_normalize        | 126 ms                                                       | 123 ms: 1.02x faster                                                 |
| pidigits                 | 251 ms                                                       | 246 ms: 1.02x faster                                                 |
| logging_silent           | 101 ns                                                       | 99.0 ns: 1.02x faster                                                |
| hexiom                   | 7.13 ms                                                      | 7.01 ms: 1.02x faster                                                |
| dulwich_log              | 68.4 ms                                                      | 67.2 ms: 1.02x faster                                                |
| regex_compile            | 158 ms                                                       | 157 ms: 1.01x faster                                                 |
| deepcopy                 | 399 us                                                       | 403 us: 1.01x slower                                                 |
| sympy_expand             | 555 ms                                                       | 562 ms: 1.01x slower                                                 |
| logging_simple           | 7.19 us                                                      | 7.32 us: 1.02x slower                                                |
| coroutines               | 27.6 ms                                                      | 28.1 ms: 1.02x slower                                                |
| sympy_str                | 337 ms                                                       | 344 ms: 1.02x slower                                                 |
| regex_dna                | 227 ms                                                       | 233 ms: 1.02x slower                                                 |
| sympy_integrate          | 25.8 ms                                                      | 26.4 ms: 1.03x slower                                                |
| mdp                      | 2.75 sec                                                     | 2.82 sec: 1.03x slower                                               |
| go                       | 164 ms                                                       | 169 ms: 1.03x slower                                                 |
| pickle_pure_python       | 319 us                                                       | 329 us: 1.03x slower                                                 |
| genshi_text              | 26.1 ms                                                      | 27.0 ms: 1.03x slower                                                |
| thrift                   | 925 us                                                       | 957 us: 1.03x slower                                                 |
| sympy_sum                | 185 ms                                                       | 191 ms: 1.04x slower                                                 |
| pathlib                  | 19.1 ms                                                      | 19.8 ms: 1.04x slower                                                |
| fannkuch                 | 429 ms                                                       | 447 ms: 1.04x slower                                                 |
| docutils                 | 2.86 sec                                                     | 2.99 sec: 1.05x slower                                               |
| scimark_sor              | 111 ms                                                       | 117 ms: 1.05x slower                                                 |
| 2to3                     | 288 ms                                                       | 303 ms: 1.05x slower                                                 |
| deepcopy_memo            | 38.8 us                                                      | 41.0 us: 1.06x slower                                                |
| xml_etree_generate       | 80.5 ms                                                      | 85.4 ms: 1.06x slower                                                |
| telco                    | 6.86 ms                                                      | 7.29 ms: 1.06x slower                                                |
| async_generators         | 316 ms                                                       | 335 ms: 1.06x slower                                                 |
| pickle_dict              | 30.8 us                                                      | 32.7 us: 1.06x slower                                                |
| crypto_pyaes             | 83.4 ms                                                      | 88.9 ms: 1.07x slower                                                |
| deepcopy_reduce          | 3.51 us                                                      | 3.74 us: 1.07x slower                                                |
| python_startup           | 10.8 ms                                                      | 11.5 ms: 1.07x slower                                                |
| pyflate                  | 449 ms                                                       | 482 ms: 1.07x slower                                                 |
| sqlglot_transpile        | 1.92 ms                                                      | 2.08 ms: 1.08x slower                                                |
| python_startup_no_site   | 7.76 ms                                                      | 8.45 ms: 1.09x slower                                                |
| richards_super           | 61.0 ms                                                      | 66.5 ms: 1.09x slower                                                |
| chameleon                | 7.67 ms                                                      | 8.37 ms: 1.09x slower                                                |
| typing_runtime_protocols | 523 us                                                       | 575 us: 1.10x slower                                                 |
| tomli_loads              | 2.26 sec                                                     | 2.49 sec: 1.10x slower                                               |
| unpickle_list            | 4.53 us                                                      | 5.01 us: 1.10x slower                                                |
| pprint_pformat           | 1.63 sec                                                     | 1.81 sec: 1.11x slower                                               |
| richards                 | 48.3 ms                                                      | 53.5 ms: 1.11x slower                                                |
| pprint_safe_repr         | 784 ms                                                       | 871 ms: 1.11x slower                                                 |
| xml_etree_process        | 56.5 ms                                                      | 62.8 ms: 1.11x slower                                                |
| json                     | 5.65 ms                                                      | 6.28 ms: 1.11x slower                                                |
| generators               | 56.0 ms                                                      | 62.3 ms: 1.11x slower                                                |
| nbody                    | 90.7 ms                                                      | 102 ms: 1.12x slower                                                 |
| spectral_norm            | 93.3 ms                                                      | 105 ms: 1.12x slower                                                 |
| json_loads               | 28.7 us                                                      | 32.3 us: 1.13x slower                                                |
| sqlglot_parse            | 1.53 ms                                                      | 1.73 ms: 1.13x slower                                                |
| scimark_sparse_mat_mult  | 4.05 ms                                                      | 4.58 ms: 1.13x slower                                                |
| scimark_fft              | 285 ms                                                       | 327 ms: 1.15x slower                                                 |
| unpack_sequence          | 45.6 ns                                                      | 52.4 ns: 1.15x slower                                                |
| coverage                 | 84.8 ms                                                      | 97.6 ms: 1.15x slower                                                |
| sqlite_synth             | 2.50 us                                                      | 2.88 us: 1.15x slower                                                |
| pickle_list              | 3.83 us                                                      | 4.46 us: 1.16x slower                                                |
| meteor_contest           | 131 ms                                                       | 153 ms: 1.17x slower                                                 |
| unpickle                 | 13.4 us                                                      | 15.8 us: 1.17x slower                                                |
| raytrace                 | 317 ms                                                       | 376 ms: 1.19x slower                                                 |
| create_gc_cycles         | 1.61 ms                                                      | 1.93 ms: 1.20x slower                                                |
| comprehensions           | 24.6 us                                                      | 29.6 us: 1.20x slower                                                |
| xml_etree_iterparse      | 104 ms                                                       | 126 ms: 1.21x slower                                                 |
| scimark_monte_carlo      | 68.2 ms                                                      | 82.9 ms: 1.22x slower                                                |
| mako                     | 11.0 ms                                                      | 14.9 ms: 1.36x slower                                                |
| bench_mp_pool            | 4.62 ms                                                      | 7.77 ms: 1.68x slower                                                |
| bench_thread_pool        | 1.01 ms                                                      | 2.03 ms: 2.00x slower                                                |
| Geometric mean           | (ref)                                                        | 1.02x slower                                                         |

Benchmark hidden because not significant (7): mypy2, deltablue, pickle, sqlglot_optimize, html5lib, logging_format, django_template
Ignored benchmarks (8) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, dask, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http


# HPT report

- Reliability score: 99.90% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x
