# Results vs. 3.13.0b2

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: darwin-arm64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.00x slower
- HPT reliability: 85.61%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.56x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| chameleon      | 4.27 ms                                                    | 4.33 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                      | 1.00x slower                                                          |

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_tg              | 41.4 ms                                                    | 41.5 ms: 1.00x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 332 ms: 1.00x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 360 ms: 1.01x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 61.0 ms: 1.01x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.01x slower                                                          |

Benchmark hidden because not significant (12): async_tree_none_tg, async_tree_memoization_tg, async_tree_io_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_memoization, async_tree_eager_io, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 282 ms                                                     | 281 ms: 1.00x faster                                                  |
| nbody          | 59.6 ms                                                    | 59.9 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                      | 1.00x slower                                                          |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.56 ms: 1.01x faster                                                 |
| regex_compile  | 68.5 ms                                                    | 68.3 ms: 1.00x faster                                                 |
| regex_dna      | 149 ms                                                     | 149 ms: 1.00x slower                                                  |
| regex_v8       | 17.3 ms                                                    | 17.7 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                      | 1.00x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 106 ms                                                     | 103 ms: 1.02x faster                                                  |
| xml_etree_generate   | 52.7 ms                                                    | 51.8 ms: 1.02x faster                                                 |
| pickle               | 7.48 us                                                    | 7.36 us: 1.02x faster                                                 |
| tomli_loads          | 1.47 sec                                                   | 1.45 sec: 1.01x faster                                                |
| xml_etree_process    | 37.1 ms                                                    | 36.8 ms: 1.01x faster                                                 |
| unpickle_list        | 2.88 us                                                    | 2.86 us: 1.01x faster                                                 |
| pickle_dict          | 18.3 us                                                    | 18.2 us: 1.00x faster                                                 |
| json_loads           | 16.8 us                                                    | 16.9 us: 1.01x slower                                                 |
| pickle_list          | 2.96 us                                                    | 2.98 us: 1.01x slower                                                 |
| unpickle_pure_python | 141 us                                                     | 142 us: 1.01x slower                                                  |
| pickle_pure_python   | 179 us                                                     | 180 us: 1.01x slower                                                  |
| json_dumps           | 6.23 ms                                                    | 6.32 ms: 1.01x slower                                                 |
| unpickle             | 9.12 us                                                    | 9.28 us: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.00x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 14.9 ms: 1.02x faster                                                 |
| python_startup_no_site | 12.3 ms                                                    | 12.2 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 29.9 ms                                                    | 29.8 ms: 1.00x faster                                                 |
| genshi_text     | 13.9 ms                                                    | 13.8 ms: 1.00x faster                                                 |
| django_template | 19.4 ms                                                    | 19.6 ms: 1.01x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.00x faster                                                          |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| flaskblogging                    | 3.61 ms                                                    | 3.35 ms: 1.08x faster                                                 |
| pathlib                          | 23.3 ms                                                    | 21.9 ms: 1.07x faster                                                 |
| mdp                              | 1.53 sec                                                   | 1.48 sec: 1.03x faster                                                |
| thrift                           | 435 us                                                     | 424 us: 1.03x faster                                                  |
| xml_etree_parse                  | 106 ms                                                     | 103 ms: 1.02x faster                                                  |
| python_startup                   | 15.2 ms                                                    | 14.9 ms: 1.02x faster                                                 |
| deepcopy_reduce                  | 1.82 us                                                    | 1.79 us: 1.02x faster                                                 |
| xml_etree_generate               | 52.7 ms                                                    | 51.8 ms: 1.02x faster                                                 |
| pickle                           | 7.48 us                                                    | 7.36 us: 1.02x faster                                                 |
| bench_mp_pool                    | 47.2 ms                                                    | 46.5 ms: 1.02x faster                                                 |
| telco                            | 4.60 ms                                                    | 4.53 ms: 1.01x faster                                                 |
| pprint_safe_repr                 | 465 ms                                                     | 459 ms: 1.01x faster                                                  |
| python_startup_no_site           | 12.3 ms                                                    | 12.2 ms: 1.01x faster                                                 |
| pprint_pformat                   | 947 ms                                                     | 937 ms: 1.01x faster                                                  |
| deepcopy                         | 204 us                                                     | 202 us: 1.01x faster                                                  |
| sqlite_synth                     | 1.55 us                                                    | 1.54 us: 1.01x faster                                                 |
| richards_super                   | 35.2 ms                                                    | 34.9 ms: 1.01x faster                                                 |
| tomli_loads                      | 1.47 sec                                                   | 1.45 sec: 1.01x faster                                                |
| regex_effbot                     | 2.58 ms                                                    | 2.56 ms: 1.01x faster                                                 |
| xml_etree_process                | 37.1 ms                                                    | 36.8 ms: 1.01x faster                                                 |
| unpickle_list                    | 2.88 us                                                    | 2.86 us: 1.01x faster                                                 |
| async_generators                 | 281 ms                                                     | 279 ms: 1.01x faster                                                  |
| go                               | 101 ms                                                     | 100 ms: 1.01x faster                                                  |
| genshi_xml                       | 29.9 ms                                                    | 29.8 ms: 1.00x faster                                                 |
| genshi_text                      | 13.9 ms                                                    | 13.8 ms: 1.00x faster                                                 |
| logging_simple                   | 3.04 us                                                    | 3.03 us: 1.00x faster                                                 |
| generators                       | 22.9 ms                                                    | 22.8 ms: 1.00x faster                                                 |
| regex_compile                    | 68.5 ms                                                    | 68.3 ms: 1.00x faster                                                 |
| pickle_dict                      | 18.3 us                                                    | 18.2 us: 1.00x faster                                                 |
| logging_silent                   | 60.1 ns                                                    | 60.0 ns: 1.00x faster                                                 |
| scimark_monte_carlo              | 42.5 ms                                                    | 42.3 ms: 1.00x faster                                                 |
| scimark_lu                       | 66.9 ms                                                    | 66.7 ms: 1.00x faster                                                 |
| pidigits                         | 282 ms                                                     | 281 ms: 1.00x faster                                                  |
| asyncio_websockets               | 409 ms                                                     | 408 ms: 1.00x faster                                                  |
| regex_dna                        | 149 ms                                                     | 149 ms: 1.00x slower                                                  |
| meteor_contest                   | 70.3 ms                                                    | 70.4 ms: 1.00x slower                                                 |
| deltablue                        | 2.14 ms                                                    | 2.14 ms: 1.00x slower                                                 |
| create_gc_cycles                 | 897 us                                                     | 900 us: 1.00x slower                                                  |
| sympy_expand                     | 226 ms                                                     | 227 ms: 1.00x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.5 ms: 1.00x slower                                                 |
| logging_format                   | 3.31 us                                                    | 3.32 us: 1.00x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 332 ms: 1.00x slower                                                  |
| sqlglot_optimize                 | 30.9 ms                                                    | 31.0 ms: 1.00x slower                                                 |
| coroutines                       | 15.8 ms                                                    | 15.9 ms: 1.00x slower                                                 |
| nbody                            | 59.6 ms                                                    | 59.9 ms: 1.00x slower                                                 |
| hexiom                           | 4.06 ms                                                    | 4.08 ms: 1.00x slower                                                 |
| raytrace                         | 147 ms                                                     | 148 ms: 1.01x slower                                                  |
| json_loads                       | 16.8 us                                                    | 16.9 us: 1.01x slower                                                 |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.79 ms: 1.01x slower                                                 |
| scimark_sor                      | 94.9 ms                                                    | 95.4 ms: 1.01x slower                                                 |
| gc_traversal                     | 2.45 ms                                                    | 2.46 ms: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 360 ms: 1.01x slower                                                  |
| pickle_list                      | 2.96 us                                                    | 2.98 us: 1.01x slower                                                 |
| coverage                         | 45.0 ms                                                    | 45.3 ms: 1.01x slower                                                 |
| crypto_pyaes                     | 49.5 ms                                                    | 49.8 ms: 1.01x slower                                                 |
| django_template                  | 19.4 ms                                                    | 19.6 ms: 1.01x slower                                                 |
| unpickle_pure_python             | 141 us                                                     | 142 us: 1.01x slower                                                  |
| pickle_pure_python               | 179 us                                                     | 180 us: 1.01x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 61.0 ms: 1.01x slower                                                 |
| nqueens                          | 52.2 ms                                                    | 52.8 ms: 1.01x slower                                                 |
| sqlglot_normalize                | 166 ms                                                     | 167 ms: 1.01x slower                                                  |
| spectral_norm                    | 66.4 ms                                                    | 67.2 ms: 1.01x slower                                                 |
| chameleon                        | 4.27 ms                                                    | 4.33 ms: 1.01x slower                                                 |
| json_dumps                       | 6.23 ms                                                    | 6.32 ms: 1.01x slower                                                 |
| unpickle                         | 9.12 us                                                    | 9.28 us: 1.02x slower                                                 |
| regex_v8                         | 17.3 ms                                                    | 17.7 ms: 1.02x slower                                                 |
| fannkuch                         | 248 ms                                                     | 257 ms: 1.04x slower                                                  |
| bench_thread_pool                | 447 us                                                     | 463 us: 1.04x slower                                                  |
| typing_runtime_protocols         | 87.6 us                                                    | 91.2 us: 1.04x slower                                                 |
| chaos                            | 34.0 ms                                                    | 35.5 ms: 1.04x slower                                                 |
| comprehensions                   | 10.2 us                                                    | 10.7 us: 1.05x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.00x slower                                                          |

Benchmark hidden because not significant (34): async_tree_none_tg, async_tree_memoization_tg, async_tree_io_tg, dask, 2to3, asyncio_tcp_ssl, sympy_sum, html5lib, async_tree_eager_io_tg, sympy_str, async_tree_eager_memoization_tg, async_tree_cpu_io_mixed_tg, json, docutils, pycparser, sqlglot_parse, deepcopy_memo, sympy_integrate, pyflate, richards, mako, tornado_http, async_tree_eager_memoization, sqlglot_transpile, scimark_fft, float, xml_etree_iterparse, pylint, async_tree_eager_io, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none, async_tree_io, asyncio_tcp
Ignored benchmarks (5) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, dulwich_log, gunicorn, mypy2

# HPT report

- Reliability score: 85.61% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.56x