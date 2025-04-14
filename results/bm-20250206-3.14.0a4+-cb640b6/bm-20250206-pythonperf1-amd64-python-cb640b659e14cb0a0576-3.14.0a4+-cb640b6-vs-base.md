# Results vs. base

- fork: python
- ref: cb640b659e14cb0a0576
- machine: windows-amd64
- commit hash: cb640b6
- commit date: 2025-02-06
- overall geometric mean: 1.001x slower
- HPT reliability: 57.26%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20250206-pythonperf1-amd64-python-555dc50c811e3e9ebdc3-3.14.0a4+-555dc50 | bm-20250206-pythonperf1-amd64-python-cb640b659e14cb0a0576-3.14.0a4+-cb640b6 |
|---------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg | 225 ms                                                                      | 216 ms: 1.04x faster                                                        |
| async_tree_none           | 189 ms                                                                      | 185 ms: 1.02x faster                                                        |
| async_tree_io             | 423 ms                                                                      | 417 ms: 1.01x faster                                                        |
| async_tree_memoization    | 223 ms                                                                      | 220 ms: 1.01x faster                                                        |
| async_tree_none_tg        | 177 ms                                                                      | 175 ms: 1.01x faster                                                        |
| async_tree_cpu_io_mixed   | 339 ms                                                                      | 336 ms: 1.01x faster                                                        |
| async_generators          | 221 ms                                                                      | 227 ms: 1.03x slower                                                        |
| asyncio_websockets        | 306 ms                                                                      | 314 ms: 1.03x slower                                                        |
| Geometric mean            | (ref)                                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed_tg, async_tree_io_tg, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250206-pythonperf1-amd64-python-555dc50c811e3e9ebdc3-3.14.0a4+-555dc50 | bm-20250206-pythonperf1-amd64-python-cb640b659e14cb0a0576-3.14.0a4+-cb640b6 |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.2 ms                                                                     | 72.2 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250206-pythonperf1-amd64-python-555dc50c811e3e9ebdc3-3.14.0a4+-555dc50 | bm-20250206-pythonperf1-amd64-python-cb640b659e14cb0a0576-3.14.0a4+-cb640b6 |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 85.6 ms                                                                     | 84.7 ms: 1.01x faster                                                       |
| regex_effbot   | 1.44 ms                                                                     | 1.46 ms: 1.01x slower                                                       |
| regex_dna      | 115 ms                                                                      | 124 ms: 1.08x slower                                                        |
| regex_v8       | 14.3 ms                                                                     | 15.5 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                                       | 1.04x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250206-pythonperf1-amd64-python-555dc50c811e3e9ebdc3-3.14.0a4+-555dc50 | bm-20250206-pythonperf1-amd64-python-cb640b659e14cb0a0576-3.14.0a4+-cb640b6 |
|----------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 148 us                                                                      | 140 us: 1.06x faster                                                        |
| tomli_loads          | 1.39 sec                                                                    | 1.36 sec: 1.03x faster                                                      |
| xml_etree_generate   | 56.4 ms                                                                     | 55.5 ms: 1.02x faster                                                       |
| pickle_pure_python   | 218 us                                                                      | 214 us: 1.01x faster                                                        |
| json_loads           | 15.5 us                                                                     | 15.3 us: 1.01x faster                                                       |
| xml_etree_process    | 39.5 ms                                                                     | 39.1 ms: 1.01x faster                                                       |
| xml_etree_parse      | 90.5 ms                                                                     | 94.1 ms: 1.04x slower                                                       |
| xml_etree_iterparse  | 63.4 ms                                                                     | 67.3 ms: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250206-pythonperf1-amd64-python-555dc50c811e3e9ebdc3-3.14.0a4+-555dc50 | bm-20250206-pythonperf1-amd64-python-cb640b659e14cb0a0576-3.14.0a4+-cb640b6 |
|------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 19.7 ms                                                                     | 19.4 ms: 1.02x faster                                                       |
| Geometric mean         | (ref)                                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250206-pythonperf1-amd64-python-555dc50c811e3e9ebdc3-3.14.0a4+-555dc50 | bm-20250206-pythonperf1-amd64-python-cb640b659e14cb0a0576-3.14.0a4+-cb640b6 |
|-----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.74 ms                                                                     | 6.61 ms: 1.02x faster                                                       |
| genshi_text     | 15.6 ms                                                                     | 15.5 ms: 1.01x faster                                                       |
| django_template | 25.1 ms                                                                     | 25.5 ms: 1.02x slower                                                       |
| Geometric mean  | (ref)                                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                 | bm-20250206-pythonperf1-amd64-python-555dc50c811e3e9ebdc3-3.14.0a4+-555dc50 | bm-20250206-pythonperf1-amd64-python-cb640b659e14cb0a0576-3.14.0a4+-cb640b6 |
|---------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python      | 148 us                                                                      | 140 us: 1.06x faster                                                        |
| async_tree_memoization_tg | 225 ms                                                                      | 216 ms: 1.04x faster                                                        |
| scimark_sparse_mat_mult   | 2.63 ms                                                                     | 2.55 ms: 1.03x faster                                                       |
| generators                | 20.2 ms                                                                     | 19.7 ms: 1.03x faster                                                       |
| tomli_loads               | 1.39 sec                                                                    | 1.36 sec: 1.03x faster                                                      |
| logging_simple            | 6.33 us                                                                     | 6.20 us: 1.02x faster                                                       |
| scimark_sor               | 85.4 ms                                                                     | 83.5 ms: 1.02x faster                                                       |
| scimark_monte_carlo       | 44.7 ms                                                                     | 43.7 ms: 1.02x faster                                                       |
| mako                      | 6.74 ms                                                                     | 6.61 ms: 1.02x faster                                                       |
| async_tree_none           | 189 ms                                                                      | 185 ms: 1.02x faster                                                        |
| logging_format            | 6.73 us                                                                     | 6.62 us: 1.02x faster                                                       |
| python_startup_no_site    | 19.7 ms                                                                     | 19.4 ms: 1.02x faster                                                       |
| xml_etree_generate        | 56.4 ms                                                                     | 55.5 ms: 1.02x faster                                                       |
| pickle_pure_python        | 218 us                                                                      | 214 us: 1.01x faster                                                        |
| bpe_tokeniser             | 2.91 sec                                                                    | 2.87 sec: 1.01x faster                                                      |
| json_loads                | 15.5 us                                                                     | 15.3 us: 1.01x faster                                                       |
| async_tree_io             | 423 ms                                                                      | 417 ms: 1.01x faster                                                        |
| async_tree_memoization    | 223 ms                                                                      | 220 ms: 1.01x faster                                                        |
| comprehensions            | 11.1 us                                                                     | 10.9 us: 1.01x faster                                                       |
| deepcopy_memo             | 19.2 us                                                                     | 18.9 us: 1.01x faster                                                       |
| xml_etree_process         | 39.5 ms                                                                     | 39.1 ms: 1.01x faster                                                       |
| regex_compile             | 85.6 ms                                                                     | 84.7 ms: 1.01x faster                                                       |
| async_tree_none_tg        | 177 ms                                                                      | 175 ms: 1.01x faster                                                        |
| genshi_text               | 15.6 ms                                                                     | 15.5 ms: 1.01x faster                                                       |
| scimark_lu                | 60.8 ms                                                                     | 60.2 ms: 1.01x faster                                                       |
| pyflate                   | 296 ms                                                                      | 294 ms: 1.01x faster                                                        |
| async_tree_cpu_io_mixed   | 339 ms                                                                      | 336 ms: 1.01x faster                                                        |
| sympy_expand              | 301 ms                                                                      | 299 ms: 1.01x faster                                                        |
| richards_super            | 32.8 ms                                                                     | 32.5 ms: 1.01x faster                                                       |
| sqlglot_normalize         | 189 ms                                                                      | 188 ms: 1.00x faster                                                        |
| dulwich_log               | 42.5 ms                                                                     | 42.3 ms: 1.00x faster                                                       |
| go                        | 85.7 ms                                                                     | 86.1 ms: 1.01x slower                                                       |
| many_optionals            | 434 us                                                                      | 437 us: 1.01x slower                                                        |
| sqlglot_transpile         | 1.06 ms                                                                     | 1.06 ms: 1.01x slower                                                       |
| create_gc_cycles          | 1.21 ms                                                                     | 1.22 ms: 1.01x slower                                                       |
| shortest_path             | 352 ms                                                                      | 355 ms: 1.01x slower                                                        |
| subparsers                | 16.3 ms                                                                     | 16.4 ms: 1.01x slower                                                       |
| hexiom                    | 4.24 ms                                                                     | 4.27 ms: 1.01x slower                                                       |
| mdp                       | 1.58 sec                                                                    | 1.59 sec: 1.01x slower                                                      |
| chaos                     | 41.3 ms                                                                     | 41.8 ms: 1.01x slower                                                       |
| typing_runtime_protocols  | 105 us                                                                      | 106 us: 1.01x slower                                                        |
| regex_effbot              | 1.44 ms                                                                     | 1.46 ms: 1.01x slower                                                       |
| sqlglot_parse             | 852 us                                                                      | 863 us: 1.01x slower                                                        |
| nbody                     | 71.2 ms                                                                     | 72.2 ms: 1.01x slower                                                       |
| gc_traversal              | 2.00 ms                                                                     | 2.03 ms: 1.01x slower                                                       |
| pycparser                 | 717 ms                                                                      | 728 ms: 1.02x slower                                                        |
| pprint_pformat            | 1.05 sec                                                                    | 1.06 sec: 1.02x slower                                                      |
| django_template           | 25.1 ms                                                                     | 25.5 ms: 1.02x slower                                                       |
| spectral_norm             | 57.9 ms                                                                     | 59.0 ms: 1.02x slower                                                       |
| richards                  | 28.7 ms                                                                     | 29.2 ms: 1.02x slower                                                       |
| nqueens                   | 62.0 ms                                                                     | 63.2 ms: 1.02x slower                                                       |
| logging_silent            | 57.8 ns                                                                     | 58.9 ns: 1.02x slower                                                       |
| crypto_pyaes              | 47.0 ms                                                                     | 48.1 ms: 1.02x slower                                                       |
| async_generators          | 221 ms                                                                      | 227 ms: 1.03x slower                                                        |
| asyncio_websockets        | 306 ms                                                                      | 314 ms: 1.03x slower                                                        |
| fannkuch                  | 262 ms                                                                      | 272 ms: 1.04x slower                                                        |
| xml_etree_parse           | 90.5 ms                                                                     | 94.1 ms: 1.04x slower                                                       |
| xml_etree_iterparse       | 63.4 ms                                                                     | 67.3 ms: 1.06x slower                                                       |
| regex_dna                 | 115 ms                                                                      | 124 ms: 1.08x slower                                                        |
| regex_v8                  | 14.3 ms                                                                     | 15.5 ms: 1.08x slower                                                       |
| Geometric mean            | (ref)                                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (34): json, scimark_fft, deepcopy, async_tree_cpu_io_mixed_tg, meteor_contest, async_tree_io_tg, sqlite_synth, sphinx, sympy_str, sympy_sum, coverage, float, raytrace, bench_mp_pool, docutils, sympy_integrate, connected_components, pprint_safe_repr, sqlglot_optimize, 2to3, pidigits, deltablue, python_startup, bench_thread_pool, genshi_xml, telco, html5lib, k_core, coroutines, deepcopy_reduce, pylint, thrift, json_dumps, pathlib

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 57.26% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown