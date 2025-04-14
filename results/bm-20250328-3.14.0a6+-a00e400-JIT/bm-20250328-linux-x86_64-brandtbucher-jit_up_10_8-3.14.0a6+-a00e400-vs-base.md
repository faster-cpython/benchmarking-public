# Results vs. base

- fork: brandtbucher
- ref: jit_up_10_8
- machine: linux-x86_64
- commit hash: a00e400
- commit date: 2025-03-28
- overall geometric mean: 1.009x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_8-3.14.0a6+-a00e400 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 263 ms                                                                 | 266 ms: 1.01x slower                                                |
| docutils       | 2.69 sec                                                               | 2.70 sec: 1.01x slower                                              |
| html5lib       | 63.2 ms                                                                | 62.5 ms: 1.01x faster                                               |
| sphinx         | 1.02 sec                                                               | 1.04 sec: 1.01x slower                                              |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_8-3.14.0a6+-a00e400 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| coroutines                 | 24.1 ms                                                                | 23.6 ms: 1.02x faster                                               |
| async_tree_none            | 266 ms                                                                 | 262 ms: 1.01x faster                                                |
| async_tree_cpu_io_mixed_tg | 479 ms                                                                 | 475 ms: 1.01x faster                                                |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (8): async_tree_memoization_tg, async_tree_memoization, async_tree_io, async_tree_io_tg, async_tree_none_tg, asyncio_websockets, async_tree_cpu_io_mixed, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_8-3.14.0a6+-a00e400 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 89.4 ms                                                                | 87.3 ms: 1.02x faster                                               |
| pidigits       | 186 ms                                                                 | 185 ms: 1.00x faster                                                |
| float          | 64.9 ms                                                                | 65.4 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_8-3.14.0a6+-a00e400 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 128 ms                                                                 | 129 ms: 1.01x slower                                                |
| regex_v8       | 23.5 ms                                                                | 24.0 ms: 1.02x slower                                               |
| regex_dna      | 217 ms                                                                 | 226 ms: 1.05x slower                                                |
| regex_effbot   | 3.16 ms                                                                | 3.54 ms: 1.12x slower                                               |
| Geometric mean | (ref)                                                                  | 1.05x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_8-3.14.0a6+-a00e400 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_process    | 57.1 ms                                                                | 56.5 ms: 1.01x faster                                               |
| unpickle_pure_python | 214 us                                                                 | 212 us: 1.01x faster                                                |
| xml_etree_parse      | 140 ms                                                                 | 139 ms: 1.01x faster                                                |
| xml_etree_generate   | 80.8 ms                                                                | 80.2 ms: 1.01x faster                                               |
| xml_etree_iterparse  | 97.6 ms                                                                | 98.0 ms: 1.00x slower                                               |
| tomli_loads          | 1.87 sec                                                               | 1.89 sec: 1.01x slower                                              |
| json_dumps           | 11.6 ms                                                                | 11.7 ms: 1.02x slower                                               |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (2): json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_8-3.14.0a6+-a00e400 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 13.1 ms                                                                | 13.2 ms: 1.00x slower                                               |
| python_startup_no_site | 8.19 ms                                                                | 8.23 ms: 1.00x slower                                               |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_8-3.14.0a6+-a00e400 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako           | 11.0 ms                                                                | 11.0 ms: 1.00x faster                                               |
| genshi_text    | 21.4 ms                                                                | 21.6 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_8-3.14.0a6+-a00e400 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| crypto_pyaes               | 78.3 ms                                                                | 75.2 ms: 1.04x faster                                               |
| gc_traversal               | 5.05 ms                                                                | 4.91 ms: 1.03x faster                                               |
| comprehensions             | 19.0 us                                                                | 18.5 us: 1.03x faster                                               |
| nbody                      | 89.4 ms                                                                | 87.3 ms: 1.02x faster                                               |
| telco                      | 7.93 ms                                                                | 7.78 ms: 1.02x faster                                               |
| coroutines                 | 24.1 ms                                                                | 23.6 ms: 1.02x faster                                               |
| async_tree_none            | 266 ms                                                                 | 262 ms: 1.01x faster                                                |
| html5lib                   | 63.2 ms                                                                | 62.5 ms: 1.01x faster                                               |
| xml_etree_process          | 57.1 ms                                                                | 56.5 ms: 1.01x faster                                               |
| unpickle_pure_python       | 214 us                                                                 | 212 us: 1.01x faster                                                |
| async_tree_cpu_io_mixed_tg | 479 ms                                                                 | 475 ms: 1.01x faster                                                |
| scimark_lu                 | 118 ms                                                                 | 117 ms: 1.01x faster                                                |
| xml_etree_parse            | 140 ms                                                                 | 139 ms: 1.01x faster                                                |
| xml_etree_generate         | 80.8 ms                                                                | 80.2 ms: 1.01x faster                                               |
| mako                       | 11.0 ms                                                                | 11.0 ms: 1.00x faster                                               |
| pidigits                   | 186 ms                                                                 | 185 ms: 1.00x faster                                                |
| deepcopy_memo              | 29.0 us                                                                | 29.1 us: 1.00x slower                                               |
| create_gc_cycles           | 2.48 ms                                                                | 2.49 ms: 1.00x slower                                               |
| python_startup             | 13.1 ms                                                                | 13.2 ms: 1.00x slower                                               |
| chaos                      | 60.3 ms                                                                | 60.6 ms: 1.00x slower                                               |
| generators                 | 29.2 ms                                                                | 29.4 ms: 1.00x slower                                               |
| python_startup_no_site     | 8.19 ms                                                                | 8.23 ms: 1.00x slower                                               |
| xml_etree_iterparse        | 97.6 ms                                                                | 98.0 ms: 1.00x slower                                               |
| docutils                   | 2.69 sec                                                               | 2.70 sec: 1.01x slower                                              |
| meteor_contest             | 108 ms                                                                 | 109 ms: 1.01x slower                                                |
| go                         | 128 ms                                                                 | 129 ms: 1.01x slower                                                |
| sympy_expand               | 475 ms                                                                 | 478 ms: 1.01x slower                                                |
| regex_compile              | 128 ms                                                                 | 129 ms: 1.01x slower                                                |
| fannkuch                   | 423 ms                                                                 | 426 ms: 1.01x slower                                                |
| float                      | 64.9 ms                                                                | 65.4 ms: 1.01x slower                                               |
| logging_format             | 6.16 us                                                                | 6.21 us: 1.01x slower                                               |
| logging_simple             | 5.59 us                                                                | 5.63 us: 1.01x slower                                               |
| shortest_path              | 494 ms                                                                 | 498 ms: 1.01x slower                                                |
| bpe_tokeniser              | 4.57 sec                                                               | 4.61 sec: 1.01x slower                                              |
| subparsers                 | 21.0 ms                                                                | 21.2 ms: 1.01x slower                                               |
| genshi_text                | 21.4 ms                                                                | 21.6 ms: 1.01x slower                                               |
| mdp                        | 2.48 sec                                                               | 2.50 sec: 1.01x slower                                              |
| typing_runtime_protocols   | 167 us                                                                 | 169 us: 1.01x slower                                                |
| bench_thread_pool          | 882 us                                                                 | 892 us: 1.01x slower                                                |
| tomli_loads                | 1.87 sec                                                               | 1.89 sec: 1.01x slower                                              |
| sphinx                     | 1.02 sec                                                               | 1.04 sec: 1.01x slower                                              |
| 2to3                       | 263 ms                                                                 | 266 ms: 1.01x slower                                                |
| sympy_integrate            | 20.0 ms                                                                | 20.3 ms: 1.01x slower                                               |
| sqlglot_v2_optimize        | 54.1 ms                                                                | 54.9 ms: 1.01x slower                                               |
| scimark_sor                | 119 ms                                                                 | 120 ms: 1.01x slower                                                |
| sqlglot_v2_parse           | 1.29 ms                                                                | 1.31 ms: 1.02x slower                                               |
| deepcopy_reduce            | 2.66 us                                                                | 2.70 us: 1.02x slower                                               |
| sympy_str                  | 274 ms                                                                 | 279 ms: 1.02x slower                                                |
| thrift                     | 783 us                                                                 | 796 us: 1.02x slower                                                |
| json_dumps                 | 11.6 ms                                                                | 11.7 ms: 1.02x slower                                               |
| spectral_norm              | 97.1 ms                                                                | 98.8 ms: 1.02x slower                                               |
| sqlglot_v2_normalize       | 107 ms                                                                 | 109 ms: 1.02x slower                                                |
| sqlglot_v2_transpile       | 1.61 ms                                                                | 1.64 ms: 1.02x slower                                               |
| scimark_fft                | 312 ms                                                                 | 318 ms: 1.02x slower                                                |
| regex_v8                   | 23.5 ms                                                                | 24.0 ms: 1.02x slower                                               |
| pprint_safe_repr           | 756 ms                                                                 | 774 ms: 1.02x slower                                                |
| sqlalchemy_imperative      | 17.1 ms                                                                | 17.5 ms: 1.02x slower                                               |
| many_optionals             | 970 us                                                                 | 996 us: 1.03x slower                                                |
| sympy_sum                  | 152 ms                                                                 | 156 ms: 1.03x slower                                                |
| sqlalchemy_declarative     | 133 ms                                                                 | 136 ms: 1.03x slower                                                |
| hexiom                     | 6.86 ms                                                                | 7.07 ms: 1.03x slower                                               |
| nqueens                    | 84.9 ms                                                                | 87.5 ms: 1.03x slower                                               |
| richards                   | 35.8 ms                                                                | 37.0 ms: 1.03x slower                                               |
| pyflate                    | 432 ms                                                                 | 447 ms: 1.04x slower                                                |
| scimark_sparse_mat_mult    | 4.61 ms                                                                | 4.79 ms: 1.04x slower                                               |
| logging_silent             | 95.7 ns                                                                | 99.5 ns: 1.04x slower                                               |
| richards_super             | 41.1 ms                                                                | 42.9 ms: 1.04x slower                                               |
| pycparser                  | 1.13 sec                                                               | 1.18 sec: 1.05x slower                                              |
| regex_dna                  | 217 ms                                                                 | 226 ms: 1.05x slower                                                |
| pprint_pformat             | 1.55 sec                                                               | 1.63 sec: 1.05x slower                                              |
| connected_components       | 454 ms                                                                 | 495 ms: 1.09x slower                                                |
| regex_effbot               | 3.16 ms                                                                | 3.54 ms: 1.12x slower                                               |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (24): k_core, async_tree_memoization_tg, json_loads, async_tree_memoization, async_tree_io, deltablue, async_tree_io_tg, async_tree_none_tg, raytrace, dulwich_log, pickle_pure_python, pathlib, json, asyncio_websockets, async_tree_cpu_io_mixed, bench_mp_pool, sqlite_synth, scimark_monte_carlo, async_generators, django_template, genshi_xml, deepcopy, coverage, pylint

- Geometric mean (including insignificant results): 1.009x slower

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x