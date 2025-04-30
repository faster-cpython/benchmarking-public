# Results vs. base

- fork: faster-cpython
- ref: virtual_iterators
- machine: darwin-arm64
- commit hash: cad1946
- commit date: 2025-04-30
- overall geometric mean: 1.006x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250430-darwin-arm64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 | bm-20250430-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 190 ms                                                                 | 219 ms: 1.15x slower                                                          |
| docutils       | 1.55 sec                                                               | 1.53 sec: 1.01x faster                                                        |
| sphinx         | 632 ms                                                                 | 619 ms: 1.02x faster                                                          |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                                  |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250430-darwin-arm64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 | bm-20250430-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_eager                 | 78.1 ms                                                                | 76.7 ms: 1.02x faster                                                         |
| async_tree_none                  | 191 ms                                                                 | 188 ms: 1.02x faster                                                          |
| async_tree_memoization           | 229 ms                                                                 | 226 ms: 1.01x faster                                                          |
| async_generators                 | 279 ms                                                                 | 277 ms: 1.01x faster                                                          |
| async_tree_eager_cpu_io_mixed_tg | 402 ms                                                                 | 404 ms: 1.00x slower                                                          |
| asyncio_websockets               | 242 ms                                                                 | 244 ms: 1.01x slower                                                          |
| async_tree_memoization_tg        | 210 ms                                                                 | 212 ms: 1.01x slower                                                          |
| async_tree_eager_io_tg           | 409 ms                                                                 | 413 ms: 1.01x slower                                                          |
| Geometric mean                   | (ref)                                                                  | 1.00x faster                                                                  |

Benchmark hidden because not significant (11): async_tree_eager_memoization, async_tree_eager_cpu_io_mixed, async_tree_eager_tg, async_tree_cpu_io_mixed, async_tree_eager_io, async_tree_eager_memoization_tg, coroutines, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250430-darwin-arm64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 | bm-20250430-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 93.6 ms                                                                | 89.1 ms: 1.05x faster                                                         |
| float          | 58.5 ms                                                                | 57.7 ms: 1.01x faster                                                         |
| pidigits       | 284 ms                                                                 | 284 ms: 1.00x faster                                                          |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250430-darwin-arm64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 | bm-20250430-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 2.27 ms                                                                | 2.24 ms: 1.01x faster                                                         |
| regex_compile  | 86.5 ms                                                                | 85.4 ms: 1.01x faster                                                         |
| regex_v8       | 15.9 ms                                                                | 15.8 ms: 1.01x faster                                                         |
| regex_dna      | 141 ms                                                                 | 140 ms: 1.00x faster                                                          |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250430-darwin-arm64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 | bm-20250430-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 1.52 sec                                                               | 1.50 sec: 1.02x faster                                                        |
| xml_etree_process    | 45.7 ms                                                                | 45.0 ms: 1.02x faster                                                         |
| unpickle_pure_python | 186 us                                                                 | 183 us: 1.02x faster                                                          |
| pickle_pure_python   | 253 us                                                                 | 251 us: 1.01x faster                                                          |
| xml_etree_generate   | 62.0 ms                                                                | 61.4 ms: 1.01x faster                                                         |
| xml_etree_iterparse  | 76.1 ms                                                                | 75.7 ms: 1.01x faster                                                         |
| json_dumps           | 8.13 ms                                                                | 8.16 ms: 1.00x slower                                                         |
| json_loads           | 18.6 us                                                                | 18.8 us: 1.01x slower                                                         |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                                  |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250430-darwin-arm64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 | bm-20250430-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 14.6 ms                                                                | 14.7 ms: 1.00x slower                                                         |
| python_startup         | 19.7 ms                                                                | 19.8 ms: 1.01x slower                                                         |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250430-darwin-arm64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 | bm-20250430-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|-----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| django_template | 26.2 ms                                                                | 25.6 ms: 1.02x faster                                                         |
| genshi_xml      | 37.5 ms                                                                | 36.7 ms: 1.02x faster                                                         |
| genshi_text     | 18.5 ms                                                                | 18.2 ms: 1.02x faster                                                         |
| mako            | 9.16 ms                                                                | 9.07 ms: 1.01x faster                                                         |
| Geometric mean  | (ref)                                                                  | 1.02x faster                                                                  |

All benchmarks:
===============

| Benchmark                        | bm-20250430-darwin-arm64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 | bm-20250430-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| comprehensions                   | 14.5 us                                                                | 13.7 us: 1.06x faster                                                         |
| nbody                            | 93.6 ms                                                                | 89.1 ms: 1.05x faster                                                         |
| typing_runtime_protocols         | 112 us                                                                 | 107 us: 1.04x faster                                                          |
| go                               | 105 ms                                                                 | 102 ms: 1.03x faster                                                          |
| hexiom                           | 5.46 ms                                                                | 5.33 ms: 1.03x faster                                                         |
| sqlglot_v2_normalize             | 79.4 ms                                                                | 77.6 ms: 1.02x faster                                                         |
| django_template                  | 26.2 ms                                                                | 25.6 ms: 1.02x faster                                                         |
| pprint_pformat                   | 1.17 sec                                                               | 1.15 sec: 1.02x faster                                                        |
| sqlalchemy_declarative           | 66.5 ms                                                                | 65.1 ms: 1.02x faster                                                         |
| genshi_xml                       | 37.5 ms                                                                | 36.7 ms: 1.02x faster                                                         |
| sphinx                           | 632 ms                                                                 | 619 ms: 1.02x faster                                                          |
| pprint_safe_repr                 | 579 ms                                                                 | 568 ms: 1.02x faster                                                          |
| bench_thread_pool                | 553 us                                                                 | 542 us: 1.02x faster                                                          |
| mdp                              | 872 ms                                                                 | 855 ms: 1.02x faster                                                          |
| deepcopy_memo                    | 24.0 us                                                                | 23.6 us: 1.02x faster                                                         |
| deepcopy                         | 188 us                                                                 | 184 us: 1.02x faster                                                          |
| sqlglot_v2_optimize              | 37.5 ms                                                                | 36.8 ms: 1.02x faster                                                         |
| logging_silent                   | 79.9 ns                                                                | 78.5 ns: 1.02x faster                                                         |
| async_tree_eager                 | 78.1 ms                                                                | 76.7 ms: 1.02x faster                                                         |
| genshi_text                      | 18.5 ms                                                                | 18.2 ms: 1.02x faster                                                         |
| tomli_loads                      | 1.52 sec                                                               | 1.50 sec: 1.02x faster                                                        |
| nqueens                          | 75.3 ms                                                                | 74.0 ms: 1.02x faster                                                         |
| logging_format                   | 4.30 us                                                                | 4.23 us: 1.02x faster                                                         |
| async_tree_none                  | 191 ms                                                                 | 188 ms: 1.02x faster                                                          |
| xml_etree_process                | 45.7 ms                                                                | 45.0 ms: 1.02x faster                                                         |
| many_optionals                   | 497 us                                                                 | 489 us: 1.02x faster                                                          |
| raytrace                         | 206 ms                                                                 | 203 ms: 1.02x faster                                                          |
| pyflate                          | 351 ms                                                                 | 346 ms: 1.02x faster                                                          |
| unpickle_pure_python             | 186 us                                                                 | 183 us: 1.02x faster                                                          |
| async_tree_memoization           | 229 ms                                                                 | 226 ms: 1.01x faster                                                          |
| regex_effbot                     | 2.27 ms                                                                | 2.24 ms: 1.01x faster                                                         |
| float                            | 58.5 ms                                                                | 57.7 ms: 1.01x faster                                                         |
| regex_compile                    | 86.5 ms                                                                | 85.4 ms: 1.01x faster                                                         |
| scimark_sor                      | 95.0 ms                                                                | 93.8 ms: 1.01x faster                                                         |
| docutils                         | 1.55 sec                                                               | 1.53 sec: 1.01x faster                                                        |
| sqlalchemy_imperative            | 7.46 ms                                                                | 7.37 ms: 1.01x faster                                                         |
| generators                       | 31.4 ms                                                                | 31.0 ms: 1.01x faster                                                         |
| pickle_pure_python               | 253 us                                                                 | 251 us: 1.01x faster                                                          |
| spectral_norm                    | 78.2 ms                                                                | 77.4 ms: 1.01x faster                                                         |
| async_generators                 | 279 ms                                                                 | 277 ms: 1.01x faster                                                          |
| logging_simple                   | 3.98 us                                                                | 3.94 us: 1.01x faster                                                         |
| xml_etree_generate               | 62.0 ms                                                                | 61.4 ms: 1.01x faster                                                         |
| mako                             | 9.16 ms                                                                | 9.07 ms: 1.01x faster                                                         |
| subparsers                       | 13.7 ms                                                                | 13.6 ms: 1.01x faster                                                         |
| sqlglot_v2_transpile             | 1.16 ms                                                                | 1.16 ms: 1.01x faster                                                         |
| scimark_monte_carlo              | 54.0 ms                                                                | 53.6 ms: 1.01x faster                                                         |
| regex_v8                         | 15.9 ms                                                                | 15.8 ms: 1.01x faster                                                         |
| fannkuch                         | 318 ms                                                                 | 316 ms: 1.01x faster                                                          |
| meteor_contest                   | 77.9 ms                                                                | 77.5 ms: 1.01x faster                                                         |
| xml_etree_iterparse              | 76.1 ms                                                                | 75.7 ms: 1.01x faster                                                         |
| scimark_fft                      | 210 ms                                                                 | 209 ms: 1.01x faster                                                          |
| sqlglot_v2_parse                 | 988 us                                                                 | 984 us: 1.00x faster                                                          |
| regex_dna                        | 141 ms                                                                 | 140 ms: 1.00x faster                                                          |
| dulwich_log                      | 27.3 ms                                                                | 27.2 ms: 1.00x faster                                                         |
| coverage                         | 50.4 ms                                                                | 50.3 ms: 1.00x faster                                                         |
| pidigits                         | 284 ms                                                                 | 284 ms: 1.00x faster                                                          |
| richards_super                   | 44.0 ms                                                                | 44.1 ms: 1.00x slower                                                         |
| scimark_lu                       | 83.0 ms                                                                | 83.3 ms: 1.00x slower                                                         |
| json_dumps                       | 8.13 ms                                                                | 8.16 ms: 1.00x slower                                                         |
| python_startup_no_site           | 14.6 ms                                                                | 14.7 ms: 1.00x slower                                                         |
| async_tree_eager_cpu_io_mixed_tg | 402 ms                                                                 | 404 ms: 1.00x slower                                                          |
| bpe_tokeniser                    | 3.36 sec                                                               | 3.38 sec: 1.01x slower                                                        |
| shortest_path                    | 339 ms                                                                 | 341 ms: 1.01x slower                                                          |
| python_startup                   | 19.7 ms                                                                | 19.8 ms: 1.01x slower                                                         |
| asyncio_websockets               | 242 ms                                                                 | 244 ms: 1.01x slower                                                          |
| async_tree_memoization_tg        | 210 ms                                                                 | 212 ms: 1.01x slower                                                          |
| async_tree_eager_io_tg           | 409 ms                                                                 | 413 ms: 1.01x slower                                                          |
| json_loads                       | 18.6 us                                                                | 18.8 us: 1.01x slower                                                         |
| create_gc_cycles                 | 1.28 ms                                                                | 1.30 ms: 1.01x slower                                                         |
| json                             | 3.18 ms                                                                | 3.24 ms: 1.02x slower                                                         |
| connected_components             | 311 ms                                                                 | 317 ms: 1.02x slower                                                          |
| 2to3                             | 190 ms                                                                 | 219 ms: 1.15x slower                                                          |
| Geometric mean                   | (ref)                                                                  | 1.01x faster                                                                  |

Benchmark hidden because not significant (26): pathlib, html5lib, pycparser, async_tree_eager_memoization, xml_etree_parse, scimark_sparse_mat_mult, telco, k_core, richards, gc_traversal, async_tree_eager_cpu_io_mixed, deltablue, async_tree_eager_tg, async_tree_cpu_io_mixed, async_tree_eager_io, sqlite_synth, async_tree_eager_memoization_tg, coroutines, chaos, async_tree_io, crypto_pyaes, deepcopy_reduce, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_none_tg, bench_mp_pool
Ignored benchmarks (5) of results/bm-20250430-3.14.0a7+-44e4c47/bm-20250430-darwin-arm64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47.json: pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum

- Geometric mean (including insignificant results): 1.006x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x