# Results vs. base

- fork: brandtbucher
- ref: no_cold_exits
- machine: linux-aarch64
- commit hash: f837cc6
- commit date: 2024-06-10
- overall geometric mean: 1.01x faster
- HPT reliability: 94.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| docutils       | 3.50 sec                                                                | 3.53 sec: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                   | 1.00x faster                                                           |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark       | bm-20240605-arminc-aarch64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|-----------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io   | 1.25 sec                                                                | 1.22 sec: 1.02x faster                                                 |
| async_tree_none | 504 ms                                                                  | 494 ms: 1.02x faster                                                   |
| Geometric mean  | (ref)                                                                   | 1.01x faster                                                           |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_none_tg, async_tree_memoization_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 115 ms                                                                  | 117 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                   | 1.00x slower                                                           |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 30.1 ms                                                                 | 30.0 ms: 1.00x faster                                                  |
| regex_effbot   | 4.87 ms                                                                 | 4.94 ms: 1.01x slower                                                  |
| regex_dna      | 250 ms                                                                  | 258 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                           |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-arminc-aarch64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|---------------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_generate  | 115 ms                                                                  | 112 ms: 1.03x faster                                                   |
| pickle              | 13.7 us                                                                 | 13.4 us: 1.02x faster                                                  |
| tomli_loads         | 2.64 sec                                                                | 2.59 sec: 1.02x faster                                                 |
| xml_etree_iterparse | 149 ms                                                                  | 148 ms: 1.01x faster                                                   |
| json_loads          | 32.1 us                                                                 | 32.4 us: 1.01x slower                                                  |
| Geometric mean      | (ref)                                                                   | 1.00x faster                                                           |

Benchmark hidden because not significant (9): unpickle_pure_python, pickle_dict, unpickle, pickle_pure_python, pickle_list, xml_etree_parse, json_dumps, xml_etree_process, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|------------------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 11.0 ms                                                                 | 8.68 ms: 1.27x faster                                                  |
| python_startup         | 15.2 ms                                                                 | 12.8 ms: 1.19x faster                                                  |
| Geometric mean         | (ref)                                                                   | 1.23x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|-----------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 51.2 ms                                                                 | 49.1 ms: 1.04x faster                                                  |
| genshi_xml      | 83.0 ms                                                                 | 81.1 ms: 1.02x faster                                                  |
| mako            | 13.0 ms                                                                 | 12.9 ms: 1.01x faster                                                  |
| Geometric mean  | (ref)                                                                   | 1.02x faster                                                           |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark              | bm-20240605-arminc-aarch64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|------------------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 11.0 ms                                                                 | 8.68 ms: 1.27x faster                                                  |
| python_startup         | 15.2 ms                                                                 | 12.8 ms: 1.19x faster                                                  |
| django_template        | 51.2 ms                                                                 | 49.1 ms: 1.04x faster                                                  |
| telco                  | 10.4 ms                                                                 | 9.98 ms: 1.04x faster                                                  |
| bench_mp_pool          | 8.23 ms                                                                 | 8.01 ms: 1.03x faster                                                  |
| logging_format         | 8.09 us                                                                 | 7.89 us: 1.03x faster                                                  |
| chaos                  | 90.4 ms                                                                 | 88.2 ms: 1.03x faster                                                  |
| xml_etree_generate     | 115 ms                                                                  | 112 ms: 1.03x faster                                                   |
| richards               | 56.7 ms                                                                 | 55.4 ms: 1.02x faster                                                  |
| async_tree_io          | 1.25 sec                                                                | 1.22 sec: 1.02x faster                                                 |
| spectral_norm          | 149 ms                                                                  | 146 ms: 1.02x faster                                                   |
| sympy_expand           | 546 ms                                                                  | 534 ms: 1.02x faster                                                   |
| deepcopy_memo          | 49.9 us                                                                 | 48.8 us: 1.02x faster                                                  |
| genshi_xml             | 83.0 ms                                                                 | 81.1 ms: 1.02x faster                                                  |
| nqueens                | 118 ms                                                                  | 116 ms: 1.02x faster                                                   |
| thrift                 | 964 us                                                                  | 944 us: 1.02x faster                                                   |
| pickle                 | 13.7 us                                                                 | 13.4 us: 1.02x faster                                                  |
| async_tree_none        | 504 ms                                                                  | 494 ms: 1.02x faster                                                   |
| tomli_loads            | 2.64 sec                                                                | 2.59 sec: 1.02x faster                                                 |
| comprehensions         | 23.4 us                                                                 | 23.1 us: 1.02x faster                                                  |
| generators             | 38.6 ms                                                                 | 38.2 ms: 1.01x faster                                                  |
| deepcopy               | 494 us                                                                  | 490 us: 1.01x faster                                                   |
| mako                   | 13.0 ms                                                                 | 12.9 ms: 1.01x faster                                                  |
| pyflate                | 603 ms                                                                  | 598 ms: 1.01x faster                                                   |
| bench_thread_pool      | 1.34 ms                                                                 | 1.33 ms: 1.01x faster                                                  |
| xml_etree_iterparse    | 149 ms                                                                  | 148 ms: 1.01x faster                                                   |
| regex_v8               | 30.1 ms                                                                 | 30.0 ms: 1.00x faster                                                  |
| sympy_integrate        | 25.8 ms                                                                 | 25.9 ms: 1.01x slower                                                  |
| docutils               | 3.50 sec                                                                | 3.53 sec: 1.01x slower                                                 |
| scimark_sor            | 175 ms                                                                  | 176 ms: 1.01x slower                                                   |
| json_loads             | 32.1 us                                                                 | 32.4 us: 1.01x slower                                                  |
| nbody                  | 115 ms                                                                  | 117 ms: 1.01x slower                                                   |
| pathlib                | 21.9 ms                                                                 | 22.2 ms: 1.01x slower                                                  |
| regex_effbot           | 4.87 ms                                                                 | 4.94 ms: 1.01x slower                                                  |
| fannkuch               | 468 ms                                                                  | 476 ms: 1.02x slower                                                   |
| gc_traversal           | 5.07 ms                                                                 | 5.18 ms: 1.02x slower                                                  |
| asyncio_tcp            | 614 ms                                                                  | 630 ms: 1.03x slower                                                   |
| regex_dna              | 250 ms                                                                  | 258 ms: 1.03x slower                                                   |
| Geometric mean         | (ref)                                                                   | 1.01x faster                                                           |

Benchmark hidden because not significant (58): html5lib, dask, async_tree_cpu_io_mixed, sqlglot_optimize, sqlglot_normalize, async_generators, sympy_str, dulwich_log, scimark_monte_carlo, async_tree_cpu_io_mixed_tg, unpickle_pure_python, pycparser, richards_super, raytrace, logging_simple, pickle_dict, hexiom, crypto_pyaes, float, meteor_contest, go, 2to3, create_gc_cycles, scimark_lu, pprint_safe_repr, sqlglot_parse, unpickle, json, sympy_sum, pickle_pure_python, pprint_pformat, pidigits, asyncio_websockets, pickle_list, async_tree_io_tg, deltablue, async_tree_none_tg, xml_etree_parse, mdp, json_dumps, async_tree_memoization_tg, scimark_fft, typing_runtime_protocols, tornado_http, coroutines, sqlglot_transpile, async_tree_memoization, xml_etree_process, asyncio_tcp_ssl, scimark_sparse_mat_mult, logging_silent, coverage, sqlite_synth, unpickle_list, regex_compile, genshi_text, deepcopy_reduce, pylint

# HPT report

- Reliability score: 94.96% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x