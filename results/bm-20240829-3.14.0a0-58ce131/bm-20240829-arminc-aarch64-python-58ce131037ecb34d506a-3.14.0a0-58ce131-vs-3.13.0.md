# Results vs. 3.13.0

- fork: python
- ref: 58ce131037ecb34d506a
- machine: linux-aarch64
- commit hash: 58ce131
- commit date: 2024-08-29
- overall geometric mean: 1.031x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 297 ms: 1.02x faster                                                    |
| docutils       | 2.89 sec                                                 | 3.01 sec: 1.04x slower                                                  |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 552 ms: 1.18x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 555 ms: 1.17x faster                                                    |
| async_tree_none            | 497 ms                                                   | 424 ms: 1.17x faster                                                    |
| async_tree_none_tg         | 470 ms                                                   | 413 ms: 1.14x faster                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 728 ms: 1.06x faster                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 731 ms: 1.05x faster                                                    |
| async_generators           | 489 ms                                                   | 482 ms: 1.02x faster                                                    |
| async_tree_io_tg           | 1.13 sec                                                 | 1.17 sec: 1.03x slower                                                  |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.03x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.06x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 110 ms: 1.04x faster                                                    |
| float          | 93.3 ms                                                  | 92.6 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 30.3 ms: 1.05x faster                                                   |
| regex_dna      | 253 ms                                                   | 247 ms: 1.02x faster                                                    |
| regex_compile  | 127 ms                                                   | 125 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 197 ms                                                   | 188 ms: 1.04x faster                                                    |
| unpickle_pure_python | 251 us                                                   | 253 us: 1.01x slower                                                    |
| pickle_pure_python   | 357 us                                                   | 363 us: 1.02x slower                                                    |
| json_loads           | 31.7 us                                                  | 32.6 us: 1.03x slower                                                   |
| tomli_loads          | 2.54 sec                                                 | 2.63 sec: 1.04x slower                                                  |
| Geometric mean       | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (4): xml_etree_process, xml_etree_generate, xml_etree_iterparse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 13.1 ms: 1.17x faster                                                   |
| Geometric mean | (ref)                                                    | 1.08x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 13.4 ms                                                  | 13.5 ms: 1.01x slower                                                   |
| django_template | 41.6 ms                                                  | 42.8 ms: 1.03x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 2.29 ms: 1.46x faster                                                   |
| deepcopy                   | 447 us                                                   | 334 us: 1.34x faster                                                    |
| deepcopy_memo              | 50.4 us                                                  | 38.1 us: 1.32x faster                                                   |
| gc_traversal               | 5.77 ms                                                  | 4.84 ms: 1.19x faster                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 552 ms: 1.18x faster                                                    |
| python_startup             | 15.4 ms                                                  | 13.1 ms: 1.17x faster                                                   |
| async_tree_memoization     | 651 ms                                                   | 555 ms: 1.17x faster                                                    |
| async_tree_none            | 497 ms                                                   | 424 ms: 1.17x faster                                                    |
| go                         | 160 ms                                                   | 137 ms: 1.17x faster                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 3.56 us: 1.14x faster                                                   |
| async_tree_none_tg         | 470 ms                                                   | 413 ms: 1.14x faster                                                    |
| bench_mp_pool              | 7.68 ms                                                  | 7.04 ms: 1.09x faster                                                   |
| generators                 | 37.6 ms                                                  | 34.8 ms: 1.08x faster                                                   |
| pathlib                    | 22.7 ms                                                  | 21.1 ms: 1.08x faster                                                   |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 728 ms: 1.06x faster                                                    |
| regex_v8                   | 31.8 ms                                                  | 30.3 ms: 1.05x faster                                                   |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 731 ms: 1.05x faster                                                    |
| pycparser                  | 1.27 sec                                                 | 1.22 sec: 1.05x faster                                                  |
| nbody                      | 114 ms                                                   | 110 ms: 1.04x faster                                                    |
| xml_etree_parse            | 197 ms                                                   | 188 ms: 1.04x faster                                                    |
| scimark_lu                 | 139 ms                                                   | 134 ms: 1.04x faster                                                    |
| scimark_sparse_mat_mult    | 6.51 ms                                                  | 6.33 ms: 1.03x faster                                                   |
| scimark_monte_carlo        | 83.6 ms                                                  | 81.4 ms: 1.03x faster                                                   |
| regex_dna                  | 253 ms                                                   | 247 ms: 1.02x faster                                                    |
| bench_thread_pool          | 1.27 ms                                                  | 1.24 ms: 1.02x faster                                                   |
| 2to3                       | 304 ms                                                   | 297 ms: 1.02x faster                                                    |
| regex_compile              | 127 ms                                                   | 125 ms: 1.02x faster                                                    |
| meteor_contest             | 114 ms                                                   | 112 ms: 1.02x faster                                                    |
| crypto_pyaes               | 83.7 ms                                                  | 82.3 ms: 1.02x faster                                                   |
| scimark_sor                | 160 ms                                                   | 157 ms: 1.02x faster                                                    |
| async_generators           | 489 ms                                                   | 482 ms: 1.02x faster                                                    |
| sympy_sum                  | 144 ms                                                   | 141 ms: 1.01x faster                                                    |
| thrift                     | 968 us                                                   | 954 us: 1.01x faster                                                    |
| scimark_fft                | 447 ms                                                   | 440 ms: 1.01x faster                                                    |
| hexiom                     | 7.11 ms                                                  | 7.02 ms: 1.01x faster                                                   |
| sqlglot_normalize          | 127 ms                                                   | 125 ms: 1.01x faster                                                    |
| richards_super             | 60.1 ms                                                  | 59.6 ms: 1.01x faster                                                   |
| float                      | 93.3 ms                                                  | 92.6 ms: 1.01x faster                                                   |
| pyflate                    | 556 ms                                                   | 560 ms: 1.01x slower                                                    |
| raytrace                   | 300 ms                                                   | 301 ms: 1.01x slower                                                    |
| mako                       | 13.4 ms                                                  | 13.5 ms: 1.01x slower                                                   |
| pprint_pformat             | 1.90 sec                                                 | 1.91 sec: 1.01x slower                                                  |
| unpickle_pure_python       | 251 us                                                   | 253 us: 1.01x slower                                                    |
| pickle_pure_python         | 357 us                                                   | 363 us: 1.02x slower                                                    |
| pprint_safe_repr           | 926 ms                                                   | 942 ms: 1.02x slower                                                    |
| deltablue                  | 3.82 ms                                                  | 3.91 ms: 1.02x slower                                                   |
| django_template            | 41.6 ms                                                  | 42.8 ms: 1.03x slower                                                   |
| json_loads                 | 31.7 us                                                  | 32.6 us: 1.03x slower                                                   |
| async_tree_io_tg           | 1.13 sec                                                 | 1.17 sec: 1.03x slower                                                  |
| sqlglot_parse              | 1.38 ms                                                  | 1.42 ms: 1.03x slower                                                   |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.03x slower                                                  |
| telco                      | 9.74 ms                                                  | 10.1 ms: 1.03x slower                                                   |
| tomli_loads                | 2.54 sec                                                 | 2.63 sec: 1.04x slower                                                  |
| docutils                   | 2.89 sec                                                 | 3.01 sec: 1.04x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (33): html5lib, logging_format, spectral_norm, xml_etree_process, regex_effbot, json, tornado_http, logging_silent, coverage, sqlglot_optimize, bpe_tokeniser, sqlglot_transpile, xml_etree_generate, logging_simple, fannkuch, genshi_text, xml_etree_iterparse, asyncio_websockets, mdp, json_dumps, richards, sympy_integrate, comprehensions, sympy_str, pidigits, sympy_expand, chaos, typing_runtime_protocols, coroutines, python_startup_no_site, nqueens, genshi_xml, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240829-3.14.0a0-58ce131/bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.031x faster
# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x