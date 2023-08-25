
# Results vs. 3.11.0

- fork: python
- ref: f533f216e6aaba3f3663
- machine: linux-x86_64
- commit hash: f533f21
- commit date: 2023-03-06
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230306-pythonperf2-x86_64-python-f533f216e6aaba3f3663-3.12.0a5+-f533f21 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 284 ms: 1.01x faster                                                         |
| chameleon      | 7.67 ms                                                      | 7.24 ms: 1.06x faster                                                        |
| docutils       | 2.86 sec                                                     | 2.81 sec: 1.02x faster                                                       |
| html5lib       | 72.9 ms                                                      | 66.8 ms: 1.09x faster                                                        |
| tornado_http   | 122 ms                                                       | 116 ms: 1.05x faster                                                         |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230306-pythonperf2-x86_64-python-f533f216e6aaba3f3663-3.12.0a5+-f533f21 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 74.2 ms                                                      | 73.5 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                 |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230306-pythonperf2-x86_64-python-f533f216e6aaba3f3663-3.12.0a5+-f533f21 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 148 ms: 1.06x faster                                                         |
| regex_v8       | 23.9 ms                                                      | 24.1 ms: 1.01x slower                                                        |
| regex_dna      | 227 ms                                                       | 232 ms: 1.02x slower                                                         |
| regex_effbot   | 3.50 ms                                                      | 3.62 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230306-pythonperf2-x86_64-python-f533f216e6aaba3f3663-3.12.0a5+-f533f21 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.2 ms: 1.31x faster                                                        |
| json_loads           | 28.7 us                                                      | 24.0 us: 1.20x faster                                                        |
| unpickle_pure_python | 241 us                                                       | 202 us: 1.19x faster                                                         |
| xml_etree_parse      | 158 ms                                                       | 143 ms: 1.10x faster                                                         |
| pickle_pure_python   | 319 us                                                       | 305 us: 1.05x faster                                                         |
| pickle_list          | 3.83 us                                                      | 3.85 us: 1.01x slower                                                        |
| xml_etree_process    | 56.5 ms                                                      | 57.4 ms: 1.02x slower                                                        |
| unpickle             | 13.4 us                                                      | 13.8 us: 1.03x slower                                                        |
| xml_etree_generate   | 80.5 ms                                                      | 83.5 ms: 1.04x slower                                                        |
| pickle_dict          | 30.8 us                                                      | 32.2 us: 1.05x slower                                                        |
| pickle               | 9.64 us                                                      | 10.2 us: 1.05x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.05x faster                                                                 |

