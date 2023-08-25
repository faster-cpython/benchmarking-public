
# Results vs. 3.11.0

- fork: python
- ref: e95dd40aff35775efce4
- machine: linux-x86_64
- commit hash: e95dd40
- commit date: 2023-05-03
- overall geometric mean: 1.03x faster \*
- HPT reliability: 99.44%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230503-pythonperf2-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 284 ms: 1.01x faster                                                         |
| docutils       | 2.86 sec                                                     | 2.90 sec: 1.01x slower                                                       |
| tornado_http   | 122 ms                                                       | 114 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230503-pythonperf2-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 85.3 ms: 1.06x faster                                                        |
| pidigits       | 251 ms                                                       | 260 ms: 1.04x slower                                                         |
| float          | 74.2 ms                                                      | 78.9 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230503-pythonperf2-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 145 ms: 1.09x faster                                                         |
| regex_effbot   | 3.50 ms                                                      | 3.47 ms: 1.01x faster                                                        |
| regex_v8       | 23.9 ms                                                      | 23.8 ms: 1.00x faster                                                        |
| regex_dna      | 227 ms                                                       | 232 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230503-pythonperf2-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.5 ms: 1.28x faster                                                        |
| unpickle_pure_python | 241 us                                                       | 205 us: 1.18x faster                                                         |
| json_loads           | 28.7 us                                                      | 25.2 us: 1.14x faster                                                        |
| xml_etree_parse      | 158 ms                                                       | 148 ms: 1.07x faster                                                         |
| pickle_pure_python   | 319 us                                                       | 318 us: 1.00x faster                                                         |
| unpickle_list        | 4.53 us                                                      | 4.61 us: 1.02x slower                                                        |
| xml_etree_process    | 56.5 ms                                                      | 58.8 ms: 1.04x slower                                                        |
| xml_etree_generate   | 80.5 ms                                                      | 85.6 ms: 1.06x slower                                                        |
| pickle_dict          | 30.8 us                                                      | 33.3 us: 1.08x slower                                                        |
| pickle               | 9.64 us                                                      | 10.5 us: 1.09x slower                                                        |
| unpickle             | 13.4 us                                                      | 15.0 us: 1.12x slower                                                        |
| pickle_list          | 3.83 us                                                      | 4.41 us: 1.15x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230503-pythonperf2-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.2 ms: 1.04x slower                                                        |
| python_startup_no_site | 7.76 ms                                                      | 8.39 ms: 1.08x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230503-pythonperf2-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|-----------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako      | 11.0 ms                                                      | 9.92 ms: 1.11x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230503-pythonperf2-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| asyncio_tcp             | 753 ms                                                       | 380 ms: 1.98x faster                                                         |
| generators              | 56.0 ms                                                      | 36.0 ms: 1.56x faster                                                        |
| json_dumps              | 13.4 ms                                                      | 10.5 ms: 1.28x faster                                                        |
| deltablue               | 4.00 ms                                                      | 3.25 ms: 1.23x faster                                                        |
| coroutines              | 27.6 ms                                                      | 22.4 ms: 1.23x faster                                                        |
| hexiom                  | 7.13 ms                                                      | 5.86 ms: 1.22x faster                                                        |
| fannkuch                | 429 ms                                                       | 357 ms: 1.20x faster                                                         |
| mypy2                   | 451 ms                                                       | 377 ms: 1.20x faster                                                         |
| chaos                   | 80.9 ms                                                      | 67.8 ms: 1.19x faster                                                        |
| unpickle_pure_python    | 241 us                                                       | 205 us: 1.18x faster                                                         |
| nqueens                 | 103 ms                                                       | 88.9 ms: 1.16x faster                                                        |
| scimark_lu              | 115 ms                                                       | 99.5 ms: 1.15x faster                                                        |
| json_loads              | 28.7 us                                                      | 25.2 us: 1.14x faster                                                        |
| go                      | 164 ms                                                       | 146 ms: 1.12x faster                                                         |
| mako                    | 11.0 ms                                                      | 9.92 ms: 1.11x faster                                                        |
| sqlglot_parse           | 1.53 ms                                                      | 1.39 ms: 1.10x faster                                                        |
| async_tree_memoization  | 630 ms                                                       | 572 ms: 1.10x faster                                                         |
| async_tree_none         | 519 ms                                                       | 476 ms: 1.09x faster                                                         |
| json                    | 5.65 ms                                                      | 5.18 ms: 1.09x faster                                                        |
| logging_silent          | 101 ns                                                       | 92.4 ns: 1.09x faster                                                        |
| regex_compile           | 158 ms                                                       | 145 ms: 1.09x faster                                                         |
| richards                | 48.3 ms                                                      | 44.5 ms: 1.08x faster                                                        |
| mdp                     | 2.75 sec                                                     | 2.53 sec: 1.08x faster                                                       |
| logging_format          | 8.11 us                                                      | 7.51 us: 1.08x faster                                                        |
| async_tree_io           | 1.17 sec                                                     | 1.09 sec: 1.08x faster                                                       |
| pycparser               | 1.32 sec                                                     | 1.23 sec: 1.07x faster                                                       |
| xml_etree_parse         | 158 ms                                                       | 148 ms: 1.07x faster                                                         |
| tornado_http            | 122 ms                                                       | 114 ms: 1.07x faster                                                         |
| async_tree_cpu_io_mixed | 749 ms                                                       | 703 ms: 1.07x faster                                                         |
| nbody                   | 90.7 ms                                                      | 85.3 ms: 1.06x faster                                                        |
| sqlglot_transpile       | 1.92 ms                                                      | 1.81 ms: 1.06x faster                                                        |
| logging_simple          | 7.19 us                                                      | 6.78 us: 1.06x faster                                                        |
| dulwich_log             | 68.4 ms                                                      | 64.8 ms: 1.06x faster                                                        |
| bench_thread_pool       | 1.01 ms                                                      | 958 us: 1.06x faster                                                         |
| sqlglot_normalize       | 126 ms                                                       | 120 ms: 1.05x faster                                                         |
| deepcopy                | 399 us                                                       | 383 us: 1.04x faster                                                         |
| deepcopy_memo           | 38.8 us                                                      | 37.2 us: 1.04x faster                                                        |
| crypto_pyaes            | 83.4 ms                                                      | 80.3 ms: 1.04x faster                                                        |
| spectral_norm           | 93.3 ms                                                      | 90.2 ms: 1.03x faster                                                        |
| pyflate                 | 449 ms                                                       | 437 ms: 1.03x faster                                                         |
| gc_traversal            | 3.85 ms                                                      | 3.76 ms: 1.02x faster                                                        |
| deepcopy_reduce         | 3.51 us                                                      | 3.46 us: 1.01x faster                                                        |
| 2to3                    | 288 ms                                                       | 284 ms: 1.01x faster                                                         |
| sqlglot_optimize        | 59.8 ms                                                      | 59.2 ms: 1.01x faster                                                        |
| regex_effbot            | 3.50 ms                                                      | 3.47 ms: 1.01x faster                                                        |
| pickle_pure_python      | 319 us                                                       | 318 us: 1.00x faster                                                         |
| regex_v8                | 23.9 ms                                                      | 23.8 ms: 1.00x faster                                                        |
| comprehensions          | 24.6 us                                                      | 24.5 us: 1.00x faster                                                        |
| pprint_pformat          | 1.63 sec                                                     | 1.65 sec: 1.01x slower                                                       |
| docutils                | 2.86 sec                                                     | 2.90 sec: 1.01x slower                                                       |
| unpickle_list           | 4.53 us                                                      | 4.61 us: 1.02x slower                                                        |
| pathlib                 | 19.1 ms                                                      | 19.4 ms: 1.02x slower                                                        |
| regex_dna               | 227 ms                                                       | 232 ms: 1.02x slower                                                         |
| pprint_safe_repr        | 784 ms                                                       | 808 ms: 1.03x slower                                                         |
| pidigits                | 251 ms                                                       | 260 ms: 1.04x slower                                                         |
| python_startup          | 10.8 ms                                                      | 11.2 ms: 1.04x slower                                                        |
| xml_etree_process       | 56.5 ms                                                      | 58.8 ms: 1.04x slower                                                        |
| scimark_fft             | 285 ms                                                       | 298 ms: 1.04x slower                                                         |
| sqlite_synth            | 2.50 us                                                      | 2.62 us: 1.05x slower                                                        |
| meteor_contest          | 131 ms                                                       | 138 ms: 1.06x slower                                                         |
| telco                   | 6.86 ms                                                      | 7.26 ms: 1.06x slower                                                        |
| scimark_monte_carlo     | 68.2 ms                                                      | 72.3 ms: 1.06x slower                                                        |
| xml_etree_generate      | 80.5 ms                                                      | 85.6 ms: 1.06x slower                                                        |
| float                   | 74.2 ms                                                      | 78.9 ms: 1.06x slower                                                        |
| coverage                | 84.8 ms                                                      | 90.6 ms: 1.07x slower                                                        |
| python_startup_no_site  | 7.76 ms                                                      | 8.39 ms: 1.08x slower                                                        |
| pickle_dict             | 30.8 us                                                      | 33.3 us: 1.08x slower                                                        |
| pickle                  | 9.64 us                                                      | 10.5 us: 1.09x slower                                                        |
| scimark_sparse_mat_mult | 4.05 ms                                                      | 4.44 ms: 1.10x slower                                                        |
| unpickle                | 13.4 us                                                      | 15.0 us: 1.12x slower                                                        |
| pickle_list             | 3.83 us                                                      | 4.41 us: 1.15x slower                                                        |
| unpack_sequence         | 45.6 ns                                                      | 52.7 ns: 1.16x slower                                                        |
| async_generators        | 316 ms                                                       | 389 ms: 1.23x slower                                                         |
| dask                    | 410 ms                                                       | 563 ms: 1.37x slower                                                         |
| bench_mp_pool           | 4.62 ms                                                      | 7.84 ms: 1.70x slower                                                        |
| Geometric mean          | (ref)                                                        | 1.03x faster                                                                 |

Benchmark hidden because not significant (4): scimark_sor, create_gc_cycles, raytrace, xml_etree_iterparse
Ignored benchmarks (20) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 99.44% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
