# Results vs. base

- fork: brandtbucher
- ref: jit_targets
- machine: windows-amd64
- commit hash: 997a858
- commit date: 2025-07-08
- overall geometric mean: 1.006x slower
- HPT reliability: 98.82%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250707-pythonperf1_clang-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-pythonperf1_clang-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:--------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                                           | 211 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                                            | 1.01x slower                                                                  |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250707-pythonperf1_clang-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-pythonperf1_clang-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------------------|:--------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| asyncio_websockets         | 163 ms                                                                           | 159 ms: 1.02x faster                                                          |
| async_tree_cpu_io_mixed    | 313 ms                                                                           | 316 ms: 1.01x slower                                                          |
| async_generators           | 211 ms                                                                           | 213 ms: 1.01x slower                                                          |
| async_tree_cpu_io_mixed_tg | 316 ms                                                                           | 320 ms: 1.01x slower                                                          |
| async_tree_none            | 150 ms                                                                           | 152 ms: 1.01x slower                                                          |
| coroutines                 | 12.4 ms                                                                          | 12.7 ms: 1.02x slower                                                         |
| async_tree_none_tg         | 153 ms                                                                           | 156 ms: 1.02x slower                                                          |
| Geometric mean             | (ref)                                                                            | 1.01x slower                                                                  |

Benchmark hidden because not significant (4): async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250707-pythonperf1_clang-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-pythonperf1_clang-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:--------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 146 ms                                                                           | 145 ms: 1.01x faster                                                          |
| nbody          | 60.9 ms                                                                          | 62.0 ms: 1.02x slower                                                         |
| float          | 40.3 ms                                                                          | 41.4 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                                            | 1.01x slower                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250707-pythonperf1_clang-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-pythonperf1_clang-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:--------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 1.51 ms                                                                          | 1.49 ms: 1.02x faster                                                         |
| regex_dna      | 114 ms                                                                           | 115 ms: 1.01x slower                                                          |
| regex_compile  | 72.6 ms                                                                          | 73.5 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                                            | 1.00x slower                                                                  |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250707-pythonperf1_clang-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-pythonperf1_clang-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------------|:--------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| unpickle_pure_python | 105 us                                                                           | 104 us: 1.02x faster                                                          |
| xml_etree_parse      | 90.2 ms                                                                          | 88.8 ms: 1.02x faster                                                         |
| tomli_loads          | 1.06 sec                                                                         | 1.05 sec: 1.01x faster                                                        |
| xml_etree_generate   | 46.3 ms                                                                          | 46.6 ms: 1.01x slower                                                         |
| xml_etree_process    | 32.4 ms                                                                          | 32.7 ms: 1.01x slower                                                         |
| pickle_pure_python   | 182 us                                                                           | 185 us: 1.02x slower                                                          |
| json_dumps           | 5.28 ms                                                                          | 5.47 ms: 1.04x slower                                                         |
| Geometric mean       | (ref)                                                                            | 1.00x slower                                                                  |

Benchmark hidden because not significant (2): json_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250707-pythonperf1_clang-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-pythonperf1_clang-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|------------------------|:--------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 26.7 ms                                                                          | 25.9 ms: 1.03x faster                                                         |
| python_startup_no_site | 19.8 ms                                                                          | 19.5 ms: 1.02x faster                                                         |
| Geometric mean         | (ref)                                                                            | 1.03x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250707-pythonperf1_clang-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-pythonperf1_clang-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|-----------------|:--------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| django_template | 19.8 ms                                                                          | 20.0 ms: 1.01x slower                                                         |
| genshi_xml      | 28.4 ms                                                                          | 29.2 ms: 1.03x slower                                                         |
| genshi_text     | 12.4 ms                                                                          | 12.8 ms: 1.04x slower                                                         |
| Geometric mean  | (ref)                                                                            | 1.02x slower                                                                  |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20250707-pythonperf1_clang-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-pythonperf1_clang-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------------------|:--------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pprint_safe_repr           | 431 ms                                                                           | 405 ms: 1.07x faster                                                          |
| gc_traversal               | 2.86 ms                                                                          | 2.73 ms: 1.05x faster                                                         |
| crypto_pyaes               | 43.7 ms                                                                          | 42.0 ms: 1.04x faster                                                         |
| python_startup             | 26.7 ms                                                                          | 25.9 ms: 1.03x faster                                                         |
| pprint_pformat             | 849 ms                                                                           | 825 ms: 1.03x faster                                                          |
| bpe_tokeniser              | 2.56 sec                                                                         | 2.50 sec: 1.03x faster                                                        |
| asyncio_websockets         | 163 ms                                                                           | 159 ms: 1.02x faster                                                          |
| json                       | 2.93 ms                                                                          | 2.86 ms: 1.02x faster                                                         |
| logging_format             | 5.95 us                                                                          | 5.81 us: 1.02x faster                                                         |
| fannkuch                   | 231 ms                                                                           | 226 ms: 1.02x faster                                                          |
| logging_simple             | 5.58 us                                                                          | 5.47 us: 1.02x faster                                                         |
| python_startup_no_site     | 19.8 ms                                                                          | 19.5 ms: 1.02x faster                                                         |
| unpickle_pure_python       | 105 us                                                                           | 104 us: 1.02x faster                                                          |
| telco                      | 4.15 ms                                                                          | 4.08 ms: 1.02x faster                                                         |
| comprehensions             | 9.76 us                                                                          | 9.60 us: 1.02x faster                                                         |
| regex_effbot               | 1.51 ms                                                                          | 1.49 ms: 1.02x faster                                                         |
| xml_etree_parse            | 90.2 ms                                                                          | 88.8 ms: 1.02x faster                                                         |
| shortest_path              | 348 ms                                                                           | 344 ms: 1.01x faster                                                          |
| create_gc_cycles           | 1.42 ms                                                                          | 1.40 ms: 1.01x faster                                                         |
| connected_components       | 322 ms                                                                           | 318 ms: 1.01x faster                                                          |
| tomli_loads                | 1.06 sec                                                                         | 1.05 sec: 1.01x faster                                                        |
| pidigits                   | 146 ms                                                                           | 145 ms: 1.01x faster                                                          |
| xml_etree_generate         | 46.3 ms                                                                          | 46.6 ms: 1.01x slower                                                         |
| regex_dna                  | 114 ms                                                                           | 115 ms: 1.01x slower                                                          |
| meteor_contest             | 68.6 ms                                                                          | 69.1 ms: 1.01x slower                                                         |
| xml_etree_process          | 32.4 ms                                                                          | 32.7 ms: 1.01x slower                                                         |
| async_tree_cpu_io_mixed    | 313 ms                                                                           | 316 ms: 1.01x slower                                                          |
| async_generators           | 211 ms                                                                           | 213 ms: 1.01x slower                                                          |
| async_tree_cpu_io_mixed_tg | 316 ms                                                                           | 320 ms: 1.01x slower                                                          |
| django_template            | 19.8 ms                                                                          | 20.0 ms: 1.01x slower                                                         |
| 2to3                       | 209 ms                                                                           | 211 ms: 1.01x slower                                                          |
| regex_compile              | 72.6 ms                                                                          | 73.5 ms: 1.01x slower                                                         |
| sqlglot_v2_optimize        | 31.6 ms                                                                          | 32.0 ms: 1.01x slower                                                         |
| sympy_integrate            | 11.5 ms                                                                          | 11.6 ms: 1.01x slower                                                         |
| generators                 | 17.2 ms                                                                          | 17.5 ms: 1.01x slower                                                         |
| sympy_sum                  | 80.8 ms                                                                          | 81.9 ms: 1.01x slower                                                         |
| async_tree_none            | 150 ms                                                                           | 152 ms: 1.01x slower                                                          |
| sqlglot_v2_normalize       | 62.2 ms                                                                          | 63.2 ms: 1.02x slower                                                         |
| pickle_pure_python         | 182 us                                                                           | 185 us: 1.02x slower                                                          |
| coroutines                 | 12.4 ms                                                                          | 12.7 ms: 1.02x slower                                                         |
| nbody                      | 60.9 ms                                                                          | 62.0 ms: 1.02x slower                                                         |
| coverage                   | 42.2 ms                                                                          | 43.0 ms: 1.02x slower                                                         |
| thrift                     | 429 us                                                                           | 437 us: 1.02x slower                                                          |
| async_tree_none_tg         | 153 ms                                                                           | 156 ms: 1.02x slower                                                          |
| scimark_sor                | 64.5 ms                                                                          | 65.9 ms: 1.02x slower                                                         |
| raytrace                   | 148 ms                                                                           | 151 ms: 1.02x slower                                                          |
| spectral_norm              | 47.7 ms                                                                          | 48.8 ms: 1.02x slower                                                         |
| mdp                        | 672 ms                                                                           | 687 ms: 1.02x slower                                                          |
| subparsers                 | 15.6 ms                                                                          | 15.9 ms: 1.02x slower                                                         |
| chaos                      | 32.8 ms                                                                          | 33.6 ms: 1.02x slower                                                         |
| float                      | 40.3 ms                                                                          | 41.4 ms: 1.03x slower                                                         |
| deltablue                  | 1.75 ms                                                                          | 1.79 ms: 1.03x slower                                                         |
| genshi_xml                 | 28.4 ms                                                                          | 29.2 ms: 1.03x slower                                                         |
| richards_super             | 25.6 ms                                                                          | 26.4 ms: 1.03x slower                                                         |
| richards                   | 22.6 ms                                                                          | 23.3 ms: 1.03x slower                                                         |
| sympy_str                  | 155 ms                                                                           | 159 ms: 1.03x slower                                                          |
| deepcopy                   | 140 us                                                                           | 144 us: 1.03x slower                                                          |
| go                         | 65.6 ms                                                                          | 67.9 ms: 1.03x slower                                                         |
| deepcopy_reduce            | 1.48 us                                                                          | 1.53 us: 1.03x slower                                                         |
| genshi_text                | 12.4 ms                                                                          | 12.8 ms: 1.04x slower                                                         |
| json_dumps                 | 5.28 ms                                                                          | 5.47 ms: 1.04x slower                                                         |
| hexiom                     | 3.28 ms                                                                          | 3.43 ms: 1.05x slower                                                         |
| logging_silent             | 45.4 ns                                                                          | 47.7 ns: 1.05x slower                                                         |
| nqueens                    | 51.2 ms                                                                          | 54.3 ms: 1.06x slower                                                         |
| deepcopy_memo              | 15.3 us                                                                          | 16.3 us: 1.07x slower                                                         |
| scimark_monte_carlo        | 32.6 ms                                                                          | 34.9 ms: 1.07x slower                                                         |
| scimark_lu                 | 46.8 ms                                                                          | 51.1 ms: 1.09x slower                                                         |
| Geometric mean             | (ref)                                                                            | 1.01x slower                                                                  |

Benchmark hidden because not significant (25): k_core, typing_runtime_protocols, mako, scimark_sparse_mat_mult, pycparser, pathlib, sqlglot_v2_parse, scimark_fft, html5lib, docutils, json_loads, xml_etree_iterparse, pylint, dulwich_log, async_tree_io, pyflate, regex_v8, async_tree_io_tg, async_tree_memoization, sqlglot_v2_transpile, sqlite_synth, many_optionals, sympy_expand, async_tree_memoization_tg, sphinx

- Geometric mean (including insignificant results): 1.006x slower

# HPT report

- Reliability score: 98.82% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown