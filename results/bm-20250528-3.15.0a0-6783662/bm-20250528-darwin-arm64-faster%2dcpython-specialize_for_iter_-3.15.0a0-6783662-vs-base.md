# Results vs. base

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: darwin-arm64
- commit hash: 6783662
- commit date: 2025-05-28
- overall geometric mean: 1.000x faster
- HPT reliability: 72.82%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20250527-darwin-arm64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a | bm-20250528-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-6783662 |
|-------------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager_cpu_io_mixed | 369 ms                                                                | 370 ms: 1.00x slower                                                            |
| async_tree_cpu_io_mixed_tg    | 425 ms                                                                | 427 ms: 1.01x slower                                                            |
| async_tree_eager              | 73.1 ms                                                               | 73.5 ms: 1.01x slower                                                           |
| async_tree_none               | 184 ms                                                                | 186 ms: 1.01x slower                                                            |
| Geometric mean                | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (15): async_tree_io_tg, async_tree_eager_memoization, async_tree_none_tg, coroutines, async_tree_memoization_tg, asyncio_websockets, async_tree_eager_memoization_tg, async_tree_memoization, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_io, async_tree_cpu_io_mixed, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250527-darwin-arm64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a | bm-20250528-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-6783662 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 58.5 ms                                                               | 59.4 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250527-darwin-arm64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a | bm-20250528-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-6783662 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 143 ms                                                                | 143 ms: 1.00x slower                                                            |
| regex_effbot   | 2.34 ms                                                               | 2.35 ms: 1.00x slower                                                           |
| regex_compile  | 81.2 ms                                                               | 81.5 ms: 1.00x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250527-darwin-arm64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a | bm-20250528-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-6783662 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.45 sec                                                              | 1.43 sec: 1.01x faster                                                          |
| json_dumps           | 6.87 ms                                                               | 6.85 ms: 1.00x faster                                                           |
| xml_etree_process    | 43.6 ms                                                               | 43.5 ms: 1.00x faster                                                           |
| xml_etree_generate   | 58.3 ms                                                               | 58.2 ms: 1.00x faster                                                           |
| unpickle_pure_python | 179 us                                                                | 179 us: 1.00x slower                                                            |
| pickle_pure_python   | 241 us                                                                | 242 us: 1.00x slower                                                            |
| json_loads           | 18.1 us                                                               | 18.2 us: 1.00x slower                                                           |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250527-darwin-arm64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a | bm-20250528-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-6783662 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 12.7 ms                                                               | 12.0 ms: 1.05x faster                                                           |
| python_startup         | 16.9 ms                                                               | 16.4 ms: 1.03x faster                                                           |
| Geometric mean         | (ref)                                                                 | 1.04x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250527-darwin-arm64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a | bm-20250528-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-6783662 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 25.2 ms                                                               | 24.9 ms: 1.01x faster                                                           |
| genshi_xml      | 36.4 ms                                                               | 36.1 ms: 1.01x faster                                                           |
| genshi_text     | 17.7 ms                                                               | 17.5 ms: 1.01x faster                                                           |
| mako            | 9.01 ms                                                               | 8.96 ms: 1.01x faster                                                           |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                                    |

All benchmarks:
===============

| Benchmark                     | bm-20250527-darwin-arm64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a | bm-20250528-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-6783662 |
|-------------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site        | 12.7 ms                                                               | 12.0 ms: 1.05x faster                                                           |
| python_startup                | 16.9 ms                                                               | 16.4 ms: 1.03x faster                                                           |
| logging_silent                | 348 ns                                                                | 340 ns: 1.02x faster                                                            |
| typing_runtime_protocols      | 111 us                                                                | 108 us: 1.02x faster                                                            |
| chaos                         | 48.3 ms                                                               | 47.7 ms: 1.01x faster                                                           |
| django_template               | 25.2 ms                                                               | 24.9 ms: 1.01x faster                                                           |
| tomli_loads                   | 1.45 sec                                                              | 1.43 sec: 1.01x faster                                                          |
| sympy_expand                  | 263 ms                                                                | 260 ms: 1.01x faster                                                            |
| deepcopy                      | 175 us                                                                | 174 us: 1.01x faster                                                            |
| deltablue                     | 2.83 ms                                                               | 2.81 ms: 1.01x faster                                                           |
| genshi_xml                    | 36.4 ms                                                               | 36.1 ms: 1.01x faster                                                           |
| genshi_text                   | 17.7 ms                                                               | 17.5 ms: 1.01x faster                                                           |
| deepcopy_reduce               | 1.91 us                                                               | 1.90 us: 1.01x faster                                                           |
| sympy_str                     | 155 ms                                                                | 154 ms: 1.01x faster                                                            |
| crypto_pyaes                  | 61.7 ms                                                               | 61.3 ms: 1.01x faster                                                           |
| nqueens                       | 71.7 ms                                                               | 71.3 ms: 1.01x faster                                                           |
| sympy_sum                     | 81.9 ms                                                               | 81.3 ms: 1.01x faster                                                           |
| mdp                           | 832 ms                                                                | 828 ms: 1.01x faster                                                            |
| mako                          | 9.01 ms                                                               | 8.96 ms: 1.01x faster                                                           |
| bpe_tokeniser                 | 3.27 sec                                                              | 3.26 sec: 1.00x faster                                                          |
| json_dumps                    | 6.87 ms                                                               | 6.85 ms: 1.00x faster                                                           |
| sqlglot_v2_normalize          | 76.3 ms                                                               | 76.0 ms: 1.00x faster                                                           |
| xml_etree_process             | 43.6 ms                                                               | 43.5 ms: 1.00x faster                                                           |
| xml_etree_generate            | 58.3 ms                                                               | 58.2 ms: 1.00x faster                                                           |
| sqlglot_v2_optimize           | 36.5 ms                                                               | 36.4 ms: 1.00x faster                                                           |
| regex_dna                     | 143 ms                                                                | 143 ms: 1.00x slower                                                            |
| go                            | 100 ms                                                                | 100 ms: 1.00x slower                                                            |
| unpickle_pure_python          | 179 us                                                                | 179 us: 1.00x slower                                                            |
| pyflate                       | 338 ms                                                                | 339 ms: 1.00x slower                                                            |
| sqlite_synth                  | 1.62 us                                                               | 1.62 us: 1.00x slower                                                           |
| fannkuch                      | 310 ms                                                                | 311 ms: 1.00x slower                                                            |
| regex_effbot                  | 2.34 ms                                                               | 2.35 ms: 1.00x slower                                                           |
| shortest_path                 | 341 ms                                                                | 342 ms: 1.00x slower                                                            |
| create_gc_cycles              | 1.35 ms                                                               | 1.36 ms: 1.00x slower                                                           |
| pickle_pure_python            | 241 us                                                                | 242 us: 1.00x slower                                                            |
| async_tree_eager_cpu_io_mixed | 369 ms                                                                | 370 ms: 1.00x slower                                                            |
| json_loads                    | 18.1 us                                                               | 18.2 us: 1.00x slower                                                           |
| regex_compile                 | 81.2 ms                                                               | 81.5 ms: 1.00x slower                                                           |
| dulwich_log                   | 26.7 ms                                                               | 26.9 ms: 1.00x slower                                                           |
| scimark_sparse_mat_mult       | 3.19 ms                                                               | 3.21 ms: 1.00x slower                                                           |
| async_tree_cpu_io_mixed_tg    | 425 ms                                                                | 427 ms: 1.01x slower                                                            |
| scimark_sor                   | 91.3 ms                                                               | 91.8 ms: 1.01x slower                                                           |
| async_tree_eager              | 73.1 ms                                                               | 73.5 ms: 1.01x slower                                                           |
| subparsers                    | 14.9 ms                                                               | 15.0 ms: 1.01x slower                                                           |
| many_optionals                | 495 us                                                                | 498 us: 1.01x slower                                                            |
| logging_simple                | 4.05 us                                                               | 4.09 us: 1.01x slower                                                           |
| pprint_safe_repr              | 620 ms                                                                | 625 ms: 1.01x slower                                                            |
| deepcopy_memo                 | 21.8 us                                                               | 22.0 us: 1.01x slower                                                           |
| telco                         | 4.76 ms                                                               | 4.81 ms: 1.01x slower                                                           |
| logging_format                | 4.34 us                                                               | 4.39 us: 1.01x slower                                                           |
| pprint_pformat                | 1.26 sec                                                              | 1.27 sec: 1.01x slower                                                          |
| spectral_norm                 | 74.7 ms                                                               | 75.6 ms: 1.01x slower                                                           |
| async_tree_none               | 184 ms                                                                | 186 ms: 1.01x slower                                                            |
| scimark_monte_carlo           | 52.9 ms                                                               | 53.6 ms: 1.01x slower                                                           |
| scimark_fft                   | 207 ms                                                                | 210 ms: 1.01x slower                                                            |
| float                         | 58.5 ms                                                               | 59.4 ms: 1.02x slower                                                           |
| scimark_lu                    | 83.9 ms                                                               | 85.3 ms: 1.02x slower                                                           |
| Geometric mean                | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (46): pylint, sphinx, pycparser, async_tree_io_tg, html5lib, async_tree_eager_memoization, async_tree_none_tg, regex_v8, coroutines, docutils, sympy_integrate, 2to3, async_tree_memoization_tg, asyncio_websockets, async_tree_eager_memoization_tg, gc_traversal, async_tree_memoization, async_tree_eager_io, meteor_contest, async_tree_eager_io_tg, richards_super, async_tree_eager_tg, nbody, sqlglot_v2_transpile, async_tree_eager_cpu_io_mixed_tg, xml_etree_parse, async_tree_io, pidigits, dask, raytrace, generators, coverage, sqlglot_v2_parse, connected_components, xml_etree_iterparse, k_core, bench_thread_pool, thrift, json, hexiom, pathlib, async_tree_cpu_io_mixed, richards, comprehensions, async_generators, bench_mp_pool

- Geometric mean (including insignificant results): 1.000x faster

# HPT report

- Reliability score: 72.82% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x