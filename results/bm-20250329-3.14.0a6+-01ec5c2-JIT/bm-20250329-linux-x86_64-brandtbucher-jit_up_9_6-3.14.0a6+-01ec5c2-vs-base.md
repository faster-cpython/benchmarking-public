# Results vs. base

- fork: brandtbucher
- ref: jit_up_9_6
- machine: linux-x86_64
- commit hash: 01ec5c2
- commit date: 2025-03-29
- overall geometric mean: 1.006x slower
- HPT reliability: 99.90%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250329-linux-x86_64-brandtbucher-jit_up_9_6-3.14.0a6+-01ec5c2 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 263 ms                                                                 | 270 ms: 1.03x slower                                               |
| docutils       | 2.69 sec                                                               | 2.73 sec: 1.02x slower                                             |
| sphinx         | 1.02 sec                                                               | 1.04 sec: 1.02x slower                                             |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                       |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250329-linux-x86_64-brandtbucher-jit_up_9_6-3.14.0a6+-01ec5c2 |
|----------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| coroutines                 | 24.1 ms                                                                | 23.3 ms: 1.03x faster                                              |
| async_generators           | 418 ms                                                                 | 415 ms: 1.01x faster                                               |
| asyncio_websockets         | 552 ms                                                                 | 555 ms: 1.00x slower                                               |
| async_tree_cpu_io_mixed_tg | 479 ms                                                                 | 484 ms: 1.01x slower                                               |
| async_tree_cpu_io_mixed    | 492 ms                                                                 | 504 ms: 1.03x slower                                               |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                       |

Benchmark hidden because not significant (6): async_tree_none, async_tree_memoization_tg, async_tree_none_tg, async_tree_io, async_tree_memoization, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250329-linux-x86_64-brandtbucher-jit_up_9_6-3.14.0a6+-01ec5c2 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 89.4 ms                                                                | 87.6 ms: 1.02x faster                                              |
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x slower                                               |
| float          | 64.9 ms                                                                | 65.8 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250329-linux-x86_64-brandtbucher-jit_up_9_6-3.14.0a6+-01ec5c2 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 23.5 ms                                                                | 23.2 ms: 1.01x faster                                              |
| regex_dna      | 217 ms                                                                 | 216 ms: 1.00x faster                                               |
| regex_compile  | 128 ms                                                                 | 130 ms: 1.02x slower                                               |
| regex_effbot   | 3.16 ms                                                                | 3.40 ms: 1.08x slower                                              |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250329-linux-x86_64-brandtbucher-jit_up_9_6-3.14.0a6+-01ec5c2 |
|---------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| xml_etree_generate  | 80.8 ms                                                                | 80.1 ms: 1.01x faster                                              |
| json_loads          | 30.1 us                                                                | 29.9 us: 1.01x faster                                              |
| xml_etree_iterparse | 97.6 ms                                                                | 98.0 ms: 1.00x slower                                              |
| tomli_loads         | 1.87 sec                                                               | 1.89 sec: 1.01x slower                                             |
| Geometric mean      | (ref)                                                                  | 1.00x slower                                                       |

Benchmark hidden because not significant (5): xml_etree_parse, xml_etree_process, json_dumps, pickle_pure_python, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250329-linux-x86_64-brandtbucher-jit_up_9_6-3.14.0a6+-01ec5c2 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 8.19 ms                                                                | 8.18 ms: 1.00x faster                                              |
| python_startup         | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                              |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250329-linux-x86_64-brandtbucher-jit_up_9_6-3.14.0a6+-01ec5c2 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| mako           | 11.0 ms                                                                | 11.0 ms: 1.00x faster                                              |
| genshi_xml     | 49.8 ms                                                                | 50.1 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                       |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250329-linux-x86_64-brandtbucher-jit_up_9_6-3.14.0a6+-01ec5c2 |
|----------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| gc_traversal               | 5.05 ms                                                                | 4.83 ms: 1.05x faster                                              |
| crypto_pyaes               | 78.3 ms                                                                | 75.4 ms: 1.04x faster                                              |
| coroutines                 | 24.1 ms                                                                | 23.3 ms: 1.03x faster                                              |
| deepcopy_memo              | 29.0 us                                                                | 28.2 us: 1.03x faster                                              |
| nbody                      | 89.4 ms                                                                | 87.6 ms: 1.02x faster                                              |
| comprehensions             | 19.0 us                                                                | 18.7 us: 1.01x faster                                              |
| shortest_path              | 494 ms                                                                 | 489 ms: 1.01x faster                                               |
| regex_v8                   | 23.5 ms                                                                | 23.2 ms: 1.01x faster                                              |
| generators                 | 29.2 ms                                                                | 29.0 ms: 1.01x faster                                              |
| xml_etree_generate         | 80.8 ms                                                                | 80.1 ms: 1.01x faster                                              |
| json_loads                 | 30.1 us                                                                | 29.9 us: 1.01x faster                                              |
| async_generators           | 418 ms                                                                 | 415 ms: 1.01x faster                                               |
| connected_components       | 454 ms                                                                 | 451 ms: 1.00x faster                                               |
| mako                       | 11.0 ms                                                                | 11.0 ms: 1.00x faster                                              |
| regex_dna                  | 217 ms                                                                 | 216 ms: 1.00x faster                                               |
| python_startup_no_site     | 8.19 ms                                                                | 8.18 ms: 1.00x faster                                              |
| python_startup             | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                              |
| pidigits                   | 186 ms                                                                 | 186 ms: 1.00x slower                                               |
| asyncio_websockets         | 552 ms                                                                 | 555 ms: 1.00x slower                                               |
| xml_etree_iterparse        | 97.6 ms                                                                | 98.0 ms: 1.00x slower                                              |
| bpe_tokeniser              | 4.57 sec                                                               | 4.59 sec: 1.00x slower                                             |
| sympy_expand               | 475 ms                                                                 | 477 ms: 1.01x slower                                               |
| genshi_xml                 | 49.8 ms                                                                | 50.1 ms: 1.01x slower                                              |
| raytrace                   | 269 ms                                                                 | 270 ms: 1.01x slower                                               |
| chaos                      | 60.3 ms                                                                | 60.7 ms: 1.01x slower                                              |
| pyflate                    | 432 ms                                                                 | 434 ms: 1.01x slower                                               |
| meteor_contest             | 108 ms                                                                 | 109 ms: 1.01x slower                                               |
| scimark_lu                 | 118 ms                                                                 | 119 ms: 1.01x slower                                               |
| deepcopy                   | 260 us                                                                 | 262 us: 1.01x slower                                               |
| async_tree_cpu_io_mixed_tg | 479 ms                                                                 | 484 ms: 1.01x slower                                               |
| bench_thread_pool          | 882 us                                                                 | 891 us: 1.01x slower                                               |
| mdp                        | 2.48 sec                                                               | 2.50 sec: 1.01x slower                                             |
| tomli_loads                | 1.87 sec                                                               | 1.89 sec: 1.01x slower                                             |
| sympy_str                  | 274 ms                                                                 | 278 ms: 1.01x slower                                               |
| typing_runtime_protocols   | 167 us                                                                 | 169 us: 1.01x slower                                               |
| go                         | 128 ms                                                                 | 130 ms: 1.01x slower                                               |
| float                      | 64.9 ms                                                                | 65.8 ms: 1.01x slower                                              |
| logging_simple             | 5.59 us                                                                | 5.66 us: 1.01x slower                                              |
| scimark_fft                | 312 ms                                                                 | 316 ms: 1.01x slower                                               |
| docutils                   | 2.69 sec                                                               | 2.73 sec: 1.02x slower                                             |
| sphinx                     | 1.02 sec                                                               | 1.04 sec: 1.02x slower                                             |
| spectral_norm              | 97.1 ms                                                                | 98.7 ms: 1.02x slower                                              |
| pprint_pformat             | 1.55 sec                                                               | 1.58 sec: 1.02x slower                                             |
| hexiom                     | 6.86 ms                                                                | 6.99 ms: 1.02x slower                                              |
| regex_compile              | 128 ms                                                                 | 130 ms: 1.02x slower                                               |
| sympy_integrate            | 20.0 ms                                                                | 20.5 ms: 1.02x slower                                              |
| sqlglot_v2_parse           | 1.29 ms                                                                | 1.31 ms: 1.02x slower                                              |
| sqlglot_v2_optimize        | 54.1 ms                                                                | 55.4 ms: 1.02x slower                                              |
| sympy_sum                  | 152 ms                                                                 | 155 ms: 1.02x slower                                               |
| deepcopy_reduce            | 2.66 us                                                                | 2.73 us: 1.03x slower                                              |
| async_tree_cpu_io_mixed    | 492 ms                                                                 | 504 ms: 1.03x slower                                               |
| 2to3                       | 263 ms                                                                 | 270 ms: 1.03x slower                                               |
| sqlglot_v2_normalize       | 107 ms                                                                 | 110 ms: 1.03x slower                                               |
| sqlglot_v2_transpile       | 1.61 ms                                                                | 1.65 ms: 1.03x slower                                              |
| sqlalchemy_imperative      | 17.1 ms                                                                | 17.6 ms: 1.03x slower                                              |
| logging_silent             | 95.7 ns                                                                | 98.6 ns: 1.03x slower                                              |
| scimark_sparse_mat_mult    | 4.61 ms                                                                | 4.76 ms: 1.03x slower                                              |
| many_optionals             | 970 us                                                                 | 1.00 ms: 1.03x slower                                              |
| scimark_sor                | 119 ms                                                                 | 123 ms: 1.04x slower                                               |
| telco                      | 7.93 ms                                                                | 8.25 ms: 1.04x slower                                              |
| sqlalchemy_declarative     | 133 ms                                                                 | 141 ms: 1.06x slower                                               |
| pycparser                  | 1.13 sec                                                               | 1.20 sec: 1.06x slower                                             |
| regex_effbot               | 3.16 ms                                                                | 3.40 ms: 1.08x slower                                              |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                       |

Benchmark hidden because not significant (33): async_tree_none, richards_super, async_tree_memoization_tg, async_tree_none_tg, pathlib, subparsers, html5lib, xml_etree_parse, async_tree_io, coverage, xml_etree_process, pprint_safe_repr, genshi_text, deltablue, scimark_monte_carlo, create_gc_cycles, sqlite_synth, k_core, async_tree_memoization, json_dumps, richards, dulwich_log, fannkuch, json, nqueens, logging_format, bench_mp_pool, django_template, pickle_pure_python, async_tree_io_tg, thrift, unpickle_pure_python, pylint

- Geometric mean (including insignificant results): 1.006x slower

# HPT report

- Reliability score: 99.90% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x