# Results vs. 3.13.0b2

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 7c66906
- commit date: 2024-07-03
- overall geometric mean: 1.02x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-darwin-arm64-python-main-3.14.0a0-7c66906 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 161 ms                                                     | 205 ms: 1.28x slower                                  |
| docutils       | 1.44 sec                                                   | 1.56 sec: 1.09x slower                                |
| html5lib       | 31.2 ms                                                    | 31.6 ms: 1.01x slower                                 |
| Geometric mean | (ref)                                                      | 1.09x slower                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-darwin-arm64-python-main-3.14.0a0-7c66906 |
|----------------------------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| async_tree_none_tg               | 198 ms                                                     | 176 ms: 1.12x faster                                  |
| async_tree_memoization           | 260 ms                                                     | 232 ms: 1.12x faster                                  |
| async_tree_io_tg                 | 565 ms                                                     | 510 ms: 1.11x faster                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 696 ms: 1.10x faster                                  |
| async_tree_none                  | 209 ms                                                     | 193 ms: 1.08x faster                                  |
| async_tree_eager_io              | 766 ms                                                     | 709 ms: 1.08x faster                                  |
| async_tree_io                    | 563 ms                                                     | 533 ms: 1.06x faster                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 453 ms: 1.03x faster                                  |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 123 ms: 1.02x faster                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.1 ms: 1.01x faster                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 332 ms: 1.00x slower                                  |
| async_tree_eager                 | 60.3 ms                                                    | 63.9 ms: 1.06x slower                                 |
| Geometric mean                   | (ref)                                                      | 1.04x faster                                          |

Benchmark hidden because not significant (4): async_tree_eager_memoization, async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-darwin-arm64-python-main-3.14.0a0-7c66906 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 59.6 ms                                                    | 60.6 ms: 1.02x slower                                 |
| float          | 48.6 ms                                                    | 49.8 ms: 1.03x slower                                 |
| Geometric mean | (ref)                                                      | 1.01x slower                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-darwin-arm64-python-main-3.14.0a0-7c66906 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| regex_dna      | 149 ms                                                     | 151 ms: 1.01x slower                                  |
| regex_v8       | 17.3 ms                                                    | 17.5 ms: 1.02x slower                                 |
| regex_effbot   | 2.58 ms                                                    | 2.64 ms: 1.02x slower                                 |
| Geometric mean | (ref)                                                      | 1.01x slower                                          |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-darwin-arm64-python-main-3.14.0a0-7c66906 |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| xml_etree_parse      | 106 ms                                                     | 107 ms: 1.01x slower                                  |
| xml_etree_iterparse  | 71.5 ms                                                    | 72.4 ms: 1.01x slower                                 |
| xml_etree_generate   | 52.7 ms                                                    | 53.5 ms: 1.02x slower                                 |
| unpickle_pure_python | 141 us                                                     | 143 us: 1.02x slower                                  |
| pickle_pure_python   | 179 us                                                     | 182 us: 1.02x slower                                  |
| xml_etree_process    | 37.1 ms                                                    | 37.8 ms: 1.02x slower                                 |
| json_loads           | 16.8 us                                                    | 17.3 us: 1.03x slower                                 |
| json_dumps           | 6.23 ms                                                    | 6.44 ms: 1.03x slower                                 |
| Geometric mean       | (ref)                                                      | 1.02x slower                                          |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-darwin-arm64-python-main-3.14.0a0-7c66906 |
|------------------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup_no_site | 12.3 ms                                                    | 26.4 ms: 2.14x slower                                 |
| python_startup         | 15.2 ms                                                    | 35.4 ms: 2.33x slower                                 |
| Geometric mean         | (ref)                                                      | 2.24x slower                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-darwin-arm64-python-main-3.14.0a0-7c66906 |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| genshi_xml      | 29.9 ms                                                    | 30.3 ms: 1.01x slower                                 |
| django_template | 19.4 ms                                                    | 19.9 ms: 1.02x slower                                 |
| mako            | 6.99 ms                                                    | 7.19 ms: 1.03x slower                                 |
| Geometric mean  | (ref)                                                      | 1.02x slower                                          |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-darwin-arm64-python-main-3.14.0a0-7c66906 |
|----------------------------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| deepcopy                         | 204 us                                                     | 145 us: 1.41x faster                                  |
| deepcopy_memo                    | 22.6 us                                                    | 17.0 us: 1.33x faster                                 |
| deepcopy_reduce                  | 1.82 us                                                    | 1.51 us: 1.21x faster                                 |
| async_tree_none_tg               | 198 ms                                                     | 176 ms: 1.12x faster                                  |
| async_tree_memoization           | 260 ms                                                     | 232 ms: 1.12x faster                                  |
| async_tree_io_tg                 | 565 ms                                                     | 510 ms: 1.11x faster                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 696 ms: 1.10x faster                                  |
| async_tree_none                  | 209 ms                                                     | 193 ms: 1.08x faster                                  |
| async_tree_eager_io              | 766 ms                                                     | 709 ms: 1.08x faster                                  |
| mdp                              | 1.53 sec                                                   | 1.43 sec: 1.08x faster                                |
| async_tree_io                    | 563 ms                                                     | 533 ms: 1.06x faster                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 453 ms: 1.03x faster                                  |
| logging_silent                   | 60.1 ns                                                    | 58.9 ns: 1.02x faster                                 |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 123 ms: 1.02x faster                                  |
| richards_super                   | 35.2 ms                                                    | 34.9 ms: 1.01x faster                                 |
| create_gc_cycles                 | 897 us                                                     | 891 us: 1.01x faster                                  |
| thrift                           | 435 us                                                     | 433 us: 1.01x faster                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.1 ms: 1.01x faster                                 |
| coverage                         | 45.0 ms                                                    | 44.8 ms: 1.01x faster                                 |
| go                               | 101 ms                                                     | 100 ms: 1.00x faster                                  |
| gc_traversal                     | 2.45 ms                                                    | 2.46 ms: 1.00x slower                                 |
| async_generators                 | 281 ms                                                     | 282 ms: 1.00x slower                                  |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 332 ms: 1.00x slower                                  |
| pprint_pformat                   | 947 ms                                                     | 952 ms: 1.01x slower                                  |
| pyflate                          | 321 ms                                                     | 323 ms: 1.01x slower                                  |
| pathlib                          | 23.3 ms                                                    | 23.5 ms: 1.01x slower                                 |
| hexiom                           | 4.06 ms                                                    | 4.09 ms: 1.01x slower                                 |
| pprint_safe_repr                 | 465 ms                                                     | 468 ms: 1.01x slower                                  |
| genshi_xml                       | 29.9 ms                                                    | 30.3 ms: 1.01x slower                                 |
| regex_dna                        | 149 ms                                                     | 151 ms: 1.01x slower                                  |
| xml_etree_parse                  | 106 ms                                                     | 107 ms: 1.01x slower                                  |
| pycparser                        | 632 ms                                                     | 640 ms: 1.01x slower                                  |
| xml_etree_iterparse              | 71.5 ms                                                    | 72.4 ms: 1.01x slower                                 |
| html5lib                         | 31.2 ms                                                    | 31.6 ms: 1.01x slower                                 |
| sqlglot_optimize                 | 30.9 ms                                                    | 31.3 ms: 1.01x slower                                 |
| sympy_integrate                  | 10.3 ms                                                    | 10.5 ms: 1.01x slower                                 |
| scimark_sor                      | 94.9 ms                                                    | 96.3 ms: 1.01x slower                                 |
| regex_v8                         | 17.3 ms                                                    | 17.5 ms: 1.02x slower                                 |
| xml_etree_generate               | 52.7 ms                                                    | 53.5 ms: 1.02x slower                                 |
| json                             | 2.93 ms                                                    | 2.98 ms: 1.02x slower                                 |
| nbody                            | 59.6 ms                                                    | 60.6 ms: 1.02x slower                                 |
| unpickle_pure_python             | 141 us                                                     | 143 us: 1.02x slower                                  |
| sqlglot_normalize                | 166 ms                                                     | 169 ms: 1.02x slower                                  |
| asyncio_tcp_ssl                  | 1.29 sec                                                   | 1.31 sec: 1.02x slower                                |
| meteor_contest                   | 70.3 ms                                                    | 71.6 ms: 1.02x slower                                 |
| sqlglot_transpile                | 891 us                                                     | 907 us: 1.02x slower                                  |
| bench_thread_pool                | 447 us                                                     | 455 us: 1.02x slower                                  |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.11 sec: 1.02x slower                                |
| logging_simple                   | 3.04 us                                                    | 3.10 us: 1.02x slower                                 |
| regex_effbot                     | 2.58 ms                                                    | 2.64 ms: 1.02x slower                                 |
| sqlglot_parse                    | 732 us                                                     | 746 us: 1.02x slower                                  |
| pickle_pure_python               | 179 us                                                     | 182 us: 1.02x slower                                  |
| xml_etree_process                | 37.1 ms                                                    | 37.8 ms: 1.02x slower                                 |
| crypto_pyaes                     | 49.5 ms                                                    | 50.5 ms: 1.02x slower                                 |
| spectral_norm                    | 66.4 ms                                                    | 67.7 ms: 1.02x slower                                 |
| sympy_str                        | 131 ms                                                     | 134 ms: 1.02x slower                                  |
| sympy_sum                        | 69.2 ms                                                    | 70.7 ms: 1.02x slower                                 |
| django_template                  | 19.4 ms                                                    | 19.9 ms: 1.02x slower                                 |
| sympy_expand                     | 226 ms                                                     | 231 ms: 1.02x slower                                  |
| raytrace                         | 147 ms                                                     | 150 ms: 1.02x slower                                  |
| coroutines                       | 15.8 ms                                                    | 16.2 ms: 1.03x slower                                 |
| float                            | 48.6 ms                                                    | 49.8 ms: 1.03x slower                                 |
| json_loads                       | 16.8 us                                                    | 17.3 us: 1.03x slower                                 |
| logging_format                   | 3.31 us                                                    | 3.41 us: 1.03x slower                                 |
| mako                             | 6.99 ms                                                    | 7.19 ms: 1.03x slower                                 |
| scimark_monte_carlo              | 42.5 ms                                                    | 43.7 ms: 1.03x slower                                 |
| json_dumps                       | 6.23 ms                                                    | 6.44 ms: 1.03x slower                                 |
| nqueens                          | 52.2 ms                                                    | 54.0 ms: 1.03x slower                                 |
| typing_runtime_protocols         | 87.6 us                                                    | 91.1 us: 1.04x slower                                 |
| scimark_fft                      | 181 ms                                                     | 189 ms: 1.05x slower                                  |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.90 ms: 1.05x slower                                 |
| comprehensions                   | 10.2 us                                                    | 10.7 us: 1.05x slower                                 |
| scimark_lu                       | 66.9 ms                                                    | 70.6 ms: 1.06x slower                                 |
| chaos                            | 34.0 ms                                                    | 36.0 ms: 1.06x slower                                 |
| async_tree_eager                 | 60.3 ms                                                    | 63.9 ms: 1.06x slower                                 |
| fannkuch                         | 248 ms                                                     | 266 ms: 1.07x slower                                  |
| docutils                         | 1.44 sec                                                   | 1.56 sec: 1.09x slower                                |
| 2to3                             | 161 ms                                                     | 205 ms: 1.28x slower                                  |
| bench_mp_pool                    | 47.2 ms                                                    | 85.9 ms: 1.82x slower                                 |
| python_startup_no_site           | 12.3 ms                                                    | 26.4 ms: 2.14x slower                                 |
| python_startup                   | 15.2 ms                                                    | 35.4 ms: 2.33x slower                                 |
| Geometric mean                   | (ref)                                                      | 1.02x slower                                          |

Benchmark hidden because not significant (17): async_tree_eager_memoization, async_tree_cpu_io_mixed_tg, deltablue, async_tree_eager_cpu_io_mixed, richards, regex_compile, tornado_http, telco, asyncio_websockets, pidigits, genshi_text, generators, tomli_loads, dask, async_tree_memoization_tg, pylint, asyncio_tcp
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.99x