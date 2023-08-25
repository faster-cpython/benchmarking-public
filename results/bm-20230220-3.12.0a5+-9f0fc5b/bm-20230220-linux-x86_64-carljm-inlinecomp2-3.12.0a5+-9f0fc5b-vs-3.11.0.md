
# Results vs. 3.11.0

- fork: carljm
- ref: inlinecomp2
- machine: linux-x86_64
- commit hash: 9f0fc5b
- commit date: 2023-02-20
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230220-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-9f0fc5b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 248 ms: 1.04x faster                                          |
| chameleon      | 6.47 ms                                                | 6.32 ms: 1.02x faster                                         |
| docutils       | 2.63 sec                                               | 2.53 sec: 1.04x faster                                        |
| html5lib       | 64.5 ms                                                | 60.4 ms: 1.07x faster                                         |
| tornado_http   | 96.3 ms                                                | 94.3 ms: 1.02x faster                                         |
| Geometric mean | (ref)                                                  | 1.04x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230220-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-9f0fc5b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.0 ms: 1.07x faster                                         |
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                          |
| nbody          | 93.1 ms                                                | 94.0 ms: 1.01x slower                                         |
| Geometric mean | (ref)                                                  | 1.04x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230220-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-9f0fc5b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 138 ms                                                 | 127 ms: 1.09x faster                                          |
| regex_effbot   | 3.99 ms                                                | 3.69 ms: 1.08x faster                                         |
| regex_v8       | 22.0 ms                                                | 21.8 ms: 1.01x faster                                         |
| regex_dna      | 204 ms                                                 | 207 ms: 1.02x slower                                          |
| Geometric mean | (ref)                                                  | 1.04x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230220-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-9f0fc5b |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.49 ms: 1.33x faster                                         |
| unpickle_pure_python | 228 us                                                 | 197 us: 1.16x faster                                          |
| json_loads           | 26.5 us                                                | 24.1 us: 1.10x faster                                         |
| pickle_pure_python   | 306 us                                                 | 281 us: 1.09x faster                                          |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                          |
| pickle_dict          | 31.1 us                                                | 30.0 us: 1.04x faster                                         |
| pickle_list          | 4.11 us                                                | 3.97 us: 1.03x faster                                         |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.01x faster                                          |
| xml_etree_process    | 53.9 ms                                                | 55.5 ms: 1.03x slower                                         |
| unpickle_list        | 4.91 us                                                | 5.13 us: 1.05x slower                                         |
| xml_etree_generate   | 76.2 ms                                                | 80.6 ms: 1.06x slower                                         |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                  |

Benchmark hidden because not significant (2): unpickle, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230220-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-9f0fc5b |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.96 ms: 1.05x slower                                         |
| python_startup_no_site | 6.01 ms                                                | 6.50 ms: 1.08x slower                                         |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230220-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-9f0fc5b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| genshi_xml     | 51.8 ms                                                | 47.9 ms: 1.08x faster                                         |
| genshi_text    | 21.6 ms                                                | 20.8 ms: 1.03x faster                                         |
| mako           | 10.1 ms                                                | 9.83 ms: 1.03x faster                                         |
| Geometric mean | (ref)                                                  | 1.03x faster                                                  |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230220-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-9f0fc5b |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.9 ms: 2.45x faster                                         |
| asyncio_tcp             | 922 ms                                                 | 502 ms: 1.83x faster                                          |
| json_dumps              | 12.6 ms                                                | 9.49 ms: 1.33x faster                                         |
| mypy2                   | 420 ms                                                 | 326 ms: 1.29x faster                                          |
| coroutines              | 25.5 ms                                                | 21.8 ms: 1.17x faster                                         |
| deltablue               | 3.67 ms                                                | 3.16 ms: 1.16x faster                                         |
| unpickle_pure_python    | 228 us                                                 | 197 us: 1.16x faster                                          |
| scimark_sparse_mat_mult | 4.50 ms                                                | 3.93 ms: 1.14x faster                                         |
| richards                | 45.7 ms                                                | 41.3 ms: 1.11x faster                                         |
| scimark_sor             | 118 ms                                                 | 107 ms: 1.10x faster                                          |
| logging_silent          | 101 ns                                                 | 91.7 ns: 1.10x faster                                         |
| json_loads              | 26.5 us                                                | 24.1 us: 1.10x faster                                         |
| gunicorn                | 1.18 ms                                                | 1.07 ms: 1.10x faster                                         |
| aiohttp                 | 1.10 ms                                                | 1.00 ms: 1.10x faster                                         |
| chaos                   | 69.2 ms                                                | 63.5 ms: 1.09x faster                                         |
| pickle_pure_python      | 306 us                                                 | 281 us: 1.09x faster                                          |
| regex_compile           | 138 ms                                                 | 127 ms: 1.09x faster                                          |
| regex_effbot            | 3.99 ms                                                | 3.69 ms: 1.08x faster                                         |
| deepcopy_memo           | 37.0 us                                                | 34.2 us: 1.08x faster                                         |
| genshi_xml              | 51.8 ms                                                | 47.9 ms: 1.08x faster                                         |
| sqlglot_normalize       | 108 ms                                                 | 99.8 ms: 1.08x faster                                         |
| float                   | 77.2 ms                                                | 72.0 ms: 1.07x faster                                         |
| hexiom                  | 6.37 ms                                                | 5.94 ms: 1.07x faster                                         |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                          |
| json                    | 4.94 ms                                                | 4.61 ms: 1.07x faster                                         |
| sympy_expand            | 475 ms                                                 | 444 ms: 1.07x faster                                          |
| sqlglot_optimize        | 53.1 ms                                                | 49.7 ms: 1.07x faster                                         |
| html5lib                | 64.5 ms                                                | 60.4 ms: 1.07x faster                                         |
| go                      | 140 ms                                                 | 131 ms: 1.07x faster                                          |
| scimark_fft             | 328 ms                                                 | 309 ms: 1.06x faster                                          |
| pycparser               | 1.18 sec                                               | 1.11 sec: 1.06x faster                                        |
| pprint_pformat          | 1.46 sec                                               | 1.37 sec: 1.06x faster                                        |
| mdp                     | 2.62 sec                                               | 2.48 sec: 1.06x faster                                        |
| logging_format          | 6.68 us                                                | 6.33 us: 1.06x faster                                         |
| raytrace                | 297 ms                                                 | 281 ms: 1.06x faster                                          |
| fannkuch                | 388 ms                                                 | 368 ms: 1.05x faster                                          |
| logging_simple          | 6.03 us                                                | 5.73 us: 1.05x faster                                         |
| scimark_monte_carlo     | 68.1 ms                                                | 64.7 ms: 1.05x faster                                         |
| pyflate                 | 418 ms                                                 | 398 ms: 1.05x faster                                          |
| bench_thread_pool       | 819 us                                                 | 783 us: 1.05x faster                                          |
| pprint_safe_repr        | 701 ms                                                 | 671 ms: 1.05x faster                                          |
| sympy_integrate         | 21.0 ms                                                | 20.1 ms: 1.05x faster                                         |
| pidigits                | 198 ms                                                 | 189 ms: 1.05x faster                                          |
| 2to3                    | 259 ms                                                 | 248 ms: 1.04x faster                                          |
| deepcopy                | 342 us                                                 | 328 us: 1.04x faster                                          |
| sympy_str               | 290 ms                                                 | 278 ms: 1.04x faster                                          |
| async_tree_none         | 526 ms                                                 | 505 ms: 1.04x faster                                          |
| coverage                | 100 ms                                                 | 96.1 ms: 1.04x faster                                         |
| spectral_norm           | 100 ms                                                 | 96.2 ms: 1.04x faster                                         |
| pickle_dict             | 31.1 us                                                | 30.0 us: 1.04x faster                                         |
| docutils                | 2.63 sec                                               | 2.53 sec: 1.04x faster                                        |
| nqueens                 | 83.4 ms                                                | 80.3 ms: 1.04x faster                                         |
| meteor_contest          | 107 ms                                                 | 103 ms: 1.04x faster                                          |
| pickle_list             | 4.11 us                                                | 3.97 us: 1.03x faster                                         |
| genshi_text             | 21.6 ms                                                | 20.8 ms: 1.03x faster                                         |
| async_tree_io           | 1.30 sec                                               | 1.26 sec: 1.03x faster                                        |
| async_tree_memoization  | 627 ms                                                 | 611 ms: 1.03x faster                                          |
| mako                    | 10.1 ms                                                | 9.83 ms: 1.03x faster                                         |
| telco                   | 6.58 ms                                                | 6.42 ms: 1.03x faster                                         |
| sqlalchemy_imperative   | 17.9 ms                                                | 17.5 ms: 1.02x faster                                         |
| chameleon               | 6.47 ms                                                | 6.32 ms: 1.02x faster                                         |
| tornado_http            | 96.3 ms                                                | 94.3 ms: 1.02x faster                                         |
| thrift                  | 756 us                                                 | 742 us: 1.02x faster                                          |
| scimark_lu              | 110 ms                                                 | 108 ms: 1.02x faster                                          |
| sympy_sum               | 167 ms                                                 | 164 ms: 1.02x faster                                          |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.01x faster                                          |
| crypto_pyaes            | 74.7 ms                                                | 73.7 ms: 1.01x faster                                         |
| create_gc_cycles        | 1.49 ms                                                | 1.47 ms: 1.01x faster                                         |
| regex_v8                | 22.0 ms                                                | 21.8 ms: 1.01x faster                                         |
| deepcopy_reduce         | 2.94 us                                                | 2.96 us: 1.01x slower                                         |
| nbody                   | 93.1 ms                                                | 94.0 ms: 1.01x slower                                         |
| sqlglot_transpile       | 1.70 ms                                                | 1.72 ms: 1.01x slower                                         |
| regex_dna               | 204 ms                                                 | 207 ms: 1.02x slower                                          |
| sqlglot_parse           | 1.40 ms                                                | 1.44 ms: 1.03x slower                                         |
| xml_etree_process       | 53.9 ms                                                | 55.5 ms: 1.03x slower                                         |
| gc_traversal            | 4.02 ms                                                | 4.18 ms: 1.04x slower                                         |
| sqlite_synth            | 2.52 us                                                | 2.63 us: 1.04x slower                                         |
| unpickle_list           | 4.91 us                                                | 5.13 us: 1.05x slower                                         |
| python_startup          | 8.52 ms                                                | 8.96 ms: 1.05x slower                                         |
| xml_etree_generate      | 76.2 ms                                                | 80.6 ms: 1.06x slower                                         |
| python_startup_no_site  | 6.01 ms                                                | 6.50 ms: 1.08x slower                                         |
| async_generators        | 368 ms                                                 | 417 ms: 1.13x slower                                          |
| dask                    | 360 ms                                                 | 498 ms: 1.38x slower                                          |
| Geometric mean          | (ref)                                                  | 1.05x faster                                                  |

Benchmark hidden because not significant (10): unpickle, sqlalchemy_declarative, unpack_sequence, pickle, dulwich_log, bench_mp_pool, async_tree_cpu_io_mixed, pathlib, django_template, djangocms
Ignored benchmarks (7) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x
