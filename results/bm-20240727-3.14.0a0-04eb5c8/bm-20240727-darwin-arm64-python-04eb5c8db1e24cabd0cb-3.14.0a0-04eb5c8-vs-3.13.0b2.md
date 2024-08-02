# Results vs. 3.13.0b2

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: darwin-arm64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.01x faster
- HPT reliability: 97.76%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.43x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 163 ms: 1.01x slower                                                  |
| docutils       | 1.44 sec                                                   | 1.49 sec: 1.04x slower                                                |
| html5lib       | 31.2 ms                                                    | 31.5 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                      | 1.01x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 641 ms: 1.20x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 678 ms: 1.13x faster                                                  |
| async_tree_io_tg                 | 565 ms                                                     | 508 ms: 1.11x faster                                                  |
| async_tree_none_tg               | 198 ms                                                     | 183 ms: 1.08x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 241 ms: 1.08x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 195 ms: 1.07x faster                                                  |
| async_tree_memoization_tg        | 240 ms                                                     | 226 ms: 1.06x faster                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 451 ms: 1.04x faster                                                  |
| async_tree_io                    | 563 ms                                                     | 545 ms: 1.03x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 356 ms: 1.01x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 333 ms: 1.01x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 61.5 ms: 1.02x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.05x faster                                                          |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 48.1 ms: 1.01x faster                                                 |
| pidigits       | 282 ms                                                     | 281 ms: 1.00x faster                                                  |
| nbody          | 59.6 ms                                                    | 61.7 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                      | 1.01x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.54 ms: 1.02x faster                                                 |
| regex_dna      | 149 ms                                                     | 149 ms: 1.00x slower                                                  |
| regex_v8       | 17.3 ms                                                    | 17.4 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                      | 1.00x faster                                                          |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_generate   | 52.7 ms                                                    | 53.0 ms: 1.01x slower                                                 |
| tomli_loads          | 1.47 sec                                                   | 1.48 sec: 1.01x slower                                                |
| json_loads           | 16.8 us                                                    | 17.0 us: 1.01x slower                                                 |
| xml_etree_process    | 37.1 ms                                                    | 37.4 ms: 1.01x slower                                                 |
| xml_etree_iterparse  | 71.5 ms                                                    | 72.6 ms: 1.01x slower                                                 |
| pickle_pure_python   | 179 us                                                     | 182 us: 1.02x slower                                                  |
| json_dumps           | 6.23 ms                                                    | 6.37 ms: 1.02x slower                                                 |
| unpickle_pure_python | 141 us                                                     | 144 us: 1.02x slower                                                  |
| Geometric mean       | (ref)                                                      | 1.01x slower                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 15.2 ms: 1.00x slower                                                 |
| python_startup_no_site | 12.3 ms                                                    | 12.5 ms: 1.02x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 7.04 ms: 1.01x slower                                                 |
| genshi_xml      | 29.9 ms                                                    | 30.3 ms: 1.01x slower                                                 |
| django_template | 19.4 ms                                                    | 19.7 ms: 1.02x slower                                                 |
| genshi_text     | 13.9 ms                                                    | 14.2 ms: 1.02x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                         | 204 us                                                     | 145 us: 1.41x faster                                                  |
| deepcopy_memo                    | 22.6 us                                                    | 17.0 us: 1.33x faster                                                 |
| deepcopy_reduce                  | 1.82 us                                                    | 1.49 us: 1.22x faster                                                 |
| async_tree_eager_io              | 766 ms                                                     | 641 ms: 1.20x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 678 ms: 1.13x faster                                                  |
| async_tree_io_tg                 | 565 ms                                                     | 508 ms: 1.11x faster                                                  |
| generators                       | 22.9 ms                                                    | 20.6 ms: 1.11x faster                                                 |
| mdp                              | 1.53 sec                                                   | 1.42 sec: 1.08x faster                                                |
| async_tree_none_tg               | 198 ms                                                     | 183 ms: 1.08x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 241 ms: 1.08x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 195 ms: 1.07x faster                                                  |
| async_tree_memoization_tg        | 240 ms                                                     | 226 ms: 1.06x faster                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 451 ms: 1.04x faster                                                  |
| async_tree_io                    | 563 ms                                                     | 545 ms: 1.03x faster                                                  |
| go                               | 101 ms                                                     | 98.1 ms: 1.03x faster                                                 |
| coverage                         | 45.0 ms                                                    | 44.2 ms: 1.02x faster                                                 |
| richards_super                   | 35.2 ms                                                    | 34.6 ms: 1.02x faster                                                 |
| regex_effbot                     | 2.58 ms                                                    | 2.54 ms: 1.02x faster                                                 |
| deltablue                        | 2.14 ms                                                    | 2.11 ms: 1.02x faster                                                 |
| dulwich_log                      | 27.6 ms                                                    | 27.2 ms: 1.01x faster                                                 |
| asyncio_tcp_ssl                  | 1.29 sec                                                   | 1.27 sec: 1.01x faster                                                |
| telco                            | 4.60 ms                                                    | 4.55 ms: 1.01x faster                                                 |
| float                            | 48.6 ms                                                    | 48.1 ms: 1.01x faster                                                 |
| richards                         | 31.8 ms                                                    | 31.6 ms: 1.01x faster                                                 |
| thrift                           | 435 us                                                     | 432 us: 1.01x faster                                                  |
| logging_silent                   | 60.1 ns                                                    | 59.7 ns: 1.01x faster                                                 |
| spectral_norm                    | 66.4 ms                                                    | 65.9 ms: 1.01x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 356 ms: 1.01x faster                                                  |
| pidigits                         | 282 ms                                                     | 281 ms: 1.00x faster                                                  |
| asyncio_websockets               | 409 ms                                                     | 408 ms: 1.00x faster                                                  |
| raytrace                         | 147 ms                                                     | 147 ms: 1.00x faster                                                  |
| regex_dna                        | 149 ms                                                     | 149 ms: 1.00x slower                                                  |
| scimark_sor                      | 94.9 ms                                                    | 95.1 ms: 1.00x slower                                                 |
| pyflate                          | 321 ms                                                     | 322 ms: 1.00x slower                                                  |
| python_startup                   | 15.2 ms                                                    | 15.2 ms: 1.00x slower                                                 |
| gc_traversal                     | 2.45 ms                                                    | 2.46 ms: 1.00x slower                                                 |
| bench_thread_pool                | 447 us                                                     | 449 us: 1.00x slower                                                  |
| sympy_integrate                  | 10.3 ms                                                    | 10.4 ms: 1.00x slower                                                 |
| regex_v8                         | 17.3 ms                                                    | 17.4 ms: 1.00x slower                                                 |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.79 ms: 1.01x slower                                                 |
| xml_etree_generate               | 52.7 ms                                                    | 53.0 ms: 1.01x slower                                                 |
| scimark_fft                      | 181 ms                                                     | 182 ms: 1.01x slower                                                  |
| tomli_loads                      | 1.47 sec                                                   | 1.48 sec: 1.01x slower                                                |
| create_gc_cycles                 | 897 us                                                     | 903 us: 1.01x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 333 ms: 1.01x slower                                                  |
| mako                             | 6.99 ms                                                    | 7.04 ms: 1.01x slower                                                 |
| json_loads                       | 16.8 us                                                    | 17.0 us: 1.01x slower                                                 |
| pprint_pformat                   | 947 ms                                                     | 955 ms: 1.01x slower                                                  |
| xml_etree_process                | 37.1 ms                                                    | 37.4 ms: 1.01x slower                                                 |
| html5lib                         | 31.2 ms                                                    | 31.5 ms: 1.01x slower                                                 |
| sqlglot_optimize                 | 30.9 ms                                                    | 31.2 ms: 1.01x slower                                                 |
| pprint_safe_repr                 | 465 ms                                                     | 470 ms: 1.01x slower                                                  |
| logging_simple                   | 3.04 us                                                    | 3.08 us: 1.01x slower                                                 |
| sympy_sum                        | 69.2 ms                                                    | 70.0 ms: 1.01x slower                                                 |
| genshi_xml                       | 29.9 ms                                                    | 30.3 ms: 1.01x slower                                                 |
| sqlglot_normalize                | 166 ms                                                     | 168 ms: 1.01x slower                                                  |
| 2to3                             | 161 ms                                                     | 163 ms: 1.01x slower                                                  |
| sqlglot_parse                    | 732 us                                                     | 742 us: 1.01x slower                                                  |
| sympy_str                        | 131 ms                                                     | 133 ms: 1.01x slower                                                  |
| xml_etree_iterparse              | 71.5 ms                                                    | 72.6 ms: 1.01x slower                                                 |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.10 sec: 1.01x slower                                                |
| sympy_expand                     | 226 ms                                                     | 229 ms: 1.02x slower                                                  |
| python_startup_no_site           | 12.3 ms                                                    | 12.5 ms: 1.02x slower                                                 |
| sqlglot_transpile                | 891 us                                                     | 905 us: 1.02x slower                                                  |
| django_template                  | 19.4 ms                                                    | 19.7 ms: 1.02x slower                                                 |
| hexiom                           | 4.06 ms                                                    | 4.12 ms: 1.02x slower                                                 |
| pycparser                        | 632 ms                                                     | 643 ms: 1.02x slower                                                  |
| coroutines                       | 15.8 ms                                                    | 16.1 ms: 1.02x slower                                                 |
| bench_mp_pool                    | 47.2 ms                                                    | 48.1 ms: 1.02x slower                                                 |
| genshi_text                      | 13.9 ms                                                    | 14.2 ms: 1.02x slower                                                 |
| async_tree_eager                 | 60.3 ms                                                    | 61.5 ms: 1.02x slower                                                 |
| pickle_pure_python               | 179 us                                                     | 182 us: 1.02x slower                                                  |
| meteor_contest                   | 70.3 ms                                                    | 71.9 ms: 1.02x slower                                                 |
| json_dumps                       | 6.23 ms                                                    | 6.37 ms: 1.02x slower                                                 |
| crypto_pyaes                     | 49.5 ms                                                    | 50.6 ms: 1.02x slower                                                 |
| unpickle_pure_python             | 141 us                                                     | 144 us: 1.02x slower                                                  |
| logging_format                   | 3.31 us                                                    | 3.39 us: 1.03x slower                                                 |
| chaos                            | 34.0 ms                                                    | 34.9 ms: 1.03x slower                                                 |
| nqueens                          | 52.2 ms                                                    | 53.6 ms: 1.03x slower                                                 |
| nbody                            | 59.6 ms                                                    | 61.7 ms: 1.04x slower                                                 |
| docutils                         | 1.44 sec                                                   | 1.49 sec: 1.04x slower                                                |
| scimark_lu                       | 66.9 ms                                                    | 69.5 ms: 1.04x slower                                                 |
| typing_runtime_protocols         | 87.6 us                                                    | 93.7 us: 1.07x slower                                                 |
| asyncio_tcp                      | 402 ms                                                     | 431 ms: 1.07x slower                                                  |
| comprehensions                   | 10.2 us                                                    | 10.9 us: 1.07x slower                                                 |
| fannkuch                         | 248 ms                                                     | 266 ms: 1.07x slower                                                  |
| Geometric mean                   | (ref)                                                      | 1.01x faster                                                          |

Benchmark hidden because not significant (13): async_tree_cpu_io_mixed_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, tornado_http, regex_compile, async_generators, scimark_monte_carlo, dask, json, async_tree_eager_tg, pathlib, xml_etree_parse, pylint
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 97.76% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.43x