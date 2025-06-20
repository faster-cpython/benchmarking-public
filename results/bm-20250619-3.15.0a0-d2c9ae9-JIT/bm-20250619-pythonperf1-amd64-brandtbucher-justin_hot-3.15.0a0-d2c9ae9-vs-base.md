# Results vs. base

- fork: brandtbucher
- ref: justin_hot
- machine: windows-amd64
- commit hash: d2c9ae9
- commit date: 2025-06-19
- overall geometric mean: 1.003x faster
- HPT reliability: 82.73%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250619-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| docutils       | 1.68 sec                                                                   | 1.66 sec: 1.01x faster                                                 |
| sphinx         | 651 ms                                                                     | 644 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                           |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250619-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 345 ms                                                                     | 342 ms: 1.01x faster                                                   |
| async_tree_none            | 169 ms                                                                     | 171 ms: 1.01x slower                                                   |
| coroutines                 | 14.1 ms                                                                    | 14.3 ms: 1.02x slower                                                  |
| Geometric mean             | (ref)                                                                      | 1.00x slower                                                           |

Benchmark hidden because not significant (8): async_tree_memoization_tg, async_tree_io_tg, async_generators, async_tree_io, asyncio_websockets, async_tree_memoization, async_tree_none_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250619-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 57.7 ms                                                                    | 62.4 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                                      | 1.03x slower                                                           |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

Benchmark hidden because not significant (4): regex_dna, regex_effbot, regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250619-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|---------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_iterparse | 64.6 ms                                                                    | 62.8 ms: 1.03x faster                                                  |
| xml_etree_generate  | 52.2 ms                                                                    | 50.7 ms: 1.03x faster                                                  |
| xml_etree_process   | 36.7 ms                                                                    | 36.4 ms: 1.01x faster                                                  |
| pickle_pure_python  | 206 us                                                                     | 205 us: 1.01x faster                                                   |
| xml_etree_parse     | 87.5 ms                                                                    | 88.1 ms: 1.01x slower                                                  |
| json_dumps          | 6.32 ms                                                                    | 6.47 ms: 1.02x slower                                                  |
| Geometric mean      | (ref)                                                                      | 1.01x faster                                                           |

Benchmark hidden because not significant (3): unpickle_pure_python, json_loads, tomli_loads

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250619-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|-----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 24.2 ms                                                                    | 24.0 ms: 1.01x faster                                                  |
| mako            | 5.42 ms                                                                    | 5.47 ms: 1.01x slower                                                  |
| genshi_text     | 15.5 ms                                                                    | 15.7 ms: 1.01x slower                                                  |
| genshi_xml      | 34.3 ms                                                                    | 35.1 ms: 1.02x slower                                                  |
| Geometric mean  | (ref)                                                                      | 1.01x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250619-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| scimark_monte_carlo        | 42.4 ms                                                                    | 40.2 ms: 1.05x faster                                                  |
| fannkuch                   | 241 ms                                                                     | 232 ms: 1.04x faster                                                   |
| shortest_path              | 372 ms                                                                     | 359 ms: 1.04x faster                                                   |
| richards                   | 28.1 ms                                                                    | 27.2 ms: 1.03x faster                                                  |
| pprint_pformat             | 1.07 sec                                                                   | 1.03 sec: 1.03x faster                                                 |
| xml_etree_iterparse        | 64.6 ms                                                                    | 62.8 ms: 1.03x faster                                                  |
| richards_super             | 31.6 ms                                                                    | 30.7 ms: 1.03x faster                                                  |
| xml_etree_generate         | 52.2 ms                                                                    | 50.7 ms: 1.03x faster                                                  |
| scimark_lu                 | 60.5 ms                                                                    | 58.9 ms: 1.03x faster                                                  |
| pprint_safe_repr           | 520 ms                                                                     | 507 ms: 1.03x faster                                                   |
| logging_silent             | 322 ns                                                                     | 314 ns: 1.03x faster                                                   |
| hexiom                     | 4.21 ms                                                                    | 4.12 ms: 1.02x faster                                                  |
| meteor_contest             | 73.3 ms                                                                    | 71.8 ms: 1.02x faster                                                  |
| generators                 | 20.0 ms                                                                    | 19.6 ms: 1.02x faster                                                  |
| create_gc_cycles           | 1.34 ms                                                                    | 1.32 ms: 1.02x faster                                                  |
| nqueens                    | 59.2 ms                                                                    | 58.4 ms: 1.01x faster                                                  |
| typing_runtime_protocols   | 104 us                                                                     | 103 us: 1.01x faster                                                   |
| deepcopy_reduce            | 1.81 us                                                                    | 1.79 us: 1.01x faster                                                  |
| logging_format             | 6.73 us                                                                    | 6.64 us: 1.01x faster                                                  |
| json                       | 3.11 ms                                                                    | 3.07 ms: 1.01x faster                                                  |
| sphinx                     | 651 ms                                                                     | 644 ms: 1.01x faster                                                   |
| docutils                   | 1.68 sec                                                                   | 1.66 sec: 1.01x faster                                                 |
| crypto_pyaes               | 46.9 ms                                                                    | 46.5 ms: 1.01x faster                                                  |
| mdp                        | 802 ms                                                                     | 795 ms: 1.01x faster                                                   |
| comprehensions             | 10.9 us                                                                    | 10.8 us: 1.01x faster                                                  |
| logging_simple             | 6.32 us                                                                    | 6.27 us: 1.01x faster                                                  |
| sqlglot_v2_transpile       | 1.01 ms                                                                    | 1.00 ms: 1.01x faster                                                  |
| deltablue                  | 2.26 ms                                                                    | 2.24 ms: 1.01x faster                                                  |
| async_tree_cpu_io_mixed_tg | 345 ms                                                                     | 342 ms: 1.01x faster                                                   |
| django_template            | 24.2 ms                                                                    | 24.0 ms: 1.01x faster                                                  |
| xml_etree_process          | 36.7 ms                                                                    | 36.4 ms: 1.01x faster                                                  |
| pickle_pure_python         | 206 us                                                                     | 205 us: 1.01x faster                                                   |
| bpe_tokeniser              | 2.65 sec                                                                   | 2.63 sec: 1.01x faster                                                 |
| sqlglot_v2_optimize        | 34.6 ms                                                                    | 34.4 ms: 1.01x faster                                                  |
| sqlglot_v2_normalize       | 71.2 ms                                                                    | 70.7 ms: 1.01x faster                                                  |
| coverage                   | 50.5 ms                                                                    | 50.2 ms: 1.01x faster                                                  |
| raytrace                   | 181 ms                                                                     | 182 ms: 1.00x slower                                                   |
| sympy_expand               | 295 ms                                                                     | 297 ms: 1.01x slower                                                   |
| xml_etree_parse            | 87.5 ms                                                                    | 88.1 ms: 1.01x slower                                                  |
| scimark_fft                | 160 ms                                                                     | 161 ms: 1.01x slower                                                   |
| mako                       | 5.42 ms                                                                    | 5.47 ms: 1.01x slower                                                  |
| sympy_str                  | 170 ms                                                                     | 172 ms: 1.01x slower                                                   |
| deepcopy                   | 167 us                                                                     | 169 us: 1.01x slower                                                   |
| telco                      | 4.36 ms                                                                    | 4.41 ms: 1.01x slower                                                  |
| genshi_text                | 15.5 ms                                                                    | 15.7 ms: 1.01x slower                                                  |
| gc_traversal               | 2.14 ms                                                                    | 2.17 ms: 1.01x slower                                                  |
| async_tree_none            | 169 ms                                                                     | 171 ms: 1.01x slower                                                   |
| sympy_integrate            | 12.6 ms                                                                    | 12.8 ms: 1.02x slower                                                  |
| coroutines                 | 14.1 ms                                                                    | 14.3 ms: 1.02x slower                                                  |
| chaos                      | 39.5 ms                                                                    | 40.4 ms: 1.02x slower                                                  |
| json_dumps                 | 6.32 ms                                                                    | 6.47 ms: 1.02x slower                                                  |
| genshi_xml                 | 34.3 ms                                                                    | 35.1 ms: 1.02x slower                                                  |
| deepcopy_memo              | 17.8 us                                                                    | 18.2 us: 1.03x slower                                                  |
| nbody                      | 57.7 ms                                                                    | 62.4 ms: 1.08x slower                                                  |
| Geometric mean             | (ref)                                                                      | 1.00x faster                                                           |

Benchmark hidden because not significant (38): sqlglot_v2_parse, unpickle_pure_python, html5lib, go, async_tree_memoization_tg, json_loads, pylint, scimark_sparse_mat_mult, k_core, async_tree_io_tg, python_startup, pidigits, pyflate, connected_components, scimark_sor, tomli_loads, sqlite_synth, regex_dna, python_startup_no_site, subparsers, regex_effbot, pathlib, sympy_sum, regex_compile, thrift, async_generators, spectral_norm, pycparser, many_optionals, 2to3, async_tree_io, dulwich_log, asyncio_websockets, float, async_tree_memoization, async_tree_none_tg, async_tree_cpu_io_mixed, regex_v8

- Geometric mean (including insignificant results): 1.003x faster

# HPT report

- Reliability score: 82.73% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown