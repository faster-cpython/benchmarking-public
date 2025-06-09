# Results vs. base

- fork: gpshead
- ref: traceback_timestamps
- machine: linux-aarch64
- commit hash: e4f54d4
- commit date: 2025-06-08
- overall geometric mean: 1.000x faster
- HPT reliability: 71.41%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250608-arminc-aarch64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea | bm-20250608-arminc-aarch64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------|:-----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 300 ms                                                                  | 298 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                                   | 1.00x slower                                                             |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250608-arminc-aarch64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea | bm-20250608-arminc-aarch64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|-------------------------|:-----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 392 ms                                                                  | 383 ms: 1.02x faster                                                     |
| async_tree_memoization  | 468 ms                                                                  | 457 ms: 1.02x faster                                                     |
| async_tree_cpu_io_mixed | 661 ms                                                                  | 650 ms: 1.02x faster                                                     |
| Geometric mean          | (ref)                                                                   | 1.01x faster                                                             |

Benchmark hidden because not significant (8): async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, asyncio_websockets, coroutines, async_tree_none_tg, async_tree_io, async_generators

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, pidigits, nbody

Benchmarks with tag 'regex':
============================

Benchmark hidden because not significant (4): regex_effbot, regex_v8, regex_dna, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark      | bm-20250608-arminc-aarch64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea | bm-20250608-arminc-aarch64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------|:-----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads    | 2.47 sec                                                                | 2.49 sec: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                   | 1.00x faster                                                             |

Benchmark hidden because not significant (8): pickle_pure_python, json_dumps, xml_etree_iterparse, xml_etree_generate, json_loads, xml_etree_parse, unpickle_pure_python, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250608-arminc-aarch64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea | bm-20250608-arminc-aarch64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------|:-----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup | 15.3 ms                                                                 | 15.1 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                                   | 1.01x faster                                                             |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, mako, genshi_xml, django_template

All benchmarks:
===============

| Benchmark               | bm-20250608-arminc-aarch64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea | bm-20250608-arminc-aarch64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|-------------------------|:-----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 392 ms                                                                  | 383 ms: 1.02x faster                                                     |
| async_tree_memoization  | 468 ms                                                                  | 457 ms: 1.02x faster                                                     |
| thrift                  | 197 ms                                                                  | 192 ms: 1.02x faster                                                     |
| sqlite_synth            | 3.93 us                                                                 | 3.86 us: 1.02x faster                                                    |
| async_tree_cpu_io_mixed | 661 ms                                                                  | 650 ms: 1.02x faster                                                     |
| python_startup          | 15.3 ms                                                                 | 15.1 ms: 1.01x faster                                                    |
| logging_silent          | 618 ns                                                                  | 612 ns: 1.01x faster                                                     |
| 2to3                    | 300 ms                                                                  | 298 ms: 1.01x faster                                                     |
| richards                | 51.6 ms                                                                 | 52.1 ms: 1.01x slower                                                    |
| tomli_loads             | 2.47 sec                                                                | 2.49 sec: 1.01x slower                                                   |
| shortest_path           | 580 ms                                                                  | 585 ms: 1.01x slower                                                     |
| gc_traversal            | 6.82 ms                                                                 | 6.90 ms: 1.01x slower                                                    |
| pprint_pformat          | 2.03 sec                                                                | 2.06 sec: 1.01x slower                                                   |
| create_gc_cycles        | 3.72 ms                                                                 | 3.82 ms: 1.03x slower                                                    |
| Geometric mean          | (ref)                                                                   | 1.00x faster                                                             |

Benchmark hidden because not significant (78): generators, spectral_norm, pickle_pure_python, scimark_lu, scimark_sparse_mat_mult, deepcopy_reduce, sympy_sum, json_dumps, scimark_monte_carlo, many_optionals, logging_simple, hexiom, pycparser, coverage, sqlglot_v2_parse, sympy_expand, scimark_sor, sqlglot_v2_normalize, scimark_fft, async_tree_io_tg, genshi_text, async_tree_cpu_io_mixed_tg, deepcopy_memo, async_tree_memoization_tg, asyncio_websockets, sphinx, python_startup_no_site, fannkuch, json, coroutines, raytrace, mako, logging_format, regex_effbot, pprint_safe_repr, regex_v8, async_tree_none_tg, async_tree_io, pylint, regex_dna, subparsers, xml_etree_iterparse, deltablue, nqueens, float, crypto_pyaes, dulwich_log, xml_etree_generate, comprehensions, bpe_tokeniser, json_loads, genshi_xml, xml_etree_parse, mdp, regex_compile, django_template, docutils, meteor_contest, connected_components, k_core, pathlib, unpickle_pure_python, xml_etree_process, telco, pyflate, typing_runtime_protocols, deepcopy, sqlglot_v2_optimize, pidigits, go, html5lib, async_generators, sympy_integrate, chaos, richards_super, nbody, sympy_str, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.000x faster

# HPT report

- Reliability score: 71.41% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x