# Results vs. base

- fork: zooba
- ref: gh_134923
- machine: windows-amd64
- commit hash: 25f01a3
- commit date: 2025-05-30
- overall geometric mean: 1.001x slower
- HPT reliability: 77.38%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250530-pythonperf1-amd64-python-b367e27af9b52528e395-3.15.0a0-b367e27 | bm-20250530-pythonperf1-amd64-zooba-gh_134923-3.15.0a0-25f01a3 |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------:|
| html5lib       | 39.1 ms                                                                    | 38.7 ms: 1.01x faster                                          |
| Geometric mean | (ref)                                                                      | 1.00x faster                                                   |

Benchmark hidden because not significant (3): 2to3, docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20250530-pythonperf1-amd64-python-b367e27af9b52528e395-3.15.0a0-b367e27 | bm-20250530-pythonperf1-amd64-zooba-gh_134923-3.15.0a0-25f01a3 |
|------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_io_tg       | 402 ms                                                                     | 389 ms: 1.03x faster                                           |
| async_tree_memoization | 206 ms                                                                     | 204 ms: 1.01x faster                                           |
| coroutines             | 13.7 ms                                                                    | 13.8 ms: 1.00x slower                                          |
| Geometric mean         | (ref)                                                                      | 1.00x faster                                                   |

Benchmark hidden because not significant (8): async_tree_memoization_tg, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_io, async_tree_none, async_generators, async_tree_none_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250530-pythonperf1-amd64-python-b367e27af9b52528e395-3.15.0a0-b367e27 | bm-20250530-pythonperf1-amd64-zooba-gh_134923-3.15.0a0-25f01a3 |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 43.7 ms                                                                    | 44.8 ms: 1.03x slower                                          |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                   |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250530-pythonperf1-amd64-python-b367e27af9b52528e395-3.15.0a0-b367e27 | bm-20250530-pythonperf1-amd64-zooba-gh_134923-3.15.0a0-25f01a3 |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_effbot   | 1.59 ms                                                                    | 1.57 ms: 1.02x faster                                          |
| regex_compile  | 79.7 ms                                                                    | 78.7 ms: 1.01x faster                                          |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                   |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250530-pythonperf1-amd64-python-b367e27af9b52528e395-3.15.0a0-b367e27 | bm-20250530-pythonperf1-amd64-zooba-gh_134923-3.15.0a0-25f01a3 |
|---------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------:|
| tomli_loads         | 1.37 sec                                                                   | 1.33 sec: 1.03x faster                                         |
| xml_etree_iterparse | 63.5 ms                                                                    | 62.9 ms: 1.01x faster                                          |
| json_loads          | 14.9 us                                                                    | 15.0 us: 1.01x slower                                          |
| json_dumps          | 6.11 ms                                                                    | 6.19 ms: 1.01x slower                                          |
| xml_etree_parse     | 87.9 ms                                                                    | 89.0 ms: 1.01x slower                                          |
| xml_etree_process   | 38.1 ms                                                                    | 38.8 ms: 1.02x slower                                          |
| xml_etree_generate  | 54.8 ms                                                                    | 55.9 ms: 1.02x slower                                          |
| pickle_pure_python  | 209 us                                                                     | 215 us: 1.03x slower                                           |
| Geometric mean      | (ref)                                                                      | 1.01x slower                                                   |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250530-pythonperf1-amd64-python-b367e27af9b52528e395-3.15.0a0-b367e27 | bm-20250530-pythonperf1-amd64-zooba-gh_134923-3.15.0a0-25f01a3 |
|-----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------:|
| genshi_xml      | 33.3 ms                                                                    | 33.6 ms: 1.01x slower                                          |
| genshi_text     | 15.0 ms                                                                    | 15.1 ms: 1.01x slower                                          |
| django_template | 24.2 ms                                                                    | 24.4 ms: 1.01x slower                                          |
| Geometric mean  | (ref)                                                                      | 1.01x slower                                                   |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20250530-pythonperf1-amd64-python-b367e27af9b52528e395-3.15.0a0-b367e27 | bm-20250530-pythonperf1-amd64-zooba-gh_134923-3.15.0a0-25f01a3 |
|--------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------:|
| fannkuch                 | 258 ms                                                                     | 247 ms: 1.05x faster                                           |
| spectral_norm            | 57.7 ms                                                                    | 55.7 ms: 1.03x faster                                          |
| async_tree_io_tg         | 402 ms                                                                     | 389 ms: 1.03x faster                                           |
| bpe_tokeniser            | 2.93 sec                                                                   | 2.85 sec: 1.03x faster                                         |
| tomli_loads              | 1.37 sec                                                                   | 1.33 sec: 1.03x faster                                         |
| typing_runtime_protocols | 103 us                                                                     | 101 us: 1.02x faster                                           |
| deltablue                | 2.18 ms                                                                    | 2.14 ms: 1.02x faster                                          |
| crypto_pyaes             | 47.1 ms                                                                    | 46.1 ms: 1.02x faster                                          |
| scimark_sor              | 76.1 ms                                                                    | 74.7 ms: 1.02x faster                                          |
| hexiom                   | 3.99 ms                                                                    | 3.93 ms: 1.02x faster                                          |
| comprehensions           | 10.6 us                                                                    | 10.5 us: 1.02x faster                                          |
| richards                 | 27.1 ms                                                                    | 26.7 ms: 1.02x faster                                          |
| regex_effbot             | 1.59 ms                                                                    | 1.57 ms: 1.02x faster                                          |
| richards_super           | 30.9 ms                                                                    | 30.5 ms: 1.01x faster                                          |
| regex_compile            | 79.7 ms                                                                    | 78.7 ms: 1.01x faster                                          |
| async_tree_memoization   | 206 ms                                                                     | 204 ms: 1.01x faster                                           |
| logging_silent           | 321 ns                                                                     | 317 ns: 1.01x faster                                           |
| go                       | 75.1 ms                                                                    | 74.2 ms: 1.01x faster                                          |
| html5lib                 | 39.1 ms                                                                    | 38.7 ms: 1.01x faster                                          |
| mdp                      | 795 ms                                                                     | 788 ms: 1.01x faster                                           |
| xml_etree_iterparse      | 63.5 ms                                                                    | 62.9 ms: 1.01x faster                                          |
| dulwich_log              | 41.0 ms                                                                    | 40.9 ms: 1.00x faster                                          |
| coroutines               | 13.7 ms                                                                    | 13.8 ms: 1.00x slower                                          |
| generators               | 19.2 ms                                                                    | 19.4 ms: 1.01x slower                                          |
| sqlglot_v2_optimize      | 33.5 ms                                                                    | 33.7 ms: 1.01x slower                                          |
| genshi_xml               | 33.3 ms                                                                    | 33.6 ms: 1.01x slower                                          |
| genshi_text              | 15.0 ms                                                                    | 15.1 ms: 1.01x slower                                          |
| gc_traversal             | 2.11 ms                                                                    | 2.13 ms: 1.01x slower                                          |
| django_template          | 24.2 ms                                                                    | 24.4 ms: 1.01x slower                                          |
| json_loads               | 14.9 us                                                                    | 15.0 us: 1.01x slower                                          |
| coverage                 | 290 ms                                                                     | 293 ms: 1.01x slower                                           |
| json_dumps               | 6.11 ms                                                                    | 6.19 ms: 1.01x slower                                          |
| subparsers               | 16.9 ms                                                                    | 17.1 ms: 1.01x slower                                          |
| xml_etree_parse          | 87.9 ms                                                                    | 89.0 ms: 1.01x slower                                          |
| deepcopy_reduce          | 1.84 us                                                                    | 1.87 us: 1.01x slower                                          |
| scimark_monte_carlo      | 38.7 ms                                                                    | 39.2 ms: 1.02x slower                                          |
| xml_etree_process        | 38.1 ms                                                                    | 38.8 ms: 1.02x slower                                          |
| scimark_lu               | 56.6 ms                                                                    | 57.7 ms: 1.02x slower                                          |
| xml_etree_generate       | 54.8 ms                                                                    | 55.9 ms: 1.02x slower                                          |
| float                    | 43.7 ms                                                                    | 44.8 ms: 1.03x slower                                          |
| deepcopy                 | 168 us                                                                     | 172 us: 1.03x slower                                           |
| deepcopy_memo            | 17.7 us                                                                    | 18.1 us: 1.03x slower                                          |
| pickle_pure_python       | 209 us                                                                     | 215 us: 1.03x slower                                           |
| scimark_sparse_mat_mult  | 2.46 ms                                                                    | 2.53 ms: 1.03x slower                                          |
| raytrace                 | 179 ms                                                                     | 185 ms: 1.03x slower                                           |
| pprint_pformat           | 1.09 sec                                                                   | 1.12 sec: 1.03x slower                                         |
| pprint_safe_repr         | 530 ms                                                                     | 549 ms: 1.04x slower                                           |
| json                     | 3.02 ms                                                                    | 3.16 ms: 1.05x slower                                          |
| Geometric mean           | (ref)                                                                      | 1.00x faster                                                   |

Benchmark hidden because not significant (46): bench_thread_pool, regex_v8, pycparser, sphinx, pyflate, thrift, async_tree_memoization_tg, shortest_path, asyncio_websockets, pylint, many_optionals, mako, regex_dna, async_tree_cpu_io_mixed, chaos, async_tree_io, bench_mp_pool, create_gc_cycles, python_startup_no_site, meteor_contest, telco, sympy_str, sympy_integrate, sympy_sum, sqlglot_v2_transpile, sqlglot_v2_parse, sympy_expand, nqueens, docutils, async_tree_none, logging_simple, sqlglot_v2_normalize, scimark_fft, async_generators, connected_components, sqlite_synth, unpickle_pure_python, pidigits, 2to3, python_startup, logging_format, nbody, async_tree_none_tg, async_tree_cpu_io_mixed_tg, pathlib, k_core

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 77.38% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown