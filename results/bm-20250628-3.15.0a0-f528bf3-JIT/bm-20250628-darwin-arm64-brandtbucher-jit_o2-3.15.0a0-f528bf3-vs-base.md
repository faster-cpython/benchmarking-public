# Results vs. base

- fork: brandtbucher
- ref: jit_o2
- machine: darwin-arm64
- commit hash: f528bf3
- commit date: 2025-06-28
- overall geometric mean: 1.001x slower
- HPT reliability: 97.30%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250628-darwin-arm64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-darwin-arm64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 172 ms                                                                | 174 ms: 1.01x slower                                          |
| docutils       | 1.46 sec                                                              | 1.47 sec: 1.01x slower                                        |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                  |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20250628-darwin-arm64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-darwin-arm64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| async_generators | 279 ms                                                                | 277 ms: 1.01x faster                                          |
| async_tree_eager | 64.3 ms                                                               | 64.6 ms: 1.00x slower                                         |
| Geometric mean   | (ref)                                                                 | 1.00x slower                                                  |

Benchmark hidden because not significant (17): async_tree_cpu_io_mixed_tg, async_tree_eager_tg, async_tree_cpu_io_mixed, async_tree_eager_cpu_io_mixed, async_tree_none, async_tree_eager_cpu_io_mixed_tg, asyncio_websockets, async_tree_eager_io, async_tree_memoization, coroutines, async_tree_eager_io_tg, async_tree_memoization_tg, async_tree_none_tg, async_tree_io_tg, async_tree_io, async_tree_eager_memoization, async_tree_eager_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250628-darwin-arm64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-darwin-arm64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| nbody          | 75.3 ms                                                               | 75.7 ms: 1.00x slower                                         |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                  |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250628-darwin-arm64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-darwin-arm64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_dna      | 145 ms                                                                | 143 ms: 1.01x faster                                          |
| regex_effbot   | 2.37 ms                                                               | 2.36 ms: 1.00x faster                                         |
| regex_v8       | 16.2 ms                                                               | 16.1 ms: 1.00x faster                                         |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                  |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250628-darwin-arm64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-darwin-arm64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|---------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| xml_etree_iterparse | 72.7 ms                                                               | 72.3 ms: 1.01x faster                                         |
| json_loads          | 16.3 us                                                               | 16.4 us: 1.00x slower                                         |
| Geometric mean      | (ref)                                                                 | 1.00x faster                                                  |

Benchmark hidden because not significant (7): json_dumps, tomli_loads, pickle_pure_python, xml_etree_generate, unpickle_pure_python, xml_etree_parse, xml_etree_process

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250628-darwin-arm64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-darwin-arm64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| mako           | 6.93 ms                                                               | 6.94 ms: 1.00x slower                                         |
| genshi_text    | 14.8 ms                                                               | 14.8 ms: 1.00x slower                                         |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                  |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark               | bm-20250628-darwin-arm64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-darwin-arm64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| sqlite_synth            | 1.62 us                                                               | 1.58 us: 1.02x faster                                         |
| pprint_safe_repr        | 534 ms                                                                | 527 ms: 1.01x faster                                          |
| regex_dna               | 145 ms                                                                | 143 ms: 1.01x faster                                          |
| create_gc_cycles        | 1.37 ms                                                               | 1.35 ms: 1.01x faster                                         |
| async_generators        | 279 ms                                                                | 277 ms: 1.01x faster                                          |
| sympy_sum               | 75.7 ms                                                               | 75.1 ms: 1.01x faster                                         |
| xml_etree_iterparse     | 72.7 ms                                                               | 72.3 ms: 1.01x faster                                         |
| dask                    | 770 ms                                                                | 766 ms: 1.00x faster                                          |
| thrift                  | 443 us                                                                | 440 us: 1.00x faster                                          |
| gc_traversal            | 3.21 ms                                                               | 3.19 ms: 1.00x faster                                         |
| deepcopy_memo           | 19.6 us                                                               | 19.5 us: 1.00x faster                                         |
| spectral_norm           | 68.2 ms                                                               | 67.9 ms: 1.00x faster                                         |
| regex_effbot            | 2.37 ms                                                               | 2.36 ms: 1.00x faster                                         |
| regex_v8                | 16.2 ms                                                               | 16.1 ms: 1.00x faster                                         |
| dulwich_log             | 25.0 ms                                                               | 24.9 ms: 1.00x faster                                         |
| bpe_tokeniser           | 3.09 sec                                                              | 3.08 sec: 1.00x faster                                        |
| sqlglot_v2_normalize    | 68.6 ms                                                               | 68.4 ms: 1.00x faster                                         |
| mako                    | 6.93 ms                                                               | 6.94 ms: 1.00x slower                                         |
| mdp                     | 757 ms                                                                | 759 ms: 1.00x slower                                          |
| chaos                   | 39.4 ms                                                               | 39.5 ms: 1.00x slower                                         |
| crypto_pyaes            | 55.8 ms                                                               | 56.0 ms: 1.00x slower                                         |
| scimark_lu              | 82.1 ms                                                               | 82.4 ms: 1.00x slower                                         |
| async_tree_eager        | 64.3 ms                                                               | 64.6 ms: 1.00x slower                                         |
| deepcopy                | 156 us                                                                | 156 us: 1.00x slower                                          |
| go                      | 87.2 ms                                                               | 87.6 ms: 1.00x slower                                         |
| json_loads              | 16.3 us                                                               | 16.4 us: 1.00x slower                                         |
| genshi_text             | 14.8 ms                                                               | 14.8 ms: 1.00x slower                                         |
| raytrace                | 178 ms                                                                | 179 ms: 1.00x slower                                          |
| nbody                   | 75.3 ms                                                               | 75.7 ms: 1.00x slower                                         |
| nqueens                 | 61.6 ms                                                               | 61.9 ms: 1.00x slower                                         |
| logging_format          | 3.75 us                                                               | 3.77 us: 1.01x slower                                         |
| many_optionals          | 476 us                                                                | 479 us: 1.01x slower                                          |
| logging_silent          | 72.4 ns                                                               | 72.8 ns: 1.01x slower                                         |
| sympy_expand            | 243 ms                                                                | 244 ms: 1.01x slower                                          |
| deepcopy_reduce         | 1.66 us                                                               | 1.67 us: 1.01x slower                                         |
| hexiom                  | 4.73 ms                                                               | 4.76 ms: 1.01x slower                                         |
| scimark_fft             | 199 ms                                                                | 200 ms: 1.01x slower                                          |
| logging_simple          | 3.45 us                                                               | 3.48 us: 1.01x slower                                         |
| comprehensions          | 12.1 us                                                               | 12.2 us: 1.01x slower                                         |
| richards                | 36.1 ms                                                               | 36.4 ms: 1.01x slower                                         |
| docutils                | 1.46 sec                                                              | 1.47 sec: 1.01x slower                                        |
| scimark_sor             | 88.1 ms                                                               | 89.0 ms: 1.01x slower                                         |
| fannkuch                | 299 ms                                                                | 302 ms: 1.01x slower                                          |
| telco                   | 4.59 ms                                                               | 4.64 ms: 1.01x slower                                         |
| 2to3                    | 172 ms                                                                | 174 ms: 1.01x slower                                          |
| scimark_sparse_mat_mult | 3.53 ms                                                               | 3.58 ms: 1.01x slower                                         |
| sqlglot_v2_transpile    | 974 us                                                                | 991 us: 1.02x slower                                          |
| pathlib                 | 21.9 ms                                                               | 22.4 ms: 1.02x slower                                         |
| sqlglot_v2_parse        | 796 us                                                                | 816 us: 1.02x slower                                          |
| richards_super          | 39.7 ms                                                               | 41.1 ms: 1.04x slower                                         |
| Geometric mean          | (ref)                                                                 | 1.00x slower                                                  |

Benchmark hidden because not significant (51): python_startup, coverage, sympy_integrate, json_dumps, async_tree_cpu_io_mixed_tg, html5lib, tomli_loads, scimark_monte_carlo, genshi_xml, async_tree_eager_tg, pickle_pure_python, float, async_tree_cpu_io_mixed, sphinx, generators, async_tree_eager_cpu_io_mixed, xml_etree_generate, meteor_contest, async_tree_none, async_tree_eager_cpu_io_mixed_tg, asyncio_websockets, async_tree_eager_io, k_core, async_tree_memoization, unpickle_pure_python, pidigits, coroutines, connected_components, json, async_tree_eager_io_tg, xml_etree_parse, shortest_path, django_template, sympy_str, regex_compile, pyflate, pylint, async_tree_memoization_tg, async_tree_none_tg, async_tree_io_tg, sqlglot_v2_optimize, typing_runtime_protocols, python_startup_no_site, async_tree_io, deltablue, async_tree_eager_memoization, async_tree_eager_memoization_tg, pprint_pformat, xml_etree_process, subparsers, pycparser

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 97.30% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x