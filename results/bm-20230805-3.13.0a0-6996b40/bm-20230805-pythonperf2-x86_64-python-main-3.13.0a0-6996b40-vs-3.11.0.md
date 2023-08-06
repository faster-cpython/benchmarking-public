
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 6996b40
- commit date: 2023-08-05
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-pythonperf2-x86_64-python-main-3.13.0a0-6996b40 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| docutils       | 2.86 sec                                                     | 2.92 sec: 1.02x slower                                      |
| Geometric mean | (ref)                                                        | 1.01x slower                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-pythonperf2-x86_64-python-main-3.13.0a0-6996b40 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| pidigits       | 251 ms                                                       | 259 ms: 1.03x slower                                        |
| float          | 74.2 ms                                                      | 81.3 ms: 1.10x slower                                       |
| Geometric mean | (ref)                                                        | 1.05x slower                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-pythonperf2-x86_64-python-main-3.13.0a0-6996b40 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 150 ms: 1.05x faster                                        |
| regex_effbot   | 3.50 ms                                                      | 3.41 ms: 1.03x faster                                       |
| regex_dna      | 227 ms                                                       | 236 ms: 1.04x slower                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-pythonperf2-x86_64-python-main-3.13.0a0-6996b40 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.4 ms: 1.29x faster                                       |
| json_loads           | 28.7 us                                                      | 25.4 us: 1.13x faster                                       |
| unpickle_pure_python | 241 us                                                       | 221 us: 1.09x faster                                        |
| xml_etree_parse      | 158 ms                                                       | 148 ms: 1.07x faster                                        |
| xml_etree_iterparse  | 104 ms                                                       | 105 ms: 1.01x slower                                        |
| pickle_pure_python   | 319 us                                                       | 323 us: 1.01x slower                                        |
| unpickle_list        | 4.53 us                                                      | 4.64 us: 1.02x slower                                       |
| tomli_loads          | 2.26 sec                                                     | 2.32 sec: 1.03x slower                                      |
| pickle_dict          | 30.8 us                                                      | 31.7 us: 1.03x slower                                       |
| xml_etree_process    | 56.5 ms                                                      | 59.4 ms: 1.05x slower                                       |
| xml_etree_generate   | 80.5 ms                                                      | 86.7 ms: 1.08x slower                                       |
| pickle               | 9.64 us                                                      | 10.4 us: 1.08x slower                                       |
| unpickle             | 13.4 us                                                      | 14.6 us: 1.08x slower                                       |
| pickle_list          | 3.83 us                                                      | 4.38 us: 1.14x slower                                       |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-pythonperf2-x86_64-python-main-3.13.0a0-6996b40 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.6 ms: 1.08x slower                                       |
| python_startup_no_site | 7.76 ms                                                      | 8.64 ms: 1.11x slower                                       |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-pythonperf2-x86_64-python-main-3.13.0a0-6996b40 |
|-----------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| mako      | 11.0 ms                                                      | 10.2 ms: 1.08x faster                                       |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-pythonperf2-x86_64-python-main-3.13.0a0-6996b40 |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 153 us: 3.41x faster                                        |
| asyncio_tcp              | 753 ms                                                       | 371 ms: 2.03x faster                                        |
| asyncio_tcp_ssl          | 3.08 sec                                                     | 1.58 sec: 1.95x faster                                      |
| generators               | 56.0 ms                                                      | 37.1 ms: 1.51x faster                                       |
| chaos                    | 80.9 ms                                                      | 62.5 ms: 1.29x faster                                       |
| json_dumps               | 13.4 ms                                                      | 10.4 ms: 1.29x faster                                       |
| mypy2                    | 451 ms                                                       | 372 ms: 1.21x faster                                        |
| coroutines               | 27.6 ms                                                      | 23.2 ms: 1.19x faster                                       |
| crypto_pyaes             | 83.4 ms                                                      | 72.5 ms: 1.15x faster                                       |
| scimark_lu               | 115 ms                                                       | 100 ms: 1.14x faster                                        |
| nqueens                  | 103 ms                                                       | 91.2 ms: 1.13x faster                                       |
| json_loads               | 28.7 us                                                      | 25.4 us: 1.13x faster                                       |
| raytrace                 | 317 ms                                                       | 281 ms: 1.13x faster                                        |
| comprehensions           | 24.6 us                                                      | 21.9 us: 1.12x faster                                       |
| async_tree_memoization   | 630 ms                                                       | 564 ms: 1.12x faster                                        |
| async_tree_none          | 519 ms                                                       | 469 ms: 1.11x faster                                        |
| fannkuch                 | 429 ms                                                       | 390 ms: 1.10x faster                                        |
| deltablue                | 4.00 ms                                                      | 3.63 ms: 1.10x faster                                       |
| hexiom                   | 7.13 ms                                                      | 6.50 ms: 1.10x faster                                       |
| logging_format           | 8.11 us                                                      | 7.46 us: 1.09x faster                                       |
| unpickle_pure_python     | 241 us                                                       | 221 us: 1.09x faster                                        |
| async_tree_io            | 1.17 sec                                                     | 1.08 sec: 1.09x faster                                      |
| json                     | 5.65 ms                                                      | 5.25 ms: 1.08x faster                                       |
| mako                     | 11.0 ms                                                      | 10.2 ms: 1.08x faster                                       |
| mdp                      | 2.75 sec                                                     | 2.55 sec: 1.07x faster                                      |
| sqlglot_normalize        | 126 ms                                                       | 117 ms: 1.07x faster                                        |
| xml_etree_parse          | 158 ms                                                       | 148 ms: 1.07x faster                                        |
| sqlglot_parse            | 1.53 ms                                                      | 1.44 ms: 1.07x faster                                       |
| logging_simple           | 7.19 us                                                      | 6.82 us: 1.05x faster                                       |
| regex_compile            | 158 ms                                                       | 150 ms: 1.05x faster                                        |
| bench_thread_pool        | 1.01 ms                                                      | 965 us: 1.05x faster                                        |
| async_tree_cpu_io_mixed  | 749 ms                                                       | 716 ms: 1.05x faster                                        |
| sqlglot_transpile        | 1.92 ms                                                      | 1.84 ms: 1.04x faster                                       |
| gc_traversal             | 3.85 ms                                                      | 3.73 ms: 1.03x faster                                       |
| deepcopy                 | 399 us                                                       | 388 us: 1.03x faster                                        |
| logging_silent           | 101 ns                                                       | 98.1 ns: 1.03x faster                                       |
| regex_effbot             | 3.50 ms                                                      | 3.41 ms: 1.03x faster                                       |
| deepcopy_memo            | 38.8 us                                                      | 37.9 us: 1.02x faster                                       |
| sqlglot_optimize         | 59.8 ms                                                      | 59.2 ms: 1.01x faster                                       |
| meteor_contest           | 131 ms                                                       | 130 ms: 1.01x faster                                        |
| richards_super           | 61.0 ms                                                      | 60.5 ms: 1.01x faster                                       |
| spectral_norm            | 93.3 ms                                                      | 93.9 ms: 1.01x slower                                       |
| xml_etree_iterparse      | 104 ms                                                       | 105 ms: 1.01x slower                                        |
| scimark_monte_carlo      | 68.2 ms                                                      | 69.0 ms: 1.01x slower                                       |
| pickle_pure_python       | 319 us                                                       | 323 us: 1.01x slower                                        |
| pycparser                | 1.32 sec                                                     | 1.34 sec: 1.02x slower                                      |
| docutils                 | 2.86 sec                                                     | 2.92 sec: 1.02x slower                                      |
| unpickle_list            | 4.53 us                                                      | 4.64 us: 1.02x slower                                       |
| tomli_loads              | 2.26 sec                                                     | 2.32 sec: 1.03x slower                                      |
| pathlib                  | 19.1 ms                                                      | 19.6 ms: 1.03x slower                                       |
| create_gc_cycles         | 1.61 ms                                                      | 1.65 ms: 1.03x slower                                       |
| pickle_dict              | 30.8 us                                                      | 31.7 us: 1.03x slower                                       |
| pidigits                 | 251 ms                                                       | 259 ms: 1.03x slower                                        |
| pprint_pformat           | 1.63 sec                                                     | 1.68 sec: 1.03x slower                                      |
| regex_dna                | 227 ms                                                       | 236 ms: 1.04x slower                                        |
| go                       | 164 ms                                                       | 171 ms: 1.04x slower                                        |
| pprint_safe_repr         | 784 ms                                                       | 821 ms: 1.05x slower                                        |
| xml_etree_process        | 56.5 ms                                                      | 59.4 ms: 1.05x slower                                       |
| xml_etree_generate       | 80.5 ms                                                      | 86.7 ms: 1.08x slower                                       |
| pickle                   | 9.64 us                                                      | 10.4 us: 1.08x slower                                       |
| python_startup           | 10.8 ms                                                      | 11.6 ms: 1.08x slower                                       |
| scimark_sparse_mat_mult  | 4.05 ms                                                      | 4.38 ms: 1.08x slower                                       |
| coverage                 | 84.8 ms                                                      | 91.9 ms: 1.08x slower                                       |
| unpickle                 | 13.4 us                                                      | 14.6 us: 1.08x slower                                       |
| sqlite_synth             | 2.50 us                                                      | 2.74 us: 1.10x slower                                       |
| float                    | 74.2 ms                                                      | 81.3 ms: 1.10x slower                                       |
| scimark_fft              | 285 ms                                                       | 316 ms: 1.11x slower                                        |
| python_startup_no_site   | 7.76 ms                                                      | 8.64 ms: 1.11x slower                                       |
| richards                 | 48.3 ms                                                      | 53.9 ms: 1.11x slower                                       |
| unpack_sequence          | 45.6 ns                                                      | 51.4 ns: 1.13x slower                                       |
| pickle_list              | 3.83 us                                                      | 4.38 us: 1.14x slower                                       |
| pyflate                  | 449 ms                                                       | 519 ms: 1.16x slower                                        |
| telco                    | 6.86 ms                                                      | 8.10 ms: 1.18x slower                                       |
| async_generators         | 316 ms                                                       | 395 ms: 1.25x slower                                        |
| scimark_sor              | 111 ms                                                       | 146 ms: 1.31x slower                                        |
| dask                     | 410 ms                                                       | 591 ms: 1.44x slower                                        |
| Geometric mean           | (ref)                                                        | 1.04x faster                                                |

Benchmark hidden because not significant (6): tornado_http, deepcopy_reduce, dulwich_log, regex_v8, bench_mp_pool, nbody
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
