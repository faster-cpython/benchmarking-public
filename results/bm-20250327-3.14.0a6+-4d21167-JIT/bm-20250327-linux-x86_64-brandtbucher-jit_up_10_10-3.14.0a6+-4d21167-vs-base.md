# Results vs. base

- fork: brandtbucher
- ref: jit_up_10_10
- machine: linux-x86_64
- commit hash: 4d21167
- commit date: 2025-03-27
- overall geometric mean: 1.009x slower
- HPT reliability: 99.71%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250327-linux-x86_64-brandtbucher-jit_up_10_10-3.14.0a6+-4d21167 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 263 ms                                                                 | 264 ms: 1.01x slower                                                 |
| docutils       | 2.69 sec                                                               | 2.71 sec: 1.01x slower                                               |
| html5lib       | 63.2 ms                                                                | 62.4 ms: 1.01x faster                                                |
| sphinx         | 1.02 sec                                                               | 1.04 sec: 1.01x slower                                               |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250327-linux-x86_64-brandtbucher-jit_up_10_10-3.14.0a6+-4d21167 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 479 ms                                                                 | 471 ms: 1.02x faster                                                 |
| async_tree_none_tg         | 255 ms                                                                 | 252 ms: 1.01x faster                                                 |
| async_tree_memoization     | 319 ms                                                                 | 315 ms: 1.01x faster                                                 |
| async_tree_cpu_io_mixed    | 492 ms                                                                 | 488 ms: 1.01x faster                                                 |
| async_generators           | 418 ms                                                                 | 419 ms: 1.00x slower                                                 |
| coroutines                 | 24.1 ms                                                                | 24.2 ms: 1.00x slower                                                |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (5): async_tree_io, async_tree_io_tg, async_tree_memoization_tg, async_tree_none, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250327-linux-x86_64-brandtbucher-jit_up_10_10-3.14.0a6+-4d21167 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 185 ms: 1.00x faster                                                 |
| float          | 64.9 ms                                                                | 65.7 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250327-linux-x86_64-brandtbucher-jit_up_10_10-3.14.0a6+-4d21167 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 128 ms                                                                 | 129 ms: 1.01x slower                                                 |
| regex_dna      | 217 ms                                                                 | 219 ms: 1.01x slower                                                 |
| regex_effbot   | 3.16 ms                                                                | 3.42 ms: 1.08x slower                                                |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                         |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250327-linux-x86_64-brandtbucher-jit_up_10_10-3.14.0a6+-4d21167 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| unpickle_pure_python | 214 us                                                                 | 211 us: 1.02x faster                                                 |
| xml_etree_iterparse  | 97.6 ms                                                                | 98.3 ms: 1.01x slower                                                |
| tomli_loads          | 1.87 sec                                                               | 1.89 sec: 1.01x slower                                               |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (6): xml_etree_process, json_loads, xml_etree_generate, xml_etree_parse, json_dumps, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250327-linux-x86_64-brandtbucher-jit_up_10_10-3.14.0a6+-4d21167 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 13.1 ms                                                                | 13.1 ms: 1.00x slower                                                |
| python_startup_no_site | 8.19 ms                                                                | 8.22 ms: 1.00x slower                                                |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250327-linux-x86_64-brandtbucher-jit_up_10_10-3.14.0a6+-4d21167 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_xml      | 49.8 ms                                                                | 50.2 ms: 1.01x slower                                                |
| django_template | 32.0 ms                                                                | 32.3 ms: 1.01x slower                                                |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (2): mako, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250327-linux-x86_64-brandtbucher-jit_up_10_10-3.14.0a6+-4d21167 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| crypto_pyaes               | 78.3 ms                                                                | 76.1 ms: 1.03x faster                                                |
| spectral_norm              | 97.1 ms                                                                | 95.1 ms: 1.02x faster                                                |
| async_tree_cpu_io_mixed_tg | 479 ms                                                                 | 471 ms: 1.02x faster                                                 |
| generators                 | 29.2 ms                                                                | 28.8 ms: 1.02x faster                                                |
| unpickle_pure_python       | 214 us                                                                 | 211 us: 1.02x faster                                                 |
| async_tree_none_tg         | 255 ms                                                                 | 252 ms: 1.01x faster                                                 |
| html5lib                   | 63.2 ms                                                                | 62.4 ms: 1.01x faster                                                |
| gc_traversal               | 5.05 ms                                                                | 4.99 ms: 1.01x faster                                                |
| async_tree_memoization     | 319 ms                                                                 | 315 ms: 1.01x faster                                                 |
| subparsers                 | 21.0 ms                                                                | 20.9 ms: 1.01x faster                                                |
| thrift                     | 783 us                                                                 | 777 us: 1.01x faster                                                 |
| async_tree_cpu_io_mixed    | 492 ms                                                                 | 488 ms: 1.01x faster                                                 |
| pathlib                    | 16.8 ms                                                                | 16.6 ms: 1.01x faster                                                |
| scimark_monte_carlo        | 68.6 ms                                                                | 68.2 ms: 1.01x faster                                                |
| deltablue                  | 3.06 ms                                                                | 3.04 ms: 1.01x faster                                                |
| deepcopy_memo              | 29.0 us                                                                | 28.8 us: 1.00x faster                                                |
| pidigits                   | 186 ms                                                                 | 185 ms: 1.00x faster                                                 |
| python_startup             | 13.1 ms                                                                | 13.1 ms: 1.00x slower                                                |
| async_generators           | 418 ms                                                                 | 419 ms: 1.00x slower                                                 |
| python_startup_no_site     | 8.19 ms                                                                | 8.22 ms: 1.00x slower                                                |
| mdp                        | 2.48 sec                                                               | 2.49 sec: 1.00x slower                                               |
| coroutines                 | 24.1 ms                                                                | 24.2 ms: 1.00x slower                                                |
| logging_silent             | 95.7 ns                                                                | 96.1 ns: 1.00x slower                                                |
| create_gc_cycles           | 2.48 ms                                                                | 2.50 ms: 1.01x slower                                                |
| regex_compile              | 128 ms                                                                 | 129 ms: 1.01x slower                                                 |
| 2to3                       | 263 ms                                                                 | 264 ms: 1.01x slower                                                 |
| sympy_expand               | 475 ms                                                                 | 478 ms: 1.01x slower                                                 |
| genshi_xml                 | 49.8 ms                                                                | 50.2 ms: 1.01x slower                                                |
| bench_thread_pool          | 882 us                                                                 | 888 us: 1.01x slower                                                 |
| xml_etree_iterparse        | 97.6 ms                                                                | 98.3 ms: 1.01x slower                                                |
| django_template            | 32.0 ms                                                                | 32.3 ms: 1.01x slower                                                |
| docutils                   | 2.69 sec                                                               | 2.71 sec: 1.01x slower                                               |
| sqlglot_v2_optimize        | 54.1 ms                                                                | 54.6 ms: 1.01x slower                                                |
| pyflate                    | 432 ms                                                                 | 435 ms: 1.01x slower                                                 |
| coverage                   | 85.5 ms                                                                | 86.3 ms: 1.01x slower                                                |
| json                       | 5.29 ms                                                                | 5.34 ms: 1.01x slower                                                |
| scimark_sor                | 119 ms                                                                 | 120 ms: 1.01x slower                                                 |
| float                      | 64.9 ms                                                                | 65.7 ms: 1.01x slower                                                |
| meteor_contest             | 108 ms                                                                 | 110 ms: 1.01x slower                                                 |
| tomli_loads                | 1.87 sec                                                               | 1.89 sec: 1.01x slower                                               |
| sympy_str                  | 274 ms                                                                 | 278 ms: 1.01x slower                                                 |
| regex_dna                  | 217 ms                                                                 | 219 ms: 1.01x slower                                                 |
| sphinx                     | 1.02 sec                                                               | 1.04 sec: 1.01x slower                                               |
| sympy_integrate            | 20.0 ms                                                                | 20.3 ms: 1.02x slower                                                |
| scimark_sparse_mat_mult    | 4.61 ms                                                                | 4.68 ms: 1.02x slower                                                |
| nqueens                    | 84.9 ms                                                                | 86.4 ms: 1.02x slower                                                |
| pprint_safe_repr           | 756 ms                                                                 | 771 ms: 1.02x slower                                                 |
| deepcopy_reduce            | 2.66 us                                                                | 2.71 us: 1.02x slower                                                |
| sqlglot_v2_parse           | 1.29 ms                                                                | 1.31 ms: 1.02x slower                                                |
| bpe_tokeniser              | 4.57 sec                                                               | 4.66 sec: 1.02x slower                                               |
| typing_runtime_protocols   | 167 us                                                                 | 170 us: 1.02x slower                                                 |
| sympy_sum                  | 152 ms                                                                 | 155 ms: 1.02x slower                                                 |
| many_optionals             | 970 us                                                                 | 992 us: 1.02x slower                                                 |
| sqlglot_v2_transpile       | 1.61 ms                                                                | 1.64 ms: 1.02x slower                                                |
| hexiom                     | 6.86 ms                                                                | 7.03 ms: 1.02x slower                                                |
| sqlglot_v2_normalize       | 107 ms                                                                 | 110 ms: 1.03x slower                                                 |
| sqlalchemy_declarative     | 133 ms                                                                 | 136 ms: 1.03x slower                                                 |
| sqlalchemy_imperative      | 17.1 ms                                                                | 17.7 ms: 1.04x slower                                                |
| pycparser                  | 1.13 sec                                                               | 1.18 sec: 1.05x slower                                               |
| regex_effbot               | 3.16 ms                                                                | 3.42 ms: 1.08x slower                                                |
| connected_components       | 454 ms                                                                 | 496 ms: 1.09x slower                                                 |
| richards_super             | 41.1 ms                                                                | 47.2 ms: 1.15x slower                                                |
| richards                   | 35.8 ms                                                                | 41.1 ms: 1.15x slower                                                |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (33): async_tree_io, async_tree_io_tg, async_tree_memoization_tg, async_tree_none, xml_etree_process, go, nbody, pprint_pformat, logging_simple, scimark_lu, telco, bench_mp_pool, regex_v8, asyncio_websockets, comprehensions, chaos, sqlite_synth, dulwich_log, logging_format, json_loads, xml_etree_generate, xml_etree_parse, json_dumps, pickle_pure_python, mako, genshi_text, scimark_fft, raytrace, fannkuch, k_core, shortest_path, deepcopy, pylint

- Geometric mean (including insignificant results): 1.009x slower

# HPT report

- Reliability score: 99.71% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x