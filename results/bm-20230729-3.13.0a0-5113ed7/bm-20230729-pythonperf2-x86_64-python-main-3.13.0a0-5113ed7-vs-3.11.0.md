
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 5113ed7
- commit date: 2023-07-29
- overall geometric mean: 1.04x faster
- HPT reliability: 80.32%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-pythonperf2-x86_64-python-main-3.13.0a0-5113ed7 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| docutils       | 2.86 sec                                                     | 2.90 sec: 1.01x slower                                      |
| tornado_http   | 122 ms                                                       | 120 ms: 1.01x faster                                        |
| Geometric mean | (ref)                                                        | 1.00x slower                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-pythonperf2-x86_64-python-main-3.13.0a0-5113ed7 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 88.4 ms: 1.03x faster                                       |
| pidigits       | 251 ms                                                       | 259 ms: 1.03x slower                                        |
| float          | 74.2 ms                                                      | 81.1 ms: 1.09x slower                                       |
| Geometric mean | (ref)                                                        | 1.03x slower                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-pythonperf2-x86_64-python-main-3.13.0a0-5113ed7 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 150 ms: 1.05x faster                                        |
| regex_effbot   | 3.50 ms                                                      | 3.48 ms: 1.01x faster                                       |
| regex_v8       | 23.9 ms                                                      | 24.2 ms: 1.01x slower                                       |
| regex_dna      | 227 ms                                                       | 245 ms: 1.08x slower                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-pythonperf2-x86_64-python-main-3.13.0a0-5113ed7 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.2 ms: 1.31x faster                                       |
| json_loads           | 28.7 us                                                      | 24.8 us: 1.16x faster                                       |
| xml_etree_parse      | 158 ms                                                       | 147 ms: 1.07x faster                                        |
| unpickle_pure_python | 241 us                                                       | 239 us: 1.01x faster                                        |
| xml_etree_iterparse  | 104 ms                                                       | 106 ms: 1.01x slower                                        |
| tomli_loads          | 2.26 sec                                                     | 2.32 sec: 1.03x slower                                      |
| pickle_dict          | 30.8 us                                                      | 31.7 us: 1.03x slower                                       |
| xml_etree_process    | 56.5 ms                                                      | 58.8 ms: 1.04x slower                                       |
| pickle               | 9.64 us                                                      | 10.1 us: 1.05x slower                                       |
| unpickle_list        | 4.53 us                                                      | 4.82 us: 1.06x slower                                       |
| xml_etree_generate   | 80.5 ms                                                      | 85.8 ms: 1.07x slower                                       |
| unpickle             | 13.4 us                                                      | 14.5 us: 1.08x slower                                       |
| pickle_list          | 3.83 us                                                      | 4.43 us: 1.16x slower                                       |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-pythonperf2-x86_64-python-main-3.13.0a0-5113ed7 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.6 ms: 1.08x slower                                       |
| python_startup_no_site | 7.76 ms                                                      | 8.63 ms: 1.11x slower                                       |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-pythonperf2-x86_64-python-main-3.13.0a0-5113ed7 |
|-----------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| mako      | 11.0 ms                                                      | 10.3 ms: 1.07x faster                                       |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-pythonperf2-x86_64-python-main-3.13.0a0-5113ed7 |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 153 us: 3.41x faster                                        |
| asyncio_tcp              | 753 ms                                                       | 368 ms: 2.05x faster                                        |
| asyncio_tcp_ssl          | 3.08 sec                                                     | 1.58 sec: 1.95x faster                                      |
| generators               | 56.0 ms                                                      | 36.7 ms: 1.53x faster                                       |
| json_dumps               | 13.4 ms                                                      | 10.2 ms: 1.31x faster                                       |
| chaos                    | 80.9 ms                                                      | 62.3 ms: 1.30x faster                                       |
| mypy2                    | 451 ms                                                       | 373 ms: 1.21x faster                                        |
| coroutines               | 27.6 ms                                                      | 23.4 ms: 1.18x faster                                       |
| scimark_lu               | 115 ms                                                       | 97.4 ms: 1.18x faster                                       |
| json_loads               | 28.7 us                                                      | 24.8 us: 1.16x faster                                       |
| crypto_pyaes             | 83.4 ms                                                      | 73.2 ms: 1.14x faster                                       |
| raytrace                 | 317 ms                                                       | 283 ms: 1.12x faster                                        |
| nqueens                  | 103 ms                                                       | 92.1 ms: 1.12x faster                                       |
| comprehensions           | 24.6 us                                                      | 22.1 us: 1.11x faster                                       |
| gc_traversal             | 3.85 ms                                                      | 3.48 ms: 1.10x faster                                       |
| async_tree_memoization   | 630 ms                                                       | 571 ms: 1.10x faster                                        |
| async_tree_none          | 519 ms                                                       | 473 ms: 1.10x faster                                        |
| hexiom                   | 7.13 ms                                                      | 6.51 ms: 1.10x faster                                       |
| sqlglot_normalize        | 126 ms                                                       | 116 ms: 1.09x faster                                        |
| json                     | 5.65 ms                                                      | 5.19 ms: 1.09x faster                                       |
| logging_format           | 8.11 us                                                      | 7.50 us: 1.08x faster                                       |
| mdp                      | 2.75 sec                                                     | 2.54 sec: 1.08x faster                                      |
| async_tree_io            | 1.17 sec                                                     | 1.09 sec: 1.08x faster                                      |
| xml_etree_parse          | 158 ms                                                       | 147 ms: 1.07x faster                                        |
| deltablue                | 4.00 ms                                                      | 3.73 ms: 1.07x faster                                       |
| mako                     | 11.0 ms                                                      | 10.3 ms: 1.07x faster                                       |
| bench_thread_pool        | 1.01 ms                                                      | 950 us: 1.06x faster                                        |
| fannkuch                 | 429 ms                                                       | 404 ms: 1.06x faster                                        |
| sqlglot_parse            | 1.53 ms                                                      | 1.44 ms: 1.06x faster                                       |
| deepcopy                 | 399 us                                                       | 377 us: 1.06x faster                                        |
| regex_compile            | 158 ms                                                       | 150 ms: 1.05x faster                                        |
| async_tree_cpu_io_mixed  | 749 ms                                                       | 718 ms: 1.04x faster                                        |
| logging_simple           | 7.19 us                                                      | 6.92 us: 1.04x faster                                       |
| sqlglot_transpile        | 1.92 ms                                                      | 1.85 ms: 1.04x faster                                       |
| logging_silent           | 101 ns                                                       | 97.3 ns: 1.04x faster                                       |
| deepcopy_reduce          | 3.51 us                                                      | 3.42 us: 1.03x faster                                       |
| nbody                    | 90.7 ms                                                      | 88.4 ms: 1.03x faster                                       |
| deepcopy_memo            | 38.8 us                                                      | 37.8 us: 1.03x faster                                       |
| sqlglot_optimize         | 59.8 ms                                                      | 58.8 ms: 1.02x faster                                       |
| tornado_http             | 122 ms                                                       | 120 ms: 1.01x faster                                        |
| unpickle_pure_python     | 241 us                                                       | 239 us: 1.01x faster                                        |
| regex_effbot             | 3.50 ms                                                      | 3.48 ms: 1.01x faster                                       |
| meteor_contest           | 131 ms                                                       | 131 ms: 1.00x slower                                        |
| pprint_pformat           | 1.63 sec                                                     | 1.65 sec: 1.01x slower                                      |
| pycparser                | 1.32 sec                                                     | 1.34 sec: 1.01x slower                                      |
| xml_etree_iterparse      | 104 ms                                                       | 106 ms: 1.01x slower                                        |
| regex_v8                 | 23.9 ms                                                      | 24.2 ms: 1.01x slower                                       |
| docutils                 | 2.86 sec                                                     | 2.90 sec: 1.01x slower                                      |
| richards_super           | 61.0 ms                                                      | 62.3 ms: 1.02x slower                                       |
| pprint_safe_repr         | 784 ms                                                       | 802 ms: 1.02x slower                                        |
| tomli_loads              | 2.26 sec                                                     | 2.32 sec: 1.03x slower                                      |
| unpack_sequence          | 45.6 ns                                                      | 47.0 ns: 1.03x slower                                       |
| pickle_dict              | 30.8 us                                                      | 31.7 us: 1.03x slower                                       |
| pidigits                 | 251 ms                                                       | 259 ms: 1.03x slower                                        |
| spectral_norm            | 93.3 ms                                                      | 97.1 ms: 1.04x slower                                       |
| xml_etree_process        | 56.5 ms                                                      | 58.8 ms: 1.04x slower                                       |
| pathlib                  | 19.1 ms                                                      | 19.9 ms: 1.04x slower                                       |
| pickle                   | 9.64 us                                                      | 10.1 us: 1.05x slower                                       |
| go                       | 164 ms                                                       | 173 ms: 1.06x slower                                        |
| scimark_sparse_mat_mult  | 4.05 ms                                                      | 4.30 ms: 1.06x slower                                       |
| unpickle_list            | 4.53 us                                                      | 4.82 us: 1.06x slower                                       |
| xml_etree_generate       | 80.5 ms                                                      | 85.8 ms: 1.07x slower                                       |
| scimark_fft              | 285 ms                                                       | 306 ms: 1.08x slower                                        |
| unpickle                 | 13.4 us                                                      | 14.5 us: 1.08x slower                                       |
| regex_dna                | 227 ms                                                       | 245 ms: 1.08x slower                                        |
| python_startup           | 10.8 ms                                                      | 11.6 ms: 1.08x slower                                       |
| sqlite_synth             | 2.50 us                                                      | 2.70 us: 1.08x slower                                       |
| coverage                 | 84.8 ms                                                      | 92.0 ms: 1.09x slower                                       |
| float                    | 74.2 ms                                                      | 81.1 ms: 1.09x slower                                       |
| python_startup_no_site   | 7.76 ms                                                      | 8.63 ms: 1.11x slower                                       |
| richards                 | 48.3 ms                                                      | 55.2 ms: 1.14x slower                                       |
| pyflate                  | 449 ms                                                       | 516 ms: 1.15x slower                                        |
| pickle_list              | 3.83 us                                                      | 4.43 us: 1.16x slower                                       |
| telco                    | 6.86 ms                                                      | 7.94 ms: 1.16x slower                                       |
| async_generators         | 316 ms                                                       | 393 ms: 1.25x slower                                        |
| scimark_sor              | 111 ms                                                       | 144 ms: 1.29x slower                                        |
| dask                     | 410 ms                                                       | 586 ms: 1.43x slower                                        |
| Geometric mean           | (ref)                                                        | 1.04x faster                                                |

Benchmark hidden because not significant (5): pickle_pure_python, scimark_monte_carlo, dulwich_log, bench_mp_pool, create_gc_cycles
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 80.32% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
