# Results vs. base

- fork: brandtbucher
- ref: no_cold_exits
- machine: linux-aarch64
- commit hash: a1bdb94
- commit date: 2024-06-18
- overall geometric mean: 1.00x faster
- HPT reliability: 70.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_none, async_tree_io, async_tree_memoization, async_tree_io_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240618-arminc-aarch64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240618-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 114 ms                                                                  | 116 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                           |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240618-arminc-aarch64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240618-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 257 ms                                                                  | 252 ms: 1.02x faster                                                   |
| regex_v8       | 30.2 ms                                                                 | 30.5 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                   | 1.00x faster                                                           |

Benchmark hidden because not significant (2): regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240618-arminc-aarch64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240618-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|---------------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads         | 2.66 sec                                                                | 2.64 sec: 1.01x faster                                                 |
| xml_etree_iterparse | 148 ms                                                                  | 148 ms: 1.00x faster                                                   |
| pickle_pure_python  | 385 us                                                                  | 393 us: 1.02x slower                                                   |
| Geometric mean      | (ref)                                                                   | 1.00x faster                                                           |

Benchmark hidden because not significant (11): xml_etree_process, unpickle_list, pickle, json_loads, pickle_list, json_dumps, xml_etree_parse, pickle_dict, xml_etree_generate, unpickle_pure_python, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240618-arminc-aarch64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240618-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|------------------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 11.1 ms                                                                 | 8.79 ms: 1.26x faster                                                  |
| python_startup         | 15.4 ms                                                                 | 13.0 ms: 1.19x faster                                                  |
| Geometric mean         | (ref)                                                                   | 1.22x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240618-arminc-aarch64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240618-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|-----------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 50.5 ms                                                                 | 49.8 ms: 1.01x faster                                                  |
| mako            | 13.1 ms                                                                 | 13.2 ms: 1.01x slower                                                  |
| genshi_text     | 34.8 ms                                                                 | 35.2 ms: 1.01x slower                                                  |
| Geometric mean  | (ref)                                                                   | 1.00x faster                                                           |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20240618-arminc-aarch64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240618-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|-------------------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site  | 11.1 ms                                                                 | 8.79 ms: 1.26x faster                                                  |
| python_startup          | 15.4 ms                                                                 | 13.0 ms: 1.19x faster                                                  |
| gc_traversal            | 5.02 ms                                                                 | 4.85 ms: 1.04x faster                                                  |
| deepcopy_memo           | 38.9 us                                                                 | 37.7 us: 1.03x faster                                                  |
| asyncio_tcp             | 632 ms                                                                  | 617 ms: 1.03x faster                                                   |
| bench_mp_pool           | 7.83 ms                                                                 | 7.66 ms: 1.02x faster                                                  |
| regex_dna               | 257 ms                                                                  | 252 ms: 1.02x faster                                                   |
| telco                   | 10.3 ms                                                                 | 10.1 ms: 1.02x faster                                                  |
| django_template         | 50.5 ms                                                                 | 49.8 ms: 1.01x faster                                                  |
| richards                | 54.5 ms                                                                 | 53.8 ms: 1.01x faster                                                  |
| sympy_expand            | 549 ms                                                                  | 543 ms: 1.01x faster                                                   |
| bpe_tokeniser           | 6.07 sec                                                                | 6.01 sec: 1.01x faster                                                 |
| asyncio_tcp_ssl         | 2.28 sec                                                                | 2.26 sec: 1.01x faster                                                 |
| tomli_loads             | 2.66 sec                                                                | 2.64 sec: 1.01x faster                                                 |
| xml_etree_iterparse     | 148 ms                                                                  | 148 ms: 1.00x faster                                                   |
| coverage                | 101 ms                                                                  | 101 ms: 1.01x slower                                                   |
| regex_v8                | 30.2 ms                                                                 | 30.5 ms: 1.01x slower                                                  |
| mako                    | 13.1 ms                                                                 | 13.2 ms: 1.01x slower                                                  |
| scimark_sparse_mat_mult | 6.83 ms                                                                 | 6.90 ms: 1.01x slower                                                  |
| pprint_pformat          | 2.33 sec                                                                | 2.35 sec: 1.01x slower                                                 |
| meteor_contest          | 115 ms                                                                  | 116 ms: 1.01x slower                                                   |
| genshi_text             | 34.8 ms                                                                 | 35.2 ms: 1.01x slower                                                  |
| deltablue               | 4.43 ms                                                                 | 4.48 ms: 1.01x slower                                                  |
| deepcopy                | 376 us                                                                  | 381 us: 1.01x slower                                                   |
| nbody                   | 114 ms                                                                  | 116 ms: 1.02x slower                                                   |
| pickle_pure_python      | 385 us                                                                  | 393 us: 1.02x slower                                                   |
| scimark_sor             | 174 ms                                                                  | 178 ms: 1.02x slower                                                   |
| logging_format          | 7.83 us                                                                 | 8.02 us: 1.02x slower                                                  |
| scimark_monte_carlo     | 86.3 ms                                                                 | 89.2 ms: 1.03x slower                                                  |
| deepcopy_reduce         | 4.07 us                                                                 | 4.21 us: 1.03x slower                                                  |
| Geometric mean          | (ref)                                                                   | 1.00x faster                                                           |

Benchmark hidden because not significant (67): pylint, xml_etree_process, async_generators, bench_thread_pool, dask, genshi_xml, async_tree_cpu_io_mixed, dulwich_log, unpickle_list, async_tree_cpu_io_mixed_tg, pickle, async_tree_none_tg, create_gc_cycles, asyncio_websockets, comprehensions, richards_super, async_tree_none, coroutines, pyflate, regex_effbot, docutils, pidigits, fannkuch, sqlglot_optimize, 2to3, json_loads, spectral_norm, hexiom, pickle_list, json_dumps, thrift, sqlglot_transpile, xml_etree_parse, sqlglot_normalize, regex_compile, mdp, pycparser, pickle_dict, raytrace, typing_runtime_protocols, xml_etree_generate, sqlglot_parse, sympy_str, async_tree_io, pprint_safe_repr, unpickle_pure_python, async_tree_memoization, scimark_fft, scimark_lu, async_tree_io_tg, sqlite_synth, go, nqueens, tornado_http, unpickle, sympy_sum, pathlib, json, generators, logging_silent, sympy_integrate, html5lib, chaos, crypto_pyaes, float, logging_simple, async_tree_memoization_tg

# HPT report

- Reliability score: 70.96% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x