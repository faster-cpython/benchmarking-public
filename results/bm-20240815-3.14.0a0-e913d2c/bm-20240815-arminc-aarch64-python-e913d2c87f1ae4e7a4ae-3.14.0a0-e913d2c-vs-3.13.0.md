# Results vs. 3.13.0

- fork: python
- ref: e913d2c87f1ae4e7a4ae
- machine: linux-aarch64
- commit hash: e913d2c
- commit date: 2024-08-15
- overall geometric mean: 1.028x faster
- HPT reliability: 99.83%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-arminc-aarch64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 2.89 sec                                                 | 3.11 sec: 1.07x slower                                                  |
| Geometric mean | (ref)                                                    | 1.02x slower                                                            |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-arminc-aarch64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 531 ms: 1.22x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 547 ms: 1.19x faster                                                    |
| async_tree_none_tg         | 470 ms                                                   | 398 ms: 1.18x faster                                                    |
| async_tree_none            | 497 ms                                                   | 433 ms: 1.15x faster                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 699 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 729 ms: 1.05x faster                                                    |
| Geometric mean             | (ref)                                                    | 1.08x faster                                                            |

Benchmark hidden because not significant (5): async_tree_io_tg, async_tree_io, async_generators, coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-arminc-aarch64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 111 ms: 1.03x faster                                                    |
| float          | 93.3 ms                                                  | 92.5 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-arminc-aarch64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 30.3 ms: 1.05x faster                                                   |
| regex_dna      | 253 ms                                                   | 247 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (2): regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-arminc-aarch64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 197 ms                                                   | 189 ms: 1.04x faster                                                    |
| xml_etree_iterparse  | 149 ms                                                   | 148 ms: 1.01x faster                                                    |
| tomli_loads          | 2.54 sec                                                 | 2.56 sec: 1.01x slower                                                  |
| unpickle_pure_python | 251 us                                                   | 255 us: 1.02x slower                                                    |
| json_loads           | 31.7 us                                                  | 32.5 us: 1.03x slower                                                   |
| Geometric mean       | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (4): xml_etree_generate, xml_etree_process, json_dumps, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-arminc-aarch64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 13.1 ms: 1.18x faster                                                   |
| Geometric mean | (ref)                                                    | 1.08x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): mako, genshi_text, genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-arminc-aarch64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 2.30 ms: 1.46x faster                                                   |
| deepcopy                   | 447 us                                                   | 332 us: 1.35x faster                                                    |
| deepcopy_memo              | 50.4 us                                                  | 37.9 us: 1.33x faster                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 531 ms: 1.22x faster                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 3.42 us: 1.19x faster                                                   |
| async_tree_memoization     | 651 ms                                                   | 547 ms: 1.19x faster                                                    |
| async_tree_none_tg         | 470 ms                                                   | 398 ms: 1.18x faster                                                    |
| python_startup             | 15.4 ms                                                  | 13.1 ms: 1.18x faster                                                   |
| async_tree_none            | 497 ms                                                   | 433 ms: 1.15x faster                                                    |
| gc_traversal               | 5.77 ms                                                  | 5.05 ms: 1.14x faster                                                   |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 699 ms: 1.10x faster                                                    |
| bench_mp_pool              | 7.68 ms                                                  | 7.04 ms: 1.09x faster                                                   |
| generators                 | 37.6 ms                                                  | 34.7 ms: 1.08x faster                                                   |
| pathlib                    | 22.7 ms                                                  | 21.5 ms: 1.06x faster                                                   |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 729 ms: 1.05x faster                                                    |
| regex_v8                   | 31.8 ms                                                  | 30.3 ms: 1.05x faster                                                   |
| pycparser                  | 1.27 sec                                                 | 1.22 sec: 1.04x faster                                                  |
| xml_etree_parse            | 197 ms                                                   | 189 ms: 1.04x faster                                                    |
| scimark_lu                 | 139 ms                                                   | 134 ms: 1.04x faster                                                    |
| nbody                      | 114 ms                                                   | 111 ms: 1.03x faster                                                    |
| logging_format             | 7.82 us                                                  | 7.59 us: 1.03x faster                                                   |
| bench_thread_pool          | 1.27 ms                                                  | 1.24 ms: 1.03x faster                                                   |
| regex_dna                  | 253 ms                                                   | 247 ms: 1.03x faster                                                    |
| scimark_sparse_mat_mult    | 6.51 ms                                                  | 6.37 ms: 1.02x faster                                                   |
| scimark_monte_carlo        | 83.6 ms                                                  | 81.9 ms: 1.02x faster                                                   |
| coverage                   | 99.1 ms                                                  | 97.4 ms: 1.02x faster                                                   |
| crypto_pyaes               | 83.7 ms                                                  | 82.4 ms: 1.02x faster                                                   |
| logging_silent             | 133 ns                                                   | 131 ns: 1.02x faster                                                    |
| xml_etree_iterparse        | 149 ms                                                   | 148 ms: 1.01x faster                                                    |
| float                      | 93.3 ms                                                  | 92.5 ms: 1.01x faster                                                   |
| mdp                        | 3.34 sec                                                 | 3.31 sec: 1.01x faster                                                  |
| deltablue                  | 3.82 ms                                                  | 3.79 ms: 1.01x faster                                                   |
| bpe_tokeniser              | 5.87 sec                                                 | 5.83 sec: 1.01x faster                                                  |
| tomli_loads                | 2.54 sec                                                 | 2.56 sec: 1.01x slower                                                  |
| pprint_safe_repr           | 926 ms                                                   | 934 ms: 1.01x slower                                                    |
| sympy_expand               | 457 ms                                                   | 461 ms: 1.01x slower                                                    |
| telco                      | 9.74 ms                                                  | 9.88 ms: 1.01x slower                                                   |
| sympy_str                  | 264 ms                                                   | 268 ms: 1.02x slower                                                    |
| unpickle_pure_python       | 251 us                                                   | 255 us: 1.02x slower                                                    |
| pprint_pformat             | 1.90 sec                                                 | 1.93 sec: 1.02x slower                                                  |
| pyflate                    | 556 ms                                                   | 566 ms: 1.02x slower                                                    |
| sympy_integrate            | 20.8 ms                                                  | 21.2 ms: 1.02x slower                                                   |
| sympy_sum                  | 144 ms                                                   | 147 ms: 1.02x slower                                                    |
| sqlglot_parse              | 1.38 ms                                                  | 1.41 ms: 1.02x slower                                                   |
| json_loads                 | 31.7 us                                                  | 32.5 us: 1.03x slower                                                   |
| typing_runtime_protocols   | 193 us                                                   | 201 us: 1.04x slower                                                    |
| docutils                   | 2.89 sec                                                 | 3.11 sec: 1.07x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (40): xml_etree_generate, async_tree_io_tg, async_tree_io, scimark_sor, logging_simple, tornado_http, nqueens, sqlglot_optimize, xml_etree_process, meteor_contest, 2to3, hexiom, scimark_fft, richards, raytrace, spectral_norm, async_generators, regex_compile, json_dumps, regex_effbot, mako, json, pickle_pure_python, go, chaos, genshi_text, coroutines, pidigits, sqlglot_transpile, fannkuch, comprehensions, asyncio_websockets, python_startup_no_site, genshi_xml, thrift, richards_super, django_template, sqlglot_normalize, html5lib, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240815-3.14.0a0-e913d2c/bm-20240815-arminc-aarch64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.028x faster
# HPT report

- Reliability score: 99.83% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x