# Results vs. 3.13.0

- fork: python
- ref: 2a66dd33dfc0b845042d
- machine: linux-x86_64
- commit hash: 2a66dd3
- commit date: 2024-12-20
- overall geometric mean: 1.053x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 283 ms: 1.04x faster                                                         |
| docutils       | 2.83 sec                                                     | 2.90 sec: 1.03x slower                                                       |
| html5lib       | 73.5 ms                                                      | 67.2 ms: 1.09x faster                                                        |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                 |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 335 ms: 1.39x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 634 ms: 1.31x faster                                                         |
| async_tree_io              | 843 ms                                                       | 649 ms: 1.30x faster                                                         |
| async_tree_none            | 376 ms                                                       | 292 ms: 1.29x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 357 ms: 1.27x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 274 ms: 1.26x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 519 ms: 1.16x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 505 ms: 1.15x faster                                                         |
| async_generators           | 457 ms                                                       | 435 ms: 1.05x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 20.7 ms: 1.04x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.20x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 76.3 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                 |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.20 ms: 1.15x faster                                                        |
| regex_compile  | 143 ms                                                       | 136 ms: 1.05x faster                                                         |
| regex_dna      | 247 ms                                                       | 238 ms: 1.04x faster                                                         |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                 |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.08 sec: 1.18x faster                                                       |
| xml_etree_parse      | 150 ms                                                       | 135 ms: 1.11x faster                                                         |
| xml_etree_iterparse  | 103 ms                                                       | 95.6 ms: 1.08x faster                                                        |
| unpickle_pure_python | 217 us                                                       | 202 us: 1.07x faster                                                         |
| json_loads           | 24.7 us                                                      | 23.9 us: 1.03x faster                                                        |
| xml_etree_process    | 61.2 ms                                                      | 59.6 ms: 1.03x faster                                                        |
| xml_etree_generate   | 86.5 ms                                                      | 84.3 ms: 1.03x faster                                                        |
| pickle_pure_python   | 323 us                                                       | 327 us: 1.01x slower                                                         |
| json_dumps           | 11.1 ms                                                      | 11.5 ms: 1.04x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.05x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.96 ms                                                      | 9.09 ms: 1.02x slower                                                        |
| python_startup         | 15.9 ms                                                      | 16.2 ms: 1.02x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.02x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 24.4 ms: 1.07x faster                                                        |
| genshi_xml      | 57.1 ms                                                      | 55.1 ms: 1.04x faster                                                        |
| django_template | 36.4 ms                                                      | 35.5 ms: 1.02x faster                                                        |
| mako            | 10.4 ms                                                      | 11.0 ms: 1.06x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 335 ms: 1.39x faster                                                         |
| deepcopy                   | 392 us                                                       | 284 us: 1.38x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 634 ms: 1.31x faster                                                         |
| async_tree_io              | 843 ms                                                       | 649 ms: 1.30x faster                                                         |
| async_tree_none            | 376 ms                                                       | 292 ms: 1.29x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 357 ms: 1.27x faster                                                         |
| deepcopy_memo              | 38.6 us                                                      | 30.5 us: 1.27x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 274 ms: 1.26x faster                                                         |
| go                         | 162 ms                                                       | 129 ms: 1.26x faster                                                         |
| deepcopy_reduce            | 3.54 us                                                      | 2.90 us: 1.22x faster                                                        |
| tomli_loads                | 2.46 sec                                                     | 2.08 sec: 1.18x faster                                                       |
| generators                 | 33.6 ms                                                      | 28.8 ms: 1.17x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 519 ms: 1.16x faster                                                         |
| richards                   | 52.9 ms                                                      | 45.9 ms: 1.15x faster                                                        |
| richards_super             | 59.6 ms                                                      | 51.7 ms: 1.15x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 505 ms: 1.15x faster                                                         |
| regex_effbot               | 3.67 ms                                                      | 3.20 ms: 1.15x faster                                                        |
| telco                      | 8.79 ms                                                      | 7.81 ms: 1.13x faster                                                        |
| scimark_sor                | 123 ms                                                       | 110 ms: 1.12x faster                                                         |
| xml_etree_parse            | 150 ms                                                       | 135 ms: 1.11x faster                                                         |
| json                       | 5.69 ms                                                      | 5.14 ms: 1.11x faster                                                        |
| pyflate                    | 503 ms                                                       | 459 ms: 1.10x faster                                                         |
| html5lib                   | 73.5 ms                                                      | 67.2 ms: 1.09x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 4.67 sec: 1.09x faster                                                       |
| hexiom                     | 6.55 ms                                                      | 6.02 ms: 1.09x faster                                                        |
| pprint_pformat             | 1.72 sec                                                     | 1.58 sec: 1.09x faster                                                       |
| pathlib                    | 17.5 ms                                                      | 16.2 ms: 1.09x faster                                                        |
| pylint                     | 347 ms                                                       | 322 ms: 1.08x faster                                                         |
| pprint_safe_repr           | 843 ms                                                       | 783 ms: 1.08x faster                                                         |
| xml_etree_iterparse        | 103 ms                                                       | 95.6 ms: 1.08x faster                                                        |
| unpickle_pure_python       | 217 us                                                       | 202 us: 1.07x faster                                                         |
| genshi_text                | 26.2 ms                                                      | 24.4 ms: 1.07x faster                                                        |
| spectral_norm              | 97.0 ms                                                      | 90.4 ms: 1.07x faster                                                        |
| float                      | 81.3 ms                                                      | 76.3 ms: 1.07x faster                                                        |
| scimark_fft                | 328 ms                                                       | 308 ms: 1.06x faster                                                         |
| sqlglot_normalize          | 119 ms                                                       | 113 ms: 1.05x faster                                                         |
| async_generators           | 457 ms                                                       | 435 ms: 1.05x faster                                                         |
| regex_compile              | 143 ms                                                       | 136 ms: 1.05x faster                                                         |
| sqlglot_parse              | 1.40 ms                                                      | 1.34 ms: 1.05x faster                                                        |
| scimark_lu                 | 98.7 ms                                                      | 94.3 ms: 1.05x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 20.7 ms: 1.04x faster                                                        |
| thrift                     | 901 us                                                       | 866 us: 1.04x faster                                                         |
| regex_dna                  | 247 ms                                                       | 238 ms: 1.04x faster                                                         |
| 2to3                       | 293 ms                                                       | 283 ms: 1.04x faster                                                         |
| genshi_xml                 | 57.1 ms                                                      | 55.1 ms: 1.04x faster                                                        |
| shortest_path              | 460 ms                                                       | 445 ms: 1.03x faster                                                         |
| k_core                     | 2.17 sec                                                     | 2.10 sec: 1.03x faster                                                       |
| json_loads                 | 24.7 us                                                      | 23.9 us: 1.03x faster                                                        |
| sqlglot_optimize           | 59.3 ms                                                      | 57.3 ms: 1.03x faster                                                        |
| sqlglot_transpile          | 1.79 ms                                                      | 1.73 ms: 1.03x faster                                                        |
| nqueens                    | 90.7 ms                                                      | 87.9 ms: 1.03x faster                                                        |
| connected_components       | 432 ms                                                       | 421 ms: 1.03x faster                                                         |
| xml_etree_process          | 61.2 ms                                                      | 59.6 ms: 1.03x faster                                                        |
| xml_etree_generate         | 86.5 ms                                                      | 84.3 ms: 1.03x faster                                                        |
| coverage                   | 80.0 ms                                                      | 77.9 ms: 1.03x faster                                                        |
| fannkuch                   | 363 ms                                                       | 354 ms: 1.03x faster                                                         |
| django_template            | 36.4 ms                                                      | 35.5 ms: 1.02x faster                                                        |
| sqlalchemy_declarative     | 148 ms                                                       | 145 ms: 1.02x faster                                                         |
| meteor_contest             | 130 ms                                                       | 127 ms: 1.02x faster                                                         |
| scimark_monte_carlo        | 66.1 ms                                                      | 64.7 ms: 1.02x faster                                                        |
| sqlite_synth               | 2.91 us                                                      | 2.84 us: 1.02x faster                                                        |
| mdp                        | 2.54 sec                                                     | 2.50 sec: 1.01x faster                                                       |
| sympy_str                  | 298 ms                                                       | 295 ms: 1.01x faster                                                         |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.72 ms: 1.01x faster                                                        |
| sympy_expand               | 509 ms                                                       | 504 ms: 1.01x faster                                                         |
| logging_simple             | 6.39 us                                                      | 6.33 us: 1.01x faster                                                        |
| dulwich_log                | 68.2 ms                                                      | 68.5 ms: 1.00x slower                                                        |
| sqlalchemy_imperative      | 18.3 ms                                                      | 18.4 ms: 1.00x slower                                                        |
| logging_silent             | 97.9 ns                                                      | 98.4 ns: 1.01x slower                                                        |
| pycparser                  | 1.24 sec                                                     | 1.26 sec: 1.01x slower                                                       |
| pickle_pure_python         | 323 us                                                       | 327 us: 1.01x slower                                                         |
| python_startup_no_site     | 8.96 ms                                                      | 9.09 ms: 1.02x slower                                                        |
| chaos                      | 60.2 ms                                                      | 61.3 ms: 1.02x slower                                                        |
| python_startup             | 15.9 ms                                                      | 16.2 ms: 1.02x slower                                                        |
| docutils                   | 2.83 sec                                                     | 2.90 sec: 1.03x slower                                                       |
| create_gc_cycles           | 2.68 ms                                                      | 2.75 ms: 1.03x slower                                                        |
| raytrace                   | 273 ms                                                       | 281 ms: 1.03x slower                                                         |
| crypto_pyaes               | 73.3 ms                                                      | 75.6 ms: 1.03x slower                                                        |
| json_dumps                 | 11.1 ms                                                      | 11.5 ms: 1.04x slower                                                        |
| comprehensions             | 17.0 us                                                      | 17.8 us: 1.04x slower                                                        |
| mako                       | 10.4 ms                                                      | 11.0 ms: 1.06x slower                                                        |
| many_optionals             | 930 us                                                       | 1.04 ms: 1.12x slower                                                        |
| subparsers                 | 17.5 ms                                                      | 22.7 ms: 1.30x slower                                                        |
| gc_traversal               | 4.74 ms                                                      | 6.34 ms: 1.34x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 1.26 sec: 246.07x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.00x slower                                                                 |

Benchmark hidden because not significant (12): nbody, regex_v8, sphinx, djangocms, deltablue, asyncio_websockets, sympy_sum, pidigits, sympy_integrate, logging_format, typing_runtime_protocols, bench_thread_pool
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20241220-3.14.0a3+-2a66dd3/bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json: mypy2

- Geometric mean (including insignificant results): 1.053x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.02x