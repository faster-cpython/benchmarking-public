# Results vs. base

- fork: brandtbucher
- ref: jit_oz
- machine: windows-amd64
- commit hash: 6448067
- commit date: 2025-06-28
- overall geometric mean: 1.006x slower
- HPT reliability: 99.78%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250628-pythonperf1_win32_clang-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf1_win32_clang-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:--------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| docutils       | 1.55 sec                                                                               | 1.57 sec: 1.01x slower                                                         |
| html5lib       | 35.5 ms                                                                                | 36.0 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                                                  | 1.01x slower                                                                   |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250628-pythonperf1_win32_clang-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf1_win32_clang-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------------------|:--------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 323 ms                                                                                 | 317 ms: 1.02x faster                                                           |
| async_tree_none            | 149 ms                                                                                 | 151 ms: 1.01x slower                                                           |
| async_generators           | 209 ms                                                                                 | 211 ms: 1.01x slower                                                           |
| async_tree_none_tg         | 150 ms                                                                                 | 151 ms: 1.01x slower                                                           |
| Geometric mean             | (ref)                                                                                  | 1.00x slower                                                                   |

Benchmark hidden because not significant (7): async_tree_io, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_io_tg, coroutines, async_tree_memoization_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250628-pythonperf1_win32_clang-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf1_win32_clang-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:--------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 62.4 ms                                                                                | 63.9 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                                                  | 1.01x slower                                                                   |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250628-pythonperf1_win32_clang-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf1_win32_clang-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:--------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 115 ms                                                                                 | 114 ms: 1.01x faster                                                           |
| regex_compile  | 71.4 ms                                                                                | 72.2 ms: 1.01x slower                                                          |
| regex_effbot   | 1.43 ms                                                                                | 1.45 ms: 1.02x slower                                                          |
| regex_v8       | 12.3 ms                                                                                | 12.6 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                                                  | 1.01x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250628-pythonperf1_win32_clang-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf1_win32_clang-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------------|:--------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 62.1 ms                                                                                | 61.1 ms: 1.02x faster                                                          |
| xml_etree_parse      | 90.3 ms                                                                                | 89.0 ms: 1.01x faster                                                          |
| json_loads           | 13.4 us                                                                                | 13.5 us: 1.01x slower                                                          |
| xml_etree_generate   | 46.9 ms                                                                                | 47.3 ms: 1.01x slower                                                          |
| unpickle_pure_python | 105 us                                                                                 | 107 us: 1.02x slower                                                           |
| tomli_loads          | 1.05 sec                                                                               | 1.14 sec: 1.08x slower                                                         |
| Geometric mean       | (ref)                                                                                  | 1.01x slower                                                                   |

Benchmark hidden because not significant (3): pickle_pure_python, json_dumps, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250628-pythonperf1_win32_clang-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf1_win32_clang-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:--------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup | 26.1 ms                                                                                | 27.0 ms: 1.04x slower                                                          |
| Geometric mean | (ref)                                                                                  | 1.02x slower                                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250628-pythonperf1_win32_clang-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf1_win32_clang-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|-----------------|:--------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 5.36 ms                                                                                | 5.42 ms: 1.01x slower                                                          |
| genshi_text     | 12.4 ms                                                                                | 12.6 ms: 1.02x slower                                                          |
| django_template | 19.8 ms                                                                                | 20.2 ms: 1.02x slower                                                          |
| Geometric mean  | (ref)                                                                                  | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20250628-pythonperf1_win32_clang-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf1_win32_clang-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------------------|:--------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| scimark_lu                 | 49.9 ms                                                                                | 47.1 ms: 1.06x faster                                                          |
| coverage                   | 42.5 ms                                                                                | 41.2 ms: 1.03x faster                                                          |
| async_tree_cpu_io_mixed_tg | 323 ms                                                                                 | 317 ms: 1.02x faster                                                           |
| xml_etree_iterparse        | 62.1 ms                                                                                | 61.1 ms: 1.02x faster                                                          |
| xml_etree_parse            | 90.3 ms                                                                                | 89.0 ms: 1.01x faster                                                          |
| json                       | 2.84 ms                                                                                | 2.81 ms: 1.01x faster                                                          |
| deepcopy                   | 141 us                                                                                 | 139 us: 1.01x faster                                                           |
| telco                      | 4.19 ms                                                                                | 4.14 ms: 1.01x faster                                                          |
| mdp                        | 680 ms                                                                                 | 673 ms: 1.01x faster                                                           |
| scimark_sparse_mat_mult    | 2.39 ms                                                                                | 2.36 ms: 1.01x faster                                                          |
| shortest_path              | 347 ms                                                                                 | 344 ms: 1.01x faster                                                           |
| regex_dna                  | 115 ms                                                                                 | 114 ms: 1.01x faster                                                           |
| raytrace                   | 145 ms                                                                                 | 145 ms: 1.01x faster                                                           |
| scimark_sor                | 62.6 ms                                                                                | 62.3 ms: 1.01x faster                                                          |
| deepcopy_reduce            | 1.49 us                                                                                | 1.50 us: 1.01x slower                                                          |
| async_tree_none            | 149 ms                                                                                 | 151 ms: 1.01x slower                                                           |
| json_loads                 | 13.4 us                                                                                | 13.5 us: 1.01x slower                                                          |
| async_generators           | 209 ms                                                                                 | 211 ms: 1.01x slower                                                           |
| xml_etree_generate         | 46.9 ms                                                                                | 47.3 ms: 1.01x slower                                                          |
| docutils                   | 1.55 sec                                                                               | 1.57 sec: 1.01x slower                                                         |
| async_tree_none_tg         | 150 ms                                                                                 | 151 ms: 1.01x slower                                                           |
| connected_components       | 320 ms                                                                                 | 323 ms: 1.01x slower                                                           |
| hexiom                     | 3.26 ms                                                                                | 3.29 ms: 1.01x slower                                                          |
| regex_compile              | 71.4 ms                                                                                | 72.2 ms: 1.01x slower                                                          |
| mako                       | 5.36 ms                                                                                | 5.42 ms: 1.01x slower                                                          |
| pyflate                    | 236 ms                                                                                 | 239 ms: 1.01x slower                                                           |
| go                         | 65.5 ms                                                                                | 66.5 ms: 1.01x slower                                                          |
| html5lib                   | 35.5 ms                                                                                | 36.0 ms: 1.02x slower                                                          |
| regex_effbot               | 1.43 ms                                                                                | 1.45 ms: 1.02x slower                                                          |
| logging_silent             | 44.8 ns                                                                                | 45.6 ns: 1.02x slower                                                          |
| sqlglot_v2_transpile       | 885 us                                                                                 | 899 us: 1.02x slower                                                           |
| deepcopy_memo              | 15.1 us                                                                                | 15.3 us: 1.02x slower                                                          |
| pprint_pformat             | 843 ms                                                                                 | 858 ms: 1.02x slower                                                           |
| unpickle_pure_python       | 105 us                                                                                 | 107 us: 1.02x slower                                                           |
| sqlglot_v2_optimize        | 31.2 ms                                                                                | 31.8 ms: 1.02x slower                                                          |
| dulwich_log                | 38.4 ms                                                                                | 39.1 ms: 1.02x slower                                                          |
| genshi_text                | 12.4 ms                                                                                | 12.6 ms: 1.02x slower                                                          |
| thrift                     | 428 us                                                                                 | 437 us: 1.02x slower                                                           |
| sqlglot_v2_parse           | 697 us                                                                                 | 713 us: 1.02x slower                                                           |
| django_template            | 19.8 ms                                                                                | 20.2 ms: 1.02x slower                                                          |
| comprehensions             | 9.66 us                                                                                | 9.88 us: 1.02x slower                                                          |
| scimark_fft                | 153 ms                                                                                 | 156 ms: 1.02x slower                                                           |
| regex_v8                   | 12.3 ms                                                                                | 12.6 ms: 1.02x slower                                                          |
| nbody                      | 62.4 ms                                                                                | 63.9 ms: 1.02x slower                                                          |
| crypto_pyaes               | 42.8 ms                                                                                | 43.8 ms: 1.03x slower                                                          |
| gc_traversal               | 2.82 ms                                                                                | 2.89 ms: 1.03x slower                                                          |
| fannkuch                   | 243 ms                                                                                 | 250 ms: 1.03x slower                                                           |
| pprint_safe_repr           | 406 ms                                                                                 | 419 ms: 1.03x slower                                                           |
| python_startup             | 26.1 ms                                                                                | 27.0 ms: 1.04x slower                                                          |
| nqueens                    | 49.7 ms                                                                                | 51.5 ms: 1.04x slower                                                          |
| bpe_tokeniser              | 2.53 sec                                                                               | 2.64 sec: 1.04x slower                                                         |
| tomli_loads                | 1.05 sec                                                                               | 1.14 sec: 1.08x slower                                                         |
| spectral_norm              | 45.6 ms                                                                                | 50.8 ms: 1.11x slower                                                          |
| Geometric mean             | (ref)                                                                                  | 1.01x slower                                                                   |

Benchmark hidden because not significant (39): create_gc_cycles, logging_simple, logging_format, async_tree_io, deltablue, async_tree_cpu_io_mixed, 2to3, scimark_monte_carlo, float, generators, sympy_str, richards, async_tree_memoization, async_tree_io_tg, sympy_expand, richards_super, sqlglot_v2_normalize, sympy_integrate, pickle_pure_python, pidigits, coroutines, typing_runtime_protocols, async_tree_memoization_tg, json_dumps, k_core, sqlite_synth, sphinx, sympy_sum, genshi_xml, xml_etree_process, meteor_contest, pycparser, many_optionals, subparsers, python_startup_no_site, pylint, asyncio_websockets, chaos, pathlib

- Geometric mean (including insignificant results): 1.006x slower

# HPT report

- Reliability score: 99.78% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown