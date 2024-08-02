# Results vs. base

- fork: brandtbucher
- ref: no_cold_exits
- machine: darwin-arm64
- commit hash: f837cc6
- commit date: 2024-06-10
- overall geometric mean: 1.00x faster
- HPT reliability: 95.49%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.86x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 170 ms                                                                | 168 ms: 1.01x faster                                                 |
| docutils       | 1.50 sec                                                              | 1.50 sec: 1.00x faster                                               |
| html5lib       | 30.9 ms                                                               | 30.7 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                         |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_eager_tg              | 42.5 ms                                                               | 42.3 ms: 1.00x faster                                                |
| async_tree_eager_cpu_io_mixed_tg | 333 ms                                                                | 332 ms: 1.00x faster                                                 |
| Geometric mean                   | (ref)                                                                 | 1.00x faster                                                         |

Benchmark hidden because not significant (14): async_tree_eager_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_io_tg, async_tree_none, async_tree_eager_memoization, async_tree_none_tg, async_tree_io, async_tree_memoization, async_tree_eager_io, async_tree_eager_memoization_tg, async_tree_eager

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 64.0 ms                                                               | 63.7 ms: 1.00x faster                                                |
| pidigits       | 281 ms                                                                | 282 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                         |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_v8       | 17.4 ms                                                               | 17.3 ms: 1.00x faster                                                |
| regex_dna      | 149 ms                                                                | 149 ms: 1.00x faster                                                 |
| regex_compile  | 72.4 ms                                                               | 73.4 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                         |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240605-darwin-arm64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|--------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_parse    | 105 ms                                                                | 102 ms: 1.02x faster                                                 |
| xml_etree_generate | 51.1 ms                                                               | 51.2 ms: 1.00x slower                                                |
| pickle_pure_python | 172 us                                                                | 173 us: 1.01x slower                                                 |
| xml_etree_process  | 35.6 ms                                                               | 35.9 ms: 1.01x slower                                                |
| tomli_loads        | 1.25 sec                                                              | 1.26 sec: 1.01x slower                                               |
| pickle_list        | 2.94 us                                                               | 2.98 us: 1.02x slower                                                |
| unpickle_list      | 2.85 us                                                               | 3.07 us: 1.08x slower                                                |
| Geometric mean     | (ref)                                                                 | 1.01x slower                                                         |

Benchmark hidden because not significant (7): json_loads, json_dumps, unpickle_pure_python, xml_etree_iterparse, pickle, pickle_dict, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 12.7 ms                                                               | 11.6 ms: 1.10x faster                                                |
| python_startup         | 15.4 ms                                                               | 14.1 ms: 1.09x faster                                                |
| Geometric mean         | (ref)                                                                 | 1.09x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                               | 16.1 ms: 1.05x faster                                                |
| django_template | 21.5 ms                                                               | 21.4 ms: 1.01x faster                                                |
| genshi_xml      | 39.3 ms                                                               | 39.6 ms: 1.01x slower                                                |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                         |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| asyncio_tcp                      | 457 ms                                                                | 415 ms: 1.10x faster                                                 |
| python_startup_no_site           | 12.7 ms                                                               | 11.6 ms: 1.10x faster                                                |
| python_startup                   | 15.4 ms                                                               | 14.1 ms: 1.09x faster                                                |
| genshi_text                      | 16.9 ms                                                               | 16.1 ms: 1.05x faster                                                |
| richards_super                   | 35.6 ms                                                               | 34.2 ms: 1.04x faster                                                |
| richards                         | 31.6 ms                                                               | 30.4 ms: 1.04x faster                                                |
| nqueens                          | 58.9 ms                                                               | 57.1 ms: 1.03x faster                                                |
| bench_mp_pool                    | 49.4 ms                                                               | 48.0 ms: 1.03x faster                                                |
| logging_silent                   | 63.8 ns                                                               | 62.3 ns: 1.02x faster                                                |
| xml_etree_parse                  | 105 ms                                                                | 102 ms: 1.02x faster                                                 |
| create_gc_cycles                 | 914 us                                                                | 895 us: 1.02x faster                                                 |
| logging_format                   | 3.44 us                                                               | 3.39 us: 1.02x faster                                                |
| typing_runtime_protocols         | 95.3 us                                                               | 94.1 us: 1.01x faster                                                |
| pathlib                          | 21.9 ms                                                               | 21.6 ms: 1.01x faster                                                |
| scimark_sparse_mat_mult          | 2.95 ms                                                               | 2.92 ms: 1.01x faster                                                |
| scimark_monte_carlo              | 44.5 ms                                                               | 44.0 ms: 1.01x faster                                                |
| scimark_sor                      | 102 ms                                                                | 101 ms: 1.01x faster                                                 |
| async_generators                 | 289 ms                                                                | 287 ms: 1.01x faster                                                 |
| 2to3                             | 170 ms                                                                | 168 ms: 1.01x faster                                                 |
| html5lib                         | 30.9 ms                                                               | 30.7 ms: 1.01x faster                                                |
| sqlite_synth                     | 1.56 us                                                               | 1.55 us: 1.01x faster                                                |
| django_template                  | 21.5 ms                                                               | 21.4 ms: 1.01x faster                                                |
| sympy_str                        | 139 ms                                                                | 138 ms: 1.01x faster                                                 |
| sympy_expand                     | 239 ms                                                                | 237 ms: 1.01x faster                                                 |
| generators                       | 23.5 ms                                                               | 23.3 ms: 1.00x faster                                                |
| gc_traversal                     | 2.47 ms                                                               | 2.46 ms: 1.00x faster                                                |
| mdp                              | 1.44 sec                                                              | 1.44 sec: 1.00x faster                                               |
| chaos                            | 39.7 ms                                                               | 39.5 ms: 1.00x faster                                                |
| async_tree_eager_tg              | 42.5 ms                                                               | 42.3 ms: 1.00x faster                                                |
| regex_v8                         | 17.4 ms                                                               | 17.3 ms: 1.00x faster                                                |
| nbody                            | 64.0 ms                                                               | 63.7 ms: 1.00x faster                                                |
| async_tree_eager_cpu_io_mixed_tg | 333 ms                                                                | 332 ms: 1.00x faster                                                 |
| deepcopy_memo                    | 21.3 us                                                               | 21.2 us: 1.00x faster                                                |
| regex_dna                        | 149 ms                                                                | 149 ms: 1.00x faster                                                 |
| logging_simple                   | 3.10 us                                                               | 3.09 us: 1.00x faster                                                |
| docutils                         | 1.50 sec                                                              | 1.50 sec: 1.00x faster                                               |
| sympy_integrate                  | 10.9 ms                                                               | 10.9 ms: 1.00x faster                                                |
| asyncio_websockets               | 409 ms                                                                | 409 ms: 1.00x faster                                                 |
| scimark_fft                      | 185 ms                                                                | 185 ms: 1.00x faster                                                 |
| pidigits                         | 281 ms                                                                | 282 ms: 1.00x slower                                                 |
| go                               | 102 ms                                                                | 103 ms: 1.00x slower                                                 |
| xml_etree_generate               | 51.1 ms                                                               | 51.2 ms: 1.00x slower                                                |
| raytrace                         | 164 ms                                                                | 165 ms: 1.00x slower                                                 |
| scimark_lu                       | 79.1 ms                                                               | 79.4 ms: 1.00x slower                                                |
| sqlglot_transpile                | 1.01 ms                                                               | 1.01 ms: 1.01x slower                                                |
| deepcopy                         | 206 us                                                                | 207 us: 1.01x slower                                                 |
| deepcopy_reduce                  | 1.82 us                                                               | 1.83 us: 1.01x slower                                                |
| pickle_pure_python               | 172 us                                                                | 173 us: 1.01x slower                                                 |
| xml_etree_process                | 35.6 ms                                                               | 35.9 ms: 1.01x slower                                                |
| genshi_xml                       | 39.3 ms                                                               | 39.6 ms: 1.01x slower                                                |
| hexiom                           | 4.41 ms                                                               | 4.44 ms: 1.01x slower                                                |
| thrift                           | 434 us                                                                | 437 us: 1.01x slower                                                 |
| comprehensions                   | 12.3 us                                                               | 12.4 us: 1.01x slower                                                |
| sqlglot_parse                    | 830 us                                                                | 840 us: 1.01x slower                                                 |
| tomli_loads                      | 1.25 sec                                                              | 1.26 sec: 1.01x slower                                               |
| meteor_contest                   | 72.5 ms                                                               | 73.5 ms: 1.01x slower                                                |
| regex_compile                    | 72.4 ms                                                               | 73.4 ms: 1.01x slower                                                |
| pickle_list                      | 2.94 us                                                               | 2.98 us: 1.02x slower                                                |
| pyflate                          | 314 ms                                                                | 320 ms: 1.02x slower                                                 |
| crypto_pyaes                     | 51.8 ms                                                               | 52.8 ms: 1.02x slower                                                |
| telco                            | 4.47 ms                                                               | 4.57 ms: 1.02x slower                                                |
| pprint_pformat                   | 947 ms                                                                | 986 ms: 1.04x slower                                                 |
| pprint_safe_repr                 | 460 ms                                                                | 483 ms: 1.05x slower                                                 |
| fannkuch                         | 239 ms                                                                | 251 ms: 1.05x slower                                                 |
| unpickle_list                    | 2.85 us                                                               | 3.07 us: 1.08x slower                                                |
| Geometric mean                   | (ref)                                                                 | 1.00x faster                                                         |

Benchmark hidden because not significant (37): deltablue, pylint, bench_thread_pool, async_tree_eager_cpu_io_mixed, sympy_sum, async_tree_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_cpu_io_mixed, float, pycparser, json_loads, json_dumps, asyncio_tcp_ssl, async_tree_memoization_tg, dask, async_tree_io_tg, spectral_norm, unpickle_pure_python, async_tree_none, sqlglot_optimize, async_tree_eager_memoization, async_tree_none_tg, coroutines, regex_effbot, mako, xml_etree_iterparse, async_tree_io, pickle, pickle_dict, async_tree_memoization, async_tree_eager_io, async_tree_eager_memoization_tg, unpickle, async_tree_eager, json, coverage, tornado_http

# HPT report

- Reliability score: 95.49% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.86x