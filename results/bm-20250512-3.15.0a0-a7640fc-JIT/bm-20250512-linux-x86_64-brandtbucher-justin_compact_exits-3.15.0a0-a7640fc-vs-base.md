# Results vs. base

- fork: brandtbucher
- ref: justin_compact_exits
- machine: linux-x86_64
- commit hash: a7640fc
- commit date: 2025-05-12
- overall geometric mean: 1.002x slower
- HPT reliability: 65.08%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250512-linux-x86_64-python-121ed71f4e395948d313-3.15.0a0-121ed71 | bm-20250512-linux-x86_64-brandtbucher-justin_compact_exits-3.15.0a0-a7640fc |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 2.64 sec                                                              | 2.65 sec: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250512-linux-x86_64-python-121ed71f4e395948d313-3.15.0a0-121ed71 | bm-20250512-linux-x86_64-brandtbucher-justin_compact_exits-3.15.0a0-a7640fc |
|----------------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg        | 313 ms                                                                | 308 ms: 1.01x faster                                                        |
| async_tree_none_tg               | 250 ms                                                                | 247 ms: 1.01x faster                                                        |
| async_tree_eager_memoization_tg  | 282 ms                                                                | 279 ms: 1.01x faster                                                        |
| async_tree_cpu_io_mixed_tg       | 492 ms                                                                | 496 ms: 1.01x slower                                                        |
| async_tree_eager_cpu_io_mixed_tg | 467 ms                                                                | 472 ms: 1.01x slower                                                        |
| async_tree_cpu_io_mixed          | 501 ms                                                                | 506 ms: 1.01x slower                                                        |
| coroutines                       | 24.8 ms                                                               | 25.2 ms: 1.02x slower                                                       |
| async_tree_eager                 | 104 ms                                                                | 106 ms: 1.02x slower                                                        |
| async_tree_eager_cpu_io_mixed    | 394 ms                                                                | 402 ms: 1.02x slower                                                        |
| Geometric mean                   | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (10): async_tree_eager_io_tg, async_tree_eager_tg, async_tree_memoization, async_tree_eager_io, async_tree_none, async_generators, asyncio_websockets, async_tree_io, async_tree_io_tg, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250512-linux-x86_64-python-121ed71f4e395948d313-3.15.0a0-121ed71 | bm-20250512-linux-x86_64-brandtbucher-justin_compact_exits-3.15.0a0-a7640fc |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 190 ms                                                                | 191 ms: 1.01x slower                                                        |
| float          | 63.7 ms                                                               | 64.5 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250512-linux-x86_64-python-121ed71f4e395948d313-3.15.0a0-121ed71 | bm-20250512-linux-x86_64-brandtbucher-justin_compact_exits-3.15.0a0-a7640fc |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.05 ms                                                               | 3.06 ms: 1.00x slower                                                       |
| regex_dna      | 200 ms                                                                | 205 ms: 1.02x slower                                                        |
| regex_v8       | 22.2 ms                                                               | 23.0 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250512-linux-x86_64-python-121ed71f4e395948d313-3.15.0a0-121ed71 | bm-20250512-linux-x86_64-brandtbucher-justin_compact_exits-3.15.0a0-a7640fc |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 206 us                                                                | 201 us: 1.03x faster                                                        |
| json_dumps           | 12.0 ms                                                               | 12.0 ms: 1.00x faster                                                       |
| xml_etree_generate   | 80.1 ms                                                               | 79.8 ms: 1.00x faster                                                       |
| xml_etree_parse      | 140 ms                                                                | 141 ms: 1.01x slower                                                        |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (5): tomli_loads, xml_etree_iterparse, pickle_pure_python, json_loads, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250512-linux-x86_64-python-121ed71f4e395948d313-3.15.0a0-121ed71 | bm-20250512-linux-x86_64-brandtbucher-justin_compact_exits-3.15.0a0-a7640fc |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 12.2 ms                                                               | 12.3 ms: 1.00x slower                                                       |
| python_startup_no_site | 6.94 ms                                                               | 6.96 ms: 1.00x slower                                                       |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250512-linux-x86_64-python-121ed71f4e395948d313-3.15.0a0-121ed71 | bm-20250512-linux-x86_64-brandtbucher-justin_compact_exits-3.15.0a0-a7640fc |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 32.4 ms                                                               | 32.3 ms: 1.00x faster                                                       |
| genshi_text     | 21.6 ms                                                               | 21.7 ms: 1.00x slower                                                       |
| mako            | 11.2 ms                                                               | 11.3 ms: 1.01x slower                                                       |
| genshi_xml      | 49.4 ms                                                               | 50.2 ms: 1.02x slower                                                       |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                                |

All benchmarks:
===============

| Benchmark                        | bm-20250512-linux-x86_64-python-121ed71f4e395948d313-3.15.0a0-121ed71 | bm-20250512-linux-x86_64-brandtbucher-justin_compact_exits-3.15.0a0-a7640fc |
|----------------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| coverage                         | 430 ms                                                                | 419 ms: 1.03x faster                                                        |
| unpickle_pure_python             | 206 us                                                                | 201 us: 1.03x faster                                                        |
| logging_format                   | 7.02 us                                                               | 6.86 us: 1.02x faster                                                       |
| go                               | 126 ms                                                                | 124 ms: 1.02x faster                                                        |
| pathlib                          | 17.5 ms                                                               | 17.2 ms: 1.02x faster                                                       |
| scimark_fft                      | 332 ms                                                                | 326 ms: 1.02x faster                                                        |
| raytrace                         | 276 ms                                                                | 271 ms: 1.02x faster                                                        |
| sqlglot_v2_parse                 | 1.26 ms                                                               | 1.24 ms: 1.02x faster                                                       |
| fannkuch                         | 412 ms                                                                | 405 ms: 1.02x faster                                                        |
| chaos                            | 61.0 ms                                                               | 60.1 ms: 1.02x faster                                                       |
| async_tree_memoization_tg        | 313 ms                                                                | 308 ms: 1.01x faster                                                        |
| async_tree_none_tg               | 250 ms                                                                | 247 ms: 1.01x faster                                                        |
| meteor_contest                   | 108 ms                                                                | 107 ms: 1.01x faster                                                        |
| async_tree_eager_memoization_tg  | 282 ms                                                                | 279 ms: 1.01x faster                                                        |
| hexiom                           | 6.60 ms                                                               | 6.54 ms: 1.01x faster                                                       |
| sqlite_synth                     | 2.82 us                                                               | 2.79 us: 1.01x faster                                                       |
| sqlglot_v2_transpile             | 1.58 ms                                                               | 1.56 ms: 1.01x faster                                                       |
| deepcopy                         | 262 us                                                                | 259 us: 1.01x faster                                                        |
| shortest_path                    | 487 ms                                                                | 483 ms: 1.01x faster                                                        |
| sympy_str                        | 273 ms                                                                | 271 ms: 1.01x faster                                                        |
| deltablue                        | 3.07 ms                                                               | 3.05 ms: 1.01x faster                                                       |
| json_dumps                       | 12.0 ms                                                               | 12.0 ms: 1.00x faster                                                       |
| django_template                  | 32.4 ms                                                               | 32.3 ms: 1.00x faster                                                       |
| xml_etree_generate               | 80.1 ms                                                               | 79.8 ms: 1.00x faster                                                       |
| sympy_expand                     | 474 ms                                                                | 472 ms: 1.00x faster                                                        |
| python_startup                   | 12.2 ms                                                               | 12.3 ms: 1.00x slower                                                       |
| python_startup_no_site           | 6.94 ms                                                               | 6.96 ms: 1.00x slower                                                       |
| genshi_text                      | 21.6 ms                                                               | 21.7 ms: 1.00x slower                                                       |
| regex_effbot                     | 3.05 ms                                                               | 3.06 ms: 1.00x slower                                                       |
| docutils                         | 2.64 sec                                                              | 2.65 sec: 1.01x slower                                                      |
| async_tree_cpu_io_mixed_tg       | 492 ms                                                                | 496 ms: 1.01x slower                                                        |
| deepcopy_memo                    | 29.9 us                                                               | 30.1 us: 1.01x slower                                                       |
| pidigits                         | 190 ms                                                                | 191 ms: 1.01x slower                                                        |
| create_gc_cycles                 | 2.56 ms                                                               | 2.58 ms: 1.01x slower                                                       |
| xml_etree_parse                  | 140 ms                                                                | 141 ms: 1.01x slower                                                        |
| scimark_lu                       | 118 ms                                                                | 119 ms: 1.01x slower                                                        |
| sqlglot_v2_normalize             | 106 ms                                                                | 107 ms: 1.01x slower                                                        |
| mako                             | 11.2 ms                                                               | 11.3 ms: 1.01x slower                                                       |
| sympy_integrate                  | 19.4 ms                                                               | 19.6 ms: 1.01x slower                                                       |
| async_tree_eager_cpu_io_mixed_tg | 467 ms                                                                | 472 ms: 1.01x slower                                                        |
| async_tree_cpu_io_mixed          | 501 ms                                                                | 506 ms: 1.01x slower                                                        |
| typing_runtime_protocols         | 172 us                                                                | 174 us: 1.01x slower                                                        |
| float                            | 63.7 ms                                                               | 64.5 ms: 1.01x slower                                                       |
| scimark_monte_carlo              | 67.7 ms                                                               | 68.6 ms: 1.01x slower                                                       |
| comprehensions                   | 17.8 us                                                               | 18.0 us: 1.02x slower                                                       |
| genshi_xml                       | 49.4 ms                                                               | 50.2 ms: 1.02x slower                                                       |
| coroutines                       | 24.8 ms                                                               | 25.2 ms: 1.02x slower                                                       |
| async_tree_eager                 | 104 ms                                                                | 106 ms: 1.02x slower                                                        |
| gc_traversal                     | 4.86 ms                                                               | 4.95 ms: 1.02x slower                                                       |
| async_tree_eager_cpu_io_mixed    | 394 ms                                                                | 402 ms: 1.02x slower                                                        |
| pprint_safe_repr                 | 737 ms                                                                | 753 ms: 1.02x slower                                                        |
| scimark_sor                      | 119 ms                                                                | 122 ms: 1.02x slower                                                        |
| regex_dna                        | 200 ms                                                                | 205 ms: 1.02x slower                                                        |
| pyflate                          | 435 ms                                                                | 450 ms: 1.03x slower                                                        |
| richards                         | 33.8 ms                                                               | 35.0 ms: 1.04x slower                                                       |
| scimark_sparse_mat_mult          | 4.83 ms                                                               | 5.00 ms: 1.04x slower                                                       |
| regex_v8                         | 22.2 ms                                                               | 23.0 ms: 1.04x slower                                                       |
| generators                       | 31.4 ms                                                               | 32.6 ms: 1.04x slower                                                       |
| richards_super                   | 38.3 ms                                                               | 41.0 ms: 1.07x slower                                                       |
| Geometric mean                   | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (44): async_tree_eager_io_tg, pycparser, telco, async_tree_eager_tg, crypto_pyaes, logging_simple, k_core, async_tree_memoization, logging_silent, nqueens, html5lib, async_tree_eager_io, pylint, bpe_tokeniser, connected_components, spectral_norm, dulwich_log, async_tree_none, mdp, pprint_pformat, bench_mp_pool, tomli_loads, xml_etree_iterparse, thrift, pickle_pure_python, sqlglot_v2_optimize, async_generators, deepcopy_reduce, asyncio_websockets, 2to3, json_loads, async_tree_io, bench_thread_pool, dask, async_tree_io_tg, many_optionals, sympy_sum, subparsers, regex_compile, json, sphinx, xml_etree_process, nbody, async_tree_eager_memoization

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 65.08% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x