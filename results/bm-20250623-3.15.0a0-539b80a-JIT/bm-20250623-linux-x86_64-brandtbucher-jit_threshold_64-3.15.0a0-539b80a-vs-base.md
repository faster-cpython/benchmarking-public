# Results vs. base

- fork: brandtbucher
- ref: jit_threshold_64
- machine: linux-x86_64
- commit hash: 539b80a
- commit date: 2025-06-23
- overall geometric mean: 1.000x slower
- HPT reliability: 63.17%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250623-linux-x86_64-brandtbucher-jit_threshold_64-3.15.0a0-539b80a |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 262 ms                                                                | 270 ms: 1.03x slower                                                    |
| docutils       | 2.66 sec                                                              | 2.68 sec: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250623-linux-x86_64-brandtbucher-jit_threshold_64-3.15.0a0-539b80a |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 495 ms                                                                | 489 ms: 1.01x faster                                                    |
| async_tree_cpu_io_mixed    | 503 ms                                                                | 498 ms: 1.01x faster                                                    |
| async_tree_memoization     | 316 ms                                                                | 313 ms: 1.01x faster                                                    |
| coroutines                 | 25.2 ms                                                               | 25.6 ms: 1.02x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                            |

Benchmark hidden because not significant (7): async_tree_memoization_tg, async_tree_io, async_generators, async_tree_none, asyncio_websockets, async_tree_none_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250623-linux-x86_64-brandtbucher-jit_threshold_64-3.15.0a0-539b80a |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 191 ms                                                                | 186 ms: 1.03x faster                                                    |
| float          | 64.9 ms                                                               | 65.6 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                            |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250623-linux-x86_64-brandtbucher-jit_threshold_64-3.15.0a0-539b80a |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 23.6 ms                                                               | 23.3 ms: 1.01x faster                                                   |
| regex_effbot   | 3.44 ms                                                               | 3.43 ms: 1.00x faster                                                   |
| regex_compile  | 127 ms                                                                | 128 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250623-linux-x86_64-brandtbucher-jit_threshold_64-3.15.0a0-539b80a |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_loads           | 28.4 us                                                               | 27.8 us: 1.02x faster                                                   |
| json_dumps           | 11.0 ms                                                               | 10.8 ms: 1.02x faster                                                   |
| tomli_loads          | 1.91 sec                                                              | 1.88 sec: 1.01x faster                                                  |
| unpickle_pure_python | 200 us                                                                | 199 us: 1.01x faster                                                    |
| xml_etree_iterparse  | 97.6 ms                                                               | 98.4 ms: 1.01x slower                                                   |
| xml_etree_parse      | 139 ms                                                                | 141 ms: 1.02x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                            |

Benchmark hidden because not significant (3): xml_etree_process, xml_etree_generate, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250623-linux-x86_64-brandtbucher-jit_threshold_64-3.15.0a0-539b80a |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 12.2 ms                                                               | 12.2 ms: 1.01x slower                                                   |
| python_startup_no_site | 6.92 ms                                                               | 6.97 ms: 1.01x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250623-linux-x86_64-brandtbucher-jit_threshold_64-3.15.0a0-539b80a |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 10.7 ms                                                               | 10.6 ms: 1.02x faster                                                   |
| django_template | 32.7 ms                                                               | 32.5 ms: 1.01x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                            |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250623-linux-x86_64-brandtbucher-jit_threshold_64-3.15.0a0-539b80a |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pprint_pformat             | 1.73 sec                                                              | 1.60 sec: 1.08x faster                                                  |
| pidigits                   | 191 ms                                                                | 186 ms: 1.03x faster                                                    |
| subparsers                 | 24.1 ms                                                               | 23.5 ms: 1.03x faster                                                   |
| json_loads                 | 28.4 us                                                               | 27.8 us: 1.02x faster                                                   |
| pprint_safe_repr           | 833 ms                                                                | 816 ms: 1.02x faster                                                    |
| json_dumps                 | 11.0 ms                                                               | 10.8 ms: 1.02x faster                                                   |
| json                       | 5.24 ms                                                               | 5.15 ms: 1.02x faster                                                   |
| dulwich_log                | 60.3 ms                                                               | 59.2 ms: 1.02x faster                                                   |
| thrift                     | 783 us                                                                | 770 us: 1.02x faster                                                    |
| pathlib                    | 17.0 ms                                                               | 16.7 ms: 1.02x faster                                                   |
| mako                       | 10.7 ms                                                               | 10.6 ms: 1.02x faster                                                   |
| deepcopy_reduce            | 2.75 us                                                               | 2.71 us: 1.01x faster                                                   |
| logging_simple             | 6.27 us                                                               | 6.18 us: 1.01x faster                                                   |
| comprehensions             | 17.0 us                                                               | 16.8 us: 1.01x faster                                                   |
| sqlglot_v2_parse           | 1.28 ms                                                               | 1.26 ms: 1.01x faster                                                   |
| regex_v8                   | 23.6 ms                                                               | 23.3 ms: 1.01x faster                                                   |
| tomli_loads                | 1.91 sec                                                              | 1.88 sec: 1.01x faster                                                  |
| pyflate                    | 426 ms                                                                | 421 ms: 1.01x faster                                                    |
| typing_runtime_protocols   | 170 us                                                                | 168 us: 1.01x faster                                                    |
| async_tree_cpu_io_mixed_tg | 495 ms                                                                | 489 ms: 1.01x faster                                                    |
| async_tree_cpu_io_mixed    | 503 ms                                                                | 498 ms: 1.01x faster                                                    |
| async_tree_memoization     | 316 ms                                                                | 313 ms: 1.01x faster                                                    |
| raytrace                   | 276 ms                                                                | 274 ms: 1.01x faster                                                    |
| scimark_sparse_mat_mult    | 4.89 ms                                                               | 4.85 ms: 1.01x faster                                                   |
| unpickle_pure_python       | 200 us                                                                | 199 us: 1.01x faster                                                    |
| django_template            | 32.7 ms                                                               | 32.5 ms: 1.01x faster                                                   |
| fannkuch                   | 411 ms                                                                | 408 ms: 1.01x faster                                                    |
| scimark_fft                | 330 ms                                                                | 328 ms: 1.01x faster                                                    |
| regex_effbot               | 3.44 ms                                                               | 3.43 ms: 1.00x faster                                                   |
| sympy_expand               | 468 ms                                                                | 470 ms: 1.00x slower                                                    |
| python_startup             | 12.2 ms                                                               | 12.2 ms: 1.01x slower                                                   |
| logging_silent             | 474 ns                                                                | 477 ns: 1.01x slower                                                    |
| meteor_contest             | 107 ms                                                                | 108 ms: 1.01x slower                                                    |
| python_startup_no_site     | 6.92 ms                                                               | 6.97 ms: 1.01x slower                                                   |
| sqlite_synth               | 2.79 us                                                               | 2.81 us: 1.01x slower                                                   |
| docutils                   | 2.66 sec                                                              | 2.68 sec: 1.01x slower                                                  |
| sympy_str                  | 273 ms                                                                | 275 ms: 1.01x slower                                                    |
| sqlglot_v2_normalize       | 106 ms                                                                | 107 ms: 1.01x slower                                                    |
| scimark_sor                | 121 ms                                                                | 122 ms: 1.01x slower                                                    |
| regex_compile              | 127 ms                                                                | 128 ms: 1.01x slower                                                    |
| shortest_path              | 493 ms                                                                | 497 ms: 1.01x slower                                                    |
| xml_etree_iterparse        | 97.6 ms                                                               | 98.4 ms: 1.01x slower                                                   |
| gc_traversal               | 4.93 ms                                                               | 4.97 ms: 1.01x slower                                                   |
| deltablue                  | 3.15 ms                                                               | 3.18 ms: 1.01x slower                                                   |
| float                      | 64.9 ms                                                               | 65.6 ms: 1.01x slower                                                   |
| coverage                   | 87.5 ms                                                               | 88.4 ms: 1.01x slower                                                   |
| sqlglot_v2_optimize        | 52.8 ms                                                               | 53.5 ms: 1.01x slower                                                   |
| generators                 | 30.1 ms                                                               | 30.5 ms: 1.01x slower                                                   |
| deepcopy_memo              | 29.1 us                                                               | 29.4 us: 1.01x slower                                                   |
| sqlglot_v2_transpile       | 1.59 ms                                                               | 1.61 ms: 1.01x slower                                                   |
| create_gc_cycles           | 2.58 ms                                                               | 2.61 ms: 1.01x slower                                                   |
| xml_etree_parse            | 139 ms                                                                | 141 ms: 1.02x slower                                                    |
| coroutines                 | 25.2 ms                                                               | 25.6 ms: 1.02x slower                                                   |
| connected_components       | 457 ms                                                                | 467 ms: 1.02x slower                                                    |
| many_optionals             | 985 us                                                                | 1.01 ms: 1.02x slower                                                   |
| sympy_integrate            | 19.4 ms                                                               | 20.0 ms: 1.03x slower                                                   |
| 2to3                       | 262 ms                                                                | 270 ms: 1.03x slower                                                    |
| sympy_sum                  | 150 ms                                                                | 155 ms: 1.04x slower                                                    |
| richards_super             | 39.9 ms                                                               | 42.0 ms: 1.05x slower                                                   |
| richards                   | 34.4 ms                                                               | 36.9 ms: 1.07x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.00x slower                                                            |

Benchmark hidden because not significant (33): async_tree_memoization_tg, telco, pycparser, nqueens, genshi_xml, xml_etree_process, genshi_text, spectral_norm, go, html5lib, hexiom, mdp, djangocms, chaos, bpe_tokeniser, regex_dna, nbody, async_tree_io, xml_etree_generate, crypto_pyaes, k_core, scimark_monte_carlo, async_generators, sphinx, deepcopy, async_tree_none, pickle_pure_python, asyncio_websockets, logging_format, async_tree_none_tg, scimark_lu, async_tree_io_tg, pylint

- Geometric mean (including insignificant results): 1.000x slower

# HPT report

- Reliability score: 63.17% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.03x