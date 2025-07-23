# Results vs. 3.13.0

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-x86_64
- commit hash: a4de1bf
- commit date: 2025-07-22
- overall geometric mean: 1.125x slower
- HPT reliability: 99.81%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 328 ms: 1.12x slower                                                                |
| docutils       | 2.83 sec                                                     | 3.14 sec: 1.11x slower                                                              |
| html5lib       | 73.5 ms                                                      | 83.6 ms: 1.14x slower                                                               |
| sphinx         | 1.12 sec                                                     | 1.14 sec: 1.01x slower                                                              |
| Geometric mean | (ref)                                                        | 1.09x slower                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 355 ms: 1.31x faster                                                                |
| async_tree_none            | 376 ms                                                       | 297 ms: 1.27x faster                                                                |
| async_tree_io              | 843 ms                                                       | 665 ms: 1.27x faster                                                                |
| async_tree_memoization     | 453 ms                                                       | 358 ms: 1.27x faster                                                                |
| async_tree_io_tg           | 831 ms                                                       | 661 ms: 1.26x faster                                                                |
| async_tree_none_tg         | 346 ms                                                       | 292 ms: 1.19x faster                                                                |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 528 ms: 1.14x faster                                                                |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 530 ms: 1.10x faster                                                                |
| async_generators           | 457 ms                                                       | 459 ms: 1.01x slower                                                                |
| coroutines                 | 21.6 ms                                                      | 22.2 ms: 1.03x slower                                                               |
| Geometric mean             | (ref)                                                        | 1.15x faster                                                                        |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| pidigits       | 252 ms                                                       | 257 ms: 1.02x slower                                                                |
| float          | 81.3 ms                                                      | 102 ms: 1.26x slower                                                                |
| nbody          | 89.3 ms                                                      | 198 ms: 2.21x slower                                                                |
| Geometric mean | (ref)                                                        | 1.42x slower                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_v8       | 26.1 ms                                                      | 23.7 ms: 1.10x faster                                                               |
| regex_dna      | 247 ms                                                       | 226 ms: 1.09x faster                                                                |
| regex_effbot   | 3.67 ms                                                      | 3.60 ms: 1.02x faster                                                               |
| regex_compile  | 143 ms                                                       | 160 ms: 1.12x slower                                                                |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| xml_etree_parse      | 150 ms                                                       | 144 ms: 1.04x faster                                                                |
| xml_etree_iterparse  | 103 ms                                                       | 109 ms: 1.06x slower                                                                |
| json_loads           | 24.7 us                                                      | 26.2 us: 1.06x slower                                                               |
| tomli_loads          | 2.46 sec                                                     | 2.92 sec: 1.19x slower                                                              |
| xml_etree_process    | 61.2 ms                                                      | 76.9 ms: 1.26x slower                                                               |
| pickle_pure_python   | 323 us                                                       | 414 us: 1.28x slower                                                                |
| xml_etree_generate   | 86.5 ms                                                      | 111 ms: 1.28x slower                                                                |
| unpickle_pure_python | 217 us                                                       | 383 us: 1.76x slower                                                                |
| Geometric mean       | (ref)                                                        | 1.19x slower                                                                        |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 15.2 ms: 1.04x faster                                                               |
| python_startup_no_site | 8.96 ms                                                      | 8.69 ms: 1.03x faster                                                               |
| Geometric mean         | (ref)                                                        | 1.04x faster                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.7 ms: 1.11x faster                                                               |
| django_template | 36.4 ms                                                      | 35.7 ms: 1.02x faster                                                               |
| genshi_xml      | 57.1 ms                                                      | 56.5 ms: 1.01x faster                                                               |
| mako            | 10.4 ms                                                      | 18.4 ms: 1.78x slower                                                               |
| Geometric mean  | (ref)                                                        | 1.12x slower                                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.49 sec: 1.71x faster                                                              |
| deepcopy                   | 392 us                                                       | 277 us: 1.41x faster                                                                |
| deepcopy_memo              | 38.6 us                                                      | 27.7 us: 1.39x faster                                                               |
| async_tree_memoization_tg  | 466 ms                                                       | 355 ms: 1.31x faster                                                                |
| async_tree_none            | 376 ms                                                       | 297 ms: 1.27x faster                                                                |
| async_tree_io              | 843 ms                                                       | 665 ms: 1.27x faster                                                                |
| async_tree_memoization     | 453 ms                                                       | 358 ms: 1.27x faster                                                                |
| async_tree_io_tg           | 831 ms                                                       | 661 ms: 1.26x faster                                                                |
| scimark_sor                | 123 ms                                                       | 102 ms: 1.21x faster                                                                |
| deepcopy_reduce            | 3.54 us                                                      | 2.94 us: 1.20x faster                                                               |
| async_tree_none_tg         | 346 ms                                                       | 292 ms: 1.19x faster                                                                |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 528 ms: 1.14x faster                                                                |
| generators                 | 33.6 ms                                                      | 29.9 ms: 1.13x faster                                                               |
| genshi_text                | 26.2 ms                                                      | 23.7 ms: 1.11x faster                                                               |
| regex_v8                   | 26.1 ms                                                      | 23.7 ms: 1.10x faster                                                               |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 530 ms: 1.10x faster                                                                |
| dulwich_log                | 68.2 ms                                                      | 62.4 ms: 1.09x faster                                                               |
| regex_dna                  | 247 ms                                                       | 226 ms: 1.09x faster                                                                |
| thrift                     | 901 us                                                       | 833 us: 1.08x faster                                                                |
| logging_silent             | 97.9 ns                                                      | 92.2 ns: 1.06x faster                                                               |
| json                       | 5.69 ms                                                      | 5.36 ms: 1.06x faster                                                               |
| scimark_lu                 | 98.7 ms                                                      | 94.2 ms: 1.05x faster                                                               |
| python_startup             | 15.9 ms                                                      | 15.2 ms: 1.04x faster                                                               |
| xml_etree_parse            | 150 ms                                                       | 144 ms: 1.04x faster                                                                |
| pylint                     | 347 ms                                                       | 333 ms: 1.04x faster                                                                |
| logging_simple             | 6.39 us                                                      | 6.17 us: 1.04x faster                                                               |
| pathlib                    | 17.5 ms                                                      | 17.0 ms: 1.03x faster                                                               |
| python_startup_no_site     | 8.96 ms                                                      | 8.69 ms: 1.03x faster                                                               |
| logging_format             | 6.94 us                                                      | 6.74 us: 1.03x faster                                                               |
| regex_effbot               | 3.67 ms                                                      | 3.60 ms: 1.02x faster                                                               |
| django_template            | 36.4 ms                                                      | 35.7 ms: 1.02x faster                                                               |
| genshi_xml                 | 57.1 ms                                                      | 56.5 ms: 1.01x faster                                                               |
| richards                   | 52.9 ms                                                      | 52.6 ms: 1.01x faster                                                               |
| coverage                   | 80.0 ms                                                      | 79.6 ms: 1.00x faster                                                               |
| async_generators           | 457 ms                                                       | 459 ms: 1.01x slower                                                                |
| sphinx                     | 1.12 sec                                                     | 1.14 sec: 1.01x slower                                                              |
| pidigits                   | 252 ms                                                       | 257 ms: 1.02x slower                                                                |
| coroutines                 | 21.6 ms                                                      | 22.2 ms: 1.03x slower                                                               |
| sqlite_synth               | 2.91 us                                                      | 3.04 us: 1.05x slower                                                               |
| chaos                      | 60.2 ms                                                      | 63.2 ms: 1.05x slower                                                               |
| xml_etree_iterparse        | 103 ms                                                       | 109 ms: 1.06x slower                                                                |
| sympy_sum                  | 155 ms                                                       | 164 ms: 1.06x slower                                                                |
| json_loads                 | 24.7 us                                                      | 26.2 us: 1.06x slower                                                               |
| sympy_str                  | 298 ms                                                       | 318 ms: 1.07x slower                                                                |
| k_core                     | 2.17 sec                                                     | 2.32 sec: 1.07x slower                                                              |
| create_gc_cycles           | 2.68 ms                                                      | 2.90 ms: 1.08x slower                                                               |
| sympy_expand               | 509 ms                                                       | 559 ms: 1.10x slower                                                                |
| docutils                   | 2.83 sec                                                     | 3.14 sec: 1.11x slower                                                              |
| regex_compile              | 143 ms                                                       | 160 ms: 1.12x slower                                                                |
| 2to3                       | 293 ms                                                       | 328 ms: 1.12x slower                                                                |
| shortest_path              | 460 ms                                                       | 517 ms: 1.12x slower                                                                |
| html5lib                   | 73.5 ms                                                      | 83.6 ms: 1.14x slower                                                               |
| connected_components       | 432 ms                                                       | 503 ms: 1.16x slower                                                                |
| nqueens                    | 90.7 ms                                                      | 106 ms: 1.17x slower                                                                |
| tomli_loads                | 2.46 sec                                                     | 2.92 sec: 1.19x slower                                                              |
| pycparser                  | 1.24 sec                                                     | 1.51 sec: 1.21x slower                                                              |
| raytrace                   | 273 ms                                                       | 332 ms: 1.22x slower                                                                |
| typing_runtime_protocols   | 169 us                                                       | 208 us: 1.23x slower                                                                |
| meteor_contest             | 130 ms                                                       | 162 ms: 1.25x slower                                                                |
| xml_etree_process          | 61.2 ms                                                      | 76.9 ms: 1.26x slower                                                               |
| float                      | 81.3 ms                                                      | 102 ms: 1.26x slower                                                                |
| pyflate                    | 503 ms                                                       | 633 ms: 1.26x slower                                                                |
| pickle_pure_python         | 323 us                                                       | 414 us: 1.28x slower                                                                |
| xml_etree_generate         | 86.5 ms                                                      | 111 ms: 1.28x slower                                                                |
| bpe_tokeniser              | 5.09 sec                                                     | 6.58 sec: 1.29x slower                                                              |
| gc_traversal               | 4.74 ms                                                      | 6.27 ms: 1.32x slower                                                               |
| scimark_monte_carlo        | 66.1 ms                                                      | 89.0 ms: 1.35x slower                                                               |
| pprint_pformat             | 1.72 sec                                                     | 2.32 sec: 1.35x slower                                                              |
| pprint_safe_repr           | 843 ms                                                       | 1.14 sec: 1.35x slower                                                              |
| many_optionals             | 930 us                                                       | 1.28 ms: 1.37x slower                                                               |
| go                         | 162 ms                                                       | 228 ms: 1.40x slower                                                                |
| scimark_fft                | 328 ms                                                       | 479 ms: 1.46x slower                                                                |
| crypto_pyaes               | 73.3 ms                                                      | 109 ms: 1.49x slower                                                                |
| hexiom                     | 6.55 ms                                                      | 10.7 ms: 1.63x slower                                                               |
| deltablue                  | 3.42 ms                                                      | 5.71 ms: 1.67x slower                                                               |
| fannkuch                   | 363 ms                                                       | 622 ms: 1.71x slower                                                                |
| comprehensions             | 17.0 us                                                      | 29.2 us: 1.71x slower                                                               |
| unpickle_pure_python       | 217 us                                                       | 383 us: 1.76x slower                                                                |
| spectral_norm              | 97.0 ms                                                      | 172 ms: 1.77x slower                                                                |
| mako                       | 10.4 ms                                                      | 18.4 ms: 1.78x slower                                                               |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 8.59 ms: 1.80x slower                                                               |
| nbody                      | 89.3 ms                                                      | 198 ms: 2.21x slower                                                                |
| subparsers                 | 17.5 ms                                                      | 43.4 ms: 2.48x slower                                                               |
| telco                      | 8.79 ms                                                      | 159 ms: 18.06x slower                                                               |
| Geometric mean             | (ref)                                                        | 1.14x slower                                                                        |

Benchmark hidden because not significant (5): asyncio_websockets, djangocms, richards_super, sympy_integrate, json_dumps
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250722-3.15.0a0-a4de1bf-PYTHON_UOPS/bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.125x slower

# HPT report

- Reliability score: 99.81% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.11x