# Results vs. 3.13.0

- fork: faster-cpython
- ref: use_stackrefs
- machine: windows-amd64
- commit hash: 3e929d7
- commit date: 2025-02-28
- overall geometric mean: 1.005x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 227 ms: 1.06x slower                                                           |
| docutils       | 1.53 sec                                                    | 1.69 sec: 1.10x slower                                                         |
| html5lib       | 38.2 ms                                                     | 41.0 ms: 1.07x slower                                                          |
| sphinx         | 617 ms                                                      | 651 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                       | 1.07x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 218 ms: 1.29x faster                                                           |
| async_tree_io              | 513 ms                                                      | 423 ms: 1.21x faster                                                           |
| async_tree_io_tg           | 497 ms                                                      | 414 ms: 1.20x faster                                                           |
| async_tree_memoization     | 265 ms                                                      | 221 ms: 1.20x faster                                                           |
| async_tree_none            | 219 ms                                                      | 188 ms: 1.17x faster                                                           |
| async_tree_none_tg         | 200 ms                                                      | 178 ms: 1.12x faster                                                           |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 345 ms: 1.10x faster                                                           |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 348 ms: 1.10x faster                                                           |
| asyncio_websockets         | 300 ms                                                      | 308 ms: 1.02x slower                                                           |
| async_generators           | 223 ms                                                      | 230 ms: 1.03x slower                                                           |
| coroutines                 | 12.5 ms                                                     | 13.7 ms: 1.10x slower                                                          |
| Geometric mean             | (ref)                                                       | 1.11x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 46.5 ms: 1.09x faster                                                          |
| pidigits       | 146 ms                                                      | 151 ms: 1.03x slower                                                           |
| nbody          | 66.3 ms                                                     | 68.6 ms: 1.04x slower                                                          |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 15.5 ms: 1.54x faster                                                          |
| regex_effbot   | 1.69 ms                                                     | 1.47 ms: 1.15x faster                                                          |
| regex_dna      | 115 ms                                                      | 117 ms: 1.02x slower                                                           |
| regex_compile  | 80.7 ms                                                     | 85.9 ms: 1.06x slower                                                          |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.7 us: 1.03x faster                                                          |
| xml_etree_parse      | 92.2 ms                                                     | 90.3 ms: 1.02x faster                                                          |
| tomli_loads          | 1.37 sec                                                    | 1.42 sec: 1.03x slower                                                         |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.7 ms: 1.05x slower                                                          |
| xml_etree_generate   | 53.5 ms                                                     | 58.7 ms: 1.10x slower                                                          |
| json_dumps           | 6.19 ms                                                     | 6.97 ms: 1.13x slower                                                          |
| unpickle_pure_python | 130 us                                                      | 148 us: 1.14x slower                                                           |
| xml_etree_process    | 36.5 ms                                                     | 42.3 ms: 1.16x slower                                                          |
| pickle_pure_python   | 186 us                                                      | 230 us: 1.24x slower                                                           |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.2 ms: 1.03x slower                                                          |
| python_startup_no_site | 16.9 ms                                                     | 19.2 ms: 1.14x slower                                                          |
| Geometric mean         | (ref)                                                       | 1.08x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.93 ms: 1.06x slower                                                          |
| genshi_xml      | 33.9 ms                                                     | 38.0 ms: 1.12x slower                                                          |
| genshi_text     | 15.2 ms                                                     | 17.2 ms: 1.13x slower                                                          |
| django_template | 20.3 ms                                                     | 26.4 ms: 1.30x slower                                                          |
| Geometric mean  | (ref)                                                       | 1.15x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 510 us: 16.59x faster                                                          |
| pathlib                    | 75.3 ms                                                     | 32.2 ms: 2.34x faster                                                          |
| regex_v8                   | 23.8 ms                                                     | 15.5 ms: 1.54x faster                                                          |
| async_tree_memoization_tg  | 281 ms                                                      | 218 ms: 1.29x faster                                                           |
| deepcopy                   | 223 us                                                      | 183 us: 1.22x faster                                                           |
| async_tree_io              | 513 ms                                                      | 423 ms: 1.21x faster                                                           |
| async_tree_io_tg           | 497 ms                                                      | 414 ms: 1.20x faster                                                           |
| async_tree_memoization     | 265 ms                                                      | 221 ms: 1.20x faster                                                           |
| deepcopy_memo              | 23.1 us                                                     | 19.5 us: 1.18x faster                                                          |
| async_tree_none            | 219 ms                                                      | 188 ms: 1.17x faster                                                           |
| regex_effbot               | 1.69 ms                                                     | 1.47 ms: 1.15x faster                                                          |
| async_tree_none_tg         | 200 ms                                                      | 178 ms: 1.12x faster                                                           |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 345 ms: 1.10x faster                                                           |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 348 ms: 1.10x faster                                                           |
| float                      | 50.8 ms                                                     | 46.5 ms: 1.09x faster                                                          |
| json                       | 3.30 ms                                                     | 3.06 ms: 1.08x faster                                                          |
| spectral_norm              | 63.4 ms                                                     | 60.0 ms: 1.06x faster                                                          |
| deepcopy_reduce            | 2.02 us                                                     | 1.96 us: 1.03x faster                                                          |
| json_loads                 | 15.1 us                                                     | 14.7 us: 1.03x faster                                                          |
| xml_etree_parse            | 92.2 ms                                                     | 90.3 ms: 1.02x faster                                                          |
| create_gc_cycles           | 1.22 ms                                                     | 1.21 ms: 1.01x faster                                                          |
| telco                      | 4.85 ms                                                     | 4.93 ms: 1.02x slower                                                          |
| regex_dna                  | 115 ms                                                      | 117 ms: 1.02x slower                                                           |
| k_core                     | 1.70 sec                                                    | 1.74 sec: 1.02x slower                                                         |
| asyncio_websockets         | 300 ms                                                      | 308 ms: 1.02x slower                                                           |
| gc_traversal               | 1.96 ms                                                     | 2.01 ms: 1.03x slower                                                          |
| bench_mp_pool              | 84.2 ms                                                     | 86.4 ms: 1.03x slower                                                          |
| pidigits                   | 146 ms                                                      | 151 ms: 1.03x slower                                                           |
| python_startup             | 24.4 ms                                                     | 25.2 ms: 1.03x slower                                                          |
| async_generators           | 223 ms                                                      | 230 ms: 1.03x slower                                                           |
| generators                 | 19.0 ms                                                     | 19.6 ms: 1.03x slower                                                          |
| tomli_loads                | 1.37 sec                                                    | 1.42 sec: 1.03x slower                                                         |
| nbody                      | 66.3 ms                                                     | 68.6 ms: 1.04x slower                                                          |
| shortest_path              | 355 ms                                                      | 370 ms: 1.04x slower                                                           |
| bpe_tokeniser              | 2.87 sec                                                    | 2.99 sec: 1.04x slower                                                         |
| connected_components       | 320 ms                                                      | 335 ms: 1.05x slower                                                           |
| go                         | 84.7 ms                                                     | 88.8 ms: 1.05x slower                                                          |
| sympy_sum                  | 85.2 ms                                                     | 89.6 ms: 1.05x slower                                                          |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.7 ms: 1.05x slower                                                          |
| scimark_sor                | 76.2 ms                                                     | 80.3 ms: 1.05x slower                                                          |
| sphinx                     | 617 ms                                                      | 651 ms: 1.05x slower                                                           |
| sympy_expand               | 286 ms                                                      | 301 ms: 1.05x slower                                                           |
| sympy_str                  | 167 ms                                                      | 176 ms: 1.05x slower                                                           |
| mako                       | 6.56 ms                                                     | 6.93 ms: 1.06x slower                                                          |
| dulwich_log                | 40.1 ms                                                     | 42.4 ms: 1.06x slower                                                          |
| 2to3                       | 215 ms                                                      | 227 ms: 1.06x slower                                                           |
| bench_thread_pool          | 810 us                                                      | 861 us: 1.06x slower                                                           |
| regex_compile              | 80.7 ms                                                     | 85.9 ms: 1.06x slower                                                          |
| meteor_contest             | 72.0 ms                                                     | 76.8 ms: 1.07x slower                                                          |
| sympy_integrate            | 12.3 ms                                                     | 13.2 ms: 1.07x slower                                                          |
| logging_silent             | 54.6 ns                                                     | 58.5 ns: 1.07x slower                                                          |
| html5lib                   | 38.2 ms                                                     | 41.0 ms: 1.07x slower                                                          |
| coverage                   | 45.3 ms                                                     | 48.7 ms: 1.07x slower                                                          |
| scimark_fft                | 175 ms                                                      | 190 ms: 1.08x slower                                                           |
| typing_runtime_protocols   | 103 us                                                      | 113 us: 1.09x slower                                                           |
| pycparser                  | 695 ms                                                      | 761 ms: 1.09x slower                                                           |
| scimark_monte_carlo        | 40.7 ms                                                     | 44.6 ms: 1.09x slower                                                          |
| coroutines                 | 12.5 ms                                                     | 13.7 ms: 1.10x slower                                                          |
| xml_etree_generate         | 53.5 ms                                                     | 58.7 ms: 1.10x slower                                                          |
| scimark_lu                 | 56.7 ms                                                     | 62.4 ms: 1.10x slower                                                          |
| fannkuch                   | 252 ms                                                      | 277 ms: 1.10x slower                                                           |
| docutils                   | 1.53 sec                                                    | 1.69 sec: 1.10x slower                                                         |
| pyflate                    | 283 ms                                                      | 312 ms: 1.10x slower                                                           |
| crypto_pyaes               | 45.6 ms                                                     | 50.5 ms: 1.11x slower                                                          |
| richards                   | 26.3 ms                                                     | 29.1 ms: 1.11x slower                                                          |
| richards_super             | 29.8 ms                                                     | 33.0 ms: 1.11x slower                                                          |
| mdp                        | 1.43 sec                                                    | 1.59 sec: 1.11x slower                                                         |
| pprint_safe_repr           | 485 ms                                                      | 540 ms: 1.11x slower                                                           |
| sqlglot_optimize           | 32.5 ms                                                     | 36.4 ms: 1.12x slower                                                          |
| genshi_xml                 | 33.9 ms                                                     | 38.0 ms: 1.12x slower                                                          |
| pprint_pformat             | 977 ms                                                      | 1.10 sec: 1.12x slower                                                         |
| json_dumps                 | 6.19 ms                                                     | 6.97 ms: 1.13x slower                                                          |
| genshi_text                | 15.2 ms                                                     | 17.2 ms: 1.13x slower                                                          |
| logging_simple             | 5.77 us                                                     | 6.52 us: 1.13x slower                                                          |
| hexiom                     | 3.84 ms                                                     | 4.36 ms: 1.14x slower                                                          |
| python_startup_no_site     | 16.9 ms                                                     | 19.2 ms: 1.14x slower                                                          |
| unpickle_pure_python       | 130 us                                                      | 148 us: 1.14x slower                                                           |
| logging_format             | 6.18 us                                                     | 7.06 us: 1.14x slower                                                          |
| xml_etree_process          | 36.5 ms                                                     | 42.3 ms: 1.16x slower                                                          |
| comprehensions             | 10.4 us                                                     | 12.0 us: 1.16x slower                                                          |
| chaos                      | 37.9 ms                                                     | 43.9 ms: 1.16x slower                                                          |
| sqlglot_transpile          | 953 us                                                      | 1.11 ms: 1.16x slower                                                          |
| nqueens                    | 56.1 ms                                                     | 65.3 ms: 1.16x slower                                                          |
| sqlglot_normalize          | 172 ms                                                      | 199 ms: 1.16x slower                                                           |
| sqlglot_parse              | 764 us                                                      | 892 us: 1.17x slower                                                           |
| many_optionals             | 361 us                                                      | 432 us: 1.19x slower                                                           |
| deltablue                  | 1.89 ms                                                     | 2.28 ms: 1.21x slower                                                          |
| pickle_pure_python         | 186 us                                                      | 230 us: 1.24x slower                                                           |
| raytrace                   | 153 ms                                                      | 197 ms: 1.29x slower                                                           |
| django_template            | 20.3 ms                                                     | 26.4 ms: 1.30x slower                                                          |
| subparsers                 | 10.9 ms                                                     | 16.7 ms: 1.54x slower                                                          |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                                   |

Benchmark hidden because not significant (3): pylint, sqlite_synth, scimark_sparse_mat_mult
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.005x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown