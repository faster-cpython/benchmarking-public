# Results vs. base

- fork: brandtbucher
- ref: inline_class_call_de
- machine: linux-x86_64
- commit hash: 1108a82
- commit date: 2024-06-05
- overall geometric mean: 1.00x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240605-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-1108a82 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 277 ms                                                                | 280 ms: 1.01x slower                                                        |
| docutils       | 2.93 sec                                                              | 2.95 sec: 1.01x slower                                                      |
| html5lib       | 66.6 ms                                                               | 69.3 ms: 1.04x slower                                                       |
| tornado_http   | 96.7 ms                                                               | 97.2 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_none, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240605-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-1108a82 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 84.0 ms                                                               | 81.4 ms: 1.03x faster                                                       |
| float          | 72.3 ms                                                               | 72.7 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240605-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-1108a82 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 230 ms                                                                | 231 ms: 1.01x slower                                                        |
| regex_v8       | 24.5 ms                                                               | 25.1 ms: 1.02x slower                                                       |
| regex_effbot   | 3.65 ms                                                               | 3.86 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240605-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-1108a82 |
|--------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_dict        | 35.7 us                                                               | 35.1 us: 1.02x faster                                                       |
| json_dumps         | 10.4 ms                                                               | 10.3 ms: 1.01x faster                                                       |
| xml_etree_generate | 82.0 ms                                                               | 82.7 ms: 1.01x slower                                                       |
| tomli_loads        | 1.93 sec                                                              | 1.95 sec: 1.01x slower                                                      |
| pickle_list        | 5.23 us                                                               | 5.34 us: 1.02x slower                                                       |
| json_loads         | 28.7 us                                                               | 29.4 us: 1.02x slower                                                       |
| Geometric mean     | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (8): pickle, unpickle_pure_python, unpickle_list, xml_etree_process, xml_etree_iterparse, xml_etree_parse, pickle_pure_python, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240605-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-1108a82 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.62 ms                                                               | 7.63 ms: 1.00x slower                                                       |
| python_startup         | 11.2 ms                                                               | 11.2 ms: 1.00x slower                                                       |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240605-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-1108a82 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 37.0 ms                                                               | 36.6 ms: 1.01x faster                                                       |
| mako            | 10.0 ms                                                               | 10.1 ms: 1.01x slower                                                       |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240605-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-1108a82 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| gc_traversal             | 4.04 ms                                                               | 3.76 ms: 1.07x faster                                                       |
| scimark_sparse_mat_mult  | 4.49 ms                                                               | 4.33 ms: 1.04x faster                                                       |
| nbody                    | 84.0 ms                                                               | 81.4 ms: 1.03x faster                                                       |
| pprint_safe_repr         | 720 ms                                                                | 701 ms: 1.03x faster                                                        |
| pickle_dict              | 35.7 us                                                               | 35.1 us: 1.02x faster                                                       |
| mdp                      | 2.63 sec                                                              | 2.58 sec: 1.02x faster                                                      |
| scimark_fft              | 319 ms                                                                | 314 ms: 1.02x faster                                                        |
| json_dumps               | 10.4 ms                                                               | 10.3 ms: 1.01x faster                                                       |
| deepcopy_memo            | 38.5 us                                                               | 38.1 us: 1.01x faster                                                       |
| django_template          | 37.0 ms                                                               | 36.6 ms: 1.01x faster                                                       |
| coroutines               | 22.9 ms                                                               | 22.7 ms: 1.01x faster                                                       |
| sqlite_synth             | 2.85 us                                                               | 2.84 us: 1.01x faster                                                       |
| comprehensions           | 16.7 us                                                               | 16.6 us: 1.01x faster                                                       |
| sqlglot_normalize        | 114 ms                                                                | 113 ms: 1.01x faster                                                        |
| crypto_pyaes             | 67.7 ms                                                               | 67.4 ms: 1.00x faster                                                       |
| fannkuch                 | 356 ms                                                                | 355 ms: 1.00x faster                                                        |
| python_startup_no_site   | 7.62 ms                                                               | 7.63 ms: 1.00x slower                                                       |
| bench_thread_pool        | 873 us                                                                | 875 us: 1.00x slower                                                        |
| python_startup           | 11.2 ms                                                               | 11.2 ms: 1.00x slower                                                       |
| async_generators         | 465 ms                                                                | 466 ms: 1.00x slower                                                        |
| sqlglot_transpile        | 1.64 ms                                                               | 1.65 ms: 1.00x slower                                                       |
| tornado_http             | 96.7 ms                                                               | 97.2 ms: 1.01x slower                                                       |
| regex_dna                | 230 ms                                                                | 231 ms: 1.01x slower                                                        |
| float                    | 72.3 ms                                                               | 72.7 ms: 1.01x slower                                                       |
| mako                     | 10.0 ms                                                               | 10.1 ms: 1.01x slower                                                       |
| asyncio_tcp_ssl          | 1.85 sec                                                              | 1.86 sec: 1.01x slower                                                      |
| asyncio_tcp              | 515 ms                                                                | 519 ms: 1.01x slower                                                        |
| docutils                 | 2.93 sec                                                              | 2.95 sec: 1.01x slower                                                      |
| logging_simple           | 5.69 us                                                               | 5.74 us: 1.01x slower                                                       |
| xml_etree_generate       | 82.0 ms                                                               | 82.7 ms: 1.01x slower                                                       |
| 2to3                     | 277 ms                                                                | 280 ms: 1.01x slower                                                        |
| tomli_loads              | 1.93 sec                                                              | 1.95 sec: 1.01x slower                                                      |
| spectral_norm            | 102 ms                                                                | 104 ms: 1.01x slower                                                        |
| hexiom                   | 6.61 ms                                                               | 6.70 ms: 1.01x slower                                                       |
| pathlib                  | 16.4 ms                                                               | 16.7 ms: 1.02x slower                                                       |
| go                       | 146 ms                                                                | 149 ms: 1.02x slower                                                        |
| pyflate                  | 452 ms                                                                | 460 ms: 1.02x slower                                                        |
| logging_format           | 6.32 us                                                               | 6.44 us: 1.02x slower                                                       |
| richards_super           | 47.6 ms                                                               | 48.5 ms: 1.02x slower                                                       |
| raytrace                 | 278 ms                                                                | 283 ms: 1.02x slower                                                        |
| pickle_list              | 5.23 us                                                               | 5.34 us: 1.02x slower                                                       |
| regex_v8                 | 24.5 ms                                                               | 25.1 ms: 1.02x slower                                                       |
| json_loads               | 28.7 us                                                               | 29.4 us: 1.02x slower                                                       |
| typing_runtime_protocols | 170 us                                                                | 174 us: 1.03x slower                                                        |
| richards                 | 41.1 ms                                                               | 42.2 ms: 1.03x slower                                                       |
| scimark_sor              | 129 ms                                                                | 133 ms: 1.03x slower                                                        |
| html5lib                 | 66.6 ms                                                               | 69.3 ms: 1.04x slower                                                       |
| pycparser                | 1.15 sec                                                              | 1.21 sec: 1.05x slower                                                      |
| regex_effbot             | 3.65 ms                                                               | 3.86 ms: 1.06x slower                                                       |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (47): telco, sqlglot_optimize, json, generators, create_gc_cycles, logging_silent, regex_compile, genshi_xml, sympy_expand, pickle, asyncio_websockets, sympy_integrate, pprint_pformat, sympy_sum, unpickle_pure_python, pidigits, sqlglot_parse, dulwich_log, bench_mp_pool, genshi_text, sympy_str, scimark_monte_carlo, meteor_contest, dask, pylint, unpickle_list, chaos, thrift, xml_etree_process, xml_etree_iterparse, async_tree_none, coverage, xml_etree_parse, pickle_pure_python, deepcopy_reduce, scimark_lu, deepcopy, nqueens, async_tree_none_tg, async_tree_cpu_io_mixed, deltablue, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_io_tg, unpickle, async_tree_memoization, async_tree_io

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x