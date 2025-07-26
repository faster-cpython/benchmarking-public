# Results vs. base

- fork: brandtbucher
- ref: jit_shim
- machine: darwin-arm64
- commit hash: a6ef3b7
- commit date: 2025-07-25
- overall geometric mean: 1.004x faster
- HPT reliability: 97.59%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250725-darwin-arm64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 | bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 202 ms                                                                | 202 ms: 1.00x faster                                            |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                    |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20250725-darwin-arm64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 | bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| coroutines       | 18.1 ms                                                               | 18.0 ms: 1.00x faster                                           |
| async_tree_eager | 71.1 ms                                                               | 71.4 ms: 1.00x slower                                           |
| async_generators | 311 ms                                                                | 316 ms: 1.02x slower                                            |
| Geometric mean   | (ref)                                                                 | 1.00x slower                                                    |

Benchmark hidden because not significant (16): async_tree_io_tg, async_tree_none, async_tree_eager_io, async_tree_eager_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_eager_io_tg, asyncio_websockets, async_tree_eager_cpu_io_mixed, async_tree_io, async_tree_eager_memoization_tg, async_tree_eager_memoization, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_eager_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250725-darwin-arm64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 | bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 56.9 ms                                                               | 55.7 ms: 1.02x faster                                           |
| pidigits       | 310 ms                                                                | 310 ms: 1.00x slower                                            |
| nbody          | 78.4 ms                                                               | 78.9 ms: 1.01x slower                                           |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250725-darwin-arm64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 | bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 2.38 ms                                                               | 2.35 ms: 1.01x faster                                           |
| regex_compile  | 83.1 ms                                                               | 82.1 ms: 1.01x faster                                           |
| regex_dna      | 153 ms                                                                | 152 ms: 1.01x faster                                            |
| regex_v8       | 17.1 ms                                                               | 17.0 ms: 1.01x faster                                           |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250725-darwin-arm64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 | bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|---------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| json_dumps          | 7.33 ms                                                               | 7.25 ms: 1.01x faster                                           |
| pickle_pure_python  | 234 us                                                                | 233 us: 1.01x faster                                            |
| json_loads          | 19.3 us                                                               | 19.2 us: 1.00x faster                                           |
| xml_etree_iterparse | 82.5 ms                                                               | 82.3 ms: 1.00x faster                                           |
| xml_etree_process   | 39.1 ms                                                               | 39.3 ms: 1.01x slower                                           |
| tomli_loads         | 1.37 sec                                                              | 1.39 sec: 1.01x slower                                          |
| Geometric mean      | (ref)                                                                 | 1.00x faster                                                    |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_generate, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250725-darwin-arm64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 | bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 18.5 ms                                                               | 18.5 ms: 1.00x slower                                           |
| python_startup_no_site | 13.6 ms                                                               | 14.0 ms: 1.03x slower                                           |
| Geometric mean         | (ref)                                                                 | 1.02x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250725-darwin-arm64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 | bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| genshi_xml      | 37.7 ms                                                               | 36.3 ms: 1.04x faster                                           |
| genshi_text     | 17.1 ms                                                               | 16.6 ms: 1.03x faster                                           |
| django_template | 26.0 ms                                                               | 25.7 ms: 1.01x faster                                           |
| Geometric mean  | (ref)                                                                 | 1.02x faster                                                    |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20250725-darwin-arm64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 | bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| deepcopy_memo           | 24.5 us                                                               | 23.5 us: 1.04x faster                                           |
| genshi_xml              | 37.7 ms                                                               | 36.3 ms: 1.04x faster                                           |
| genshi_text             | 17.1 ms                                                               | 16.6 ms: 1.03x faster                                           |
| chaos                   | 43.7 ms                                                               | 42.7 ms: 1.02x faster                                           |
| go                      | 97.9 ms                                                               | 95.8 ms: 1.02x faster                                           |
| scimark_lu              | 82.9 ms                                                               | 81.2 ms: 1.02x faster                                           |
| float                   | 56.9 ms                                                               | 55.7 ms: 1.02x faster                                           |
| deepcopy_reduce         | 2.00 us                                                               | 1.96 us: 1.02x faster                                           |
| deepcopy                | 194 us                                                                | 190 us: 1.02x faster                                            |
| logging_silent          | 81.7 ns                                                               | 80.3 ns: 1.02x faster                                           |
| pprint_pformat          | 1.03 sec                                                              | 1.01 sec: 1.02x faster                                          |
| telco                   | 4.92 ms                                                               | 4.84 ms: 1.02x faster                                           |
| scimark_monte_carlo     | 49.9 ms                                                               | 49.1 ms: 1.01x faster                                           |
| coverage                | 52.1 ms                                                               | 51.3 ms: 1.01x faster                                           |
| nqueens                 | 68.0 ms                                                               | 67.1 ms: 1.01x faster                                           |
| regex_effbot            | 2.38 ms                                                               | 2.35 ms: 1.01x faster                                           |
| django_template         | 26.0 ms                                                               | 25.7 ms: 1.01x faster                                           |
| regex_compile           | 83.1 ms                                                               | 82.1 ms: 1.01x faster                                           |
| pprint_safe_repr        | 505 ms                                                                | 498 ms: 1.01x faster                                            |
| richards                | 37.1 ms                                                               | 36.7 ms: 1.01x faster                                           |
| json_dumps              | 7.33 ms                                                               | 7.25 ms: 1.01x faster                                           |
| json                    | 3.44 ms                                                               | 3.40 ms: 1.01x faster                                           |
| meteor_contest          | 84.3 ms                                                               | 83.5 ms: 1.01x faster                                           |
| richards_super          | 41.4 ms                                                               | 41.0 ms: 1.01x faster                                           |
| logging_simple          | 3.77 us                                                               | 3.73 us: 1.01x faster                                           |
| hexiom                  | 5.18 ms                                                               | 5.14 ms: 1.01x faster                                           |
| thrift                  | 513 us                                                                | 508 us: 1.01x faster                                            |
| mdp                     | 932 ms                                                                | 925 ms: 1.01x faster                                            |
| regex_dna               | 153 ms                                                                | 152 ms: 1.01x faster                                            |
| logging_format          | 4.09 us                                                               | 4.06 us: 1.01x faster                                           |
| sympy_expand            | 287 ms                                                                | 285 ms: 1.01x faster                                            |
| fannkuch                | 276 ms                                                                | 274 ms: 1.01x faster                                            |
| scimark_sor             | 92.6 ms                                                               | 92.0 ms: 1.01x faster                                           |
| pickle_pure_python      | 234 us                                                                | 233 us: 1.01x faster                                            |
| regex_v8                | 17.1 ms                                                               | 17.0 ms: 1.01x faster                                           |
| spectral_norm           | 69.2 ms                                                               | 68.8 ms: 1.00x faster                                           |
| crypto_pyaes            | 55.7 ms                                                               | 55.4 ms: 1.00x faster                                           |
| sqlglot_v2_transpile    | 1.13 ms                                                               | 1.12 ms: 1.00x faster                                           |
| json_loads              | 19.3 us                                                               | 19.2 us: 1.00x faster                                           |
| sqlglot_v2_parse        | 900 us                                                                | 896 us: 1.00x faster                                            |
| sympy_str               | 173 ms                                                                | 172 ms: 1.00x faster                                            |
| 2to3                    | 202 ms                                                                | 202 ms: 1.00x faster                                            |
| coroutines              | 18.1 ms                                                               | 18.0 ms: 1.00x faster                                           |
| shortest_path           | 454 ms                                                                | 452 ms: 1.00x faster                                            |
| xml_etree_iterparse     | 82.5 ms                                                               | 82.3 ms: 1.00x faster                                           |
| generators              | 26.9 ms                                                               | 26.8 ms: 1.00x faster                                           |
| pidigits                | 310 ms                                                                | 310 ms: 1.00x slower                                            |
| raytrace                | 193 ms                                                                | 193 ms: 1.00x slower                                            |
| gc_traversal            | 4.61 ms                                                               | 4.62 ms: 1.00x slower                                           |
| sqlite_synth            | 1.74 us                                                               | 1.75 us: 1.00x slower                                           |
| sqlglot_v2_optimize     | 38.5 ms                                                               | 38.6 ms: 1.00x slower                                           |
| connected_components    | 417 ms                                                                | 419 ms: 1.00x slower                                            |
| python_startup          | 18.5 ms                                                               | 18.5 ms: 1.00x slower                                           |
| async_tree_eager        | 71.1 ms                                                               | 71.4 ms: 1.00x slower                                           |
| bpe_tokeniser           | 3.31 sec                                                              | 3.32 sec: 1.00x slower                                          |
| subparsers              | 29.2 ms                                                               | 29.3 ms: 1.00x slower                                           |
| many_optionals          | 709 us                                                                | 713 us: 1.01x slower                                            |
| pyflate                 | 340 ms                                                                | 342 ms: 1.01x slower                                            |
| nbody                   | 78.4 ms                                                               | 78.9 ms: 1.01x slower                                           |
| scimark_sparse_mat_mult | 3.70 ms                                                               | 3.72 ms: 1.01x slower                                           |
| xml_etree_process       | 39.1 ms                                                               | 39.3 ms: 1.01x slower                                           |
| create_gc_cycles        | 2.12 ms                                                               | 2.14 ms: 1.01x slower                                           |
| tomli_loads             | 1.37 sec                                                              | 1.39 sec: 1.01x slower                                          |
| async_generators        | 311 ms                                                                | 316 ms: 1.02x slower                                            |
| python_startup_no_site  | 13.6 ms                                                               | 14.0 ms: 1.03x slower                                           |
| Geometric mean          | (ref)                                                                 | 1.00x faster                                                    |

Benchmark hidden because not significant (36): html5lib, async_tree_io_tg, async_tree_none, async_tree_eager_io, k_core, async_tree_eager_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization, scimark_fft, async_tree_eager_io_tg, mako, deltablue, asyncio_websockets, sqlglot_v2_normalize, xml_etree_parse, async_tree_eager_cpu_io_mixed, comprehensions, async_tree_io, typing_runtime_protocols, dulwich_log, xml_etree_generate, async_tree_eager_memoization_tg, sympy_sum, async_tree_eager_memoization, unpickle_pure_python, sympy_integrate, async_tree_cpu_io_mixed_tg, pathlib, dask, async_tree_memoization_tg, pylint, docutils, async_tree_eager_tg, async_tree_none_tg, sphinx, pycparser

- Geometric mean (including insignificant results): 1.004x faster

# HPT report

- Reliability score: 97.59% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x