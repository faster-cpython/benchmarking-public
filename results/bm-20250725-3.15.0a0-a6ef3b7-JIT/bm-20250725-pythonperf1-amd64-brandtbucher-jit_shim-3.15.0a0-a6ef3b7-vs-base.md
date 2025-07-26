# Results vs. base

- fork: brandtbucher
- ref: jit_shim
- machine: windows-amd64
- commit hash: a6ef3b7
- commit date: 2025-07-25
- overall geometric mean: 1.002x slower
- HPT reliability: 92.71%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250725-pythonperf1-amd64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 | bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 220 ms                                                                     | 223 ms: 1.01x slower                                                 |
| docutils       | 1.65 sec                                                                   | 1.66 sec: 1.01x slower                                               |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                         |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20250725-pythonperf1-amd64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 | bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|---------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io             | 398 ms                                                                     | 389 ms: 1.02x faster                                                 |
| async_generators          | 253 ms                                                                     | 248 ms: 1.02x faster                                                 |
| asyncio_websockets        | 166 ms                                                                     | 164 ms: 1.02x faster                                                 |
| async_tree_cpu_io_mixed   | 337 ms                                                                     | 344 ms: 1.02x slower                                                 |
| async_tree_io_tg          | 386 ms                                                                     | 395 ms: 1.02x slower                                                 |
| async_tree_memoization_tg | 210 ms                                                                     | 218 ms: 1.04x slower                                                 |
| async_tree_memoization    | 203 ms                                                                     | 216 ms: 1.07x slower                                                 |
| Geometric mean            | (ref)                                                                      | 1.01x slower                                                         |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_none_tg, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250725-pythonperf1-amd64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 | bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 44.4 ms                                                                    | 43.9 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                                      | 1.00x faster                                                         |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250725-pythonperf1-amd64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 | bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_v8       | 14.9 ms                                                                    | 14.4 ms: 1.04x faster                                                |
| regex_compile  | 80.0 ms                                                                    | 82.5 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                                      | 1.00x slower                                                         |

Benchmark hidden because not significant (2): regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250725-pythonperf1-amd64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 | bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 1.11 sec                                                                   | 1.12 sec: 1.01x slower                                               |
| json_loads           | 14.2 us                                                                    | 14.4 us: 1.01x slower                                                |
| xml_etree_process    | 35.2 ms                                                                    | 36.0 ms: 1.02x slower                                                |
| xml_etree_generate   | 49.8 ms                                                                    | 51.4 ms: 1.03x slower                                                |
| unpickle_pure_python | 105 us                                                                     | 109 us: 1.04x slower                                                 |
| Geometric mean       | (ref)                                                                      | 1.02x slower                                                         |

