# Results vs. base

- fork: gpshead
- ref: traceback_timestamps
- machine: darwin-arm64
- commit hash: e4f54d4
- commit date: 2025-06-08
- overall geometric mean: 1.000x slower
- HPT reliability: 65.72%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250608-darwin-arm64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea | bm-20250608-darwin-arm64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 265 ms                                                                | 262 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                           |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20250608-darwin-arm64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea | bm-20250608-darwin-arm64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_generators | 264 ms                                                                | 267 ms: 1.01x slower                                                   |
| Geometric mean   | (ref)                                                                 | 1.00x faster                                                           |

Benchmark hidden because not significant (18): async_tree_io_tg, async_tree_memoization_tg, async_tree_eager_memoization_tg, async_tree_io, async_tree_none, async_tree_eager_io_tg, async_tree_eager_io, asyncio_websockets, async_tree_memoization, async_tree_none_tg, async_tree_eager_memoization, async_tree_cpu_io_mixed_tg, async_tree_eager_tg, async_tree_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250608-darwin-arm64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea | bm-20250608-darwin-arm64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 74.9 ms                                                               | 74.0 ms: 1.01x faster                                                  |
| pidigits       | 283 ms                                                                | 283 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                           |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250608-darwin-arm64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea | bm-20250608-darwin-arm64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.37 ms                                                               | 2.38 ms: 1.00x slower                                                  |
| regex_v8       | 16.2 ms                                                               | 16.4 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                           |

Benchmark hidden because not significant (2): regex_compile, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250608-darwin-arm64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea | bm-20250608-darwin-arm64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 218 us                                                                | 217 us: 1.01x faster                                                   |
| unpickle_pure_python | 161 us                                                                | 160 us: 1.00x faster                                                   |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                           |

Benchmark hidden because not significant (7): json_loads, json_dumps, xml_etree_parse, xml_etree_process, xml_etree_generate, xml_etree_iterparse, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250608-darwin-arm64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea | bm-20250608-darwin-arm64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 28.0 ms                                                               | 28.1 ms: 1.00x slower                                                  |
| python_startup_no_site | 18.6 ms                                                               | 18.7 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250608-darwin-arm64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea | bm-20250608-darwin-arm64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 21.9 ms                                                               | 21.9 ms: 1.00x slower                                                  |
| mako            | 7.83 ms                                                               | 7.87 ms: 1.00x slower                                                  |
| Geometric mean  | (ref)                                                                 | 1.00x slower                                                           |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                | bm-20250608-darwin-arm64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea | bm-20250608-darwin-arm64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|--------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody                    | 74.9 ms                                                               | 74.0 ms: 1.01x faster                                                  |
| logging_silent           | 335 ns                                                                | 331 ns: 1.01x faster                                                   |
| 2to3                     | 265 ms                                                                | 262 ms: 1.01x faster                                                   |
| json                     | 2.89 ms                                                               | 2.87 ms: 1.01x faster                                                  |
| pickle_pure_python       | 218 us                                                                | 217 us: 1.01x faster                                                   |
| logging_format           | 4.00 us                                                               | 3.98 us: 1.01x faster                                                  |
| dask                     | 827 ms                                                                | 823 ms: 1.00x faster                                                   |
| crypto_pyaes             | 57.3 ms                                                               | 57.1 ms: 1.00x faster                                                  |
| sqlglot_v2_parse         | 827 us                                                                | 824 us: 1.00x faster                                                   |
| sqlglot_v2_optimize      | 33.4 ms                                                               | 33.3 ms: 1.00x faster                                                  |
| unpickle_pure_python     | 161 us                                                                | 160 us: 1.00x faster                                                   |
| scimark_lu               | 83.4 ms                                                               | 83.2 ms: 1.00x faster                                                  |
| dulwich_log              | 24.9 ms                                                               | 24.9 ms: 1.00x faster                                                  |
| hexiom                   | 4.67 ms                                                               | 4.66 ms: 1.00x faster                                                  |
| pidigits                 | 283 ms                                                                | 283 ms: 1.00x slower                                                   |
| richards                 | 35.9 ms                                                               | 35.9 ms: 1.00x slower                                                  |
| nqueens                  | 61.8 ms                                                               | 61.9 ms: 1.00x slower                                                  |
| raytrace                 | 180 ms                                                                | 180 ms: 1.00x slower                                                   |
| go                       | 87.5 ms                                                               | 87.7 ms: 1.00x slower                                                  |
| sympy_integrate          | 11.0 ms                                                               | 11.1 ms: 1.00x slower                                                  |
| chaos                    | 40.3 ms                                                               | 40.4 ms: 1.00x slower                                                  |
| richards_super           | 39.7 ms                                                               | 39.8 ms: 1.00x slower                                                  |
| sympy_str                | 143 ms                                                                | 143 ms: 1.00x slower                                                   |
| django_template          | 21.9 ms                                                               | 21.9 ms: 1.00x slower                                                  |
| many_optionals           | 465 us                                                                | 467 us: 1.00x slower                                                   |
| meteor_contest           | 73.7 ms                                                               | 73.9 ms: 1.00x slower                                                  |
| deltablue                | 2.59 ms                                                               | 2.59 ms: 1.00x slower                                                  |
| generators               | 24.1 ms                                                               | 24.2 ms: 1.00x slower                                                  |
| fannkuch                 | 267 ms                                                                | 268 ms: 1.00x slower                                                   |
| python_startup           | 28.0 ms                                                               | 28.1 ms: 1.00x slower                                                  |
| mako                     | 7.83 ms                                                               | 7.87 ms: 1.00x slower                                                  |
| regex_effbot             | 2.37 ms                                                               | 2.38 ms: 1.00x slower                                                  |
| python_startup_no_site   | 18.6 ms                                                               | 18.7 ms: 1.01x slower                                                  |
| coverage                 | 290 ms                                                                | 291 ms: 1.01x slower                                                   |
| comprehensions           | 12.0 us                                                               | 12.0 us: 1.01x slower                                                  |
| typing_runtime_protocols | 96.3 us                                                               | 97.1 us: 1.01x slower                                                  |
| deepcopy_memo            | 19.1 us                                                               | 19.3 us: 1.01x slower                                                  |
| async_generators         | 264 ms                                                                | 267 ms: 1.01x slower                                                   |
| deepcopy                 | 157 us                                                                | 159 us: 1.01x slower                                                   |
| regex_v8                 | 16.2 ms                                                               | 16.4 ms: 1.01x slower                                                  |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                           |

Benchmark hidden because not significant (61): async_tree_io_tg, async_tree_memoization_tg, telco, async_tree_eager_memoization_tg, async_tree_io, async_tree_none, genshi_xml, json_loads, scimark_sparse_mat_mult, async_tree_eager_io_tg, spectral_norm, regex_compile, pprint_safe_repr, sqlglot_v2_transpile, async_tree_eager_io, logging_simple, sqlite_synth, asyncio_websockets, async_tree_memoization, async_tree_none_tg, scimark_fft, shortest_path, mdp, sympy_sum, sqlglot_v2_normalize, async_tree_eager_memoization, json_dumps, async_tree_cpu_io_mixed_tg, gc_traversal, bpe_tokeniser, xml_etree_parse, scimark_sor, async_tree_eager_tg, xml_etree_process, sympy_expand, async_tree_cpu_io_mixed, pylint, docutils, pyflate, html5lib, async_tree_eager_cpu_io_mixed_tg, regex_dna, subparsers, async_tree_eager, deepcopy_reduce, create_gc_cycles, async_tree_eager_cpu_io_mixed, xml_etree_generate, coroutines, xml_etree_iterparse, scimark_monte_carlo, pycparser, connected_components, pprint_pformat, sphinx, float, tomli_loads, genshi_text, k_core, pathlib, thrift

- Geometric mean (including insignificant results): 1.000x slower

# HPT report

- Reliability score: 65.72% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x