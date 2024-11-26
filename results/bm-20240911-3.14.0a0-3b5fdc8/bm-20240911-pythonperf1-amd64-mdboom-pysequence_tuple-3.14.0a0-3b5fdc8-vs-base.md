# Results vs. base

- fork: mdboom
- ref: pysequence_tuple
- machine: windows-amd64
- commit hash: 3b5fdc8
- commit date: 2024-09-11
- overall geometric mean: 1.014x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 221 ms                                                                     | 222 ms: 1.01x slower                                                   |
| html5lib       | 39.4 ms                                                                    | 40.3 ms: 1.02x slower                                                  |
| tornado_http   | 83.3 ms                                                                    | 84.1 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                           |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_generators           | 238 ms                                                                     | 239 ms: 1.01x slower                                                   |
| async_tree_cpu_io_mixed_tg | 390 ms                                                                     | 395 ms: 1.01x slower                                                   |
| Geometric mean             | (ref)                                                                      | 1.01x slower                                                           |

Benchmark hidden because not significant (10): async_tree_none, coroutines, async_tree_memoization, async_tree_io, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_memoization_tg, asyncio_tcp, asyncio_tcp_ssl, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 79.8 ms                                                                    | 81.8 ms: 1.02x slower                                                  |
| float          | 54.4 ms                                                                    | 56.6 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                                      | 1.02x slower                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 89.6 ms                                                                    | 91.5 ms: 1.02x slower                                                  |
| regex_effbot   | 1.55 ms                                                                    | 1.59 ms: 1.03x slower                                                  |
| regex_v8       | 14.6 ms                                                                    | 15.1 ms: 1.03x slower                                                  |
| regex_dna      | 114 ms                                                                     | 121 ms: 1.07x slower                                                   |
| Geometric mean | (ref)                                                                      | 1.04x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_dict          | 19.7 us                                                                    | 18.7 us: 1.05x faster                                                  |
| unpickle_list        | 2.77 us                                                                    | 2.72 us: 1.02x faster                                                  |
| pickle               | 7.28 us                                                                    | 7.17 us: 1.02x faster                                                  |
| json_dumps           | 6.18 ms                                                                    | 6.23 ms: 1.01x slower                                                  |
| xml_etree_process    | 40.4 ms                                                                    | 40.8 ms: 1.01x slower                                                  |
| pickle_pure_python   | 209 us                                                                     | 212 us: 1.02x slower                                                   |
| tomli_loads          | 1.56 sec                                                                   | 1.59 sec: 1.02x slower                                                 |
| xml_etree_generate   | 57.2 ms                                                                    | 58.6 ms: 1.02x slower                                                  |
| unpickle_pure_python | 145 us                                                                     | 153 us: 1.05x slower                                                   |
| Geometric mean       | (ref)                                                                      | 1.00x slower                                                           |

