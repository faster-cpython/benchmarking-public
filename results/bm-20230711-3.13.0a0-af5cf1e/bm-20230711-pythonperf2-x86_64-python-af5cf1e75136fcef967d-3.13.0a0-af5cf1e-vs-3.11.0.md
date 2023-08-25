
# Results vs. 3.11.0

- fork: python
- ref: af5cf1e75136fcef967d
- machine: linux-x86_64
- commit hash: af5cf1e
- commit date: 2023-07-11
- overall geometric mean: 1.04x faster
- HPT reliability: 66.39%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230711-pythonperf2-x86_64-python-af5cf1e75136fcef967d-3.13.0a0-af5cf1e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 2.86 sec                                                     | 2.92 sec: 1.02x slower                                                      |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230711-pythonperf2-x86_64-python-af5cf1e75136fcef967d-3.13.0a0-af5cf1e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 88.8 ms: 1.02x faster                                                       |
| pidigits       | 251 ms                                                       | 259 ms: 1.03x slower                                                        |
| float          | 74.2 ms                                                      | 84.3 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230711-pythonperf2-x86_64-python-af5cf1e75136fcef967d-3.13.0a0-af5cf1e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 151 ms: 1.05x faster                                                        |
| regex_v8       | 23.9 ms                                                      | 24.1 ms: 1.01x slower                                                       |
| regex_effbot   | 3.50 ms                                                      | 3.57 ms: 1.02x slower                                                       |
| regex_dna      | 227 ms                                                       | 246 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230711-pythonperf2-x86_64-python-af5cf1e75136fcef967d-3.13.0a0-af5cf1e |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.1 ms: 1.32x faster                                                       |
| json_loads           | 28.7 us                                                      | 24.8 us: 1.16x faster                                                       |
| unpickle_pure_python | 241 us                                                       | 220 us: 1.09x faster                                                        |
| xml_etree_parse      | 158 ms                                                       | 147 ms: 1.07x faster                                                        |
| pickle_pure_python   | 319 us                                                       | 312 us: 1.02x faster                                                        |
| xml_etree_iterparse  | 104 ms                                                       | 106 ms: 1.02x slower                                                        |
| unpickle_list        | 4.53 us                                                      | 4.67 us: 1.03x slower                                                       |
| pickle               | 9.64 us                                                      | 9.96 us: 1.03x slower                                                       |
| pickle_dict          | 30.8 us                                                      | 32.1 us: 1.04x slower                                                       |
| tomli_loads          | 2.26 sec                                                     | 2.36 sec: 1.05x slower                                                      |
| xml_etree_process    | 56.5 ms                                                      | 59.6 ms: 1.05x slower                                                       |
| xml_etree_generate   | 80.5 ms                                                      | 85.6 ms: 1.06x slower                                                       |
| unpickle             | 13.4 us                                                      | 14.6 us: 1.09x slower                                                       |
| pickle_list          | 3.83 us                                                      | 4.42 us: 1.15x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230711-pythonperf2-x86_64-python-af5cf1e75136fcef967d-3.13.0a0-af5cf1e |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.4 ms: 1.06x slower                                                       |
| python_startup_no_site | 7.76 ms                                                      | 8.41 ms: 1.08x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230711-pythonperf2-x86_64-python-af5cf1e75136fcef967d-3.13.0a0-af5cf1e |
|-----------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 11.0 ms                                                      | 10.5 ms: 1.04x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230711-pythonperf2-x86_64-python-af5cf1e75136fcef967d-3.13.0a0-af5cf1e |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 151 us: 3.46x faster                                                        |
| asyncio_tcp_ssl          | 3.08 sec                                                     | 1.58 sec: 1.95x faster                                                      |
| asyncio_tcp              | 753 ms                                                       | 386 ms: 1.95x faster                                                        |
| generators               | 56.0 ms                                                      | 36.7 ms: 1.53x faster                                                       |
| json_dumps               | 13.4 ms                                                      | 10.1 ms: 1.32x faster                                                       |
| chaos                    | 80.9 ms                                                      | 62.2 ms: 1.30x faster                                                       |
| mypy2                    | 451 ms                                                       | 372 ms: 1.21x faster                                                        |
| coroutines               | 27.6 ms                                                      | 23.2 ms: 1.19x faster                                                       |
| json_loads               | 28.7 us                                                      | 24.8 us: 1.16x faster                                                       |
| scimark_lu               | 115 ms                                                       | 99.2 ms: 1.15x faster                                                       |
| raytrace                 | 317 ms                                                       | 277 ms: 1.14x faster                                                        |
| crypto_pyaes             | 83.4 ms                                                      | 73.7 ms: 1.13x faster                                                       |
| comprehensions           | 24.6 us                                                      | 22.0 us: 1.12x faster                                                       |
| nqueens                  | 103 ms                                                       | 92.1 ms: 1.12x faster                                                       |
| json                     | 5.65 ms                                                      | 5.12 ms: 1.10x faster                                                       |
| hexiom                   | 7.13 ms                                                      | 6.47 ms: 1.10x faster                                                       |
| async_tree_memoization   | 630 ms                                                       | 573 ms: 1.10x faster                                                        |
| async_tree_none          | 519 ms                                                       | 474 ms: 1.10x faster                                                        |
| unpickle_pure_python     | 241 us                                                       | 220 us: 1.09x faster                                                        |
| sqlglot_normalize        | 126 ms                                                       | 116 ms: 1.09x faster                                                        |
| mdp                      | 2.75 sec                                                     | 2.54 sec: 1.08x faster                                                      |
| xml_etree_parse          | 158 ms                                                       | 147 ms: 1.07x faster                                                        |
| async_tree_io            | 1.17 sec                                                     | 1.10 sec: 1.07x faster                                                      |
| sqlglot_parse            | 1.53 ms                                                      | 1.44 ms: 1.07x faster                                                       |
| fannkuch                 | 429 ms                                                       | 402 ms: 1.07x faster                                                        |
| deltablue                | 4.00 ms                                                      | 3.75 ms: 1.07x faster                                                       |
| deepcopy                 | 399 us                                                       | 376 us: 1.06x faster                                                        |
| logging_format           | 8.11 us                                                      | 7.65 us: 1.06x faster                                                       |
| bench_thread_pool        | 1.01 ms                                                      | 962 us: 1.05x faster                                                        |
| regex_compile            | 158 ms                                                       | 151 ms: 1.05x faster                                                        |
| mako                     | 11.0 ms                                                      | 10.5 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed  | 749 ms                                                       | 720 ms: 1.04x faster                                                        |
| sqlglot_transpile        | 1.92 ms                                                      | 1.85 ms: 1.03x faster                                                       |
| deepcopy_memo            | 38.8 us                                                      | 37.6 us: 1.03x faster                                                       |
| logging_silent           | 101 ns                                                       | 97.7 ns: 1.03x faster                                                       |
| logging_simple           | 7.19 us                                                      | 6.99 us: 1.03x faster                                                       |
| deepcopy_reduce          | 3.51 us                                                      | 3.42 us: 1.03x faster                                                       |
| nbody                    | 90.7 ms                                                      | 88.8 ms: 1.02x faster                                                       |
| pickle_pure_python       | 319 us                                                       | 312 us: 1.02x faster                                                        |
| sqlglot_optimize         | 59.8 ms                                                      | 58.7 ms: 1.02x faster                                                       |
| richards_super           | 61.0 ms                                                      | 60.3 ms: 1.01x faster                                                       |
| dulwich_log              | 68.4 ms                                                      | 67.6 ms: 1.01x faster                                                       |
| meteor_contest           | 131 ms                                                       | 130 ms: 1.00x faster                                                        |
| regex_v8                 | 23.9 ms                                                      | 24.1 ms: 1.01x slower                                                       |
| pycparser                | 1.32 sec                                                     | 1.34 sec: 1.01x slower                                                      |
| regex_effbot             | 3.50 ms                                                      | 3.57 ms: 1.02x slower                                                       |
| xml_etree_iterparse      | 104 ms                                                       | 106 ms: 1.02x slower                                                        |
| docutils                 | 2.86 sec                                                     | 2.92 sec: 1.02x slower                                                      |
| pathlib                  | 19.1 ms                                                      | 19.5 ms: 1.02x slower                                                       |
| unpickle_list            | 4.53 us                                                      | 4.67 us: 1.03x slower                                                       |
| pidigits                 | 251 ms                                                       | 259 ms: 1.03x slower                                                        |
| pickle                   | 9.64 us                                                      | 9.96 us: 1.03x slower                                                       |
| create_gc_cycles         | 1.61 ms                                                      | 1.67 ms: 1.04x slower                                                       |
| pprint_pformat           | 1.63 sec                                                     | 1.69 sec: 1.04x slower                                                      |
| pickle_dict              | 30.8 us                                                      | 32.1 us: 1.04x slower                                                       |
| tomli_loads              | 2.26 sec                                                     | 2.36 sec: 1.05x slower                                                      |
| gc_traversal             | 3.85 ms                                                      | 4.02 ms: 1.05x slower                                                       |
| unpack_sequence          | 45.6 ns                                                      | 47.9 ns: 1.05x slower                                                       |
| xml_etree_process        | 56.5 ms                                                      | 59.6 ms: 1.05x slower                                                       |
| spectral_norm            | 93.3 ms                                                      | 98.6 ms: 1.06x slower                                                       |
| pprint_safe_repr         | 784 ms                                                       | 828 ms: 1.06x slower                                                        |
| python_startup           | 10.8 ms                                                      | 11.4 ms: 1.06x slower                                                       |
| scimark_sparse_mat_mult  | 4.05 ms                                                      | 4.29 ms: 1.06x slower                                                       |
| xml_etree_generate       | 80.5 ms                                                      | 85.6 ms: 1.06x slower                                                       |
| go                       | 164 ms                                                       | 176 ms: 1.07x slower                                                        |
| regex_dna                | 227 ms                                                       | 246 ms: 1.08x slower                                                        |
| python_startup_no_site   | 7.76 ms                                                      | 8.41 ms: 1.08x slower                                                       |
| coverage                 | 84.8 ms                                                      | 91.9 ms: 1.08x slower                                                       |
| unpickle                 | 13.4 us                                                      | 14.6 us: 1.09x slower                                                       |
| scimark_monte_carlo      | 68.2 ms                                                      | 74.1 ms: 1.09x slower                                                       |
| scimark_fft              | 285 ms                                                       | 312 ms: 1.09x slower                                                        |
| sqlite_synth             | 2.50 us                                                      | 2.77 us: 1.11x slower                                                       |
| telco                    | 6.86 ms                                                      | 7.70 ms: 1.12x slower                                                       |
| float                    | 74.2 ms                                                      | 84.3 ms: 1.14x slower                                                       |
| richards                 | 48.3 ms                                                      | 54.9 ms: 1.14x slower                                                       |
| pyflate                  | 449 ms                                                       | 516 ms: 1.15x slower                                                        |
| pickle_list              | 3.83 us                                                      | 4.42 us: 1.15x slower                                                       |
| async_generators         | 316 ms                                                       | 398 ms: 1.26x slower                                                        |
| scimark_sor              | 111 ms                                                       | 147 ms: 1.32x slower                                                        |
| dask                     | 410 ms                                                       | 589 ms: 1.44x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (2): bench_mp_pool, tornado_http
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 66.39% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
