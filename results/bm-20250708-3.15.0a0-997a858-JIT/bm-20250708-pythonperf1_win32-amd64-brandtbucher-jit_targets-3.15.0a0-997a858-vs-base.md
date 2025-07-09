# Results vs. base

- fork: brandtbucher
- ref: jit_targets
- machine: windows-amd64
- commit hash: 997a858
- commit date: 2025-07-08
- overall geometric mean: 1.004x slower
- HPT reliability: 93.96%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250707-pythonperf1_win32-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-pythonperf1_win32-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:--------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| docutils       | 1.65 sec                                                                         | 1.64 sec: 1.01x faster                                                        |
| sphinx         | 635 ms                                                                           | 657 ms: 1.03x slower                                                          |
| Geometric mean | (ref)                                                                            | 1.01x slower                                                                  |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250707-pythonperf1_win32-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-pythonperf1_win32-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------------------|:--------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 341 ms                                                                           | 333 ms: 1.02x faster                                                          |
| async_tree_none            | 168 ms                                                                           | 165 ms: 1.02x faster                                                          |
| async_tree_none_tg         | 169 ms                                                                           | 166 ms: 1.02x faster                                                          |
| async_tree_cpu_io_mixed    | 332 ms                                                                           | 328 ms: 1.01x faster                                                          |
| async_tree_memoization     | 204 ms                                                                           | 202 ms: 1.01x faster                                                          |
| coroutines                 | 14.5 ms                                                                          | 14.7 ms: 1.02x slower                                                         |
| Geometric mean             | (ref)                                                                            | 1.01x faster                                                                  |

Benchmark hidden because not significant (5): async_tree_memoization_tg, async_tree_io, asyncio_websockets, async_tree_io_tg, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250707-pythonperf1_win32-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-pythonperf1_win32-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:--------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 147 ms                                                                           | 149 ms: 1.02x slower                                                          |
| nbody          | 53.7 ms                                                                          | 55.4 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                                            | 1.01x slower                                                                  |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250707-pythonperf1_win32-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-pythonperf1_win32-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:--------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 78.2 ms                                                                          | 80.2 ms: 1.03x slower                                                         |
| regex_dna      | 118 ms                                                                           | 122 ms: 1.03x slower                                                          |
| regex_effbot   | 1.58 ms                                                                          | 1.66 ms: 1.05x slower                                                         |
| Geometric mean | (ref)                                                                            | 1.03x slower                                                                  |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250707-pythonperf1_win32-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-pythonperf1_win32-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|---------------------|:--------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| json_dumps          | 6.32 ms                                                                          | 6.17 ms: 1.02x faster                                                         |
| tomli_loads         | 1.13 sec                                                                         | 1.12 sec: 1.01x faster                                                        |
| xml_etree_generate  | 49.9 ms                                                                          | 51.1 ms: 1.02x slower                                                         |
| xml_etree_parse     | 86.1 ms                                                                          | 88.5 ms: 1.03x slower                                                         |
| xml_etree_process   | 34.9 ms                                                                          | 36.2 ms: 1.04x slower                                                         |
| xml_etree_iterparse | 61.7 ms                                                                          | 65.4 ms: 1.06x slower                                                         |
| Geometric mean      | (ref)                                                                            | 1.02x slower                                                                  |

Benchmark hidden because not significant (3): json_loads, pickle_pure_python, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250707-pythonperf1_win32-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-pythonperf1_win32-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|-----------------|:--------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| django_template | 24.5 ms                                                                          | 23.7 ms: 1.03x faster                                                         |
| Geometric mean  | (ref)                                                                            | 1.01x faster                                                                  |

Benchmark hidden because not significant (3): genshi_text, genshi_xml, mako

All benchmarks:
===============

| Benchmark                  | bm-20250707-pythonperf1_win32-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-pythonperf1_win32-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------------------|:--------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| logging_format             | 6.69 us                                                                          | 6.42 us: 1.04x faster                                                         |
| deepcopy_memo              | 18.0 us                                                                          | 17.3 us: 1.04x faster                                                         |
| django_template            | 24.5 ms                                                                          | 23.7 ms: 1.03x faster                                                         |
| subparsers                 | 17.1 ms                                                                          | 16.6 ms: 1.03x faster                                                         |
| typing_runtime_protocols   | 106 us                                                                           | 104 us: 1.02x faster                                                          |
| json_dumps                 | 6.32 ms                                                                          | 6.17 ms: 1.02x faster                                                         |
| async_tree_cpu_io_mixed_tg | 341 ms                                                                           | 333 ms: 1.02x faster                                                          |
| logging_simple             | 6.19 us                                                                          | 6.04 us: 1.02x faster                                                         |
| async_tree_none            | 168 ms                                                                           | 165 ms: 1.02x faster                                                          |
| async_tree_none_tg         | 169 ms                                                                           | 166 ms: 1.02x faster                                                          |
| coverage                   | 50.6 ms                                                                          | 49.8 ms: 1.02x faster                                                         |
| pprint_pformat             | 923 ms                                                                           | 908 ms: 1.02x faster                                                          |
| connected_components       | 324 ms                                                                           | 319 ms: 1.02x faster                                                          |
| shortest_path              | 357 ms                                                                           | 352 ms: 1.02x faster                                                          |
| deepcopy                   | 170 us                                                                           | 168 us: 1.01x faster                                                          |
| many_optionals             | 447 us                                                                           | 441 us: 1.01x faster                                                          |
| hexiom                     | 4.09 ms                                                                          | 4.04 ms: 1.01x faster                                                         |
| bpe_tokeniser              | 2.59 sec                                                                         | 2.55 sec: 1.01x faster                                                        |
| go                         | 76.2 ms                                                                          | 75.3 ms: 1.01x faster                                                         |
| async_tree_cpu_io_mixed    | 332 ms                                                                           | 328 ms: 1.01x faster                                                          |
| comprehensions             | 10.5 us                                                                          | 10.3 us: 1.01x faster                                                         |
| async_tree_memoization     | 204 ms                                                                           | 202 ms: 1.01x faster                                                          |
| crypto_pyaes               | 45.8 ms                                                                          | 45.4 ms: 1.01x faster                                                         |
| docutils                   | 1.65 sec                                                                         | 1.64 sec: 1.01x faster                                                        |
| tomli_loads                | 1.13 sec                                                                         | 1.12 sec: 1.01x faster                                                        |
| generators                 | 19.4 ms                                                                          | 19.6 ms: 1.01x slower                                                         |
| scimark_monte_carlo        | 40.8 ms                                                                          | 41.1 ms: 1.01x slower                                                         |
| sqlglot_v2_optimize        | 34.3 ms                                                                          | 34.6 ms: 1.01x slower                                                         |
| scimark_sor                | 75.3 ms                                                                          | 76.0 ms: 1.01x slower                                                         |
| scimark_lu                 | 61.1 ms                                                                          | 61.7 ms: 1.01x slower                                                         |
| sympy_expand               | 294 ms                                                                           | 297 ms: 1.01x slower                                                          |
| sqlglot_v2_transpile       | 992 us                                                                           | 1.00 ms: 1.01x slower                                                         |
| nqueens                    | 58.5 ms                                                                          | 59.2 ms: 1.01x slower                                                         |
| deltablue                  | 2.13 ms                                                                          | 2.16 ms: 1.01x slower                                                         |
| raytrace                   | 179 ms                                                                           | 182 ms: 1.02x slower                                                          |
| richards                   | 26.7 ms                                                                          | 27.1 ms: 1.02x slower                                                         |
| pidigits                   | 147 ms                                                                           | 149 ms: 1.02x slower                                                          |
| coroutines                 | 14.5 ms                                                                          | 14.7 ms: 1.02x slower                                                         |
| sympy_str                  | 170 ms                                                                           | 173 ms: 1.02x slower                                                          |
| gc_traversal               | 2.11 ms                                                                          | 2.14 ms: 1.02x slower                                                         |
| create_gc_cycles           | 1.31 ms                                                                          | 1.34 ms: 1.02x slower                                                         |
| sympy_integrate            | 12.6 ms                                                                          | 12.8 ms: 1.02x slower                                                         |
| pycparser                  | 698 ms                                                                           | 711 ms: 1.02x slower                                                          |
| telco                      | 4.30 ms                                                                          | 4.38 ms: 1.02x slower                                                         |
| sympy_sum                  | 87.0 ms                                                                          | 88.8 ms: 1.02x slower                                                         |
| fannkuch                   | 219 ms                                                                           | 223 ms: 1.02x slower                                                          |
| richards_super             | 30.4 ms                                                                          | 31.0 ms: 1.02x slower                                                         |
| sqlglot_v2_normalize       | 70.3 ms                                                                          | 71.8 ms: 1.02x slower                                                         |
| deepcopy_reduce            | 1.82 us                                                                          | 1.86 us: 1.02x slower                                                         |
| xml_etree_generate         | 49.9 ms                                                                          | 51.1 ms: 1.02x slower                                                         |
| regex_compile              | 78.2 ms                                                                          | 80.2 ms: 1.03x slower                                                         |
| xml_etree_parse            | 86.1 ms                                                                          | 88.5 ms: 1.03x slower                                                         |
| scimark_fft                | 152 ms                                                                           | 157 ms: 1.03x slower                                                          |
| nbody                      | 53.7 ms                                                                          | 55.4 ms: 1.03x slower                                                         |
| scimark_sparse_mat_mult    | 2.29 ms                                                                          | 2.37 ms: 1.03x slower                                                         |
| sphinx                     | 635 ms                                                                           | 657 ms: 1.03x slower                                                          |
| regex_dna                  | 118 ms                                                                           | 122 ms: 1.03x slower                                                          |
| pylint                     | 198 ms                                                                           | 205 ms: 1.03x slower                                                          |
| xml_etree_process          | 34.9 ms                                                                          | 36.2 ms: 1.04x slower                                                         |
| pathlib                    | 29.1 ms                                                                          | 30.2 ms: 1.04x slower                                                         |
| spectral_norm              | 63.5 ms                                                                          | 66.1 ms: 1.04x slower                                                         |
| regex_effbot               | 1.58 ms                                                                          | 1.66 ms: 1.05x slower                                                         |
| xml_etree_iterparse        | 61.7 ms                                                                          | 65.4 ms: 1.06x slower                                                         |
| Geometric mean             | (ref)                                                                            | 1.01x slower                                                                  |

Benchmark hidden because not significant (29): async_tree_memoization_tg, async_tree_io, asyncio_websockets, async_tree_io_tg, json, 2to3, json_loads, float, dulwich_log, genshi_text, chaos, meteor_contest, mdp, python_startup_no_site, async_generators, python_startup, genshi_xml, pyflate, sqlite_synth, html5lib, mako, thrift, sqlglot_v2_parse, regex_v8, pickle_pure_python, logging_silent, k_core, pprint_safe_repr, unpickle_pure_python

- Geometric mean (including insignificant results): 1.004x slower

# HPT report

- Reliability score: 93.96% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown