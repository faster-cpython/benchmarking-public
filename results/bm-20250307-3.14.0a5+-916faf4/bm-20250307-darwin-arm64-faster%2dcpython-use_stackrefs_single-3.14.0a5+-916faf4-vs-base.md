# Results vs. base

- fork: faster-cpython
- ref: use_stackrefs_single
- machine: darwin-arm64
- commit hash: 916faf4
- commit date: 2025-03-07
- overall geometric mean: 1.001x faster
- HPT reliability: 64.09%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250303-darwin-arm64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf | bm-20250307-darwin-arm64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| docutils       | 1.50 sec                                                               | 1.51 sec: 1.00x slower                                                           |
| html5lib       | 33.2 ms                                                                | 32.6 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250303-darwin-arm64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf | bm-20250307-darwin-arm64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| coroutines                       | 18.6 ms                                                                | 18.0 ms: 1.03x faster                                                            |
| async_tree_memoization           | 222 ms                                                                 | 218 ms: 1.02x faster                                                             |
| async_tree_io_tg                 | 401 ms                                                                 | 395 ms: 1.02x faster                                                             |
| async_generators                 | 268 ms                                                                 | 264 ms: 1.01x faster                                                             |
| async_tree_none_tg               | 172 ms                                                                 | 170 ms: 1.01x faster                                                             |
| async_tree_cpu_io_mixed          | 435 ms                                                                 | 430 ms: 1.01x faster                                                             |
| asyncio_websockets               | 242 ms                                                                 | 242 ms: 1.00x slower                                                             |
| async_tree_eager_memoization     | 151 ms                                                                 | 152 ms: 1.01x slower                                                             |
| async_tree_eager_cpu_io_mixed_tg | 402 ms                                                                 | 405 ms: 1.01x slower                                                             |
| async_tree_eager                 | 69.0 ms                                                                | 70.3 ms: 1.02x slower                                                            |
| Geometric mean                   | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (9): async_tree_eager_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_tg, async_tree_none, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_memoization_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250303-darwin-arm64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf | bm-20250307-darwin-arm64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                                | 90.5 ms: 1.02x faster                                                            |
| float          | 54.4 ms                                                                | 56.4 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250303-darwin-arm64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf | bm-20250307-darwin-arm64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_dna      | 146 ms                                                                 | 141 ms: 1.04x faster                                                             |
| regex_effbot   | 2.32 ms                                                                | 2.29 ms: 1.01x faster                                                            |
| regex_v8       | 16.9 ms                                                                | 17.0 ms: 1.00x slower                                                            |
| regex_compile  | 78.1 ms                                                                | 78.5 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250303-darwin-arm64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf | bm-20250307-darwin-arm64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 1.44 sec                                                               | 1.35 sec: 1.07x faster                                                           |
| xml_etree_process    | 42.8 ms                                                                | 42.0 ms: 1.02x faster                                                            |
| xml_etree_iterparse  | 75.1 ms                                                                | 73.9 ms: 1.02x faster                                                            |
| xml_etree_generate   | 58.2 ms                                                                | 58.1 ms: 1.00x faster                                                            |
| json_dumps           | 7.49 ms                                                                | 7.54 ms: 1.01x slower                                                            |
| json_loads           | 17.7 us                                                                | 17.9 us: 1.01x slower                                                            |
| unpickle_pure_python | 169 us                                                                 | 173 us: 1.02x slower                                                             |
| pickle_pure_python   | 230 us                                                                 | 237 us: 1.03x slower                                                             |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250303-darwin-arm64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf | bm-20250307-darwin-arm64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 14.5 ms                                                                | 14.4 ms: 1.01x faster                                                            |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                                     |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250303-darwin-arm64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf | bm-20250307-darwin-arm64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 24.2 ms                                                                | 23.4 ms: 1.03x faster                                                            |
| genshi_xml      | 33.9 ms                                                                | 33.5 ms: 1.01x faster                                                            |
| mako            | 8.32 ms                                                                | 8.64 ms: 1.04x slower                                                            |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                        | bm-20250303-darwin-arm64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf | bm-20250307-darwin-arm64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| richards                         | 40.0 ms                                                                | 36.9 ms: 1.08x faster                                                            |
| spectral_norm                    | 78.1 ms                                                                | 72.8 ms: 1.07x faster                                                            |
| tomli_loads                      | 1.44 sec                                                               | 1.35 sec: 1.07x faster                                                           |
| raytrace                         | 212 ms                                                                 | 199 ms: 1.06x faster                                                             |
| scimark_lu                       | 84.7 ms                                                                | 80.0 ms: 1.06x faster                                                            |
| generators                       | 28.9 ms                                                                | 27.8 ms: 1.04x faster                                                            |
| regex_dna                        | 146 ms                                                                 | 141 ms: 1.04x faster                                                             |
| django_template                  | 24.2 ms                                                                | 23.4 ms: 1.03x faster                                                            |
| coroutines                       | 18.6 ms                                                                | 18.0 ms: 1.03x faster                                                            |
| pyflate                          | 351 ms                                                                 | 340 ms: 1.03x faster                                                             |
| html5lib                         | 33.2 ms                                                                | 32.6 ms: 1.02x faster                                                            |
| nbody                            | 92.1 ms                                                                | 90.5 ms: 1.02x faster                                                            |
| pprint_safe_repr                 | 545 ms                                                                 | 535 ms: 1.02x faster                                                             |
| xml_etree_process                | 42.8 ms                                                                | 42.0 ms: 1.02x faster                                                            |
| async_tree_memoization           | 222 ms                                                                 | 218 ms: 1.02x faster                                                             |
| coverage                         | 47.8 ms                                                                | 47.0 ms: 1.02x faster                                                            |
| pprint_pformat                   | 1.10 sec                                                               | 1.08 sec: 1.02x faster                                                           |
| async_tree_io_tg                 | 401 ms                                                                 | 395 ms: 1.02x faster                                                             |
| logging_simple                   | 3.77 us                                                                | 3.71 us: 1.02x faster                                                            |
| xml_etree_iterparse              | 75.1 ms                                                                | 73.9 ms: 1.02x faster                                                            |
| async_generators                 | 268 ms                                                                 | 264 ms: 1.01x faster                                                             |
| dulwich_log                      | 29.9 ms                                                                | 29.5 ms: 1.01x faster                                                            |
| async_tree_none_tg               | 172 ms                                                                 | 170 ms: 1.01x faster                                                             |
| regex_effbot                     | 2.32 ms                                                                | 2.29 ms: 1.01x faster                                                            |
| genshi_xml                       | 33.9 ms                                                                | 33.5 ms: 1.01x faster                                                            |
| async_tree_cpu_io_mixed          | 435 ms                                                                 | 430 ms: 1.01x faster                                                             |
| sqlite_synth                     | 1.55 us                                                                | 1.54 us: 1.01x faster                                                            |
| bench_thread_pool                | 524 us                                                                 | 519 us: 1.01x faster                                                             |
| logging_format                   | 4.08 us                                                                | 4.04 us: 1.01x faster                                                            |
| python_startup_no_site           | 14.5 ms                                                                | 14.4 ms: 1.01x faster                                                            |
| telco                            | 4.79 ms                                                                | 4.75 ms: 1.01x faster                                                            |
| richards_super                   | 42.9 ms                                                                | 42.6 ms: 1.01x faster                                                            |
| sympy_sum                        | 79.9 ms                                                                | 79.4 ms: 1.01x faster                                                            |
| sqlglot_optimize                 | 35.7 ms                                                                | 35.5 ms: 1.01x faster                                                            |
| scimark_sor                      | 92.8 ms                                                                | 92.3 ms: 1.01x faster                                                            |
| sympy_expand                     | 256 ms                                                                 | 255 ms: 1.01x faster                                                             |
| sqlalchemy_imperative            | 7.09 ms                                                                | 7.06 ms: 1.00x faster                                                            |
| meteor_contest                   | 78.7 ms                                                                | 78.3 ms: 1.00x faster                                                            |
| xml_etree_generate               | 58.2 ms                                                                | 58.1 ms: 1.00x faster                                                            |
| asyncio_websockets               | 242 ms                                                                 | 242 ms: 1.00x slower                                                             |
| bpe_tokeniser                    | 3.24 sec                                                               | 3.24 sec: 1.00x slower                                                           |
| hexiom                           | 5.28 ms                                                                | 5.29 ms: 1.00x slower                                                            |
| regex_v8                         | 16.9 ms                                                                | 17.0 ms: 1.00x slower                                                            |
| sympy_str                        | 153 ms                                                                 | 153 ms: 1.00x slower                                                             |
| docutils                         | 1.50 sec                                                               | 1.51 sec: 1.00x slower                                                           |
| sqlglot_normalize                | 196 ms                                                                 | 197 ms: 1.00x slower                                                             |
| gc_traversal                     | 3.08 ms                                                                | 3.10 ms: 1.00x slower                                                            |
| regex_compile                    | 78.1 ms                                                                | 78.5 ms: 1.01x slower                                                            |
| async_tree_eager_memoization     | 151 ms                                                                 | 152 ms: 1.01x slower                                                             |
| shortest_path                    | 339 ms                                                                 | 342 ms: 1.01x slower                                                             |
| async_tree_eager_cpu_io_mixed_tg | 402 ms                                                                 | 405 ms: 1.01x slower                                                             |
| json_dumps                       | 7.49 ms                                                                | 7.54 ms: 1.01x slower                                                            |
| scimark_sparse_mat_mult          | 3.08 ms                                                                | 3.11 ms: 1.01x slower                                                            |
| create_gc_cycles                 | 1.26 ms                                                                | 1.27 ms: 1.01x slower                                                            |
| deepcopy_reduce                  | 1.76 us                                                                | 1.78 us: 1.01x slower                                                            |
| json_loads                       | 17.7 us                                                                | 17.9 us: 1.01x slower                                                            |
| thrift                           | 463 us                                                                 | 469 us: 1.01x slower                                                             |
| many_optionals                   | 465 us                                                                 | 472 us: 1.02x slower                                                             |
| sqlalchemy_declarative           | 62.6 ms                                                                | 63.7 ms: 1.02x slower                                                            |
| async_tree_eager                 | 69.0 ms                                                                | 70.3 ms: 1.02x slower                                                            |
| k_core                           | 1.54 sec                                                               | 1.57 sec: 1.02x slower                                                           |
| comprehensions                   | 13.1 us                                                                | 13.3 us: 1.02x slower                                                            |
| deepcopy                         | 168 us                                                                 | 172 us: 1.02x slower                                                             |
| typing_runtime_protocols         | 100 us                                                                 | 103 us: 1.02x slower                                                             |
| unpickle_pure_python             | 169 us                                                                 | 173 us: 1.02x slower                                                             |
| sqlglot_parse                    | 891 us                                                                 | 912 us: 1.02x slower                                                             |
| nqueens                          | 65.2 ms                                                                | 66.8 ms: 1.02x slower                                                            |
| sqlglot_transpile                | 1.07 ms                                                                | 1.10 ms: 1.02x slower                                                            |
| deltablue                        | 2.75 ms                                                                | 2.83 ms: 1.03x slower                                                            |
| pickle_pure_python               | 230 us                                                                 | 237 us: 1.03x slower                                                             |
| pylint                           | 171 ms                                                                 | 176 ms: 1.03x slower                                                             |
| pycparser                        | 705 ms                                                                 | 728 ms: 1.03x slower                                                             |
| chaos                            | 44.1 ms                                                                | 45.6 ms: 1.03x slower                                                            |
| float                            | 54.4 ms                                                                | 56.4 ms: 1.04x slower                                                            |
| mako                             | 8.32 ms                                                                | 8.64 ms: 1.04x slower                                                            |
| fannkuch                         | 292 ms                                                                 | 304 ms: 1.04x slower                                                             |
| crypto_pyaes                     | 59.0 ms                                                                | 61.5 ms: 1.04x slower                                                            |
| go                               | 94.8 ms                                                                | 101 ms: 1.06x slower                                                             |
| logging_silent                   | 73.1 ns                                                                | 78.4 ns: 1.07x slower                                                            |
| deepcopy_memo                    | 21.0 us                                                                | 22.7 us: 1.08x slower                                                            |
| Geometric mean                   | (ref)                                                                  | 1.00x slower                                                                     |

Benchmark hidden because not significant (25): python_startup, subparsers, json, mdp, bench_mp_pool, genshi_text, async_tree_eager_cpu_io_mixed, async_tree_cpu_io_mixed_tg, dask, pidigits, scimark_monte_carlo, sympy_integrate, 2to3, xml_etree_parse, async_tree_eager_io, async_tree_eager_tg, async_tree_none, async_tree_eager_io_tg, scimark_fft, async_tree_eager_memoization_tg, async_tree_memoization_tg, pathlib, connected_components, async_tree_io, sphinx

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 64.09% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x