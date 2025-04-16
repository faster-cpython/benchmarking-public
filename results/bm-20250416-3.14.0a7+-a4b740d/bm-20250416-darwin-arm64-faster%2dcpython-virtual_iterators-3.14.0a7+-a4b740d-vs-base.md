# Results vs. base

- fork: faster-cpython
- ref: virtual_iterators
- machine: darwin-arm64
- commit hash: a4b740d
- commit date: 2025-04-16
- overall geometric mean: 1.003x faster
- HPT reliability: 96.73%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250414-darwin-arm64-python-844596c09fc812a58ac1-3.14.0a7+-844596c | bm-20250416-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 187 ms                                                                 | 218 ms: 1.17x slower                                                          |
| docutils       | 1.54 sec                                                               | 1.59 sec: 1.03x slower                                                        |
| html5lib       | 35.0 ms                                                                | 36.3 ms: 1.04x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.06x slower                                                                  |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250414-darwin-arm64-python-844596c09fc812a58ac1-3.14.0a7+-844596c | bm-20250416-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_eager_io              | 414 ms                                                                 | 405 ms: 1.02x faster                                                          |
| async_tree_memoization           | 224 ms                                                                 | 221 ms: 1.01x faster                                                          |
| async_tree_cpu_io_mixed          | 437 ms                                                                 | 431 ms: 1.01x faster                                                          |
| async_tree_eager                 | 75.8 ms                                                                | 75.2 ms: 1.01x faster                                                         |
| async_tree_io_tg                 | 409 ms                                                                 | 406 ms: 1.01x faster                                                          |
| async_tree_cpu_io_mixed_tg       | 426 ms                                                                 | 424 ms: 1.00x faster                                                          |
| async_tree_eager_cpu_io_mixed_tg | 400 ms                                                                 | 404 ms: 1.01x slower                                                          |
| asyncio_websockets               | 243 ms                                                                 | 245 ms: 1.01x slower                                                          |
| coroutines                       | 19.5 ms                                                                | 20.3 ms: 1.04x slower                                                         |
| Geometric mean                   | (ref)                                                                  | 1.00x faster                                                                  |

Benchmark hidden because not significant (10): async_tree_io, async_tree_eager_memoization, async_generators, async_tree_none, async_tree_none_tg, async_tree_eager_tg, async_tree_eager_io_tg, async_tree_eager_cpu_io_mixed, async_tree_memoization_tg, async_tree_eager_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250414-darwin-arm64-python-844596c09fc812a58ac1-3.14.0a7+-844596c | bm-20250416-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 89.5 ms                                                                | 87.0 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                  |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250414-darwin-arm64-python-844596c09fc812a58ac1-3.14.0a7+-844596c | bm-20250416-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 84.8 ms                                                                | 82.8 ms: 1.02x faster                                                         |
| regex_v8       | 15.7 ms                                                                | 15.8 ms: 1.01x slower                                                         |
| regex_effbot   | 2.24 ms                                                                | 2.30 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                  |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250414-darwin-arm64-python-844596c09fc812a58ac1-3.14.0a7+-844596c | bm-20250416-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| unpickle_pure_python | 186 us                                                                 | 181 us: 1.03x faster                                                          |
| pickle_pure_python   | 252 us                                                                 | 247 us: 1.02x faster                                                          |
| xml_etree_process    | 46.8 ms                                                                | 46.0 ms: 1.02x faster                                                         |
| xml_etree_generate   | 63.2 ms                                                                | 62.2 ms: 1.02x faster                                                         |
| tomli_loads          | 1.50 sec                                                               | 1.48 sec: 1.01x faster                                                        |
| json_loads           | 17.7 us                                                                | 17.8 us: 1.01x slower                                                         |
| json_dumps           | 7.71 ms                                                                | 7.78 ms: 1.01x slower                                                         |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                                  |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250414-darwin-arm64-python-844596c09fc812a58ac1-3.14.0a7+-844596c | bm-20250416-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 14.7 ms                                                                | 14.7 ms: 1.00x faster                                                         |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                  |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250414-darwin-arm64-python-844596c09fc812a58ac1-3.14.0a7+-844596c | bm-20250416-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|-----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 9.07 ms                                                                | 8.88 ms: 1.02x faster                                                         |
| genshi_xml      | 37.9 ms                                                                | 37.4 ms: 1.01x faster                                                         |
| django_template | 26.3 ms                                                                | 26.9 ms: 1.02x slower                                                         |
| genshi_text     | 18.5 ms                                                                | 19.4 ms: 1.05x slower                                                         |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                                  |

All benchmarks:
===============

| Benchmark                        | bm-20250414-darwin-arm64-python-844596c09fc812a58ac1-3.14.0a7+-844596c | bm-20250416-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pprint_safe_repr                 | 630 ms                                                                 | 578 ms: 1.09x faster                                                          |
| pprint_pformat                   | 1.28 sec                                                               | 1.17 sec: 1.09x faster                                                        |
| comprehensions                   | 14.1 us                                                                | 13.1 us: 1.08x faster                                                         |
| richards                         | 41.4 ms                                                                | 39.0 ms: 1.06x faster                                                         |
| typing_runtime_protocols         | 109 us                                                                 | 105 us: 1.04x faster                                                          |
| sqlglot_v2_normalize             | 78.6 ms                                                                | 75.8 ms: 1.04x faster                                                         |
| many_optionals                   | 495 us                                                                 | 478 us: 1.04x faster                                                          |
| hexiom                           | 5.30 ms                                                                | 5.12 ms: 1.03x faster                                                         |
| mdp                              | 878 ms                                                                 | 849 ms: 1.03x faster                                                          |
| nbody                            | 89.5 ms                                                                | 87.0 ms: 1.03x faster                                                         |
| unpickle_pure_python             | 186 us                                                                 | 181 us: 1.03x faster                                                          |
| go                               | 109 ms                                                                 | 106 ms: 1.03x faster                                                          |
| regex_compile                    | 84.8 ms                                                                | 82.8 ms: 1.02x faster                                                         |
| sqlalchemy_declarative           | 65.9 ms                                                                | 64.4 ms: 1.02x faster                                                         |
| deepcopy_memo                    | 23.6 us                                                                | 23.1 us: 1.02x faster                                                         |
| async_tree_eager_io              | 414 ms                                                                 | 405 ms: 1.02x faster                                                          |
| mako                             | 9.07 ms                                                                | 8.88 ms: 1.02x faster                                                         |
| deepcopy                         | 181 us                                                                 | 177 us: 1.02x faster                                                          |
| pickle_pure_python               | 252 us                                                                 | 247 us: 1.02x faster                                                          |
| sqlglot_v2_optimize              | 37.1 ms                                                                | 36.3 ms: 1.02x faster                                                         |
| bench_thread_pool                | 552 us                                                                 | 542 us: 1.02x faster                                                          |
| xml_etree_process                | 46.8 ms                                                                | 46.0 ms: 1.02x faster                                                         |
| sqlglot_v2_transpile             | 1.16 ms                                                                | 1.14 ms: 1.02x faster                                                         |
| sqlalchemy_imperative            | 7.60 ms                                                                | 7.48 ms: 1.02x faster                                                         |
| xml_etree_generate               | 63.2 ms                                                                | 62.2 ms: 1.02x faster                                                         |
| raytrace                         | 206 ms                                                                 | 202 ms: 1.02x faster                                                          |
| async_tree_memoization           | 224 ms                                                                 | 221 ms: 1.01x faster                                                          |
| meteor_contest                   | 77.3 ms                                                                | 76.1 ms: 1.01x faster                                                         |
| async_tree_cpu_io_mixed          | 437 ms                                                                 | 431 ms: 1.01x faster                                                          |
| pyflate                          | 343 ms                                                                 | 338 ms: 1.01x faster                                                          |
| genshi_xml                       | 37.9 ms                                                                | 37.4 ms: 1.01x faster                                                         |
| fannkuch                         | 319 ms                                                                 | 315 ms: 1.01x faster                                                          |
| nqueens                          | 73.9 ms                                                                | 73.0 ms: 1.01x faster                                                         |
| tomli_loads                      | 1.50 sec                                                               | 1.48 sec: 1.01x faster                                                        |
| generators                       | 32.0 ms                                                                | 31.8 ms: 1.01x faster                                                         |
| sqlglot_v2_parse                 | 971 us                                                                 | 963 us: 1.01x faster                                                          |
| async_tree_eager                 | 75.8 ms                                                                | 75.2 ms: 1.01x faster                                                         |
| subparsers                       | 13.7 ms                                                                | 13.6 ms: 1.01x faster                                                         |
| async_tree_io_tg                 | 409 ms                                                                 | 406 ms: 1.01x faster                                                          |
| dulwich_log                      | 26.9 ms                                                                | 26.8 ms: 1.01x faster                                                         |
| logging_silent                   | 78.4 ns                                                                | 78.0 ns: 1.01x faster                                                         |
| async_tree_cpu_io_mixed_tg       | 426 ms                                                                 | 424 ms: 1.00x faster                                                          |
| python_startup_no_site           | 14.7 ms                                                                | 14.7 ms: 1.00x faster                                                         |
| shortest_path                    | 341 ms                                                                 | 341 ms: 1.00x slower                                                          |
| coverage                         | 48.7 ms                                                                | 48.8 ms: 1.00x slower                                                         |
| bench_mp_pool                    | 66.1 ms                                                                | 66.3 ms: 1.00x slower                                                         |
| sqlite_synth                     | 1.58 us                                                                | 1.59 us: 1.01x slower                                                         |
| scimark_sor                      | 93.2 ms                                                                | 93.7 ms: 1.01x slower                                                         |
| gc_traversal                     | 3.11 ms                                                                | 3.13 ms: 1.01x slower                                                         |
| bpe_tokeniser                    | 3.30 sec                                                               | 3.32 sec: 1.01x slower                                                        |
| json_loads                       | 17.7 us                                                                | 17.8 us: 1.01x slower                                                         |
| scimark_sparse_mat_mult          | 3.16 ms                                                                | 3.18 ms: 1.01x slower                                                         |
| json_dumps                       | 7.71 ms                                                                | 7.78 ms: 1.01x slower                                                         |
| async_tree_eager_cpu_io_mixed_tg | 400 ms                                                                 | 404 ms: 1.01x slower                                                          |
| regex_v8                         | 15.7 ms                                                                | 15.8 ms: 1.01x slower                                                         |
| asyncio_websockets               | 243 ms                                                                 | 245 ms: 1.01x slower                                                          |
| create_gc_cycles                 | 1.28 ms                                                                | 1.29 ms: 1.01x slower                                                         |
| logging_simple                   | 3.94 us                                                                | 3.98 us: 1.01x slower                                                         |
| logging_format                   | 4.24 us                                                                | 4.29 us: 1.01x slower                                                         |
| scimark_lu                       | 83.6 ms                                                                | 84.6 ms: 1.01x slower                                                         |
| connected_components             | 312 ms                                                                 | 317 ms: 1.02x slower                                                          |
| telco                            | 4.81 ms                                                                | 4.90 ms: 1.02x slower                                                         |
| django_template                  | 26.3 ms                                                                | 26.9 ms: 1.02x slower                                                         |
| regex_effbot                     | 2.24 ms                                                                | 2.30 ms: 1.03x slower                                                         |
| docutils                         | 1.54 sec                                                               | 1.59 sec: 1.03x slower                                                        |
| scimark_fft                      | 204 ms                                                                 | 211 ms: 1.03x slower                                                          |
| scimark_monte_carlo              | 52.9 ms                                                                | 54.9 ms: 1.04x slower                                                         |
| html5lib                         | 35.0 ms                                                                | 36.3 ms: 1.04x slower                                                         |
| coroutines                       | 19.5 ms                                                                | 20.3 ms: 1.04x slower                                                         |
| richards_super                   | 43.6 ms                                                                | 45.4 ms: 1.04x slower                                                         |
| genshi_text                      | 18.5 ms                                                                | 19.4 ms: 1.05x slower                                                         |
| chaos                            | 46.1 ms                                                                | 49.2 ms: 1.07x slower                                                         |
| 2to3                             | 187 ms                                                                 | 218 ms: 1.17x slower                                                          |
| Geometric mean                   | (ref)                                                                  | 1.00x faster                                                                  |

Benchmark hidden because not significant (25): k_core, sphinx, float, async_tree_io, python_startup, pycparser, async_tree_eager_memoization, async_generators, async_tree_none, async_tree_none_tg, xml_etree_iterparse, pidigits, async_tree_eager_tg, async_tree_eager_io_tg, regex_dna, deepcopy_reduce, spectral_norm, crypto_pyaes, async_tree_eager_cpu_io_mixed, deltablue, pathlib, json, async_tree_memoization_tg, xml_etree_parse, async_tree_eager_memoization_tg
Ignored benchmarks (5) of results/bm-20250414-3.14.0a7+-844596c/bm-20250414-darwin-arm64-python-844596c09fc812a58ac1-3.14.0a7+-844596c.json: pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum

- Geometric mean (including insignificant results): 1.003x faster

# HPT report

- Reliability score: 96.73% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x