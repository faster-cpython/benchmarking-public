# Results vs. base

- fork: brandtbucher
- ref: justin_hot
- machine: linux-aarch64
- commit hash: d2c9ae9
- commit date: 2025-06-19
- overall geometric mean: 1.043x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb | bm-20250619-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:-------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 312 ms                                                  | 317 ms: 1.02x slower                                                |
| docutils       | 3.09 sec                                                | 3.15 sec: 1.02x slower                                              |
| Geometric mean | (ref)                                                   | 1.01x slower                                                        |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb | bm-20250619-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|------------------------|:-------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none_tg     | 385 ms                                                  | 379 ms: 1.01x faster                                                |
| async_tree_memoization | 478 ms                                                  | 473 ms: 1.01x faster                                                |
| Geometric mean         | (ref)                                                   | 1.00x faster                                                        |

Benchmark hidden because not significant (9): async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_io, async_tree_none, async_generators, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb | bm-20250619-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:-------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 235 ms                                                  | 236 ms: 1.01x slower                                                |
| float          | 82.8 ms                                                 | 88.6 ms: 1.07x slower                                               |
| nbody          | 119 ms                                                  | 147 ms: 1.24x slower                                                |
| Geometric mean | (ref)                                                   | 1.10x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb | bm-20250619-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:-------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 27.1 ms                                                 | 26.9 ms: 1.01x faster                                               |
| regex_compile  | 122 ms                                                  | 130 ms: 1.07x slower                                                |
| Geometric mean | (ref)                                                   | 1.01x slower                                                        |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb | bm-20250619-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------------|:-------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_iterparse  | 143 ms                                                  | 144 ms: 1.01x slower                                                |
| xml_etree_parse      | 179 ms                                                  | 180 ms: 1.01x slower                                                |
| pickle_pure_python   | 388 us                                                  | 404 us: 1.04x slower                                                |
| tomli_loads          | 2.37 sec                                                | 2.55 sec: 1.08x slower                                              |
| unpickle_pure_python | 248 us                                                  | 295 us: 1.19x slower                                                |
| Geometric mean       | (ref)                                                   | 1.04x slower                                                        |

Benchmark hidden because not significant (4): json_loads, json_dumps, xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb | bm-20250619-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|-----------------|:-------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 41.7 ms                                                 | 39.0 ms: 1.07x faster                                               |
| mako            | 13.6 ms                                                 | 15.1 ms: 1.12x slower                                               |
| Geometric mean  | (ref)                                                   | 1.01x slower                                                        |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb | bm-20250619-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|-------------------------|:-------------------------------------------------------:|:-------------------------------------------------------------------:|
| thrift                  | 191 ms                                                  | 940 us: 202.63x faster                                              |
| coverage                | 554 ms                                                  | 101 ms: 5.49x faster                                                |
| django_template         | 41.7 ms                                                 | 39.0 ms: 1.07x faster                                               |
| async_tree_none_tg      | 385 ms                                                  | 379 ms: 1.01x faster                                                |
| async_tree_memoization  | 478 ms                                                  | 473 ms: 1.01x faster                                                |
| logging_simple          | 7.57 us                                                 | 7.49 us: 1.01x faster                                               |
| regex_v8                | 27.1 ms                                                 | 26.9 ms: 1.01x faster                                               |
| logging_silent          | 606 ns                                                  | 609 ns: 1.01x slower                                                |
| xml_etree_iterparse     | 143 ms                                                  | 144 ms: 1.01x slower                                                |
| pidigits                | 235 ms                                                  | 236 ms: 1.01x slower                                                |
| xml_etree_parse         | 179 ms                                                  | 180 ms: 1.01x slower                                                |
| sqlite_synth            | 3.71 us                                                 | 3.77 us: 1.01x slower                                               |
| 2to3                    | 312 ms                                                  | 317 ms: 1.02x slower                                                |
| sqlglot_v2_optimize     | 62.8 ms                                                 | 63.9 ms: 1.02x slower                                               |
| shortest_path           | 587 ms                                                  | 598 ms: 1.02x slower                                                |
| docutils                | 3.09 sec                                                | 3.15 sec: 1.02x slower                                              |
| mdp                     | 1.68 sec                                                | 1.72 sec: 1.02x slower                                              |
| many_optionals          | 803 us                                                  | 824 us: 1.03x slower                                                |
| k_core                  | 2.82 sec                                                | 2.93 sec: 1.04x slower                                              |
| connected_components    | 561 ms                                                  | 583 ms: 1.04x slower                                                |
| pickle_pure_python      | 388 us                                                  | 404 us: 1.04x slower                                                |
| pycparser               | 1.40 sec                                                | 1.46 sec: 1.04x slower                                              |
| scimark_monte_carlo     | 82.9 ms                                                 | 86.9 ms: 1.05x slower                                               |
| nqueens                 | 101 ms                                                  | 106 ms: 1.05x slower                                                |
| sqlglot_v2_transpile    | 1.87 ms                                                 | 1.96 ms: 1.05x slower                                               |
| regex_compile           | 122 ms                                                  | 130 ms: 1.07x slower                                                |
| telco                   | 9.45 ms                                                 | 10.1 ms: 1.07x slower                                               |
| bpe_tokeniser           | 5.45 sec                                                | 5.82 sec: 1.07x slower                                              |
| float                   | 82.8 ms                                                 | 88.6 ms: 1.07x slower                                               |
| scimark_sparse_mat_mult | 6.93 ms                                                 | 7.46 ms: 1.08x slower                                               |
| tomli_loads             | 2.37 sec                                                | 2.55 sec: 1.08x slower                                              |
| richards_super          | 51.1 ms                                                 | 55.7 ms: 1.09x slower                                               |
| meteor_contest          | 116 ms                                                  | 127 ms: 1.10x slower                                                |
| scimark_fft             | 424 ms                                                  | 466 ms: 1.10x slower                                                |
| sqlglot_v2_parse        | 1.54 ms                                                 | 1.69 ms: 1.10x slower                                               |
| crypto_pyaes            | 92.8 ms                                                 | 102 ms: 1.10x slower                                                |
| pyflate                 | 549 ms                                                  | 606 ms: 1.10x slower                                                |
| comprehensions          | 22.7 us                                                 | 25.1 us: 1.11x slower                                               |
| mako                    | 13.6 ms                                                 | 15.1 ms: 1.12x slower                                               |
| spectral_norm           | 134 ms                                                  | 152 ms: 1.14x slower                                                |
| deltablue               | 3.97 ms                                                 | 4.57 ms: 1.15x slower                                               |
| fannkuch                | 483 ms                                                  | 557 ms: 1.15x slower                                                |
| richards                | 44.7 ms                                                 | 52.1 ms: 1.16x slower                                               |
| hexiom                  | 7.49 ms                                                 | 8.91 ms: 1.19x slower                                               |
| unpickle_pure_python    | 248 us                                                  | 295 us: 1.19x slower                                                |
| go                      | 159 ms                                                  | 193 ms: 1.22x slower                                                |
| pprint_safe_repr        | 1.25 sec                                                | 1.54 sec: 1.23x slower                                              |
| nbody                   | 119 ms                                                  | 147 ms: 1.24x slower                                                |
| pprint_pformat          | 2.58 sec                                                | 3.25 sec: 1.26x slower                                              |
| Geometric mean          | (ref)                                                   | 1.04x faster                                                        |

Benchmark hidden because not significant (43): deepcopy, sympy_sum, deepcopy_memo, regex_effbot, genshi_text, deepcopy_reduce, pathlib, sqlglot_v2_normalize, scimark_lu, chaos, json_loads, python_startup, async_tree_cpu_io_mixed_tg, async_tree_io_tg, sympy_str, json_dumps, async_tree_memoization_tg, logging_format, python_startup_no_site, gc_traversal, async_tree_cpu_io_mixed, html5lib, asyncio_websockets, sympy_integrate, regex_dna, subparsers, async_tree_io, create_gc_cycles, dulwich_log, async_tree_none, sympy_expand, async_generators, sphinx, scimark_sor, generators, genshi_xml, json, raytrace, xml_etree_process, coroutines, xml_etree_generate, typing_runtime_protocols, pylint
Ignored benchmarks (1) of results/bm-20250619-3.15.0a0-d2c9ae9-JIT/bm-20250619-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9.json: djangocms

- Geometric mean (including insignificant results): 1.043x faster

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x