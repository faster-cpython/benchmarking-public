# Results vs. base

- fork: JelleZijlstra
- ref: sunder_io
- machine: windows-amd64
- commit hash: dac50cc
- commit date: 2025-04-25
- overall geometric mean: 1.003x faster
- HPT reliability: 65.35%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250425-pythonperf1-amd64-python-17718b0503e5d1c98725-3.14.0a7+-17718b0 | bm-20250425-pythonperf1-amd64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| html5lib       | 38.0 ms                                                                     | 38.6 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                            |

Benchmark hidden because not significant (3): 2to3, docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20250425-pythonperf1-amd64-python-17718b0503e5d1c98725-3.14.0a7+-17718b0 | bm-20250425-pythonperf1-amd64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_generators | 224 ms                                                                      | 230 ms: 1.02x slower                                                    |
| Geometric mean   | (ref)                                                                       | 1.00x slower                                                            |

Benchmark hidden because not significant (10): async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_cpu_io_mixed, coroutines, async_tree_io_tg, async_tree_memoization_tg, async_tree_memoization, async_tree_none_tg, async_tree_io, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250425-pythonperf1-amd64-python-17718b0503e5d1c98725-3.14.0a7+-17718b0 | bm-20250425-pythonperf1-amd64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 149 ms                                                                      | 148 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                            |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250425-pythonperf1-amd64-python-17718b0503e5d1c98725-3.14.0a7+-17718b0 | bm-20250425-pythonperf1-amd64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 1.49 ms                                                                     | 1.43 ms: 1.04x faster                                                   |
| regex_dna      | 117 ms                                                                      | 117 ms: 1.01x faster                                                    |
| regex_compile  | 80.8 ms                                                                     | 81.5 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                            |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250425-pythonperf1-amd64-python-17718b0503e5d1c98725-3.14.0a7+-17718b0 | bm-20250425-pythonperf1-amd64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate   | 56.8 ms                                                                     | 55.6 ms: 1.02x faster                                                   |
| xml_etree_iterparse  | 65.1 ms                                                                     | 64.3 ms: 1.01x faster                                                   |
| unpickle_pure_python | 136 us                                                                      | 135 us: 1.00x faster                                                    |
| xml_etree_process    | 39.7 ms                                                                     | 40.0 ms: 1.01x slower                                                   |
| json_loads           | 15.0 us                                                                     | 15.4 us: 1.02x slower                                                   |
| Geometric mean       | (ref)                                                                       | 1.00x slower                                                            |

Benchmark hidden because not significant (4): pickle_pure_python, tomli_loads, json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250425-pythonperf1-amd64-python-17718b0503e5d1c98725-3.14.0a7+-17718b0 | bm-20250425-pythonperf1-amd64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 20.4 ms                                                                     | 19.4 ms: 1.05x faster                                                   |
| python_startup         | 26.4 ms                                                                     | 26.6 ms: 1.01x slower                                                   |
| Geometric mean         | (ref)                                                                       | 1.02x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250425-pythonperf1-amd64-python-17718b0503e5d1c98725-3.14.0a7+-17718b0 | bm-20250425-pythonperf1-amd64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text    | 15.4 ms                                                                     | 15.6 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                            |

Benchmark hidden because not significant (3): django_template, mako, genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20250425-pythonperf1-amd64-python-17718b0503e5d1c98725-3.14.0a7+-17718b0 | bm-20250425-pythonperf1-amd64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|--------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| scimark_lu               | 64.3 ms                                                                     | 59.1 ms: 1.09x faster                                                   |
| scimark_sparse_mat_mult  | 2.66 ms                                                                     | 2.49 ms: 1.07x faster                                                   |
| scimark_monte_carlo      | 42.4 ms                                                                     | 40.3 ms: 1.05x faster                                                   |
| python_startup_no_site   | 20.4 ms                                                                     | 19.4 ms: 1.05x faster                                                   |
| regex_effbot             | 1.49 ms                                                                     | 1.43 ms: 1.04x faster                                                   |
| scimark_fft              | 183 ms                                                                      | 176 ms: 1.04x faster                                                    |
| xml_etree_generate       | 56.8 ms                                                                     | 55.6 ms: 1.02x faster                                                   |
| logging_format           | 6.94 us                                                                     | 6.81 us: 1.02x faster                                                   |
| scimark_sor              | 79.5 ms                                                                     | 78.1 ms: 1.02x faster                                                   |
| pprint_safe_repr         | 506 ms                                                                      | 499 ms: 1.01x faster                                                    |
| xml_etree_iterparse      | 65.1 ms                                                                     | 64.3 ms: 1.01x faster                                                   |
| dulwich_log              | 43.1 ms                                                                     | 42.6 ms: 1.01x faster                                                   |
| bpe_tokeniser            | 2.87 sec                                                                    | 2.84 sec: 1.01x faster                                                  |
| typing_runtime_protocols | 108 us                                                                      | 107 us: 1.01x faster                                                    |
| sympy_sum                | 89.1 ms                                                                     | 88.3 ms: 1.01x faster                                                   |
| coverage                 | 51.9 ms                                                                     | 51.5 ms: 1.01x faster                                                   |
| sympy_expand             | 297 ms                                                                      | 295 ms: 1.01x faster                                                    |
| deepcopy_reduce          | 1.81 us                                                                     | 1.80 us: 1.01x faster                                                   |
| regex_dna                | 117 ms                                                                      | 117 ms: 1.01x faster                                                    |
| logging_simple           | 6.37 us                                                                     | 6.32 us: 1.01x faster                                                   |
| comprehensions           | 11.3 us                                                                     | 11.2 us: 1.01x faster                                                   |
| pidigits                 | 149 ms                                                                      | 148 ms: 1.01x faster                                                    |
| unpickle_pure_python     | 136 us                                                                      | 135 us: 1.00x faster                                                    |
| sympy_integrate          | 12.5 ms                                                                     | 12.6 ms: 1.01x slower                                                   |
| chaos                    | 38.4 ms                                                                     | 38.6 ms: 1.01x slower                                                   |
| telco                    | 4.57 ms                                                                     | 4.60 ms: 1.01x slower                                                   |
| python_startup           | 26.4 ms                                                                     | 26.6 ms: 1.01x slower                                                   |
| deltablue                | 2.17 ms                                                                     | 2.19 ms: 1.01x slower                                                   |
| nqueens                  | 61.1 ms                                                                     | 61.5 ms: 1.01x slower                                                   |
| xml_etree_process        | 39.7 ms                                                                     | 40.0 ms: 1.01x slower                                                   |
| sqlite_synth             | 1.58 us                                                                     | 1.59 us: 1.01x slower                                                   |
| go                       | 78.4 ms                                                                     | 79.0 ms: 1.01x slower                                                   |
| regex_compile            | 80.8 ms                                                                     | 81.5 ms: 1.01x slower                                                   |
| raytrace                 | 173 ms                                                                      | 175 ms: 1.01x slower                                                    |
| sqlglot_v2_transpile     | 1.01 ms                                                                     | 1.02 ms: 1.01x slower                                                   |
| genshi_text              | 15.4 ms                                                                     | 15.6 ms: 1.01x slower                                                   |
| crypto_pyaes             | 47.1 ms                                                                     | 47.7 ms: 1.01x slower                                                   |
| mdp                      | 780 ms                                                                      | 789 ms: 1.01x slower                                                    |
| deepcopy_memo            | 18.3 us                                                                     | 18.6 us: 1.01x slower                                                   |
| sqlglot_v2_optimize      | 33.8 ms                                                                     | 34.4 ms: 1.02x slower                                                   |
| deepcopy                 | 173 us                                                                      | 175 us: 1.02x slower                                                    |
| html5lib                 | 38.0 ms                                                                     | 38.6 ms: 1.02x slower                                                   |
| sqlglot_v2_normalize     | 69.7 ms                                                                     | 70.9 ms: 1.02x slower                                                   |
| spectral_norm            | 56.8 ms                                                                     | 57.8 ms: 1.02x slower                                                   |
| json_loads               | 15.0 us                                                                     | 15.4 us: 1.02x slower                                                   |
| async_generators         | 224 ms                                                                      | 230 ms: 1.02x slower                                                    |
| bench_thread_pool        | 864 us                                                                      | 894 us: 1.04x slower                                                    |
| Geometric mean           | (ref)                                                                       | 1.00x faster                                                            |

Benchmark hidden because not significant (46): sphinx, django_template, float, async_tree_cpu_io_mixed_tg, logging_silent, pyflate, async_tree_none, richards, async_tree_cpu_io_mixed, create_gc_cycles, coroutines, shortest_path, generators, pycparser, pathlib, hexiom, docutils, sqlglot_v2_parse, async_tree_io_tg, async_tree_memoization_tg, subparsers, meteor_contest, richards_super, bench_mp_pool, fannkuch, pprint_pformat, pickle_pure_python, async_tree_memoization, mako, async_tree_none_tg, sympy_str, tomli_loads, regex_v8, 2to3, genshi_xml, json_dumps, gc_traversal, async_tree_io, xml_etree_parse, pylint, k_core, connected_components, asyncio_websockets, many_optionals, nbody, json

- Geometric mean (including insignificant results): 1.003x faster

# HPT report

- Reliability score: 65.35% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown