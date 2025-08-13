# Results vs. base

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-x86_64
- commit hash: 6a85f95
- commit date: 2025-08-13
- overall geometric mean: 1.000x slower
- HPT reliability: 90.42%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250809-pythonperf2-x86_64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d | bm-20250813-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                                      | 287 ms: 1.01x slower                                                                |
| docutils       | 2.90 sec                                                                    | 2.92 sec: 1.01x slower                                                              |
| html5lib       | 66.9 ms                                                                     | 68.5 ms: 1.02x slower                                                               |
| sphinx         | 1.08 sec                                                                    | 1.09 sec: 1.01x slower                                                              |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20250809-pythonperf2-x86_64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d | bm-20250813-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_memoization | 330 ms                                                                      | 328 ms: 1.01x faster                                                                |
| coroutines             | 22.5 ms                                                                     | 22.5 ms: 1.00x faster                                                               |
| asyncio_websockets     | 381 ms                                                                      | 386 ms: 1.01x slower                                                                |
| Geometric mean         | (ref)                                                                       | 1.00x slower                                                                        |

Benchmark hidden because not significant (8): async_tree_memoization_tg, async_tree_io_tg, async_generators, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_io, async_tree_none_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250809-pythonperf2-x86_64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d | bm-20250813-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| nbody          | 99.6 ms                                                                     | 86.6 ms: 1.15x faster                                                               |
| float          | 64.2 ms                                                                     | 61.7 ms: 1.04x faster                                                               |
| Geometric mean | (ref)                                                                       | 1.06x faster                                                                        |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250809-pythonperf2-x86_64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d | bm-20250813-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_v8       | 24.2 ms                                                                     | 23.3 ms: 1.04x faster                                                               |
| regex_dna      | 226 ms                                                                      | 223 ms: 1.01x faster                                                                |
| regex_compile  | 132 ms                                                                      | 133 ms: 1.01x slower                                                                |
| regex_effbot   | 3.60 ms                                                                     | 3.71 ms: 1.03x slower                                                               |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250809-pythonperf2-x86_64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d | bm-20250813-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|----------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| xml_etree_process    | 55.8 ms                                                                     | 55.2 ms: 1.01x faster                                                               |
| tomli_loads          | 1.90 sec                                                                    | 1.91 sec: 1.00x slower                                                              |
| unpickle_pure_python | 193 us                                                                      | 195 us: 1.01x slower                                                                |
| json_dumps           | 10.1 ms                                                                     | 10.3 ms: 1.02x slower                                                               |
| xml_etree_iterparse  | 97.9 ms                                                                     | 99.5 ms: 1.02x slower                                                               |
| pickle_pure_python   | 327 us                                                                      | 335 us: 1.02x slower                                                                |
| json_loads           | 25.2 us                                                                     | 25.9 us: 1.03x slower                                                               |
| xml_etree_parse      | 139 ms                                                                      | 144 ms: 1.04x slower                                                                |
| Geometric mean       | (ref)                                                                       | 1.01x slower                                                                        |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250809-pythonperf2-x86_64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d | bm-20250813-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup_no_site | 8.81 ms                                                                     | 8.86 ms: 1.01x slower                                                               |
| python_startup         | 15.3 ms                                                                     | 15.5 ms: 1.01x slower                                                               |
| Geometric mean         | (ref)                                                                       | 1.01x slower                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250809-pythonperf2-x86_64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d | bm-20250813-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|-----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| genshi_xml      | 56.9 ms                                                                     | 54.5 ms: 1.04x faster                                                               |
| genshi_text     | 23.3 ms                                                                     | 23.1 ms: 1.01x faster                                                               |
| django_template | 34.7 ms                                                                     | 35.3 ms: 1.02x slower                                                               |
| Geometric mean  | (ref)                                                                       | 1.01x faster                                                                        |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20250809-pythonperf2-x86_64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d | bm-20250813-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|--------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| nbody                    | 99.6 ms                                                                     | 86.6 ms: 1.15x faster                                                               |
| gc_traversal             | 6.79 ms                                                                     | 6.32 ms: 1.07x faster                                                               |
| genshi_xml               | 56.9 ms                                                                     | 54.5 ms: 1.04x faster                                                               |
| float                    | 64.2 ms                                                                     | 61.7 ms: 1.04x faster                                                               |
| regex_v8                 | 24.2 ms                                                                     | 23.3 ms: 1.04x faster                                                               |
| pyflate                  | 406 ms                                                                      | 393 ms: 1.03x faster                                                                |
| go                       | 126 ms                                                                      | 122 ms: 1.03x faster                                                                |
| richards_super           | 40.2 ms                                                                     | 39.1 ms: 1.03x faster                                                               |
| fannkuch                 | 371 ms                                                                      | 362 ms: 1.02x faster                                                                |
| pprint_pformat           | 1.51 sec                                                                    | 1.48 sec: 1.02x faster                                                              |
| richards                 | 34.2 ms                                                                     | 33.6 ms: 1.02x faster                                                               |
| hexiom                   | 6.10 ms                                                                     | 6.00 ms: 1.02x faster                                                               |
| pprint_safe_repr         | 749 ms                                                                      | 739 ms: 1.01x faster                                                                |
| regex_dna                | 226 ms                                                                      | 223 ms: 1.01x faster                                                                |
| meteor_contest           | 122 ms                                                                      | 120 ms: 1.01x faster                                                                |
| logging_simple           | 6.09 us                                                                     | 6.02 us: 1.01x faster                                                               |
| xml_etree_process        | 55.8 ms                                                                     | 55.2 ms: 1.01x faster                                                               |
| spectral_norm            | 78.8 ms                                                                     | 78.0 ms: 1.01x faster                                                               |
| logging_format           | 6.70 us                                                                     | 6.64 us: 1.01x faster                                                               |
| deltablue                | 2.89 ms                                                                     | 2.86 ms: 1.01x faster                                                               |
| create_gc_cycles         | 2.92 ms                                                                     | 2.90 ms: 1.01x faster                                                               |
| raytrace                 | 282 ms                                                                      | 279 ms: 1.01x faster                                                                |
| async_tree_memoization   | 330 ms                                                                      | 328 ms: 1.01x faster                                                                |
| chaos                    | 58.9 ms                                                                     | 58.5 ms: 1.01x faster                                                               |
| genshi_text              | 23.3 ms                                                                     | 23.1 ms: 1.01x faster                                                               |
| deepcopy_memo            | 27.7 us                                                                     | 27.6 us: 1.00x faster                                                               |
| shortest_path            | 444 ms                                                                      | 443 ms: 1.00x faster                                                                |
| crypto_pyaes             | 76.9 ms                                                                     | 76.7 ms: 1.00x faster                                                               |
| coroutines               | 22.5 ms                                                                     | 22.5 ms: 1.00x faster                                                               |
| sqlglot_v2_optimize      | 57.9 ms                                                                     | 58.0 ms: 1.00x slower                                                               |
| sqlite_synth             | 2.79 us                                                                     | 2.80 us: 1.00x slower                                                               |
| tomli_loads              | 1.90 sec                                                                    | 1.91 sec: 1.00x slower                                                              |
| sympy_expand             | 497 ms                                                                      | 499 ms: 1.00x slower                                                                |
| scimark_sor              | 101 ms                                                                      | 102 ms: 1.01x slower                                                                |
| python_startup_no_site   | 8.81 ms                                                                     | 8.86 ms: 1.01x slower                                                               |
| bpe_tokeniser            | 4.52 sec                                                                    | 4.54 sec: 1.01x slower                                                              |
| regex_compile            | 132 ms                                                                      | 133 ms: 1.01x slower                                                                |
| python_startup           | 15.3 ms                                                                     | 15.5 ms: 1.01x slower                                                               |
| deepcopy_reduce          | 2.95 us                                                                     | 2.98 us: 1.01x slower                                                               |
| scimark_sparse_mat_mult  | 4.91 ms                                                                     | 4.95 ms: 1.01x slower                                                               |
| typing_runtime_protocols | 170 us                                                                      | 172 us: 1.01x slower                                                                |
| sympy_sum                | 151 ms                                                                      | 152 ms: 1.01x slower                                                                |
| docutils                 | 2.90 sec                                                                    | 2.92 sec: 1.01x slower                                                              |
| sympy_str                | 289 ms                                                                      | 291 ms: 1.01x slower                                                                |
| mdp                      | 1.28 sec                                                                    | 1.29 sec: 1.01x slower                                                              |
| pathlib                  | 16.7 ms                                                                     | 16.9 ms: 1.01x slower                                                               |
| 2to3                     | 285 ms                                                                      | 287 ms: 1.01x slower                                                                |
| unpickle_pure_python     | 193 us                                                                      | 195 us: 1.01x slower                                                                |
| connected_components     | 403 ms                                                                      | 407 ms: 1.01x slower                                                                |
| comprehensions           | 17.3 us                                                                     | 17.5 us: 1.01x slower                                                               |
| sphinx                   | 1.08 sec                                                                    | 1.09 sec: 1.01x slower                                                              |
| asyncio_websockets       | 381 ms                                                                      | 386 ms: 1.01x slower                                                                |
| sqlglot_v2_normalize     | 115 ms                                                                      | 116 ms: 1.01x slower                                                                |
| nqueens                  | 92.3 ms                                                                     | 93.4 ms: 1.01x slower                                                               |
| sympy_integrate          | 22.2 ms                                                                     | 22.5 ms: 1.01x slower                                                               |
| deepcopy                 | 272 us                                                                      | 276 us: 1.01x slower                                                                |
| telco                    | 158 ms                                                                      | 160 ms: 1.02x slower                                                                |
| json_dumps               | 10.1 ms                                                                     | 10.3 ms: 1.02x slower                                                               |
| generators               | 29.7 ms                                                                     | 30.2 ms: 1.02x slower                                                               |
| xml_etree_iterparse      | 97.9 ms                                                                     | 99.5 ms: 1.02x slower                                                               |
| django_template          | 34.7 ms                                                                     | 35.3 ms: 1.02x slower                                                               |
| scimark_monte_carlo      | 62.1 ms                                                                     | 63.3 ms: 1.02x slower                                                               |
| scimark_lu               | 93.9 ms                                                                     | 95.8 ms: 1.02x slower                                                               |
| json                     | 5.43 ms                                                                     | 5.54 ms: 1.02x slower                                                               |
| many_optionals           | 1.21 ms                                                                     | 1.23 ms: 1.02x slower                                                               |
| pickle_pure_python       | 327 us                                                                      | 335 us: 1.02x slower                                                                |
| html5lib                 | 66.9 ms                                                                     | 68.5 ms: 1.02x slower                                                               |
| subparsers               | 42.2 ms                                                                     | 43.2 ms: 1.02x slower                                                               |
| json_loads               | 25.2 us                                                                     | 25.9 us: 1.03x slower                                                               |
| regex_effbot             | 3.60 ms                                                                     | 3.71 ms: 1.03x slower                                                               |
| pycparser                | 1.21 sec                                                                    | 1.24 sec: 1.03x slower                                                              |
| xml_etree_parse          | 139 ms                                                                      | 144 ms: 1.04x slower                                                                |
| coverage                 | 77.9 ms                                                                     | 83.8 ms: 1.08x slower                                                               |
| Geometric mean           | (ref)                                                                       | 1.00x slower                                                                        |

Benchmark hidden because not significant (20): async_tree_memoization_tg, k_core, thrift, async_tree_io_tg, async_generators, async_tree_cpu_io_mixed_tg, djangocms, pidigits, sqlglot_v2_parse, xml_etree_generate, async_tree_cpu_io_mixed, mako, async_tree_io, sqlglot_v2_transpile, dulwich_log, async_tree_none_tg, async_tree_none, scimark_fft, logging_silent, pylint

- Geometric mean (including insignificant results): 1.000x slower

# HPT report

- Reliability score: 90.42% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x