# Results vs. base

- fork: brandtbucher
- ref: jit_up_11_8
- machine: linux-x86_64
- commit hash: 414beb9
- commit date: 2025-03-28
- overall geometric mean: 1.003x slower
- HPT reliability: 69.77%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_8-3.14.0a6+-414beb9 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none            | 266 ms                                                                 | 260 ms: 1.02x faster                                                |
| async_tree_none_tg         | 255 ms                                                                 | 250 ms: 1.02x faster                                                |
| async_tree_cpu_io_mixed_tg | 479 ms                                                                 | 470 ms: 1.02x faster                                                |
| async_tree_memoization     | 319 ms                                                                 | 314 ms: 1.01x faster                                                |
| async_tree_cpu_io_mixed    | 492 ms                                                                 | 487 ms: 1.01x faster                                                |
| coroutines                 | 24.1 ms                                                                | 23.8 ms: 1.01x faster                                               |
| async_generators           | 418 ms                                                                 | 414 ms: 1.01x faster                                                |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (4): async_tree_memoization_tg, async_tree_io, async_tree_io_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_8-3.14.0a6+-414beb9 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 89.4 ms                                                                | 88.4 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_8-3.14.0a6+-414beb9 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_dna      | 217 ms                                                                 | 210 ms: 1.03x faster                                                |
| regex_compile  | 128 ms                                                                 | 129 ms: 1.01x slower                                                |
| regex_effbot   | 3.16 ms                                                                | 3.18 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_8-3.14.0a6+-414beb9 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_loads           | 30.1 us                                                                | 29.8 us: 1.01x faster                                               |
| unpickle_pure_python | 214 us                                                                 | 212 us: 1.01x faster                                                |
| json_dumps           | 11.6 ms                                                                | 11.6 ms: 1.01x slower                                               |
| xml_etree_iterparse  | 97.6 ms                                                                | 98.8 ms: 1.01x slower                                               |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (5): xml_etree_parse, xml_etree_generate, xml_etree_process, tomli_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_8-3.14.0a6+-414beb9 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                               |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_8-3.14.0a6+-414beb9 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako           | 11.0 ms                                                                | 10.9 ms: 1.01x faster                                               |
| genshi_text    | 21.4 ms                                                                | 21.6 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_8-3.14.0a6+-414beb9 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| gc_traversal               | 5.05 ms                                                                | 4.82 ms: 1.05x faster                                               |
| crypto_pyaes               | 78.3 ms                                                                | 75.8 ms: 1.03x faster                                               |
| regex_dna                  | 217 ms                                                                 | 210 ms: 1.03x faster                                                |
| spectral_norm              | 97.1 ms                                                                | 94.5 ms: 1.03x faster                                               |
| async_tree_none            | 266 ms                                                                 | 260 ms: 1.02x faster                                                |
| async_tree_none_tg         | 255 ms                                                                 | 250 ms: 1.02x faster                                                |
| async_tree_cpu_io_mixed_tg | 479 ms                                                                 | 470 ms: 1.02x faster                                                |
| fannkuch                   | 423 ms                                                                 | 416 ms: 1.02x faster                                                |
| raytrace                   | 269 ms                                                                 | 265 ms: 1.02x faster                                                |
| nqueens                    | 84.9 ms                                                                | 83.5 ms: 1.02x faster                                               |
| async_tree_memoization     | 319 ms                                                                 | 314 ms: 1.01x faster                                                |
| mako                       | 11.0 ms                                                                | 10.9 ms: 1.01x faster                                               |
| json_loads                 | 30.1 us                                                                | 29.8 us: 1.01x faster                                               |
| unpickle_pure_python       | 214 us                                                                 | 212 us: 1.01x faster                                                |
| nbody                      | 89.4 ms                                                                | 88.4 ms: 1.01x faster                                               |
| telco                      | 7.93 ms                                                                | 7.85 ms: 1.01x faster                                               |
| async_tree_cpu_io_mixed    | 492 ms                                                                 | 487 ms: 1.01x faster                                                |
| coroutines                 | 24.1 ms                                                                | 23.8 ms: 1.01x faster                                               |
| scimark_monte_carlo        | 68.6 ms                                                                | 68.0 ms: 1.01x faster                                               |
| async_generators           | 418 ms                                                                 | 414 ms: 1.01x faster                                                |
| subparsers                 | 21.0 ms                                                                | 20.9 ms: 1.01x faster                                               |
| deltablue                  | 3.06 ms                                                                | 3.03 ms: 1.01x faster                                               |
| generators                 | 29.2 ms                                                                | 29.0 ms: 1.01x faster                                               |
| python_startup             | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                               |
| bench_thread_pool          | 882 us                                                                 | 884 us: 1.00x slower                                                |
| dulwich_log                | 60.6 ms                                                                | 60.9 ms: 1.00x slower                                               |
| meteor_contest             | 108 ms                                                                 | 109 ms: 1.01x slower                                                |
| json_dumps                 | 11.6 ms                                                                | 11.6 ms: 1.01x slower                                               |
| regex_compile              | 128 ms                                                                 | 129 ms: 1.01x slower                                                |
| regex_effbot               | 3.16 ms                                                                | 3.18 ms: 1.01x slower                                               |
| genshi_text                | 21.4 ms                                                                | 21.6 ms: 1.01x slower                                               |
| sqlglot_v2_optimize        | 54.1 ms                                                                | 54.6 ms: 1.01x slower                                               |
| bpe_tokeniser              | 4.57 sec                                                               | 4.61 sec: 1.01x slower                                              |
| deepcopy_memo              | 29.0 us                                                                | 29.3 us: 1.01x slower                                               |
| sympy_integrate            | 20.0 ms                                                                | 20.2 ms: 1.01x slower                                               |
| sympy_expand               | 475 ms                                                                 | 480 ms: 1.01x slower                                                |
| typing_runtime_protocols   | 167 us                                                                 | 169 us: 1.01x slower                                                |
| scimark_sor                | 119 ms                                                                 | 120 ms: 1.01x slower                                                |
| connected_components       | 454 ms                                                                 | 459 ms: 1.01x slower                                                |
| sympy_str                  | 274 ms                                                                 | 278 ms: 1.01x slower                                                |
| xml_etree_iterparse        | 97.6 ms                                                                | 98.8 ms: 1.01x slower                                               |
| coverage                   | 85.5 ms                                                                | 86.6 ms: 1.01x slower                                               |
| scimark_fft                | 312 ms                                                                 | 316 ms: 1.01x slower                                                |
| deepcopy                   | 260 us                                                                 | 263 us: 1.01x slower                                                |
| thrift                     | 783 us                                                                 | 794 us: 1.01x slower                                                |
| many_optionals             | 970 us                                                                 | 984 us: 1.01x slower                                                |
| sqlalchemy_declarative     | 133 ms                                                                 | 135 ms: 1.02x slower                                                |
| sqlglot_v2_parse           | 1.29 ms                                                                | 1.31 ms: 1.02x slower                                               |
| sqlglot_v2_normalize       | 107 ms                                                                 | 110 ms: 1.02x slower                                                |
| logging_silent             | 95.7 ns                                                                | 97.6 ns: 1.02x slower                                               |
| sqlglot_v2_transpile       | 1.61 ms                                                                | 1.64 ms: 1.02x slower                                               |
| pprint_safe_repr           | 756 ms                                                                 | 774 ms: 1.02x slower                                                |
| sympy_sum                  | 152 ms                                                                 | 155 ms: 1.02x slower                                                |
| pyflate                    | 432 ms                                                                 | 442 ms: 1.02x slower                                                |
| pprint_pformat             | 1.55 sec                                                               | 1.59 sec: 1.03x slower                                              |
| sqlalchemy_imperative      | 17.1 ms                                                                | 17.5 ms: 1.03x slower                                               |
| go                         | 128 ms                                                                 | 132 ms: 1.03x slower                                                |
| deepcopy_reduce            | 2.66 us                                                                | 2.76 us: 1.04x slower                                               |
| scimark_sparse_mat_mult    | 4.61 ms                                                                | 4.84 ms: 1.05x slower                                               |
| richards_super             | 41.1 ms                                                                | 45.4 ms: 1.10x slower                                               |
| richards                   | 35.8 ms                                                                | 39.8 ms: 1.11x slower                                               |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (35): scimark_lu, async_tree_memoization_tg, async_tree_io, comprehensions, html5lib, async_tree_io_tg, xml_etree_parse, xml_etree_generate, xml_etree_process, logging_format, sqlite_synth, tomli_loads, bench_mp_pool, json, asyncio_websockets, k_core, pathlib, create_gc_cycles, pidigits, mdp, python_startup_no_site, shortest_path, hexiom, pickle_pure_python, chaos, django_template, logging_simple, 2to3, docutils, sphinx, regex_v8, float, pylint, genshi_xml, pycparser

- Geometric mean (including insignificant results): 1.003x slower

# HPT report

- Reliability score: 69.77% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x