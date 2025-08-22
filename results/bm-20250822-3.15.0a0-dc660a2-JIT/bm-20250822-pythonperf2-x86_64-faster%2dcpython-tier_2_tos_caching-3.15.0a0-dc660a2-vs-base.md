# Results vs. base

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-x86_64
- commit hash: dc660a2
- commit date: 2025-08-22
- overall geometric mean: 1.008x faster
- HPT reliability: 99.94%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250822-pythonperf2-x86_64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| 2to3           | 287 ms                                                                      | 286 ms: 1.00x faster                                                                |
| docutils       | 2.93 sec                                                                    | 2.92 sec: 1.00x faster                                                              |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                                        |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20250822-pythonperf2-x86_64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|---------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_generators          | 434 ms                                                                      | 436 ms: 1.00x slower                                                                |
| async_tree_memoization_tg | 328 ms                                                                      | 330 ms: 1.01x slower                                                                |
| async_tree_none           | 270 ms                                                                      | 272 ms: 1.01x slower                                                                |
| coroutines                | 22.3 ms                                                                     | 22.5 ms: 1.01x slower                                                               |
| Geometric mean            | (ref)                                                                       | 1.00x slower                                                                        |

Benchmark hidden because not significant (7): async_tree_io, async_tree_io_tg, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250822-pythonperf2-x86_64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| nbody          | 105 ms                                                                      | 87.5 ms: 1.20x faster                                                               |
| float          | 65.0 ms                                                                     | 59.8 ms: 1.09x faster                                                               |
| pidigits       | 255 ms                                                                      | 255 ms: 1.00x faster                                                                |
| Geometric mean | (ref)                                                                       | 1.09x faster                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250822-pythonperf2-x86_64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_effbot   | 3.72 ms                                                                     | 3.59 ms: 1.04x faster                                                               |
| regex_compile  | 134 ms                                                                      | 132 ms: 1.01x faster                                                                |
| regex_dna      | 223 ms                                                                      | 227 ms: 1.02x slower                                                                |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                        |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250822-pythonperf2-x86_64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| tomli_loads          | 1.96 sec                                                                    | 1.89 sec: 1.04x faster                                                              |
| unpickle_pure_python | 195 us                                                                      | 191 us: 1.02x faster                                                                |
| xml_etree_parse      | 138 ms                                                                      | 136 ms: 1.01x faster                                                                |
| xml_etree_iterparse  | 96.5 ms                                                                     | 95.6 ms: 1.01x faster                                                               |
| xml_etree_generate   | 80.3 ms                                                                     | 79.8 ms: 1.01x faster                                                               |
| pickle_pure_python   | 333 us                                                                      | 331 us: 1.01x faster                                                                |
| xml_etree_process    | 55.2 ms                                                                     | 55.0 ms: 1.00x faster                                                               |
| json_loads           | 25.2 us                                                                     | 25.7 us: 1.02x slower                                                               |
| Geometric mean       | (ref)                                                                       | 1.01x faster                                                                        |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250822-pythonperf2-x86_64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup_no_site | 8.81 ms                                                                     | 8.80 ms: 1.00x faster                                                               |
| Geometric mean         | (ref)                                                                       | 1.00x faster                                                                        |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250822-pythonperf2-x86_64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|-----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| django_template | 35.6 ms                                                                     | 35.3 ms: 1.01x faster                                                               |
| genshi_xml      | 55.5 ms                                                                     | 55.2 ms: 1.01x faster                                                               |
| genshi_text     | 23.1 ms                                                                     | 23.5 ms: 1.02x slower                                                               |
| mako            | 9.85 ms                                                                     | 10.1 ms: 1.03x slower                                                               |
| Geometric mean  | (ref)                                                                       | 1.01x slower                                                                        |

All benchmarks:
===============

| Benchmark                 | bm-20250822-pythonperf2-x86_64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|---------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| nbody                     | 105 ms                                                                      | 87.5 ms: 1.20x faster                                                               |
| float                     | 65.0 ms                                                                     | 59.8 ms: 1.09x faster                                                               |
| go                        | 127 ms                                                                      | 121 ms: 1.05x faster                                                                |
| richards_super            | 39.4 ms                                                                     | 37.8 ms: 1.04x faster                                                               |
| richards                  | 34.0 ms                                                                     | 32.7 ms: 1.04x faster                                                               |
| spectral_norm             | 79.6 ms                                                                     | 76.7 ms: 1.04x faster                                                               |
| regex_effbot              | 3.72 ms                                                                     | 3.59 ms: 1.04x faster                                                               |
| tomli_loads               | 1.96 sec                                                                    | 1.89 sec: 1.04x faster                                                              |
| hexiom                    | 6.13 ms                                                                     | 5.93 ms: 1.03x faster                                                               |
| pycparser                 | 1.23 sec                                                                    | 1.19 sec: 1.03x faster                                                              |
| crypto_pyaes              | 78.8 ms                                                                     | 76.3 ms: 1.03x faster                                                               |
| unpickle_pure_python      | 195 us                                                                      | 191 us: 1.02x faster                                                                |
| raytrace                  | 283 ms                                                                      | 277 ms: 1.02x faster                                                                |
| json                      | 5.53 ms                                                                     | 5.42 ms: 1.02x faster                                                               |
| fannkuch                  | 369 ms                                                                      | 362 ms: 1.02x faster                                                                |
| pprint_pformat            | 1.52 sec                                                                    | 1.49 sec: 1.02x faster                                                              |
| telco                     | 162 ms                                                                      | 159 ms: 1.02x faster                                                                |
| subparsers                | 42.7 ms                                                                     | 42.0 ms: 1.02x faster                                                               |
| logging_format            | 6.42 us                                                                     | 6.31 us: 1.02x faster                                                               |
| deltablue                 | 2.89 ms                                                                     | 2.85 ms: 1.02x faster                                                               |
| sqlglot_v2_parse          | 1.31 ms                                                                     | 1.30 ms: 1.01x faster                                                               |
| logging_simple            | 5.85 us                                                                     | 5.77 us: 1.01x faster                                                               |
| sqlglot_v2_transpile      | 1.70 ms                                                                     | 1.68 ms: 1.01x faster                                                               |
| sqlglot_v2_normalize      | 116 ms                                                                      | 114 ms: 1.01x faster                                                                |
| comprehensions            | 17.5 us                                                                     | 17.3 us: 1.01x faster                                                               |
| xml_etree_parse           | 138 ms                                                                      | 136 ms: 1.01x faster                                                                |
| many_optionals            | 1.25 ms                                                                     | 1.23 ms: 1.01x faster                                                               |
| sympy_sum                 | 153 ms                                                                      | 151 ms: 1.01x faster                                                                |
| dulwich_log               | 59.1 ms                                                                     | 58.5 ms: 1.01x faster                                                               |
| xml_etree_iterparse       | 96.5 ms                                                                     | 95.6 ms: 1.01x faster                                                               |
| regex_compile             | 134 ms                                                                      | 132 ms: 1.01x faster                                                                |
| django_template           | 35.6 ms                                                                     | 35.3 ms: 1.01x faster                                                               |
| logging_silent            | 93.1 ns                                                                     | 92.3 ns: 1.01x faster                                                               |
| meteor_contest            | 122 ms                                                                      | 121 ms: 1.01x faster                                                                |
| pathlib                   | 16.8 ms                                                                     | 16.6 ms: 1.01x faster                                                               |
| sqlglot_v2_optimize       | 58.4 ms                                                                     | 57.9 ms: 1.01x faster                                                               |
| bpe_tokeniser             | 4.56 sec                                                                    | 4.53 sec: 1.01x faster                                                              |
| xml_etree_generate        | 80.3 ms                                                                     | 79.8 ms: 1.01x faster                                                               |
| scimark_fft               | 302 ms                                                                      | 300 ms: 1.01x faster                                                                |
| pickle_pure_python        | 333 us                                                                      | 331 us: 1.01x faster                                                                |
| genshi_xml                | 55.5 ms                                                                     | 55.2 ms: 1.01x faster                                                               |
| shortest_path             | 444 ms                                                                      | 441 ms: 1.00x faster                                                                |
| docutils                  | 2.93 sec                                                                    | 2.92 sec: 1.00x faster                                                              |
| sympy_integrate           | 22.4 ms                                                                     | 22.3 ms: 1.00x faster                                                               |
| connected_components      | 409 ms                                                                      | 408 ms: 1.00x faster                                                                |
| 2to3                      | 287 ms                                                                      | 286 ms: 1.00x faster                                                                |
| xml_etree_process         | 55.2 ms                                                                     | 55.0 ms: 1.00x faster                                                               |
| python_startup_no_site    | 8.81 ms                                                                     | 8.80 ms: 1.00x faster                                                               |
| pidigits                  | 255 ms                                                                      | 255 ms: 1.00x faster                                                                |
| scimark_monte_carlo       | 62.4 ms                                                                     | 62.5 ms: 1.00x slower                                                               |
| sqlite_synth              | 2.80 us                                                                     | 2.81 us: 1.00x slower                                                               |
| mdp                       | 1.29 sec                                                                    | 1.29 sec: 1.00x slower                                                              |
| async_generators          | 434 ms                                                                      | 436 ms: 1.00x slower                                                                |
| sympy_expand              | 500 ms                                                                      | 503 ms: 1.01x slower                                                                |
| scimark_lu                | 94.4 ms                                                                     | 95.1 ms: 1.01x slower                                                               |
| chaos                     | 59.2 ms                                                                     | 59.7 ms: 1.01x slower                                                               |
| async_tree_memoization_tg | 328 ms                                                                      | 330 ms: 1.01x slower                                                                |
| async_tree_none           | 270 ms                                                                      | 272 ms: 1.01x slower                                                                |
| gc_traversal              | 6.49 ms                                                                     | 6.54 ms: 1.01x slower                                                               |
| pyflate                   | 402 ms                                                                      | 405 ms: 1.01x slower                                                                |
| coroutines                | 22.3 ms                                                                     | 22.5 ms: 1.01x slower                                                               |
| genshi_text               | 23.1 ms                                                                     | 23.5 ms: 1.02x slower                                                               |
| regex_dna                 | 223 ms                                                                      | 227 ms: 1.02x slower                                                                |
| coverage                  | 81.4 ms                                                                     | 83.0 ms: 1.02x slower                                                               |
| json_loads                | 25.2 us                                                                     | 25.7 us: 1.02x slower                                                               |
| mako                      | 9.85 ms                                                                     | 10.1 ms: 1.03x slower                                                               |
| generators                | 29.0 ms                                                                     | 31.0 ms: 1.07x slower                                                               |
| Geometric mean            | (ref)                                                                       | 1.01x faster                                                                        |

Benchmark hidden because not significant (26): scimark_sparse_mat_mult, regex_v8, sphinx, k_core, async_tree_io, create_gc_cycles, pprint_safe_repr, html5lib, typing_runtime_protocols, deepcopy_reduce, json_dumps, async_tree_io_tg, deepcopy, djangocms, pylint, deepcopy_memo, python_startup, async_tree_cpu_io_mixed, sympy_str, nqueens, asyncio_websockets, scimark_sor, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_none_tg, thrift

- Geometric mean (including insignificant results): 1.008x faster

# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x