# Results vs. base

- fork: mdboom
- ref: marshal_slice
- machine: windows-amd64
- commit hash: 0e19ac7
- commit date: 2024-10-07
- overall geometric mean: 1.022x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| html5lib       | 43.0 ms                                                                    | 40.1 ms: 1.07x faster                                               |
| Geometric mean | (ref)                                                                      | 1.02x faster                                                        |

Benchmark hidden because not significant (3): 2to3, docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| coroutines                 | 14.9 ms                                                                    | 13.9 ms: 1.08x faster                                               |
| async_tree_cpu_io_mixed_tg | 400 ms                                                                     | 384 ms: 1.04x faster                                                |
| async_generators           | 248 ms                                                                     | 246 ms: 1.01x faster                                                |
| Geometric mean             | (ref)                                                                      | 1.01x faster                                                        |

Benchmark hidden because not significant (9): async_tree_none, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_io, asyncio_tcp, async_tree_io_tg, async_tree_memoization_tg, async_tree_memoization, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 87.6 ms                                                                    | 81.0 ms: 1.08x faster                                               |
| float          | 56.9 ms                                                                    | 56.0 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                                      | 1.03x faster                                                        |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_dna      | 118 ms                                                                     | 114 ms: 1.04x faster                                                |
| regex_compile  | 93.0 ms                                                                    | 90.4 ms: 1.03x faster                                               |
| regex_effbot   | 1.59 ms                                                                    | 1.54 ms: 1.03x faster                                               |
| regex_v8       | 15.0 ms                                                                    | 14.7 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                                      | 1.03x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle               | 7.49 us                                                                    | 7.12 us: 1.05x faster                                               |
| unpickle_list        | 2.83 us                                                                    | 2.74 us: 1.03x faster                                               |
| unpickle_pure_python | 155 us                                                                     | 150 us: 1.03x faster                                                |
| xml_etree_process    | 42.1 ms                                                                    | 40.7 ms: 1.03x faster                                               |
| xml_etree_iterparse  | 66.6 ms                                                                    | 64.4 ms: 1.03x faster                                               |
| tomli_loads          | 1.62 sec                                                                   | 1.58 sec: 1.03x faster                                              |
| xml_etree_generate   | 59.5 ms                                                                    | 58.0 ms: 1.02x faster                                               |
| unpickle             | 9.52 us                                                                    | 9.30 us: 1.02x faster                                               |
| pickle_pure_python   | 218 us                                                                     | 215 us: 1.02x faster                                                |
| xml_etree_parse      | 94.4 ms                                                                    | 93.5 ms: 1.01x faster                                               |
| pickle_dict          | 18.3 us                                                                    | 18.4 us: 1.00x slower                                               |
| pickle_list          | 2.88 us                                                                    | 2.90 us: 1.01x slower                                               |
| Geometric mean       | (ref)                                                                      | 1.02x faster                                                        |

