# Results vs. base

- fork: brandtbucher
- ref: justin_hot
- machine: darwin-arm64
- commit hash: a987be7
- commit date: 2025-06-23
- overall geometric mean: 1.000x faster
- HPT reliability: 99.11%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250623-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| html5lib       | 34.9 ms                                                               | 34.0 ms: 1.03x faster                                             |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                      |

Benchmark hidden because not significant (3): 2to3, docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250623-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_generators | 291 ms                                                                | 288 ms: 1.01x faster                                              |
| coroutines       | 19.3 ms                                                               | 19.2 ms: 1.00x faster                                             |
| async_tree_eager | 71.5 ms                                                               | 71.8 ms: 1.01x slower                                             |
| Geometric mean   | (ref)                                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (16): async_tree_memoization_tg, async_tree_eager_io_tg, async_tree_io_tg, async_tree_none, async_tree_io, async_tree_none_tg, async_tree_eager_cpu_io_mixed, async_tree_memoization, async_tree_eager_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_eager_io, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250623-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 58.2 ms                                                               | 57.8 ms: 1.01x faster                                             |
| nbody          | 76.4 ms                                                               | 76.2 ms: 1.00x faster                                             |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250623-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 79.7 ms                                                               | 79.5 ms: 1.00x faster                                             |
| regex_v8       | 16.2 ms                                                               | 16.2 ms: 1.00x faster                                             |
| regex_dna      | 143 ms                                                                | 143 ms: 1.00x faster                                              |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250623-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| unpickle_pure_python | 138 us                                                                | 137 us: 1.01x faster                                              |
| xml_etree_process    | 37.5 ms                                                               | 37.4 ms: 1.00x faster                                             |
| json_dumps           | 6.83 ms                                                               | 6.88 ms: 1.01x slower                                             |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                      |

Benchmark hidden because not significant (6): json_loads, xml_etree_iterparse, pickle_pure_python, xml_etree_generate, xml_etree_parse, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250623-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 18.2 ms                                                               | 18.1 ms: 1.01x faster                                             |
| python_startup         | 27.8 ms                                                               | 27.6 ms: 1.01x faster                                             |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250623-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| django_template | 25.4 ms                                                               | 25.2 ms: 1.01x faster                                             |
| genshi_xml      | 36.2 ms                                                               | 36.0 ms: 1.01x faster                                             |
| genshi_text     | 17.6 ms                                                               | 17.7 ms: 1.00x slower                                             |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250623-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| html5lib                 | 34.9 ms                                                               | 34.0 ms: 1.03x faster                                             |
| typing_runtime_protocols | 105 us                                                                | 103 us: 1.02x faster                                              |
| async_generators         | 291 ms                                                                | 288 ms: 1.01x faster                                              |
| telco                    | 4.63 ms                                                               | 4.59 ms: 1.01x faster                                             |
| python_startup_no_site   | 18.2 ms                                                               | 18.1 ms: 1.01x faster                                             |
| bpe_tokeniser            | 3.10 sec                                                              | 3.08 sec: 1.01x faster                                            |
| sympy_sum                | 81.3 ms                                                               | 80.8 ms: 1.01x faster                                             |
| python_startup           | 27.8 ms                                                               | 27.6 ms: 1.01x faster                                             |
| float                    | 58.2 ms                                                               | 57.8 ms: 1.01x faster                                             |
| django_template          | 25.4 ms                                                               | 25.2 ms: 1.01x faster                                             |
| unpickle_pure_python     | 138 us                                                                | 137 us: 1.01x faster                                              |
| genshi_xml               | 36.2 ms                                                               | 36.0 ms: 1.01x faster                                             |
| xml_etree_process        | 37.5 ms                                                               | 37.4 ms: 1.00x faster                                             |
| sympy_expand             | 265 ms                                                                | 264 ms: 1.00x faster                                              |
| nbody                    | 76.4 ms                                                               | 76.2 ms: 1.00x faster                                             |
| scimark_sor              | 91.1 ms                                                               | 90.8 ms: 1.00x faster                                             |
| coroutines               | 19.3 ms                                                               | 19.2 ms: 1.00x faster                                             |
| shortest_path            | 339 ms                                                                | 338 ms: 1.00x faster                                              |
| dulwich_log              | 26.8 ms                                                               | 26.8 ms: 1.00x faster                                             |
| sqlglot_v2_transpile     | 1.08 ms                                                               | 1.08 ms: 1.00x faster                                             |
| mdp                      | 826 ms                                                                | 824 ms: 1.00x faster                                              |
| regex_compile            | 79.7 ms                                                               | 79.5 ms: 1.00x faster                                             |
| deepcopy                 | 175 us                                                                | 174 us: 1.00x faster                                              |
| sqlglot_v2_parse         | 892 us                                                                | 890 us: 1.00x faster                                              |
| regex_v8                 | 16.2 ms                                                               | 16.2 ms: 1.00x faster                                             |
| comprehensions           | 13.0 us                                                               | 13.0 us: 1.00x faster                                             |
| regex_dna                | 143 ms                                                                | 143 ms: 1.00x faster                                              |
| pyflate                  | 321 ms                                                                | 321 ms: 1.00x slower                                              |
| genshi_text              | 17.6 ms                                                               | 17.7 ms: 1.00x slower                                             |
| spectral_norm            | 74.3 ms                                                               | 74.5 ms: 1.00x slower                                             |
| meteor_contest           | 76.8 ms                                                               | 77.1 ms: 1.00x slower                                             |
| go                       | 100 ms                                                                | 101 ms: 1.00x slower                                              |
| scimark_monte_carlo      | 53.4 ms                                                               | 53.6 ms: 1.00x slower                                             |
| sympy_integrate          | 11.4 ms                                                               | 11.5 ms: 1.00x slower                                             |
| chaos                    | 47.9 ms                                                               | 48.1 ms: 1.00x slower                                             |
| create_gc_cycles         | 1.36 ms                                                               | 1.36 ms: 1.00x slower                                             |
| generators               | 31.6 ms                                                               | 31.7 ms: 1.00x slower                                             |
| raytrace                 | 210 ms                                                                | 211 ms: 1.00x slower                                              |
| async_tree_eager         | 71.5 ms                                                               | 71.8 ms: 1.01x slower                                             |
| sqlite_synth             | 1.59 us                                                               | 1.60 us: 1.01x slower                                             |
| json_dumps               | 6.83 ms                                                               | 6.88 ms: 1.01x slower                                             |
| logging_silent           | 341 ns                                                                | 345 ns: 1.01x slower                                              |
| scimark_fft              | 206 ms                                                                | 209 ms: 1.01x slower                                              |
| nqueens                  | 68.6 ms                                                               | 69.5 ms: 1.01x slower                                             |
| scimark_sparse_mat_mult  | 3.55 ms                                                               | 3.65 ms: 1.03x slower                                             |
| scimark_lu               | 84.5 ms                                                               | 86.8 ms: 1.03x slower                                             |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (55): pprint_safe_repr, connected_components, async_tree_memoization_tg, json, async_tree_eager_io_tg, async_tree_io_tg, async_tree_none, many_optionals, async_tree_io, async_tree_none_tg, hexiom, sphinx, pylint, json_loads, sqlglot_v2_normalize, xml_etree_iterparse, async_tree_eager_cpu_io_mixed, async_tree_memoization, fannkuch, k_core, async_tree_eager_memoization_tg, richards_super, async_tree_cpu_io_mixed_tg, deepcopy_memo, async_tree_eager_tg, logging_simple, async_tree_eager_cpu_io_mixed_tg, dask, regex_effbot, async_tree_cpu_io_mixed, asyncio_websockets, 2to3, pidigits, pickle_pure_python, async_tree_eager_io, logging_format, mako, gc_traversal, docutils, pathlib, thrift, subparsers, async_tree_eager_memoization, crypto_pyaes, xml_etree_generate, richards, deepcopy_reduce, sympy_str, xml_etree_parse, coverage, pprint_pformat, pycparser, sqlglot_v2_optimize, tomli_loads, deltablue

- Geometric mean (including insignificant results): 1.000x faster

# HPT report

- Reliability score: 99.11% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x