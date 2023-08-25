
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 2d526cd
- commit date: 2023-05-01
- overall geometric mean: 1.04x faster \*
- HPT reliability: 99.78%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230501-pythonperf2-x86_64-python-main-3.12.0a7+-2d526cd |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 286 ms: 1.01x faster                                         |
| docutils       | 2.86 sec                                                     | 2.89 sec: 1.01x slower                                       |
| html5lib       | 72.9 ms                                                      | 68.0 ms: 1.07x faster                                        |
| tornado_http   | 122 ms                                                       | 113 ms: 1.08x faster                                         |
| Geometric mean | (ref)                                                        | 1.03x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230501-pythonperf2-x86_64-python-main-3.12.0a7+-2d526cd |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| pidigits       | 251 ms                                                       | 259 ms: 1.03x slower                                         |
| float          | 74.2 ms                                                      | 77.8 ms: 1.05x slower                                        |
| Geometric mean | (ref)                                                        | 1.02x slower                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230501-pythonperf2-x86_64-python-main-3.12.0a7+-2d526cd |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 144 ms: 1.09x faster                                         |
| regex_v8       | 23.9 ms                                                      | 23.5 ms: 1.02x faster                                        |
| regex_effbot   | 3.50 ms                                                      | 3.46 ms: 1.01x faster                                        |
| regex_dna      | 227 ms                                                       | 230 ms: 1.01x slower                                         |
| Geometric mean | (ref)                                                        | 1.03x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230501-pythonperf2-x86_64-python-main-3.12.0a7+-2d526cd |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.7 ms: 1.25x faster                                        |
| unpickle_pure_python | 241 us                                                       | 208 us: 1.16x faster                                         |
| json_loads           | 28.7 us                                                      | 25.4 us: 1.13x faster                                        |
| xml_etree_parse      | 158 ms                                                       | 146 ms: 1.08x faster                                         |
| pickle               | 9.64 us                                                      | 9.94 us: 1.03x slower                                        |
| pickle_dict          | 30.8 us                                                      | 31.8 us: 1.03x slower                                        |
| xml_etree_process    | 56.5 ms                                                      | 58.6 ms: 1.04x slower                                        |
| unpickle_list        | 4.53 us                                                      | 4.83 us: 1.06x slower                                        |
| xml_etree_generate   | 80.5 ms                                                      | 86.2 ms: 1.07x slower                                        |
| unpickle             | 13.4 us                                                      | 14.6 us: 1.09x slower                                        |
| pickle_list          | 3.83 us                                                      | 4.41 us: 1.15x slower                                        |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                 |

