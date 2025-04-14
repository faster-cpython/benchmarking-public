# Results vs. base

- fork: brandtbucher
- ref: jit_up_10_7
- machine: linux-x86_64
- commit hash: c421917
- commit date: 2025-03-29
- overall geometric mean: 1.006x slower
- HPT reliability: 95.10%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_7-3.14.0a6+-c421917 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 263 ms                                                                 | 267 ms: 1.02x slower                                                |
| docutils       | 2.69 sec                                                               | 2.71 sec: 1.01x slower                                              |
| sphinx         | 1.02 sec                                                               | 1.04 sec: 1.01x slower                                              |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_7-3.14.0a6+-c421917 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| coroutines                 | 24.1 ms                                                                | 23.5 ms: 1.03x faster                                               |
| async_tree_none            | 266 ms                                                                 | 260 ms: 1.02x faster                                                |
| async_tree_memoization     | 319 ms                                                                 | 312 ms: 1.02x faster                                                |
| async_tree_none_tg         | 255 ms                                                                 | 250 ms: 1.02x faster                                                |
| async_tree_cpu_io_mixed_tg | 479 ms                                                                 | 472 ms: 1.02x faster                                                |
| async_tree_cpu_io_mixed    | 492 ms                                                                 | 486 ms: 1.01x faster                                                |
| async_generators           | 418 ms                                                                 | 414 ms: 1.01x faster                                                |
| Geometric mean             | (ref)                                                                  | 1.02x faster                                                        |

Benchmark hidden because not significant (4): async_tree_memoization_tg, async_tree_io_tg, async_tree_io, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_7-3.14.0a6+-c421917 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 185 ms: 1.00x faster                                                |
| float          | 64.9 ms                                                                | 65.5 ms: 1.01x slower                                               |
| nbody          | 89.4 ms                                                                | 90.2 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_7-3.14.0a6+-c421917 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 23.5 ms                                                                | 23.6 ms: 1.00x slower                                               |
| regex_compile  | 128 ms                                                                 | 129 ms: 1.01x slower                                                |
| regex_dna      | 217 ms                                                                 | 221 ms: 1.02x slower                                                |
| regex_effbot   | 3.16 ms                                                                | 3.45 ms: 1.09x slower                                               |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_7-3.14.0a6+-c421917 |
|---------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_process   | 57.1 ms                                                                | 56.3 ms: 1.01x faster                                               |
| xml_etree_generate  | 80.8 ms                                                                | 80.3 ms: 1.01x faster                                               |
| xml_etree_iterparse | 97.6 ms                                                                | 98.1 ms: 1.01x slower                                               |
| tomli_loads         | 1.87 sec                                                               | 1.89 sec: 1.01x slower                                              |
| json_dumps          | 11.6 ms                                                                | 11.7 ms: 1.02x slower                                               |
| Geometric mean      | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (4): unpickle_pure_python, pickle_pure_python, xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_7-3.14.0a6+-c421917 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                               |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_7-3.14.0a6+-c421917 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako           | 11.0 ms                                                                | 11.0 ms: 1.00x faster                                               |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (3): genshi_xml, genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_7-3.14.0a6+-c421917 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| coroutines                 | 24.1 ms                                                                | 23.5 ms: 1.03x faster                                               |
| richards_super             | 41.1 ms                                                                | 40.1 ms: 1.02x faster                                               |
| crypto_pyaes               | 78.3 ms                                                                | 76.4 ms: 1.02x faster                                               |
| async_tree_none            | 266 ms                                                                 | 260 ms: 1.02x faster                                                |
| spectral_norm              | 97.1 ms                                                                | 94.9 ms: 1.02x faster                                               |
| async_tree_memoization     | 319 ms                                                                 | 312 ms: 1.02x faster                                                |
| async_tree_none_tg         | 255 ms                                                                 | 250 ms: 1.02x faster                                                |
| async_tree_cpu_io_mixed_tg | 479 ms                                                                 | 472 ms: 1.02x faster                                                |
| telco                      | 7.93 ms                                                                | 7.82 ms: 1.01x faster                                               |
| gc_traversal               | 5.05 ms                                                                | 4.98 ms: 1.01x faster                                               |
| xml_etree_process          | 57.1 ms                                                                | 56.3 ms: 1.01x faster                                               |
| async_tree_cpu_io_mixed    | 492 ms                                                                 | 486 ms: 1.01x faster                                                |
| async_generators           | 418 ms                                                                 | 414 ms: 1.01x faster                                                |
| deltablue                  | 3.06 ms                                                                | 3.04 ms: 1.01x faster                                               |
| xml_etree_generate         | 80.8 ms                                                                | 80.3 ms: 1.01x faster                                               |
| shortest_path              | 494 ms                                                                 | 492 ms: 1.01x faster                                                |
| bench_mp_pool              | 83.3 ms                                                                | 82.9 ms: 1.01x faster                                               |
| scimark_sor                | 119 ms                                                                 | 118 ms: 1.00x faster                                                |
| dulwich_log                | 60.6 ms                                                                | 60.4 ms: 1.00x faster                                               |
| mako                       | 11.0 ms                                                                | 11.0 ms: 1.00x faster                                               |
| deepcopy_memo              | 29.0 us                                                                | 28.9 us: 1.00x faster                                               |
| pidigits                   | 186 ms                                                                 | 185 ms: 1.00x faster                                                |
| meteor_contest             | 108 ms                                                                 | 108 ms: 1.00x faster                                                |
| python_startup             | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                               |
| create_gc_cycles           | 2.48 ms                                                                | 2.49 ms: 1.00x slower                                               |
| scimark_fft                | 312 ms                                                                 | 313 ms: 1.00x slower                                                |
| regex_v8                   | 23.5 ms                                                                | 23.6 ms: 1.00x slower                                               |
| generators                 | 29.2 ms                                                                | 29.4 ms: 1.01x slower                                               |
| xml_etree_iterparse        | 97.6 ms                                                                | 98.1 ms: 1.01x slower                                               |
| typing_runtime_protocols   | 167 us                                                                 | 168 us: 1.01x slower                                                |
| float                      | 64.9 ms                                                                | 65.5 ms: 1.01x slower                                               |
| json                       | 5.29 ms                                                                | 5.34 ms: 1.01x slower                                               |
| bpe_tokeniser              | 4.57 sec                                                               | 4.61 sec: 1.01x slower                                              |
| subparsers                 | 21.0 ms                                                                | 21.2 ms: 1.01x slower                                               |
| nbody                      | 89.4 ms                                                                | 90.2 ms: 1.01x slower                                               |
| docutils                   | 2.69 sec                                                               | 2.71 sec: 1.01x slower                                              |
| regex_compile              | 128 ms                                                                 | 129 ms: 1.01x slower                                                |
| pyflate                    | 432 ms                                                                 | 436 ms: 1.01x slower                                                |
| tomli_loads                | 1.87 sec                                                               | 1.89 sec: 1.01x slower                                              |
| bench_thread_pool          | 882 us                                                                 | 892 us: 1.01x slower                                                |
| sphinx                     | 1.02 sec                                                               | 1.04 sec: 1.01x slower                                              |
| sympy_expand               | 475 ms                                                                 | 481 ms: 1.01x slower                                                |
| nqueens                    | 84.9 ms                                                                | 86.1 ms: 1.02x slower                                               |
| sympy_str                  | 274 ms                                                                 | 279 ms: 1.02x slower                                                |
| json_dumps                 | 11.6 ms                                                                | 11.7 ms: 1.02x slower                                               |
| 2to3                       | 263 ms                                                                 | 267 ms: 1.02x slower                                                |
| sympy_integrate            | 20.0 ms                                                                | 20.4 ms: 1.02x slower                                               |
| sqlglot_v2_optimize        | 54.1 ms                                                                | 55.2 ms: 1.02x slower                                               |
| pprint_pformat             | 1.55 sec                                                               | 1.58 sec: 1.02x slower                                              |
| regex_dna                  | 217 ms                                                                 | 221 ms: 1.02x slower                                                |
| deepcopy                   | 260 us                                                                 | 266 us: 1.02x slower                                                |
| many_optionals             | 970 us                                                                 | 993 us: 1.02x slower                                                |
| sqlglot_v2_normalize       | 107 ms                                                                 | 110 ms: 1.02x slower                                                |
| sqlglot_v2_parse           | 1.29 ms                                                                | 1.32 ms: 1.03x slower                                               |
| hexiom                     | 6.86 ms                                                                | 7.04 ms: 1.03x slower                                               |
| go                         | 128 ms                                                                 | 132 ms: 1.03x slower                                                |
| sqlglot_v2_transpile       | 1.61 ms                                                                | 1.65 ms: 1.03x slower                                               |
| logging_silent             | 95.7 ns                                                                | 98.5 ns: 1.03x slower                                               |
| sqlalchemy_imperative      | 17.1 ms                                                                | 17.6 ms: 1.03x slower                                               |
| sympy_sum                  | 152 ms                                                                 | 156 ms: 1.03x slower                                                |
| sqlalchemy_declarative     | 133 ms                                                                 | 137 ms: 1.03x slower                                                |
| pprint_safe_repr           | 756 ms                                                                 | 783 ms: 1.04x slower                                                |
| mdp                        | 2.48 sec                                                               | 2.57 sec: 1.04x slower                                              |
| scimark_sparse_mat_mult    | 4.61 ms                                                                | 4.78 ms: 1.04x slower                                               |
| pycparser                  | 1.13 sec                                                               | 1.18 sec: 1.05x slower                                              |
| deepcopy_reduce            | 2.66 us                                                                | 2.80 us: 1.05x slower                                               |
| connected_components       | 454 ms                                                                 | 483 ms: 1.06x slower                                                |
| regex_effbot               | 3.16 ms                                                                | 3.45 ms: 1.09x slower                                               |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (28): async_tree_memoization_tg, async_tree_io_tg, async_tree_io, thrift, fannkuch, logging_simple, genshi_xml, genshi_text, asyncio_websockets, unpickle_pure_python, pickle_pure_python, raytrace, python_startup_no_site, k_core, scimark_lu, logging_format, django_template, chaos, richards, comprehensions, xml_etree_parse, json_loads, coverage, pathlib, html5lib, sqlite_synth, scimark_monte_carlo, pylint

- Geometric mean (including insignificant results): 1.006x slower

# HPT report

- Reliability score: 95.10% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x