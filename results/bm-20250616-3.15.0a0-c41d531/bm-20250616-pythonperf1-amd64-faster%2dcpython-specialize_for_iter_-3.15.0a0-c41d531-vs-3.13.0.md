# Results vs. 3.13.0

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: windows-amd64
- commit hash: c41d531
- commit date: 2025-06-16
- overall geometric mean: 1.032x slower
- HPT reliability: 99.54%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 222 ms: 1.03x slower                                                                 |
| docutils       | 1.53 sec                                                    | 1.63 sec: 1.06x slower                                                               |
| html5lib       | 38.2 ms                                                     | 38.8 ms: 1.02x slower                                                                |
| sphinx         | 617 ms                                                      | 639 ms: 1.03x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 159 ms: 1.89x faster                                                                 |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                                 |
| async_tree_io              | 513 ms                                                      | 400 ms: 1.28x faster                                                                 |
| async_tree_memoization     | 265 ms                                                      | 208 ms: 1.27x faster                                                                 |
| async_tree_none            | 219 ms                                                      | 172 ms: 1.27x faster                                                                 |
| async_tree_io_tg           | 497 ms                                                      | 398 ms: 1.25x faster                                                                 |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.18x faster                                                                 |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 326 ms: 1.16x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 340 ms: 1.12x faster                                                                 |
| async_generators           | 223 ms                                                      | 234 ms: 1.05x slower                                                                 |
| coroutines                 | 12.5 ms                                                     | 14.0 ms: 1.12x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.21x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 45.6 ms: 1.11x faster                                                                |
| nbody          | 66.3 ms                                                     | 65.7 ms: 1.01x faster                                                                |
| pidigits       | 146 ms                                                      | 148 ms: 1.01x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.8 ms: 1.61x faster                                                                |
| regex_effbot   | 1.69 ms                                                     | 1.51 ms: 1.12x faster                                                                |
| regex_compile  | 80.7 ms                                                     | 82.2 ms: 1.02x slower                                                                |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.3 us: 1.05x faster                                                                |
| xml_etree_parse      | 92.2 ms                                                     | 89.1 ms: 1.03x faster                                                                |
| json_dumps           | 6.19 ms                                                     | 6.29 ms: 1.02x slower                                                                |
| tomli_loads          | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                                               |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.7 ms: 1.05x slower                                                                |
| unpickle_pure_python | 130 us                                                      | 139 us: 1.07x slower                                                                 |
| xml_etree_generate   | 53.5 ms                                                     | 57.2 ms: 1.07x slower                                                                |
| xml_etree_process    | 36.5 ms                                                     | 39.4 ms: 1.08x slower                                                                |
| pickle_pure_python   | 186 us                                                      | 215 us: 1.15x slower                                                                 |
| Geometric mean       | (ref)                                                       | 1.04x slower                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.6 ms: 1.05x slower                                                                |
| python_startup_no_site | 16.9 ms                                                     | 19.4 ms: 1.15x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 15.4 ms: 1.01x slower                                                                |
| mako            | 6.56 ms                                                     | 6.67 ms: 1.02x slower                                                                |
| django_template | 20.3 ms                                                     | 24.4 ms: 1.20x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.05x slower                                                                         |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 32.3 ms: 2.33x faster                                                                |
| asyncio_websockets         | 300 ms                                                      | 159 ms: 1.89x faster                                                                 |
| mdp                        | 1.43 sec                                                    | 826 ms: 1.73x faster                                                                 |
| regex_v8                   | 23.8 ms                                                     | 14.8 ms: 1.61x faster                                                                |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                                 |
| deepcopy                   | 223 us                                                      | 172 us: 1.30x faster                                                                 |
| async_tree_io              | 513 ms                                                      | 400 ms: 1.28x faster                                                                 |
| async_tree_memoization     | 265 ms                                                      | 208 ms: 1.27x faster                                                                 |
| async_tree_none            | 219 ms                                                      | 172 ms: 1.27x faster                                                                 |
| async_tree_io_tg           | 497 ms                                                      | 398 ms: 1.25x faster                                                                 |
| deepcopy_memo              | 23.1 us                                                     | 19.0 us: 1.21x faster                                                                |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.18x faster                                                                 |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 326 ms: 1.16x faster                                                                 |
| regex_effbot               | 1.69 ms                                                     | 1.51 ms: 1.12x faster                                                                |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 340 ms: 1.12x faster                                                                 |
| float                      | 50.8 ms                                                     | 45.6 ms: 1.11x faster                                                                |
| json                       | 3.30 ms                                                     | 3.00 ms: 1.10x faster                                                                |
| go                         | 84.7 ms                                                     | 77.3 ms: 1.10x faster                                                                |
| deepcopy_reduce            | 2.02 us                                                     | 1.88 us: 1.08x faster                                                                |
| spectral_norm              | 63.4 ms                                                     | 59.4 ms: 1.07x faster                                                                |
| json_loads                 | 15.1 us                                                     | 14.3 us: 1.05x faster                                                                |
| telco                      | 4.85 ms                                                     | 4.62 ms: 1.05x faster                                                                |
| xml_etree_parse            | 92.2 ms                                                     | 89.1 ms: 1.03x faster                                                                |
| pyflate                    | 283 ms                                                      | 280 ms: 1.01x faster                                                                 |
| nbody                      | 66.3 ms                                                     | 65.7 ms: 1.01x faster                                                                |
| sqlite_synth               | 1.59 us                                                     | 1.57 us: 1.01x faster                                                                |
| scimark_monte_carlo        | 40.7 ms                                                     | 40.9 ms: 1.00x slower                                                                |
| sympy_expand               | 286 ms                                                      | 287 ms: 1.00x slower                                                                 |
| sympy_integrate            | 12.3 ms                                                     | 12.5 ms: 1.01x slower                                                                |
| genshi_text                | 15.2 ms                                                     | 15.4 ms: 1.01x slower                                                                |
| pidigits                   | 146 ms                                                      | 148 ms: 1.01x slower                                                                 |
| json_dumps                 | 6.19 ms                                                     | 6.29 ms: 1.02x slower                                                                |
| mako                       | 6.56 ms                                                     | 6.67 ms: 1.02x slower                                                                |
| html5lib                   | 38.2 ms                                                     | 38.8 ms: 1.02x slower                                                                |
| tomli_loads                | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                                               |
| regex_compile              | 80.7 ms                                                     | 82.2 ms: 1.02x slower                                                                |
| sympy_str                  | 167 ms                                                      | 170 ms: 1.02x slower                                                                 |
| bpe_tokeniser              | 2.87 sec                                                    | 2.93 sec: 1.02x slower                                                               |
| fannkuch                   | 252 ms                                                      | 257 ms: 1.02x slower                                                                 |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.66 ms: 1.02x slower                                                                |
| scimark_fft                | 175 ms                                                      | 179 ms: 1.03x slower                                                                 |
| shortest_path              | 355 ms                                                      | 364 ms: 1.03x slower                                                                 |
| chaos                      | 37.9 ms                                                     | 39.0 ms: 1.03x slower                                                                |
| sympy_sum                  | 85.2 ms                                                     | 87.7 ms: 1.03x slower                                                                |
| 2to3                       | 215 ms                                                      | 222 ms: 1.03x slower                                                                 |
| meteor_contest             | 72.0 ms                                                     | 74.3 ms: 1.03x slower                                                                |
| generators                 | 19.0 ms                                                     | 19.6 ms: 1.03x slower                                                                |
| sphinx                     | 617 ms                                                      | 639 ms: 1.03x slower                                                                 |
| crypto_pyaes               | 45.6 ms                                                     | 47.3 ms: 1.04x slower                                                                |
| scimark_sor                | 76.2 ms                                                     | 79.1 ms: 1.04x slower                                                                |
| dulwich_log                | 40.1 ms                                                     | 41.7 ms: 1.04x slower                                                                |
| connected_components       | 320 ms                                                      | 334 ms: 1.04x slower                                                                 |
| scimark_lu                 | 56.7 ms                                                     | 59.3 ms: 1.05x slower                                                                |
| async_generators           | 223 ms                                                      | 234 ms: 1.05x slower                                                                 |
| python_startup             | 24.4 ms                                                     | 25.6 ms: 1.05x slower                                                                |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.7 ms: 1.05x slower                                                                |
| regex_dna                  | 115 ms                                                      | 121 ms: 1.05x slower                                                                 |
| richards                   | 26.3 ms                                                     | 27.9 ms: 1.06x slower                                                                |
| docutils                   | 1.53 sec                                                    | 1.63 sec: 1.06x slower                                                               |
| richards_super             | 29.8 ms                                                     | 31.7 ms: 1.06x slower                                                                |
| unpickle_pure_python       | 130 us                                                      | 139 us: 1.07x slower                                                                 |
| xml_etree_generate         | 53.5 ms                                                     | 57.2 ms: 1.07x slower                                                                |
| xml_etree_process          | 36.5 ms                                                     | 39.4 ms: 1.08x slower                                                                |
| hexiom                     | 3.84 ms                                                     | 4.14 ms: 1.08x slower                                                                |
| comprehensions             | 10.4 us                                                     | 11.2 us: 1.08x slower                                                                |
| create_gc_cycles           | 1.22 ms                                                     | 1.33 ms: 1.08x slower                                                                |
| logging_simple             | 5.77 us                                                     | 6.30 us: 1.09x slower                                                                |
| logging_format             | 6.18 us                                                     | 6.78 us: 1.10x slower                                                                |
| gc_traversal               | 1.96 ms                                                     | 2.18 ms: 1.11x slower                                                                |
| nqueens                    | 56.1 ms                                                     | 62.8 ms: 1.12x slower                                                                |
| coroutines                 | 12.5 ms                                                     | 14.0 ms: 1.12x slower                                                                |
| pprint_safe_repr           | 485 ms                                                      | 553 ms: 1.14x slower                                                                 |
| python_startup_no_site     | 16.9 ms                                                     | 19.4 ms: 1.15x slower                                                                |
| pickle_pure_python         | 186 us                                                      | 215 us: 1.15x slower                                                                 |
| pprint_pformat             | 977 ms                                                      | 1.13 sec: 1.16x slower                                                               |
| deltablue                  | 1.89 ms                                                     | 2.23 ms: 1.18x slower                                                                |
| django_template            | 20.3 ms                                                     | 24.4 ms: 1.20x slower                                                                |
| many_optionals             | 361 us                                                      | 435 us: 1.20x slower                                                                 |
| raytrace                   | 153 ms                                                      | 186 ms: 1.21x slower                                                                 |
| subparsers                 | 10.9 ms                                                     | 17.1 ms: 1.58x slower                                                                |
| logging_silent             | 54.6 ns                                                     | 317 ns: 5.81x slower                                                                 |
| coverage                   | 45.3 ms                                                     | 293 ms: 6.46x slower                                                                 |
| thrift                     | 8.47 ms                                                     | 97.5 ms: 11.52x slower                                                               |
| Geometric mean             | (ref)                                                       | 1.05x slower                                                                         |

Benchmark hidden because not significant (5): pylint, typing_runtime_protocols, genshi_xml, k_core, pycparser
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250616-3.15.0a0-c41d531/bm-20250616-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.032x slower

# HPT report

- Reliability score: 99.54% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown