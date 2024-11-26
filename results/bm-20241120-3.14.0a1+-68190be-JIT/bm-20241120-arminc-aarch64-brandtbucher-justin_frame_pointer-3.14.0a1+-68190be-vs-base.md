# Results vs. base

- fork: brandtbucher
- ref: justin_frame_pointer
- machine: linux-aarch64
- commit hash: 68190be
- commit date: 2024-11-20
- overall geometric mean: 1.031x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241118-arminc-aarch64-python-4cd10762b06ec57252e3-3.14.0a1+-4cd1076 | bm-20241120-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-68190be |
|----------------|:------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| docutils       | 3.48 sec                                                                 | 3.54 sec: 1.01x slower                                                         |
| sphinx         | 1.41 sec                                                                 | 1.45 sec: 1.03x slower                                                         |
| Geometric mean | (ref)                                                                    | 1.02x slower                                                                   |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20241118-arminc-aarch64-python-4cd10762b06ec57252e3-3.14.0a1+-4cd1076 | bm-20241120-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-68190be |
|-------------------------|:------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io           | 981 ms                                                                   | 1.01 sec: 1.03x slower                                                         |
| async_tree_io_tg        | 944 ms                                                                   | 975 ms: 1.03x slower                                                           |
| async_tree_cpu_io_mixed | 725 ms                                                                   | 752 ms: 1.04x slower                                                           |
| async_tree_memoization  | 550 ms                                                                   | 574 ms: 1.04x slower                                                           |
| async_tree_none_tg      | 417 ms                                                                   | 437 ms: 1.05x slower                                                           |
| async_tree_none         | 436 ms                                                                   | 462 ms: 1.06x slower                                                           |
| Geometric mean          | (ref)                                                                    | 1.03x slower                                                                   |

Benchmark hidden because not significant (5): asyncio_websockets, async_tree_cpu_io_mixed_tg, async_generators, async_tree_memoization_tg, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241118-arminc-aarch64-python-4cd10762b06ec57252e3-3.14.0a1+-4cd1076 | bm-20241120-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-68190be |
|----------------|:------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 100 ms                                                                   | 111 ms: 1.11x slower                                                           |
| nbody          | 121 ms                                                                   | 135 ms: 1.12x slower                                                           |
| Geometric mean | (ref)                                                                    | 1.08x slower                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241118-arminc-aarch64-python-4cd10762b06ec57252e3-3.14.0a1+-4cd1076 | bm-20241120-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-68190be |
|----------------|:------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 163 ms                                                                   | 172 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                                    | 1.01x slower                                                                   |

Benchmark hidden because not significant (3): regex_dna, regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241118-arminc-aarch64-python-4cd10762b06ec57252e3-3.14.0a1+-4cd1076 | bm-20241120-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-68190be |
|----------------------|:------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pickle_pure_python   | 394 us                                                                   | 412 us: 1.05x slower                                                           |
| xml_etree_generate   | 115 ms                                                                   | 122 ms: 1.06x slower                                                           |
| xml_etree_process    | 81.5 ms                                                                  | 86.8 ms: 1.07x slower                                                          |
| tomli_loads          | 2.65 sec                                                                 | 2.86 sec: 1.08x slower                                                         |
| unpickle_pure_python | 264 us                                                                   | 294 us: 1.11x slower                                                           |
| Geometric mean       | (ref)                                                                    | 1.05x slower                                                                   |

Benchmark hidden because not significant (4): json_loads, xml_etree_parse, xml_etree_iterparse, json_dumps

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241118-arminc-aarch64-python-4cd10762b06ec57252e3-3.14.0a1+-4cd1076 | bm-20241120-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-68190be |
|-----------------|:------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 80.5 ms                                                                  | 84.0 ms: 1.04x slower                                                          |
| django_template | 46.9 ms                                                                  | 50.1 ms: 1.07x slower                                                          |
| Geometric mean  | (ref)                                                                    | 1.05x slower                                                                   |

Benchmark hidden because not significant (2): mako, genshi_text

All benchmarks:
===============

| Benchmark                | bm-20241118-arminc-aarch64-python-4cd10762b06ec57252e3-3.14.0a1+-4cd1076 | bm-20241120-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-68190be |
|--------------------------|:------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| gc_traversal             | 2.99 ms                                                                  | 2.88 ms: 1.04x faster                                                          |
| djangocms                | 68.0 us                                                                  | 66.7 us: 1.02x faster                                                          |
| docutils                 | 3.48 sec                                                                 | 3.54 sec: 1.01x slower                                                         |
| sphinx                   | 1.41 sec                                                                 | 1.45 sec: 1.03x slower                                                         |
| k_core                   | 2.93 sec                                                                 | 3.02 sec: 1.03x slower                                                         |
| async_tree_io            | 981 ms                                                                   | 1.01 sec: 1.03x slower                                                         |
| async_tree_io_tg         | 944 ms                                                                   | 975 ms: 1.03x slower                                                           |
| pycparser                | 1.50 sec                                                                 | 1.55 sec: 1.03x slower                                                         |
| async_tree_cpu_io_mixed  | 725 ms                                                                   | 752 ms: 1.04x slower                                                           |
| meteor_contest           | 125 ms                                                                   | 130 ms: 1.04x slower                                                           |
| scimark_fft              | 449 ms                                                                   | 467 ms: 1.04x slower                                                           |
| mdp                      | 3.61 sec                                                                 | 3.75 sec: 1.04x slower                                                         |
| genshi_xml               | 80.5 ms                                                                  | 84.0 ms: 1.04x slower                                                          |
| async_tree_memoization   | 550 ms                                                                   | 574 ms: 1.04x slower                                                           |
| pyflate                  | 659 ms                                                                   | 689 ms: 1.05x slower                                                           |
| connected_components     | 547 ms                                                                   | 573 ms: 1.05x slower                                                           |
| pickle_pure_python       | 394 us                                                                   | 412 us: 1.05x slower                                                           |
| async_tree_none_tg       | 417 ms                                                                   | 437 ms: 1.05x slower                                                           |
| shortest_path            | 579 ms                                                                   | 609 ms: 1.05x slower                                                           |
| regex_compile            | 163 ms                                                                   | 172 ms: 1.05x slower                                                           |
| bpe_tokeniser            | 6.17 sec                                                                 | 6.51 sec: 1.05x slower                                                         |
| deepcopy_memo            | 41.9 us                                                                  | 44.3 us: 1.06x slower                                                          |
| xml_etree_generate       | 115 ms                                                                   | 122 ms: 1.06x slower                                                           |
| typing_runtime_protocols | 226 us                                                                   | 239 us: 1.06x slower                                                           |
| async_tree_none          | 436 ms                                                                   | 462 ms: 1.06x slower                                                           |
| sqlglot_optimize         | 70.9 ms                                                                  | 75.3 ms: 1.06x slower                                                          |
| nqueens                  | 129 ms                                                                   | 137 ms: 1.06x slower                                                           |
| xml_etree_process        | 81.5 ms                                                                  | 86.8 ms: 1.07x slower                                                          |
| django_template          | 46.9 ms                                                                  | 50.1 ms: 1.07x slower                                                          |
| deepcopy_reduce          | 4.03 us                                                                  | 4.33 us: 1.07x slower                                                          |
| tomli_loads              | 2.65 sec                                                                 | 2.86 sec: 1.08x slower                                                         |
| scimark_lu               | 153 ms                                                                   | 166 ms: 1.08x slower                                                           |
| go                       | 187 ms                                                                   | 203 ms: 1.08x slower                                                           |
| raytrace                 | 367 ms                                                                   | 405 ms: 1.10x slower                                                           |
| float                    | 100 ms                                                                   | 111 ms: 1.11x slower                                                           |
| scimark_monte_carlo      | 88.7 ms                                                                  | 98.2 ms: 1.11x slower                                                          |
| unpickle_pure_python     | 264 us                                                                   | 294 us: 1.11x slower                                                           |
| chaos                    | 83.9 ms                                                                  | 93.9 ms: 1.12x slower                                                          |
| nbody                    | 121 ms                                                                   | 135 ms: 1.12x slower                                                           |
| comprehensions           | 24.7 us                                                                  | 27.8 us: 1.12x slower                                                          |
| scimark_sor              | 163 ms                                                                   | 183 ms: 1.12x slower                                                           |
| richards_super           | 62.8 ms                                                                  | 72.1 ms: 1.15x slower                                                          |
| richards                 | 57.0 ms                                                                  | 65.6 ms: 1.15x slower                                                          |
| hexiom                   | 9.82 ms                                                                  | 11.6 ms: 1.18x slower                                                          |
| generators               | 48.6 ms                                                                  | 58.2 ms: 1.20x slower                                                          |
| logging_silent           | 137 ns                                                                   | 164 ns: 1.20x slower                                                           |
| deltablue                | 4.43 ms                                                                  | 5.47 ms: 1.24x slower                                                          |
| Geometric mean           | (ref)                                                                    | 1.04x slower                                                                   |

Benchmark hidden because not significant (50): bench_mp_pool, pathlib, create_gc_cycles, telco, regex_dna, python_startup, json, many_optionals, regex_v8, pylint, python_startup_no_site, coverage, regex_effbot, html5lib, thrift, json_loads, sqlalchemy_imperative, sqlalchemy_declarative, pprint_pformat, asyncio_websockets, deepcopy, sympy_sum, async_tree_cpu_io_mixed_tg, sympy_integrate, async_generators, async_tree_memoization_tg, fannkuch, logging_format, 2to3, sympy_str, xml_etree_parse, pidigits, sympy_expand, pprint_safe_repr, xml_etree_iterparse, subparsers, mako, json_dumps, dulwich_log, sqlglot_transpile, coroutines, crypto_pyaes, logging_simple, sqlglot_normalize, genshi_text, bench_thread_pool, sqlite_synth, spectral_norm, sqlglot_parse, scimark_sparse_mat_mult

- Geometric mean (including insignificant results): 1.031x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.00x