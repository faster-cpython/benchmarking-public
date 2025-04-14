# Results vs. base

- fork: faster-cpython
- ref: no_conditional_stack
- machine: linux-x86_64
- commit hash: d5e47ea
- commit date: 2025-01-20
- overall geometric mean: 1.008x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250120-linux-x86_64-python-f0f7b978be84c432139d-3.14.0a4+-f0f7b97 | bm-20250120-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d5e47ea |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 310 ms                                                                 | 313 ms: 1.01x slower                                                             |
| docutils       | 2.82 sec                                                               | 2.87 sec: 1.02x slower                                                           |
| html5lib       | 69.1 ms                                                                | 71.2 ms: 1.03x slower                                                            |
| sphinx         | 1.13 sec                                                               | 1.15 sec: 1.02x slower                                                           |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250120-linux-x86_64-python-f0f7b978be84c432139d-3.14.0a4+-f0f7b97 | bm-20250120-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d5e47ea |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| coroutines                 | 25.6 ms                                                                | 25.5 ms: 1.01x faster                                                            |
| async_generators           | 436 ms                                                                 | 437 ms: 1.00x slower                                                             |
| async_tree_io_tg           | 544 ms                                                                 | 551 ms: 1.01x slower                                                             |
| async_tree_cpu_io_mixed_tg | 463 ms                                                                 | 469 ms: 1.01x slower                                                             |
| async_tree_none_tg         | 236 ms                                                                 | 241 ms: 1.02x slower                                                             |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (6): asyncio_websockets, async_tree_io, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250120-linux-x86_64-python-f0f7b978be84c432139d-3.14.0a4+-f0f7b97 | bm-20250120-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d5e47ea |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 143 ms                                                                 | 139 ms: 1.03x faster                                                             |
| float          | 78.1 ms                                                                | 78.9 ms: 1.01x slower                                                            |
| pidigits       | 181 ms                                                                 | 190 ms: 1.05x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250120-linux-x86_64-python-f0f7b978be84c432139d-3.14.0a4+-f0f7b97 | bm-20250120-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d5e47ea |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.44 ms                                                                | 3.36 ms: 1.02x faster                                                            |
| regex_v8       | 25.4 ms                                                                | 25.0 ms: 1.02x faster                                                            |
| regex_dna      | 226 ms                                                                 | 223 ms: 1.01x faster                                                             |
| regex_compile  | 150 ms                                                                 | 153 ms: 1.02x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250120-linux-x86_64-python-f0f7b978be84c432139d-3.14.0a4+-f0f7b97 | bm-20250120-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d5e47ea |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_parse      | 148 ms                                                                 | 150 ms: 1.01x slower                                                             |
| xml_etree_iterparse  | 94.3 ms                                                                | 96.4 ms: 1.02x slower                                                            |
| pickle_pure_python   | 374 us                                                                 | 382 us: 1.02x slower                                                             |
| tomli_loads          | 2.37 sec                                                               | 2.45 sec: 1.03x slower                                                           |
| unpickle_pure_python | 259 us                                                                 | 273 us: 1.05x slower                                                             |
| xml_etree_process    | 68.5 ms                                                                | 72.1 ms: 1.05x slower                                                            |
| Geometric mean       | (ref)                                                                  | 1.02x slower                                                                     |

Benchmark hidden because not significant (3): json_dumps, json_loads, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250120-linux-x86_64-python-f0f7b978be84c432139d-3.14.0a4+-f0f7b97 | bm-20250120-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d5e47ea |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 14.9 ms                                                                | 15.1 ms: 1.01x slower                                                            |
| python_startup_no_site | 9.28 ms                                                                | 9.37 ms: 1.01x slower                                                            |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250120-linux-x86_64-python-f0f7b978be84c432139d-3.14.0a4+-f0f7b97 | bm-20250120-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d5e47ea |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako           | 16.3 ms                                                                | 16.5 ms: 1.01x slower                                                            |
| genshi_xml     | 60.9 ms                                                                | 62.8 ms: 1.03x slower                                                            |
| genshi_text    | 28.4 ms                                                                | 29.3 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                                     |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20250120-linux-x86_64-python-f0f7b978be84c432139d-3.14.0a4+-f0f7b97 | bm-20250120-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d5e47ea |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mdp                        | 2.87 sec                                                               | 2.73 sec: 1.05x faster                                                           |
| nbody                      | 143 ms                                                                 | 139 ms: 1.03x faster                                                             |
| regex_effbot               | 3.44 ms                                                                | 3.36 ms: 1.02x faster                                                            |
| gc_traversal               | 4.54 ms                                                                | 4.44 ms: 1.02x faster                                                            |
| regex_v8                   | 25.4 ms                                                                | 25.0 ms: 1.02x faster                                                            |
| regex_dna                  | 226 ms                                                                 | 223 ms: 1.01x faster                                                             |
| meteor_contest             | 133 ms                                                                 | 132 ms: 1.01x faster                                                             |
| pycparser                  | 1.22 sec                                                               | 1.21 sec: 1.01x faster                                                           |
| generators                 | 31.9 ms                                                                | 31.6 ms: 1.01x faster                                                            |
| crypto_pyaes               | 91.5 ms                                                                | 90.7 ms: 1.01x faster                                                            |
| deltablue                  | 4.80 ms                                                                | 4.77 ms: 1.01x faster                                                            |
| hexiom                     | 7.88 ms                                                                | 7.83 ms: 1.01x faster                                                            |
| coroutines                 | 25.6 ms                                                                | 25.5 ms: 1.01x faster                                                            |
| bpe_tokeniser              | 5.06 sec                                                               | 5.04 sec: 1.00x faster                                                           |
| pyflate                    | 523 ms                                                                 | 521 ms: 1.00x faster                                                             |
| chaos                      | 74.6 ms                                                                | 74.3 ms: 1.00x faster                                                            |
| scimark_sparse_mat_mult    | 6.14 ms                                                                | 6.13 ms: 1.00x faster                                                            |
| async_generators           | 436 ms                                                                 | 437 ms: 1.00x slower                                                             |
| raytrace                   | 359 ms                                                                 | 360 ms: 1.00x slower                                                             |
| comprehensions             | 21.1 us                                                                | 21.2 us: 1.00x slower                                                            |
| deepcopy_memo              | 39.4 us                                                                | 39.7 us: 1.01x slower                                                            |
| bench_thread_pool          | 3.47 ms                                                                | 3.49 ms: 1.01x slower                                                            |
| scimark_monte_carlo        | 87.4 ms                                                                | 88.1 ms: 1.01x slower                                                            |
| connected_components       | 526 ms                                                                 | 530 ms: 1.01x slower                                                             |
| 2to3                       | 310 ms                                                                 | 313 ms: 1.01x slower                                                             |
| go                         | 143 ms                                                                 | 145 ms: 1.01x slower                                                             |
| python_startup             | 14.9 ms                                                                | 15.1 ms: 1.01x slower                                                            |
| sympy_str                  | 320 ms                                                                 | 323 ms: 1.01x slower                                                             |
| thrift                     | 954 us                                                                 | 963 us: 1.01x slower                                                             |
| richards                   | 54.4 ms                                                                | 54.9 ms: 1.01x slower                                                            |
| python_startup_no_site     | 9.28 ms                                                                | 9.37 ms: 1.01x slower                                                            |
| richards_super             | 63.4 ms                                                                | 64.0 ms: 1.01x slower                                                            |
| float                      | 78.1 ms                                                                | 78.9 ms: 1.01x slower                                                            |
| xml_etree_parse            | 148 ms                                                                 | 150 ms: 1.01x slower                                                             |
| shortest_path              | 567 ms                                                                 | 573 ms: 1.01x slower                                                             |
| scimark_fft                | 420 ms                                                                 | 425 ms: 1.01x slower                                                             |
| bench_mp_pool              | 88.8 ms                                                                | 89.8 ms: 1.01x slower                                                            |
| mako                       | 16.3 ms                                                                | 16.5 ms: 1.01x slower                                                            |
| async_tree_io_tg           | 544 ms                                                                 | 551 ms: 1.01x slower                                                             |
| sqlglot_optimize           | 61.2 ms                                                                | 62.0 ms: 1.01x slower                                                            |
| async_tree_cpu_io_mixed_tg | 463 ms                                                                 | 469 ms: 1.01x slower                                                             |
| sympy_integrate            | 23.8 ms                                                                | 24.1 ms: 1.01x slower                                                            |
| pprint_safe_repr           | 854 ms                                                                 | 866 ms: 1.01x slower                                                             |
| spectral_norm              | 118 ms                                                                 | 119 ms: 1.01x slower                                                             |
| sympy_sum                  | 177 ms                                                                 | 180 ms: 1.01x slower                                                             |
| create_gc_cycles           | 1.69 ms                                                                | 1.71 ms: 1.01x slower                                                            |
| logging_silent             | 119 ns                                                                 | 120 ns: 1.01x slower                                                             |
| many_optionals             | 1.09 ms                                                                | 1.11 ms: 1.01x slower                                                            |
| sympy_expand               | 533 ms                                                                 | 541 ms: 1.02x slower                                                             |
| fannkuch                   | 513 ms                                                                 | 521 ms: 1.02x slower                                                             |
| deepcopy                   | 314 us                                                                 | 319 us: 1.02x slower                                                             |
| sphinx                     | 1.13 sec                                                               | 1.15 sec: 1.02x slower                                                           |
| sqlglot_normalize          | 120 ms                                                                 | 122 ms: 1.02x slower                                                             |
| docutils                   | 2.82 sec                                                               | 2.87 sec: 1.02x slower                                                           |
| regex_compile              | 150 ms                                                                 | 153 ms: 1.02x slower                                                             |
| pprint_pformat             | 1.75 sec                                                               | 1.79 sec: 1.02x slower                                                           |
| xml_etree_iterparse        | 94.3 ms                                                                | 96.4 ms: 1.02x slower                                                            |
| async_tree_none_tg         | 236 ms                                                                 | 241 ms: 1.02x slower                                                             |
| pickle_pure_python         | 374 us                                                                 | 382 us: 1.02x slower                                                             |
| subparsers                 | 24.5 ms                                                                | 25.0 ms: 1.02x slower                                                            |
| typing_runtime_protocols   | 212 us                                                                 | 216 us: 1.02x slower                                                             |
| dulwich_log                | 69.2 ms                                                                | 71.3 ms: 1.03x slower                                                            |
| html5lib                   | 69.1 ms                                                                | 71.2 ms: 1.03x slower                                                            |
| genshi_xml                 | 60.9 ms                                                                | 62.8 ms: 1.03x slower                                                            |
| genshi_text                | 28.4 ms                                                                | 29.3 ms: 1.03x slower                                                            |
| tomli_loads                | 2.37 sec                                                               | 2.45 sec: 1.03x slower                                                           |
| sqlalchemy_imperative      | 20.8 ms                                                                | 21.5 ms: 1.04x slower                                                            |
| pidigits                   | 181 ms                                                                 | 190 ms: 1.05x slower                                                             |
| logging_simple             | 6.69 us                                                                | 7.01 us: 1.05x slower                                                            |
| unpickle_pure_python       | 259 us                                                                 | 273 us: 1.05x slower                                                             |
| xml_etree_process          | 68.5 ms                                                                | 72.1 ms: 1.05x slower                                                            |
| logging_format             | 7.61 us                                                                | 8.02 us: 1.05x slower                                                            |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (24): coverage, json, scimark_lu, json_dumps, pathlib, nqueens, json_loads, deepcopy_reduce, sqlite_synth, k_core, scimark_sor, xml_etree_generate, telco, django_template, asyncio_websockets, sqlalchemy_declarative, pylint, sqlglot_parse, sqlglot_transpile, async_tree_io, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none, async_tree_memoization_tg

- Geometric mean (including insignificant results): 1.008x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x