# Results vs. 3.13.0

- fork: mdboom
- ref: pysequence_tuple
- machine: darwin-arm64
- commit hash: 3b5fdc8
- commit date: 2024-09-11
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 158 ms: 1.13x faster                                              |
| docutils       | 1.44 sec                                               | 1.43 sec: 1.01x faster                                            |
| html5lib       | 36.6 ms                                                | 30.3 ms: 1.21x faster                                             |
| Geometric mean | (ref)                                                  | 1.07x faster                                                      |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.1 ms: 1.23x faster                                             |
| async_tree_eager                 | 70.5 ms                                                | 61.1 ms: 1.15x faster                                             |
| async_tree_eager_tg              | 48.4 ms                                                | 42.5 ms: 1.14x faster                                             |
| async_tree_memoization_tg        | 291 ms                                                 | 257 ms: 1.13x faster                                              |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 123 ms: 1.13x faster                                              |
| async_tree_eager_memoization     | 169 ms                                                 | 153 ms: 1.11x faster                                              |
| async_tree_memoization           | 270 ms                                                 | 247 ms: 1.09x faster                                              |
| asyncio_tcp                      | 457 ms                                                 | 419 ms: 1.09x faster                                              |
| async_tree_none                  | 212 ms                                                 | 199 ms: 1.07x faster                                              |
| async_tree_none_tg               | 198 ms                                                 | 188 ms: 1.06x faster                                              |
| async_generators                 | 294 ms                                                 | 279 ms: 1.06x faster                                              |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 361 ms: 1.04x faster                                              |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 336 ms: 1.04x faster                                              |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.29 sec: 1.02x slower                                            |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 463 ms: 1.03x slower                                              |
| async_tree_io_tg                 | 500 ms                                                 | 543 ms: 1.09x slower                                              |
| async_tree_io                    | 507 ms                                                 | 581 ms: 1.15x slower                                              |
| async_tree_eager_io              | 513 ms                                                 | 682 ms: 1.33x slower                                              |
| async_tree_eager_io_tg           | 477 ms                                                 | 705 ms: 1.48x slower                                              |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                              |
| Geometric mean                   | (ref)                                                  | 1.01x slower                                                      |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 73.9 ms                                                | 60.7 ms: 1.22x faster                                             |
| float          | 56.2 ms                                                | 49.2 ms: 1.14x faster                                             |
| pidigits       | 284 ms                                                 | 282 ms: 1.00x faster                                              |
| Geometric mean | (ref)                                                  | 1.12x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 67.2 ms: 1.17x faster                                             |
| regex_effbot   | 2.63 ms                                                | 2.46 ms: 1.07x faster                                             |
| regex_v8       | 16.9 ms                                                | 16.6 ms: 1.02x faster                                             |
| regex_dna      | 148 ms                                                 | 145 ms: 1.02x faster                                              |
| Geometric mean | (ref)                                                  | 1.07x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| pickle_pure_python   | 213 us                                                 | 182 us: 1.17x faster                                              |
| unpickle_pure_python | 163 us                                                 | 141 us: 1.16x faster                                              |
| xml_etree_process    | 40.9 ms                                                | 37.4 ms: 1.09x faster                                             |
| xml_etree_generate   | 56.6 ms                                                | 53.1 ms: 1.07x faster                                             |
| tomli_loads          | 1.56 sec                                               | 1.50 sec: 1.04x faster                                            |
| json_dumps           | 6.56 ms                                                | 6.41 ms: 1.02x faster                                             |
| pickle_list          | 2.99 us                                                | 2.95 us: 1.01x faster                                             |
| unpickle_list        | 2.93 us                                                | 2.91 us: 1.01x faster                                             |
| pickle               | 7.36 us                                                | 7.38 us: 1.00x slower                                             |
| unpickle             | 9.15 us                                                | 9.21 us: 1.01x slower                                             |
| pickle_dict          | 18.2 us                                                | 18.3 us: 1.01x slower                                             |
| json_loads           | 16.9 us                                                | 17.1 us: 1.02x slower                                             |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                      |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup | 17.0 ms                                                | 17.0 ms: 1.00x faster                                             |
| Geometric mean | (ref)                                                  | 1.00x slower                                                      |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 14.0 ms: 1.21x faster                                             |
| django_template | 22.2 ms                                                | 19.6 ms: 1.13x faster                                             |
| genshi_xml      | 34.4 ms                                                | 30.5 ms: 1.13x faster                                             |
| mako            | 7.68 ms                                                | 7.00 ms: 1.10x faster                                             |
| Geometric mean  | (ref)                                                  | 1.14x faster                                                      |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| deepcopy_memo                    | 27.2 us                                                | 16.5 us: 1.65x faster                                             |
| deepcopy                         | 232 us                                                 | 145 us: 1.61x faster                                              |
| generators                       | 31.5 ms                                                | 20.4 ms: 1.55x faster                                             |
| go                               | 115 ms                                                 | 79.2 ms: 1.45x faster                                             |
| deepcopy_reduce                  | 2.06 us                                                | 1.51 us: 1.37x faster                                             |
| unpack_sequence                  | 36.1 ns                                                | 27.4 ns: 1.32x faster                                             |
| deltablue                        | 2.68 ms                                                | 2.13 ms: 1.26x faster                                             |
| coroutines                       | 19.8 ms                                                | 16.1 ms: 1.23x faster                                             |
| raytrace                         | 182 ms                                                 | 148 ms: 1.22x faster                                              |
| nbody                            | 73.9 ms                                                | 60.7 ms: 1.22x faster                                             |
| comprehensions                   | 12.2 us                                                | 10.0 us: 1.22x faster                                             |
| html5lib                         | 36.6 ms                                                | 30.3 ms: 1.21x faster                                             |
| genshi_text                      | 16.9 ms                                                | 14.0 ms: 1.21x faster                                             |
| logging_simple                   | 3.57 us                                                | 3.01 us: 1.19x faster                                             |
| pprint_safe_repr                 | 531 ms                                                 | 448 ms: 1.19x faster                                              |
| chaos                            | 41.3 ms                                                | 34.9 ms: 1.18x faster                                             |
| hexiom                           | 4.85 ms                                                | 4.11 ms: 1.18x faster                                             |
| nqueens                          | 62.9 ms                                                | 53.3 ms: 1.18x faster                                             |
| pprint_pformat                   | 1.08 sec                                               | 919 ms: 1.17x faster                                              |
| richards                         | 35.4 ms                                                | 30.3 ms: 1.17x faster                                             |
| pickle_pure_python               | 213 us                                                 | 182 us: 1.17x faster                                              |
| richards_super                   | 39.1 ms                                                | 33.5 ms: 1.17x faster                                             |
| regex_compile                    | 78.5 ms                                                | 67.2 ms: 1.17x faster                                             |
| scimark_monte_carlo              | 50.4 ms                                                | 43.4 ms: 1.16x faster                                             |
| logging_format                   | 3.85 us                                                | 3.32 us: 1.16x faster                                             |
| unpickle_pure_python             | 163 us                                                 | 141 us: 1.16x faster                                              |
| logging_silent                   | 69.9 ns                                                | 60.5 ns: 1.16x faster                                             |
| async_tree_eager                 | 70.5 ms                                                | 61.1 ms: 1.15x faster                                             |
| sqlglot_parse                    | 856 us                                                 | 744 us: 1.15x faster                                              |
| spectral_norm                    | 77.3 ms                                                | 67.3 ms: 1.15x faster                                             |
| float                            | 56.2 ms                                                | 49.2 ms: 1.14x faster                                             |
| async_tree_eager_tg              | 48.4 ms                                                | 42.5 ms: 1.14x faster                                             |
| django_template                  | 22.2 ms                                                | 19.6 ms: 1.13x faster                                             |
| scimark_sor                      | 106 ms                                                 | 93.2 ms: 1.13x faster                                             |
| sqlglot_normalize                | 189 ms                                                 | 167 ms: 1.13x faster                                              |
| scimark_lu                       | 76.5 ms                                                | 67.7 ms: 1.13x faster                                             |
| async_tree_memoization_tg        | 291 ms                                                 | 257 ms: 1.13x faster                                              |
| sqlglot_transpile                | 1.02 ms                                                | 907 us: 1.13x faster                                              |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 123 ms: 1.13x faster                                              |
| bench_thread_pool                | 506 us                                                 | 449 us: 1.13x faster                                              |
| genshi_xml                       | 34.4 ms                                                | 30.5 ms: 1.13x faster                                             |
| 2to3                             | 178 ms                                                 | 158 ms: 1.13x faster                                              |
| sqlglot_optimize                 | 34.9 ms                                                | 31.2 ms: 1.12x faster                                             |
| pycparser                        | 706 ms                                                 | 636 ms: 1.11x faster                                              |
| sympy_str                        | 145 ms                                                 | 131 ms: 1.11x faster                                              |
| async_tree_eager_memoization     | 169 ms                                                 | 153 ms: 1.11x faster                                              |
| sympy_integrate                  | 11.3 ms                                                | 10.3 ms: 1.10x faster                                             |
| typing_runtime_protocols         | 101 us                                                 | 91.7 us: 1.10x faster                                             |
| sympy_sum                        | 75.6 ms                                                | 68.9 ms: 1.10x faster                                             |
| mako                             | 7.68 ms                                                | 7.00 ms: 1.10x faster                                             |
| thrift                           | 466 us                                                 | 425 us: 1.10x faster                                              |
| async_tree_memoization           | 270 ms                                                 | 247 ms: 1.09x faster                                              |
| xml_etree_process                | 40.9 ms                                                | 37.4 ms: 1.09x faster                                             |
| asyncio_tcp                      | 457 ms                                                 | 419 ms: 1.09x faster                                              |
| pyflate                          | 351 ms                                                 | 322 ms: 1.09x faster                                              |
| sympy_expand                     | 246 ms                                                 | 226 ms: 1.09x faster                                              |
| fannkuch                         | 282 ms                                                 | 260 ms: 1.08x faster                                              |
| scimark_fft                      | 201 ms                                                 | 186 ms: 1.08x faster                                              |
| crypto_pyaes                     | 54.0 ms                                                | 50.2 ms: 1.08x faster                                             |
| regex_effbot                     | 2.63 ms                                                | 2.46 ms: 1.07x faster                                             |
| xml_etree_generate               | 56.6 ms                                                | 53.1 ms: 1.07x faster                                             |
| async_tree_none                  | 212 ms                                                 | 199 ms: 1.07x faster                                              |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.82 ms: 1.06x faster                                             |
| mdp                              | 1.50 sec                                               | 1.42 sec: 1.06x faster                                            |
| dulwich_log                      | 28.7 ms                                                | 27.1 ms: 1.06x faster                                             |
| async_tree_none_tg               | 198 ms                                                 | 188 ms: 1.06x faster                                              |
| async_generators                 | 294 ms                                                 | 279 ms: 1.06x faster                                              |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 361 ms: 1.04x faster                                              |
| coverage                         | 46.1 ms                                                | 44.4 ms: 1.04x faster                                             |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 336 ms: 1.04x faster                                              |
| tomli_loads                      | 1.56 sec                                               | 1.50 sec: 1.04x faster                                            |
| bench_mp_pool                    | 50.9 ms                                                | 49.2 ms: 1.03x faster                                             |
| bpe_tokeniser                    | 3.24 sec                                               | 3.14 sec: 1.03x faster                                            |
| meteor_contest                   | 73.8 ms                                                | 71.5 ms: 1.03x faster                                             |
| json_dumps                       | 6.56 ms                                                | 6.41 ms: 1.02x faster                                             |
| regex_v8                         | 16.9 ms                                                | 16.6 ms: 1.02x faster                                             |
| regex_dna                        | 148 ms                                                 | 145 ms: 1.02x faster                                              |
| docutils                         | 1.44 sec                                               | 1.43 sec: 1.01x faster                                            |
| pickle_list                      | 2.99 us                                                | 2.95 us: 1.01x faster                                             |
| gc_traversal                     | 2.48 ms                                                | 2.45 ms: 1.01x faster                                             |
| unpickle_list                    | 2.93 us                                                | 2.91 us: 1.01x faster                                             |
| pidigits                         | 284 ms                                                 | 282 ms: 1.00x faster                                              |
| python_startup                   | 17.0 ms                                                | 17.0 ms: 1.00x faster                                             |
| pickle                           | 7.36 us                                                | 7.38 us: 1.00x slower                                             |
| unpickle                         | 9.15 us                                                | 9.21 us: 1.01x slower                                             |
| sqlite_synth                     | 1.54 us                                                | 1.56 us: 1.01x slower                                             |
| pickle_dict                      | 18.2 us                                                | 18.3 us: 1.01x slower                                             |
| json                             | 2.94 ms                                                | 2.97 ms: 1.01x slower                                             |
| json_loads                       | 16.9 us                                                | 17.1 us: 1.02x slower                                             |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.29 sec: 1.02x slower                                            |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 463 ms: 1.03x slower                                              |
| pathlib                          | 22.8 ms                                                | 23.8 ms: 1.05x slower                                             |
| async_tree_io_tg                 | 500 ms                                                 | 543 ms: 1.09x slower                                              |
| create_gc_cycles                 | 803 us                                                 | 892 us: 1.11x slower                                              |
| async_tree_io                    | 507 ms                                                 | 581 ms: 1.15x slower                                              |
| async_tree_eager_io              | 513 ms                                                 | 682 ms: 1.33x slower                                              |
| async_tree_eager_io_tg           | 477 ms                                                 | 705 ms: 1.48x slower                                              |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                              |
| Geometric mean                   | (ref)                                                  | 1.09x faster                                                      |

Benchmark hidden because not significant (7): xml_etree_iterparse, pylint, async_tree_cpu_io_mixed, xml_etree_parse, telco, python_startup_no_site, tornado_http
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 0.99x