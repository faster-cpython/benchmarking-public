# Results vs. base

- fork: faster-cpython
- ref: explicit_check_perio
- machine: windows-amd64
- commit hash: 892a89d
- commit date: 2025-06-26
- overall geometric mean: 1.000x slower
- HPT reliability: 65.11%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| docutils       | 1.62 sec                                                                   | 1.63 sec: 1.01x slower                                                               |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                                         |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_generators           | 236 ms                                                                     | 226 ms: 1.04x faster                                                                 |
| async_tree_memoization_tg  | 210 ms                                                                     | 207 ms: 1.01x faster                                                                 |
| async_tree_none_tg         | 168 ms                                                                     | 166 ms: 1.01x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 339 ms                                                                     | 335 ms: 1.01x faster                                                                 |
| async_tree_io              | 393 ms                                                                     | 398 ms: 1.01x slower                                                                 |
| coroutines                 | 14.5 ms                                                                    | 14.7 ms: 1.02x slower                                                                |
| asyncio_websockets         | 156 ms                                                                     | 165 ms: 1.06x slower                                                                 |
| Geometric mean             | (ref)                                                                      | 1.00x slower                                                                         |

Benchmark hidden because not significant (4): async_tree_io_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_effbot   | 1.55 ms                                                                    | 1.53 ms: 1.02x faster                                                                |
| regex_dna      | 118 ms                                                                     | 120 ms: 1.02x slower                                                                 |
| regex_v8       | 13.2 ms                                                                    | 14.0 ms: 1.06x slower                                                                |
| Geometric mean | (ref)                                                                      | 1.02x slower                                                                         |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                                    | 63.6 ms: 1.02x faster                                                                |
| unpickle_pure_python | 134 us                                                                     | 132 us: 1.02x faster                                                                 |
| xml_etree_process    | 39.2 ms                                                                    | 38.7 ms: 1.01x faster                                                                |
| xml_etree_parse      | 90.6 ms                                                                    | 89.4 ms: 1.01x faster                                                                |
| pickle_pure_python   | 211 us                                                                     | 210 us: 1.01x faster                                                                 |
| json_dumps           | 6.15 ms                                                                    | 6.26 ms: 1.02x slower                                                                |
| json_loads           | 14.1 us                                                                    | 14.6 us: 1.04x slower                                                                |
| Geometric mean       | (ref)                                                                      | 1.00x faster                                                                         |

Benchmark hidden because not significant (2): tomli_loads, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 26.1 ms                                                                    | 26.3 ms: 1.01x slower                                                                |
| python_startup_no_site | 19.1 ms                                                                    | 19.5 ms: 1.02x slower                                                                |
| Geometric mean         | (ref)                                                                      | 1.01x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|-----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| genshi_text     | 15.3 ms                                                                    | 14.8 ms: 1.03x faster                                                                |
| genshi_xml      | 34.6 ms                                                                    | 33.9 ms: 1.02x faster                                                                |
| django_template | 24.1 ms                                                                    | 23.8 ms: 1.01x faster                                                                |
| Geometric mean  | (ref)                                                                      | 1.01x faster                                                                         |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| scimark_monte_carlo        | 41.9 ms                                                                    | 39.7 ms: 1.06x faster                                                                |
| async_generators           | 236 ms                                                                     | 226 ms: 1.04x faster                                                                 |
| scimark_sparse_mat_mult    | 2.60 ms                                                                    | 2.51 ms: 1.04x faster                                                                |
| logging_simple             | 6.47 us                                                                    | 6.26 us: 1.03x faster                                                                |
| genshi_text                | 15.3 ms                                                                    | 14.8 ms: 1.03x faster                                                                |
| crypto_pyaes               | 48.2 ms                                                                    | 46.8 ms: 1.03x faster                                                                |
| meteor_contest             | 72.7 ms                                                                    | 70.7 ms: 1.03x faster                                                                |
| scimark_lu                 | 59.3 ms                                                                    | 57.8 ms: 1.03x faster                                                                |
| xml_etree_iterparse        | 65.2 ms                                                                    | 63.6 ms: 1.02x faster                                                                |
| fannkuch                   | 263 ms                                                                     | 258 ms: 1.02x faster                                                                 |
| logging_format             | 6.85 us                                                                    | 6.72 us: 1.02x faster                                                                |
| genshi_xml                 | 34.6 ms                                                                    | 33.9 ms: 1.02x faster                                                                |
| unpickle_pure_python       | 134 us                                                                     | 132 us: 1.02x faster                                                                 |
| regex_effbot               | 1.55 ms                                                                    | 1.53 ms: 1.02x faster                                                                |
| generators                 | 19.6 ms                                                                    | 19.3 ms: 1.01x faster                                                                |
| xml_etree_process          | 39.2 ms                                                                    | 38.7 ms: 1.01x faster                                                                |
| async_tree_memoization_tg  | 210 ms                                                                     | 207 ms: 1.01x faster                                                                 |
| xml_etree_parse            | 90.6 ms                                                                    | 89.4 ms: 1.01x faster                                                                |
| async_tree_none_tg         | 168 ms                                                                     | 166 ms: 1.01x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 339 ms                                                                     | 335 ms: 1.01x faster                                                                 |
| django_template            | 24.1 ms                                                                    | 23.8 ms: 1.01x faster                                                                |
| create_gc_cycles           | 1.33 ms                                                                    | 1.31 ms: 1.01x faster                                                                |
| coverage                   | 49.8 ms                                                                    | 49.3 ms: 1.01x faster                                                                |
| sqlglot_v2_normalize       | 69.9 ms                                                                    | 69.2 ms: 1.01x faster                                                                |
| pickle_pure_python         | 211 us                                                                     | 210 us: 1.01x faster                                                                 |
| sqlglot_v2_parse           | 822 us                                                                     | 816 us: 1.01x faster                                                                 |
| telco                      | 4.56 ms                                                                    | 4.53 ms: 1.01x faster                                                                |
| pprint_safe_repr           | 535 ms                                                                     | 532 ms: 1.01x faster                                                                 |
| bpe_tokeniser              | 2.95 sec                                                                   | 2.97 sec: 1.01x slower                                                               |
| mdp                        | 806 ms                                                                     | 811 ms: 1.01x slower                                                                 |
| go                         | 76.0 ms                                                                    | 76.5 ms: 1.01x slower                                                                |
| sqlglot_v2_optimize        | 33.3 ms                                                                    | 33.6 ms: 1.01x slower                                                                |
| docutils                   | 1.62 sec                                                                   | 1.63 sec: 1.01x slower                                                               |
| raytrace                   | 177 ms                                                                     | 178 ms: 1.01x slower                                                                 |
| python_startup             | 26.1 ms                                                                    | 26.3 ms: 1.01x slower                                                                |
| deepcopy_reduce            | 1.80 us                                                                    | 1.82 us: 1.01x slower                                                                |
| logging_silent             | 315 ns                                                                     | 319 ns: 1.01x slower                                                                 |
| richards_super             | 30.6 ms                                                                    | 31.0 ms: 1.01x slower                                                                |
| sqlite_synth               | 1.58 us                                                                    | 1.60 us: 1.01x slower                                                                |
| sympy_expand               | 289 ms                                                                     | 292 ms: 1.01x slower                                                                 |
| sympy_sum                  | 87.0 ms                                                                    | 88.1 ms: 1.01x slower                                                                |
| richards                   | 27.0 ms                                                                    | 27.3 ms: 1.01x slower                                                                |
| async_tree_io              | 393 ms                                                                     | 398 ms: 1.01x slower                                                                 |
| subparsers                 | 17.0 ms                                                                    | 17.2 ms: 1.01x slower                                                                |
| sympy_str                  | 168 ms                                                                     | 171 ms: 1.01x slower                                                                 |
| dulwich_log                | 40.6 ms                                                                    | 41.3 ms: 1.02x slower                                                                |
| json_dumps                 | 6.15 ms                                                                    | 6.26 ms: 1.02x slower                                                                |
| python_startup_no_site     | 19.1 ms                                                                    | 19.5 ms: 1.02x slower                                                                |
| thrift                     | 495 us                                                                     | 504 us: 1.02x slower                                                                 |
| pycparser                  | 700 ms                                                                     | 713 ms: 1.02x slower                                                                 |
| coroutines                 | 14.5 ms                                                                    | 14.7 ms: 1.02x slower                                                                |
| regex_dna                  | 118 ms                                                                     | 120 ms: 1.02x slower                                                                 |
| chaos                      | 40.2 ms                                                                    | 41.3 ms: 1.03x slower                                                                |
| json_loads                 | 14.1 us                                                                    | 14.6 us: 1.04x slower                                                                |
| json                       | 2.95 ms                                                                    | 3.11 ms: 1.05x slower                                                                |
| regex_v8                   | 13.2 ms                                                                    | 14.0 ms: 1.06x slower                                                                |
| asyncio_websockets         | 156 ms                                                                     | 165 ms: 1.06x slower                                                                 |
| spectral_norm              | 62.2 ms                                                                    | 66.2 ms: 1.06x slower                                                                |
| Geometric mean             | (ref)                                                                      | 1.00x slower                                                                         |

Benchmark hidden because not significant (34): float, gc_traversal, k_core, comprehensions, hexiom, async_tree_io_tg, many_optionals, scimark_fft, tomli_loads, nqueens, deepcopy, nbody, pidigits, async_tree_memoization, async_tree_cpu_io_mixed, shortest_path, deltablue, pprint_pformat, pathlib, sphinx, regex_compile, xml_etree_generate, scimark_sor, deepcopy_memo, sympy_integrate, html5lib, sqlglot_v2_transpile, 2to3, async_tree_none, typing_runtime_protocols, pyflate, pylint, connected_components, mako

- Geometric mean (including insignificant results): 1.000x slower

# HPT report

- Reliability score: 65.11% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown