# Results vs. base

- fork: brandtbucher
- ref: call_list_append
- machine: linux-x86_64
- commit hash: d7c7f4c
- commit date: 2024-06-06
- overall geometric mean: 1.00x slower
- HPT reliability: 99.33%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240606-linux-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 277 ms                                                                | 281 ms: 1.01x slower                                                    |
| docutils       | 2.93 sec                                                              | 2.95 sec: 1.01x slower                                                  |
| html5lib       | 66.6 ms                                                               | 68.4 ms: 1.03x slower                                                   |
| tornado_http   | 96.7 ms                                                               | 97.1 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark      | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240606-linux-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io  | 962 ms                                                                | 999 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (7): async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240606-linux-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 188 ms                                                                | 188 ms: 1.00x slower                                                    |
| float          | 72.3 ms                                                               | 72.6 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                            |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240606-linux-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 230 ms                                                                | 222 ms: 1.03x faster                                                    |
| regex_effbot   | 3.65 ms                                                               | 3.56 ms: 1.03x faster                                                   |
| regex_compile  | 138 ms                                                                | 138 ms: 1.00x slower                                                    |
| regex_v8       | 24.5 ms                                                               | 25.0 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240606-linux-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_dict          | 35.7 us                                                               | 34.7 us: 1.03x faster                                                   |
| json_dumps           | 10.4 ms                                                               | 10.2 ms: 1.02x faster                                                   |
| pickle_list          | 5.23 us                                                               | 5.14 us: 1.02x faster                                                   |
| pickle               | 12.2 us                                                               | 12.0 us: 1.01x faster                                                   |
| xml_etree_process    | 58.2 ms                                                               | 57.7 ms: 1.01x faster                                                   |
| xml_etree_iterparse  | 101 ms                                                                | 101 ms: 1.01x faster                                                    |
| unpickle_list        | 5.39 us                                                               | 5.37 us: 1.00x faster                                                   |
| json_loads           | 28.7 us                                                               | 28.9 us: 1.01x slower                                                   |
| tomli_loads          | 1.93 sec                                                              | 1.96 sec: 1.01x slower                                                  |
| unpickle_pure_python | 222 us                                                                | 225 us: 1.01x slower                                                    |
| pickle_pure_python   | 298 us                                                                | 306 us: 1.03x slower                                                    |
| unpickle             | 14.9 us                                                               | 15.6 us: 1.05x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                            |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240606-linux-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 11.1 ms: 1.00x faster                                                   |
| python_startup_no_site | 7.62 ms                                                               | 7.60 ms: 1.00x faster                                                   |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                            |

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, genshi_xml, mako, django_template

All benchmarks:
===============

| Benchmark                | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240606-linux-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal             | 4.04 ms                                                               | 3.87 ms: 1.04x faster                                                   |
| regex_dna                | 230 ms                                                                | 222 ms: 1.03x faster                                                    |
| pickle_dict              | 35.7 us                                                               | 34.7 us: 1.03x faster                                                   |
| nqueens                  | 87.3 ms                                                               | 85.0 ms: 1.03x faster                                                   |
| regex_effbot             | 3.65 ms                                                               | 3.56 ms: 1.03x faster                                                   |
| mdp                      | 2.63 sec                                                              | 2.58 sec: 1.02x faster                                                  |
| json_dumps               | 10.4 ms                                                               | 10.2 ms: 1.02x faster                                                   |
| pickle_list              | 5.23 us                                                               | 5.14 us: 1.02x faster                                                   |
| pprint_pformat           | 1.47 sec                                                              | 1.45 sec: 1.02x faster                                                  |
| pickle                   | 12.2 us                                                               | 12.0 us: 1.01x faster                                                   |
| pyflate                  | 452 ms                                                                | 446 ms: 1.01x faster                                                    |
| pprint_safe_repr         | 720 ms                                                                | 712 ms: 1.01x faster                                                    |
| coroutines               | 22.9 ms                                                               | 22.6 ms: 1.01x faster                                                   |
| json                     | 5.37 ms                                                               | 5.32 ms: 1.01x faster                                                   |
| xml_etree_process        | 58.2 ms                                                               | 57.7 ms: 1.01x faster                                                   |
| sqlglot_normalize        | 114 ms                                                                | 113 ms: 1.01x faster                                                    |
| xml_etree_iterparse      | 101 ms                                                                | 101 ms: 1.01x faster                                                    |
| sqlglot_optimize         | 57.3 ms                                                               | 57.0 ms: 1.00x faster                                                   |
| python_startup           | 11.2 ms                                                               | 11.1 ms: 1.00x faster                                                   |
| unpickle_list            | 5.39 us                                                               | 5.37 us: 1.00x faster                                                   |
| python_startup_no_site   | 7.62 ms                                                               | 7.60 ms: 1.00x faster                                                   |
| pidigits                 | 188 ms                                                                | 188 ms: 1.00x slower                                                    |
| sqlglot_transpile        | 1.64 ms                                                               | 1.65 ms: 1.00x slower                                                   |
| float                    | 72.3 ms                                                               | 72.6 ms: 1.00x slower                                                   |
| asyncio_tcp              | 515 ms                                                                | 518 ms: 1.00x slower                                                    |
| regex_compile            | 138 ms                                                                | 138 ms: 1.00x slower                                                    |
| tornado_http             | 96.7 ms                                                               | 97.1 ms: 1.00x slower                                                   |
| dulwich_log              | 68.5 ms                                                               | 68.9 ms: 1.01x slower                                                   |
| coverage                 | 92.9 ms                                                               | 93.5 ms: 1.01x slower                                                   |
| asyncio_tcp_ssl          | 1.85 sec                                                              | 1.87 sec: 1.01x slower                                                  |
| json_loads               | 28.7 us                                                               | 28.9 us: 1.01x slower                                                   |
| docutils                 | 2.93 sec                                                              | 2.95 sec: 1.01x slower                                                  |
| meteor_contest           | 108 ms                                                                | 109 ms: 1.01x slower                                                    |
| hexiom                   | 6.61 ms                                                               | 6.66 ms: 1.01x slower                                                   |
| bench_thread_pool        | 873 us                                                                | 881 us: 1.01x slower                                                    |
| comprehensions           | 16.7 us                                                               | 16.9 us: 1.01x slower                                                   |
| async_generators         | 465 ms                                                                | 469 ms: 1.01x slower                                                    |
| deepcopy_reduce          | 3.30 us                                                               | 3.34 us: 1.01x slower                                                   |
| tomli_loads              | 1.93 sec                                                              | 1.96 sec: 1.01x slower                                                  |
| unpickle_pure_python     | 222 us                                                                | 225 us: 1.01x slower                                                    |
| 2to3                     | 277 ms                                                                | 281 ms: 1.01x slower                                                    |
| logging_format           | 6.32 us                                                               | 6.42 us: 1.02x slower                                                   |
| scimark_fft              | 319 ms                                                                | 324 ms: 1.02x slower                                                    |
| richards                 | 41.1 ms                                                               | 41.8 ms: 1.02x slower                                                   |
| richards_super           | 47.6 ms                                                               | 48.4 ms: 1.02x slower                                                   |
| go                       | 146 ms                                                                | 149 ms: 1.02x slower                                                    |
| regex_v8                 | 24.5 ms                                                               | 25.0 ms: 1.02x slower                                                   |
| thrift                   | 810 us                                                                | 826 us: 1.02x slower                                                    |
| typing_runtime_protocols | 170 us                                                                | 174 us: 1.02x slower                                                    |
| html5lib                 | 66.6 ms                                                               | 68.4 ms: 1.03x slower                                                   |
| pickle_pure_python       | 298 us                                                                | 306 us: 1.03x slower                                                    |
| spectral_norm            | 102 ms                                                                | 106 ms: 1.03x slower                                                    |
| scimark_sparse_mat_mult  | 4.49 ms                                                               | 4.64 ms: 1.04x slower                                                   |
| crypto_pyaes             | 67.7 ms                                                               | 70.2 ms: 1.04x slower                                                   |
| async_tree_io            | 962 ms                                                                | 999 ms: 1.04x slower                                                    |
| unpickle                 | 14.9 us                                                               | 15.6 us: 1.05x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                            |

Benchmark hidden because not significant (40): nbody, pycparser, telco, genshi_text, create_gc_cycles, deepcopy_memo, logging_silent, sympy_sum, sympy_str, genshi_xml, scimark_lu, asyncio_websockets, xml_etree_generate, sympy_integrate, fannkuch, scimark_sor, raytrace, mako, async_tree_io_tg, sympy_expand, sqlglot_parse, pylint, logging_simple, chaos, bench_mp_pool, generators, scimark_monte_carlo, pathlib, sqlite_synth, deepcopy, dask, async_tree_memoization, xml_etree_parse, django_template, async_tree_memoization_tg, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_none, deltablue, async_tree_cpu_io_mixed_tg

# HPT report

- Reliability score: 99.33% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x