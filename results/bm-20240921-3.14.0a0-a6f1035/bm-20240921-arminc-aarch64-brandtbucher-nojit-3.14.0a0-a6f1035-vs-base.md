# Results vs. base

- fork: brandtbucher
- ref: nojit
- machine: linux-aarch64
- commit hash: a6f1035
- commit date: 2024-09-21
- overall geometric mean: 1.00x faster
- HPT reliability: 53.66%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| docutils       | 3.05 sec                                                                | 3.01 sec: 1.01x faster                                         |
| Geometric mean | (ref)                                                                   | 1.01x faster                                                   |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|-------------------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_memoization  | 562 ms                                                                  | 553 ms: 1.02x faster                                           |
| async_tree_io           | 1.14 sec                                                                | 1.15 sec: 1.01x slower                                         |
| async_tree_cpu_io_mixed | 720 ms                                                                  | 736 ms: 1.02x slower                                           |
| Geometric mean          | (ref)                                                                   | 1.00x faster                                                   |

Benchmark hidden because not significant (10): asyncio_tcp, async_tree_none, async_tree_io_tg, coroutines, asyncio_tcp_ssl, async_tree_memoization_tg, asyncio_websockets, async_generators, async_tree_cpu_io_mixed_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 92.9 ms                                                                 | 94.9 ms: 1.02x slower                                          |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                   |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_dna      | 255 ms                                                                  | 251 ms: 1.02x faster                                           |
| Geometric mean | (ref)                                                                   | 1.01x faster                                                   |

Benchmark hidden because not significant (3): regex_effbot, regex_v8, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|--------------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| pickle_pure_python | 373 us                                                                  | 360 us: 1.03x faster                                           |
| xml_etree_parse    | 191 ms                                                                  | 187 ms: 1.02x faster                                           |
| tomli_loads        | 2.65 sec                                                                | 2.66 sec: 1.00x slower                                         |
| Geometric mean     | (ref)                                                                   | 1.01x faster                                                   |

Benchmark hidden because not significant (11): xml_etree_process, pickle_dict, unpickle, xml_etree_generate, pickle, json_dumps, xml_etree_iterparse, unpickle_list, pickle_list, json_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup | 13.1 ms                                                                 | 13.1 ms: 1.00x faster                                          |
| Geometric mean | (ref)                                                                   | 1.00x faster                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|-----------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| django_template | 42.3 ms                                                                 | 41.9 ms: 1.01x faster                                          |
| mako            | 13.5 ms                                                                 | 13.3 ms: 1.01x faster                                          |
| Geometric mean  | (ref)                                                                   | 1.00x slower                                                   |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|-------------------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| pickle_pure_python      | 373 us                                                                  | 360 us: 1.03x faster                                           |
| pyflate                 | 580 ms                                                                  | 563 ms: 1.03x faster                                           |
| logging_format          | 7.90 us                                                                 | 7.71 us: 1.02x faster                                          |
| xml_etree_parse         | 191 ms                                                                  | 187 ms: 1.02x faster                                           |
| regex_dna               | 255 ms                                                                  | 251 ms: 1.02x faster                                           |
| pprint_safe_repr        | 926 ms                                                                  | 911 ms: 1.02x faster                                           |
| async_tree_memoization  | 562 ms                                                                  | 553 ms: 1.02x faster                                           |
| pprint_pformat          | 1.91 sec                                                                | 1.88 sec: 1.01x faster                                         |
| docutils                | 3.05 sec                                                                | 3.01 sec: 1.01x faster                                         |
| django_template         | 42.3 ms                                                                 | 41.9 ms: 1.01x faster                                          |
| mako                    | 13.5 ms                                                                 | 13.3 ms: 1.01x faster                                          |
| sqlglot_transpile       | 1.75 ms                                                                 | 1.73 ms: 1.01x faster                                          |
| gc_traversal            | 5.09 ms                                                                 | 5.04 ms: 1.01x faster                                          |
| python_startup          | 13.1 ms                                                                 | 13.1 ms: 1.00x faster                                          |
| tomli_loads             | 2.65 sec                                                                | 2.66 sec: 1.00x slower                                         |
| bpe_tokeniser           | 5.83 sec                                                                | 5.87 sec: 1.01x slower                                         |
| telco                   | 10.2 ms                                                                 | 10.3 ms: 1.01x slower                                          |
| async_tree_io           | 1.14 sec                                                                | 1.15 sec: 1.01x slower                                         |
| chaos                   | 68.4 ms                                                                 | 69.2 ms: 1.01x slower                                          |
| meteor_contest          | 112 ms                                                                  | 114 ms: 1.02x slower                                           |
| deltablue               | 3.87 ms                                                                 | 3.94 ms: 1.02x slower                                          |
| spectral_norm           | 140 ms                                                                  | 142 ms: 1.02x slower                                           |
| sqlite_synth            | 3.81 us                                                                 | 3.88 us: 1.02x slower                                          |
| float                   | 92.9 ms                                                                 | 94.9 ms: 1.02x slower                                          |
| async_tree_cpu_io_mixed | 720 ms                                                                  | 736 ms: 1.02x slower                                           |
| bench_thread_pool       | 1.23 ms                                                                 | 1.26 ms: 1.03x slower                                          |
| deepcopy_memo           | 37.5 us                                                                 | 39.2 us: 1.05x slower                                          |
| Geometric mean          | (ref)                                                                   | 1.00x faster                                                   |

Benchmark hidden because not significant (70): xml_etree_process, tornado_http, html5lib, richards_super, asyncio_tcp, sqlglot_parse, scimark_sor, logging_simple, async_tree_none, pickle_dict, unpickle, xml_etree_generate, go, mdp, async_tree_io_tg, thrift, pickle, regex_effbot, sympy_expand, sqlglot_normalize, deepcopy, scimark_fft, json_dumps, scimark_sparse_mat_mult, coroutines, regex_v8, dulwich_log, sqlglot_optimize, asyncio_tcp_ssl, async_tree_memoization_tg, richards, scimark_monte_carlo, pidigits, logging_silent, 2to3, asyncio_websockets, python_startup_no_site, bench_mp_pool, typing_runtime_protocols, nbody, regex_compile, async_generators, hexiom, deepcopy_reduce, unpack_sequence, xml_etree_iterparse, unpickle_list, coverage, pickle_list, raytrace, pycparser, genshi_text, scimark_lu, json_loads, async_tree_cpu_io_mixed_tg, pylint, fannkuch, comprehensions, sympy_sum, crypto_pyaes, unpickle_pure_python, async_tree_none_tg, nqueens, pathlib, create_gc_cycles, sympy_integrate, sympy_str, generators, json, genshi_xml

# HPT report

- Reliability score: 53.66% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x