Benchmark hidden because not significant (5): unpickle, xml_etree_parse, json_loads, xml_etree_iterparse, pickle_list

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|-----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 24.5 ms                                                                    | 24.9 ms: 1.02x slower                                                  |
| genshi_text     | 16.9 ms                                                                    | 17.3 ms: 1.02x slower                                                  |
| genshi_xml      | 35.9 ms                                                                    | 37.4 ms: 1.04x slower                                                  |
| Geometric mean  | (ref)                                                                      | 1.02x slower                                                           |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_dict                | 19.7 us                                                                    | 18.7 us: 1.05x faster                                                  |
| coverage                   | 48.1 ms                                                                    | 46.9 ms: 1.03x faster                                                  |
| unpickle_list              | 2.77 us                                                                    | 2.72 us: 1.02x faster                                                  |
| pickle                     | 7.28 us                                                                    | 7.17 us: 1.02x faster                                                  |
| pathlib                    | 73.9 ms                                                                    | 73.5 ms: 1.01x faster                                                  |
| scimark_fft                | 204 ms                                                                     | 203 ms: 1.00x faster                                                   |
| sympy_expand               | 306 ms                                                                     | 307 ms: 1.00x slower                                                   |
| generators                 | 20.9 ms                                                                    | 21.0 ms: 1.01x slower                                                  |
| 2to3                       | 221 ms                                                                     | 222 ms: 1.01x slower                                                   |
| async_generators           | 238 ms                                                                     | 239 ms: 1.01x slower                                                   |
| sqlglot_normalize          | 191 ms                                                                     | 193 ms: 1.01x slower                                                   |
| json_dumps                 | 6.18 ms                                                                    | 6.23 ms: 1.01x slower                                                  |
| tornado_http               | 83.3 ms                                                                    | 84.1 ms: 1.01x slower                                                  |
| pprint_safe_repr           | 541 ms                                                                     | 546 ms: 1.01x slower                                                   |
| xml_etree_process          | 40.4 ms                                                                    | 40.8 ms: 1.01x slower                                                  |
| logging_silent             | 61.9 ns                                                                    | 62.6 ns: 1.01x slower                                                  |
| pyflate                    | 315 ms                                                                     | 319 ms: 1.01x slower                                                   |
| bench_mp_pool              | 65.8 ms                                                                    | 66.6 ms: 1.01x slower                                                  |
| sympy_str                  | 176 ms                                                                     | 178 ms: 1.01x slower                                                   |
| deltablue                  | 2.24 ms                                                                    | 2.26 ms: 1.01x slower                                                  |
| nqueens                    | 62.9 ms                                                                    | 63.7 ms: 1.01x slower                                                  |
| sqlglot_optimize           | 36.0 ms                                                                    | 36.5 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed_tg | 390 ms                                                                     | 395 ms: 1.01x slower                                                   |
| richards_super             | 35.8 ms                                                                    | 36.4 ms: 1.02x slower                                                  |
| dulwich_log                | 41.9 ms                                                                    | 42.6 ms: 1.02x slower                                                  |
| pickle_pure_python         | 209 us                                                                     | 212 us: 1.02x slower                                                   |
| scimark_sor                | 87.5 ms                                                                    | 88.8 ms: 1.02x slower                                                  |
| django_template            | 24.5 ms                                                                    | 24.9 ms: 1.02x slower                                                  |
| telco                      | 5.06 ms                                                                    | 5.16 ms: 1.02x slower                                                  |
| sympy_integrate            | 13.0 ms                                                                    | 13.2 ms: 1.02x slower                                                  |
| comprehensions             | 11.4 us                                                                    | 11.7 us: 1.02x slower                                                  |
| regex_compile              | 89.6 ms                                                                    | 91.5 ms: 1.02x slower                                                  |
| hexiom                     | 4.30 ms                                                                    | 4.39 ms: 1.02x slower                                                  |
| logging_simple             | 6.25 us                                                                    | 6.39 us: 1.02x slower                                                  |
| html5lib                   | 39.4 ms                                                                    | 40.3 ms: 1.02x slower                                                  |
| sympy_sum                  | 89.2 ms                                                                    | 91.2 ms: 1.02x slower                                                  |
| richards                   | 31.7 ms                                                                    | 32.4 ms: 1.02x slower                                                  |
| tomli_loads                | 1.56 sec                                                                   | 1.59 sec: 1.02x slower                                                 |
| xml_etree_generate         | 57.2 ms                                                                    | 58.6 ms: 1.02x slower                                                  |
| genshi_text                | 16.9 ms                                                                    | 17.3 ms: 1.02x slower                                                  |
| nbody                      | 79.8 ms                                                                    | 81.8 ms: 1.02x slower                                                  |
| crypto_pyaes               | 46.9 ms                                                                    | 48.1 ms: 1.03x slower                                                  |
| sqlglot_transpile          | 1.09 ms                                                                    | 1.12 ms: 1.03x slower                                                  |
| regex_effbot               | 1.55 ms                                                                    | 1.59 ms: 1.03x slower                                                  |
| sqlglot_parse              | 875 us                                                                     | 900 us: 1.03x slower                                                   |
| scimark_lu                 | 61.8 ms                                                                    | 63.6 ms: 1.03x slower                                                  |
| scimark_sparse_mat_mult    | 2.64 ms                                                                    | 2.72 ms: 1.03x slower                                                  |
| scimark_monte_carlo        | 48.5 ms                                                                    | 49.9 ms: 1.03x slower                                                  |
| deepcopy_memo              | 20.0 us                                                                    | 20.6 us: 1.03x slower                                                  |
| go                         | 84.6 ms                                                                    | 87.3 ms: 1.03x slower                                                  |
| chaos                      | 42.3 ms                                                                    | 43.7 ms: 1.03x slower                                                  |
| logging_format             | 6.66 us                                                                    | 6.88 us: 1.03x slower                                                  |
| regex_v8                   | 14.6 ms                                                                    | 15.1 ms: 1.03x slower                                                  |
| float                      | 54.4 ms                                                                    | 56.6 ms: 1.04x slower                                                  |
| fannkuch                   | 280 ms                                                                     | 292 ms: 1.04x slower                                                   |
| genshi_xml                 | 35.9 ms                                                                    | 37.4 ms: 1.04x slower                                                  |
| unpickle_pure_python       | 145 us                                                                     | 153 us: 1.05x slower                                                   |
| regex_dna                  | 114 ms                                                                     | 121 ms: 1.07x slower                                                   |
| spectral_norm              | 64.7 ms                                                                    | 69.0 ms: 1.07x slower                                                  |
| thrift                     | 507 us                                                                     | 544 us: 1.07x slower                                                   |
| pycparser                  | 744 ms                                                                     | 802 ms: 1.08x slower                                                   |
| Geometric mean             | (ref)                                                                      | 1.01x slower                                                           |

Benchmark hidden because not significant (34): unpickle, create_gc_cycles, bench_thread_pool, async_tree_none, deepcopy_reduce, typing_runtime_protocols, pidigits, coroutines, pprint_pformat, async_tree_memoization, mdp, unpack_sequence, xml_etree_parse, sqlite_synth, gc_traversal, deepcopy, async_tree_io, docutils, json_loads, meteor_contest, python_startup, async_tree_cpu_io_mixed, raytrace, xml_etree_iterparse, mako, python_startup_no_site, async_tree_io_tg, async_tree_memoization_tg, pickle_list, asyncio_tcp, pylint, asyncio_tcp_ssl, async_tree_none_tg, json

- Geometric mean (including insignificant results): 1.014x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown