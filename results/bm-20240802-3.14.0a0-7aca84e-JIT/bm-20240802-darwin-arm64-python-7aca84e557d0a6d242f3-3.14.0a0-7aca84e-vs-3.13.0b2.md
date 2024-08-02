# Results vs. 3.13.0b2

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: darwin-arm64
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.01x slower
- HPT reliability: 98.62%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.83x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 174 ms: 1.08x slower                                                  |
| docutils       | 1.44 sec                                                   | 1.54 sec: 1.07x slower                                                |
| html5lib       | 31.2 ms                                                    | 30.9 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                      | 1.04x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 640 ms: 1.20x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 675 ms: 1.14x faster                                                  |
| async_tree_io_tg                 | 565 ms                                                     | 506 ms: 1.12x faster                                                  |
| async_tree_none_tg               | 198 ms                                                     | 182 ms: 1.09x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 239 ms: 1.08x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 194 ms: 1.08x faster                                                  |
| async_tree_memoization_tg        | 240 ms                                                     | 228 ms: 1.05x faster                                                  |
| async_tree_io                    | 563 ms                                                     | 544 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 453 ms: 1.03x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 363 ms: 1.01x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 337 ms: 1.02x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 43.1 ms: 1.04x slower                                                 |
| async_tree_eager                 | 60.3 ms                                                    | 64.0 ms: 1.06x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.04x faster                                                          |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed_tg, async_tree_eager_memoization_tg, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 46.7 ms: 1.04x faster                                                 |
| pidigits       | 282 ms                                                     | 281 ms: 1.00x faster                                                  |
| nbody          | 59.6 ms                                                    | 62.7 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                      | 1.00x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 17.3 ms                                                    | 17.2 ms: 1.00x faster                                                 |
| regex_dna      | 149 ms                                                     | 153 ms: 1.03x slower                                                  |
| regex_compile  | 68.5 ms                                                    | 71.2 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                      | 1.02x slower                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                   | 1.25 sec: 1.17x faster                                                |
| unpickle_pure_python | 141 us                                                     | 131 us: 1.07x faster                                                  |
| xml_etree_process    | 37.1 ms                                                    | 35.8 ms: 1.04x faster                                                 |
| pickle_pure_python   | 179 us                                                     | 174 us: 1.03x faster                                                  |
| xml_etree_generate   | 52.7 ms                                                    | 51.7 ms: 1.02x faster                                                 |
| xml_etree_iterparse  | 71.5 ms                                                    | 72.8 ms: 1.02x slower                                                 |
| json_dumps           | 6.23 ms                                                    | 6.35 ms: 1.02x slower                                                 |
| json_loads           | 16.8 us                                                    | 17.3 us: 1.03x slower                                                 |
| xml_etree_parse      | 106 ms                                                     | 109 ms: 1.04x slower                                                  |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 16.1 ms: 1.06x slower                                                 |
| python_startup_no_site | 12.3 ms                                                    | 13.1 ms: 1.06x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 6.46 ms: 1.08x faster                                                 |
| genshi_text     | 13.9 ms                                                    | 14.7 ms: 1.06x slower                                                 |
| django_template | 19.4 ms                                                    | 21.6 ms: 1.11x slower                                                 |
| genshi_xml      | 29.9 ms                                                    | 34.9 ms: 1.16x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.06x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                         | 204 us                                                     | 154 us: 1.32x faster                                                  |
| deepcopy_memo                    | 22.6 us                                                    | 17.2 us: 1.31x faster                                                 |
| async_tree_eager_io              | 766 ms                                                     | 640 ms: 1.20x faster                                                  |
| deepcopy_reduce                  | 1.82 us                                                    | 1.54 us: 1.18x faster                                                 |
| tomli_loads                      | 1.47 sec                                                   | 1.25 sec: 1.17x faster                                                |
| async_tree_eager_io_tg           | 768 ms                                                     | 675 ms: 1.14x faster                                                  |
| async_tree_io_tg                 | 565 ms                                                     | 506 ms: 1.12x faster                                                  |
| async_tree_none_tg               | 198 ms                                                     | 182 ms: 1.09x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 239 ms: 1.08x faster                                                  |
| mako                             | 6.99 ms                                                    | 6.46 ms: 1.08x faster                                                 |
| async_tree_none                  | 209 ms                                                     | 194 ms: 1.08x faster                                                  |
| scimark_sor                      | 94.9 ms                                                    | 88.4 ms: 1.07x faster                                                 |
| unpickle_pure_python             | 141 us                                                     | 131 us: 1.07x faster                                                  |
| async_tree_memoization_tg        | 240 ms                                                     | 228 ms: 1.05x faster                                                  |
| mdp                              | 1.53 sec                                                   | 1.46 sec: 1.05x faster                                                |
| float                            | 48.6 ms                                                    | 46.7 ms: 1.04x faster                                                 |
| xml_etree_process                | 37.1 ms                                                    | 35.8 ms: 1.04x faster                                                 |
| async_tree_io                    | 563 ms                                                     | 544 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 453 ms: 1.03x faster                                                  |
| richards                         | 31.8 ms                                                    | 30.9 ms: 1.03x faster                                                 |
| richards_super                   | 35.2 ms                                                    | 34.2 ms: 1.03x faster                                                 |
| pickle_pure_python               | 179 us                                                     | 174 us: 1.03x faster                                                  |
| pyflate                          | 321 ms                                                     | 313 ms: 1.02x faster                                                  |
| xml_etree_generate               | 52.7 ms                                                    | 51.7 ms: 1.02x faster                                                 |
| logging_simple                   | 3.04 us                                                    | 2.99 us: 1.02x faster                                                 |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.01 sec: 1.01x faster                                                |
| scimark_lu                       | 66.9 ms                                                    | 66.2 ms: 1.01x faster                                                 |
| telco                            | 4.60 ms                                                    | 4.56 ms: 1.01x faster                                                 |
| html5lib                         | 31.2 ms                                                    | 30.9 ms: 1.01x faster                                                 |
| coverage                         | 45.0 ms                                                    | 44.7 ms: 1.01x faster                                                 |
| json                             | 2.93 ms                                                    | 2.91 ms: 1.01x faster                                                 |
| thrift                           | 435 us                                                     | 433 us: 1.00x faster                                                  |
| regex_v8                         | 17.3 ms                                                    | 17.2 ms: 1.00x faster                                                 |
| pidigits                         | 282 ms                                                     | 281 ms: 1.00x faster                                                  |
| gc_traversal                     | 2.45 ms                                                    | 2.47 ms: 1.01x slower                                                 |
| go                               | 101 ms                                                     | 101 ms: 1.01x slower                                                  |
| create_gc_cycles                 | 897 us                                                     | 904 us: 1.01x slower                                                  |
| meteor_contest                   | 70.3 ms                                                    | 71.0 ms: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 363 ms: 1.01x slower                                                  |
| logging_silent                   | 60.1 ns                                                    | 61.0 ns: 1.01x slower                                                 |
| coroutines                       | 15.8 ms                                                    | 16.1 ms: 1.02x slower                                                 |
| xml_etree_iterparse              | 71.5 ms                                                    | 72.8 ms: 1.02x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 337 ms: 1.02x slower                                                  |
| json_dumps                       | 6.23 ms                                                    | 6.35 ms: 1.02x slower                                                 |
| dulwich_log                      | 27.6 ms                                                    | 28.2 ms: 1.02x slower                                                 |
| json_loads                       | 16.8 us                                                    | 17.3 us: 1.03x slower                                                 |
| regex_dna                        | 149 ms                                                     | 153 ms: 1.03x slower                                                  |
| spectral_norm                    | 66.4 ms                                                    | 68.3 ms: 1.03x slower                                                 |
| scimark_monte_carlo              | 42.5 ms                                                    | 43.8 ms: 1.03x slower                                                 |
| xml_etree_parse                  | 106 ms                                                     | 109 ms: 1.04x slower                                                  |
| pprint_pformat                   | 947 ms                                                     | 982 ms: 1.04x slower                                                  |
| regex_compile                    | 68.5 ms                                                    | 71.2 ms: 1.04x slower                                                 |
| pprint_safe_repr                 | 465 ms                                                     | 483 ms: 1.04x slower                                                  |
| crypto_pyaes                     | 49.5 ms                                                    | 51.6 ms: 1.04x slower                                                 |
| async_tree_eager_tg              | 41.4 ms                                                    | 43.1 ms: 1.04x slower                                                 |
| scimark_fft                      | 181 ms                                                     | 189 ms: 1.05x slower                                                  |
| async_generators                 | 281 ms                                                     | 295 ms: 1.05x slower                                                  |
| nbody                            | 59.6 ms                                                    | 62.7 ms: 1.05x slower                                                 |
| dask                             | 221 ms                                                     | 233 ms: 1.05x slower                                                  |
| bench_thread_pool                | 447 us                                                     | 472 us: 1.06x slower                                                  |
| genshi_text                      | 13.9 ms                                                    | 14.7 ms: 1.06x slower                                                 |
| python_startup                   | 15.2 ms                                                    | 16.1 ms: 1.06x slower                                                 |
| async_tree_eager                 | 60.3 ms                                                    | 64.0 ms: 1.06x slower                                                 |
| python_startup_no_site           | 12.3 ms                                                    | 13.1 ms: 1.06x slower                                                 |
| docutils                         | 1.44 sec                                                   | 1.54 sec: 1.07x slower                                                |
| sympy_sum                        | 69.2 ms                                                    | 74.2 ms: 1.07x slower                                                 |
| generators                       | 22.9 ms                                                    | 24.6 ms: 1.08x slower                                                 |
| sympy_str                        | 131 ms                                                     | 142 ms: 1.08x slower                                                  |
| 2to3                             | 161 ms                                                     | 174 ms: 1.08x slower                                                  |
| sqlglot_optimize                 | 30.9 ms                                                    | 33.4 ms: 1.08x slower                                                 |
| bench_mp_pool                    | 47.2 ms                                                    | 51.0 ms: 1.08x slower                                                 |
| pycparser                        | 632 ms                                                     | 684 ms: 1.08x slower                                                  |
| sqlglot_normalize                | 166 ms                                                     | 179 ms: 1.08x slower                                                  |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 3.01 ms: 1.08x slower                                                 |
| deltablue                        | 2.14 ms                                                    | 2.32 ms: 1.09x slower                                                 |
| sympy_integrate                  | 10.3 ms                                                    | 11.3 ms: 1.09x slower                                                 |
| hexiom                           | 4.06 ms                                                    | 4.43 ms: 1.09x slower                                                 |
| raytrace                         | 147 ms                                                     | 160 ms: 1.09x slower                                                  |
| sympy_expand                     | 226 ms                                                     | 246 ms: 1.09x slower                                                  |
| nqueens                          | 52.2 ms                                                    | 57.8 ms: 1.11x slower                                                 |
| django_template                  | 19.4 ms                                                    | 21.6 ms: 1.11x slower                                                 |
| typing_runtime_protocols         | 87.6 us                                                    | 97.8 us: 1.12x slower                                                 |
| chaos                            | 34.0 ms                                                    | 38.8 ms: 1.14x slower                                                 |
| pylint                           | 170 ms                                                     | 194 ms: 1.14x slower                                                  |
| sqlglot_transpile                | 891 us                                                     | 1.02 ms: 1.14x slower                                                 |
| sqlglot_parse                    | 732 us                                                     | 847 us: 1.16x slower                                                  |
| genshi_xml                       | 29.9 ms                                                    | 34.9 ms: 1.16x slower                                                 |
| comprehensions                   | 10.2 us                                                    | 12.2 us: 1.20x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.01x slower                                                          |

Benchmark hidden because not significant (11): async_tree_cpu_io_mixed_tg, logging_format, asyncio_websockets, regex_effbot, fannkuch, asyncio_tcp_ssl, async_tree_eager_memoization_tg, pathlib, async_tree_eager_memoization, tornado_http, asyncio_tcp
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 98.62% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.83x