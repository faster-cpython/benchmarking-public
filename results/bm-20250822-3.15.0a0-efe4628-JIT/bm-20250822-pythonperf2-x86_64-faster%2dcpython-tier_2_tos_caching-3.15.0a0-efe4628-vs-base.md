# Results vs. base

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-x86_64
- commit hash: efe4628
- commit date: 2025-08-22
- overall geometric mean: 1.007x faster
- HPT reliability: 98.48%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250821-pythonperf2-x86_64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94 | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| 2to3           | 288 ms                                                                      | 287 ms: 1.01x faster                                                                |
| docutils       | 2.93 sec                                                                    | 2.91 sec: 1.01x faster                                                              |
| html5lib       | 67.8 ms                                                                     | 67.4 ms: 1.01x faster                                                               |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                        |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20250821-pythonperf2-x86_64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94 | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| coroutines       | 22.4 ms                                                                     | 22.5 ms: 1.00x slower                                                               |
| async_generators | 444 ms                                                                      | 451 ms: 1.02x slower                                                                |
| Geometric mean   | (ref)                                                                       | 1.00x slower                                                                        |

Benchmark hidden because not significant (9): asyncio_websockets, async_tree_none, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250821-pythonperf2-x86_64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94 | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| nbody          | 105 ms                                                                      | 86.9 ms: 1.21x faster                                                               |
| float          | 64.5 ms                                                                     | 59.7 ms: 1.08x faster                                                               |
| pidigits       | 255 ms                                                                      | 255 ms: 1.00x faster                                                                |
| Geometric mean | (ref)                                                                       | 1.09x faster                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250821-pythonperf2-x86_64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94 | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_effbot   | 3.79 ms                                                                     | 3.68 ms: 1.03x faster                                                               |
| regex_v8       | 23.4 ms                                                                     | 23.2 ms: 1.01x faster                                                               |
| regex_compile  | 132 ms                                                                      | 133 ms: 1.00x slower                                                                |
| regex_dna      | 227 ms                                                                      | 231 ms: 1.02x slower                                                                |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250821-pythonperf2-x86_64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94 | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| tomli_loads          | 1.94 sec                                                                    | 1.90 sec: 1.02x faster                                                              |
| pickle_pure_python   | 334 us                                                                      | 329 us: 1.01x faster                                                                |
| unpickle_pure_python | 194 us                                                                      | 192 us: 1.01x faster                                                                |
| json_loads           | 25.2 us                                                                     | 25.4 us: 1.01x slower                                                               |
| xml_etree_iterparse  | 98.5 ms                                                                     | 99.3 ms: 1.01x slower                                                               |
| json_dumps           | 10.2 ms                                                                     | 10.2 ms: 1.01x slower                                                               |
| Geometric mean       | (ref)                                                                       | 1.00x faster                                                                        |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250821-pythonperf2-x86_64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94 | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup_no_site | 8.83 ms                                                                     | 8.86 ms: 1.00x slower                                                               |
| python_startup         | 15.4 ms                                                                     | 15.4 ms: 1.00x slower                                                               |
| Geometric mean         | (ref)                                                                       | 1.00x slower                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250821-pythonperf2-x86_64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94 | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|-----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| genshi_text     | 23.2 ms                                                                     | 22.6 ms: 1.03x faster                                                               |
| django_template | 35.6 ms                                                                     | 35.1 ms: 1.01x faster                                                               |
| Geometric mean  | (ref)                                                                       | 1.01x faster                                                                        |

Benchmark hidden because not significant (2): genshi_xml, mako

All benchmarks:
===============

| Benchmark                | bm-20250821-pythonperf2-x86_64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94 | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|--------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| nbody                    | 105 ms                                                                      | 86.9 ms: 1.21x faster                                                               |
| coverage                 | 85.7 ms                                                                     | 79.0 ms: 1.09x faster                                                               |
| float                    | 64.5 ms                                                                     | 59.7 ms: 1.08x faster                                                               |
| pycparser                | 1.24 sec                                                                    | 1.18 sec: 1.05x faster                                                              |
| pprint_safe_repr         | 757 ms                                                                      | 731 ms: 1.04x faster                                                                |
| regex_effbot             | 3.79 ms                                                                     | 3.68 ms: 1.03x faster                                                               |
| genshi_text              | 23.2 ms                                                                     | 22.6 ms: 1.03x faster                                                               |
| deepcopy_reduce          | 3.08 us                                                                     | 3.01 us: 1.02x faster                                                               |
| tomli_loads              | 1.94 sec                                                                    | 1.90 sec: 1.02x faster                                                              |
| generators               | 29.8 ms                                                                     | 29.2 ms: 1.02x faster                                                               |
| hexiom                   | 6.12 ms                                                                     | 5.99 ms: 1.02x faster                                                               |
| go                       | 125 ms                                                                      | 122 ms: 1.02x faster                                                                |
| deepcopy_memo            | 28.4 us                                                                     | 27.9 us: 1.02x faster                                                               |
| crypto_pyaes             | 77.4 ms                                                                     | 75.8 ms: 1.02x faster                                                               |
| sqlglot_v2_parse         | 1.32 ms                                                                     | 1.30 ms: 1.02x faster                                                               |
| chaos                    | 60.3 ms                                                                     | 59.2 ms: 1.02x faster                                                               |
| richards                 | 33.9 ms                                                                     | 33.4 ms: 1.02x faster                                                               |
| connected_components     | 408 ms                                                                      | 402 ms: 1.01x faster                                                                |
| sqlglot_v2_transpile     | 1.71 ms                                                                     | 1.68 ms: 1.01x faster                                                               |
| telco                    | 160 ms                                                                      | 158 ms: 1.01x faster                                                                |
| pprint_pformat           | 1.50 sec                                                                    | 1.48 sec: 1.01x faster                                                              |
| django_template          | 35.6 ms                                                                     | 35.1 ms: 1.01x faster                                                               |
| pickle_pure_python       | 334 us                                                                      | 329 us: 1.01x faster                                                                |
| shortest_path            | 442 ms                                                                      | 437 ms: 1.01x faster                                                                |
| deepcopy                 | 284 us                                                                      | 281 us: 1.01x faster                                                                |
| fannkuch                 | 364 ms                                                                      | 360 ms: 1.01x faster                                                                |
| unpickle_pure_python     | 194 us                                                                      | 192 us: 1.01x faster                                                                |
| scimark_sparse_mat_mult  | 5.05 ms                                                                     | 5.00 ms: 1.01x faster                                                               |
| spectral_norm            | 80.3 ms                                                                     | 79.4 ms: 1.01x faster                                                               |
| bpe_tokeniser            | 4.56 sec                                                                    | 4.52 sec: 1.01x faster                                                              |
| docutils                 | 2.93 sec                                                                    | 2.91 sec: 1.01x faster                                                              |
| mdp                      | 1.29 sec                                                                    | 1.28 sec: 1.01x faster                                                              |
| html5lib                 | 67.8 ms                                                                     | 67.4 ms: 1.01x faster                                                               |
| regex_v8                 | 23.4 ms                                                                     | 23.2 ms: 1.01x faster                                                               |
| 2to3                     | 288 ms                                                                      | 287 ms: 1.01x faster                                                                |
| sympy_expand             | 502 ms                                                                      | 499 ms: 1.01x faster                                                                |
| sqlglot_v2_optimize      | 58.0 ms                                                                     | 57.7 ms: 1.01x faster                                                               |
| dulwich_log              | 59.3 ms                                                                     | 59.0 ms: 1.01x faster                                                               |
| sqlite_synth             | 2.83 us                                                                     | 2.81 us: 1.00x faster                                                               |
| scimark_fft              | 302 ms                                                                      | 301 ms: 1.00x faster                                                                |
| sympy_str                | 291 ms                                                                      | 290 ms: 1.00x faster                                                                |
| sympy_integrate          | 22.4 ms                                                                     | 22.4 ms: 1.00x faster                                                               |
| pidigits                 | 255 ms                                                                      | 255 ms: 1.00x faster                                                                |
| gc_traversal             | 6.70 ms                                                                     | 6.72 ms: 1.00x slower                                                               |
| python_startup_no_site   | 8.83 ms                                                                     | 8.86 ms: 1.00x slower                                                               |
| python_startup           | 15.4 ms                                                                     | 15.4 ms: 1.00x slower                                                               |
| coroutines               | 22.4 ms                                                                     | 22.5 ms: 1.00x slower                                                               |
| comprehensions           | 17.3 us                                                                     | 17.4 us: 1.00x slower                                                               |
| regex_compile            | 132 ms                                                                      | 133 ms: 1.00x slower                                                                |
| logging_silent           | 91.7 ns                                                                     | 92.2 ns: 1.01x slower                                                               |
| json_loads               | 25.2 us                                                                     | 25.4 us: 1.01x slower                                                               |
| many_optionals           | 1.24 ms                                                                     | 1.24 ms: 1.01x slower                                                               |
| deltablue                | 2.86 ms                                                                     | 2.88 ms: 1.01x slower                                                               |
| pathlib                  | 16.7 ms                                                                     | 16.8 ms: 1.01x slower                                                               |
| xml_etree_iterparse      | 98.5 ms                                                                     | 99.3 ms: 1.01x slower                                                               |
| subparsers               | 43.0 ms                                                                     | 43.4 ms: 1.01x slower                                                               |
| scimark_lu               | 95.0 ms                                                                     | 95.8 ms: 1.01x slower                                                               |
| json_dumps               | 10.2 ms                                                                     | 10.2 ms: 1.01x slower                                                               |
| nqueens                  | 92.0 ms                                                                     | 92.9 ms: 1.01x slower                                                               |
| meteor_contest           | 120 ms                                                                      | 121 ms: 1.01x slower                                                                |
| logging_format           | 6.47 us                                                                     | 6.54 us: 1.01x slower                                                               |
| async_generators         | 444 ms                                                                      | 451 ms: 1.02x slower                                                                |
| typing_runtime_protocols | 170 us                                                                      | 173 us: 1.02x slower                                                                |
| regex_dna                | 227 ms                                                                      | 231 ms: 1.02x slower                                                                |
| scimark_monte_carlo      | 62.7 ms                                                                     | 64.0 ms: 1.02x slower                                                               |
| pyflate                  | 400 ms                                                                      | 408 ms: 1.02x slower                                                                |
| scimark_sor              | 101 ms                                                                      | 104 ms: 1.03x slower                                                                |
| Geometric mean           | (ref)                                                                       | 1.01x faster                                                                        |

Benchmark hidden because not significant (26): json, sphinx, richards_super, asyncio_websockets, genshi_xml, sympy_sum, async_tree_none, xml_etree_parse, raytrace, pylint, djangocms, sqlglot_v2_normalize, async_tree_memoization, k_core, mako, xml_etree_process, async_tree_cpu_io_mixed, logging_simple, thrift, xml_etree_generate, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_io, async_tree_io_tg, create_gc_cycles

- Geometric mean (including insignificant results): 1.007x faster

# HPT report

- Reliability score: 98.48% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x