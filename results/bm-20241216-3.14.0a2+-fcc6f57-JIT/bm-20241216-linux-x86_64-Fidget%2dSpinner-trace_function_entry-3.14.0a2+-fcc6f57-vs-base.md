# Results vs. base

- fork: Fidget-Spinner
- ref: trace_function_entry
- machine: linux-x86_64
- commit hash: fcc6f57
- commit date: 2024-12-16
- overall geometric mean: 1.008x faster
- HPT reliability: 99.82%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241213-linux-x86_64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c | bm-20241216-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 260 ms                                                                 | 257 ms: 1.01x faster                                                             |
| html5lib       | 65.5 ms                                                                | 61.7 ms: 1.06x faster                                                            |
| sphinx         | 1.06 sec                                                               | 1.03 sec: 1.03x faster                                                           |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                                     |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241213-linux-x86_64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c | bm-20241216-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_generators           | 446 ms                                                                 | 422 ms: 1.06x faster                                                             |
| coroutines                 | 24.1 ms                                                                | 23.5 ms: 1.03x faster                                                            |
| async_tree_memoization_tg  | 311 ms                                                                 | 308 ms: 1.01x faster                                                             |
| async_tree_cpu_io_mixed_tg | 478 ms                                                                 | 482 ms: 1.01x slower                                                             |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                                     |

Benchmark hidden because not significant (7): async_tree_memoization, async_tree_io_tg, async_tree_io, asyncio_websockets, async_tree_none_tg, async_tree_none, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241213-linux-x86_64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c | bm-20241216-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 83.2 ms                                                                | 82.8 ms: 1.01x faster                                                            |
| pidigits       | 187 ms                                                                 | 187 ms: 1.00x faster                                                             |
| float          | 72.7 ms                                                                | 73.5 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241213-linux-x86_64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c | bm-20241216-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_dna      | 213 ms                                                                 | 209 ms: 1.02x faster                                                             |
| regex_effbot   | 3.26 ms                                                                | 3.21 ms: 1.01x faster                                                            |
| regex_compile  | 128 ms                                                                 | 126 ms: 1.01x faster                                                             |
| regex_v8       | 24.8 ms                                                                | 25.0 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241213-linux-x86_64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c | bm-20241216-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|---------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_process   | 54.9 ms                                                                | 54.3 ms: 1.01x faster                                                            |
| xml_etree_generate  | 77.6 ms                                                                | 76.9 ms: 1.01x faster                                                            |
| json_dumps          | 11.0 ms                                                                | 11.1 ms: 1.01x slower                                                            |
| xml_etree_iterparse | 94.6 ms                                                                | 96.0 ms: 1.01x slower                                                            |
| Geometric mean      | (ref)                                                                  | 1.00x slower                                                                     |

