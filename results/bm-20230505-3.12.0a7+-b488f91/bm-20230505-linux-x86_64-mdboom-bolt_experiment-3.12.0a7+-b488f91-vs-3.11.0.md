
# Results vs. 3.11.0

- fork: mdboom
- ref: bolt_experiment
- machine: linux-x86_64
- commit hash: b488f91
- commit date: 2023-05-05
- overall geometric mean: 1.01x slower \*
- HPT reliability: 96.49%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230505-linux-x86_64-mdboom-bolt_experiment-3.12.0a7+-b488f91 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 270 ms: 1.04x slower                                              |
| docutils       | 2.63 sec                                               | 2.73 sec: 1.04x slower                                            |
| tornado_http   | 96.3 ms                                                | 102 ms: 1.06x slower                                              |
| Geometric mean | (ref)                                                  | 1.05x slower                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230505-linux-x86_64-mdboom-bolt_experiment-3.12.0a7+-b488f91 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 87.7 ms: 1.06x faster                                             |
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                              |
| float          | 77.2 ms                                                | 81.6 ms: 1.06x slower                                             |
| Geometric mean | (ref)                                                  | 1.02x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230505-linux-x86_64-mdboom-bolt_experiment-3.12.0a7+-b488f91 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.81 ms: 1.05x faster                                             |
| regex_dna      | 204 ms                                                 | 203 ms: 1.00x faster                                              |
| regex_compile  | 138 ms                                                 | 146 ms: 1.06x slower                                              |
| Geometric mean | (ref)                                                  | 1.00x slower                                                      |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230505-linux-x86_64-mdboom-bolt_experiment-3.12.0a7+-b488f91 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.92 ms: 1.27x faster                                             |
| unpickle_pure_python | 228 us                                                 | 220 us: 1.04x faster                                              |
| json_loads           | 26.5 us                                                | 25.7 us: 1.03x faster                                             |
| xml_etree_parse      | 158 ms                                                 | 154 ms: 1.03x faster                                              |
| unpickle_list        | 4.91 us                                                | 4.88 us: 1.01x faster                                             |
| pickle_dict          | 31.1 us                                                | 31.7 us: 1.02x slower                                             |
| pickle               | 10.1 us                                                | 10.6 us: 1.06x slower                                             |
| pickle_pure_python   | 306 us                                                 | 323 us: 1.06x slower                                              |
| unpickle             | 13.7 us                                                | 15.0 us: 1.10x slower                                             |
| xml_etree_process    | 53.9 ms                                                | 59.7 ms: 1.11x slower                                             |
| pickle_list          | 4.11 us                                                | 4.57 us: 1.11x slower                                             |
| xml_etree_generate   | 76.2 ms                                                | 85.3 ms: 1.12x slower                                             |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                      |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230505-linux-x86_64-mdboom-bolt_experiment-3.12.0a7+-b488f91 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.14 ms: 1.07x slower                                             |
| python_startup_no_site | 6.01 ms                                                | 6.67 ms: 1.11x slower                                             |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230505-linux-x86_64-mdboom-bolt_experiment-3.12.0a7+-b488f91 |
|-----------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.9 ms: 1.08x slower                                             |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230505-linux-x86_64-mdboom-bolt_experiment-3.12.0a7+-b488f91 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 30.7 ms: 2.39x faster                                             |
| asyncio_tcp             | 922 ms                                                 | 510 ms: 1.81x faster                                              |
| json_dumps              | 12.6 ms                                                | 9.92 ms: 1.27x faster                                             |
| mypy2                   | 420 ms                                                 | 353 ms: 1.19x faster                                              |
| coroutines              | 25.5 ms                                                | 22.2 ms: 1.15x faster                                             |
| gc_traversal            | 4.02 ms                                                | 3.68 ms: 1.09x faster                                             |
| nbody                   | 93.1 ms                                                | 87.7 ms: 1.06x faster                                             |
| async_tree_none         | 526 ms                                                 | 500 ms: 1.05x faster                                              |
| regex_effbot            | 3.99 ms                                                | 3.81 ms: 1.05x faster                                             |
| pidigits                | 198 ms                                                 | 189 ms: 1.05x faster                                              |
| async_tree_io           | 1.30 sec                                               | 1.24 sec: 1.05x faster                                            |
| sqlglot_parse           | 1.40 ms                                                | 1.34 ms: 1.04x faster                                             |
| unpickle_pure_python    | 228 us                                                 | 220 us: 1.04x faster                                              |
| pycparser               | 1.18 sec                                               | 1.14 sec: 1.04x faster                                            |
| fannkuch                | 388 ms                                                 | 375 ms: 1.03x faster                                              |
| json_loads              | 26.5 us                                                | 25.7 us: 1.03x faster                                             |
| deltablue               | 3.67 ms                                                | 3.56 ms: 1.03x faster                                             |
| xml_etree_parse         | 158 ms                                                 | 154 ms: 1.03x faster                                              |
| richards                | 45.7 ms                                                | 44.6 ms: 1.03x faster                                             |
| async_tree_cpu_io_mixed | 739 ms                                                 | 723 ms: 1.02x faster                                              |
| meteor_contest          | 107 ms                                                 | 104 ms: 1.02x faster                                              |
| sqlglot_transpile       | 1.70 ms                                                | 1.67 ms: 1.02x faster                                             |
| go                      | 140 ms                                                 | 138 ms: 1.02x faster                                              |
| async_tree_memoization  | 627 ms                                                 | 617 ms: 1.02x faster                                              |
| nqueens                 | 83.4 ms                                                | 82.1 ms: 1.02x faster                                             |
| unpickle_list           | 4.91 us                                                | 4.88 us: 1.01x faster                                             |
| create_gc_cycles        | 1.49 ms                                                | 1.48 ms: 1.00x faster                                             |
| regex_dna               | 204 ms                                                 | 203 ms: 1.00x faster                                              |
| hexiom                  | 6.37 ms                                                | 6.41 ms: 1.01x slower                                             |
| chaos                   | 69.2 ms                                                | 69.8 ms: 1.01x slower                                             |
| pickle_dict             | 31.1 us                                                | 31.7 us: 1.02x slower                                             |
| bench_thread_pool       | 819 us                                                 | 837 us: 1.02x slower                                              |
| logging_silent          | 101 ns                                                 | 104 ns: 1.03x slower                                              |
| pathlib                 | 18.2 ms                                                | 18.8 ms: 1.03x slower                                             |
| coverage                | 100 ms                                                 | 103 ms: 1.03x slower                                              |
| deepcopy_memo           | 37.0 us                                                | 38.3 us: 1.04x slower                                             |
| telco                   | 6.58 ms                                                | 6.82 ms: 1.04x slower                                             |
| comprehensions          | 22.4 us                                                | 23.3 us: 1.04x slower                                             |
| docutils                | 2.63 sec                                               | 2.73 sec: 1.04x slower                                            |
| 2to3                    | 259 ms                                                 | 270 ms: 1.04x slower                                              |
| raytrace                | 297 ms                                                 | 310 ms: 1.04x slower                                              |
| sqlglot_optimize        | 53.1 ms                                                | 55.6 ms: 1.05x slower                                             |
| pprint_pformat          | 1.46 sec                                               | 1.53 sec: 1.05x slower                                            |
| sqlglot_normalize       | 108 ms                                                 | 113 ms: 1.05x slower                                              |
| scimark_sor             | 118 ms                                                 | 124 ms: 1.05x slower                                              |
| pickle                  | 10.1 us                                                | 10.6 us: 1.06x slower                                             |
| float                   | 77.2 ms                                                | 81.6 ms: 1.06x slower                                             |
| pickle_pure_python      | 306 us                                                 | 323 us: 1.06x slower                                              |
| regex_compile           | 138 ms                                                 | 146 ms: 1.06x slower                                              |
| scimark_lu              | 110 ms                                                 | 116 ms: 1.06x slower                                              |
| tornado_http            | 96.3 ms                                                | 102 ms: 1.06x slower                                              |
| deepcopy                | 342 us                                                 | 363 us: 1.06x slower                                              |
| logging_format          | 6.68 us                                                | 7.12 us: 1.06x slower                                             |
| sqlalchemy_declarative  | 138 ms                                                 | 147 ms: 1.07x slower                                              |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.80 ms: 1.07x slower                                             |
| pyflate                 | 418 ms                                                 | 447 ms: 1.07x slower                                              |
| pprint_safe_repr        | 701 ms                                                 | 750 ms: 1.07x slower                                              |
| python_startup          | 8.52 ms                                                | 9.14 ms: 1.07x slower                                             |
| dulwich_log             | 63.7 ms                                                | 68.3 ms: 1.07x slower                                             |
| logging_simple          | 6.03 us                                                | 6.47 us: 1.07x slower                                             |
| crypto_pyaes            | 74.7 ms                                                | 80.4 ms: 1.08x slower                                             |
| sqlalchemy_imperative   | 17.9 ms                                                | 19.3 ms: 1.08x slower                                             |
| mako                    | 10.1 ms                                                | 10.9 ms: 1.08x slower                                             |
| scimark_monte_carlo     | 68.1 ms                                                | 73.6 ms: 1.08x slower                                             |
| scimark_fft             | 328 ms                                                 | 355 ms: 1.08x slower                                              |
| unpack_sequence         | 43.1 ns                                                | 46.6 ns: 1.08x slower                                             |
| deepcopy_reduce         | 2.94 us                                                | 3.19 us: 1.09x slower                                             |
| unpickle                | 13.7 us                                                | 15.0 us: 1.10x slower                                             |
| sqlite_synth            | 2.52 us                                                | 2.79 us: 1.11x slower                                             |
| spectral_norm           | 100 ms                                                 | 111 ms: 1.11x slower                                              |
| xml_etree_process       | 53.9 ms                                                | 59.7 ms: 1.11x slower                                             |
| python_startup_no_site  | 6.01 ms                                                | 6.67 ms: 1.11x slower                                             |
| pickle_list             | 4.11 us                                                | 4.57 us: 1.11x slower                                             |
| xml_etree_generate      | 76.2 ms                                                | 85.3 ms: 1.12x slower                                             |
| async_generators        | 368 ms                                                 | 459 ms: 1.24x slower                                              |
| dask                    | 360 ms                                                 | 542 ms: 1.51x slower                                              |
| Geometric mean          | (ref)                                                  | 1.01x slower                                                      |

Benchmark hidden because not significant (5): regex_v8, mdp, xml_etree_iterparse, json, bench_mp_pool
Ignored benchmarks (19) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, richards_super, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 96.49% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
