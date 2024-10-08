# Results vs. 3.13.0b2

- fork: mdboom
- ref: rc1_mdboom
- machine: darwin-arm64
- commit hash: 2a88001
- commit date: 2024-08-26
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: 0.42x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-darwin-arm64-mdboom-rc1_mdboom-3.13.0rc1-2a88001 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 200 ms: 1.24x slower                                         |
| chameleon      | 4.27 ms                                                    | 4.65 ms: 1.09x slower                                        |
| docutils       | 1.44 sec                                                   | 1.54 sec: 1.07x slower                                       |
| html5lib       | 31.2 ms                                                    | 33.3 ms: 1.07x slower                                        |
| tornado_http   | 66.7 ms                                                    | 84.8 ms: 1.27x slower                                        |
| Geometric mean | (ref)                                                      | 1.15x slower                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-darwin-arm64-mdboom-rc1_mdboom-3.13.0rc1-2a88001 |
|----------------------------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 338 ms: 1.02x slower                                         |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 464 ms: 1.03x slower                                         |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 370 ms: 1.03x slower                                         |
| async_tree_eager_io_tg           | 768 ms                                                     | 794 ms: 1.03x slower                                         |
| async_tree_eager_io              | 766 ms                                                     | 796 ms: 1.04x slower                                         |
| async_tree_io_tg                 | 565 ms                                                     | 587 ms: 1.04x slower                                         |
| async_tree_io                    | 563 ms                                                     | 587 ms: 1.04x slower                                         |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 488 ms: 1.04x slower                                         |
| async_tree_memoization           | 260 ms                                                     | 279 ms: 1.07x slower                                         |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 135 ms: 1.08x slower                                         |
| async_tree_none_tg               | 198 ms                                                     | 213 ms: 1.08x slower                                         |
| async_tree_eager_memoization     | 152 ms                                                     | 165 ms: 1.08x slower                                         |
| async_tree_none                  | 209 ms                                                     | 227 ms: 1.08x slower                                         |
| async_tree_memoization_tg        | 240 ms                                                     | 267 ms: 1.12x slower                                         |
| async_tree_eager_tg              | 41.4 ms                                                    | 47.9 ms: 1.16x slower                                        |
| async_tree_eager                 | 60.3 ms                                                    | 70.7 ms: 1.17x slower                                        |
| Geometric mean                   | (ref)                                                      | 1.07x slower                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-darwin-arm64-mdboom-rc1_mdboom-3.13.0rc1-2a88001 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| pidigits       | 282 ms                                                     | 283 ms: 1.00x slower                                         |
| float          | 48.6 ms                                                    | 51.4 ms: 1.06x slower                                        |
| nbody          | 59.6 ms                                                    | 66.0 ms: 1.11x slower                                        |
| Geometric mean | (ref)                                                      | 1.05x slower                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-darwin-arm64-mdboom-rc1_mdboom-3.13.0rc1-2a88001 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| regex_dna      | 149 ms                                                     | 144 ms: 1.04x faster                                         |
| regex_v8       | 17.3 ms                                                    | 16.8 ms: 1.03x faster                                        |
| regex_effbot   | 2.58 ms                                                    | 2.55 ms: 1.02x faster                                        |
| regex_compile  | 68.5 ms                                                    | 73.9 ms: 1.08x slower                                        |
| Geometric mean | (ref)                                                      | 1.00x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-darwin-arm64-mdboom-rc1_mdboom-3.13.0rc1-2a88001 |
|----------------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| xml_etree_parse      | 106 ms                                                     | 108 ms: 1.02x slower                                         |
| xml_etree_iterparse  | 71.5 ms                                                    | 74.4 ms: 1.04x slower                                        |
| json_loads           | 16.8 us                                                    | 17.8 us: 1.06x slower                                        |
| json_dumps           | 6.23 ms                                                    | 6.65 ms: 1.07x slower                                        |
| tomli_loads          | 1.47 sec                                                   | 1.56 sec: 1.07x slower                                       |
| pickle_pure_python   | 179 us                                                     | 191 us: 1.07x slower                                         |
| unpickle_pure_python | 141 us                                                     | 152 us: 1.08x slower                                         |
| xml_etree_generate   | 52.7 ms                                                    | 59.9 ms: 1.14x slower                                        |
| xml_etree_process    | 37.1 ms                                                    | 42.2 ms: 1.14x slower                                        |
| Geometric mean       | (ref)                                                      | 1.07x slower                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-darwin-arm64-mdboom-rc1_mdboom-3.13.0rc1-2a88001 |
|------------------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 15.9 ms: 1.05x slower                                        |
| python_startup_no_site | 12.3 ms                                                    | 13.0 ms: 1.05x slower                                        |
| Geometric mean         | (ref)                                                      | 1.05x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-darwin-arm64-mdboom-rc1_mdboom-3.13.0rc1-2a88001 |
|-----------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 7.37 ms: 1.06x slower                                        |
| genshi_text     | 13.9 ms                                                    | 14.7 ms: 1.06x slower                                        |
| genshi_xml      | 29.9 ms                                                    | 31.9 ms: 1.07x slower                                        |
| django_template | 19.4 ms                                                    | 22.2 ms: 1.15x slower                                        |
| Geometric mean  | (ref)                                                      | 1.08x slower                                                 |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-darwin-arm64-mdboom-rc1_mdboom-3.13.0rc1-2a88001 |
|----------------------------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| regex_dna                        | 149 ms                                                     | 144 ms: 1.04x faster                                         |
| regex_v8                         | 17.3 ms                                                    | 16.8 ms: 1.03x faster                                        |
| create_gc_cycles                 | 897 us                                                     | 882 us: 1.02x faster                                         |
| regex_effbot                     | 2.58 ms                                                    | 2.55 ms: 1.02x faster                                        |
| asyncio_websockets               | 409 ms                                                     | 408 ms: 1.00x faster                                         |
| pidigits                         | 282 ms                                                     | 283 ms: 1.00x slower                                         |
| gc_traversal                     | 2.45 ms                                                    | 2.47 ms: 1.01x slower                                        |
| crypto_pyaes                     | 49.5 ms                                                    | 50.5 ms: 1.02x slower                                        |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 338 ms: 1.02x slower                                         |
| dulwich_log                      | 27.6 ms                                                    | 28.2 ms: 1.02x slower                                        |
| xml_etree_parse                  | 106 ms                                                     | 108 ms: 1.02x slower                                         |
| go                               | 101 ms                                                     | 103 ms: 1.03x slower                                         |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 464 ms: 1.03x slower                                         |
| bench_mp_pool                    | 47.2 ms                                                    | 48.8 ms: 1.03x slower                                        |
| generators                       | 22.9 ms                                                    | 23.7 ms: 1.03x slower                                        |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 370 ms: 1.03x slower                                         |
| hexiom                           | 4.06 ms                                                    | 4.20 ms: 1.03x slower                                        |
| async_tree_eager_io_tg           | 768 ms                                                     | 794 ms: 1.03x slower                                         |
| async_tree_eager_io              | 766 ms                                                     | 796 ms: 1.04x slower                                         |
| async_tree_io_tg                 | 565 ms                                                     | 587 ms: 1.04x slower                                         |
| xml_etree_iterparse              | 71.5 ms                                                    | 74.4 ms: 1.04x slower                                        |
| async_tree_io                    | 563 ms                                                     | 587 ms: 1.04x slower                                         |
| mdp                              | 1.53 sec                                                   | 1.60 sec: 1.04x slower                                       |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 488 ms: 1.04x slower                                         |
| json                             | 2.93 ms                                                    | 3.06 ms: 1.05x slower                                        |
| meteor_contest                   | 70.3 ms                                                    | 73.6 ms: 1.05x slower                                        |
| pyflate                          | 321 ms                                                     | 336 ms: 1.05x slower                                         |
| python_startup                   | 15.2 ms                                                    | 15.9 ms: 1.05x slower                                        |
| scimark_monte_carlo              | 42.5 ms                                                    | 44.6 ms: 1.05x slower                                        |
| richards_super                   | 35.2 ms                                                    | 37.0 ms: 1.05x slower                                        |
| richards                         | 31.8 ms                                                    | 33.5 ms: 1.05x slower                                        |
| python_startup_no_site           | 12.3 ms                                                    | 13.0 ms: 1.05x slower                                        |
| json_loads                       | 16.8 us                                                    | 17.8 us: 1.06x slower                                        |
| mako                             | 6.99 ms                                                    | 7.37 ms: 1.06x slower                                        |
| genshi_text                      | 13.9 ms                                                    | 14.7 ms: 1.06x slower                                        |
| float                            | 48.6 ms                                                    | 51.4 ms: 1.06x slower                                        |
| json_dumps                       | 6.23 ms                                                    | 6.65 ms: 1.07x slower                                        |
| genshi_xml                       | 29.9 ms                                                    | 31.9 ms: 1.07x slower                                        |
| tomli_loads                      | 1.47 sec                                                   | 1.56 sec: 1.07x slower                                       |
| pickle_pure_python               | 179 us                                                     | 191 us: 1.07x slower                                         |
| deltablue                        | 2.14 ms                                                    | 2.29 ms: 1.07x slower                                        |
| docutils                         | 1.44 sec                                                   | 1.54 sec: 1.07x slower                                       |
| html5lib                         | 31.2 ms                                                    | 33.3 ms: 1.07x slower                                        |
| sqlglot_parse                    | 732 us                                                     | 784 us: 1.07x slower                                         |
| async_tree_memoization           | 260 ms                                                     | 279 ms: 1.07x slower                                         |
| deepcopy_memo                    | 22.6 us                                                    | 24.3 us: 1.07x slower                                        |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 135 ms: 1.08x slower                                         |
| sqlglot_transpile                | 891 us                                                     | 958 us: 1.08x slower                                         |
| telco                            | 4.60 ms                                                    | 4.95 ms: 1.08x slower                                        |
| pycparser                        | 632 ms                                                     | 682 ms: 1.08x slower                                         |
| regex_compile                    | 68.5 ms                                                    | 73.9 ms: 1.08x slower                                        |
| async_tree_none_tg               | 198 ms                                                     | 213 ms: 1.08x slower                                         |
| unpickle_pure_python             | 141 us                                                     | 152 us: 1.08x slower                                         |
| async_tree_eager_memoization     | 152 ms                                                     | 165 ms: 1.08x slower                                         |
| sympy_integrate                  | 10.3 ms                                                    | 11.2 ms: 1.08x slower                                        |
| async_tree_none                  | 209 ms                                                     | 227 ms: 1.08x slower                                         |
| bench_thread_pool                | 447 us                                                     | 486 us: 1.09x slower                                         |
| chameleon                        | 4.27 ms                                                    | 4.65 ms: 1.09x slower                                        |
| scimark_fft                      | 181 ms                                                     | 197 ms: 1.09x slower                                         |
| pathlib                          | 23.3 ms                                                    | 25.5 ms: 1.09x slower                                        |
| spectral_norm                    | 66.4 ms                                                    | 72.5 ms: 1.09x slower                                        |
| scimark_sor                      | 94.9 ms                                                    | 104 ms: 1.09x slower                                         |
| pprint_pformat                   | 947 ms                                                     | 1.04 sec: 1.09x slower                                       |
| dask                             | 221 ms                                                     | 243 ms: 1.10x slower                                         |
| pprint_safe_repr                 | 465 ms                                                     | 511 ms: 1.10x slower                                         |
| nbody                            | 59.6 ms                                                    | 66.0 ms: 1.11x slower                                        |
| nqueens                          | 52.2 ms                                                    | 57.8 ms: 1.11x slower                                        |
| deepcopy                         | 204 us                                                     | 227 us: 1.11x slower                                         |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 3.08 ms: 1.11x slower                                        |
| deepcopy_reduce                  | 1.82 us                                                    | 2.03 us: 1.11x slower                                        |
| sympy_sum                        | 69.2 ms                                                    | 77.1 ms: 1.11x slower                                        |
| async_tree_memoization_tg        | 240 ms                                                     | 267 ms: 1.12x slower                                         |
| pylint                           | 170 ms                                                     | 190 ms: 1.12x slower                                         |
| chaos                            | 34.0 ms                                                    | 38.1 ms: 1.12x slower                                        |
| sympy_str                        | 131 ms                                                     | 147 ms: 1.12x slower                                         |
| logging_simple                   | 3.04 us                                                    | 3.42 us: 1.12x slower                                        |
| logging_silent                   | 60.1 ns                                                    | 67.8 ns: 1.13x slower                                        |
| logging_format                   | 3.31 us                                                    | 3.74 us: 1.13x slower                                        |
| coverage                         | 45.0 ms                                                    | 50.8 ms: 1.13x slower                                        |
| thrift                           | 435 us                                                     | 493 us: 1.13x slower                                         |
| xml_etree_generate               | 52.7 ms                                                    | 59.9 ms: 1.14x slower                                        |
| xml_etree_process                | 37.1 ms                                                    | 42.2 ms: 1.14x slower                                        |
| sympy_expand                     | 226 ms                                                     | 257 ms: 1.14x slower                                         |
| raytrace                         | 147 ms                                                     | 168 ms: 1.14x slower                                         |
| django_template                  | 19.4 ms                                                    | 22.2 ms: 1.15x slower                                        |
| scimark_lu                       | 66.9 ms                                                    | 76.7 ms: 1.15x slower                                        |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.51 sec: 1.15x slower                                       |
| async_generators                 | 281 ms                                                     | 323 ms: 1.15x slower                                         |
| async_tree_eager_tg              | 41.4 ms                                                    | 47.9 ms: 1.16x slower                                        |
| comprehensions                   | 10.2 us                                                    | 11.8 us: 1.16x slower                                        |
| sqlglot_optimize                 | 30.9 ms                                                    | 35.8 ms: 1.16x slower                                        |
| sqlglot_normalize                | 166 ms                                                     | 193 ms: 1.16x slower                                         |
| async_tree_eager                 | 60.3 ms                                                    | 70.7 ms: 1.17x slower                                        |
| fannkuch                         | 248 ms                                                     | 296 ms: 1.19x slower                                         |
| typing_runtime_protocols         | 87.6 us                                                    | 108 us: 1.24x slower                                         |
| 2to3                             | 161 ms                                                     | 200 ms: 1.24x slower                                         |
| coroutines                       | 15.8 ms                                                    | 19.8 ms: 1.25x slower                                        |
| tornado_http                     | 66.7 ms                                                    | 84.8 ms: 1.27x slower                                        |
| mypy2                            | 379 ms                                                     | 494 ms: 1.30x slower                                         |
| Geometric mean                   | (ref)                                                      | 1.08x slower                                                 |

Benchmark hidden because not significant (2): asyncio_tcp_ssl, asyncio_tcp
Ignored benchmarks (9) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: 0.42x