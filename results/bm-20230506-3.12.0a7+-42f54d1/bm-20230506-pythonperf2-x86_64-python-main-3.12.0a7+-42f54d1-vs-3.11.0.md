
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 42f54d1
- commit date: 2023-05-06
- overall geometric mean: 1.04x faster \*
- HPT reliability: 99.38%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230506-pythonperf2-x86_64-python-main-3.12.0a7+-42f54d1 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 284 ms: 1.01x faster                                         |
| docutils       | 2.86 sec                                                     | 2.90 sec: 1.01x slower                                       |
| tornado_http   | 122 ms                                                       | 116 ms: 1.05x faster                                         |
| Geometric mean | (ref)                                                        | 1.02x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230506-pythonperf2-x86_64-python-main-3.12.0a7+-42f54d1 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| pidigits       | 251 ms                                                       | 260 ms: 1.04x slower                                         |
| float          | 74.2 ms                                                      | 77.6 ms: 1.05x slower                                        |
| Geometric mean | (ref)                                                        | 1.03x slower                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230506-pythonperf2-x86_64-python-main-3.12.0a7+-42f54d1 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 146 ms: 1.08x faster                                         |
| regex_effbot   | 3.50 ms                                                      | 3.42 ms: 1.02x faster                                        |
| regex_v8       | 23.9 ms                                                      | 23.9 ms: 1.00x faster                                        |
| regex_dna      | 227 ms                                                       | 234 ms: 1.03x slower                                         |
| Geometric mean | (ref)                                                        | 1.02x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230506-pythonperf2-x86_64-python-main-3.12.0a7+-42f54d1 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.2 ms: 1.31x faster                                        |
| json_loads           | 28.7 us                                                      | 24.2 us: 1.19x faster                                        |
| unpickle_pure_python | 241 us                                                       | 206 us: 1.17x faster                                         |
| xml_etree_parse      | 158 ms                                                       | 146 ms: 1.08x faster                                         |
| pickle               | 9.64 us                                                      | 9.94 us: 1.03x slower                                        |
| pickle_dict          | 30.8 us                                                      | 31.8 us: 1.03x slower                                        |
| xml_etree_process    | 56.5 ms                                                      | 58.8 ms: 1.04x slower                                        |
| xml_etree_generate   | 80.5 ms                                                      | 85.2 ms: 1.06x slower                                        |
| unpickle_list        | 4.53 us                                                      | 4.81 us: 1.06x slower                                        |
| unpickle             | 13.4 us                                                      | 14.6 us: 1.08x slower                                        |
| pickle_list          | 3.83 us                                                      | 4.42 us: 1.15x slower                                        |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                 |

