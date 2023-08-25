
# Results vs. 3.11.0

- fork: python
- ref: 2ba7c7f7b151ff56cf12
- machine: linux-x86_64
- commit hash: 2ba7c7f
- commit date: 2023-08-04
- overall geometric mean: 1.04x faster
- HPT reliability: 72.22%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230804-pythonperf2-x86_64-python-2ba7c7f7b151ff56cf12-3.13.0a0-2ba7c7f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 2.86 sec                                                     | 2.92 sec: 1.02x slower                                                      |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230804-pythonperf2-x86_64-python-2ba7c7f7b151ff56cf12-3.13.0a0-2ba7c7f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 89.2 ms: 1.02x faster                                                       |
| pidigits       | 251 ms                                                       | 260 ms: 1.04x slower                                                        |
| float          | 74.2 ms                                                      | 80.7 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230804-pythonperf2-x86_64-python-2ba7c7f7b151ff56cf12-3.13.0a0-2ba7c7f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 149 ms: 1.06x faster                                                        |
| regex_v8       | 23.9 ms                                                      | 23.6 ms: 1.01x faster                                                       |
| regex_dna      | 227 ms                                                       | 242 ms: 1.07x slower                                                        |
| regex_effbot   | 3.50 ms                                                      | 3.77 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230804-pythonperf2-x86_64-python-2ba7c7f7b151ff56cf12-3.13.0a0-2ba7c7f |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.4 ms: 1.29x faster                                                       |
| json_loads           | 28.7 us                                                      | 24.5 us: 1.17x faster                                                       |
| xml_etree_parse      | 158 ms                                                       | 152 ms: 1.04x faster                                                        |
| unpickle_pure_python | 241 us                                                       | 233 us: 1.03x faster                                                        |
| pickle_pure_python   | 319 us                                                       | 323 us: 1.01x slower                                                        |
| tomli_loads          | 2.26 sec                                                     | 2.29 sec: 1.01x slower                                                      |
| xml_etree_iterparse  | 104 ms                                                       | 107 ms: 1.03x slower                                                        |
| unpickle_list        | 4.53 us                                                      | 4.69 us: 1.03x slower                                                       |
| xml_etree_process    | 56.5 ms                                                      | 59.1 ms: 1.05x slower                                                       |
| pickle               | 9.64 us                                                      | 10.1 us: 1.05x slower                                                       |
| pickle_dict          | 30.8 us                                                      | 32.6 us: 1.06x slower                                                       |
| xml_etree_generate   | 80.5 ms                                                      | 86.5 ms: 1.07x slower                                                       |
| unpickle             | 13.4 us                                                      | 14.7 us: 1.09x slower                                                       |
| pickle_list          | 3.83 us                                                      | 4.54 us: 1.19x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230804-pythonperf2-x86_64-python-2ba7c7f7b151ff56cf12-3.13.0a0-2ba7c7f |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.6 ms: 1.08x slower                                                       |
| python_startup_no_site | 7.76 ms                                                      | 8.63 ms: 1.11x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230804-pythonperf2-x86_64-python-2ba7c7f7b151ff56cf12-3.13.0a0-2ba7c7f |
|-----------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 11.0 ms                                                      | 10.3 ms: 1.07x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230804-pythonperf2-x86_64-python-2ba7c7f7b151ff56cf12-3.13.0a0-2ba7c7f |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 152 us: 3.45x faster                                                        |
| asyncio_tcp              | 753 ms                                                       | 373 ms: 2.02x faster                                                        |
| asyncio_tcp_ssl          | 3.08 sec                                                     | 1.58 sec: 1.95x faster                                                      |
| generators               | 56.0 ms                                                      | 36.7 ms: 1.53x faster                                                       |
| chaos                    | 80.9 ms                                                      | 62.5 ms: 1.29x faster                                                       |
| json_dumps               | 13.4 ms                                                      | 10.4 ms: 1.29x faster                                                       |
| mypy2                    | 451 ms                                                       | 372 ms: 1.21x faster                                                        |
| coroutines               | 27.6 ms                                                      | 23.3 ms: 1.18x faster                                                       |
| json_loads               | 28.7 us                                                      | 24.5 us: 1.17x faster                                                       |
| scimark_lu               | 115 ms                                                       | 97.9 ms: 1.17x faster                                                       |
| raytrace                 | 317 ms                                                       | 275 ms: 1.15x faster                                                        |
| crypto_pyaes             | 83.4 ms                                                      | 73.6 ms: 1.13x faster                                                       |
| nqueens                  | 103 ms                                                       | 91.2 ms: 1.13x faster                                                       |
| comprehensions           | 24.6 us                                                      | 22.2 us: 1.11x faster                                                       |
| async_tree_memoization   | 630 ms                                                       | 569 ms: 1.11x faster                                                        |
| json                     | 5.65 ms                                                      | 5.12 ms: 1.10x faster                                                       |
| hexiom                   | 7.13 ms                                                      | 6.48 ms: 1.10x faster                                                       |
| async_tree_none          | 519 ms                                                       | 474 ms: 1.10x faster                                                        |
| logging_format           | 8.11 us                                                      | 7.45 us: 1.09x faster                                                       |
| gc_traversal             | 3.85 ms                                                      | 3.54 ms: 1.09x faster                                                       |
| fannkuch                 | 429 ms                                                       | 395 ms: 1.09x faster                                                        |
| deltablue                | 4.00 ms                                                      | 3.70 ms: 1.08x faster                                                       |
| async_tree_io            | 1.17 sec                                                     | 1.09 sec: 1.08x faster                                                      |
| mako                     | 11.0 ms                                                      | 10.3 ms: 1.07x faster                                                       |
| mdp                      | 2.75 sec                                                     | 2.58 sec: 1.07x faster                                                      |
| sqlglot_parse            | 1.53 ms                                                      | 1.44 ms: 1.06x faster                                                       |
| sqlglot_normalize        | 126 ms                                                       | 118 ms: 1.06x faster                                                        |
| regex_compile            | 158 ms                                                       | 149 ms: 1.06x faster                                                        |
| logging_simple           | 7.19 us                                                      | 6.87 us: 1.05x faster                                                       |
| bench_thread_pool        | 1.01 ms                                                      | 966 us: 1.05x faster                                                        |
| sqlglot_transpile        | 1.92 ms                                                      | 1.84 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed  | 749 ms                                                       | 719 ms: 1.04x faster                                                        |
| xml_etree_parse          | 158 ms                                                       | 152 ms: 1.04x faster                                                        |
| unpickle_pure_python     | 241 us                                                       | 233 us: 1.03x faster                                                        |
| deepcopy                 | 399 us                                                       | 387 us: 1.03x faster                                                        |
| deepcopy_memo            | 38.8 us                                                      | 37.9 us: 1.02x faster                                                       |
| deepcopy_reduce          | 3.51 us                                                      | 3.45 us: 1.02x faster                                                       |
| nbody                    | 90.7 ms                                                      | 89.2 ms: 1.02x faster                                                       |
| sqlglot_optimize         | 59.8 ms                                                      | 59.0 ms: 1.01x faster                                                       |
| regex_v8                 | 23.9 ms                                                      | 23.6 ms: 1.01x faster                                                       |
| meteor_contest           | 131 ms                                                       | 131 ms: 1.00x slower                                                        |
| dulwich_log              | 68.4 ms                                                      | 69.1 ms: 1.01x slower                                                       |
| richards_super           | 61.0 ms                                                      | 61.7 ms: 1.01x slower                                                       |
| pickle_pure_python       | 319 us                                                       | 323 us: 1.01x slower                                                        |
| tomli_loads              | 2.26 sec                                                     | 2.29 sec: 1.01x slower                                                      |
| pathlib                  | 19.1 ms                                                      | 19.4 ms: 1.02x slower                                                       |
| docutils                 | 2.86 sec                                                     | 2.92 sec: 1.02x slower                                                      |
| xml_etree_iterparse      | 104 ms                                                       | 107 ms: 1.03x slower                                                        |
| unpickle_list            | 4.53 us                                                      | 4.69 us: 1.03x slower                                                       |
| pprint_pformat           | 1.63 sec                                                     | 1.69 sec: 1.03x slower                                                      |
| pidigits                 | 251 ms                                                       | 260 ms: 1.04x slower                                                        |
| create_gc_cycles         | 1.61 ms                                                      | 1.67 ms: 1.04x slower                                                       |
| scimark_sparse_mat_mult  | 4.05 ms                                                      | 4.21 ms: 1.04x slower                                                       |
| coverage                 | 84.8 ms                                                      | 88.4 ms: 1.04x slower                                                       |
| spectral_norm            | 93.3 ms                                                      | 97.6 ms: 1.05x slower                                                       |
| xml_etree_process        | 56.5 ms                                                      | 59.1 ms: 1.05x slower                                                       |
| pickle                   | 9.64 us                                                      | 10.1 us: 1.05x slower                                                       |
| pprint_safe_repr         | 784 ms                                                       | 824 ms: 1.05x slower                                                        |
| pickle_dict              | 30.8 us                                                      | 32.6 us: 1.06x slower                                                       |
| regex_dna                | 227 ms                                                       | 242 ms: 1.07x slower                                                        |
| scimark_fft              | 285 ms                                                       | 304 ms: 1.07x slower                                                        |
| xml_etree_generate       | 80.5 ms                                                      | 86.5 ms: 1.07x slower                                                       |
| regex_effbot             | 3.50 ms                                                      | 3.77 ms: 1.08x slower                                                       |
| go                       | 164 ms                                                       | 176 ms: 1.08x slower                                                        |
| python_startup           | 10.8 ms                                                      | 11.6 ms: 1.08x slower                                                       |
| unpack_sequence          | 45.6 ns                                                      | 49.6 ns: 1.09x slower                                                       |
| float                    | 74.2 ms                                                      | 80.7 ms: 1.09x slower                                                       |
| unpickle                 | 13.4 us                                                      | 14.7 us: 1.09x slower                                                       |
| sqlite_synth             | 2.50 us                                                      | 2.76 us: 1.10x slower                                                       |
| python_startup_no_site   | 7.76 ms                                                      | 8.63 ms: 1.11x slower                                                       |
| richards                 | 48.3 ms                                                      | 55.2 ms: 1.14x slower                                                       |
| pyflate                  | 449 ms                                                       | 515 ms: 1.15x slower                                                        |
| telco                    | 6.86 ms                                                      | 8.00 ms: 1.17x slower                                                       |
| pickle_list              | 3.83 us                                                      | 4.54 us: 1.19x slower                                                       |
| async_generators         | 316 ms                                                       | 396 ms: 1.25x slower                                                        |
| scimark_sor              | 111 ms                                                       | 144 ms: 1.30x slower                                                        |
| dask                     | 410 ms                                                       | 588 ms: 1.43x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (5): tornado_http, scimark_monte_carlo, logging_silent, pycparser, bench_mp_pool
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 72.22% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