Benchmark hidden because not significant (2): unpickle_list, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230306-pythonperf2-x86_64-python-f533f216e6aaba3f3663-3.12.0a5+-f533f21 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.3 ms: 1.05x slower                                                        |
| python_startup_no_site | 7.76 ms                                                      | 8.34 ms: 1.08x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230306-pythonperf2-x86_64-python-f533f216e6aaba3f3663-3.12.0a5+-f533f21 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.0 ms                                                      | 10.2 ms: 1.08x faster                                                        |
| genshi_xml      | 58.5 ms                                                      | 54.9 ms: 1.07x faster                                                        |
| django_template | 40.2 ms                                                      | 39.1 ms: 1.03x faster                                                        |
| genshi_text     | 26.1 ms                                                      | 25.5 ms: 1.02x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.05x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230306-pythonperf2-x86_64-python-f533f216e6aaba3f3663-3.12.0a5+-f533f21 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| asyncio_tcp             | 753 ms                                                       | 386 ms: 1.95x faster                                                         |
| generators              | 56.0 ms                                                      | 38.2 ms: 1.47x faster                                                        |
| json_dumps              | 13.4 ms                                                      | 10.2 ms: 1.31x faster                                                        |
| mypy2                   | 451 ms                                                       | 375 ms: 1.20x faster                                                         |
| json_loads              | 28.7 us                                                      | 24.0 us: 1.20x faster                                                        |
| unpickle_pure_python    | 241 us                                                       | 202 us: 1.19x faster                                                         |
| deltablue               | 4.00 ms                                                      | 3.35 ms: 1.19x faster                                                        |
| json                    | 5.65 ms                                                      | 4.97 ms: 1.14x faster                                                        |
| coroutines              | 27.6 ms                                                      | 24.8 ms: 1.11x faster                                                        |
| scimark_lu              | 115 ms                                                       | 103 ms: 1.11x faster                                                         |
| xml_etree_parse         | 158 ms                                                       | 143 ms: 1.10x faster                                                         |
| richards                | 48.3 ms                                                      | 44.0 ms: 1.10x faster                                                        |
| chaos                   | 80.9 ms                                                      | 74.1 ms: 1.09x faster                                                        |
| html5lib                | 72.9 ms                                                      | 66.8 ms: 1.09x faster                                                        |
| hexiom                  | 7.13 ms                                                      | 6.55 ms: 1.09x faster                                                        |
| logging_format          | 8.11 us                                                      | 7.45 us: 1.09x faster                                                        |
| deepcopy_memo           | 38.8 us                                                      | 35.8 us: 1.08x faster                                                        |
| mako                    | 11.0 ms                                                      | 10.2 ms: 1.08x faster                                                        |
| logging_simple          | 7.19 us                                                      | 6.66 us: 1.08x faster                                                        |
| raytrace                | 317 ms                                                       | 295 ms: 1.07x faster                                                         |
| go                      | 164 ms                                                       | 153 ms: 1.07x faster                                                         |
| genshi_xml              | 58.5 ms                                                      | 54.9 ms: 1.07x faster                                                        |
| regex_compile           | 158 ms                                                       | 148 ms: 1.06x faster                                                         |
| dulwich_log             | 68.4 ms                                                      | 64.3 ms: 1.06x faster                                                        |
| chameleon               | 7.67 ms                                                      | 7.24 ms: 1.06x faster                                                        |
| logging_silent          | 101 ns                                                       | 95.6 ns: 1.05x faster                                                        |
| sqlglot_normalize       | 126 ms                                                       | 120 ms: 1.05x faster                                                         |
| tornado_http            | 122 ms                                                       | 116 ms: 1.05x faster                                                         |
| pycparser               | 1.32 sec                                                     | 1.26 sec: 1.05x faster                                                       |
| bench_thread_pool       | 1.01 ms                                                      | 965 us: 1.05x faster                                                         |
| pickle_pure_python      | 319 us                                                       | 305 us: 1.05x faster                                                         |
| pprint_pformat          | 1.63 sec                                                     | 1.57 sec: 1.04x faster                                                       |
| scimark_sor             | 111 ms                                                       | 107 ms: 1.04x faster                                                         |
| mdp                     | 2.75 sec                                                     | 2.64 sec: 1.04x faster                                                       |
| async_tree_memoization  | 630 ms                                                       | 607 ms: 1.04x faster                                                         |
| sympy_expand            | 555 ms                                                       | 535 ms: 1.04x faster                                                         |
| sympy_integrate         | 25.8 ms                                                      | 24.9 ms: 1.03x faster                                                        |
| pyflate                 | 449 ms                                                       | 435 ms: 1.03x faster                                                         |
| pathlib                 | 19.1 ms                                                      | 18.5 ms: 1.03x faster                                                        |
| django_template         | 40.2 ms                                                      | 39.1 ms: 1.03x faster                                                        |
| deepcopy_reduce         | 3.51 us                                                      | 3.41 us: 1.03x faster                                                        |
| sqlglot_optimize        | 59.8 ms                                                      | 58.2 ms: 1.03x faster                                                        |
| pprint_safe_repr        | 784 ms                                                       | 764 ms: 1.03x faster                                                         |
| genshi_text             | 26.1 ms                                                      | 25.5 ms: 1.02x faster                                                        |
| async_tree_none         | 519 ms                                                       | 507 ms: 1.02x faster                                                         |
| deepcopy                | 399 us                                                       | 390 us: 1.02x faster                                                         |
| nqueens                 | 103 ms                                                       | 100 ms: 1.02x faster                                                         |
| coverage                | 84.8 ms                                                      | 82.8 ms: 1.02x faster                                                        |
| fannkuch                | 429 ms                                                       | 419 ms: 1.02x faster                                                         |
| sympy_str               | 337 ms                                                       | 332 ms: 1.02x faster                                                         |
| docutils                | 2.86 sec                                                     | 2.81 sec: 1.02x faster                                                       |
| unpack_sequence         | 45.6 ns                                                      | 45.0 ns: 1.01x faster                                                        |
| meteor_contest          | 131 ms                                                       | 129 ms: 1.01x faster                                                         |
| crypto_pyaes            | 83.4 ms                                                      | 82.3 ms: 1.01x faster                                                        |
| scimark_fft             | 285 ms                                                       | 282 ms: 1.01x faster                                                         |
| 2to3                    | 288 ms                                                       | 284 ms: 1.01x faster                                                         |
| async_tree_io           | 1.17 sec                                                     | 1.16 sec: 1.01x faster                                                       |
| float                   | 74.2 ms                                                      | 73.5 ms: 1.01x faster                                                        |
| async_tree_cpu_io_mixed | 749 ms                                                       | 744 ms: 1.01x faster                                                         |
| sympy_sum               | 185 ms                                                       | 186 ms: 1.01x slower                                                         |
| pickle_list             | 3.83 us                                                      | 3.85 us: 1.01x slower                                                        |
| regex_v8                | 23.9 ms                                                      | 24.1 ms: 1.01x slower                                                        |
| spectral_norm           | 93.3 ms                                                      | 94.0 ms: 1.01x slower                                                        |
| telco                   | 6.86 ms                                                      | 6.92 ms: 1.01x slower                                                        |
| xml_etree_process       | 56.5 ms                                                      | 57.4 ms: 1.02x slower                                                        |
| scimark_monte_carlo     | 68.2 ms                                                      | 69.4 ms: 1.02x slower                                                        |
| sqlglot_transpile       | 1.92 ms                                                      | 1.95 ms: 1.02x slower                                                        |
| regex_dna               | 227 ms                                                       | 232 ms: 1.02x slower                                                         |
| sqlglot_parse           | 1.53 ms                                                      | 1.58 ms: 1.03x slower                                                        |
| unpickle                | 13.4 us                                                      | 13.8 us: 1.03x slower                                                        |
| regex_effbot            | 3.50 ms                                                      | 3.62 ms: 1.03x slower                                                        |
| xml_etree_generate      | 80.5 ms                                                      | 83.5 ms: 1.04x slower                                                        |
| pickle_dict             | 30.8 us                                                      | 32.2 us: 1.05x slower                                                        |
| create_gc_cycles        | 1.61 ms                                                      | 1.68 ms: 1.05x slower                                                        |
| sqlite_synth            | 2.50 us                                                      | 2.62 us: 1.05x slower                                                        |
| python_startup          | 10.8 ms                                                      | 11.3 ms: 1.05x slower                                                        |
| thrift                  | 925 us                                                       | 972 us: 1.05x slower                                                         |
| scimark_sparse_mat_mult | 4.05 ms                                                      | 4.26 ms: 1.05x slower                                                        |
| bench_mp_pool           | 4.62 ms                                                      | 4.87 ms: 1.05x slower                                                        |
| pickle                  | 9.64 us                                                      | 10.2 us: 1.05x slower                                                        |
| comprehensions          | 24.6 us                                                      | 26.4 us: 1.07x slower                                                        |
| python_startup_no_site  | 7.76 ms                                                      | 8.34 ms: 1.08x slower                                                        |
| gc_traversal            | 3.85 ms                                                      | 4.26 ms: 1.11x slower                                                        |
| async_generators        | 316 ms                                                       | 389 ms: 1.23x slower                                                         |
| dask                    | 410 ms                                                       | 566 ms: 1.38x slower                                                         |
| Geometric mean          | (ref)                                                        | 1.04x faster                                                                 |

Benchmark hidden because not significant (4): unpickle_list, pidigits, xml_etree_iterparse, nbody
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x
