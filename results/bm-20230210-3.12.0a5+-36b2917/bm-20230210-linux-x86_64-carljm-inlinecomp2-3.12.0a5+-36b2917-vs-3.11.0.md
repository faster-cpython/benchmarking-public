
# Results vs. 3.11.0

- fork: carljm
- ref: inlinecomp2
- machine: linux-x86_64
- commit hash: 36b2917
- commit date: 2023-02-10
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                          |
| docutils       | 2.63 sec                                               | 2.53 sec: 1.04x faster                                        |
| html5lib       | 64.5 ms                                                | 60.6 ms: 1.06x faster                                         |
| tornado_http   | 96.3 ms                                                | 94.1 ms: 1.02x faster                                         |
| Geometric mean | (ref)                                                  | 1.03x faster                                                  |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.8 ms: 1.06x faster                                         |
| pidigits       | 198 ms                                                 | 193 ms: 1.03x faster                                          |
| nbody          | 93.1 ms                                                | 94.0 ms: 1.01x slower                                         |
| Geometric mean | (ref)                                                  | 1.03x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.66 ms: 1.09x faster                                         |
| regex_compile  | 138 ms                                                 | 128 ms: 1.08x faster                                          |
| regex_v8       | 22.0 ms                                                | 21.6 ms: 1.02x faster                                         |
| regex_dna      | 204 ms                                                 | 205 ms: 1.01x slower                                          |
| Geometric mean | (ref)                                                  | 1.05x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.39 ms: 1.34x faster                                         |
| unpickle_pure_python | 228 us                                                 | 198 us: 1.15x faster                                          |
| json_loads           | 26.5 us                                                | 23.7 us: 1.12x faster                                         |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                          |
| pickle_pure_python   | 306 us                                                 | 291 us: 1.05x faster                                          |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                          |
| pickle_dict          | 31.1 us                                                | 30.9 us: 1.01x faster                                         |
| pickle_list          | 4.11 us                                                | 4.15 us: 1.01x slower                                         |
| xml_etree_process    | 53.9 ms                                                | 54.8 ms: 1.02x slower                                         |
| unpickle_list        | 4.91 us                                                | 5.13 us: 1.04x slower                                         |
| xml_etree_generate   | 76.2 ms                                                | 80.2 ms: 1.05x slower                                         |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                  |

