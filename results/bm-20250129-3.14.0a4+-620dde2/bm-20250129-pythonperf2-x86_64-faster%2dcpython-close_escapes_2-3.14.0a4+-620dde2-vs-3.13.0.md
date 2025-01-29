# Results vs. 3.13.0

- fork: faster-cpython
- ref: close_escapes_2
- machine: linux-x86_64
- commit hash: 620dde2
- commit date: 2025-01-29
- overall geometric mean: 1.061x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-pythonperf2-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 283 ms: 1.04x faster                                                              |
| docutils       | 2.83 sec                                                     | 2.88 sec: 1.02x slower                                                            |
| html5lib       | 73.5 ms                                                      | 67.4 ms: 1.09x faster                                                             |
| sphinx         | 1.12 sec                                                     | 1.11 sec: 1.01x faster                                                            |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-pythonperf2-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 334 ms: 1.39x faster                                                              |
| async_tree_none            | 376 ms                                                       | 287 ms: 1.31x faster                                                              |
| async_tree_io              | 843 ms                                                       | 645 ms: 1.31x faster                                                              |
| async_tree_memoization     | 453 ms                                                       | 347 ms: 1.30x faster                                                              |
| async_tree_io_tg           | 831 ms                                                       | 648 ms: 1.28x faster                                                              |
| async_tree_none_tg         | 346 ms                                                       | 277 ms: 1.25x faster                                                              |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 515 ms: 1.17x faster                                                              |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 503 ms: 1.16x faster                                                              |
| async_generators           | 457 ms                                                       | 418 ms: 1.09x faster                                                              |
| coroutines                 | 21.6 ms                                                      | 20.8 ms: 1.04x faster                                                             |
| Geometric mean             | (ref)                                                        | 1.20x faster                                                                      |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-pythonperf2-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 69.3 ms: 1.17x faster                                                             |
| pidigits       | 252 ms                                                       | 254 ms: 1.01x slower                                                              |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                      |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-pythonperf2-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.14 ms: 1.17x faster                                                             |
| regex_compile  | 143 ms                                                       | 136 ms: 1.05x faster                                                              |
| regex_dna      | 247 ms                                                       | 237 ms: 1.04x faster                                                              |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                      |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-pythonperf2-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.06 sec: 1.20x faster                                                            |
| xml_etree_parse      | 150 ms                                                       | 137 ms: 1.09x faster                                                              |
| xml_etree_iterparse  | 103 ms                                                       | 96.4 ms: 1.07x faster                                                             |
| unpickle_pure_python | 217 us                                                       | 207 us: 1.05x faster                                                              |
| xml_etree_process    | 61.2 ms                                                      | 58.9 ms: 1.04x faster                                                             |
| xml_etree_generate   | 86.5 ms                                                      | 83.8 ms: 1.03x faster                                                             |
| pickle_pure_python   | 323 us                                                       | 326 us: 1.01x slower                                                              |
| json_dumps           | 11.1 ms                                                      | 11.6 ms: 1.05x slower                                                             |
| json_loads           | 24.7 us                                                      | 26.8 us: 1.09x slower                                                             |
| Geometric mean       | (ref)                                                        | 1.04x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-pythonperf2-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 8.96 ms                                                      | 8.98 ms: 1.00x slower                                                             |
| python_startup         | 15.9 ms                                                      | 16.0 ms: 1.00x slower                                                             |
| Geometric mean         | (ref)                                                        | 1.00x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-pythonperf2-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_text    | 26.2 ms                                                      | 23.4 ms: 1.12x faster                                                             |
| genshi_xml     | 57.1 ms                                                      | 52.6 ms: 1.08x faster                                                             |
| mako           | 10.4 ms                                                      | 10.8 ms: 1.05x slower                                                             |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                      |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-pythonperf2-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 334 ms: 1.39x faster                                                              |
| deepcopy                   | 392 us                                                       | 282 us: 1.39x faster                                                              |
| async_tree_none            | 376 ms                                                       | 287 ms: 1.31x faster                                                              |
| async_tree_io              | 843 ms                                                       | 645 ms: 1.31x faster                                                              |
| async_tree_memoization     | 453 ms                                                       | 347 ms: 1.30x faster                                                              |
| async_tree_io_tg           | 831 ms                                                       | 648 ms: 1.28x faster                                                              |
| go                         | 162 ms                                                       | 128 ms: 1.27x faster                                                              |
| deepcopy_memo              | 38.6 us                                                      | 30.7 us: 1.26x faster                                                             |
| async_tree_none_tg         | 346 ms                                                       | 277 ms: 1.25x faster                                                              |
| deepcopy_reduce            | 3.54 us                                                      | 2.91 us: 1.22x faster                                                             |
| tomli_loads                | 2.46 sec                                                     | 2.06 sec: 1.20x faster                                                            |
| generators                 | 33.6 ms                                                      | 28.3 ms: 1.19x faster                                                             |
| float                      | 81.3 ms                                                      | 69.3 ms: 1.17x faster                                                             |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 515 ms: 1.17x faster                                                              |
| regex_effbot               | 3.67 ms                                                      | 3.14 ms: 1.17x faster                                                             |
| richards_super             | 59.6 ms                                                      | 51.2 ms: 1.16x faster                                                             |
| spectral_norm              | 97.0 ms                                                      | 83.6 ms: 1.16x faster                                                             |
| richards                   | 52.9 ms                                                      | 45.7 ms: 1.16x faster                                                             |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 503 ms: 1.16x faster                                                              |
| scimark_sor                | 123 ms                                                       | 108 ms: 1.15x faster                                                              |
| genshi_text                | 26.2 ms                                                      | 23.4 ms: 1.12x faster                                                             |
| pyflate                    | 503 ms                                                       | 452 ms: 1.11x faster                                                              |
| telco                      | 8.79 ms                                                      | 7.96 ms: 1.10x faster                                                             |
| pylint                     | 347 ms                                                       | 315 ms: 1.10x faster                                                              |
| pathlib                    | 17.5 ms                                                      | 16.0 ms: 1.10x faster                                                             |
| xml_etree_parse            | 150 ms                                                       | 137 ms: 1.09x faster                                                              |
| async_generators           | 457 ms                                                       | 418 ms: 1.09x faster                                                              |
| html5lib                   | 73.5 ms                                                      | 67.4 ms: 1.09x faster                                                             |
| bpe_tokeniser              | 5.09 sec                                                     | 4.69 sec: 1.09x faster                                                            |
| genshi_xml                 | 57.1 ms                                                      | 52.6 ms: 1.08x faster                                                             |
| hexiom                     | 6.55 ms                                                      | 6.06 ms: 1.08x faster                                                             |
| scimark_fft                | 328 ms                                                       | 303 ms: 1.08x faster                                                              |
| xml_etree_iterparse        | 103 ms                                                       | 96.4 ms: 1.07x faster                                                             |
| pprint_pformat             | 1.72 sec                                                     | 1.62 sec: 1.06x faster                                                            |
| thrift                     | 901 us                                                       | 848 us: 1.06x faster                                                              |
| pprint_safe_repr           | 843 ms                                                       | 799 ms: 1.05x faster                                                              |
| sqlglot_parse              | 1.40 ms                                                      | 1.33 ms: 1.05x faster                                                             |
| unpickle_pure_python       | 217 us                                                       | 207 us: 1.05x faster                                                              |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.55 ms: 1.05x faster                                                             |
| shortest_path              | 460 ms                                                       | 439 ms: 1.05x faster                                                              |
| regex_compile              | 143 ms                                                       | 136 ms: 1.05x faster                                                              |
| coverage                   | 80.0 ms                                                      | 76.6 ms: 1.04x faster                                                             |
| sqlglot_transpile          | 1.79 ms                                                      | 1.72 ms: 1.04x faster                                                             |
| regex_dna                  | 247 ms                                                       | 237 ms: 1.04x faster                                                              |
| scimark_monte_carlo        | 66.1 ms                                                      | 63.5 ms: 1.04x faster                                                             |
| connected_components       | 432 ms                                                       | 416 ms: 1.04x faster                                                              |
| xml_etree_process          | 61.2 ms                                                      | 58.9 ms: 1.04x faster                                                             |
| coroutines                 | 21.6 ms                                                      | 20.8 ms: 1.04x faster                                                             |
| deltablue                  | 3.42 ms                                                      | 3.30 ms: 1.04x faster                                                             |
| logging_simple             | 6.39 us                                                      | 6.17 us: 1.04x faster                                                             |
| 2to3                       | 293 ms                                                       | 283 ms: 1.04x faster                                                              |
| sqlalchemy_declarative     | 148 ms                                                       | 143 ms: 1.03x faster                                                              |
| k_core                     | 2.17 sec                                                     | 2.10 sec: 1.03x faster                                                            |
| sympy_str                  | 298 ms                                                       | 289 ms: 1.03x faster                                                              |
| xml_etree_generate         | 86.5 ms                                                      | 83.8 ms: 1.03x faster                                                             |
| sqlalchemy_imperative      | 18.3 ms                                                      | 17.7 ms: 1.03x faster                                                             |
| sympy_expand               | 509 ms                                                       | 494 ms: 1.03x faster                                                              |
| pycparser                  | 1.24 sec                                                     | 1.21 sec: 1.03x faster                                                            |
| scimark_lu                 | 98.7 ms                                                      | 95.9 ms: 1.03x faster                                                             |
| json                       | 5.69 ms                                                      | 5.53 ms: 1.03x faster                                                             |
| dulwich_log                | 68.2 ms                                                      | 66.4 ms: 1.03x faster                                                             |
| sqlite_synth               | 2.91 us                                                      | 2.84 us: 1.02x faster                                                             |
| sqlglot_normalize          | 119 ms                                                       | 117 ms: 1.02x faster                                                              |
| sympy_sum                  | 155 ms                                                       | 151 ms: 1.02x faster                                                              |
| nqueens                    | 90.7 ms                                                      | 88.7 ms: 1.02x faster                                                             |
| meteor_contest             | 130 ms                                                       | 127 ms: 1.02x faster                                                              |
| bench_thread_pool          | 942 us                                                       | 923 us: 1.02x faster                                                              |
| sympy_integrate            | 23.6 ms                                                      | 23.1 ms: 1.02x faster                                                             |
| sphinx                     | 1.12 sec                                                     | 1.11 sec: 1.01x faster                                                            |
| sqlglot_optimize           | 59.3 ms                                                      | 58.5 ms: 1.01x faster                                                             |
| logging_silent             | 97.9 ns                                                      | 96.6 ns: 1.01x faster                                                             |
| raytrace                   | 273 ms                                                       | 270 ms: 1.01x faster                                                              |
| mdp                        | 2.54 sec                                                     | 2.52 sec: 1.01x faster                                                            |
| logging_format             | 6.94 us                                                      | 6.89 us: 1.01x faster                                                             |
| python_startup_no_site     | 8.96 ms                                                      | 8.98 ms: 1.00x slower                                                             |
| python_startup             | 15.9 ms                                                      | 16.0 ms: 1.00x slower                                                             |
| chaos                      | 60.2 ms                                                      | 60.5 ms: 1.00x slower                                                             |
| pidigits                   | 252 ms                                                       | 254 ms: 1.01x slower                                                              |
| pickle_pure_python         | 323 us                                                       | 326 us: 1.01x slower                                                              |
| crypto_pyaes               | 73.3 ms                                                      | 74.4 ms: 1.01x slower                                                             |
| comprehensions             | 17.0 us                                                      | 17.3 us: 1.02x slower                                                             |
| docutils                   | 2.83 sec                                                     | 2.88 sec: 1.02x slower                                                            |
| json_dumps                 | 11.1 ms                                                      | 11.6 ms: 1.05x slower                                                             |
| mako                       | 10.4 ms                                                      | 10.8 ms: 1.05x slower                                                             |
| create_gc_cycles           | 2.68 ms                                                      | 2.81 ms: 1.05x slower                                                             |
| json_loads                 | 24.7 us                                                      | 26.8 us: 1.09x slower                                                             |
| many_optionals             | 930 us                                                       | 1.02 ms: 1.10x slower                                                             |
| subparsers                 | 17.5 ms                                                      | 23.1 ms: 1.32x slower                                                             |
| gc_traversal               | 4.74 ms                                                      | 6.59 ms: 1.39x slower                                                             |
| bench_mp_pool              | 5.12 ms                                                      | 1.27 sec: 248.30x slower                                                          |
| Geometric mean             | (ref)                                                        | 1.00x faster                                                                      |

Benchmark hidden because not significant (6): regex_v8, django_template, asyncio_websockets, nbody, fannkuch, typing_runtime_protocols
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.061x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.02x