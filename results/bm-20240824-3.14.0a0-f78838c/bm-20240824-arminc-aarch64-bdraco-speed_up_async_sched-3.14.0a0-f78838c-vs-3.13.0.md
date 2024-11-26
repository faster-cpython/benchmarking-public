# Results vs. 3.13.0

- fork: bdraco
- ref: speed_up_async_sched
- machine: linux-aarch64
- commit hash: f78838c
- commit date: 2024-08-24
- overall geometric mean: 1.023x faster
- HPT reliability: 98.50%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 293 ms: 1.04x faster                                                    |
| docutils       | 2.89 sec                                                 | 3.09 sec: 1.07x slower                                                  |
| Geometric mean | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 541 ms: 1.20x faster                                                    |
| async_tree_none            | 497 ms                                                   | 426 ms: 1.17x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 575 ms: 1.13x faster                                                    |
| async_tree_none_tg         | 470 ms                                                   | 423 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 732 ms: 1.05x faster                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 733 ms: 1.05x faster                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.20 sec: 1.08x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.05x faster                                                            |

Benchmark hidden because not significant (4): asyncio_websockets, async_generators, coroutines, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 110 ms: 1.04x faster                                                    |
| float          | 93.3 ms                                                  | 91.1 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 253 ms                                                   | 247 ms: 1.02x faster                                                    |
| regex_v8       | 31.8 ms                                                  | 31.2 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (2): regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 197 ms                                                   | 191 ms: 1.03x faster                                                    |
| xml_etree_iterparse  | 149 ms                                                   | 148 ms: 1.01x faster                                                    |
| pickle_pure_python   | 357 us                                                   | 355 us: 1.00x faster                                                    |
| unpickle_pure_python | 251 us                                                   | 253 us: 1.01x slower                                                    |
| json_loads           | 31.7 us                                                  | 32.9 us: 1.04x slower                                                   |
| tomli_loads          | 2.54 sec                                                 | 2.64 sec: 1.04x slower                                                  |
| Geometric mean       | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (3): json_dumps, xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 13.0 ms: 1.18x faster                                                   |
| Geometric mean | (ref)                                                    | 1.08x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 41.6 ms                                                  | 42.1 ms: 1.01x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (3): mako, genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 2.29 ms: 1.46x faster                                                   |
| deepcopy_memo              | 50.4 us                                                  | 37.9 us: 1.33x faster                                                   |
| deepcopy                   | 447 us                                                   | 338 us: 1.32x faster                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 541 ms: 1.20x faster                                                    |
| python_startup             | 15.4 ms                                                  | 13.0 ms: 1.18x faster                                                   |
| async_tree_none            | 497 ms                                                   | 426 ms: 1.17x faster                                                    |
| gc_traversal               | 5.77 ms                                                  | 4.96 ms: 1.16x faster                                                   |
| deepcopy_reduce            | 4.07 us                                                  | 3.53 us: 1.15x faster                                                   |
| async_tree_memoization     | 651 ms                                                   | 575 ms: 1.13x faster                                                    |
| async_tree_none_tg         | 470 ms                                                   | 423 ms: 1.11x faster                                                    |
| bench_mp_pool              | 7.68 ms                                                  | 7.11 ms: 1.08x faster                                                   |
| generators                 | 37.6 ms                                                  | 34.8 ms: 1.08x faster                                                   |
| pathlib                    | 22.7 ms                                                  | 21.2 ms: 1.07x faster                                                   |
| thrift                     | 968 us                                                   | 918 us: 1.05x faster                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 732 ms: 1.05x faster                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 733 ms: 1.05x faster                                                    |
| nbody                      | 114 ms                                                   | 110 ms: 1.04x faster                                                    |
| pycparser                  | 1.27 sec                                                 | 1.22 sec: 1.04x faster                                                  |
| 2to3                       | 304 ms                                                   | 293 ms: 1.04x faster                                                    |
| bench_thread_pool          | 1.27 ms                                                  | 1.23 ms: 1.03x faster                                                   |
| scimark_lu                 | 139 ms                                                   | 135 ms: 1.03x faster                                                    |
| xml_etree_parse            | 197 ms                                                   | 191 ms: 1.03x faster                                                    |
| float                      | 93.3 ms                                                  | 91.1 ms: 1.02x faster                                                   |
| crypto_pyaes               | 83.7 ms                                                  | 81.7 ms: 1.02x faster                                                   |
| regex_dna                  | 253 ms                                                   | 247 ms: 1.02x faster                                                    |
| scimark_monte_carlo        | 83.6 ms                                                  | 81.9 ms: 1.02x faster                                                   |
| regex_v8                   | 31.8 ms                                                  | 31.2 ms: 1.02x faster                                                   |
| scimark_sor                | 160 ms                                                   | 157 ms: 1.02x faster                                                    |
| xml_etree_iterparse        | 149 ms                                                   | 148 ms: 1.01x faster                                                    |
| pickle_pure_python         | 357 us                                                   | 355 us: 1.00x faster                                                    |
| raytrace                   | 300 ms                                                   | 302 ms: 1.01x slower                                                    |
| mdp                        | 3.34 sec                                                 | 3.36 sec: 1.01x slower                                                  |
| pprint_pformat             | 1.90 sec                                                 | 1.91 sec: 1.01x slower                                                  |
| sympy_str                  | 264 ms                                                   | 267 ms: 1.01x slower                                                    |
| unpickle_pure_python       | 251 us                                                   | 253 us: 1.01x slower                                                    |
| django_template            | 41.6 ms                                                  | 42.1 ms: 1.01x slower                                                   |
| sympy_expand               | 457 ms                                                   | 463 ms: 1.01x slower                                                    |
| deltablue                  | 3.82 ms                                                  | 3.89 ms: 1.02x slower                                                   |
| telco                      | 9.74 ms                                                  | 10.0 ms: 1.03x slower                                                   |
| json_loads                 | 31.7 us                                                  | 32.9 us: 1.04x slower                                                   |
| tomli_loads                | 2.54 sec                                                 | 2.64 sec: 1.04x slower                                                  |
| sqlglot_parse              | 1.38 ms                                                  | 1.45 ms: 1.05x slower                                                   |
| pyflate                    | 556 ms                                                   | 593 ms: 1.07x slower                                                    |
| docutils                   | 2.89 sec                                                 | 3.09 sec: 1.07x slower                                                  |
| async_tree_io              | 1.11 sec                                                 | 1.20 sec: 1.08x slower                                                  |
| go                         | 160 ms                                                   | 191 ms: 1.20x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (41): json_dumps, html5lib, nqueens, tornado_http, xml_etree_generate, scimark_sparse_mat_mult, meteor_contest, sympy_sum, spectral_norm, coverage, xml_etree_process, regex_effbot, scimark_fft, logging_format, pprint_safe_repr, regex_compile, sympy_integrate, logging_silent, bpe_tokeniser, hexiom, sqlglot_transpile, mako, richards_super, sqlglot_normalize, fannkuch, pidigits, genshi_xml, genshi_text, asyncio_websockets, richards, typing_runtime_protocols, async_generators, coroutines, logging_simple, chaos, comprehensions, python_startup_no_site, json, sqlglot_optimize, async_tree_io_tg, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240824-3.14.0a0-f78838c/bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.023x faster
# HPT report

- Reliability score: 98.50% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x