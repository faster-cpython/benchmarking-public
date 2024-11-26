# Results vs. 3.13.0

- fork: python
- ref: e256a7590a0149feadfe
- machine: linux-aarch64
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.032x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.90x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 295 ms: 1.03x faster                                                    |
| docutils       | 2.89 sec                                                 | 3.03 sec: 1.05x slower                                                  |
| tornado_http   | 128 ms                                                   | 124 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 497 ms                                                   | 417 ms: 1.19x faster                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 548 ms: 1.18x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 555 ms: 1.17x faster                                                    |
| async_tree_none_tg         | 470 ms                                                   | 417 ms: 1.13x faster                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 716 ms: 1.07x faster                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 722 ms: 1.06x faster                                                    |
| coroutines                 | 28.5 ms                                                  | 28.3 ms: 1.01x faster                                                   |
| async_tree_io_tg           | 1.13 sec                                                 | 1.17 sec: 1.03x slower                                                  |
| async_tree_io              | 1.11 sec                                                 | 1.14 sec: 1.03x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.07x faster                                                            |

Benchmark hidden because not significant (2): async_generators, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 111 ms: 1.04x faster                                                    |
| float          | 93.3 ms                                                  | 92.9 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 30.7 ms: 1.04x faster                                                   |
| regex_dna      | 253 ms                                                   | 247 ms: 1.02x faster                                                    |
| regex_compile  | 127 ms                                                   | 125 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate   | 113 ms                                                   | 111 ms: 1.02x faster                                                    |
| xml_etree_iterparse  | 149 ms                                                   | 148 ms: 1.01x faster                                                    |
| pickle_pure_python   | 357 us                                                   | 361 us: 1.01x slower                                                    |
| unpickle_pure_python | 251 us                                                   | 255 us: 1.02x slower                                                    |
| tomli_loads          | 2.54 sec                                                 | 2.65 sec: 1.04x slower                                                  |
| Geometric mean       | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (4): json_dumps, xml_etree_parse, xml_etree_process, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 15.4 ms                                                  | 12.9 ms: 1.19x faster                                                   |
| python_startup_no_site | 8.73 ms                                                  | 8.57 ms: 1.02x faster                                                   |
| Geometric mean         | (ref)                                                    | 1.10x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text    | 27.7 ms                                                  | 26.9 ms: 1.03x faster                                                   |
| mako           | 13.4 ms                                                  | 13.5 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 2.28 ms: 1.47x faster                                                   |
| deepcopy_memo              | 50.4 us                                                  | 37.6 us: 1.34x faster                                                   |
| deepcopy                   | 447 us                                                   | 334 us: 1.34x faster                                                    |
| python_startup             | 15.4 ms                                                  | 12.9 ms: 1.19x faster                                                   |
| async_tree_none            | 497 ms                                                   | 417 ms: 1.19x faster                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 548 ms: 1.18x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 555 ms: 1.17x faster                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 3.48 us: 1.17x faster                                                   |
| go                         | 160 ms                                                   | 138 ms: 1.16x faster                                                    |
| async_tree_none_tg         | 470 ms                                                   | 417 ms: 1.13x faster                                                    |
| gc_traversal               | 5.77 ms                                                  | 5.13 ms: 1.13x faster                                                   |
| pathlib                    | 22.7 ms                                                  | 20.9 ms: 1.08x faster                                                   |
| generators                 | 37.6 ms                                                  | 34.7 ms: 1.08x faster                                                   |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 716 ms: 1.07x faster                                                    |
| bench_mp_pool              | 7.68 ms                                                  | 7.20 ms: 1.07x faster                                                   |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 722 ms: 1.06x faster                                                    |
| pycparser                  | 1.27 sec                                                 | 1.22 sec: 1.05x faster                                                  |
| thrift                     | 968 us                                                   | 928 us: 1.04x faster                                                    |
| regex_v8                   | 31.8 ms                                                  | 30.7 ms: 1.04x faster                                                   |
| scimark_lu                 | 139 ms                                                   | 134 ms: 1.04x faster                                                    |
| nbody                      | 114 ms                                                   | 111 ms: 1.04x faster                                                    |
| bench_thread_pool          | 1.27 ms                                                  | 1.23 ms: 1.04x faster                                                   |
| logging_format             | 7.82 us                                                  | 7.56 us: 1.03x faster                                                   |
| genshi_text                | 27.7 ms                                                  | 26.9 ms: 1.03x faster                                                   |
| 2to3                       | 304 ms                                                   | 295 ms: 1.03x faster                                                    |
| tornado_http               | 128 ms                                                   | 124 ms: 1.03x faster                                                    |
| json                       | 5.73 ms                                                  | 5.58 ms: 1.03x faster                                                   |
| logging_simple             | 7.07 us                                                  | 6.89 us: 1.03x faster                                                   |
| regex_dna                  | 253 ms                                                   | 247 ms: 1.02x faster                                                    |
| sympy_sum                  | 144 ms                                                   | 140 ms: 1.02x faster                                                    |
| richards                   | 53.6 ms                                                  | 52.4 ms: 1.02x faster                                                   |
| richards_super             | 60.1 ms                                                  | 58.9 ms: 1.02x faster                                                   |
| meteor_contest             | 114 ms                                                   | 111 ms: 1.02x faster                                                    |
| python_startup_no_site     | 8.73 ms                                                  | 8.57 ms: 1.02x faster                                                   |
| xml_etree_generate         | 113 ms                                                   | 111 ms: 1.02x faster                                                    |
| regex_compile              | 127 ms                                                   | 125 ms: 1.02x faster                                                    |
| xml_etree_iterparse        | 149 ms                                                   | 148 ms: 1.01x faster                                                    |
| coroutines                 | 28.5 ms                                                  | 28.3 ms: 1.01x faster                                                   |
| scimark_fft                | 447 ms                                                   | 443 ms: 1.01x faster                                                    |
| bpe_tokeniser              | 5.87 sec                                                 | 5.85 sec: 1.00x faster                                                  |
| float                      | 93.3 ms                                                  | 92.9 ms: 1.00x faster                                                   |
| pickle_pure_python         | 357 us                                                   | 361 us: 1.01x slower                                                    |
| raytrace                   | 300 ms                                                   | 303 ms: 1.01x slower                                                    |
| mako                       | 13.4 ms                                                  | 13.5 ms: 1.01x slower                                                   |
| pyflate                    | 556 ms                                                   | 564 ms: 1.01x slower                                                    |
| comprehensions             | 20.4 us                                                  | 20.7 us: 1.02x slower                                                   |
| unpickle_pure_python       | 251 us                                                   | 255 us: 1.02x slower                                                    |
| deltablue                  | 3.82 ms                                                  | 3.88 ms: 1.02x slower                                                   |
| telco                      | 9.74 ms                                                  | 9.97 ms: 1.02x slower                                                   |
| async_tree_io_tg           | 1.13 sec                                                 | 1.17 sec: 1.03x slower                                                  |
| sqlglot_parse              | 1.38 ms                                                  | 1.42 ms: 1.03x slower                                                   |
| async_tree_io              | 1.11 sec                                                 | 1.14 sec: 1.03x slower                                                  |
| tomli_loads                | 2.54 sec                                                 | 2.65 sec: 1.04x slower                                                  |
| docutils                   | 2.89 sec                                                 | 3.03 sec: 1.05x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (33): json_dumps, xml_etree_parse, scimark_monte_carlo, crypto_pyaes, scimark_sor, async_generators, xml_etree_process, coverage, fannkuch, genshi_xml, pprint_safe_repr, spectral_norm, json_loads, sympy_str, django_template, sqlglot_transpile, pprint_pformat, hexiom, sympy_integrate, logging_silent, html5lib, pidigits, sqlglot_normalize, asyncio_websockets, nqueens, mdp, sympy_expand, scimark_sparse_mat_mult, regex_effbot, chaos, typing_runtime_protocols, sqlglot_optimize, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20240924-3.14.0a0-e256a75/bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.032x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.90x