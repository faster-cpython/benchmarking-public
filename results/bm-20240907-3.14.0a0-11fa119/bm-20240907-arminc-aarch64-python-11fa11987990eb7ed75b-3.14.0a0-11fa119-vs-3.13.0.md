# Results vs. 3.13.0

- fork: python
- ref: 11fa11987990eb7ed75b
- machine: linux-aarch64
- commit hash: 11fa119
- commit date: 2024-09-07
- overall geometric mean: 1.031x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 293 ms: 1.03x faster                                                    |
| docutils       | 2.89 sec                                                 | 3.05 sec: 1.05x slower                                                  |
| html5lib       | 66.4 ms                                                  | 63.1 ms: 1.05x faster                                                   |
| tornado_http   | 128 ms                                                   | 124 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 549 ms: 1.18x faster                                                    |
| async_tree_none            | 497 ms                                                   | 423 ms: 1.17x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 556 ms: 1.17x faster                                                    |
| async_tree_none_tg         | 470 ms                                                   | 416 ms: 1.13x faster                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 725 ms: 1.06x faster                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 733 ms: 1.04x faster                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.13 sec: 1.02x slower                                                  |
| async_tree_io_tg           | 1.13 sec                                                 | 1.18 sec: 1.04x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.06x faster                                                            |

Benchmark hidden because not significant (3): async_generators, asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 109 ms: 1.05x faster                                                    |
| float          | 93.3 ms                                                  | 92.7 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 30.3 ms: 1.05x faster                                                   |
| regex_compile  | 127 ms                                                   | 125 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (2): regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 197 ms                                                   | 186 ms: 1.06x faster                                                    |
| xml_etree_process    | 80.5 ms                                                  | 78.5 ms: 1.03x faster                                                   |
| xml_etree_generate   | 113 ms                                                   | 111 ms: 1.02x faster                                                    |
| xml_etree_iterparse  | 149 ms                                                   | 148 ms: 1.01x faster                                                    |
| pickle_pure_python   | 357 us                                                   | 361 us: 1.01x slower                                                    |
| unpickle_pure_python | 251 us                                                   | 255 us: 1.02x slower                                                    |
| json_loads           | 31.7 us                                                  | 32.5 us: 1.03x slower                                                   |
| tomli_loads          | 2.54 sec                                                 | 2.65 sec: 1.04x slower                                                  |
| Geometric mean       | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 15.4 ms                                                  | 13.2 ms: 1.17x faster                                                   |
| python_startup_no_site | 8.73 ms                                                  | 8.83 ms: 1.01x slower                                                   |
| Geometric mean         | (ref)                                                    | 1.07x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 13.4 ms                                                  | 13.4 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (3): genshi_text, django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 2.30 ms: 1.46x faster                                                   |
| deepcopy                   | 447 us                                                   | 332 us: 1.35x faster                                                    |
| deepcopy_memo              | 50.4 us                                                  | 38.0 us: 1.33x faster                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 549 ms: 1.18x faster                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 3.45 us: 1.18x faster                                                   |
| gc_traversal               | 5.77 ms                                                  | 4.91 ms: 1.18x faster                                                   |
| async_tree_none            | 497 ms                                                   | 423 ms: 1.17x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 556 ms: 1.17x faster                                                    |
| python_startup             | 15.4 ms                                                  | 13.2 ms: 1.17x faster                                                   |
| go                         | 160 ms                                                   | 138 ms: 1.16x faster                                                    |
| async_tree_none_tg         | 470 ms                                                   | 416 ms: 1.13x faster                                                    |
| bench_mp_pool              | 7.68 ms                                                  | 7.02 ms: 1.10x faster                                                   |
| pathlib                    | 22.7 ms                                                  | 21.0 ms: 1.08x faster                                                   |
| generators                 | 37.6 ms                                                  | 35.1 ms: 1.07x faster                                                   |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 725 ms: 1.06x faster                                                    |
| xml_etree_parse            | 197 ms                                                   | 186 ms: 1.06x faster                                                    |
| html5lib                   | 66.4 ms                                                  | 63.1 ms: 1.05x faster                                                   |
| regex_v8                   | 31.8 ms                                                  | 30.3 ms: 1.05x faster                                                   |
| nbody                      | 114 ms                                                   | 109 ms: 1.05x faster                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 733 ms: 1.04x faster                                                    |
| thrift                     | 968 us                                                   | 931 us: 1.04x faster                                                    |
| scimark_lu                 | 139 ms                                                   | 134 ms: 1.04x faster                                                    |
| pycparser                  | 1.27 sec                                                 | 1.23 sec: 1.03x faster                                                  |
| 2to3                       | 304 ms                                                   | 293 ms: 1.03x faster                                                    |
| tornado_http               | 128 ms                                                   | 124 ms: 1.03x faster                                                    |
| bench_thread_pool          | 1.27 ms                                                  | 1.24 ms: 1.03x faster                                                   |
| logging_format             | 7.82 us                                                  | 7.62 us: 1.03x faster                                                   |
| xml_etree_process          | 80.5 ms                                                  | 78.5 ms: 1.03x faster                                                   |
| xml_etree_generate         | 113 ms                                                   | 111 ms: 1.02x faster                                                    |
| scimark_sparse_mat_mult    | 6.51 ms                                                  | 6.38 ms: 1.02x faster                                                   |
| scimark_monte_carlo        | 83.6 ms                                                  | 82.0 ms: 1.02x faster                                                   |
| regex_compile              | 127 ms                                                   | 125 ms: 1.02x faster                                                    |
| logging_simple             | 7.07 us                                                  | 6.95 us: 1.02x faster                                                   |
| meteor_contest             | 114 ms                                                   | 112 ms: 1.02x faster                                                    |
| pprint_safe_repr           | 926 ms                                                   | 914 ms: 1.01x faster                                                    |
| xml_etree_iterparse        | 149 ms                                                   | 148 ms: 1.01x faster                                                    |
| richards_super             | 60.1 ms                                                  | 59.5 ms: 1.01x faster                                                   |
| fannkuch                   | 461 ms                                                   | 456 ms: 1.01x faster                                                    |
| scimark_fft                | 447 ms                                                   | 443 ms: 1.01x faster                                                    |
| bpe_tokeniser              | 5.87 sec                                                 | 5.83 sec: 1.01x faster                                                  |
| float                      | 93.3 ms                                                  | 92.7 ms: 1.01x faster                                                   |
| mako                       | 13.4 ms                                                  | 13.4 ms: 1.00x slower                                                   |
| python_startup_no_site     | 8.73 ms                                                  | 8.83 ms: 1.01x slower                                                   |
| pickle_pure_python         | 357 us                                                   | 361 us: 1.01x slower                                                    |
| sympy_expand               | 457 ms                                                   | 464 ms: 1.02x slower                                                    |
| unpickle_pure_python       | 251 us                                                   | 255 us: 1.02x slower                                                    |
| pyflate                    | 556 ms                                                   | 566 ms: 1.02x slower                                                    |
| deltablue                  | 3.82 ms                                                  | 3.91 ms: 1.02x slower                                                   |
| async_tree_io              | 1.11 sec                                                 | 1.13 sec: 1.02x slower                                                  |
| telco                      | 9.74 ms                                                  | 9.99 ms: 1.02x slower                                                   |
| json_loads                 | 31.7 us                                                  | 32.5 us: 1.03x slower                                                   |
| sqlglot_parse              | 1.38 ms                                                  | 1.42 ms: 1.03x slower                                                   |
| tomli_loads                | 2.54 sec                                                 | 2.65 sec: 1.04x slower                                                  |
| async_tree_io_tg           | 1.13 sec                                                 | 1.18 sec: 1.04x slower                                                  |
| docutils                   | 2.89 sec                                                 | 3.05 sec: 1.05x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (32): json_dumps, richards, nqueens, spectral_norm, scimark_sor, genshi_text, regex_dna, json, typing_runtime_protocols, sympy_sum, crypto_pyaes, sympy_integrate, logging_silent, pprint_pformat, async_generators, sqlglot_transpile, mdp, asyncio_websockets, regex_effbot, django_template, coroutines, sympy_str, pidigits, comprehensions, genshi_xml, coverage, sqlglot_normalize, sqlglot_optimize, raytrace, chaos, hexiom, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20240907-3.14.0a0-11fa119/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.031x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x