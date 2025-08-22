# Results vs. base

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: windows-amd64
- commit hash: dc660a2
- commit date: 2025-08-22
- overall geometric mean: 1.002x slower
- HPT reliability: 99.62%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250822-pythonperf1-amd64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| html5lib       | 38.5 ms                                                                    | 38.1 ms: 1.01x faster                                                              |
| sphinx         | 620 ms                                                                     | 629 ms: 1.01x slower                                                               |
| Geometric mean | (ref)                                                                      | 1.00x slower                                                                       |

Benchmark hidden because not significant (2): 2to3, docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20250822-pythonperf1-amd64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|------------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_io          | 378 ms                                                                     | 385 ms: 1.02x slower                                                               |
| async_tree_memoization | 199 ms                                                                     | 203 ms: 1.02x slower                                                               |
| async_tree_none_tg     | 165 ms                                                                     | 168 ms: 1.02x slower                                                               |
| asyncio_websockets     | 158 ms                                                                     | 167 ms: 1.05x slower                                                               |
| Geometric mean         | (ref)                                                                      | 1.01x slower                                                                       |

Benchmark hidden because not significant (7): async_generators, async_tree_none, coroutines, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250822-pythonperf1-amd64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody          | 53.6 ms                                                                    | 42.6 ms: 1.26x faster                                                              |
| pidigits       | 144 ms                                                                     | 145 ms: 1.01x slower                                                               |
| float          | 42.6 ms                                                                    | 43.6 ms: 1.02x slower                                                              |
| Geometric mean | (ref)                                                                      | 1.07x faster                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250822-pythonperf1-amd64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_effbot   | 1.56 ms                                                                    | 1.54 ms: 1.02x faster                                                              |
| regex_dna      | 118 ms                                                                     | 119 ms: 1.00x slower                                                               |
| regex_compile  | 77.0 ms                                                                    | 78.3 ms: 1.02x slower                                                              |
| regex_v8       | 13.7 ms                                                                    | 14.0 ms: 1.02x slower                                                              |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250822-pythonperf1-amd64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| json_loads           | 14.2 us                                                                    | 14.0 us: 1.02x faster                                                              |
| json_dumps           | 5.42 ms                                                                    | 5.32 ms: 1.02x faster                                                              |
| xml_etree_parse      | 84.2 ms                                                                    | 83.1 ms: 1.01x faster                                                              |
| xml_etree_generate   | 49.2 ms                                                                    | 48.8 ms: 1.01x faster                                                              |
| tomli_loads          | 1.08 sec                                                                   | 1.08 sec: 1.00x faster                                                             |
| unpickle_pure_python | 104 us                                                                     | 105 us: 1.02x slower                                                               |
| pickle_pure_python   | 198 us                                                                     | 203 us: 1.02x slower                                                               |
| Geometric mean       | (ref)                                                                      | 1.00x faster                                                                       |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_process

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250822-pythonperf1-amd64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|-----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| django_template | 23.8 ms                                                                    | 24.1 ms: 1.01x slower                                                              |
| mako            | 5.36 ms                                                                    | 5.53 ms: 1.03x slower                                                              |
| genshi_xml      | 34.1 ms                                                                    | 35.2 ms: 1.03x slower                                                              |
| Geometric mean  | (ref)                                                                      | 1.02x slower                                                                       |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20250822-pythonperf1-amd64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|--------------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody                    | 53.6 ms                                                                    | 42.6 ms: 1.26x faster                                                              |
| json                     | 3.03 ms                                                                    | 2.82 ms: 1.07x faster                                                              |
| scimark_fft              | 150 ms                                                                     | 142 ms: 1.06x faster                                                               |
| crypto_pyaes             | 44.7 ms                                                                    | 43.5 ms: 1.03x faster                                                              |
| deepcopy_reduce          | 1.85 us                                                                    | 1.81 us: 1.02x faster                                                              |
| json_loads               | 14.2 us                                                                    | 14.0 us: 1.02x faster                                                              |
| pyflate                  | 263 ms                                                                     | 258 ms: 1.02x faster                                                               |
| json_dumps               | 5.42 ms                                                                    | 5.32 ms: 1.02x faster                                                              |
| thrift                   | 486 us                                                                     | 478 us: 1.02x faster                                                               |
| pprint_safe_repr         | 419 ms                                                                     | 412 ms: 1.02x faster                                                               |
| regex_effbot             | 1.56 ms                                                                    | 1.54 ms: 1.02x faster                                                              |
| xml_etree_parse          | 84.2 ms                                                                    | 83.1 ms: 1.01x faster                                                              |
| deepcopy                 | 172 us                                                                     | 169 us: 1.01x faster                                                               |
| scimark_sparse_mat_mult  | 2.31 ms                                                                    | 2.28 ms: 1.01x faster                                                              |
| html5lib                 | 38.5 ms                                                                    | 38.1 ms: 1.01x faster                                                              |
| sympy_expand             | 289 ms                                                                     | 287 ms: 1.01x faster                                                               |
| xml_etree_generate       | 49.2 ms                                                                    | 48.8 ms: 1.01x faster                                                              |
| shortest_path            | 350 ms                                                                     | 348 ms: 1.01x faster                                                               |
| tomli_loads              | 1.08 sec                                                                   | 1.08 sec: 1.00x faster                                                             |
| sympy_str                | 167 ms                                                                     | 167 ms: 1.00x slower                                                               |
| regex_dna                | 118 ms                                                                     | 119 ms: 1.00x slower                                                               |
| pprint_pformat           | 847 ms                                                                     | 851 ms: 1.00x slower                                                               |
| pidigits                 | 144 ms                                                                     | 145 ms: 1.01x slower                                                               |
| meteor_contest           | 69.3 ms                                                                    | 69.8 ms: 1.01x slower                                                              |
| connected_components     | 315 ms                                                                     | 317 ms: 1.01x slower                                                               |
| chaos                    | 39.9 ms                                                                    | 40.3 ms: 1.01x slower                                                              |
| comprehensions           | 10.3 us                                                                    | 10.4 us: 1.01x slower                                                              |
| sympy_integrate          | 12.3 ms                                                                    | 12.5 ms: 1.01x slower                                                              |
| logging_format           | 6.41 us                                                                    | 6.48 us: 1.01x slower                                                              |
| django_template          | 23.8 ms                                                                    | 24.1 ms: 1.01x slower                                                              |
| richards_super           | 30.3 ms                                                                    | 30.7 ms: 1.01x slower                                                              |
| sphinx                   | 620 ms                                                                     | 629 ms: 1.01x slower                                                               |
| richards                 | 26.6 ms                                                                    | 27.0 ms: 1.01x slower                                                              |
| unpickle_pure_python     | 104 us                                                                     | 105 us: 1.02x slower                                                               |
| regex_compile            | 77.0 ms                                                                    | 78.3 ms: 1.02x slower                                                              |
| logging_simple           | 5.92 us                                                                    | 6.02 us: 1.02x slower                                                              |
| async_tree_io            | 378 ms                                                                     | 385 ms: 1.02x slower                                                               |
| subparsers               | 29.8 ms                                                                    | 30.4 ms: 1.02x slower                                                              |
| coverage                 | 48.9 ms                                                                    | 49.8 ms: 1.02x slower                                                              |
| async_tree_memoization   | 199 ms                                                                     | 203 ms: 1.02x slower                                                               |
| async_tree_none_tg       | 165 ms                                                                     | 168 ms: 1.02x slower                                                               |
| mdp                      | 775 ms                                                                     | 793 ms: 1.02x slower                                                               |
| pickle_pure_python       | 198 us                                                                     | 203 us: 1.02x slower                                                               |
| regex_v8                 | 13.7 ms                                                                    | 14.0 ms: 1.02x slower                                                              |
| float                    | 42.6 ms                                                                    | 43.6 ms: 1.02x slower                                                              |
| scimark_sor              | 75.5 ms                                                                    | 77.3 ms: 1.02x slower                                                              |
| logging_silent           | 53.7 ns                                                                    | 55.1 ns: 1.03x slower                                                              |
| fannkuch                 | 204 ms                                                                     | 209 ms: 1.03x slower                                                               |
| raytrace                 | 168 ms                                                                     | 173 ms: 1.03x slower                                                               |
| generators               | 19.0 ms                                                                    | 19.6 ms: 1.03x slower                                                              |
| go                       | 74.8 ms                                                                    | 77.1 ms: 1.03x slower                                                              |
| mako                     | 5.36 ms                                                                    | 5.53 ms: 1.03x slower                                                              |
| genshi_xml               | 34.1 ms                                                                    | 35.2 ms: 1.03x slower                                                              |
| scimark_monte_carlo      | 39.7 ms                                                                    | 41.0 ms: 1.03x slower                                                              |
| typing_runtime_protocols | 98.7 us                                                                    | 103 us: 1.04x slower                                                               |
| deltablue                | 2.18 ms                                                                    | 2.26 ms: 1.04x slower                                                              |
| asyncio_websockets       | 158 ms                                                                     | 167 ms: 1.05x slower                                                               |
| Geometric mean           | (ref)                                                                      | 1.00x slower                                                                       |

Benchmark hidden because not significant (35): k_core, async_generators, pycparser, async_tree_none, create_gc_cycles, nqueens, xml_etree_iterparse, spectral_norm, telco, sqlglot_v2_transpile, pylint, deepcopy_memo, gc_traversal, pathlib, sqlglot_v2_optimize, sqlglot_v2_parse, coroutines, bpe_tokeniser, python_startup, docutils, sqlglot_v2_normalize, hexiom, async_tree_cpu_io_mixed_tg, sympy_sum, async_tree_cpu_io_mixed, async_tree_io_tg, genshi_text, 2to3, sqlite_synth, async_tree_memoization_tg, many_optionals, dulwich_log, scimark_lu, xml_etree_process, python_startup_no_site

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 99.62% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown