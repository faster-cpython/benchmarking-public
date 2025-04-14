# Results vs. base

- fork: brandtbucher
- ref: no_dynamic_exit
- machine: linux-x86_64
- commit hash: 06da973
- commit date: 2025-02-05
- overall geometric mean: 1.010x faster
- HPT reliability: 95.77%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250205-linux-x86_64-brandtbucher-no_dynamic_exit-3.14.0a4+-06da973 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 261 ms                                                                 | 259 ms: 1.01x faster                                                    |
| docutils       | 2.67 sec                                                               | 2.69 sec: 1.01x slower                                                  |
| html5lib       | 63.3 ms                                                                | 62.2 ms: 1.02x faster                                                   |
| sphinx         | 1.04 sec                                                               | 1.02 sec: 1.02x faster                                                  |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250205-linux-x86_64-brandtbucher-no_dynamic_exit-3.14.0a4+-06da973 |
|------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_generators | 411 ms                                                                 | 414 ms: 1.01x slower                                                    |
| coroutines       | 23.0 ms                                                                | 23.6 ms: 1.03x slower                                                   |
| Geometric mean   | (ref)                                                                  | 1.00x slower                                                            |

Benchmark hidden because not significant (9): async_tree_none, async_tree_io, async_tree_cpu_io_mixed, async_tree_memoization, asyncio_websockets, async_tree_io_tg, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250205-linux-x86_64-brandtbucher-no_dynamic_exit-3.14.0a4+-06da973 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 90.4 ms                                                                | 89.5 ms: 1.01x faster                                                   |
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x faster                                                    |
| float          | 67.2 ms                                                                | 70.7 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250205-linux-x86_64-brandtbucher-no_dynamic_exit-3.14.0a4+-06da973 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 130 ms                                                                 | 126 ms: 1.03x faster                                                    |
| regex_dna      | 211 ms                                                                 | 213 ms: 1.01x slower                                                    |
| regex_v8       | 24.0 ms                                                                | 24.4 ms: 1.02x slower                                                   |
| regex_effbot   | 3.18 ms                                                                | 3.29 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250205-linux-x86_64-brandtbucher-no_dynamic_exit-3.14.0a4+-06da973 |
|--------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_loads         | 28.9 us                                                                | 28.6 us: 1.01x faster                                                   |
| tomli_loads        | 1.84 sec                                                               | 1.82 sec: 1.01x faster                                                  |
| xml_etree_process  | 54.6 ms                                                                | 54.3 ms: 1.01x faster                                                   |
| xml_etree_generate | 78.0 ms                                                                | 79.0 ms: 1.01x slower                                                   |
| json_dumps         | 11.1 ms                                                                | 11.8 ms: 1.07x slower                                                   |
| Geometric mean     | (ref)                                                                  | 1.01x slower                                                            |

Benchmark hidden because not significant (4): pickle_pure_python, xml_etree_parse, unpickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250205-linux-x86_64-brandtbucher-no_dynamic_exit-3.14.0a4+-06da973 |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 12.9 ms                                                                | 12.8 ms: 1.00x faster                                                   |
| python_startup_no_site | 7.06 ms                                                                | 7.03 ms: 1.00x faster                                                   |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250205-linux-x86_64-brandtbucher-no_dynamic_exit-3.14.0a4+-06da973 |
|-----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 57.7 ms                                                                | 49.8 ms: 1.16x faster                                                   |
| genshi_text     | 23.0 ms                                                                | 21.7 ms: 1.06x faster                                                   |
| django_template | 33.1 ms                                                                | 32.1 ms: 1.03x faster                                                   |
| mako            | 10.3 ms                                                                | 9.99 ms: 1.03x faster                                                   |
| Geometric mean  | (ref)                                                                  | 1.07x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250205-linux-x86_64-brandtbucher-no_dynamic_exit-3.14.0a4+-06da973 |
|--------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| generators               | 37.5 ms                                                                | 27.6 ms: 1.36x faster                                                   |
| genshi_xml               | 57.7 ms                                                                | 49.8 ms: 1.16x faster                                                   |
| hexiom                   | 7.46 ms                                                                | 6.66 ms: 1.12x faster                                                   |
| deltablue                | 3.49 ms                                                                | 3.17 ms: 1.10x faster                                                   |
| raytrace                 | 290 ms                                                                 | 270 ms: 1.07x faster                                                    |
| go                       | 128 ms                                                                 | 120 ms: 1.07x faster                                                    |
| genshi_text              | 23.0 ms                                                                | 21.7 ms: 1.06x faster                                                   |
| logging_silent           | 108 ns                                                                 | 103 ns: 1.05x faster                                                    |
| pyflate                  | 463 ms                                                                 | 444 ms: 1.04x faster                                                    |
| scimark_sparse_mat_mult  | 4.63 ms                                                                | 4.48 ms: 1.03x faster                                                   |
| deepcopy                 | 265 us                                                                 | 257 us: 1.03x faster                                                    |
| django_template          | 33.1 ms                                                                | 32.1 ms: 1.03x faster                                                   |
| regex_compile            | 130 ms                                                                 | 126 ms: 1.03x faster                                                    |
| deepcopy_reduce          | 2.73 us                                                                | 2.66 us: 1.03x faster                                                   |
| mako                     | 10.3 ms                                                                | 9.99 ms: 1.03x faster                                                   |
| logging_simple           | 5.63 us                                                                | 5.52 us: 1.02x faster                                                   |
| sphinx                   | 1.04 sec                                                               | 1.02 sec: 1.02x faster                                                  |
| sqlglot_normalize        | 108 ms                                                                 | 106 ms: 1.02x faster                                                    |
| html5lib                 | 63.3 ms                                                                | 62.2 ms: 1.02x faster                                                   |
| sympy_integrate          | 20.5 ms                                                                | 20.2 ms: 1.02x faster                                                   |
| dulwich_log              | 66.8 ms                                                                | 65.8 ms: 1.02x faster                                                   |
| sympy_sum                | 154 ms                                                                 | 152 ms: 1.01x faster                                                    |
| scimark_fft              | 314 ms                                                                 | 310 ms: 1.01x faster                                                    |
| crypto_pyaes             | 71.3 ms                                                                | 70.4 ms: 1.01x faster                                                   |
| sqlglot_optimize         | 54.1 ms                                                                | 53.5 ms: 1.01x faster                                                   |
| typing_runtime_protocols | 165 us                                                                 | 163 us: 1.01x faster                                                    |
| nbody                    | 90.4 ms                                                                | 89.5 ms: 1.01x faster                                                   |
| json_loads               | 28.9 us                                                                | 28.6 us: 1.01x faster                                                   |
| tomli_loads              | 1.84 sec                                                               | 1.82 sec: 1.01x faster                                                  |
| logging_format           | 6.17 us                                                                | 6.12 us: 1.01x faster                                                   |
| bench_thread_pool        | 894 us                                                                 | 886 us: 1.01x faster                                                    |
| sympy_str                | 279 ms                                                                 | 277 ms: 1.01x faster                                                    |
| 2to3                     | 261 ms                                                                 | 259 ms: 1.01x faster                                                    |
| many_optionals           | 958 us                                                                 | 951 us: 1.01x faster                                                    |
| pathlib                  | 16.1 ms                                                                | 16.0 ms: 1.01x faster                                                   |
| xml_etree_process        | 54.6 ms                                                                | 54.3 ms: 1.01x faster                                                   |
| bench_mp_pool            | 81.0 ms                                                                | 80.5 ms: 1.01x faster                                                   |
| python_startup           | 12.9 ms                                                                | 12.8 ms: 1.00x faster                                                   |
| python_startup_no_site   | 7.06 ms                                                                | 7.03 ms: 1.00x faster                                                   |
| shortest_path            | 481 ms                                                                 | 481 ms: 1.00x faster                                                    |
| pidigits                 | 186 ms                                                                 | 186 ms: 1.00x faster                                                    |
| create_gc_cycles         | 2.45 ms                                                                | 2.45 ms: 1.00x slower                                                   |
| gc_traversal             | 4.77 ms                                                                | 4.78 ms: 1.00x slower                                                   |
| bpe_tokeniser            | 4.36 sec                                                               | 4.38 sec: 1.00x slower                                                  |
| sqlglot_parse            | 1.28 ms                                                                | 1.28 ms: 1.00x slower                                                   |
| sympy_expand             | 470 ms                                                                 | 472 ms: 1.00x slower                                                    |
| docutils                 | 2.67 sec                                                               | 2.69 sec: 1.01x slower                                                  |
| async_generators         | 411 ms                                                                 | 414 ms: 1.01x slower                                                    |
| mdp                      | 2.54 sec                                                               | 2.56 sec: 1.01x slower                                                  |
| regex_dna                | 211 ms                                                                 | 213 ms: 1.01x slower                                                    |
| spectral_norm            | 95.6 ms                                                                | 96.4 ms: 1.01x slower                                                   |
| scimark_lu               | 113 ms                                                                 | 114 ms: 1.01x slower                                                    |
| xml_etree_generate       | 78.0 ms                                                                | 79.0 ms: 1.01x slower                                                   |
| sqlglot_transpile        | 1.58 ms                                                                | 1.61 ms: 1.01x slower                                                   |
| nqueens                  | 89.5 ms                                                                | 90.9 ms: 1.02x slower                                                   |
| regex_v8                 | 24.0 ms                                                                | 24.4 ms: 1.02x slower                                                   |
| coroutines               | 23.0 ms                                                                | 23.6 ms: 1.03x slower                                                   |
| regex_effbot             | 3.18 ms                                                                | 3.29 ms: 1.03x slower                                                   |
| scimark_monte_carlo      | 63.9 ms                                                                | 66.2 ms: 1.04x slower                                                   |
| scimark_sor              | 114 ms                                                                 | 119 ms: 1.05x slower                                                    |
| float                    | 67.2 ms                                                                | 70.7 ms: 1.05x slower                                                   |
| json_dumps               | 11.1 ms                                                                | 11.8 ms: 1.07x slower                                                   |
| Geometric mean           | (ref)                                                                  | 1.01x faster                                                            |

Benchmark hidden because not significant (34): pylint, pycparser, async_tree_none, async_tree_io, json, pprint_pformat, pickle_pure_python, fannkuch, telco, k_core, richards, chaos, subparsers, async_tree_cpu_io_mixed, richards_super, async_tree_memoization, xml_etree_parse, comprehensions, meteor_contest, sqlalchemy_imperative, deepcopy_memo, connected_components, sqlalchemy_declarative, thrift, asyncio_websockets, async_tree_io_tg, async_tree_none_tg, sqlite_synth, unpickle_pure_python, xml_etree_iterparse, pprint_safe_repr, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, coverage

- Geometric mean (including insignificant results): 1.010x faster

# HPT report

- Reliability score: 95.77% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x