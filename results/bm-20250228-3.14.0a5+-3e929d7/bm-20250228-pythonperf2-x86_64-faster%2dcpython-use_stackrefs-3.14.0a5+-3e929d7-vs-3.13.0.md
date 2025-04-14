# Results vs. 3.13.0

- fork: faster-cpython
- ref: use_stackrefs
- machine: linux-x86_64
- commit hash: 3e929d7
- commit date: 2025-02-28
- overall geometric mean: 1.035x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 290 ms: 1.01x faster                                                            |
| docutils       | 2.83 sec                                                     | 2.91 sec: 1.03x slower                                                          |
| html5lib       | 73.5 ms                                                      | 69.3 ms: 1.06x faster                                                           |
| sphinx         | 1.12 sec                                                     | 1.11 sec: 1.01x faster                                                          |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 338 ms: 1.38x faster                                                            |
| async_tree_io              | 843 ms                                                       | 646 ms: 1.30x faster                                                            |
| async_tree_none            | 376 ms                                                       | 291 ms: 1.29x faster                                                            |
| async_tree_memoization     | 453 ms                                                       | 351 ms: 1.29x faster                                                            |
| async_tree_io_tg           | 831 ms                                                       | 650 ms: 1.28x faster                                                            |
| async_tree_none_tg         | 346 ms                                                       | 279 ms: 1.24x faster                                                            |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 520 ms: 1.16x faster                                                            |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 510 ms: 1.14x faster                                                            |
| async_generators           | 457 ms                                                       | 419 ms: 1.09x faster                                                            |
| coroutines                 | 21.6 ms                                                      | 21.0 ms: 1.03x faster                                                           |
| asyncio_websockets         | 388 ms                                                       | 386 ms: 1.01x faster                                                            |
| Geometric mean             | (ref)                                                        | 1.20x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 70.9 ms: 1.15x faster                                                           |
| pidigits       | 252 ms                                                       | 255 ms: 1.01x slower                                                            |
| nbody          | 89.3 ms                                                      | 105 ms: 1.18x slower                                                            |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.14 ms: 1.17x faster                                                           |
| regex_compile  | 143 ms                                                       | 137 ms: 1.04x faster                                                            |
| regex_v8       | 26.1 ms                                                      | 25.3 ms: 1.03x faster                                                           |
| regex_dna      | 247 ms                                                       | 245 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.16 sec: 1.14x faster                                                          |
| xml_etree_parse      | 150 ms                                                       | 143 ms: 1.05x faster                                                            |
| xml_etree_process    | 61.2 ms                                                      | 59.2 ms: 1.03x faster                                                           |
| xml_etree_iterparse  | 103 ms                                                       | 99.7 ms: 1.03x faster                                                           |
| xml_etree_generate   | 86.5 ms                                                      | 84.1 ms: 1.03x faster                                                           |
| unpickle_pure_python | 217 us                                                       | 221 us: 1.02x slower                                                            |
| json_dumps           | 11.1 ms                                                      | 11.4 ms: 1.02x slower                                                           |
| json_loads           | 24.7 us                                                      | 25.5 us: 1.03x slower                                                           |
| pickle_pure_python   | 323 us                                                       | 334 us: 1.04x slower                                                            |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 8.96 ms                                                      | 9.14 ms: 1.02x slower                                                           |
| python_startup         | 15.9 ms                                                      | 16.3 ms: 1.02x slower                                                           |
| Geometric mean         | (ref)                                                        | 1.02x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 24.2 ms: 1.08x faster                                                           |
| genshi_xml      | 57.1 ms                                                      | 56.3 ms: 1.01x faster                                                           |
| django_template | 36.4 ms                                                      | 36.0 ms: 1.01x faster                                                           |
| mako            | 10.4 ms                                                      | 11.3 ms: 1.09x slower                                                           |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 338 ms: 1.38x faster                                                            |
| deepcopy                   | 392 us                                                       | 289 us: 1.36x faster                                                            |
| deepcopy_memo              | 38.6 us                                                      | 29.1 us: 1.33x faster                                                           |
| async_tree_io              | 843 ms                                                       | 646 ms: 1.30x faster                                                            |
| async_tree_none            | 376 ms                                                       | 291 ms: 1.29x faster                                                            |
| async_tree_memoization     | 453 ms                                                       | 351 ms: 1.29x faster                                                            |
| async_tree_io_tg           | 831 ms                                                       | 650 ms: 1.28x faster                                                            |
| async_tree_none_tg         | 346 ms                                                       | 279 ms: 1.24x faster                                                            |
| go                         | 162 ms                                                       | 134 ms: 1.22x faster                                                            |
| deepcopy_reduce            | 3.54 us                                                      | 3.01 us: 1.18x faster                                                           |
| regex_effbot               | 3.67 ms                                                      | 3.14 ms: 1.17x faster                                                           |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 520 ms: 1.16x faster                                                            |
| generators                 | 33.6 ms                                                      | 29.2 ms: 1.15x faster                                                           |
| float                      | 81.3 ms                                                      | 70.9 ms: 1.15x faster                                                           |
| pyflate                    | 503 ms                                                       | 441 ms: 1.14x faster                                                            |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 510 ms: 1.14x faster                                                            |
| tomli_loads                | 2.46 sec                                                     | 2.16 sec: 1.14x faster                                                          |
| scimark_sor                | 123 ms                                                       | 110 ms: 1.12x faster                                                            |
| richards                   | 52.9 ms                                                      | 47.9 ms: 1.10x faster                                                           |
| async_generators           | 457 ms                                                       | 419 ms: 1.09x faster                                                            |
| pylint                     | 347 ms                                                       | 319 ms: 1.09x faster                                                            |
| richards_super             | 59.6 ms                                                      | 54.8 ms: 1.09x faster                                                           |
| genshi_text                | 26.2 ms                                                      | 24.2 ms: 1.08x faster                                                           |
| spectral_norm              | 97.0 ms                                                      | 90.5 ms: 1.07x faster                                                           |
| telco                      | 8.79 ms                                                      | 8.21 ms: 1.07x faster                                                           |
| bpe_tokeniser              | 5.09 sec                                                     | 4.77 sec: 1.07x faster                                                          |
| pprint_pformat             | 1.72 sec                                                     | 1.61 sec: 1.06x faster                                                          |
| json                       | 5.69 ms                                                      | 5.35 ms: 1.06x faster                                                           |
| html5lib                   | 73.5 ms                                                      | 69.3 ms: 1.06x faster                                                           |
| pprint_safe_repr           | 843 ms                                                       | 797 ms: 1.06x faster                                                            |
| xml_etree_parse            | 150 ms                                                       | 143 ms: 1.05x faster                                                            |
| thrift                     | 901 us                                                       | 860 us: 1.05x faster                                                            |
| hexiom                     | 6.55 ms                                                      | 6.27 ms: 1.05x faster                                                           |
| regex_compile              | 143 ms                                                       | 137 ms: 1.04x faster                                                            |
| logging_silent             | 97.9 ns                                                      | 94.1 ns: 1.04x faster                                                           |
| sqlite_synth               | 2.91 us                                                      | 2.80 us: 1.04x faster                                                           |
| regex_v8                   | 26.1 ms                                                      | 25.3 ms: 1.03x faster                                                           |
| xml_etree_process          | 61.2 ms                                                      | 59.2 ms: 1.03x faster                                                           |
| xml_etree_iterparse        | 103 ms                                                       | 99.7 ms: 1.03x faster                                                           |
| coroutines                 | 21.6 ms                                                      | 21.0 ms: 1.03x faster                                                           |
| xml_etree_generate         | 86.5 ms                                                      | 84.1 ms: 1.03x faster                                                           |
| k_core                     | 2.17 sec                                                     | 2.11 sec: 1.03x faster                                                          |
| pathlib                    | 17.5 ms                                                      | 17.1 ms: 1.03x faster                                                           |
| sqlglot_optimize           | 59.3 ms                                                      | 58.0 ms: 1.02x faster                                                           |
| shortest_path              | 460 ms                                                       | 450 ms: 1.02x faster                                                            |
| sqlalchemy_declarative     | 148 ms                                                       | 146 ms: 1.02x faster                                                            |
| sqlglot_normalize          | 119 ms                                                       | 117 ms: 1.02x faster                                                            |
| sympy_expand               | 509 ms                                                       | 500 ms: 1.02x faster                                                            |
| sqlglot_parse              | 1.40 ms                                                      | 1.38 ms: 1.02x faster                                                           |
| genshi_xml                 | 57.1 ms                                                      | 56.3 ms: 1.01x faster                                                           |
| sympy_str                  | 298 ms                                                       | 294 ms: 1.01x faster                                                            |
| meteor_contest             | 130 ms                                                       | 128 ms: 1.01x faster                                                            |
| mdp                        | 2.54 sec                                                     | 2.51 sec: 1.01x faster                                                          |
| 2to3                       | 293 ms                                                       | 290 ms: 1.01x faster                                                            |
| django_template            | 36.4 ms                                                      | 36.0 ms: 1.01x faster                                                           |
| sphinx                     | 1.12 sec                                                     | 1.11 sec: 1.01x faster                                                          |
| sqlglot_transpile          | 1.79 ms                                                      | 1.77 ms: 1.01x faster                                                           |
| regex_dna                  | 247 ms                                                       | 245 ms: 1.01x faster                                                            |
| sqlalchemy_imperative      | 18.3 ms                                                      | 18.2 ms: 1.01x faster                                                           |
| asyncio_websockets         | 388 ms                                                       | 386 ms: 1.01x faster                                                            |
| connected_components       | 432 ms                                                       | 430 ms: 1.01x faster                                                            |
| sympy_integrate            | 23.6 ms                                                      | 23.4 ms: 1.00x faster                                                           |
| scimark_monte_carlo        | 66.1 ms                                                      | 65.8 ms: 1.00x faster                                                           |
| sympy_sum                  | 155 ms                                                       | 154 ms: 1.00x faster                                                            |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.80 ms: 1.01x slower                                                           |
| dulwich_log                | 68.2 ms                                                      | 68.6 ms: 1.01x slower                                                           |
| pidigits                   | 252 ms                                                       | 255 ms: 1.01x slower                                                            |
| unpickle_pure_python       | 217 us                                                       | 221 us: 1.02x slower                                                            |
| json_dumps                 | 11.1 ms                                                      | 11.4 ms: 1.02x slower                                                           |
| python_startup_no_site     | 8.96 ms                                                      | 9.14 ms: 1.02x slower                                                           |
| logging_simple             | 6.39 us                                                      | 6.53 us: 1.02x slower                                                           |
| python_startup             | 15.9 ms                                                      | 16.3 ms: 1.02x slower                                                           |
| typing_runtime_protocols   | 169 us                                                       | 173 us: 1.02x slower                                                            |
| docutils                   | 2.83 sec                                                     | 2.91 sec: 1.03x slower                                                          |
| pycparser                  | 1.24 sec                                                     | 1.28 sec: 1.03x slower                                                          |
| bench_thread_pool          | 942 us                                                       | 970 us: 1.03x slower                                                            |
| scimark_lu                 | 98.7 ms                                                      | 102 ms: 1.03x slower                                                            |
| logging_format             | 6.94 us                                                      | 7.17 us: 1.03x slower                                                           |
| scimark_fft                | 328 ms                                                       | 339 ms: 1.03x slower                                                            |
| json_loads                 | 24.7 us                                                      | 25.5 us: 1.03x slower                                                           |
| pickle_pure_python         | 323 us                                                       | 334 us: 1.04x slower                                                            |
| fannkuch                   | 363 ms                                                       | 377 ms: 1.04x slower                                                            |
| nqueens                    | 90.7 ms                                                      | 94.3 ms: 1.04x slower                                                           |
| create_gc_cycles           | 2.68 ms                                                      | 2.79 ms: 1.04x slower                                                           |
| comprehensions             | 17.0 us                                                      | 17.8 us: 1.04x slower                                                           |
| coverage                   | 80.0 ms                                                      | 83.9 ms: 1.05x slower                                                           |
| raytrace                   | 273 ms                                                       | 289 ms: 1.06x slower                                                            |
| chaos                      | 60.2 ms                                                      | 65.2 ms: 1.08x slower                                                           |
| mako                       | 10.4 ms                                                      | 11.3 ms: 1.09x slower                                                           |
| many_optionals             | 930 us                                                       | 1.03 ms: 1.10x slower                                                           |
| crypto_pyaes               | 73.3 ms                                                      | 84.2 ms: 1.15x slower                                                           |
| nbody                      | 89.3 ms                                                      | 105 ms: 1.18x slower                                                            |
| subparsers                 | 17.5 ms                                                      | 23.3 ms: 1.33x slower                                                           |
| gc_traversal               | 4.74 ms                                                      | 6.54 ms: 1.38x slower                                                           |
| bench_mp_pool              | 5.12 ms                                                      | 907 ms: 177.09x slower                                                          |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): deltablue
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.035x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x