Benchmark hidden because not significant (2): unpickle, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.90 ms: 1.04x slower                                         |
| python_startup_no_site | 6.01 ms                                                | 6.46 ms: 1.08x slower                                         |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| genshi_xml     | 51.8 ms                                                | 47.8 ms: 1.08x faster                                         |
| genshi_text    | 21.6 ms                                                | 20.9 ms: 1.03x faster                                         |
| mako           | 10.1 ms                                                | 9.90 ms: 1.02x faster                                         |
| Geometric mean | (ref)                                                  | 1.03x faster                                                  |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 498 ms: 1.85x faster                                          |
| json_dumps              | 12.6 ms                                                | 9.39 ms: 1.34x faster                                         |
| mypy2                   | 420 ms                                                 | 322 ms: 1.30x faster                                          |
| deltablue               | 3.67 ms                                                | 3.13 ms: 1.17x faster                                         |
| unpickle_pure_python    | 228 us                                                 | 198 us: 1.15x faster                                          |
| scimark_sparse_mat_mult | 4.50 ms                                                | 3.94 ms: 1.14x faster                                         |
| gc_traversal            | 4.02 ms                                                | 3.58 ms: 1.12x faster                                         |
| json_loads              | 26.5 us                                                | 23.7 us: 1.12x faster                                         |
| nqueens                 | 83.4 ms                                                | 74.9 ms: 1.11x faster                                         |
| scimark_sor             | 118 ms                                                 | 106 ms: 1.11x faster                                          |
| gunicorn                | 1.18 ms                                                | 1.07 ms: 1.10x faster                                         |
| sympy_str               | 290 ms                                                 | 265 ms: 1.10x faster                                          |
| chaos                   | 69.2 ms                                                | 63.2 ms: 1.10x faster                                         |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                         |
| regex_effbot            | 3.99 ms                                                | 3.66 ms: 1.09x faster                                         |
| richards                | 45.7 ms                                                | 42.1 ms: 1.09x faster                                         |
| json                    | 4.94 ms                                                | 4.55 ms: 1.09x faster                                         |
| hexiom                  | 6.37 ms                                                | 5.87 ms: 1.09x faster                                         |
| deepcopy_memo           | 37.0 us                                                | 34.1 us: 1.09x faster                                         |
| pycparser               | 1.18 sec                                               | 1.09 sec: 1.08x faster                                        |
| genshi_xml              | 51.8 ms                                                | 47.8 ms: 1.08x faster                                         |
| regex_compile           | 138 ms                                                 | 128 ms: 1.08x faster                                          |
| sympy_expand            | 475 ms                                                 | 439 ms: 1.08x faster                                          |
| sympy_integrate         | 21.0 ms                                                | 19.5 ms: 1.08x faster                                         |
| logging_silent          | 101 ns                                                 | 94.1 ns: 1.07x faster                                         |
| sympy_sum               | 167 ms                                                 | 155 ms: 1.07x faster                                          |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                          |
| scimark_fft             | 328 ms                                                 | 307 ms: 1.07x faster                                          |
| spectral_norm           | 100 ms                                                 | 93.9 ms: 1.07x faster                                         |
| html5lib                | 64.5 ms                                                | 60.6 ms: 1.06x faster                                         |
| raytrace                | 297 ms                                                 | 279 ms: 1.06x faster                                          |
| sqlglot_normalize       | 108 ms                                                 | 101 ms: 1.06x faster                                          |
| pprint_pformat          | 1.46 sec                                               | 1.37 sec: 1.06x faster                                        |
| float                   | 77.2 ms                                                | 72.8 ms: 1.06x faster                                         |
| fannkuch                | 388 ms                                                 | 366 ms: 1.06x faster                                          |
| async_tree_none         | 526 ms                                                 | 498 ms: 1.06x faster                                          |
| deepcopy                | 342 us                                                 | 324 us: 1.06x faster                                          |
| sqlglot_optimize        | 53.1 ms                                                | 50.4 ms: 1.05x faster                                         |
| pickle_pure_python      | 306 us                                                 | 291 us: 1.05x faster                                          |
| pprint_safe_repr        | 701 ms                                                 | 668 ms: 1.05x faster                                          |
| logging_format          | 6.68 us                                                | 6.39 us: 1.05x faster                                         |
| bench_thread_pool       | 819 us                                                 | 785 us: 1.04x faster                                          |
| pathlib                 | 18.2 ms                                                | 17.5 ms: 1.04x faster                                         |
| docutils                | 2.63 sec                                               | 2.53 sec: 1.04x faster                                        |
| pyflate                 | 418 ms                                                 | 403 ms: 1.04x faster                                          |
| scimark_monte_carlo     | 68.1 ms                                                | 65.5 ms: 1.04x faster                                         |
| logging_simple          | 6.03 us                                                | 5.83 us: 1.04x faster                                         |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                          |
| sqlalchemy_declarative  | 138 ms                                                 | 134 ms: 1.03x faster                                          |
| sqlalchemy_imperative   | 17.9 ms                                                | 17.4 ms: 1.03x faster                                         |
| genshi_text             | 21.6 ms                                                | 20.9 ms: 1.03x faster                                         |
| telco                   | 6.58 ms                                                | 6.40 ms: 1.03x faster                                         |
| pidigits                | 198 ms                                                 | 193 ms: 1.03x faster                                          |
| meteor_contest          | 107 ms                                                 | 104 ms: 1.03x faster                                          |
| async_tree_memoization  | 627 ms                                                 | 612 ms: 1.03x faster                                          |
| tornado_http            | 96.3 ms                                                | 94.1 ms: 1.02x faster                                         |
| regex_v8                | 22.0 ms                                                | 21.6 ms: 1.02x faster                                         |
| go                      | 140 ms                                                 | 137 ms: 1.02x faster                                          |
| crypto_pyaes            | 74.7 ms                                                | 73.3 ms: 1.02x faster                                         |
| mako                    | 10.1 ms                                                | 9.90 ms: 1.02x faster                                         |
| async_tree_io           | 1.30 sec                                               | 1.27 sec: 1.02x faster                                        |
| dulwich_log             | 63.7 ms                                                | 62.6 ms: 1.02x faster                                         |
| scimark_lu              | 110 ms                                                 | 108 ms: 1.02x faster                                          |
| deepcopy_reduce         | 2.94 us                                                | 2.90 us: 1.01x faster                                         |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                          |
| coverage                | 100 ms                                                 | 99.3 ms: 1.01x faster                                         |
| pickle_dict             | 31.1 us                                                | 30.9 us: 1.01x faster                                         |
| create_gc_cycles        | 1.49 ms                                                | 1.48 ms: 1.01x faster                                         |
| regex_dna               | 204 ms                                                 | 205 ms: 1.01x slower                                          |
| nbody                   | 93.1 ms                                                | 94.0 ms: 1.01x slower                                         |
| sqlglot_parse           | 1.40 ms                                                | 1.41 ms: 1.01x slower                                         |
| pickle_list             | 4.11 us                                                | 4.15 us: 1.01x slower                                         |
| coroutines              | 25.5 ms                                                | 25.8 ms: 1.01x slower                                         |
| async_tree_cpu_io_mixed | 739 ms                                                 | 747 ms: 1.01x slower                                          |
| mdp                     | 2.62 sec                                               | 2.66 sec: 1.02x slower                                        |
| xml_etree_process       | 53.9 ms                                                | 54.8 ms: 1.02x slower                                         |
| sqlite_synth            | 2.52 us                                                | 2.58 us: 1.03x slower                                         |
| unpack_sequence         | 43.1 ns                                                | 44.4 ns: 1.03x slower                                         |
| python_startup          | 8.52 ms                                                | 8.90 ms: 1.04x slower                                         |
| unpickle_list           | 4.91 us                                                | 5.13 us: 1.04x slower                                         |
| xml_etree_generate      | 76.2 ms                                                | 80.2 ms: 1.05x slower                                         |
| generators              | 73.5 ms                                                | 77.7 ms: 1.06x slower                                         |
| python_startup_no_site  | 6.01 ms                                                | 6.46 ms: 1.08x slower                                         |
| async_generators        | 368 ms                                                 | 427 ms: 1.16x slower                                          |
| Geometric mean          | (ref)                                                  | 1.05x faster                                                  |

Benchmark hidden because not significant (8): django_template, bench_mp_pool, chameleon, unpickle, sqlglot_transpile, djangocms, pickle, thrift
Ignored benchmarks (8) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, dask, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x
