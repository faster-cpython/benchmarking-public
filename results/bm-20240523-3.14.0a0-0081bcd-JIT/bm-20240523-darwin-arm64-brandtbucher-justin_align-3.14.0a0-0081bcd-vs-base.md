# Results vs. base

- fork: brandtbucher
- ref: justin_align
- machine: darwin-arm64
- commit hash: 0081bcd
- commit date: 2024-05-23
- overall geometric mean: 1.00x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240522-darwin-arm64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-darwin-arm64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| chameleon      | 4.40 ms                                                               | 4.44 ms: 1.01x slower                                               |
| html5lib       | 31.0 ms                                                               | 30.8 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                        |

Benchmark hidden because not significant (3): 2to3, docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240522-darwin-arm64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-darwin-arm64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_eager                 | 63.8 ms                                                               | 62.8 ms: 1.02x faster                                               |
| async_tree_eager_tg              | 42.2 ms                                                               | 41.9 ms: 1.01x faster                                               |
| async_tree_eager_cpu_io_mixed_tg | 330 ms                                                                | 332 ms: 1.01x slower                                                |
| Geometric mean                   | (ref)                                                                 | 1.00x faster                                                        |

Benchmark hidden because not significant (13): async_tree_eager_io, async_tree_eager_memoization, async_tree_io, async_tree_none, async_tree_memoization, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_io_tg, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240522-darwin-arm64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-darwin-arm64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_dna      | 152 ms                                                                | 149 ms: 1.02x faster                                                |
| regex_effbot   | 2.58 ms                                                               | 2.57 ms: 1.00x faster                                               |
| regex_compile  | 71.9 ms                                                               | 71.7 ms: 1.00x faster                                               |
| regex_v8       | 17.4 ms                                                               | 17.4 ms: 1.00x slower                                               |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240522-darwin-arm64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-darwin-arm64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 6.24 ms                                                               | 6.07 ms: 1.03x faster                                               |
| unpickle_list        | 2.87 us                                                               | 2.83 us: 1.01x faster                                               |
| xml_etree_parse      | 104 ms                                                                | 103 ms: 1.01x faster                                                |
| tomli_loads          | 1.25 sec                                                              | 1.24 sec: 1.01x faster                                              |
| xml_etree_process    | 35.6 ms                                                               | 35.4 ms: 1.01x faster                                               |
| unpickle_pure_python | 132 us                                                                | 131 us: 1.00x faster                                                |
| pickle_pure_python   | 173 us                                                                | 172 us: 1.00x faster                                                |
| pickle_dict          | 18.2 us                                                               | 18.1 us: 1.00x faster                                               |
| pickle               | 7.43 us                                                               | 7.46 us: 1.00x slower                                               |
| pickle_list          | 2.97 us                                                               | 2.98 us: 1.00x slower                                               |
| xml_etree_generate   | 50.7 ms                                                               | 51.1 ms: 1.01x slower                                               |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                        |