Benchmark hidden because not significant (2): json_loads, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|------------------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 18.6 ms                                                                    | 17.8 ms: 1.05x faster                                               |
| python_startup         | 22.7 ms                                                                    | 22.1 ms: 1.03x faster                                               |
| Geometric mean         | (ref)                                                                      | 1.04x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|-----------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 7.23 ms                                                                    | 6.93 ms: 1.04x faster                                               |
| django_template | 25.6 ms                                                                    | 24.8 ms: 1.03x faster                                               |
| genshi_text     | 17.1 ms                                                                    | 16.8 ms: 1.02x faster                                               |
| genshi_xml      | 36.0 ms                                                                    | 35.6 ms: 1.01x faster                                               |
| Geometric mean  | (ref)                                                                      | 1.03x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpack_sequence            | 42.8 ns                                                                    | 38.5 ns: 1.11x faster                                               |
| spectral_norm              | 74.9 ms                                                                    | 68.8 ms: 1.09x faster                                               |
| nbody                      | 87.6 ms                                                                    | 81.0 ms: 1.08x faster                                               |
| coroutines                 | 14.9 ms                                                                    | 13.9 ms: 1.08x faster                                               |
| mdp                        | 1.52 sec                                                                   | 1.41 sec: 1.07x faster                                              |
| html5lib                   | 43.0 ms                                                                    | 40.1 ms: 1.07x faster                                               |
| deepcopy_memo              | 21.5 us                                                                    | 20.1 us: 1.07x faster                                               |
| fannkuch                   | 307 ms                                                                     | 288 ms: 1.07x faster                                                |
| scimark_sor                | 96.2 ms                                                                    | 90.4 ms: 1.06x faster                                               |
| hexiom                     | 4.63 ms                                                                    | 4.37 ms: 1.06x faster                                               |
| scimark_monte_carlo        | 51.3 ms                                                                    | 48.4 ms: 1.06x faster                                               |
| bench_mp_pool              | 72.5 ms                                                                    | 68.9 ms: 1.05x faster                                               |
| pickle                     | 7.49 us                                                                    | 7.12 us: 1.05x faster                                               |
| python_startup_no_site     | 18.6 ms                                                                    | 17.8 ms: 1.05x faster                                               |
| pycparser                  | 754 ms                                                                     | 720 ms: 1.05x faster                                                |
| comprehensions             | 12.3 us                                                                    | 11.8 us: 1.04x faster                                               |
| scimark_sparse_mat_mult    | 2.84 ms                                                                    | 2.72 ms: 1.04x faster                                               |
| logging_silent             | 65.9 ns                                                                    | 63.1 ns: 1.04x faster                                               |
| mako                       | 7.23 ms                                                                    | 6.93 ms: 1.04x faster                                               |
| scimark_fft                | 214 ms                                                                     | 205 ms: 1.04x faster                                                |
| meteor_contest             | 79.5 ms                                                                    | 76.3 ms: 1.04x faster                                               |
| async_tree_cpu_io_mixed_tg | 400 ms                                                                     | 384 ms: 1.04x faster                                                |
| regex_dna                  | 118 ms                                                                     | 114 ms: 1.04x faster                                                |
| unpickle_list              | 2.83 us                                                                    | 2.74 us: 1.03x faster                                               |
| unpickle_pure_python       | 155 us                                                                     | 150 us: 1.03x faster                                                |
| xml_etree_process          | 42.1 ms                                                                    | 40.7 ms: 1.03x faster                                               |
| xml_etree_iterparse        | 66.6 ms                                                                    | 64.4 ms: 1.03x faster                                               |
| django_template            | 25.6 ms                                                                    | 24.8 ms: 1.03x faster                                               |
| crypto_pyaes               | 50.9 ms                                                                    | 49.3 ms: 1.03x faster                                               |
| scimark_lu                 | 67.9 ms                                                                    | 65.8 ms: 1.03x faster                                               |
| sqlglot_parse              | 908 us                                                                     | 880 us: 1.03x faster                                                |
| chaos                      | 44.8 ms                                                                    | 43.5 ms: 1.03x faster                                               |
| pprint_pformat             | 1.14 sec                                                                   | 1.11 sec: 1.03x faster                                              |
| pyflate                    | 329 ms                                                                     | 319 ms: 1.03x faster                                                |
| python_startup             | 22.7 ms                                                                    | 22.1 ms: 1.03x faster                                               |
| regex_compile              | 93.0 ms                                                                    | 90.4 ms: 1.03x faster                                               |
| tomli_loads                | 1.62 sec                                                                   | 1.58 sec: 1.03x faster                                              |
| sqlglot_transpile          | 1.13 ms                                                                    | 1.10 ms: 1.03x faster                                               |
| regex_effbot               | 1.59 ms                                                                    | 1.54 ms: 1.03x faster                                               |
| thrift                     | 527 us                                                                     | 513 us: 1.03x faster                                                |
| regex_v8                   | 15.0 ms                                                                    | 14.7 ms: 1.03x faster                                               |
| xml_etree_generate         | 59.5 ms                                                                    | 58.0 ms: 1.02x faster                                               |
| unpickle                   | 9.52 us                                                                    | 9.30 us: 1.02x faster                                               |
| generators                 | 21.4 ms                                                                    | 20.9 ms: 1.02x faster                                               |
| pprint_safe_repr           | 554 ms                                                                     | 542 ms: 1.02x faster                                                |
| logging_simple             | 6.47 us                                                                    | 6.33 us: 1.02x faster                                               |
| go                         | 88.9 ms                                                                    | 87.1 ms: 1.02x faster                                               |
| sqlglot_normalize          | 195 ms                                                                     | 192 ms: 1.02x faster                                                |
| genshi_text                | 17.1 ms                                                                    | 16.8 ms: 1.02x faster                                               |
| float                      | 56.9 ms                                                                    | 56.0 ms: 1.02x faster                                               |
| pickle_pure_python         | 218 us                                                                     | 215 us: 1.02x faster                                                |
| richards_super             | 36.8 ms                                                                    | 36.2 ms: 1.02x faster                                               |
| deepcopy                   | 188 us                                                                     | 185 us: 1.01x faster                                                |
| sqlglot_optimize           | 36.8 ms                                                                    | 36.3 ms: 1.01x faster                                               |
| nqueens                    | 65.5 ms                                                                    | 64.6 ms: 1.01x faster                                               |
| richards                   | 32.6 ms                                                                    | 32.2 ms: 1.01x faster                                               |
| deltablue                  | 2.31 ms                                                                    | 2.28 ms: 1.01x faster                                               |
| genshi_xml                 | 36.0 ms                                                                    | 35.6 ms: 1.01x faster                                               |
| xml_etree_parse            | 94.4 ms                                                                    | 93.5 ms: 1.01x faster                                               |
| async_generators           | 248 ms                                                                     | 246 ms: 1.01x faster                                                |
| telco                      | 4.87 ms                                                                    | 4.84 ms: 1.01x faster                                               |
| sympy_integrate            | 13.5 ms                                                                    | 13.4 ms: 1.01x faster                                               |
| sqlite_synth               | 1.64 us                                                                    | 1.63 us: 1.01x faster                                               |
| sympy_sum                  | 90.4 ms                                                                    | 90.0 ms: 1.00x faster                                               |
| sympy_expand               | 308 ms                                                                     | 307 ms: 1.00x faster                                                |
| pickle_dict                | 18.3 us                                                                    | 18.4 us: 1.00x slower                                               |
| pickle_list                | 2.88 us                                                                    | 2.90 us: 1.01x slower                                               |
| deepcopy_reduce            | 1.91 us                                                                    | 1.95 us: 1.02x slower                                               |
| gc_traversal               | 1.53 ms                                                                    | 1.57 ms: 1.02x slower                                               |
| coverage                   | 47.9 ms                                                                    | 49.2 ms: 1.03x slower                                               |
| create_gc_cycles           | 884 us                                                                     | 917 us: 1.04x slower                                                |
| Geometric mean             | (ref)                                                                      | 1.02x faster                                                        |

Benchmark hidden because not significant (24): async_tree_none, pylint, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_io, 2to3, json_loads, bench_thread_pool, logging_format, sympy_str, asyncio_tcp, raytrace, docutils, typing_runtime_protocols, json_dumps, pidigits, async_tree_io_tg, dulwich_log, tornado_http, pathlib, async_tree_memoization_tg, async_tree_memoization, json, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.022x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown