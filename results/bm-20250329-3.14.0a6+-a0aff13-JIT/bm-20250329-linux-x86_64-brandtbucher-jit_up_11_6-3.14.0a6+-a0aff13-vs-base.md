# Results vs. base

- fork: brandtbucher
- ref: jit_up_11_6
- machine: linux-x86_64
- commit hash: a0aff13
- commit date: 2025-03-29
- overall geometric mean: 1.004x slower
- HPT reliability: 87.39%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250329-linux-x86_64-brandtbucher-jit_up_11_6-3.14.0a6+-a0aff13 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 263 ms                                                                 | 265 ms: 1.01x slower                                                |
| docutils       | 2.69 sec                                                               | 2.71 sec: 1.01x slower                                              |
| html5lib       | 63.2 ms                                                                | 61.9 ms: 1.02x faster                                               |
| sphinx         | 1.02 sec                                                               | 1.04 sec: 1.01x slower                                              |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250329-linux-x86_64-brandtbucher-jit_up_11_6-3.14.0a6+-a0aff13 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none            | 266 ms                                                                 | 260 ms: 1.02x faster                                                |
| async_tree_none_tg         | 255 ms                                                                 | 251 ms: 1.02x faster                                                |
| async_tree_cpu_io_mixed_tg | 479 ms                                                                 | 473 ms: 1.01x faster                                                |
| coroutines                 | 24.1 ms                                                                | 23.8 ms: 1.01x faster                                               |
| async_tree_memoization     | 319 ms                                                                 | 316 ms: 1.01x faster                                                |
| async_generators           | 418 ms                                                                 | 415 ms: 1.01x faster                                                |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (5): async_tree_memoization_tg, async_tree_io, async_tree_io_tg, async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250329-linux-x86_64-brandtbucher-jit_up_11_6-3.14.0a6+-a0aff13 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 89.4 ms                                                                | 86.8 ms: 1.03x faster                                               |
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x faster                                                |
| float          | 64.9 ms                                                                | 65.7 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250329-linux-x86_64-brandtbucher-jit_up_11_6-3.14.0a6+-a0aff13 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 128 ms                                                                 | 129 ms: 1.01x slower                                                |
| regex_dna      | 217 ms                                                                 | 226 ms: 1.04x slower                                                |
| regex_effbot   | 3.16 ms                                                                | 3.36 ms: 1.06x slower                                               |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                        |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250329-linux-x86_64-brandtbucher-jit_up_11_6-3.14.0a6+-a0aff13 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_pure_python | 214 us                                                                 | 211 us: 1.01x faster                                                |
| xml_etree_parse      | 140 ms                                                                 | 139 ms: 1.01x faster                                                |
| xml_etree_iterparse  | 97.6 ms                                                                | 98.0 ms: 1.00x slower                                               |
| tomli_loads          | 1.87 sec                                                               | 1.88 sec: 1.01x slower                                              |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (5): xml_etree_process, xml_etree_generate, json_loads, pickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250329-linux-x86_64-brandtbucher-jit_up_11_6-3.14.0a6+-a0aff13 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                               |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250329-linux-x86_64-brandtbucher-jit_up_11_6-3.14.0a6+-a0aff13 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako           | 11.0 ms                                                                | 11.0 ms: 1.00x faster                                               |
| genshi_xml     | 49.8 ms                                                                | 50.2 ms: 1.01x slower                                               |
| genshi_text    | 21.4 ms                                                                | 21.7 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250329-linux-x86_64-brandtbucher-jit_up_11_6-3.14.0a6+-a0aff13 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| gc_traversal               | 5.05 ms                                                                | 4.65 ms: 1.09x faster                                               |
| crypto_pyaes               | 78.3 ms                                                                | 75.8 ms: 1.03x faster                                               |
| nbody                      | 89.4 ms                                                                | 86.8 ms: 1.03x faster                                               |
| pprint_safe_repr           | 756 ms                                                                 | 738 ms: 1.03x faster                                                |
| html5lib                   | 63.2 ms                                                                | 61.9 ms: 1.02x faster                                               |
| async_tree_none            | 266 ms                                                                 | 260 ms: 1.02x faster                                                |
| async_tree_none_tg         | 255 ms                                                                 | 251 ms: 1.02x faster                                                |
| generators                 | 29.2 ms                                                                | 28.8 ms: 1.01x faster                                               |
| async_tree_cpu_io_mixed_tg | 479 ms                                                                 | 473 ms: 1.01x faster                                                |
| coroutines                 | 24.1 ms                                                                | 23.8 ms: 1.01x faster                                               |
| unpickle_pure_python       | 214 us                                                                 | 211 us: 1.01x faster                                                |
| xml_etree_parse            | 140 ms                                                                 | 139 ms: 1.01x faster                                                |
| subparsers                 | 21.0 ms                                                                | 20.8 ms: 1.01x faster                                               |
| async_tree_memoization     | 319 ms                                                                 | 316 ms: 1.01x faster                                                |
| shortest_path              | 494 ms                                                                 | 490 ms: 1.01x faster                                                |
| create_gc_cycles           | 2.48 ms                                                                | 2.47 ms: 1.01x faster                                               |
| scimark_lu                 | 118 ms                                                                 | 117 ms: 1.01x faster                                                |
| chaos                      | 60.3 ms                                                                | 60.0 ms: 1.01x faster                                               |
| async_generators           | 418 ms                                                                 | 415 ms: 1.01x faster                                                |
| raytrace                   | 269 ms                                                                 | 268 ms: 1.00x faster                                                |
| mako                       | 11.0 ms                                                                | 11.0 ms: 1.00x faster                                               |
| scimark_fft                | 312 ms                                                                 | 311 ms: 1.00x faster                                                |
| pidigits                   | 186 ms                                                                 | 186 ms: 1.00x faster                                                |
| python_startup             | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                               |
| deepcopy_memo              | 29.0 us                                                                | 29.1 us: 1.00x slower                                               |
| connected_components       | 454 ms                                                                 | 455 ms: 1.00x slower                                                |
| deltablue                  | 3.06 ms                                                                | 3.07 ms: 1.00x slower                                               |
| xml_etree_iterparse        | 97.6 ms                                                                | 98.0 ms: 1.00x slower                                               |
| sqlglot_v2_optimize        | 54.1 ms                                                                | 54.5 ms: 1.01x slower                                               |
| regex_compile              | 128 ms                                                                 | 129 ms: 1.01x slower                                                |
| bench_thread_pool          | 882 us                                                                 | 887 us: 1.01x slower                                                |
| genshi_xml                 | 49.8 ms                                                                | 50.2 ms: 1.01x slower                                               |
| coverage                   | 85.5 ms                                                                | 86.2 ms: 1.01x slower                                               |
| 2to3                       | 263 ms                                                                 | 265 ms: 1.01x slower                                                |
| docutils                   | 2.69 sec                                                               | 2.71 sec: 1.01x slower                                              |
| sympy_str                  | 274 ms                                                                 | 277 ms: 1.01x slower                                                |
| sqlglot_v2_parse           | 1.29 ms                                                                | 1.30 ms: 1.01x slower                                               |
| tomli_loads                | 1.87 sec                                                               | 1.88 sec: 1.01x slower                                              |
| sqlalchemy_imperative      | 17.1 ms                                                                | 17.2 ms: 1.01x slower                                               |
| go                         | 128 ms                                                                 | 130 ms: 1.01x slower                                                |
| genshi_text                | 21.4 ms                                                                | 21.7 ms: 1.01x slower                                               |
| float                      | 64.9 ms                                                                | 65.7 ms: 1.01x slower                                               |
| logging_simple             | 5.59 us                                                                | 5.65 us: 1.01x slower                                               |
| sphinx                     | 1.02 sec                                                               | 1.04 sec: 1.01x slower                                              |
| many_optionals             | 970 us                                                                 | 982 us: 1.01x slower                                                |
| typing_runtime_protocols   | 167 us                                                                 | 169 us: 1.01x slower                                                |
| mdp                        | 2.48 sec                                                               | 2.51 sec: 1.01x slower                                              |
| sympy_integrate            | 20.0 ms                                                                | 20.3 ms: 1.01x slower                                               |
| bpe_tokeniser              | 4.57 sec                                                               | 4.64 sec: 1.01x slower                                              |
| scimark_sparse_mat_mult    | 4.61 ms                                                                | 4.68 ms: 1.01x slower                                               |
| sqlglot_v2_normalize       | 107 ms                                                                 | 109 ms: 1.01x slower                                                |
| logging_format             | 6.16 us                                                                | 6.26 us: 1.02x slower                                               |
| meteor_contest             | 108 ms                                                                 | 110 ms: 1.02x slower                                                |
| deepcopy                   | 260 us                                                                 | 264 us: 1.02x slower                                                |
| sqlglot_v2_transpile       | 1.61 ms                                                                | 1.63 ms: 1.02x slower                                               |
| sympy_sum                  | 152 ms                                                                 | 154 ms: 1.02x slower                                                |
| scimark_sor                | 119 ms                                                                 | 121 ms: 1.02x slower                                                |
| json                       | 5.29 ms                                                                | 5.40 ms: 1.02x slower                                               |
| nqueens                    | 84.9 ms                                                                | 86.7 ms: 1.02x slower                                               |
| deepcopy_reduce            | 2.66 us                                                                | 2.73 us: 1.03x slower                                               |
| sqlalchemy_declarative     | 133 ms                                                                 | 136 ms: 1.03x slower                                                |
| logging_silent             | 95.7 ns                                                                | 99.6 ns: 1.04x slower                                               |
| richards_super             | 41.1 ms                                                                | 42.8 ms: 1.04x slower                                               |
| regex_dna                  | 217 ms                                                                 | 226 ms: 1.04x slower                                                |
| richards                   | 35.8 ms                                                                | 37.7 ms: 1.05x slower                                               |
| pycparser                  | 1.13 sec                                                               | 1.19 sec: 1.06x slower                                              |
| pyflate                    | 432 ms                                                                 | 458 ms: 1.06x slower                                                |
| regex_effbot               | 3.16 ms                                                                | 3.36 ms: 1.06x slower                                               |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (28): async_tree_memoization_tg, telco, async_tree_io, spectral_norm, thrift, async_tree_io_tg, xml_etree_process, sqlite_synth, xml_etree_generate, async_tree_cpu_io_mixed, json_loads, bench_mp_pool, pprint_pformat, asyncio_websockets, scimark_monte_carlo, sympy_expand, django_template, k_core, comprehensions, python_startup_no_site, dulwich_log, fannkuch, pathlib, pickle_pure_python, json_dumps, regex_v8, hexiom, pylint

- Geometric mean (including insignificant results): 1.004x slower

# HPT report

- Reliability score: 87.39% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x