Benchmark hidden because not significant (3): unpickle, json_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240522-darwin-arm64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-darwin-arm64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 13.4 ms                                                               | 13.2 ms: 1.01x faster                                               |
| python_startup         | 15.8 ms                                                               | 15.7 ms: 1.01x faster                                               |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240522-darwin-arm64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-darwin-arm64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 16.4 ms                                                               | 16.1 ms: 1.01x faster                                               |
| django_template | 21.3 ms                                                               | 21.0 ms: 1.01x faster                                               |
| mako            | 6.38 ms                                                               | 6.40 ms: 1.00x slower                                               |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                        |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                        | bm-20240522-darwin-arm64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-darwin-arm64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| fannkuch                         | 242 ms                                                                | 234 ms: 1.03x faster                                                |
| json_dumps                       | 6.24 ms                                                               | 6.07 ms: 1.03x faster                                               |
| logging_silent                   | 63.0 ns                                                               | 61.8 ns: 1.02x faster                                               |
| regex_dna                        | 152 ms                                                                | 149 ms: 1.02x faster                                                |
| meteor_contest                   | 72.6 ms                                                               | 71.5 ms: 1.02x faster                                               |
| raytrace                         | 164 ms                                                                | 162 ms: 1.02x faster                                                |
| async_tree_eager                 | 63.8 ms                                                               | 62.8 ms: 1.02x faster                                               |
| genshi_text                      | 16.4 ms                                                               | 16.1 ms: 1.01x faster                                               |
| python_startup_no_site           | 13.4 ms                                                               | 13.2 ms: 1.01x faster                                               |
| unpickle_list                    | 2.87 us                                                               | 2.83 us: 1.01x faster                                               |
| telco                            | 4.60 ms                                                               | 4.55 ms: 1.01x faster                                               |
| xml_etree_parse                  | 104 ms                                                                | 103 ms: 1.01x faster                                                |
| sympy_sum                        | 72.8 ms                                                               | 71.9 ms: 1.01x faster                                               |
| django_template                  | 21.3 ms                                                               | 21.0 ms: 1.01x faster                                               |
| coverage                         | 45.8 ms                                                               | 45.3 ms: 1.01x faster                                               |
| hexiom                           | 4.40 ms                                                               | 4.36 ms: 1.01x faster                                               |
| deepcopy                         | 206 us                                                                | 204 us: 1.01x faster                                                |
| typing_runtime_protocols         | 94.4 us                                                               | 93.5 us: 1.01x faster                                               |
| pyflate                          | 315 ms                                                                | 312 ms: 1.01x faster                                                |
| generators                       | 23.4 ms                                                               | 23.2 ms: 1.01x faster                                               |
| python_startup                   | 15.8 ms                                                               | 15.7 ms: 1.01x faster                                               |
| sqlglot_optimize                 | 33.0 ms                                                               | 32.7 ms: 1.01x faster                                               |
| chaos                            | 39.1 ms                                                               | 38.8 ms: 1.01x faster                                               |
| sympy_str                        | 137 ms                                                                | 136 ms: 1.01x faster                                                |
| scimark_monte_carlo              | 44.2 ms                                                               | 43.9 ms: 1.01x faster                                               |
| html5lib                         | 31.0 ms                                                               | 30.8 ms: 1.01x faster                                               |
| mdp                              | 1.52 sec                                                              | 1.51 sec: 1.01x faster                                              |
| async_tree_eager_tg              | 42.2 ms                                                               | 41.9 ms: 1.01x faster                                               |
| tomli_loads                      | 1.25 sec                                                              | 1.24 sec: 1.01x faster                                              |
| xml_etree_process                | 35.6 ms                                                               | 35.4 ms: 1.01x faster                                               |
| deepcopy_memo                    | 21.5 us                                                               | 21.4 us: 1.01x faster                                               |
| unpickle_pure_python             | 132 us                                                                | 131 us: 1.00x faster                                                |
| sympy_integrate                  | 10.9 ms                                                               | 10.8 ms: 1.00x faster                                               |
| scimark_fft                      | 185 ms                                                                | 184 ms: 1.00x faster                                                |
| crypto_pyaes                     | 52.1 ms                                                               | 51.9 ms: 1.00x faster                                               |
| pickle_pure_python               | 173 us                                                                | 172 us: 1.00x faster                                                |
| sympy_expand                     | 236 ms                                                                | 235 ms: 1.00x faster                                                |
| comprehensions                   | 12.2 us                                                               | 12.2 us: 1.00x faster                                               |
| regex_effbot                     | 2.58 ms                                                               | 2.57 ms: 1.00x faster                                               |
| richards_super                   | 35.0 ms                                                               | 34.9 ms: 1.00x faster                                               |
| asyncio_websockets               | 410 ms                                                                | 409 ms: 1.00x faster                                                |
| regex_compile                    | 71.9 ms                                                               | 71.7 ms: 1.00x faster                                               |
| pickle_dict                      | 18.2 us                                                               | 18.1 us: 1.00x faster                                               |
| gc_traversal                     | 2.47 ms                                                               | 2.47 ms: 1.00x faster                                               |
| spectral_norm                    | 67.2 ms                                                               | 67.1 ms: 1.00x faster                                               |
| scimark_sparse_mat_mult          | 2.90 ms                                                               | 2.91 ms: 1.00x slower                                               |
| thrift                           | 433 us                                                                | 434 us: 1.00x slower                                                |
| mako                             | 6.38 ms                                                               | 6.40 ms: 1.00x slower                                               |
| pickle                           | 7.43 us                                                               | 7.46 us: 1.00x slower                                               |
| pprint_pformat                   | 944 ms                                                                | 947 ms: 1.00x slower                                                |
| logging_format                   | 3.28 us                                                               | 3.29 us: 1.00x slower                                               |
| pprint_safe_repr                 | 455 ms                                                                | 457 ms: 1.00x slower                                                |
| pickle_list                      | 2.97 us                                                               | 2.98 us: 1.00x slower                                               |
| bench_thread_pool                | 481 us                                                                | 483 us: 1.00x slower                                                |
| regex_v8                         | 17.4 ms                                                               | 17.4 ms: 1.00x slower                                               |
| async_generators                 | 293 ms                                                                | 295 ms: 1.01x slower                                                |
| create_gc_cycles                 | 913 us                                                                | 919 us: 1.01x slower                                                |
| async_tree_eager_cpu_io_mixed_tg | 330 ms                                                                | 332 ms: 1.01x slower                                                |
| logging_simple                   | 3.00 us                                                               | 3.03 us: 1.01x slower                                               |
| xml_etree_generate               | 50.7 ms                                                               | 51.1 ms: 1.01x slower                                               |
| go                               | 102 ms                                                                | 103 ms: 1.01x slower                                                |
| chameleon                        | 4.40 ms                                                               | 4.44 ms: 1.01x slower                                               |
| json                             | 2.91 ms                                                               | 2.94 ms: 1.01x slower                                               |
| Geometric mean                   | (ref)                                                                 | 1.00x faster                                                        |

Benchmark hidden because not significant (41): asyncio_tcp, async_tree_eager_io, async_tree_eager_memoization, async_tree_io, async_tree_none, dask, unpickle, async_tree_memoization, async_tree_eager_io_tg, async_tree_eager_memoization_tg, flaskblogging, asyncio_tcp_ssl, async_tree_io_tg, async_tree_none_tg, pycparser, pathlib, genshi_xml, pylint, sqlite_synth, richards, scimark_lu, async_tree_memoization_tg, 2to3, coroutines, bench_mp_pool, nbody, nqueens, sqlglot_parse, sqlglot_transpile, float, pidigits, scimark_sor, json_loads, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, docutils, deepcopy_reduce, xml_etree_iterparse, deltablue, async_tree_eager_cpu_io_mixed, tornado_http

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x