# Results vs. 3.13.0

- fork: faster-cpython
- ref: close_escapes
- machine: linux-x86_64
- commit hash: 08894e6
- commit date: 2025-01-22
- overall geometric mean: 1.058x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250122-pythonperf2-x86_64-faster%2dcpython-close_escapes-3.14.0a4+-08894e6 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 281 ms: 1.04x faster                                                            |
| docutils       | 2.83 sec                                                     | 2.89 sec: 1.02x slower                                                          |
| html5lib       | 73.5 ms                                                      | 68.5 ms: 1.07x faster                                                           |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250122-pythonperf2-x86_64-faster%2dcpython-close_escapes-3.14.0a4+-08894e6 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 327 ms: 1.42x faster                                                            |
| async_tree_none            | 376 ms                                                       | 276 ms: 1.36x faster                                                            |
| async_tree_io              | 843 ms                                                       | 624 ms: 1.35x faster                                                            |
| async_tree_io_tg           | 831 ms                                                       | 624 ms: 1.33x faster                                                            |
| async_tree_memoization     | 453 ms                                                       | 343 ms: 1.32x faster                                                            |
| async_tree_none_tg         | 346 ms                                                       | 267 ms: 1.30x faster                                                            |
| async_generators           | 457 ms                                                       | 377 ms: 1.21x faster                                                            |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 508 ms: 1.19x faster                                                            |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 498 ms: 1.17x faster                                                            |
| coroutines                 | 21.6 ms                                                      | 21.0 ms: 1.03x faster                                                           |
| asyncio_websockets         | 388 ms                                                       | 384 ms: 1.01x faster                                                            |
| Geometric mean             | (ref)                                                        | 1.24x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250122-pythonperf2-x86_64-faster%2dcpython-close_escapes-3.14.0a4+-08894e6 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 69.9 ms: 1.16x faster                                                           |
| pidigits       | 252 ms                                                       | 254 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                    |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250122-pythonperf2-x86_64-faster%2dcpython-close_escapes-3.14.0a4+-08894e6 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.17 ms: 1.16x faster                                                           |
| regex_compile  | 143 ms                                                       | 137 ms: 1.04x faster                                                            |
| regex_dna      | 247 ms                                                       | 248 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250122-pythonperf2-x86_64-faster%2dcpython-close_escapes-3.14.0a4+-08894e6 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.09 sec: 1.18x faster                                                          |
| xml_etree_parse      | 150 ms                                                       | 134 ms: 1.12x faster                                                            |
| xml_etree_iterparse  | 103 ms                                                       | 95.4 ms: 1.08x faster                                                           |
| xml_etree_generate   | 86.5 ms                                                      | 82.5 ms: 1.05x faster                                                           |
| unpickle_pure_python | 217 us                                                       | 219 us: 1.01x slower                                                            |
| xml_etree_process    | 61.2 ms                                                      | 61.8 ms: 1.01x slower                                                           |
| json_loads           | 24.7 us                                                      | 25.5 us: 1.03x slower                                                           |
| pickle_pure_python   | 323 us                                                       | 335 us: 1.04x slower                                                            |
| json_dumps           | 11.1 ms                                                      | 11.7 ms: 1.05x slower                                                           |
| Geometric mean       | (ref)                                                        | 1.03x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250122-pythonperf2-x86_64-faster%2dcpython-close_escapes-3.14.0a4+-08894e6 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 8.96 ms                                                      | 8.97 ms: 1.00x slower                                                           |
| python_startup         | 15.9 ms                                                      | 16.0 ms: 1.00x slower                                                           |
| Geometric mean         | (ref)                                                        | 1.00x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250122-pythonperf2-x86_64-faster%2dcpython-close_escapes-3.14.0a4+-08894e6 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 24.5 ms: 1.07x faster                                                           |
| genshi_xml      | 57.1 ms                                                      | 54.6 ms: 1.04x faster                                                           |
| django_template | 36.4 ms                                                      | 36.8 ms: 1.01x slower                                                           |
| mako            | 10.4 ms                                                      | 10.9 ms: 1.05x slower                                                           |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250122-pythonperf2-x86_64-faster%2dcpython-close_escapes-3.14.0a4+-08894e6 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 327 ms: 1.42x faster                                                            |
| deepcopy                   | 392 us                                                       | 286 us: 1.37x faster                                                            |
| async_tree_none            | 376 ms                                                       | 276 ms: 1.36x faster                                                            |
| async_tree_io              | 843 ms                                                       | 624 ms: 1.35x faster                                                            |
| async_tree_io_tg           | 831 ms                                                       | 624 ms: 1.33x faster                                                            |
| async_tree_memoization     | 453 ms                                                       | 343 ms: 1.32x faster                                                            |
| async_tree_none_tg         | 346 ms                                                       | 267 ms: 1.30x faster                                                            |
| deepcopy_memo              | 38.6 us                                                      | 30.2 us: 1.28x faster                                                           |
| go                         | 162 ms                                                       | 128 ms: 1.27x faster                                                            |
| async_generators           | 457 ms                                                       | 377 ms: 1.21x faster                                                            |
| deepcopy_reduce            | 3.54 us                                                      | 2.95 us: 1.20x faster                                                           |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 508 ms: 1.19x faster                                                            |
| tomli_loads                | 2.46 sec                                                     | 2.09 sec: 1.18x faster                                                          |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 498 ms: 1.17x faster                                                            |
| generators                 | 33.6 ms                                                      | 28.8 ms: 1.17x faster                                                           |
| float                      | 81.3 ms                                                      | 69.9 ms: 1.16x faster                                                           |
| regex_effbot               | 3.67 ms                                                      | 3.17 ms: 1.16x faster                                                           |
| spectral_norm              | 97.0 ms                                                      | 84.3 ms: 1.15x faster                                                           |
| richards                   | 52.9 ms                                                      | 46.1 ms: 1.15x faster                                                           |
| xml_etree_parse            | 150 ms                                                       | 134 ms: 1.12x faster                                                            |
| richards_super             | 59.6 ms                                                      | 53.3 ms: 1.12x faster                                                           |
| pathlib                    | 17.5 ms                                                      | 15.9 ms: 1.11x faster                                                           |
| pyflate                    | 503 ms                                                       | 457 ms: 1.10x faster                                                            |
| pylint                     | 347 ms                                                       | 317 ms: 1.09x faster                                                            |
| hexiom                     | 6.55 ms                                                      | 6.01 ms: 1.09x faster                                                           |
| scimark_fft                | 328 ms                                                       | 301 ms: 1.09x faster                                                            |
| telco                      | 8.79 ms                                                      | 8.14 ms: 1.08x faster                                                           |
| xml_etree_iterparse        | 103 ms                                                       | 95.4 ms: 1.08x faster                                                           |
| bpe_tokeniser              | 5.09 sec                                                     | 4.73 sec: 1.08x faster                                                          |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.44 ms: 1.07x faster                                                           |
| html5lib                   | 73.5 ms                                                      | 68.5 ms: 1.07x faster                                                           |
| scimark_monte_carlo        | 66.1 ms                                                      | 61.7 ms: 1.07x faster                                                           |
| pprint_pformat             | 1.72 sec                                                     | 1.61 sec: 1.07x faster                                                          |
| genshi_text                | 26.2 ms                                                      | 24.5 ms: 1.07x faster                                                           |
| pprint_safe_repr           | 843 ms                                                       | 789 ms: 1.07x faster                                                            |
| sqlglot_parse              | 1.40 ms                                                      | 1.31 ms: 1.07x faster                                                           |
| coverage                   | 80.0 ms                                                      | 75.3 ms: 1.06x faster                                                           |
| json                       | 5.69 ms                                                      | 5.36 ms: 1.06x faster                                                           |
| scimark_sor                | 123 ms                                                       | 116 ms: 1.06x faster                                                            |
| sqlglot_transpile          | 1.79 ms                                                      | 1.70 ms: 1.06x faster                                                           |
| xml_etree_generate         | 86.5 ms                                                      | 82.5 ms: 1.05x faster                                                           |
| regex_compile              | 143 ms                                                       | 137 ms: 1.04x faster                                                            |
| genshi_xml                 | 57.1 ms                                                      | 54.6 ms: 1.04x faster                                                           |
| 2to3                       | 293 ms                                                       | 281 ms: 1.04x faster                                                            |
| k_core                     | 2.17 sec                                                     | 2.08 sec: 1.04x faster                                                          |
| thrift                     | 901 us                                                       | 866 us: 1.04x faster                                                            |
| meteor_contest             | 130 ms                                                       | 125 ms: 1.04x faster                                                            |
| shortest_path              | 460 ms                                                       | 445 ms: 1.03x faster                                                            |
| connected_components       | 432 ms                                                       | 418 ms: 1.03x faster                                                            |
| mdp                        | 2.54 sec                                                     | 2.46 sec: 1.03x faster                                                          |
| scimark_lu                 | 98.7 ms                                                      | 95.5 ms: 1.03x faster                                                           |
| sympy_str                  | 298 ms                                                       | 289 ms: 1.03x faster                                                            |
| sympy_expand               | 509 ms                                                       | 494 ms: 1.03x faster                                                            |
| coroutines                 | 21.6 ms                                                      | 21.0 ms: 1.03x faster                                                           |
| sqlglot_optimize           | 59.3 ms                                                      | 57.7 ms: 1.03x faster                                                           |
| sqlglot_normalize          | 119 ms                                                       | 116 ms: 1.03x faster                                                            |
| sqlite_synth               | 2.91 us                                                      | 2.83 us: 1.03x faster                                                           |
| dulwich_log                | 68.2 ms                                                      | 66.7 ms: 1.02x faster                                                           |
| sqlalchemy_declarative     | 148 ms                                                       | 145 ms: 1.02x faster                                                            |
| bench_thread_pool          | 942 us                                                       | 923 us: 1.02x faster                                                            |
| nqueens                    | 90.7 ms                                                      | 88.9 ms: 1.02x faster                                                           |
| sympy_sum                  | 155 ms                                                       | 152 ms: 1.02x faster                                                            |
| chaos                      | 60.2 ms                                                      | 59.1 ms: 1.02x faster                                                           |
| sqlalchemy_imperative      | 18.3 ms                                                      | 18.0 ms: 1.02x faster                                                           |
| sympy_integrate            | 23.6 ms                                                      | 23.2 ms: 1.02x faster                                                           |
| logging_silent             | 97.9 ns                                                      | 96.6 ns: 1.01x faster                                                           |
| asyncio_websockets         | 388 ms                                                       | 384 ms: 1.01x faster                                                            |
| fannkuch                   | 363 ms                                                       | 361 ms: 1.01x faster                                                            |
| python_startup_no_site     | 8.96 ms                                                      | 8.97 ms: 1.00x slower                                                           |
| python_startup             | 15.9 ms                                                      | 16.0 ms: 1.00x slower                                                           |
| regex_dna                  | 247 ms                                                       | 248 ms: 1.01x slower                                                            |
| deltablue                  | 3.42 ms                                                      | 3.44 ms: 1.01x slower                                                           |
| unpickle_pure_python       | 217 us                                                       | 219 us: 1.01x slower                                                            |
| pidigits                   | 252 ms                                                       | 254 ms: 1.01x slower                                                            |
| xml_etree_process          | 61.2 ms                                                      | 61.8 ms: 1.01x slower                                                           |
| django_template            | 36.4 ms                                                      | 36.8 ms: 1.01x slower                                                           |
| crypto_pyaes               | 73.3 ms                                                      | 74.4 ms: 1.02x slower                                                           |
| pycparser                  | 1.24 sec                                                     | 1.26 sec: 1.02x slower                                                          |
| raytrace                   | 273 ms                                                       | 277 ms: 1.02x slower                                                            |
| docutils                   | 2.83 sec                                                     | 2.89 sec: 1.02x slower                                                          |
| logging_simple             | 6.39 us                                                      | 6.61 us: 1.03x slower                                                           |
| json_loads                 | 24.7 us                                                      | 25.5 us: 1.03x slower                                                           |
| pickle_pure_python         | 323 us                                                       | 335 us: 1.04x slower                                                            |
| create_gc_cycles           | 2.68 ms                                                      | 2.80 ms: 1.04x slower                                                           |
| logging_format             | 6.94 us                                                      | 7.27 us: 1.05x slower                                                           |
| mako                       | 10.4 ms                                                      | 10.9 ms: 1.05x slower                                                           |
| comprehensions             | 17.0 us                                                      | 17.9 us: 1.05x slower                                                           |
| json_dumps                 | 11.1 ms                                                      | 11.7 ms: 1.05x slower                                                           |
| typing_runtime_protocols   | 169 us                                                       | 178 us: 1.05x slower                                                            |
| many_optionals             | 930 us                                                       | 1.02 ms: 1.09x slower                                                           |
| subparsers                 | 17.5 ms                                                      | 23.0 ms: 1.32x slower                                                           |
| gc_traversal               | 4.74 ms                                                      | 6.65 ms: 1.40x slower                                                           |
| bench_mp_pool              | 5.12 ms                                                      | 1.94 sec: 379.56x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                                    |

Benchmark hidden because not significant (3): regex_v8, sphinx, nbody
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.058x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.02x