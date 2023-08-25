
# Results vs. 3.11.0

- fork: python
- ref: 7aa89e505d893cd5e6f3
- machine: linux-x86_64
- commit hash: 7aa89e5
- commit date: 2023-07-16
- overall geometric mean: 1.04x faster
- HPT reliability: 64.17%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-pythonperf2-x86_64-python-7aa89e505d893cd5e6f3-3.13.0a0-7aa89e5 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 2.86 sec                                                     | 2.91 sec: 1.02x slower                                                      |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-pythonperf2-x86_64-python-7aa89e505d893cd5e6f3-3.13.0a0-7aa89e5 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 251 ms                                                       | 259 ms: 1.03x slower                                                        |
| float          | 74.2 ms                                                      | 80.3 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-pythonperf2-x86_64-python-7aa89e505d893cd5e6f3-3.13.0a0-7aa89e5 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 150 ms: 1.05x faster                                                        |
| regex_effbot   | 3.50 ms                                                      | 3.44 ms: 1.02x faster                                                       |
| regex_v8       | 23.9 ms                                                      | 24.1 ms: 1.01x slower                                                       |
| regex_dna      | 227 ms                                                       | 238 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-pythonperf2-x86_64-python-7aa89e505d893cd5e6f3-3.13.0a0-7aa89e5 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.3 ms: 1.30x faster                                                       |
| json_loads           | 28.7 us                                                      | 24.7 us: 1.16x faster                                                       |
| unpickle_pure_python | 241 us                                                       | 221 us: 1.09x faster                                                        |
| xml_etree_parse      | 158 ms                                                       | 146 ms: 1.08x faster                                                        |
| pickle_pure_python   | 319 us                                                       | 314 us: 1.01x faster                                                        |
| xml_etree_iterparse  | 104 ms                                                       | 106 ms: 1.01x slower                                                        |
| tomli_loads          | 2.26 sec                                                     | 2.33 sec: 1.03x slower                                                      |
| xml_etree_process    | 56.5 ms                                                      | 59.6 ms: 1.06x slower                                                       |
| pickle_dict          | 30.8 us                                                      | 32.6 us: 1.06x slower                                                       |
| pickle               | 9.64 us                                                      | 10.2 us: 1.06x slower                                                       |
| unpickle             | 13.4 us                                                      | 14.3 us: 1.07x slower                                                       |
| xml_etree_generate   | 80.5 ms                                                      | 86.7 ms: 1.08x slower                                                       |
| unpickle_list        | 4.53 us                                                      | 4.89 us: 1.08x slower                                                       |
| pickle_list          | 3.83 us                                                      | 4.35 us: 1.14x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-pythonperf2-x86_64-python-7aa89e505d893cd5e6f3-3.13.0a0-7aa89e5 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.3 ms: 1.06x slower                                                       |
| python_startup_no_site | 7.76 ms                                                      | 8.40 ms: 1.08x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-pythonperf2-x86_64-python-7aa89e505d893cd5e6f3-3.13.0a0-7aa89e5 |
|-----------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 11.0 ms                                                      | 10.4 ms: 1.06x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-pythonperf2-x86_64-python-7aa89e505d893cd5e6f3-3.13.0a0-7aa89e5 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 155 us: 3.38x faster                                                        |
| asyncio_tcp              | 753 ms                                                       | 380 ms: 1.98x faster                                                        |
| asyncio_tcp_ssl          | 3.08 sec                                                     | 1.58 sec: 1.96x faster                                                      |
| generators               | 56.0 ms                                                      | 36.7 ms: 1.53x faster                                                       |
| json_dumps               | 13.4 ms                                                      | 10.3 ms: 1.30x faster                                                       |
| chaos                    | 80.9 ms                                                      | 63.3 ms: 1.28x faster                                                       |
| mypy2                    | 451 ms                                                       | 372 ms: 1.21x faster                                                        |
| coroutines               | 27.6 ms                                                      | 23.2 ms: 1.19x faster                                                       |
| json_loads               | 28.7 us                                                      | 24.7 us: 1.16x faster                                                       |
| scimark_lu               | 115 ms                                                       | 99.8 ms: 1.15x faster                                                       |
| crypto_pyaes             | 83.4 ms                                                      | 73.9 ms: 1.13x faster                                                       |
| nqueens                  | 103 ms                                                       | 91.3 ms: 1.13x faster                                                       |
| async_tree_memoization   | 630 ms                                                       | 564 ms: 1.12x faster                                                        |
| json                     | 5.65 ms                                                      | 5.06 ms: 1.12x faster                                                       |
| raytrace                 | 317 ms                                                       | 284 ms: 1.11x faster                                                        |
| async_tree_none          | 519 ms                                                       | 470 ms: 1.11x faster                                                        |
| hexiom                   | 7.13 ms                                                      | 6.47 ms: 1.10x faster                                                       |
| comprehensions           | 24.6 us                                                      | 22.4 us: 1.10x faster                                                       |
| unpickle_pure_python     | 241 us                                                       | 221 us: 1.09x faster                                                        |
| async_tree_io            | 1.17 sec                                                     | 1.08 sec: 1.09x faster                                                      |
| mdp                      | 2.75 sec                                                     | 2.54 sec: 1.08x faster                                                      |
| fannkuch                 | 429 ms                                                       | 398 ms: 1.08x faster                                                        |
| xml_etree_parse          | 158 ms                                                       | 146 ms: 1.08x faster                                                        |
| deltablue                | 4.00 ms                                                      | 3.72 ms: 1.07x faster                                                       |
| sqlglot_parse            | 1.53 ms                                                      | 1.43 ms: 1.07x faster                                                       |
| sqlglot_normalize        | 126 ms                                                       | 118 ms: 1.07x faster                                                        |
| logging_format           | 8.11 us                                                      | 7.59 us: 1.07x faster                                                       |
| deepcopy                 | 399 us                                                       | 374 us: 1.07x faster                                                        |
| mako                     | 11.0 ms                                                      | 10.4 ms: 1.06x faster                                                       |
| bench_thread_pool        | 1.01 ms                                                      | 962 us: 1.05x faster                                                        |
| regex_compile            | 158 ms                                                       | 150 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed  | 749 ms                                                       | 713 ms: 1.05x faster                                                        |
| sqlglot_transpile        | 1.92 ms                                                      | 1.83 ms: 1.05x faster                                                       |
| logging_simple           | 7.19 us                                                      | 6.94 us: 1.04x faster                                                       |
| deepcopy_memo            | 38.8 us                                                      | 37.4 us: 1.04x faster                                                       |
| deepcopy_reduce          | 3.51 us                                                      | 3.40 us: 1.03x faster                                                       |
| gc_traversal             | 3.85 ms                                                      | 3.76 ms: 1.02x faster                                                       |
| logging_silent           | 101 ns                                                       | 98.5 ns: 1.02x faster                                                       |
| regex_effbot             | 3.50 ms                                                      | 3.44 ms: 1.02x faster                                                       |
| dulwich_log              | 68.4 ms                                                      | 67.4 ms: 1.02x faster                                                       |
| pickle_pure_python       | 319 us                                                       | 314 us: 1.01x faster                                                        |
| sqlglot_optimize         | 59.8 ms                                                      | 59.2 ms: 1.01x faster                                                       |
| meteor_contest           | 131 ms                                                       | 130 ms: 1.00x faster                                                        |
| regex_v8                 | 23.9 ms                                                      | 24.1 ms: 1.01x slower                                                       |
| spectral_norm            | 93.3 ms                                                      | 94.2 ms: 1.01x slower                                                       |
| xml_etree_iterparse      | 104 ms                                                       | 106 ms: 1.01x slower                                                        |
| pycparser                | 1.32 sec                                                     | 1.34 sec: 1.02x slower                                                      |
| create_gc_cycles         | 1.61 ms                                                      | 1.63 ms: 1.02x slower                                                       |
| docutils                 | 2.86 sec                                                     | 2.91 sec: 1.02x slower                                                      |
| pprint_pformat           | 1.63 sec                                                     | 1.66 sec: 1.02x slower                                                      |
| pidigits                 | 251 ms                                                       | 259 ms: 1.03x slower                                                        |
| tomli_loads              | 2.26 sec                                                     | 2.33 sec: 1.03x slower                                                      |
| pathlib                  | 19.1 ms                                                      | 19.7 ms: 1.03x slower                                                       |
| pprint_safe_repr         | 784 ms                                                       | 812 ms: 1.04x slower                                                        |
| scimark_monte_carlo      | 68.2 ms                                                      | 70.9 ms: 1.04x slower                                                       |
| regex_dna                | 227 ms                                                       | 238 ms: 1.05x slower                                                        |
| python_startup           | 10.8 ms                                                      | 11.3 ms: 1.06x slower                                                       |
| xml_etree_process        | 56.5 ms                                                      | 59.6 ms: 1.06x slower                                                       |
| pickle_dict              | 30.8 us                                                      | 32.6 us: 1.06x slower                                                       |
| pickle                   | 9.64 us                                                      | 10.2 us: 1.06x slower                                                       |
| go                       | 164 ms                                                       | 173 ms: 1.06x slower                                                        |
| unpickle                 | 13.4 us                                                      | 14.3 us: 1.07x slower                                                       |
| xml_etree_generate       | 80.5 ms                                                      | 86.7 ms: 1.08x slower                                                       |
| unpickle_list            | 4.53 us                                                      | 4.89 us: 1.08x slower                                                       |
| coverage                 | 84.8 ms                                                      | 91.7 ms: 1.08x slower                                                       |
| float                    | 74.2 ms                                                      | 80.3 ms: 1.08x slower                                                       |
| python_startup_no_site   | 7.76 ms                                                      | 8.40 ms: 1.08x slower                                                       |
| sqlite_synth             | 2.50 us                                                      | 2.72 us: 1.09x slower                                                       |
| scimark_sparse_mat_mult  | 4.05 ms                                                      | 4.41 ms: 1.09x slower                                                       |
| scimark_fft              | 285 ms                                                       | 312 ms: 1.10x slower                                                        |
| telco                    | 6.86 ms                                                      | 7.60 ms: 1.11x slower                                                       |
| richards                 | 48.3 ms                                                      | 54.6 ms: 1.13x slower                                                       |
| pickle_list              | 3.83 us                                                      | 4.35 us: 1.14x slower                                                       |
| bench_mp_pool            | 4.62 ms                                                      | 5.31 ms: 1.15x slower                                                       |
| pyflate                  | 449 ms                                                       | 516 ms: 1.15x slower                                                        |
| unpack_sequence          | 45.6 ns                                                      | 52.8 ns: 1.16x slower                                                       |
| async_generators         | 316 ms                                                       | 393 ms: 1.25x slower                                                        |
| scimark_sor              | 111 ms                                                       | 146 ms: 1.32x slower                                                        |
| dask                     | 410 ms                                                       | 587 ms: 1.43x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (3): richards_super, nbody, tornado_http
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 64.17% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