Benchmark hidden because not significant (4): xml_etree_iterparse, json_dumps, xml_etree_parse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250725-pythonperf1-amd64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 | bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup | 26.7 ms                                                                    | 27.1 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                         |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250725-pythonperf1-amd64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 | bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|-----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_text     | 16.1 ms                                                                    | 15.8 ms: 1.02x faster                                                |
| mako            | 5.40 ms                                                                    | 5.33 ms: 1.01x faster                                                |
| django_template | 23.9 ms                                                                    | 24.8 ms: 1.04x slower                                                |
| Geometric mean  | (ref)                                                                      | 1.00x slower                                                         |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                 | bm-20250725-pythonperf1-amd64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 | bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|---------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| many_optionals            | 604 us                                                                     | 576 us: 1.05x faster                                                 |
| json                      | 3.04 ms                                                                    | 2.93 ms: 1.04x faster                                                |
| subparsers                | 31.5 ms                                                                    | 30.3 ms: 1.04x faster                                                |
| sqlite_synth              | 1.61 us                                                                    | 1.55 us: 1.04x faster                                                |
| regex_v8                  | 14.9 ms                                                                    | 14.4 ms: 1.04x faster                                                |
| chaos                     | 41.3 ms                                                                    | 40.1 ms: 1.03x faster                                                |
| sqlglot_v2_transpile      | 1.01 ms                                                                    | 983 us: 1.03x faster                                                 |
| spectral_norm             | 67.0 ms                                                                    | 65.5 ms: 1.02x faster                                                |
| async_tree_io             | 398 ms                                                                     | 389 ms: 1.02x faster                                                 |
| async_generators          | 253 ms                                                                     | 248 ms: 1.02x faster                                                 |
| genshi_text               | 16.1 ms                                                                    | 15.8 ms: 1.02x faster                                                |
| richards_super            | 31.6 ms                                                                    | 31.0 ms: 1.02x faster                                                |
| asyncio_websockets        | 166 ms                                                                     | 164 ms: 1.02x faster                                                 |
| comprehensions            | 10.6 us                                                                    | 10.4 us: 1.02x faster                                                |
| deepcopy_reduce           | 1.84 us                                                                    | 1.81 us: 1.01x faster                                                |
| deepcopy_memo             | 18.0 us                                                                    | 17.8 us: 1.01x faster                                                |
| raytrace                  | 183 ms                                                                     | 181 ms: 1.01x faster                                                 |
| sympy_expand              | 304 ms                                                                     | 300 ms: 1.01x faster                                                 |
| mako                      | 5.40 ms                                                                    | 5.33 ms: 1.01x faster                                                |
| float                     | 44.4 ms                                                                    | 43.9 ms: 1.01x faster                                                |
| mdp                       | 808 ms                                                                     | 802 ms: 1.01x faster                                                 |
| bpe_tokeniser             | 2.54 sec                                                                   | 2.52 sec: 1.01x faster                                               |
| docutils                  | 1.65 sec                                                                   | 1.66 sec: 1.01x slower                                               |
| pyflate                   | 249 ms                                                                     | 252 ms: 1.01x slower                                                 |
| 2to3                      | 220 ms                                                                     | 223 ms: 1.01x slower                                                 |
| tomli_loads               | 1.11 sec                                                                   | 1.12 sec: 1.01x slower                                               |
| logging_simple            | 5.97 us                                                                    | 6.06 us: 1.01x slower                                                |
| json_loads                | 14.2 us                                                                    | 14.4 us: 1.01x slower                                                |
| hexiom                    | 4.05 ms                                                                    | 4.11 ms: 1.02x slower                                                |
| python_startup            | 26.7 ms                                                                    | 27.1 ms: 1.02x slower                                                |
| async_tree_cpu_io_mixed   | 337 ms                                                                     | 344 ms: 1.02x slower                                                 |
| async_tree_io_tg          | 386 ms                                                                     | 395 ms: 1.02x slower                                                 |
| xml_etree_process         | 35.2 ms                                                                    | 36.0 ms: 1.02x slower                                                |
| go                        | 77.0 ms                                                                    | 78.8 ms: 1.02x slower                                                |
| thrift                    | 491 us                                                                     | 505 us: 1.03x slower                                                 |
| logging_format            | 6.52 us                                                                    | 6.71 us: 1.03x slower                                                |
| scimark_lu                | 58.2 ms                                                                    | 59.9 ms: 1.03x slower                                                |
| sympy_integrate           | 13.0 ms                                                                    | 13.4 ms: 1.03x slower                                                |
| sympy_sum                 | 88.7 ms                                                                    | 91.4 ms: 1.03x slower                                                |
| regex_compile             | 80.0 ms                                                                    | 82.5 ms: 1.03x slower                                                |
| xml_etree_generate        | 49.8 ms                                                                    | 51.4 ms: 1.03x slower                                                |
| logging_silent            | 54.3 ns                                                                    | 56.1 ns: 1.03x slower                                                |
| async_tree_memoization_tg | 210 ms                                                                     | 218 ms: 1.04x slower                                                 |
| django_template           | 23.9 ms                                                                    | 24.8 ms: 1.04x slower                                                |
| unpickle_pure_python      | 105 us                                                                     | 109 us: 1.04x slower                                                 |
| scimark_monte_carlo       | 40.3 ms                                                                    | 42.2 ms: 1.05x slower                                                |
| fannkuch                  | 207 ms                                                                     | 217 ms: 1.05x slower                                                 |
| typing_runtime_protocols  | 102 us                                                                     | 108 us: 1.05x slower                                                 |
| async_tree_memoization    | 203 ms                                                                     | 216 ms: 1.07x slower                                                 |
| Geometric mean            | (ref)                                                                      | 1.00x slower                                                         |

Benchmark hidden because not significant (43): pathlib, crypto_pyaes, deepcopy, regex_dna, nqueens, scimark_fft, pidigits, sphinx, async_tree_cpu_io_mixed_tg, generators, richards, scimark_sor, xml_etree_iterparse, json_dumps, async_tree_none, pprint_safe_repr, shortest_path, pylint, deltablue, telco, sqlglot_v2_normalize, k_core, gc_traversal, connected_components, nbody, dulwich_log, pprint_pformat, meteor_contest, sympy_str, html5lib, xml_etree_parse, sqlglot_v2_optimize, genshi_xml, pycparser, sqlglot_v2_parse, async_tree_none_tg, python_startup_no_site, coverage, create_gc_cycles, coroutines, regex_effbot, pickle_pure_python, scimark_sparse_mat_mult

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 92.71% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown