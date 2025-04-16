# Results vs. 3.13.0

- fork: faster-cpython
- ref: get_iter_stats
- machine: linux-x86_64
- commit hash: 10cd875
- commit date: 2025-04-16
- overall geometric mean: 1.076x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-10cd875 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 274 ms: 1.07x faster                                                             |
| docutils       | 2.83 sec                                                     | 2.85 sec: 1.01x slower                                                           |
| html5lib       | 73.5 ms                                                      | 65.4 ms: 1.12x faster                                                            |
| sphinx         | 1.12 sec                                                     | 1.10 sec: 1.03x faster                                                           |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-10cd875 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 336 ms: 1.39x faster                                                             |
| async_tree_memoization     | 453 ms                                                       | 328 ms: 1.38x faster                                                             |
| async_tree_io              | 843 ms                                                       | 629 ms: 1.34x faster                                                             |
| async_tree_none            | 376 ms                                                       | 284 ms: 1.33x faster                                                             |
| async_tree_io_tg           | 831 ms                                                       | 634 ms: 1.31x faster                                                             |
| async_tree_none_tg         | 346 ms                                                       | 272 ms: 1.27x faster                                                             |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 507 ms: 1.19x faster                                                             |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 504 ms: 1.15x faster                                                             |
| async_generators           | 457 ms                                                       | 413 ms: 1.11x faster                                                             |
| coroutines                 | 21.6 ms                                                      | 21.9 ms: 1.01x slower                                                            |
| Geometric mean             | (ref)                                                        | 1.22x faster                                                                     |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-10cd875 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 67.2 ms: 1.21x faster                                                            |
| pidigits       | 252 ms                                                       | 255 ms: 1.01x slower                                                             |
| nbody          | 89.3 ms                                                      | 94.9 ms: 1.06x slower                                                            |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-10cd875 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.13 ms: 1.17x faster                                                            |
| regex_compile  | 143 ms                                                       | 132 ms: 1.08x faster                                                             |
| regex_v8       | 26.1 ms                                                      | 24.5 ms: 1.06x faster                                                            |
| regex_dna      | 247 ms                                                       | 239 ms: 1.03x faster                                                             |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-10cd875 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.04 sec: 1.21x faster                                                           |
| xml_etree_parse      | 150 ms                                                       | 137 ms: 1.09x faster                                                             |
| xml_etree_iterparse  | 103 ms                                                       | 97.8 ms: 1.05x faster                                                            |
| xml_etree_process    | 61.2 ms                                                      | 58.9 ms: 1.04x faster                                                            |
| unpickle_pure_python | 217 us                                                       | 210 us: 1.04x faster                                                             |
| xml_etree_generate   | 86.5 ms                                                      | 84.4 ms: 1.03x faster                                                            |
| pickle_pure_python   | 323 us                                                       | 328 us: 1.01x slower                                                             |
| json_dumps           | 11.1 ms                                                      | 11.5 ms: 1.03x slower                                                            |
| json_loads           | 24.7 us                                                      | 26.6 us: 1.08x slower                                                            |
| Geometric mean       | (ref)                                                        | 1.03x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-10cd875 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 16.5 ms: 1.04x slower                                                            |
| python_startup_no_site | 8.96 ms                                                      | 10.5 ms: 1.17x slower                                                            |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-10cd875 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 22.6 ms: 1.16x faster                                                            |
| genshi_xml      | 57.1 ms                                                      | 51.7 ms: 1.10x faster                                                            |
| django_template | 36.4 ms                                                      | 35.4 ms: 1.03x faster                                                            |
| mako            | 10.4 ms                                                      | 10.9 ms: 1.05x slower                                                            |
| Geometric mean  | (ref)                                                        | 1.06x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-10cd875 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.27 sec: 2.00x faster                                                           |
| deepcopy                   | 392 us                                                       | 276 us: 1.42x faster                                                             |
| deepcopy_memo              | 38.6 us                                                      | 27.8 us: 1.39x faster                                                            |
| async_tree_memoization_tg  | 466 ms                                                       | 336 ms: 1.39x faster                                                             |
| async_tree_memoization     | 453 ms                                                       | 328 ms: 1.38x faster                                                             |
| async_tree_io              | 843 ms                                                       | 629 ms: 1.34x faster                                                             |
| async_tree_none            | 376 ms                                                       | 284 ms: 1.33x faster                                                             |
| go                         | 162 ms                                                       | 123 ms: 1.32x faster                                                             |
| async_tree_io_tg           | 831 ms                                                       | 634 ms: 1.31x faster                                                             |
| async_tree_none_tg         | 346 ms                                                       | 272 ms: 1.27x faster                                                             |
| deepcopy_reduce            | 3.54 us                                                      | 2.90 us: 1.22x faster                                                            |
| float                      | 81.3 ms                                                      | 67.2 ms: 1.21x faster                                                            |
| tomli_loads                | 2.46 sec                                                     | 2.04 sec: 1.21x faster                                                           |
| scimark_sor                | 123 ms                                                       | 103 ms: 1.20x faster                                                             |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 507 ms: 1.19x faster                                                             |
| richards                   | 52.9 ms                                                      | 44.9 ms: 1.18x faster                                                            |
| richards_super             | 59.6 ms                                                      | 50.6 ms: 1.18x faster                                                            |
| regex_effbot               | 3.67 ms                                                      | 3.13 ms: 1.17x faster                                                            |
| genshi_text                | 26.2 ms                                                      | 22.6 ms: 1.16x faster                                                            |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 504 ms: 1.15x faster                                                             |
| pyflate                    | 503 ms                                                       | 440 ms: 1.14x faster                                                             |
| telco                      | 8.79 ms                                                      | 7.68 ms: 1.14x faster                                                            |
| html5lib                   | 73.5 ms                                                      | 65.4 ms: 1.12x faster                                                            |
| generators                 | 33.6 ms                                                      | 30.0 ms: 1.12x faster                                                            |
| dulwich_log                | 68.2 ms                                                      | 61.0 ms: 1.12x faster                                                            |
| scimark_fft                | 328 ms                                                       | 295 ms: 1.11x faster                                                             |
| async_generators           | 457 ms                                                       | 413 ms: 1.11x faster                                                             |
| genshi_xml                 | 57.1 ms                                                      | 51.7 ms: 1.10x faster                                                            |
| deltablue                  | 3.42 ms                                                      | 3.10 ms: 1.10x faster                                                            |
| pprint_safe_repr           | 843 ms                                                       | 766 ms: 1.10x faster                                                             |
| pprint_pformat             | 1.72 sec                                                     | 1.57 sec: 1.10x faster                                                           |
| scimark_monte_carlo        | 66.1 ms                                                      | 60.3 ms: 1.10x faster                                                            |
| xml_etree_parse            | 150 ms                                                       | 137 ms: 1.09x faster                                                             |
| pylint                     | 347 ms                                                       | 319 ms: 1.09x faster                                                             |
| hexiom                     | 6.55 ms                                                      | 6.03 ms: 1.09x faster                                                            |
| spectral_norm              | 97.0 ms                                                      | 89.4 ms: 1.08x faster                                                            |
| regex_compile              | 143 ms                                                       | 132 ms: 1.08x faster                                                             |
| logging_silent             | 97.9 ns                                                      | 90.5 ns: 1.08x faster                                                            |
| bpe_tokeniser              | 5.09 sec                                                     | 4.74 sec: 1.07x faster                                                           |
| sympy_integrate            | 23.6 ms                                                      | 21.9 ms: 1.07x faster                                                            |
| 2to3                       | 293 ms                                                       | 274 ms: 1.07x faster                                                             |
| regex_v8                   | 26.1 ms                                                      | 24.5 ms: 1.06x faster                                                            |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.51 ms: 1.06x faster                                                            |
| xml_etree_iterparse        | 103 ms                                                       | 97.8 ms: 1.05x faster                                                            |
| sympy_expand               | 509 ms                                                       | 487 ms: 1.05x faster                                                             |
| meteor_contest             | 130 ms                                                       | 124 ms: 1.05x faster                                                             |
| sympy_str                  | 298 ms                                                       | 286 ms: 1.04x faster                                                             |
| logging_simple             | 6.39 us                                                      | 6.14 us: 1.04x faster                                                            |
| scimark_lu                 | 98.7 ms                                                      | 95.0 ms: 1.04x faster                                                            |
| pathlib                    | 17.5 ms                                                      | 16.9 ms: 1.04x faster                                                            |
| xml_etree_process          | 61.2 ms                                                      | 58.9 ms: 1.04x faster                                                            |
| unpickle_pure_python       | 217 us                                                       | 210 us: 1.04x faster                                                             |
| connected_components       | 432 ms                                                       | 418 ms: 1.03x faster                                                             |
| chaos                      | 60.2 ms                                                      | 58.3 ms: 1.03x faster                                                            |
| regex_dna                  | 247 ms                                                       | 239 ms: 1.03x faster                                                             |
| sympy_sum                  | 155 ms                                                       | 150 ms: 1.03x faster                                                             |
| k_core                     | 2.17 sec                                                     | 2.11 sec: 1.03x faster                                                           |
| django_template            | 36.4 ms                                                      | 35.4 ms: 1.03x faster                                                            |
| sphinx                     | 1.12 sec                                                     | 1.10 sec: 1.03x faster                                                           |
| xml_etree_generate         | 86.5 ms                                                      | 84.4 ms: 1.03x faster                                                            |
| shortest_path              | 460 ms                                                       | 449 ms: 1.02x faster                                                             |
| json                       | 5.69 ms                                                      | 5.57 ms: 1.02x faster                                                            |
| sqlalchemy_imperative      | 18.3 ms                                                      | 17.9 ms: 1.02x faster                                                            |
| typing_runtime_protocols   | 169 us                                                       | 166 us: 1.02x faster                                                             |
| pycparser                  | 1.24 sec                                                     | 1.22 sec: 1.02x faster                                                           |
| sqlite_synth               | 2.91 us                                                      | 2.86 us: 1.02x faster                                                            |
| logging_format             | 6.94 us                                                      | 6.87 us: 1.01x faster                                                            |
| sqlalchemy_declarative     | 148 ms                                                       | 148 ms: 1.01x faster                                                             |
| fannkuch                   | 363 ms                                                       | 362 ms: 1.00x faster                                                             |
| pidigits                   | 252 ms                                                       | 255 ms: 1.01x slower                                                             |
| docutils                   | 2.83 sec                                                     | 2.85 sec: 1.01x slower                                                           |
| coroutines                 | 21.6 ms                                                      | 21.9 ms: 1.01x slower                                                            |
| pickle_pure_python         | 323 us                                                       | 328 us: 1.01x slower                                                             |
| comprehensions             | 17.0 us                                                      | 17.3 us: 1.02x slower                                                            |
| nqueens                    | 90.7 ms                                                      | 93.0 ms: 1.03x slower                                                            |
| coverage                   | 80.0 ms                                                      | 82.3 ms: 1.03x slower                                                            |
| json_dumps                 | 11.1 ms                                                      | 11.5 ms: 1.03x slower                                                            |
| python_startup             | 15.9 ms                                                      | 16.5 ms: 1.04x slower                                                            |
| create_gc_cycles           | 2.68 ms                                                      | 2.79 ms: 1.04x slower                                                            |
| mako                       | 10.4 ms                                                      | 10.9 ms: 1.05x slower                                                            |
| nbody                      | 89.3 ms                                                      | 94.9 ms: 1.06x slower                                                            |
| json_loads                 | 24.7 us                                                      | 26.6 us: 1.08x slower                                                            |
| many_optionals             | 930 us                                                       | 1.00 ms: 1.08x slower                                                            |
| crypto_pyaes               | 73.3 ms                                                      | 79.7 ms: 1.09x slower                                                            |
| python_startup_no_site     | 8.96 ms                                                      | 10.5 ms: 1.17x slower                                                            |
| subparsers                 | 17.5 ms                                                      | 22.7 ms: 1.30x slower                                                            |
| gc_traversal               | 4.74 ms                                                      | 6.57 ms: 1.39x slower                                                            |
| bench_mp_pool              | 5.12 ms                                                      | 1.30 sec: 253.56x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                                     |

Benchmark hidden because not significant (3): asyncio_websockets, raytrace, bench_thread_pool
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250416-3.14.0a7+-10cd875/bm-20250416-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-10cd875.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.076x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.04x