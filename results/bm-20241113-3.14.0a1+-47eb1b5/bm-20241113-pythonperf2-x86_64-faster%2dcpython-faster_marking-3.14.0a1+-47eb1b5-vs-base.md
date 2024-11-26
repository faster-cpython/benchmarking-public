# Results vs. base

- fork: faster-cpython
- ref: faster_marking
- machine: linux-x86_64
- commit hash: 47eb1b5
- commit date: 2024-11-13
- overall geometric mean: 1.023x faster
- HPT reliability: 89.59%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241109-pythonperf2-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1+-6293d00 | bm-20241113-pythonperf2-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 283 ms                                                                       | 289 ms: 1.02x slower                                                             |
| docutils       | 2.94 sec                                                                     | 2.88 sec: 1.02x faster                                                           |
| html5lib       | 71.2 ms                                                                      | 73.0 ms: 1.03x slower                                                            |
| sphinx         | 1.14 sec                                                                     | 1.11 sec: 1.03x faster                                                           |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241109-pythonperf2-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1+-6293d00 | bm-20241113-pythonperf2-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|----------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 863 ms                                                                       | 652 ms: 1.32x faster                                                             |
| async_tree_io              | 842 ms                                                                       | 653 ms: 1.29x faster                                                             |
| async_tree_memoization     | 404 ms                                                                       | 369 ms: 1.09x faster                                                             |
| async_tree_none            | 327 ms                                                                       | 304 ms: 1.07x faster                                                             |
| async_tree_cpu_io_mixed_tg | 559 ms                                                                       | 523 ms: 1.07x faster                                                             |
| async_tree_none_tg         | 320 ms                                                                       | 300 ms: 1.07x faster                                                             |
| async_tree_cpu_io_mixed    | 571 ms                                                                       | 537 ms: 1.06x faster                                                             |
| async_tree_memoization_tg  | 371 ms                                                                       | 357 ms: 1.04x faster                                                             |
| coroutines                 | 21.8 ms                                                                      | 21.2 ms: 1.03x faster                                                            |
| async_generators           | 452 ms                                                                       | 447 ms: 1.01x faster                                                             |
| Geometric mean             | (ref)                                                                        | 1.09x faster                                                                     |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241109-pythonperf2-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1+-6293d00 | bm-20241113-pythonperf2-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 89.0 ms                                                                      | 88.1 ms: 1.01x faster                                                            |
| float          | 81.1 ms                                                                      | 85.5 ms: 1.05x slower                                                            |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                                     |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241109-pythonperf2-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1+-6293d00 | bm-20241113-pythonperf2-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 25.6 ms                                                                      | 25.3 ms: 1.01x faster                                                            |
| regex_dna      | 245 ms                                                                       | 250 ms: 1.02x slower                                                             |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                                     |

Benchmark hidden because not significant (2): regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241109-pythonperf2-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1+-6293d00 | bm-20241113-pythonperf2-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|----------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 11.7 ms                                                                      | 11.6 ms: 1.01x faster                                                            |
| unpickle_pure_python | 216 us                                                                       | 215 us: 1.01x faster                                                             |
| json_loads           | 24.8 us                                                                      | 24.9 us: 1.00x slower                                                            |
| tomli_loads          | 2.46 sec                                                                     | 2.48 sec: 1.01x slower                                                           |
| pickle_pure_python   | 326 us                                                                       | 332 us: 1.02x slower                                                             |
| xml_etree_process    | 61.5 ms                                                                      | 62.8 ms: 1.02x slower                                                            |
| xml_etree_generate   | 85.5 ms                                                                      | 88.4 ms: 1.03x slower                                                            |
| xml_etree_parse      | 144 ms                                                                       | 166 ms: 1.15x slower                                                             |
| xml_etree_iterparse  | 101 ms                                                                       | 120 ms: 1.19x slower                                                             |
| Geometric mean       | (ref)                                                                        | 1.04x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241109-pythonperf2-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1+-6293d00 | bm-20241113-pythonperf2-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 9.03 ms                                                                      | 8.59 ms: 1.05x faster                                                            |
| python_startup         | 16.0 ms                                                                      | 15.5 ms: 1.03x faster                                                            |
| Geometric mean         | (ref)                                                                        | 1.04x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241109-pythonperf2-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1+-6293d00 | bm-20241113-pythonperf2-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|-----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_text     | 26.0 ms                                                                      | 24.3 ms: 1.07x faster                                                            |
| mako            | 10.8 ms                                                                      | 10.8 ms: 1.01x faster                                                            |
| django_template | 37.1 ms                                                                      | 37.4 ms: 1.01x slower                                                            |
| genshi_xml      | 55.2 ms                                                                      | 55.8 ms: 1.01x slower                                                            |
| Geometric mean  | (ref)                                                                        | 1.01x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241109-pythonperf2-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1+-6293d00 | bm-20241113-pythonperf2-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|----------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| gc_traversal               | 5.87 ms                                                                      | 1.97 ms: 2.98x faster                                                            |
| create_gc_cycles           | 3.02 ms                                                                      | 1.82 ms: 1.66x faster                                                            |
| k_core                     | 3.08 sec                                                                     | 2.04 sec: 1.51x faster                                                           |
| async_tree_io_tg           | 863 ms                                                                       | 652 ms: 1.32x faster                                                             |
| async_tree_io              | 842 ms                                                                       | 653 ms: 1.29x faster                                                             |
| pylint                     | 348 ms                                                                       | 306 ms: 1.14x faster                                                             |
| async_tree_memoization     | 404 ms                                                                       | 369 ms: 1.09x faster                                                             |
| async_tree_none            | 327 ms                                                                       | 304 ms: 1.07x faster                                                             |
| async_tree_cpu_io_mixed_tg | 559 ms                                                                       | 523 ms: 1.07x faster                                                             |
| genshi_text                | 26.0 ms                                                                      | 24.3 ms: 1.07x faster                                                            |
| async_tree_none_tg         | 320 ms                                                                       | 300 ms: 1.07x faster                                                             |
| async_tree_cpu_io_mixed    | 571 ms                                                                       | 537 ms: 1.06x faster                                                             |
| python_startup_no_site     | 9.03 ms                                                                      | 8.59 ms: 1.05x faster                                                            |
| async_tree_memoization_tg  | 371 ms                                                                       | 357 ms: 1.04x faster                                                             |
| python_startup             | 16.0 ms                                                                      | 15.5 ms: 1.03x faster                                                            |
| coroutines                 | 21.8 ms                                                                      | 21.2 ms: 1.03x faster                                                            |
| sphinx                     | 1.14 sec                                                                     | 1.11 sec: 1.03x faster                                                           |
| docutils                   | 2.94 sec                                                                     | 2.88 sec: 1.02x faster                                                           |
| raytrace                   | 285 ms                                                                       | 279 ms: 1.02x faster                                                             |
| deepcopy                   | 293 us                                                                       | 287 us: 1.02x faster                                                             |
| json                       | 5.19 ms                                                                      | 5.09 ms: 1.02x faster                                                            |
| richards_super             | 56.5 ms                                                                      | 55.5 ms: 1.02x faster                                                            |
| pprint_safe_repr           | 799 ms                                                                       | 788 ms: 1.01x faster                                                             |
| deepcopy_reduce            | 2.98 us                                                                      | 2.95 us: 1.01x faster                                                            |
| regex_v8                   | 25.6 ms                                                                      | 25.3 ms: 1.01x faster                                                            |
| async_generators           | 452 ms                                                                       | 447 ms: 1.01x faster                                                             |
| json_dumps                 | 11.7 ms                                                                      | 11.6 ms: 1.01x faster                                                            |
| telco                      | 8.11 ms                                                                      | 8.03 ms: 1.01x faster                                                            |
| nbody                      | 89.0 ms                                                                      | 88.1 ms: 1.01x faster                                                            |
| crypto_pyaes               | 74.3 ms                                                                      | 73.5 ms: 1.01x faster                                                            |
| pprint_pformat             | 1.60 sec                                                                     | 1.59 sec: 1.01x faster                                                           |
| mako                       | 10.8 ms                                                                      | 10.8 ms: 1.01x faster                                                            |
| deepcopy_memo              | 29.7 us                                                                      | 29.5 us: 1.01x faster                                                            |
| unpickle_pure_python       | 216 us                                                                       | 215 us: 1.01x faster                                                             |
| shortest_path              | 456 ms                                                                       | 456 ms: 1.00x slower                                                             |
| sympy_integrate            | 23.3 ms                                                                      | 23.3 ms: 1.00x slower                                                            |
| json_loads                 | 24.8 us                                                                      | 24.9 us: 1.00x slower                                                            |
| mdp                        | 2.51 sec                                                                     | 2.52 sec: 1.01x slower                                                           |
| tomli_loads                | 2.46 sec                                                                     | 2.48 sec: 1.01x slower                                                           |
| django_template            | 37.1 ms                                                                      | 37.4 ms: 1.01x slower                                                            |
| logging_simple             | 6.36 us                                                                      | 6.42 us: 1.01x slower                                                            |
| go                         | 133 ms                                                                       | 135 ms: 1.01x slower                                                             |
| sympy_expand               | 498 ms                                                                       | 503 ms: 1.01x slower                                                             |
| genshi_xml                 | 55.2 ms                                                                      | 55.8 ms: 1.01x slower                                                            |
| hexiom                     | 6.19 ms                                                                      | 6.25 ms: 1.01x slower                                                            |
| spectral_norm              | 95.1 ms                                                                      | 96.2 ms: 1.01x slower                                                            |
| meteor_contest             | 125 ms                                                                       | 126 ms: 1.01x slower                                                             |
| sqlglot_transpile          | 1.80 ms                                                                      | 1.82 ms: 1.01x slower                                                            |
| pyflate                    | 484 ms                                                                       | 491 ms: 1.02x slower                                                             |
| scimark_lu                 | 95.1 ms                                                                      | 96.6 ms: 1.02x slower                                                            |
| pathlib                    | 15.9 ms                                                                      | 16.2 ms: 1.02x slower                                                            |
| scimark_monte_carlo        | 65.2 ms                                                                      | 66.3 ms: 1.02x slower                                                            |
| pickle_pure_python         | 326 us                                                                       | 332 us: 1.02x slower                                                             |
| comprehensions             | 17.5 us                                                                      | 17.8 us: 1.02x slower                                                            |
| scimark_fft                | 309 ms                                                                       | 315 ms: 1.02x slower                                                             |
| regex_dna                  | 245 ms                                                                       | 250 ms: 1.02x slower                                                             |
| xml_etree_process          | 61.5 ms                                                                      | 62.8 ms: 1.02x slower                                                            |
| sqlglot_normalize          | 120 ms                                                                       | 122 ms: 1.02x slower                                                             |
| 2to3                       | 283 ms                                                                       | 289 ms: 1.02x slower                                                             |
| logging_silent             | 99.3 ns                                                                      | 102 ns: 1.02x slower                                                             |
| logging_format             | 6.93 us                                                                      | 7.09 us: 1.02x slower                                                            |
| sqlglot_parse              | 1.41 ms                                                                      | 1.45 ms: 1.02x slower                                                            |
| pycparser                  | 1.21 sec                                                                     | 1.24 sec: 1.03x slower                                                           |
| html5lib                   | 71.2 ms                                                                      | 73.0 ms: 1.03x slower                                                            |
| many_optionals             | 1.02 ms                                                                      | 1.05 ms: 1.03x slower                                                            |
| sqlglot_optimize           | 59.2 ms                                                                      | 61.0 ms: 1.03x slower                                                            |
| nqueens                    | 88.6 ms                                                                      | 91.3 ms: 1.03x slower                                                            |
| chaos                      | 60.8 ms                                                                      | 62.8 ms: 1.03x slower                                                            |
| scimark_sparse_mat_mult    | 4.67 ms                                                                      | 4.83 ms: 1.03x slower                                                            |
| xml_etree_generate         | 85.5 ms                                                                      | 88.4 ms: 1.03x slower                                                            |
| generators                 | 28.6 ms                                                                      | 29.6 ms: 1.03x slower                                                            |
| coverage                   | 79.3 ms                                                                      | 82.6 ms: 1.04x slower                                                            |
| deltablue                  | 3.43 ms                                                                      | 3.60 ms: 1.05x slower                                                            |
| float                      | 81.1 ms                                                                      | 85.5 ms: 1.05x slower                                                            |
| subparsers                 | 22.8 ms                                                                      | 24.3 ms: 1.06x slower                                                            |
| bpe_tokeniser              | 4.82 sec                                                                     | 5.18 sec: 1.07x slower                                                           |
| scimark_sor                | 108 ms                                                                       | 119 ms: 1.10x slower                                                             |
| xml_etree_parse            | 144 ms                                                                       | 166 ms: 1.15x slower                                                             |
| xml_etree_iterparse        | 101 ms                                                                       | 120 ms: 1.19x slower                                                             |
| Geometric mean             | (ref)                                                                        | 1.02x faster                                                                     |

Benchmark hidden because not significant (18): bench_mp_pool, sqlalchemy_imperative, asyncio_websockets, dulwich_log, typing_runtime_protocols, connected_components, pidigits, regex_compile, richards, sympy_str, thrift, regex_effbot, sympy_sum, sqlalchemy_declarative, fannkuch, djangocms, sqlite_synth, bench_thread_pool

- Geometric mean (including insignificant results): 1.023x faster
# HPT report

- Reliability score: 89.59% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.98x