Benchmark hidden because not significant (2): pickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230506-pythonperf2-x86_64-python-main-3.12.0a7+-42f54d1 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.3 ms: 1.05x slower                                        |
| python_startup_no_site | 7.76 ms                                                      | 8.39 ms: 1.08x slower                                        |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230506-pythonperf2-x86_64-python-main-3.12.0a7+-42f54d1 |
|-----------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| mako      | 11.0 ms                                                      | 10.1 ms: 1.09x faster                                        |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230506-pythonperf2-x86_64-python-main-3.12.0a7+-42f54d1 |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| asyncio_tcp             | 753 ms                                                       | 383 ms: 1.97x faster                                         |
| generators              | 56.0 ms                                                      | 36.6 ms: 1.53x faster                                        |
| json_dumps              | 13.4 ms                                                      | 10.2 ms: 1.31x faster                                        |
| fannkuch                | 429 ms                                                       | 343 ms: 1.25x faster                                         |
| coroutines              | 27.6 ms                                                      | 22.3 ms: 1.23x faster                                        |
| deltablue               | 4.00 ms                                                      | 3.27 ms: 1.22x faster                                        |
| hexiom                  | 7.13 ms                                                      | 5.86 ms: 1.22x faster                                        |
| mypy2                   | 451 ms                                                       | 373 ms: 1.21x faster                                         |
| chaos                   | 80.9 ms                                                      | 67.4 ms: 1.20x faster                                        |
| json_loads              | 28.7 us                                                      | 24.2 us: 1.19x faster                                        |
| unpickle_pure_python    | 241 us                                                       | 206 us: 1.17x faster                                         |
| nqueens                 | 103 ms                                                       | 88.1 ms: 1.17x faster                                        |
| scimark_lu              | 115 ms                                                       | 100 ms: 1.14x faster                                         |
| go                      | 164 ms                                                       | 147 ms: 1.12x faster                                         |
| sqlglot_parse           | 1.53 ms                                                      | 1.38 ms: 1.11x faster                                        |
| logging_silent          | 101 ns                                                       | 91.5 ns: 1.10x faster                                        |
| mdp                     | 2.75 sec                                                     | 2.51 sec: 1.09x faster                                       |
| async_tree_memoization  | 630 ms                                                       | 578 ms: 1.09x faster                                         |
| mako                    | 11.0 ms                                                      | 10.1 ms: 1.09x faster                                        |
| json                    | 5.65 ms                                                      | 5.21 ms: 1.09x faster                                        |
| xml_etree_parse         | 158 ms                                                       | 146 ms: 1.08x faster                                         |
| async_tree_none         | 519 ms                                                       | 481 ms: 1.08x faster                                         |
| regex_compile           | 158 ms                                                       | 146 ms: 1.08x faster                                         |
| sqlglot_transpile       | 1.92 ms                                                      | 1.78 ms: 1.08x faster                                        |
| logging_format          | 8.11 us                                                      | 7.56 us: 1.07x faster                                        |
| richards                | 48.3 ms                                                      | 45.0 ms: 1.07x faster                                        |
| bench_thread_pool       | 1.01 ms                                                      | 944 us: 1.07x faster                                         |
| deepcopy_memo           | 38.8 us                                                      | 36.2 us: 1.07x faster                                        |
| async_tree_io           | 1.17 sec                                                     | 1.10 sec: 1.07x faster                                       |
| pycparser               | 1.32 sec                                                     | 1.24 sec: 1.07x faster                                       |
| deepcopy                | 399 us                                                       | 375 us: 1.06x faster                                         |
| tornado_http            | 122 ms                                                       | 116 ms: 1.05x faster                                         |
| dulwich_log             | 68.4 ms                                                      | 65.3 ms: 1.05x faster                                        |
| sqlglot_normalize       | 126 ms                                                       | 120 ms: 1.05x faster                                         |
| async_tree_cpu_io_mixed | 749 ms                                                       | 715 ms: 1.05x faster                                         |
| logging_simple          | 7.19 us                                                      | 6.87 us: 1.05x faster                                        |
| deepcopy_reduce         | 3.51 us                                                      | 3.37 us: 1.04x faster                                        |
| raytrace                | 317 ms                                                       | 307 ms: 1.03x faster                                         |
| regex_effbot            | 3.50 ms                                                      | 3.42 ms: 1.02x faster                                        |
| pyflate                 | 449 ms                                                       | 438 ms: 1.02x faster                                         |
| sqlglot_optimize        | 59.8 ms                                                      | 58.8 ms: 1.02x faster                                        |
| crypto_pyaes            | 83.4 ms                                                      | 82.1 ms: 1.02x faster                                        |
| meteor_contest          | 131 ms                                                       | 129 ms: 1.01x faster                                         |
| 2to3                    | 288 ms                                                       | 284 ms: 1.01x faster                                         |
| spectral_norm           | 93.3 ms                                                      | 92.6 ms: 1.01x faster                                        |
| comprehensions          | 24.6 us                                                      | 24.4 us: 1.01x faster                                        |
| pprint_pformat          | 1.63 sec                                                     | 1.62 sec: 1.00x faster                                       |
| regex_v8                | 23.9 ms                                                      | 23.9 ms: 1.00x faster                                        |
| scimark_sor             | 111 ms                                                       | 112 ms: 1.01x slower                                         |
| docutils                | 2.86 sec                                                     | 2.90 sec: 1.01x slower                                       |
| pprint_safe_repr        | 784 ms                                                       | 798 ms: 1.02x slower                                         |
| pickle                  | 9.64 us                                                      | 9.94 us: 1.03x slower                                        |
| regex_dna               | 227 ms                                                       | 234 ms: 1.03x slower                                         |
| pickle_dict             | 30.8 us                                                      | 31.8 us: 1.03x slower                                        |
| pidigits                | 251 ms                                                       | 260 ms: 1.04x slower                                         |
| xml_etree_process       | 56.5 ms                                                      | 58.8 ms: 1.04x slower                                        |
| float                   | 74.2 ms                                                      | 77.6 ms: 1.05x slower                                        |
| python_startup          | 10.8 ms                                                      | 11.3 ms: 1.05x slower                                        |
| pathlib                 | 19.1 ms                                                      | 20.0 ms: 1.05x slower                                        |
| scimark_monte_carlo     | 68.2 ms                                                      | 71.7 ms: 1.05x slower                                        |
| scimark_sparse_mat_mult | 4.05 ms                                                      | 4.26 ms: 1.05x slower                                        |
| sqlite_synth            | 2.50 us                                                      | 2.63 us: 1.05x slower                                        |
| scimark_fft             | 285 ms                                                       | 300 ms: 1.05x slower                                         |
| xml_etree_generate      | 80.5 ms                                                      | 85.2 ms: 1.06x slower                                        |
| unpickle_list           | 4.53 us                                                      | 4.81 us: 1.06x slower                                        |
| telco                   | 6.86 ms                                                      | 7.27 ms: 1.06x slower                                        |
| bench_mp_pool           | 4.62 ms                                                      | 4.98 ms: 1.08x slower                                        |
| python_startup_no_site  | 7.76 ms                                                      | 8.39 ms: 1.08x slower                                        |
| unpickle                | 13.4 us                                                      | 14.6 us: 1.08x slower                                        |
| coverage                | 84.8 ms                                                      | 92.9 ms: 1.10x slower                                        |
| unpack_sequence         | 45.6 ns                                                      | 50.1 ns: 1.10x slower                                        |
| pickle_list             | 3.83 us                                                      | 4.42 us: 1.15x slower                                        |
| async_generators        | 316 ms                                                       | 392 ms: 1.24x slower                                         |
| dask                    | 410 ms                                                       | 560 ms: 1.36x slower                                         |
| Geometric mean          | (ref)                                                        | 1.04x faster                                                 |

Benchmark hidden because not significant (5): gc_traversal, pickle_pure_python, xml_etree_iterparse, create_gc_cycles, nbody
Ignored benchmarks (20) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 99.38% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
