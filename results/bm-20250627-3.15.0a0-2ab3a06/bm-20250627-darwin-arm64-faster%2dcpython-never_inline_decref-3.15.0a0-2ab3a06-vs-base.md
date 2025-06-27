# Results vs. base

- fork: faster-cpython
- ref: never_inline_decref
- machine: darwin-arm64
- commit hash: 2ab3a06
- commit date: 2025-06-27
- overall geometric mean: 1.001x faster
- HPT reliability: 99.93%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250626-darwin-arm64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 | bm-20250627-darwin-arm64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 187 ms                                                                | 191 ms: 1.02x slower                                                           |
| docutils       | 1.53 sec                                                              | 1.53 sec: 1.01x slower                                                         |
| html5lib       | 104 ms                                                                | 36.4 ms: 2.87x faster                                                          |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                                   |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250626-darwin-arm64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 | bm-20250627-darwin-arm64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization           | 217 ms                                                                | 218 ms: 1.00x slower                                                           |
| async_tree_cpu_io_mixed          | 436 ms                                                                | 438 ms: 1.01x slower                                                           |
| async_tree_cpu_io_mixed_tg       | 423 ms                                                                | 425 ms: 1.01x slower                                                           |
| async_tree_eager_cpu_io_mixed_tg | 401 ms                                                                | 403 ms: 1.01x slower                                                           |
| async_tree_eager                 | 73.0 ms                                                               | 73.7 ms: 1.01x slower                                                          |
| coroutines                       | 18.7 ms                                                               | 19.0 ms: 1.01x slower                                                          |
| async_tree_eager_cpu_io_mixed    | 367 ms                                                                | 372 ms: 1.01x slower                                                           |
| async_tree_eager_memoization     | 150 ms                                                                | 152 ms: 1.02x slower                                                           |
| async_tree_eager_tg              | 141 ms                                                                | 144 ms: 1.02x slower                                                           |
| async_generators                 | 277 ms                                                                | 285 ms: 1.03x slower                                                           |
| Geometric mean                   | (ref)                                                                 | 1.01x slower                                                                   |

Benchmark hidden because not significant (9): async_tree_none_tg, async_tree_eager_io_tg, async_tree_io_tg, asyncio_websockets, async_tree_none, async_tree_memoization_tg, async_tree_eager_memoization_tg, async_tree_eager_io, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250626-darwin-arm64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 | bm-20250627-darwin-arm64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 284 ms                                                                | 284 ms: 1.00x faster                                                           |
| nbody          | 85.2 ms                                                               | 85.4 ms: 1.00x slower                                                          |
| float          | 57.1 ms                                                               | 58.2 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250626-darwin-arm64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 | bm-20250627-darwin-arm64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 143 ms                                                                | 139 ms: 1.03x faster                                                           |
| regex_v8       | 16.2 ms                                                               | 15.9 ms: 1.02x faster                                                          |
| regex_effbot   | 2.37 ms                                                               | 2.35 ms: 1.01x faster                                                          |
| regex_compile  | 81.0 ms                                                               | 81.8 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250626-darwin-arm64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 | bm-20250627-darwin-arm64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|---------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads         | 1.43 sec                                                              | 1.45 sec: 1.01x slower                                                         |
| xml_etree_iterparse | 74.3 ms                                                               | 76.2 ms: 1.03x slower                                                          |
| json_loads          | 16.5 us                                                               | 17.1 us: 1.03x slower                                                          |
| json_dumps          | 6.82 ms                                                               | 7.12 ms: 1.04x slower                                                          |
| xml_etree_process   | 43.4 ms                                                               | 45.3 ms: 1.04x slower                                                          |
| xml_etree_parse     | 104 ms                                                                | 110 ms: 1.05x slower                                                           |
| xml_etree_generate  | 58.8 ms                                                               | 62.1 ms: 1.06x slower                                                          |
| Geometric mean      | (ref)                                                                 | 1.03x slower                                                                   |

Benchmark hidden because not significant (2): pickle_pure_python, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250626-darwin-arm64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 | bm-20250627-darwin-arm64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                               | 18.1 ms: 1.02x slower                                                          |
| python_startup_no_site | 13.3 ms                                                               | 13.6 ms: 1.02x slower                                                          |
| Geometric mean         | (ref)                                                                 | 1.02x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250626-darwin-arm64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 | bm-20250627-darwin-arm64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| django_template | 26.4 ms                                                               | 25.0 ms: 1.06x faster                                                          |
| genshi_xml      | 37.2 ms                                                               | 37.5 ms: 1.01x slower                                                          |
| genshi_text     | 18.6 ms                                                               | 18.8 ms: 1.01x slower                                                          |
| mako            | 9.02 ms                                                               | 9.21 ms: 1.02x slower                                                          |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                                   |

All benchmarks:
===============

| Benchmark                        | bm-20250626-darwin-arm64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 | bm-20250627-darwin-arm64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| html5lib                         | 104 ms                                                                | 36.4 ms: 2.87x faster                                                          |
| richards_super                   | 44.8 ms                                                               | 42.0 ms: 1.07x faster                                                          |
| django_template                  | 26.4 ms                                                               | 25.0 ms: 1.06x faster                                                          |
| pprint_pformat                   | 1.19 sec                                                              | 1.14 sec: 1.04x faster                                                         |
| pprint_safe_repr                 | 583 ms                                                                | 561 ms: 1.04x faster                                                           |
| logging_simple                   | 3.95 us                                                               | 3.82 us: 1.04x faster                                                          |
| logging_format                   | 4.26 us                                                               | 4.12 us: 1.03x faster                                                          |
| scimark_monte_carlo              | 54.7 ms                                                               | 53.0 ms: 1.03x faster                                                          |
| regex_dna                        | 143 ms                                                                | 139 ms: 1.03x faster                                                           |
| scimark_fft                      | 208 ms                                                                | 202 ms: 1.03x faster                                                           |
| chaos                            | 46.9 ms                                                               | 45.7 ms: 1.03x faster                                                          |
| scimark_sor                      | 92.6 ms                                                               | 90.3 ms: 1.02x faster                                                          |
| regex_v8                         | 16.2 ms                                                               | 15.9 ms: 1.02x faster                                                          |
| richards                         | 37.9 ms                                                               | 37.3 ms: 1.02x faster                                                          |
| raytrace                         | 210 ms                                                                | 206 ms: 1.02x faster                                                           |
| sqlite_synth                     | 1.64 us                                                               | 1.62 us: 1.01x faster                                                          |
| connected_components             | 305 ms                                                                | 302 ms: 1.01x faster                                                           |
| regex_effbot                     | 2.37 ms                                                               | 2.35 ms: 1.01x faster                                                          |
| dask                             | 771 ms                                                                | 768 ms: 1.00x faster                                                           |
| crypto_pyaes                     | 61.0 ms                                                               | 60.9 ms: 1.00x faster                                                          |
| pidigits                         | 284 ms                                                                | 284 ms: 1.00x faster                                                           |
| nbody                            | 85.2 ms                                                               | 85.4 ms: 1.00x slower                                                          |
| comprehensions                   | 13.2 us                                                               | 13.2 us: 1.00x slower                                                          |
| dulwich_log                      | 26.5 ms                                                               | 26.6 ms: 1.00x slower                                                          |
| async_tree_memoization           | 217 ms                                                                | 218 ms: 1.00x slower                                                           |
| spectral_norm                    | 72.3 ms                                                               | 72.7 ms: 1.01x slower                                                          |
| docutils                         | 1.53 sec                                                              | 1.53 sec: 1.01x slower                                                         |
| async_tree_cpu_io_mixed          | 436 ms                                                                | 438 ms: 1.01x slower                                                           |
| async_tree_cpu_io_mixed_tg       | 423 ms                                                                | 425 ms: 1.01x slower                                                           |
| async_tree_eager_cpu_io_mixed_tg | 401 ms                                                                | 403 ms: 1.01x slower                                                           |
| genshi_xml                       | 37.2 ms                                                               | 37.5 ms: 1.01x slower                                                          |
| scimark_lu                       | 85.8 ms                                                               | 86.5 ms: 1.01x slower                                                          |
| generators                       | 31.5 ms                                                               | 31.7 ms: 1.01x slower                                                          |
| genshi_text                      | 18.6 ms                                                               | 18.8 ms: 1.01x slower                                                          |
| sympy_integrate                  | 11.3 ms                                                               | 11.3 ms: 1.01x slower                                                          |
| async_tree_eager                 | 73.0 ms                                                               | 73.7 ms: 1.01x slower                                                          |
| tomli_loads                      | 1.43 sec                                                              | 1.45 sec: 1.01x slower                                                         |
| regex_compile                    | 81.0 ms                                                               | 81.8 ms: 1.01x slower                                                          |
| hexiom                           | 5.09 ms                                                               | 5.14 ms: 1.01x slower                                                          |
| coroutines                       | 18.7 ms                                                               | 19.0 ms: 1.01x slower                                                          |
| json                             | 2.95 ms                                                               | 2.99 ms: 1.01x slower                                                          |
| async_tree_eager_cpu_io_mixed    | 367 ms                                                                | 372 ms: 1.01x slower                                                           |
| deepcopy_reduce                  | 1.89 us                                                               | 1.92 us: 1.02x slower                                                          |
| python_startup                   | 17.8 ms                                                               | 18.1 ms: 1.02x slower                                                          |
| async_tree_eager_memoization     | 150 ms                                                                | 152 ms: 1.02x slower                                                           |
| sqlglot_v2_optimize              | 36.4 ms                                                               | 37.0 ms: 1.02x slower                                                          |
| sympy_sum                        | 80.6 ms                                                               | 82.1 ms: 1.02x slower                                                          |
| async_tree_eager_tg              | 141 ms                                                                | 144 ms: 1.02x slower                                                           |
| python_startup_no_site           | 13.3 ms                                                               | 13.6 ms: 1.02x slower                                                          |
| sympy_str                        | 154 ms                                                                | 157 ms: 1.02x slower                                                           |
| float                            | 57.1 ms                                                               | 58.2 ms: 1.02x slower                                                          |
| mako                             | 9.02 ms                                                               | 9.21 ms: 1.02x slower                                                          |
| 2to3                             | 187 ms                                                                | 191 ms: 1.02x slower                                                           |
| bpe_tokeniser                    | 3.23 sec                                                              | 3.30 sec: 1.02x slower                                                         |
| logging_silent                   | 77.0 ns                                                               | 78.7 ns: 1.02x slower                                                          |
| sympy_expand                     | 259 ms                                                                | 266 ms: 1.02x slower                                                           |
| deltablue                        | 2.74 ms                                                               | 2.81 ms: 1.02x slower                                                          |
| xml_etree_iterparse              | 74.3 ms                                                               | 76.2 ms: 1.03x slower                                                          |
| sqlglot_v2_normalize             | 75.7 ms                                                               | 77.7 ms: 1.03x slower                                                          |
| async_generators                 | 277 ms                                                                | 285 ms: 1.03x slower                                                           |
| json_loads                       | 16.5 us                                                               | 17.1 us: 1.03x slower                                                          |
| deepcopy_memo                    | 22.0 us                                                               | 22.8 us: 1.03x slower                                                          |
| mdp                              | 817 ms                                                                | 848 ms: 1.04x slower                                                           |
| meteor_contest                   | 74.4 ms                                                               | 77.2 ms: 1.04x slower                                                          |
| nqueens                          | 71.3 ms                                                               | 74.3 ms: 1.04x slower                                                          |
| json_dumps                       | 6.82 ms                                                               | 7.12 ms: 1.04x slower                                                          |
| xml_etree_process                | 43.4 ms                                                               | 45.3 ms: 1.04x slower                                                          |
| sqlglot_v2_transpile             | 1.12 ms                                                               | 1.17 ms: 1.05x slower                                                          |
| xml_etree_parse                  | 104 ms                                                                | 110 ms: 1.05x slower                                                           |
| telco                            | 4.79 ms                                                               | 5.04 ms: 1.05x slower                                                          |
| xml_etree_generate               | 58.8 ms                                                               | 62.1 ms: 1.06x slower                                                          |
| sqlglot_v2_parse                 | 938 us                                                                | 992 us: 1.06x slower                                                           |
| go                               | 99.6 ms                                                               | 106 ms: 1.06x slower                                                           |
| deepcopy                         | 175 us                                                                | 187 us: 1.07x slower                                                           |
| coverage                         | 49.7 ms                                                               | 53.2 ms: 1.07x slower                                                          |
| pyflate                          | 334 ms                                                                | 357 ms: 1.07x slower                                                           |
| pathlib                          | 22.6 ms                                                               | 24.8 ms: 1.10x slower                                                          |
| fannkuch                         | 290 ms                                                                | 321 ms: 1.11x slower                                                           |
| Geometric mean                   | (ref)                                                                 | 1.00x faster                                                                   |

Benchmark hidden because not significant (23): async_tree_none_tg, async_tree_eager_io_tg, async_tree_io_tg, scimark_sparse_mat_mult, pylint, sphinx, create_gc_cycles, shortest_path, thrift, asyncio_websockets, pickle_pure_python, unpickle_pure_python, subparsers, async_tree_none, gc_traversal, many_optionals, typing_runtime_protocols, pycparser, async_tree_memoization_tg, async_tree_eager_memoization_tg, async_tree_eager_io, async_tree_io, k_core

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 99.93% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x