Benchmark hidden because not significant (5): pickle_pure_python, xml_etree_parse, json_loads, tomli_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241213-linux-x86_64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c | bm-20241216-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                            |
| python_startup_no_site | 7.07 ms                                                                | 7.08 ms: 1.00x slower                                                            |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241213-linux-x86_64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c | bm-20241216-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 57.8 ms                                                                | 49.9 ms: 1.16x faster                                                            |
| genshi_text     | 24.3 ms                                                                | 21.8 ms: 1.11x faster                                                            |
| django_template | 33.7 ms                                                                | 31.9 ms: 1.06x faster                                                            |
| mako            | 10.0 ms                                                                | 10.1 ms: 1.01x slower                                                            |
| Geometric mean  | (ref)                                                                  | 1.08x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241213-linux-x86_64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c | bm-20241216-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| generators                 | 34.8 ms                                                                | 28.0 ms: 1.24x faster                                                            |
| genshi_xml                 | 57.8 ms                                                                | 49.9 ms: 1.16x faster                                                            |
| genshi_text                | 24.3 ms                                                                | 21.8 ms: 1.11x faster                                                            |
| html5lib                   | 65.5 ms                                                                | 61.7 ms: 1.06x faster                                                            |
| nqueens                    | 86.5 ms                                                                | 81.6 ms: 1.06x faster                                                            |
| django_template            | 33.7 ms                                                                | 31.9 ms: 1.06x faster                                                            |
| djangocms                  | 23.0 us                                                                | 21.8 us: 1.06x faster                                                            |
| async_generators           | 446 ms                                                                 | 422 ms: 1.06x faster                                                             |
| raytrace                   | 285 ms                                                                 | 273 ms: 1.04x faster                                                             |
| mdp                        | 2.59 sec                                                               | 2.48 sec: 1.04x faster                                                           |
| hexiom                     | 6.98 ms                                                                | 6.71 ms: 1.04x faster                                                            |
| pylint                     | 290 ms                                                                 | 280 ms: 1.03x faster                                                             |
| sphinx                     | 1.06 sec                                                               | 1.03 sec: 1.03x faster                                                           |
| sympy_sum                  | 156 ms                                                                 | 151 ms: 1.03x faster                                                             |
| coroutines                 | 24.1 ms                                                                | 23.5 ms: 1.03x faster                                                            |
| sympy_integrate            | 20.9 ms                                                                | 20.4 ms: 1.03x faster                                                            |
| deepcopy                   | 270 us                                                                 | 263 us: 1.02x faster                                                             |
| sympy_str                  | 283 ms                                                                 | 277 ms: 1.02x faster                                                             |
| sqlglot_normalize          | 108 ms                                                                 | 106 ms: 1.02x faster                                                             |
| go                         | 125 ms                                                                 | 123 ms: 1.02x faster                                                             |
| regex_dna                  | 213 ms                                                                 | 209 ms: 1.02x faster                                                             |
| crypto_pyaes               | 67.8 ms                                                                | 66.6 ms: 1.02x faster                                                            |
| sqlite_synth               | 2.76 us                                                                | 2.71 us: 1.02x faster                                                            |
| bench_thread_pool          | 885 us                                                                 | 872 us: 1.02x faster                                                             |
| regex_effbot               | 3.26 ms                                                                | 3.21 ms: 1.01x faster                                                            |
| sympy_expand               | 478 ms                                                                 | 472 ms: 1.01x faster                                                             |
| many_optionals             | 987 us                                                                 | 975 us: 1.01x faster                                                             |
| regex_compile              | 128 ms                                                                 | 126 ms: 1.01x faster                                                             |
| pathlib                    | 16.4 ms                                                                | 16.2 ms: 1.01x faster                                                            |
| typing_runtime_protocols   | 167 us                                                                 | 165 us: 1.01x faster                                                             |
| xml_etree_process          | 54.9 ms                                                                | 54.3 ms: 1.01x faster                                                            |
| sqlglot_optimize           | 54.2 ms                                                                | 53.6 ms: 1.01x faster                                                            |
| xml_etree_generate         | 77.6 ms                                                                | 76.9 ms: 1.01x faster                                                            |
| 2to3                       | 260 ms                                                                 | 257 ms: 1.01x faster                                                             |
| async_tree_memoization_tg  | 311 ms                                                                 | 308 ms: 1.01x faster                                                             |
| coverage                   | 83.6 ms                                                                | 82.8 ms: 1.01x faster                                                            |
| sqlalchemy_declarative     | 129 ms                                                                 | 128 ms: 1.01x faster                                                             |
| sqlglot_parse              | 1.29 ms                                                                | 1.28 ms: 1.01x faster                                                            |
| comprehensions             | 17.0 us                                                                | 16.9 us: 1.01x faster                                                            |
| nbody                      | 83.2 ms                                                                | 82.8 ms: 1.01x faster                                                            |
| shortest_path              | 480 ms                                                                 | 478 ms: 1.00x faster                                                             |
| dulwich_log                | 67.1 ms                                                                | 66.9 ms: 1.00x faster                                                            |
| connected_components       | 437 ms                                                                 | 436 ms: 1.00x faster                                                             |
| pidigits                   | 187 ms                                                                 | 187 ms: 1.00x faster                                                             |
| python_startup             | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                            |
| python_startup_no_site     | 7.07 ms                                                                | 7.08 ms: 1.00x slower                                                            |
| meteor_contest             | 107 ms                                                                 | 108 ms: 1.01x slower                                                             |
| fannkuch                   | 379 ms                                                                 | 381 ms: 1.01x slower                                                             |
| regex_v8                   | 24.8 ms                                                                | 25.0 ms: 1.01x slower                                                            |
| gc_traversal               | 4.73 ms                                                                | 4.76 ms: 1.01x slower                                                            |
| scimark_sparse_mat_mult    | 4.52 ms                                                                | 4.55 ms: 1.01x slower                                                            |
| create_gc_cycles           | 2.44 ms                                                                | 2.45 ms: 1.01x slower                                                            |
| async_tree_cpu_io_mixed_tg | 478 ms                                                                 | 482 ms: 1.01x slower                                                             |
| deepcopy_reduce            | 2.71 us                                                                | 2.74 us: 1.01x slower                                                            |
| mako                       | 10.0 ms                                                                | 10.1 ms: 1.01x slower                                                            |
| json_dumps                 | 11.0 ms                                                                | 11.1 ms: 1.01x slower                                                            |
| float                      | 72.7 ms                                                                | 73.5 ms: 1.01x slower                                                            |
| scimark_fft                | 308 ms                                                                 | 312 ms: 1.01x slower                                                             |
| thrift                     | 768 us                                                                 | 778 us: 1.01x slower                                                             |
| xml_etree_iterparse        | 94.6 ms                                                                | 96.0 ms: 1.01x slower                                                            |
| telco                      | 7.38 ms                                                                | 7.51 ms: 1.02x slower                                                            |
| logging_silent             | 107 ns                                                                 | 109 ns: 1.02x slower                                                             |
| spectral_norm              | 101 ms                                                                 | 103 ms: 1.02x slower                                                             |
| richards_super             | 51.2 ms                                                                | 52.2 ms: 1.02x slower                                                            |
| pprint_safe_repr           | 734 ms                                                                 | 752 ms: 1.02x slower                                                             |
| richards                   | 44.4 ms                                                                | 45.5 ms: 1.02x slower                                                            |
| pyflate                    | 434 ms                                                                 | 445 ms: 1.03x slower                                                             |
| chaos                      | 60.0 ms                                                                | 61.7 ms: 1.03x slower                                                            |
| scimark_lu                 | 113 ms                                                                 | 116 ms: 1.03x slower                                                             |
| pprint_pformat             | 1.47 sec                                                               | 1.56 sec: 1.06x slower                                                           |
| deepcopy_memo              | 29.7 us                                                                | 31.5 us: 1.06x slower                                                            |
| deltablue                  | 3.27 ms                                                                | 3.51 ms: 1.07x slower                                                            |
| scimark_sor                | 114 ms                                                                 | 125 ms: 1.09x slower                                                             |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                                     |

Benchmark hidden because not significant (25): pycparser, mypy2, async_tree_memoization, k_core, async_tree_io_tg, pickle_pure_python, logging_simple, sqlglot_transpile, async_tree_io, asyncio_websockets, subparsers, bpe_tokeniser, async_tree_none_tg, xml_etree_parse, bench_mp_pool, docutils, json_loads, tomli_loads, logging_format, sqlalchemy_imperative, unpickle_pure_python, async_tree_none, async_tree_cpu_io_mixed, json, scimark_monte_carlo

- Geometric mean (including insignificant results): 1.008x faster

# HPT report

- Reliability score: 99.82% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x