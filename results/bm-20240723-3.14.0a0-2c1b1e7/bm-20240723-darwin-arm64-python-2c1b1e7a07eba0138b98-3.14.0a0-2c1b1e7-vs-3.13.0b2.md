# Results vs. 3.13.0b2

- fork: python
- ref: 2c1b1e7a07eba0138b98
- machine: darwin-arm64
- commit hash: 2c1b1e7
- commit date: 2024-07-23
- overall geometric mean: 1.01x faster
- HPT reliability: 99.21%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.62x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-darwin-arm64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| docutils       | 1.44 sec                                                   | 1.48 sec: 1.03x slower                                                |
| html5lib       | 31.2 ms                                                    | 31.5 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                      | 1.02x slower                                                          |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-darwin-arm64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 648 ms: 1.18x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 669 ms: 1.15x faster                                                  |
| async_tree_none_tg               | 198 ms                                                     | 175 ms: 1.13x faster                                                  |
| async_tree_io_tg                 | 565 ms                                                     | 509 ms: 1.11x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 236 ms: 1.10x faster                                                  |
| async_tree_io                    | 563 ms                                                     | 532 ms: 1.06x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 198 ms: 1.06x faster                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 457 ms: 1.02x faster                                                  |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 123 ms: 1.02x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 355 ms: 1.01x faster                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.1 ms: 1.01x faster                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 332 ms: 1.00x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 61.2 ms: 1.01x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.05x faster                                                          |

Benchmark hidden because not significant (3): async_tree_eager_memoization, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-darwin-arm64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 282 ms                                                     | 281 ms: 1.00x faster                                                  |
| nbody          | 59.6 ms                                                    | 60.1 ms: 1.01x slower                                                 |
| float          | 48.6 ms                                                    | 49.4 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                      | 1.01x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-darwin-arm64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.62 ms: 1.01x slower                                                 |
| regex_v8       | 17.3 ms                                                    | 17.8 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                      | 1.01x slower                                                          |

Benchmark hidden because not significant (2): regex_compile, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-darwin-arm64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_generate   | 52.7 ms                                                    | 52.7 ms: 1.00x slower                                                 |
| xml_etree_process    | 37.1 ms                                                    | 37.2 ms: 1.00x slower                                                 |
| xml_etree_parse      | 106 ms                                                     | 107 ms: 1.01x slower                                                  |
| xml_etree_iterparse  | 71.5 ms                                                    | 72.5 ms: 1.01x slower                                                 |
| unpickle_pure_python | 141 us                                                     | 143 us: 1.02x slower                                                  |
| json_loads           | 16.8 us                                                    | 17.1 us: 1.02x slower                                                 |
| json_dumps           | 6.23 ms                                                    | 6.36 ms: 1.02x slower                                                 |
| pickle_pure_python   | 179 us                                                     | 183 us: 1.02x slower                                                  |
| Geometric mean       | (ref)                                                      | 1.01x slower                                                          |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-darwin-arm64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup | 15.2 ms                                                    | 15.1 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                      | 1.00x faster                                                          |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-darwin-arm64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 13.9 ms                                                    | 14.0 ms: 1.01x slower                                                 |
| genshi_xml      | 29.9 ms                                                    | 30.2 ms: 1.01x slower                                                 |
| django_template | 19.4 ms                                                    | 19.7 ms: 1.02x slower                                                 |
| mako            | 6.99 ms                                                    | 7.19 ms: 1.03x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.02x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-darwin-arm64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                         | 204 us                                                     | 146 us: 1.40x faster                                                  |
| deepcopy_memo                    | 22.6 us                                                    | 16.9 us: 1.34x faster                                                 |
| deepcopy_reduce                  | 1.82 us                                                    | 1.52 us: 1.20x faster                                                 |
| async_tree_eager_io              | 766 ms                                                     | 648 ms: 1.18x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 669 ms: 1.15x faster                                                  |
| async_tree_none_tg               | 198 ms                                                     | 175 ms: 1.13x faster                                                  |
| async_tree_io_tg                 | 565 ms                                                     | 509 ms: 1.11x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 236 ms: 1.10x faster                                                  |
| generators                       | 22.9 ms                                                    | 20.9 ms: 1.10x faster                                                 |
| mdp                              | 1.53 sec                                                   | 1.43 sec: 1.07x faster                                                |
| async_tree_io                    | 563 ms                                                     | 532 ms: 1.06x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 198 ms: 1.06x faster                                                  |
| richards_super                   | 35.2 ms                                                    | 34.4 ms: 1.02x faster                                                 |
| go                               | 101 ms                                                     | 98.3 ms: 1.02x faster                                                 |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 457 ms: 1.02x faster                                                  |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 123 ms: 1.02x faster                                                  |
| richards                         | 31.8 ms                                                    | 31.3 ms: 1.02x faster                                                 |
| asyncio_tcp_ssl                  | 1.29 sec                                                   | 1.27 sec: 1.02x faster                                                |
| logging_silent                   | 60.1 ns                                                    | 59.3 ns: 1.01x faster                                                 |
| pathlib                          | 23.3 ms                                                    | 23.0 ms: 1.01x faster                                                 |
| deltablue                        | 2.14 ms                                                    | 2.12 ms: 1.01x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 355 ms: 1.01x faster                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.1 ms: 1.01x faster                                                 |
| python_startup                   | 15.2 ms                                                    | 15.1 ms: 1.01x faster                                                 |
| pidigits                         | 282 ms                                                     | 281 ms: 1.00x faster                                                  |
| xml_etree_generate               | 52.7 ms                                                    | 52.7 ms: 1.00x slower                                                 |
| create_gc_cycles                 | 897 us                                                     | 899 us: 1.00x slower                                                  |
| pyflate                          | 321 ms                                                     | 322 ms: 1.00x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 332 ms: 1.00x slower                                                  |
| gc_traversal                     | 2.45 ms                                                    | 2.46 ms: 1.00x slower                                                 |
| coverage                         | 45.0 ms                                                    | 45.2 ms: 1.00x slower                                                 |
| hexiom                           | 4.06 ms                                                    | 4.08 ms: 1.00x slower                                                 |
| xml_etree_process                | 37.1 ms                                                    | 37.2 ms: 1.00x slower                                                 |
| sympy_integrate                  | 10.3 ms                                                    | 10.4 ms: 1.01x slower                                                 |
| genshi_text                      | 13.9 ms                                                    | 14.0 ms: 1.01x slower                                                 |
| thrift                           | 435 us                                                     | 438 us: 1.01x slower                                                  |
| scimark_monte_carlo              | 42.5 ms                                                    | 42.8 ms: 1.01x slower                                                 |
| sqlglot_normalize                | 166 ms                                                     | 167 ms: 1.01x slower                                                  |
| logging_simple                   | 3.04 us                                                    | 3.07 us: 1.01x slower                                                 |
| nbody                            | 59.6 ms                                                    | 60.1 ms: 1.01x slower                                                 |
| telco                            | 4.60 ms                                                    | 4.65 ms: 1.01x slower                                                 |
| genshi_xml                       | 29.9 ms                                                    | 30.2 ms: 1.01x slower                                                 |
| sqlglot_optimize                 | 30.9 ms                                                    | 31.2 ms: 1.01x slower                                                 |
| bench_thread_pool                | 447 us                                                     | 452 us: 1.01x slower                                                  |
| xml_etree_parse                  | 106 ms                                                     | 107 ms: 1.01x slower                                                  |
| html5lib                         | 31.2 ms                                                    | 31.5 ms: 1.01x slower                                                 |
| pycparser                        | 632 ms                                                     | 640 ms: 1.01x slower                                                  |
| raytrace                         | 147 ms                                                     | 149 ms: 1.01x slower                                                  |
| scimark_sor                      | 94.9 ms                                                    | 96.1 ms: 1.01x slower                                                 |
| regex_effbot                     | 2.58 ms                                                    | 2.62 ms: 1.01x slower                                                 |
| pprint_pformat                   | 947 ms                                                     | 960 ms: 1.01x slower                                                  |
| xml_etree_iterparse              | 71.5 ms                                                    | 72.5 ms: 1.01x slower                                                 |
| scimark_fft                      | 181 ms                                                     | 183 ms: 1.01x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 61.2 ms: 1.01x slower                                                 |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.81 ms: 1.01x slower                                                 |
| float                            | 48.6 ms                                                    | 49.4 ms: 1.02x slower                                                 |
| sympy_str                        | 131 ms                                                     | 134 ms: 1.02x slower                                                  |
| sympy_sum                        | 69.2 ms                                                    | 70.3 ms: 1.02x slower                                                 |
| django_template                  | 19.4 ms                                                    | 19.7 ms: 1.02x slower                                                 |
| unpickle_pure_python             | 141 us                                                     | 143 us: 1.02x slower                                                  |
| sympy_expand                     | 226 ms                                                     | 230 ms: 1.02x slower                                                  |
| pprint_safe_repr                 | 465 ms                                                     | 473 ms: 1.02x slower                                                  |
| json_loads                       | 16.8 us                                                    | 17.1 us: 1.02x slower                                                 |
| coroutines                       | 15.8 ms                                                    | 16.1 ms: 1.02x slower                                                 |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.11 sec: 1.02x slower                                                |
| meteor_contest                   | 70.3 ms                                                    | 71.6 ms: 1.02x slower                                                 |
| sqlglot_parse                    | 732 us                                                     | 746 us: 1.02x slower                                                  |
| sqlglot_transpile                | 891 us                                                     | 909 us: 1.02x slower                                                  |
| json_dumps                       | 6.23 ms                                                    | 6.36 ms: 1.02x slower                                                 |
| logging_format                   | 3.31 us                                                    | 3.38 us: 1.02x slower                                                 |
| crypto_pyaes                     | 49.5 ms                                                    | 50.6 ms: 1.02x slower                                                 |
| pickle_pure_python               | 179 us                                                     | 183 us: 1.02x slower                                                  |
| json                             | 2.93 ms                                                    | 3.01 ms: 1.03x slower                                                 |
| docutils                         | 1.44 sec                                                   | 1.48 sec: 1.03x slower                                                |
| regex_v8                         | 17.3 ms                                                    | 17.8 ms: 1.03x slower                                                 |
| mako                             | 6.99 ms                                                    | 7.19 ms: 1.03x slower                                                 |
| nqueens                          | 52.2 ms                                                    | 54.0 ms: 1.03x slower                                                 |
| typing_runtime_protocols         | 87.6 us                                                    | 90.8 us: 1.04x slower                                                 |
| scimark_lu                       | 66.9 ms                                                    | 69.8 ms: 1.04x slower                                                 |
| comprehensions                   | 10.2 us                                                    | 10.6 us: 1.04x slower                                                 |
| chaos                            | 34.0 ms                                                    | 35.9 ms: 1.06x slower                                                 |
| fannkuch                         | 248 ms                                                     | 263 ms: 1.06x slower                                                  |
| asyncio_tcp                      | 402 ms                                                     | 437 ms: 1.09x slower                                                  |
| Geometric mean                   | (ref)                                                      | 1.01x faster                                                          |

Benchmark hidden because not significant (15): async_tree_eager_memoization, async_tree_cpu_io_mixed_tg, python_startup_no_site, asyncio_websockets, regex_compile, spectral_norm, dask, regex_dna, bench_mp_pool, async_generators, 2to3, async_tree_memoization_tg, tomli_loads, tornado_http, pylint
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.21% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.62x