Benchmark hidden because not significant (2): pickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230501-pythonperf2-x86_64-python-main-3.12.0a7+-2d526cd |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.1 ms: 1.04x slower                                        |
| python_startup_no_site | 7.76 ms                                                      | 8.33 ms: 1.07x slower                                        |
| Geometric mean         | (ref)                                                        | 1.05x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230501-pythonperf2-x86_64-python-main-3.12.0a7+-2d526cd |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_xml     | 58.5 ms                                                      | 53.5 ms: 1.09x faster                                        |
| mako           | 11.0 ms                                                      | 10.1 ms: 1.09x faster                                        |
| genshi_text    | 26.1 ms                                                      | 24.6 ms: 1.06x faster                                        |
| Geometric mean | (ref)                                                        | 1.08x faster                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230501-pythonperf2-x86_64-python-main-3.12.0a7+-2d526cd |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| asyncio_tcp             | 753 ms                                                       | 378 ms: 1.99x faster                                         |
| generators              | 56.0 ms                                                      | 36.3 ms: 1.54x faster                                        |
| fannkuch                | 429 ms                                                       | 338 ms: 1.27x faster                                         |
| json_dumps              | 13.4 ms                                                      | 10.7 ms: 1.25x faster                                        |
| deltablue               | 4.00 ms                                                      | 3.24 ms: 1.24x faster                                        |
| coroutines              | 27.6 ms                                                      | 22.6 ms: 1.22x faster                                        |
| chaos                   | 80.9 ms                                                      | 66.9 ms: 1.21x faster                                        |
| scimark_lu              | 115 ms                                                       | 94.8 ms: 1.21x faster                                        |
| hexiom                  | 7.13 ms                                                      | 5.94 ms: 1.20x faster                                        |
| mypy2                   | 451 ms                                                       | 377 ms: 1.20x faster                                         |
| unpickle_pure_python    | 241 us                                                       | 208 us: 1.16x faster                                         |
| nqueens                 | 103 ms                                                       | 89.2 ms: 1.15x faster                                        |
| json_loads              | 28.7 us                                                      | 25.4 us: 1.13x faster                                        |
| async_tree_memoization  | 630 ms                                                       | 560 ms: 1.13x faster                                         |
| sqlglot_parse           | 1.53 ms                                                      | 1.38 ms: 1.11x faster                                        |
| go                      | 164 ms                                                       | 148 ms: 1.11x faster                                         |
| logging_format          | 8.11 us                                                      | 7.34 us: 1.11x faster                                        |
| richards                | 48.3 ms                                                      | 43.7 ms: 1.11x faster                                        |
| genshi_xml              | 58.5 ms                                                      | 53.5 ms: 1.09x faster                                        |
| regex_compile           | 158 ms                                                       | 144 ms: 1.09x faster                                         |
| async_tree_none         | 519 ms                                                       | 476 ms: 1.09x faster                                         |
| mako                    | 11.0 ms                                                      | 10.1 ms: 1.09x faster                                        |
| logging_simple          | 7.19 us                                                      | 6.60 us: 1.09x faster                                        |
| mdp                     | 2.75 sec                                                     | 2.54 sec: 1.08x faster                                       |
| xml_etree_parse         | 158 ms                                                       | 146 ms: 1.08x faster                                         |
| json                    | 5.65 ms                                                      | 5.23 ms: 1.08x faster                                        |
| async_tree_io           | 1.17 sec                                                     | 1.09 sec: 1.08x faster                                       |
| tornado_http            | 122 ms                                                       | 113 ms: 1.08x faster                                         |
| logging_silent          | 101 ns                                                       | 93.8 ns: 1.07x faster                                        |
| sqlglot_transpile       | 1.92 ms                                                      | 1.79 ms: 1.07x faster                                        |
| html5lib                | 72.9 ms                                                      | 68.0 ms: 1.07x faster                                        |
| gc_traversal            | 3.85 ms                                                      | 3.59 ms: 1.07x faster                                        |
| pycparser               | 1.32 sec                                                     | 1.24 sec: 1.07x faster                                       |
| genshi_text             | 26.1 ms                                                      | 24.6 ms: 1.06x faster                                        |
| async_tree_cpu_io_mixed | 749 ms                                                       | 709 ms: 1.06x faster                                         |
| dulwich_log             | 68.4 ms                                                      | 65.1 ms: 1.05x faster                                        |
| spectral_norm           | 93.3 ms                                                      | 88.7 ms: 1.05x faster                                        |
| sqlglot_normalize       | 126 ms                                                       | 120 ms: 1.05x faster                                         |
| deepcopy                | 399 us                                                       | 382 us: 1.05x faster                                         |
| deepcopy_memo           | 38.8 us                                                      | 37.4 us: 1.04x faster                                        |
| bench_thread_pool       | 1.01 ms                                                      | 976 us: 1.04x faster                                         |
| deepcopy_reduce         | 3.51 us                                                      | 3.42 us: 1.03x faster                                        |
| crypto_pyaes            | 83.4 ms                                                      | 81.3 ms: 1.03x faster                                        |
| thrift                  | 925 us                                                       | 904 us: 1.02x faster                                         |
| raytrace                | 317 ms                                                       | 311 ms: 1.02x faster                                         |
| regex_v8                | 23.9 ms                                                      | 23.5 ms: 1.02x faster                                        |
| sqlglot_optimize        | 59.8 ms                                                      | 58.9 ms: 1.01x faster                                        |
| pathlib                 | 19.1 ms                                                      | 18.8 ms: 1.01x faster                                        |
| regex_effbot            | 3.50 ms                                                      | 3.46 ms: 1.01x faster                                        |
| scimark_sor             | 111 ms                                                       | 110 ms: 1.01x faster                                         |
| 2to3                    | 288 ms                                                       | 286 ms: 1.01x faster                                         |
| comprehensions          | 24.6 us                                                      | 24.5 us: 1.00x faster                                        |
| pprint_pformat          | 1.63 sec                                                     | 1.65 sec: 1.01x slower                                       |
| docutils                | 2.86 sec                                                     | 2.89 sec: 1.01x slower                                       |
| regex_dna               | 227 ms                                                       | 230 ms: 1.01x slower                                         |
| pyflate                 | 449 ms                                                       | 456 ms: 1.02x slower                                         |
| pprint_safe_repr        | 784 ms                                                       | 802 ms: 1.02x slower                                         |
| create_gc_cycles        | 1.61 ms                                                      | 1.65 ms: 1.03x slower                                        |
| pidigits                | 251 ms                                                       | 259 ms: 1.03x slower                                         |
| pickle                  | 9.64 us                                                      | 9.94 us: 1.03x slower                                        |
| scimark_fft             | 285 ms                                                       | 294 ms: 1.03x slower                                         |
| pickle_dict             | 30.8 us                                                      | 31.8 us: 1.03x slower                                        |
| python_startup          | 10.8 ms                                                      | 11.1 ms: 1.04x slower                                        |
| xml_etree_process       | 56.5 ms                                                      | 58.6 ms: 1.04x slower                                        |
| sqlite_synth            | 2.50 us                                                      | 2.61 us: 1.05x slower                                        |
| float                   | 74.2 ms                                                      | 77.8 ms: 1.05x slower                                        |
| telco                   | 6.86 ms                                                      | 7.22 ms: 1.05x slower                                        |
| scimark_sparse_mat_mult | 4.05 ms                                                      | 4.29 ms: 1.06x slower                                        |
| meteor_contest          | 131 ms                                                       | 139 ms: 1.06x slower                                         |
| unpickle_list           | 4.53 us                                                      | 4.83 us: 1.06x slower                                        |
| xml_etree_generate      | 80.5 ms                                                      | 86.2 ms: 1.07x slower                                        |
| python_startup_no_site  | 7.76 ms                                                      | 8.33 ms: 1.07x slower                                        |
| unpickle                | 13.4 us                                                      | 14.6 us: 1.09x slower                                        |
| coverage                | 84.8 ms                                                      | 92.8 ms: 1.09x slower                                        |
| bench_mp_pool           | 4.62 ms                                                      | 5.21 ms: 1.13x slower                                        |
| pickle_list             | 3.83 us                                                      | 4.41 us: 1.15x slower                                        |
| async_generators        | 316 ms                                                       | 382 ms: 1.21x slower                                         |
| unpack_sequence         | 45.6 ns                                                      | 55.5 ns: 1.22x slower                                        |
| dask                    | 410 ms                                                       | 560 ms: 1.37x slower                                         |
| Geometric mean          | (ref)                                                        | 1.04x faster                                                 |

Benchmark hidden because not significant (4): nbody, pickle_pure_python, scimark_monte_carlo, xml_etree_iterparse
Ignored benchmarks (16) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 99.78% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x
