# Results vs. 3.13.0

- fork: faster-cpython
- ref: close_escapes_2
- machine: windows-amd64
- commit hash: 620dde2
- commit date: 2025-01-29
- overall geometric mean: 1.032x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 233 ms: 1.08x slower                                                             |
| docutils       | 1.53 sec                                                    | 1.69 sec: 1.11x slower                                                           |
| html5lib       | 38.2 ms                                                     | 39.8 ms: 1.04x slower                                                            |
| sphinx         | 617 ms                                                      | 660 ms: 1.07x slower                                                             |
| Geometric mean | (ref)                                                       | 1.08x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 220 ms: 1.27x faster                                                             |
| async_tree_io              | 513 ms                                                      | 431 ms: 1.19x faster                                                             |
| async_tree_io_tg           | 497 ms                                                      | 419 ms: 1.19x faster                                                             |
| async_tree_memoization     | 265 ms                                                      | 228 ms: 1.16x faster                                                             |
| async_tree_none            | 219 ms                                                      | 193 ms: 1.14x faster                                                             |
| async_tree_none_tg         | 200 ms                                                      | 180 ms: 1.11x faster                                                             |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 347 ms: 1.10x faster                                                             |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 349 ms: 1.09x faster                                                             |
| async_generators           | 223 ms                                                      | 225 ms: 1.01x slower                                                             |
| asyncio_websockets         | 300 ms                                                      | 310 ms: 1.03x slower                                                             |
| coroutines                 | 12.5 ms                                                     | 15.0 ms: 1.20x slower                                                            |
| Geometric mean             | (ref)                                                       | 1.09x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 52.6 ms: 1.03x slower                                                            |
| nbody          | 66.3 ms                                                     | 77.1 ms: 1.16x slower                                                            |
| Geometric mean | (ref)                                                       | 1.06x slower                                                                     |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 15.5 ms: 1.53x faster                                                            |
| regex_effbot   | 1.69 ms                                                     | 1.43 ms: 1.18x faster                                                            |
| regex_dna      | 115 ms                                                      | 114 ms: 1.01x faster                                                             |
| regex_compile  | 80.7 ms                                                     | 89.5 ms: 1.11x slower                                                            |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 87.5 ms: 1.05x faster                                                            |
| json_loads           | 15.1 us                                                     | 15.4 us: 1.02x slower                                                            |
| tomli_loads          | 1.37 sec                                                    | 1.44 sec: 1.05x slower                                                           |
| xml_etree_iterparse  | 60.5 ms                                                     | 64.8 ms: 1.07x slower                                                            |
| xml_etree_generate   | 53.5 ms                                                     | 58.6 ms: 1.10x slower                                                            |
| json_dumps           | 6.19 ms                                                     | 6.81 ms: 1.10x slower                                                            |
| xml_etree_process    | 36.5 ms                                                     | 41.3 ms: 1.13x slower                                                            |
| unpickle_pure_python | 130 us                                                      | 164 us: 1.26x slower                                                             |
| pickle_pure_python   | 186 us                                                      | 238 us: 1.28x slower                                                             |
| Geometric mean       | (ref)                                                       | 1.10x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 16.9 ms                                                     | 18.0 ms: 1.07x slower                                                            |
| Geometric mean         | (ref)                                                       | 1.03x slower                                                                     |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.88 ms: 1.05x slower                                                            |
| genshi_xml      | 33.9 ms                                                     | 36.0 ms: 1.06x slower                                                            |
| genshi_text     | 15.2 ms                                                     | 16.3 ms: 1.07x slower                                                            |
| django_template | 20.3 ms                                                     | 25.6 ms: 1.26x slower                                                            |
| Geometric mean  | (ref)                                                       | 1.11x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 519 us: 16.31x faster                                                            |
| regex_v8                   | 23.8 ms                                                     | 15.5 ms: 1.53x faster                                                            |
| async_tree_memoization_tg  | 281 ms                                                      | 220 ms: 1.27x faster                                                             |
| deepcopy                   | 223 us                                                      | 187 us: 1.19x faster                                                             |
| async_tree_io              | 513 ms                                                      | 431 ms: 1.19x faster                                                             |
| async_tree_io_tg           | 497 ms                                                      | 419 ms: 1.19x faster                                                             |
| regex_effbot               | 1.69 ms                                                     | 1.43 ms: 1.18x faster                                                            |
| async_tree_memoization     | 265 ms                                                      | 228 ms: 1.16x faster                                                             |
| async_tree_none            | 219 ms                                                      | 193 ms: 1.14x faster                                                             |
| async_tree_none_tg         | 200 ms                                                      | 180 ms: 1.11x faster                                                             |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 347 ms: 1.10x faster                                                             |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 349 ms: 1.09x faster                                                             |
| deepcopy_memo              | 23.1 us                                                     | 21.4 us: 1.08x faster                                                            |
| deepcopy_reduce            | 2.02 us                                                     | 1.90 us: 1.06x faster                                                            |
| xml_etree_parse            | 92.2 ms                                                     | 87.5 ms: 1.05x faster                                                            |
| shortest_path              | 355 ms                                                      | 347 ms: 1.02x faster                                                             |
| connected_components       | 320 ms                                                      | 315 ms: 1.02x faster                                                             |
| regex_dna                  | 115 ms                                                      | 114 ms: 1.01x faster                                                             |
| async_generators           | 223 ms                                                      | 225 ms: 1.01x slower                                                             |
| sqlite_synth               | 1.59 us                                                     | 1.62 us: 1.02x slower                                                            |
| json_loads                 | 15.1 us                                                     | 15.4 us: 1.02x slower                                                            |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.68 ms: 1.03x slower                                                            |
| asyncio_websockets         | 300 ms                                                      | 310 ms: 1.03x slower                                                             |
| pathlib                    | 75.3 ms                                                     | 77.8 ms: 1.03x slower                                                            |
| float                      | 50.8 ms                                                     | 52.6 ms: 1.03x slower                                                            |
| bench_mp_pool              | 84.2 ms                                                     | 87.7 ms: 1.04x slower                                                            |
| html5lib                   | 38.2 ms                                                     | 39.8 ms: 1.04x slower                                                            |
| spectral_norm              | 63.4 ms                                                     | 66.3 ms: 1.04x slower                                                            |
| mako                       | 6.56 ms                                                     | 6.88 ms: 1.05x slower                                                            |
| bpe_tokeniser              | 2.87 sec                                                    | 3.02 sec: 1.05x slower                                                           |
| tomli_loads                | 1.37 sec                                                    | 1.44 sec: 1.05x slower                                                           |
| bench_thread_pool          | 810 us                                                      | 854 us: 1.05x slower                                                             |
| meteor_contest             | 72.0 ms                                                     | 76.2 ms: 1.06x slower                                                            |
| genshi_xml                 | 33.9 ms                                                     | 36.0 ms: 1.06x slower                                                            |
| sympy_sum                  | 85.2 ms                                                     | 90.6 ms: 1.06x slower                                                            |
| python_startup_no_site     | 16.9 ms                                                     | 18.0 ms: 1.07x slower                                                            |
| sphinx                     | 617 ms                                                      | 660 ms: 1.07x slower                                                             |
| xml_etree_iterparse        | 60.5 ms                                                     | 64.8 ms: 1.07x slower                                                            |
| sympy_expand               | 286 ms                                                      | 306 ms: 1.07x slower                                                             |
| genshi_text                | 15.2 ms                                                     | 16.3 ms: 1.07x slower                                                            |
| sympy_str                  | 167 ms                                                      | 180 ms: 1.08x slower                                                             |
| pycparser                  | 695 ms                                                      | 750 ms: 1.08x slower                                                             |
| dulwich_log                | 40.1 ms                                                     | 43.3 ms: 1.08x slower                                                            |
| 2to3                       | 215 ms                                                      | 233 ms: 1.08x slower                                                             |
| coverage                   | 45.3 ms                                                     | 49.2 ms: 1.09x slower                                                            |
| crypto_pyaes               | 45.6 ms                                                     | 49.5 ms: 1.09x slower                                                            |
| go                         | 84.7 ms                                                     | 92.0 ms: 1.09x slower                                                            |
| logging_simple             | 5.77 us                                                     | 6.29 us: 1.09x slower                                                            |
| logging_format             | 6.18 us                                                     | 6.76 us: 1.09x slower                                                            |
| xml_etree_generate         | 53.5 ms                                                     | 58.6 ms: 1.10x slower                                                            |
| json_dumps                 | 6.19 ms                                                     | 6.81 ms: 1.10x slower                                                            |
| docutils                   | 1.53 sec                                                    | 1.69 sec: 1.11x slower                                                           |
| pyflate                    | 283 ms                                                      | 314 ms: 1.11x slower                                                             |
| sympy_integrate            | 12.3 ms                                                     | 13.7 ms: 1.11x slower                                                            |
| regex_compile              | 80.7 ms                                                     | 89.5 ms: 1.11x slower                                                            |
| typing_runtime_protocols   | 103 us                                                      | 116 us: 1.12x slower                                                             |
| sqlglot_optimize           | 32.5 ms                                                     | 36.6 ms: 1.13x slower                                                            |
| mdp                        | 1.43 sec                                                    | 1.62 sec: 1.13x slower                                                           |
| xml_etree_process          | 36.5 ms                                                     | 41.3 ms: 1.13x slower                                                            |
| fannkuch                   | 252 ms                                                      | 286 ms: 1.14x slower                                                             |
| generators                 | 19.0 ms                                                     | 21.6 ms: 1.14x slower                                                            |
| scimark_fft                | 175 ms                                                      | 199 ms: 1.14x slower                                                             |
| pprint_pformat             | 977 ms                                                      | 1.12 sec: 1.14x slower                                                           |
| chaos                      | 37.9 ms                                                     | 43.4 ms: 1.15x slower                                                            |
| pprint_safe_repr           | 485 ms                                                      | 556 ms: 1.15x slower                                                             |
| nbody                      | 66.3 ms                                                     | 77.1 ms: 1.16x slower                                                            |
| sqlglot_normalize          | 172 ms                                                      | 200 ms: 1.17x slower                                                             |
| sqlglot_transpile          | 953 us                                                      | 1.12 ms: 1.17x slower                                                            |
| nqueens                    | 56.1 ms                                                     | 66.2 ms: 1.18x slower                                                            |
| sqlglot_parse              | 764 us                                                      | 901 us: 1.18x slower                                                             |
| coroutines                 | 12.5 ms                                                     | 15.0 ms: 1.20x slower                                                            |
| many_optionals             | 361 us                                                      | 440 us: 1.22x slower                                                             |
| scimark_monte_carlo        | 40.7 ms                                                     | 49.7 ms: 1.22x slower                                                            |
| hexiom                     | 3.84 ms                                                     | 4.70 ms: 1.22x slower                                                            |
| scimark_lu                 | 56.7 ms                                                     | 70.1 ms: 1.24x slower                                                            |
| richards_super             | 29.8 ms                                                     | 37.0 ms: 1.24x slower                                                            |
| comprehensions             | 10.4 us                                                     | 12.9 us: 1.25x slower                                                            |
| richards                   | 26.3 ms                                                     | 32.8 ms: 1.25x slower                                                            |
| scimark_sor                | 76.2 ms                                                     | 95.4 ms: 1.25x slower                                                            |
| deltablue                  | 1.89 ms                                                     | 2.38 ms: 1.26x slower                                                            |
| unpickle_pure_python       | 130 us                                                      | 164 us: 1.26x slower                                                             |
| django_template            | 20.3 ms                                                     | 25.6 ms: 1.26x slower                                                            |
| logging_silent             | 54.6 ns                                                     | 69.1 ns: 1.27x slower                                                            |
| pickle_pure_python         | 186 us                                                      | 238 us: 1.28x slower                                                             |
| raytrace                   | 153 ms                                                      | 203 ms: 1.33x slower                                                             |
| subparsers                 | 10.9 ms                                                     | 16.1 ms: 1.48x slower                                                            |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                                     |

Benchmark hidden because not significant (8): json, pylint, create_gc_cycles, python_startup, pidigits, gc_traversal, telco, k_core
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.032x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown