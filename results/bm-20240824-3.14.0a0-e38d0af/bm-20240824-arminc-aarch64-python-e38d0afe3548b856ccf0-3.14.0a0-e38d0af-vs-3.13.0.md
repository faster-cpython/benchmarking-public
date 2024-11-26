# Results vs. 3.13.0

- fork: python
- ref: e38d0afe3548b856ccf0
- machine: linux-aarch64
- commit hash: e38d0af
- commit date: 2024-08-24
- overall geometric mean: 1.024x faster
- HPT reliability: 99.51%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 295 ms: 1.03x faster                                                    |
| docutils       | 2.89 sec                                                 | 3.06 sec: 1.06x slower                                                  |
| Geometric mean | (ref)                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 550 ms: 1.18x faster                                                    |
| async_tree_none            | 497 ms                                                   | 427 ms: 1.16x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 563 ms: 1.16x faster                                                    |
| async_tree_none_tg         | 470 ms                                                   | 421 ms: 1.12x faster                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 731 ms: 1.05x faster                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 729 ms: 1.05x faster                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.13 sec: 1.02x slower                                                  |
| async_tree_io_tg           | 1.13 sec                                                 | 1.18 sec: 1.04x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.06x faster                                                            |

Benchmark hidden because not significant (3): async_generators, coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 109 ms: 1.05x faster                                                    |
| float          | 93.3 ms                                                  | 91.9 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 30.6 ms: 1.04x faster                                                   |
| regex_dna      | 253 ms                                                   | 247 ms: 1.03x faster                                                    |
| regex_effbot   | 4.89 ms                                                  | 4.83 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 197 ms                                                   | 190 ms: 1.04x faster                                                    |
| xml_etree_generate   | 113 ms                                                   | 112 ms: 1.01x faster                                                    |
| pickle_pure_python   | 357 us                                                   | 363 us: 1.02x slower                                                    |
| unpickle_pure_python | 251 us                                                   | 255 us: 1.02x slower                                                    |
| json_loads           | 31.7 us                                                  | 32.9 us: 1.04x slower                                                   |
| tomli_loads          | 2.54 sec                                                 | 2.64 sec: 1.04x slower                                                  |
| Geometric mean       | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (3): json_dumps, xml_etree_iterparse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 13.0 ms: 1.18x faster                                                   |
| Geometric mean | (ref)                                                    | 1.09x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 13.4 ms                                                  | 13.4 ms: 1.00x slower                                                   |
| django_template | 41.6 ms                                                  | 42.1 ms: 1.01x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 2.31 ms: 1.45x faster                                                   |
| deepcopy_memo              | 50.4 us                                                  | 38.0 us: 1.33x faster                                                   |
| deepcopy                   | 447 us                                                   | 338 us: 1.32x faster                                                    |
| python_startup             | 15.4 ms                                                  | 13.0 ms: 1.18x faster                                                   |
| gc_traversal               | 5.77 ms                                                  | 4.89 ms: 1.18x faster                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 550 ms: 1.18x faster                                                    |
| async_tree_none            | 497 ms                                                   | 427 ms: 1.16x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 563 ms: 1.16x faster                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 3.54 us: 1.15x faster                                                   |
| async_tree_none_tg         | 470 ms                                                   | 421 ms: 1.12x faster                                                    |
| bench_mp_pool              | 7.68 ms                                                  | 7.13 ms: 1.08x faster                                                   |
| generators                 | 37.6 ms                                                  | 35.2 ms: 1.07x faster                                                   |
| pathlib                    | 22.7 ms                                                  | 21.3 ms: 1.06x faster                                                   |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 731 ms: 1.05x faster                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 729 ms: 1.05x faster                                                    |
| nbody                      | 114 ms                                                   | 109 ms: 1.05x faster                                                    |
| regex_v8                   | 31.8 ms                                                  | 30.6 ms: 1.04x faster                                                   |
| thrift                     | 968 us                                                   | 931 us: 1.04x faster                                                    |
| xml_etree_parse            | 197 ms                                                   | 190 ms: 1.04x faster                                                    |
| 2to3                       | 304 ms                                                   | 295 ms: 1.03x faster                                                    |
| bench_thread_pool          | 1.27 ms                                                  | 1.24 ms: 1.03x faster                                                   |
| regex_dna                  | 253 ms                                                   | 247 ms: 1.03x faster                                                    |
| pycparser                  | 1.27 sec                                                 | 1.24 sec: 1.02x faster                                                  |
| scimark_sor                | 160 ms                                                   | 156 ms: 1.02x faster                                                    |
| scimark_lu                 | 139 ms                                                   | 136 ms: 1.02x faster                                                    |
| meteor_contest             | 114 ms                                                   | 112 ms: 1.02x faster                                                    |
| logging_silent             | 133 ns                                                   | 131 ns: 1.02x faster                                                    |
| float                      | 93.3 ms                                                  | 91.9 ms: 1.02x faster                                                   |
| logging_simple             | 7.07 us                                                  | 6.96 us: 1.02x faster                                                   |
| xml_etree_generate         | 113 ms                                                   | 112 ms: 1.01x faster                                                    |
| regex_effbot               | 4.89 ms                                                  | 4.83 ms: 1.01x faster                                                   |
| richards_super             | 60.1 ms                                                  | 59.4 ms: 1.01x faster                                                   |
| bpe_tokeniser              | 5.87 sec                                                 | 5.84 sec: 1.01x faster                                                  |
| mako                       | 13.4 ms                                                  | 13.4 ms: 1.00x slower                                                   |
| telco                      | 9.74 ms                                                  | 9.84 ms: 1.01x slower                                                   |
| pprint_safe_repr           | 926 ms                                                   | 936 ms: 1.01x slower                                                    |
| pyflate                    | 556 ms                                                   | 562 ms: 1.01x slower                                                    |
| sympy_expand               | 457 ms                                                   | 462 ms: 1.01x slower                                                    |
| django_template            | 41.6 ms                                                  | 42.1 ms: 1.01x slower                                                   |
| raytrace                   | 300 ms                                                   | 303 ms: 1.01x slower                                                    |
| pprint_pformat             | 1.90 sec                                                 | 1.93 sec: 1.02x slower                                                  |
| pickle_pure_python         | 357 us                                                   | 363 us: 1.02x slower                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.13 sec: 1.02x slower                                                  |
| unpickle_pure_python       | 251 us                                                   | 255 us: 1.02x slower                                                    |
| deltablue                  | 3.82 ms                                                  | 3.91 ms: 1.02x slower                                                   |
| sqlglot_parse              | 1.38 ms                                                  | 1.43 ms: 1.03x slower                                                   |
| json_loads                 | 31.7 us                                                  | 32.9 us: 1.04x slower                                                   |
| tomli_loads                | 2.54 sec                                                 | 2.64 sec: 1.04x slower                                                  |
| async_tree_io_tg           | 1.13 sec                                                 | 1.18 sec: 1.04x slower                                                  |
| docutils                   | 2.89 sec                                                 | 3.06 sec: 1.06x slower                                                  |
| go                         | 160 ms                                                   | 192 ms: 1.20x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (36): json_dumps, scimark_monte_carlo, scimark_sparse_mat_mult, spectral_norm, logging_format, sympy_sum, async_generators, scimark_fft, crypto_pyaes, xml_etree_iterparse, richards, python_startup_no_site, xml_etree_process, regex_compile, coverage, sympy_integrate, json, typing_runtime_protocols, fannkuch, hexiom, genshi_text, sympy_str, mdp, sqlglot_optimize, comprehensions, nqueens, pidigits, coroutines, genshi_xml, asyncio_websockets, tornado_http, sqlglot_transpile, html5lib, chaos, sqlglot_normalize, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240824-3.14.0a0-e38d0af/bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.024x faster
# HPT report

- Reliability score: 99.51% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x