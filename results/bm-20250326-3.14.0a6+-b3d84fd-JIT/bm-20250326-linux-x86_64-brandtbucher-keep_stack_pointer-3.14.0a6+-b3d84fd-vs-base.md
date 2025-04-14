# Results vs. base

- fork: brandtbucher
- ref: keep_stack_pointer
- machine: linux-x86_64
- commit hash: b3d84fd
- commit date: 2025-03-26
- overall geometric mean: 1.007x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250326-linux-x86_64-python-4b3d5b604210f68005ef-3.14.0a6+-4b3d5b6 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 262 ms                                                                 | 259 ms: 1.01x faster                                                       |
| docutils       | 2.69 sec                                                               | 2.66 sec: 1.01x faster                                                     |
| html5lib       | 62.3 ms                                                                | 62.7 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250326-linux-x86_64-python-4b3d5b604210f68005ef-3.14.0a6+-4b3d5b6 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|-------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 490 ms                                                                 | 487 ms: 1.01x faster                                                       |
| async_generators        | 413 ms                                                                 | 411 ms: 1.01x faster                                                       |
| coroutines              | 23.5 ms                                                                | 24.0 ms: 1.02x slower                                                      |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_io_tg, async_tree_none, asyncio_websockets, async_tree_io, async_tree_none_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250326-linux-x86_64-python-4b3d5b604210f68005ef-3.14.0a6+-4b3d5b6 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 85.9 ms                                                                | 82.8 ms: 1.04x faster                                                      |
| float          | 63.9 ms                                                                | 62.5 ms: 1.02x faster                                                      |
| pidigits       | 186 ms                                                                 | 185 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250326-linux-x86_64-python-4b3d5b604210f68005ef-3.14.0a6+-4b3d5b6 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 225 ms                                                                 | 211 ms: 1.06x faster                                                       |
| regex_v8       | 23.9 ms                                                                | 22.6 ms: 1.06x faster                                                      |
| regex_effbot   | 3.35 ms                                                                | 3.17 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                                  | 1.04x faster                                                               |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250326-linux-x86_64-python-4b3d5b604210f68005ef-3.14.0a6+-4b3d5b6 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                                 | 205 us: 1.02x faster                                                       |
| pickle_pure_python   | 321 us                                                                 | 316 us: 1.02x faster                                                       |
| xml_etree_parse      | 141 ms                                                                 | 140 ms: 1.01x faster                                                       |
| xml_etree_process    | 56.1 ms                                                                | 55.6 ms: 1.01x faster                                                      |
| tomli_loads          | 1.87 sec                                                               | 1.86 sec: 1.01x faster                                                     |
| json_dumps           | 11.5 ms                                                                | 11.6 ms: 1.01x slower                                                      |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (3): xml_etree_generate, json_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250326-linux-x86_64-python-4b3d5b604210f68005ef-3.14.0a6+-4b3d5b6 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 8.19 ms                                                                | 8.21 ms: 1.00x slower                                                      |
| python_startup         | 13.1 ms                                                                | 13.1 ms: 1.00x slower                                                      |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250326-linux-x86_64-python-4b3d5b604210f68005ef-3.14.0a6+-4b3d5b6 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 32.1 ms                                                                | 31.5 ms: 1.02x faster                                                      |
| mako            | 11.1 ms                                                                | 10.9 ms: 1.02x faster                                                      |
| genshi_text     | 20.9 ms                                                                | 21.0 ms: 1.01x slower                                                      |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20250326-linux-x86_64-python-4b3d5b604210f68005ef-3.14.0a6+-4b3d5b6 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|--------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna                | 225 ms                                                                 | 211 ms: 1.06x faster                                                       |
| regex_v8                 | 23.9 ms                                                                | 22.6 ms: 1.06x faster                                                      |
| regex_effbot             | 3.35 ms                                                                | 3.17 ms: 1.05x faster                                                      |
| deepcopy_reduce          | 2.75 us                                                                | 2.64 us: 1.04x faster                                                      |
| comprehensions           | 18.9 us                                                                | 18.2 us: 1.04x faster                                                      |
| nbody                    | 85.9 ms                                                                | 82.8 ms: 1.04x faster                                                      |
| spectral_norm            | 94.2 ms                                                                | 90.9 ms: 1.04x faster                                                      |
| richards                 | 35.9 ms                                                                | 34.7 ms: 1.04x faster                                                      |
| go                       | 127 ms                                                                 | 122 ms: 1.04x faster                                                       |
| deltablue                | 3.06 ms                                                                | 2.97 ms: 1.03x faster                                                      |
| richards_super           | 41.0 ms                                                                | 39.8 ms: 1.03x faster                                                      |
| pprint_pformat           | 1.55 sec                                                               | 1.51 sec: 1.02x faster                                                     |
| pycparser                | 1.15 sec                                                               | 1.12 sec: 1.02x faster                                                     |
| unpickle_pure_python     | 210 us                                                                 | 205 us: 1.02x faster                                                       |
| float                    | 63.9 ms                                                                | 62.5 ms: 1.02x faster                                                      |
| sqlglot_v2_parse         | 1.28 ms                                                                | 1.25 ms: 1.02x faster                                                      |
| sqlglot_v2_transpile     | 1.60 ms                                                                | 1.57 ms: 1.02x faster                                                      |
| django_template          | 32.1 ms                                                                | 31.5 ms: 1.02x faster                                                      |
| hexiom                   | 6.75 ms                                                                | 6.61 ms: 1.02x faster                                                      |
| telco                    | 7.87 ms                                                                | 7.72 ms: 1.02x faster                                                      |
| deepcopy                 | 262 us                                                                 | 257 us: 1.02x faster                                                       |
| mako                     | 11.1 ms                                                                | 10.9 ms: 1.02x faster                                                      |
| pickle_pure_python       | 321 us                                                                 | 316 us: 1.02x faster                                                       |
| pprint_safe_repr         | 762 ms                                                                 | 750 ms: 1.02x faster                                                       |
| crypto_pyaes             | 76.4 ms                                                                | 75.2 ms: 1.02x faster                                                      |
| scimark_fft              | 313 ms                                                                 | 309 ms: 1.02x faster                                                       |
| typing_runtime_protocols | 167 us                                                                 | 164 us: 1.01x faster                                                       |
| scimark_sor              | 121 ms                                                                 | 120 ms: 1.01x faster                                                       |
| sqlglot_v2_optimize      | 54.0 ms                                                                | 53.3 ms: 1.01x faster                                                      |
| xml_etree_parse          | 141 ms                                                                 | 140 ms: 1.01x faster                                                       |
| 2to3                     | 262 ms                                                                 | 259 ms: 1.01x faster                                                       |
| deepcopy_memo            | 28.8 us                                                                | 28.6 us: 1.01x faster                                                      |
| docutils                 | 2.69 sec                                                               | 2.66 sec: 1.01x faster                                                     |
| scimark_monte_carlo      | 67.3 ms                                                                | 66.6 ms: 1.01x faster                                                      |
| raytrace                 | 268 ms                                                                 | 265 ms: 1.01x faster                                                       |
| xml_etree_process        | 56.1 ms                                                                | 55.6 ms: 1.01x faster                                                      |
| mdp                      | 2.48 sec                                                               | 2.46 sec: 1.01x faster                                                     |
| logging_simple           | 5.64 us                                                                | 5.59 us: 1.01x faster                                                      |
| bpe_tokeniser            | 4.57 sec                                                               | 4.53 sec: 1.01x faster                                                     |
| async_tree_cpu_io_mixed  | 490 ms                                                                 | 487 ms: 1.01x faster                                                       |
| async_generators         | 413 ms                                                                 | 411 ms: 1.01x faster                                                       |
| tomli_loads              | 1.87 sec                                                               | 1.86 sec: 1.01x faster                                                     |
| sqlglot_v2_normalize     | 108 ms                                                                 | 107 ms: 1.00x faster                                                       |
| create_gc_cycles         | 2.49 ms                                                                | 2.48 ms: 1.00x faster                                                      |
| sympy_str                | 273 ms                                                                 | 272 ms: 1.00x faster                                                       |
| sympy_sum                | 151 ms                                                                 | 151 ms: 1.00x faster                                                       |
| pidigits                 | 186 ms                                                                 | 185 ms: 1.00x faster                                                       |
| python_startup_no_site   | 8.19 ms                                                                | 8.21 ms: 1.00x slower                                                      |
| python_startup           | 13.1 ms                                                                | 13.1 ms: 1.00x slower                                                      |
| generators               | 28.3 ms                                                                | 28.5 ms: 1.01x slower                                                      |
| genshi_text              | 20.9 ms                                                                | 21.0 ms: 1.01x slower                                                      |
| sqlite_synth             | 2.72 us                                                                | 2.74 us: 1.01x slower                                                      |
| dulwich_log              | 60.3 ms                                                                | 60.7 ms: 1.01x slower                                                      |
| json_dumps               | 11.5 ms                                                                | 11.6 ms: 1.01x slower                                                      |
| html5lib                 | 62.3 ms                                                                | 62.7 ms: 1.01x slower                                                      |
| chaos                    | 58.7 ms                                                                | 59.2 ms: 1.01x slower                                                      |
| fannkuch                 | 414 ms                                                                 | 419 ms: 1.01x slower                                                       |
| nqueens                  | 82.7 ms                                                                | 83.6 ms: 1.01x slower                                                      |
| shortest_path            | 489 ms                                                                 | 495 ms: 1.01x slower                                                       |
| pathlib                  | 16.6 ms                                                                | 16.8 ms: 1.01x slower                                                      |
| sqlalchemy_imperative    | 17.0 ms                                                                | 17.3 ms: 1.02x slower                                                      |
| coroutines               | 23.5 ms                                                                | 24.0 ms: 1.02x slower                                                      |
| gc_traversal             | 4.85 ms                                                                | 4.98 ms: 1.03x slower                                                      |
| scimark_sparse_mat_mult  | 4.44 ms                                                                | 4.59 ms: 1.03x slower                                                      |
| pyflate                  | 423 ms                                                                 | 448 ms: 1.06x slower                                                       |
| Geometric mean           | (ref)                                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (31): sphinx, xml_etree_generate, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, subparsers, async_tree_io_tg, async_tree_none, genshi_xml, k_core, pylint, json, meteor_contest, bench_thread_pool, logging_format, sympy_expand, asyncio_websockets, json_loads, scimark_lu, regex_compile, sqlalchemy_declarative, async_tree_io, sympy_integrate, bench_mp_pool, many_optionals, async_tree_none_tg, xml_etree_iterparse, connected_components, async_tree_memoization, coverage, thrift, logging_silent

- Geometric mean (including insignificant results): 1.007x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x