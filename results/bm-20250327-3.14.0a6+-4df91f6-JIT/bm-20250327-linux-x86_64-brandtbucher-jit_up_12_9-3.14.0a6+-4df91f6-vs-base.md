# Results vs. base

- fork: brandtbucher
- ref: jit_up_12_9
- machine: linux-x86_64
- commit hash: 4df91f6
- commit date: 2025-03-27
- overall geometric mean: 1.004x slower
- HPT reliability: 91.41%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250327-linux-x86_64-brandtbucher-jit_up_12_9-3.14.0a6+-4df91f6 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 263 ms                                                                 | 265 ms: 1.01x slower                                                |
| docutils       | 2.69 sec                                                               | 2.72 sec: 1.01x slower                                              |
| html5lib       | 63.2 ms                                                                | 62.3 ms: 1.01x faster                                               |
| sphinx         | 1.02 sec                                                               | 1.04 sec: 1.01x slower                                              |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250327-linux-x86_64-brandtbucher-jit_up_12_9-3.14.0a6+-4df91f6 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none_tg         | 255 ms                                                                 | 253 ms: 1.01x faster                                                |
| async_tree_cpu_io_mixed_tg | 479 ms                                                                 | 475 ms: 1.01x faster                                                |
| async_tree_memoization     | 319 ms                                                                 | 317 ms: 1.01x faster                                                |
| coroutines                 | 24.1 ms                                                                | 24.6 ms: 1.02x slower                                               |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (7): async_tree_io_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_io, async_generators, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250327-linux-x86_64-brandtbucher-jit_up_12_9-3.14.0a6+-4df91f6 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 89.4 ms                                                                | 86.8 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250327-linux-x86_64-brandtbucher-jit_up_12_9-3.14.0a6+-4df91f6 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 23.5 ms                                                                | 23.1 ms: 1.02x faster                                               |
| regex_compile  | 128 ms                                                                 | 128 ms: 1.00x slower                                                |
| regex_dna      | 217 ms                                                                 | 220 ms: 1.01x slower                                                |
| regex_effbot   | 3.16 ms                                                                | 3.51 ms: 1.11x slower                                               |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250327-linux-x86_64-brandtbucher-jit_up_12_9-3.14.0a6+-4df91f6 |
|--------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_parse    | 140 ms                                                                 | 139 ms: 1.01x faster                                                |
| pickle_pure_python | 325 us                                                                 | 330 us: 1.01x slower                                                |
| Geometric mean     | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (7): json_loads, unpickle_pure_python, xml_etree_iterparse, xml_etree_process, json_dumps, xml_etree_generate, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250327-linux-x86_64-brandtbucher-jit_up_12_9-3.14.0a6+-4df91f6 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                               |
| python_startup_no_site | 8.19 ms                                                                | 8.19 ms: 1.00x slower                                               |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250327-linux-x86_64-brandtbucher-jit_up_12_9-3.14.0a6+-4df91f6 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml     | 49.8 ms                                                                | 50.1 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (3): django_template, genshi_text, mako

All benchmarks:
===============

| Benchmark                  | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250327-linux-x86_64-brandtbucher-jit_up_12_9-3.14.0a6+-4df91f6 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| gc_traversal               | 5.05 ms                                                                | 4.81 ms: 1.05x faster                                               |
| nbody                      | 89.4 ms                                                                | 86.8 ms: 1.03x faster                                               |
| generators                 | 29.2 ms                                                                | 28.6 ms: 1.02x faster                                               |
| regex_v8                   | 23.5 ms                                                                | 23.1 ms: 1.02x faster                                               |
| spectral_norm              | 97.1 ms                                                                | 95.5 ms: 1.02x faster                                               |
| html5lib                   | 63.2 ms                                                                | 62.3 ms: 1.01x faster                                               |
| comprehensions             | 19.0 us                                                                | 18.7 us: 1.01x faster                                               |
| async_tree_none_tg         | 255 ms                                                                 | 253 ms: 1.01x faster                                                |
| async_tree_cpu_io_mixed_tg | 479 ms                                                                 | 475 ms: 1.01x faster                                                |
| async_tree_memoization     | 319 ms                                                                 | 317 ms: 1.01x faster                                                |
| sqlite_synth               | 2.72 us                                                                | 2.70 us: 1.01x faster                                               |
| shortest_path              | 494 ms                                                                 | 491 ms: 1.01x faster                                                |
| scimark_fft                | 312 ms                                                                 | 310 ms: 1.01x faster                                                |
| xml_etree_parse            | 140 ms                                                                 | 139 ms: 1.01x faster                                                |
| bench_mp_pool              | 83.3 ms                                                                | 82.8 ms: 1.01x faster                                               |
| chaos                      | 60.3 ms                                                                | 60.1 ms: 1.00x faster                                               |
| hexiom                     | 6.86 ms                                                                | 6.83 ms: 1.00x faster                                               |
| raytrace                   | 269 ms                                                                 | 268 ms: 1.00x faster                                                |
| pathlib                    | 16.8 ms                                                                | 16.7 ms: 1.00x faster                                               |
| meteor_contest             | 108 ms                                                                 | 108 ms: 1.00x faster                                                |
| create_gc_cycles           | 2.48 ms                                                                | 2.48 ms: 1.00x faster                                               |
| python_startup             | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                               |
| python_startup_no_site     | 8.19 ms                                                                | 8.19 ms: 1.00x slower                                               |
| bench_thread_pool          | 882 us                                                                 | 883 us: 1.00x slower                                                |
| regex_compile              | 128 ms                                                                 | 128 ms: 1.00x slower                                                |
| sympy_integrate            | 20.0 ms                                                                | 20.1 ms: 1.01x slower                                               |
| genshi_xml                 | 49.8 ms                                                                | 50.1 ms: 1.01x slower                                               |
| sympy_str                  | 274 ms                                                                 | 276 ms: 1.01x slower                                                |
| sqlglot_v2_transpile       | 1.61 ms                                                                | 1.62 ms: 1.01x slower                                               |
| sqlalchemy_declarative     | 133 ms                                                                 | 134 ms: 1.01x slower                                                |
| crypto_pyaes               | 78.3 ms                                                                | 79.0 ms: 1.01x slower                                               |
| bpe_tokeniser              | 4.57 sec                                                               | 4.61 sec: 1.01x slower                                              |
| 2to3                       | 263 ms                                                                 | 265 ms: 1.01x slower                                                |
| go                         | 128 ms                                                                 | 129 ms: 1.01x slower                                                |
| many_optionals             | 970 us                                                                 | 980 us: 1.01x slower                                                |
| logging_simple             | 5.59 us                                                                | 5.64 us: 1.01x slower                                               |
| docutils                   | 2.69 sec                                                               | 2.72 sec: 1.01x slower                                              |
| pprint_pformat             | 1.55 sec                                                               | 1.57 sec: 1.01x slower                                              |
| sqlglot_v2_optimize        | 54.1 ms                                                                | 54.8 ms: 1.01x slower                                               |
| sqlglot_v2_parse           | 1.29 ms                                                                | 1.30 ms: 1.01x slower                                               |
| sphinx                     | 1.02 sec                                                               | 1.04 sec: 1.01x slower                                              |
| sqlglot_v2_normalize       | 107 ms                                                                 | 109 ms: 1.01x slower                                                |
| pickle_pure_python         | 325 us                                                                 | 330 us: 1.01x slower                                                |
| regex_dna                  | 217 ms                                                                 | 220 ms: 1.01x slower                                                |
| logging_format             | 6.16 us                                                                | 6.25 us: 1.01x slower                                               |
| scimark_sparse_mat_mult    | 4.61 ms                                                                | 4.68 ms: 1.02x slower                                               |
| sqlalchemy_imperative      | 17.1 ms                                                                | 17.4 ms: 1.02x slower                                               |
| sympy_sum                  | 152 ms                                                                 | 154 ms: 1.02x slower                                                |
| richards_super             | 41.1 ms                                                                | 41.9 ms: 1.02x slower                                               |
| coroutines                 | 24.1 ms                                                                | 24.6 ms: 1.02x slower                                               |
| mdp                        | 2.48 sec                                                               | 2.53 sec: 1.02x slower                                              |
| pprint_safe_repr           | 756 ms                                                                 | 773 ms: 1.02x slower                                                |
| nqueens                    | 84.9 ms                                                                | 87.1 ms: 1.03x slower                                               |
| deepcopy_reduce            | 2.66 us                                                                | 2.73 us: 1.03x slower                                               |
| pyflate                    | 432 ms                                                                 | 448 ms: 1.04x slower                                                |
| logging_silent             | 95.7 ns                                                                | 99.5 ns: 1.04x slower                                               |
| richards                   | 35.8 ms                                                                | 37.5 ms: 1.05x slower                                               |
| pycparser                  | 1.13 sec                                                               | 1.20 sec: 1.06x slower                                              |
| regex_effbot               | 3.16 ms                                                                | 3.51 ms: 1.11x slower                                               |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (37): async_tree_io_tg, coverage, async_tree_memoization_tg, json_loads, fannkuch, thrift, async_tree_cpu_io_mixed, scimark_lu, async_tree_none, async_tree_io, subparsers, sympy_expand, django_template, unpickle_pure_python, xml_etree_iterparse, async_generators, pidigits, deltablue, xml_etree_process, deepcopy_memo, pylint, asyncio_websockets, genshi_text, dulwich_log, json_dumps, deepcopy, float, telco, xml_etree_generate, mako, scimark_monte_carlo, tomli_loads, scimark_sor, connected_components, k_core, typing_runtime_protocols, json

- Geometric mean (including insignificant results): 1.004x slower

# HPT report

- Reliability score: 91.41% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x