# Results vs. base

- fork: mdboom
- ref: early_tail_call_load
- machine: linux-x86_64
- commit hash: e9c43a0
- commit date: 2025-02-12
- overall geometric mean: 1.008x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250209-linux-x86_64-python-d05053a203d922c8056f-3.14.0a4+-d05053a | bm-20250212-linux-x86_64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 248 ms                                                                 | 244 ms: 1.02x faster                                                   |
| docutils       | 2.55 sec                                                               | 2.51 sec: 1.02x faster                                                 |
| html5lib       | 58.7 ms                                                                | 55.3 ms: 1.06x faster                                                  |
| sphinx         | 978 ms                                                                 | 964 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                                  | 1.03x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250209-linux-x86_64-python-d05053a203d922c8056f-3.14.0a4+-d05053a | bm-20250212-linux-x86_64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 523 ms                                                                 | 487 ms: 1.08x faster                                                   |
| async_tree_cpu_io_mixed_tg | 511 ms                                                                 | 478 ms: 1.07x faster                                                   |
| coroutines                 | 21.5 ms                                                                | 21.0 ms: 1.02x faster                                                  |
| async_generators           | 381 ms                                                                 | 378 ms: 1.01x faster                                                   |
| Geometric mean             | (ref)                                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (7): async_tree_none, async_tree_none_tg, async_tree_io, async_tree_memoization, async_tree_io_tg, asyncio_websockets, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250209-linux-x86_64-python-d05053a203d922c8056f-3.14.0a4+-d05053a | bm-20250212-linux-x86_64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 219 ms                                                                 | 202 ms: 1.09x faster                                                   |
| nbody          | 84.0 ms                                                                | 80.5 ms: 1.04x faster                                                  |
| float          | 65.6 ms                                                                | 64.1 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                                  | 1.05x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250209-linux-x86_64-python-d05053a203d922c8056f-3.14.0a4+-d05053a | bm-20250212-linux-x86_64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 124 ms                                                                 | 119 ms: 1.04x faster                                                   |
| regex_effbot   | 3.16 ms                                                                | 3.13 ms: 1.01x faster                                                  |
| regex_dna      | 195 ms                                                                 | 198 ms: 1.02x slower                                                   |
| regex_v8       | 24.5 ms                                                                | 24.9 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250209-linux-x86_64-python-d05053a203d922c8056f-3.14.0a4+-d05053a | bm-20250212-linux-x86_64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.95 sec                                                               | 1.86 sec: 1.05x faster                                                 |
| unpickle_pure_python | 215 us                                                                 | 206 us: 1.05x faster                                                   |
| pickle_pure_python   | 306 us                                                                 | 299 us: 1.02x faster                                                   |
| xml_etree_process    | 57.8 ms                                                                | 56.9 ms: 1.02x faster                                                  |
| xml_etree_generate   | 84.3 ms                                                                | 83.8 ms: 1.01x faster                                                  |
| xml_etree_iterparse  | 99.7 ms                                                                | 101 ms: 1.01x slower                                                   |
| json_dumps           | 12.4 ms                                                                | 12.5 ms: 1.01x slower                                                  |
| json_loads           | 30.4 us                                                                | 30.8 us: 1.01x slower                                                  |
| xml_etree_parse      | 156 ms                                                                 | 159 ms: 1.02x slower                                                   |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250209-linux-x86_64-python-d05053a203d922c8056f-3.14.0a4+-d05053a | bm-20250212-linux-x86_64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.6 ms                                                                | 12.6 ms: 1.00x faster                                                  |
| python_startup_no_site | 6.96 ms                                                                | 6.95 ms: 1.00x faster                                                  |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250209-linux-x86_64-python-d05053a203d922c8056f-3.14.0a4+-d05053a | bm-20250212-linux-x86_64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako           | 11.6 ms                                                                | 11.3 ms: 1.03x faster                                                  |
| genshi_text    | 20.6 ms                                                                | 20.7 ms: 1.01x slower                                                  |
| genshi_xml     | 47.1 ms                                                                | 47.5 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20250209-linux-x86_64-python-d05053a203d922c8056f-3.14.0a4+-d05053a | bm-20250212-linux-x86_64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits                   | 219 ms                                                                 | 202 ms: 1.09x faster                                                   |
| async_tree_cpu_io_mixed    | 523 ms                                                                 | 487 ms: 1.08x faster                                                   |
| async_tree_cpu_io_mixed_tg | 511 ms                                                                 | 478 ms: 1.07x faster                                                   |
| logging_silent             | 87.9 ns                                                                | 82.3 ns: 1.07x faster                                                  |
| go                         | 114 ms                                                                 | 107 ms: 1.06x faster                                                   |
| html5lib                   | 58.7 ms                                                                | 55.3 ms: 1.06x faster                                                  |
| deltablue                  | 3.02 ms                                                                | 2.85 ms: 1.06x faster                                                  |
| hexiom                     | 6.03 ms                                                                | 5.70 ms: 1.06x faster                                                  |
| mdp                        | 2.76 sec                                                               | 2.61 sec: 1.06x faster                                                 |
| tomli_loads                | 1.95 sec                                                               | 1.86 sec: 1.05x faster                                                 |
| pyflate                    | 414 ms                                                                 | 394 ms: 1.05x faster                                                   |
| sqlalchemy_imperative      | 16.0 ms                                                                | 15.2 ms: 1.05x faster                                                  |
| richards                   | 41.3 ms                                                                | 39.3 ms: 1.05x faster                                                  |
| scimark_lu                 | 111 ms                                                                 | 106 ms: 1.05x faster                                                   |
| unpickle_pure_python       | 215 us                                                                 | 206 us: 1.05x faster                                                   |
| richards_super             | 47.8 ms                                                                | 45.8 ms: 1.04x faster                                                  |
| sqlglot_parse              | 1.19 ms                                                                | 1.14 ms: 1.04x faster                                                  |
| spectral_norm              | 87.8 ms                                                                | 84.1 ms: 1.04x faster                                                  |
| regex_compile              | 124 ms                                                                 | 119 ms: 1.04x faster                                                   |
| scimark_sor                | 110 ms                                                                 | 106 ms: 1.04x faster                                                   |
| fannkuch                   | 401 ms                                                                 | 384 ms: 1.04x faster                                                   |
| nbody                      | 84.0 ms                                                                | 80.5 ms: 1.04x faster                                                  |
| dulwich_log                | 62.6 ms                                                                | 60.1 ms: 1.04x faster                                                  |
| scimark_fft                | 290 ms                                                                 | 279 ms: 1.04x faster                                                   |
| deepcopy_memo              | 29.3 us                                                                | 28.2 us: 1.04x faster                                                  |
| sqlglot_transpile          | 1.49 ms                                                                | 1.44 ms: 1.04x faster                                                  |
| raytrace                   | 258 ms                                                                 | 249 ms: 1.04x faster                                                   |
| crypto_pyaes               | 68.7 ms                                                                | 66.5 ms: 1.03x faster                                                  |
| chaos                      | 54.4 ms                                                                | 52.7 ms: 1.03x faster                                                  |
| deepcopy                   | 248 us                                                                 | 240 us: 1.03x faster                                                   |
| sympy_integrate            | 19.0 ms                                                                | 18.6 ms: 1.03x faster                                                  |
| scimark_monte_carlo        | 60.2 ms                                                                | 58.7 ms: 1.03x faster                                                  |
| sympy_sum                  | 142 ms                                                                 | 139 ms: 1.03x faster                                                   |
| pprint_safe_repr           | 731 ms                                                                 | 713 ms: 1.03x faster                                                   |
| many_optionals             | 917 us                                                                 | 894 us: 1.03x faster                                                   |
| mako                       | 11.6 ms                                                                | 11.3 ms: 1.03x faster                                                  |
| sympy_str                  | 258 ms                                                                 | 251 ms: 1.02x faster                                                   |
| coroutines                 | 21.5 ms                                                                | 21.0 ms: 1.02x faster                                                  |
| sqlalchemy_declarative     | 124 ms                                                                 | 121 ms: 1.02x faster                                                   |
| float                      | 65.6 ms                                                                | 64.1 ms: 1.02x faster                                                  |
| pickle_pure_python         | 306 us                                                                 | 299 us: 1.02x faster                                                   |
| sympy_expand               | 438 ms                                                                 | 428 ms: 1.02x faster                                                   |
| pprint_pformat             | 1.48 sec                                                               | 1.45 sec: 1.02x faster                                                 |
| deepcopy_reduce            | 2.57 us                                                                | 2.52 us: 1.02x faster                                                  |
| docutils                   | 2.55 sec                                                               | 2.51 sec: 1.02x faster                                                 |
| 2to3                       | 248 ms                                                                 | 244 ms: 1.02x faster                                                   |
| comprehensions             | 15.1 us                                                                | 14.9 us: 1.02x faster                                                  |
| xml_etree_process          | 57.8 ms                                                                | 56.9 ms: 1.02x faster                                                  |
| sphinx                     | 978 ms                                                                 | 964 ms: 1.01x faster                                                   |
| telco                      | 7.27 ms                                                                | 7.18 ms: 1.01x faster                                                  |
| logging_simple             | 5.35 us                                                                | 5.28 us: 1.01x faster                                                  |
| bench_thread_pool          | 823 us                                                                 | 813 us: 1.01x faster                                                   |
| subparsers                 | 20.0 ms                                                                | 19.8 ms: 1.01x faster                                                  |
| logging_format             | 5.89 us                                                                | 5.83 us: 1.01x faster                                                  |
| regex_effbot               | 3.16 ms                                                                | 3.13 ms: 1.01x faster                                                  |
| async_generators           | 381 ms                                                                 | 378 ms: 1.01x faster                                                   |
| sqlglot_optimize           | 51.2 ms                                                                | 50.8 ms: 1.01x faster                                                  |
| bpe_tokeniser              | 4.29 sec                                                               | 4.26 sec: 1.01x faster                                                 |
| pathlib                    | 14.5 ms                                                                | 14.4 ms: 1.01x faster                                                  |
| bench_mp_pool              | 79.5 ms                                                                | 79.0 ms: 1.01x faster                                                  |
| xml_etree_generate         | 84.3 ms                                                                | 83.8 ms: 1.01x faster                                                  |
| gc_traversal               | 5.06 ms                                                                | 5.04 ms: 1.00x faster                                                  |
| nqueens                    | 75.1 ms                                                                | 74.8 ms: 1.00x faster                                                  |
| python_startup             | 12.6 ms                                                                | 12.6 ms: 1.00x faster                                                  |
| python_startup_no_site     | 6.96 ms                                                                | 6.95 ms: 1.00x faster                                                  |
| genshi_text                | 20.6 ms                                                                | 20.7 ms: 1.01x slower                                                  |
| genshi_xml                 | 47.1 ms                                                                | 47.5 ms: 1.01x slower                                                  |
| create_gc_cycles           | 2.52 ms                                                                | 2.54 ms: 1.01x slower                                                  |
| meteor_contest             | 106 ms                                                                 | 107 ms: 1.01x slower                                                   |
| xml_etree_iterparse        | 99.7 ms                                                                | 101 ms: 1.01x slower                                                   |
| json_dumps                 | 12.4 ms                                                                | 12.5 ms: 1.01x slower                                                  |
| json_loads                 | 30.4 us                                                                | 30.8 us: 1.01x slower                                                  |
| regex_dna                  | 195 ms                                                                 | 198 ms: 1.02x slower                                                   |
| sqlite_synth               | 2.66 us                                                                | 2.70 us: 1.02x slower                                                  |
| regex_v8                   | 24.5 ms                                                                | 24.9 ms: 1.02x slower                                                  |
| xml_etree_parse            | 156 ms                                                                 | 159 ms: 1.02x slower                                                   |
| scimark_sparse_mat_mult    | 3.96 ms                                                                | 4.07 ms: 1.03x slower                                                  |
| sqlglot_normalize          | 102 ms                                                                 | 265 ms: 2.60x slower                                                   |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (18): pylint, async_tree_none, async_tree_none_tg, typing_runtime_protocols, async_tree_io, pycparser, async_tree_memoization, async_tree_io_tg, asyncio_websockets, django_template, connected_components, shortest_path, k_core, async_tree_memoization_tg, generators, thrift, json, coverage

- Geometric mean (including insignificant results): 1.008x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x