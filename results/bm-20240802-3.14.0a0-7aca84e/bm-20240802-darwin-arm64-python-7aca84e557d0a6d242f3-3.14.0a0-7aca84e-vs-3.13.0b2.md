# Results vs. 3.13.0b2

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: darwin-arm64
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.01x faster
- HPT reliability: 99.11%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.38x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 164 ms: 1.02x slower                                                  |
| docutils       | 1.44 sec                                                   | 1.49 sec: 1.04x slower                                                |
| html5lib       | 31.2 ms                                                    | 31.5 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                      | 1.02x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 640 ms: 1.20x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 676 ms: 1.14x faster                                                  |
| async_tree_io_tg                 | 565 ms                                                     | 509 ms: 1.11x faster                                                  |
| async_tree_none_tg               | 198 ms                                                     | 183 ms: 1.08x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 240 ms: 1.08x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 195 ms: 1.07x faster                                                  |
| async_tree_memoization_tg        | 240 ms                                                     | 228 ms: 1.05x faster                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 453 ms: 1.03x faster                                                  |
| async_tree_io                    | 563 ms                                                     | 547 ms: 1.03x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 361 ms: 1.01x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.2 ms: 1.02x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 337 ms: 1.02x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 62.3 ms: 1.03x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.04x faster                                                          |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 48.4 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                      | 1.00x faster                                                          |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.55 ms: 1.01x faster                                                 |
| regex_dna      | 149 ms                                                     | 150 ms: 1.00x slower                                                  |
| regex_v8       | 17.3 ms                                                    | 17.4 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                      | 1.00x faster                                                          |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                   | 1.48 sec: 1.01x slower                                                |
| xml_etree_generate   | 52.7 ms                                                    | 53.4 ms: 1.01x slower                                                 |
| unpickle_pure_python | 141 us                                                     | 143 us: 1.02x slower                                                  |
| json_loads           | 16.8 us                                                    | 17.2 us: 1.02x slower                                                 |
| xml_etree_process    | 37.1 ms                                                    | 37.9 ms: 1.02x slower                                                 |
| pickle_pure_python   | 179 us                                                     | 184 us: 1.03x slower                                                  |
| xml_etree_iterparse  | 71.5 ms                                                    | 74.3 ms: 1.04x slower                                                 |
| xml_etree_parse      | 106 ms                                                     | 111 ms: 1.05x slower                                                  |
| json_dumps           | 6.23 ms                                                    | 6.54 ms: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.03x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 15.4 ms: 1.02x slower                                                 |
| python_startup_no_site | 12.3 ms                                                    | 12.8 ms: 1.04x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.03x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 7.02 ms: 1.00x slower                                                 |
| genshi_xml      | 29.9 ms                                                    | 30.3 ms: 1.01x slower                                                 |
| genshi_text     | 13.9 ms                                                    | 14.1 ms: 1.01x slower                                                 |
| django_template | 19.4 ms                                                    | 19.9 ms: 1.03x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                         | 204 us                                                     | 145 us: 1.40x faster                                                  |
| deepcopy_memo                    | 22.6 us                                                    | 16.9 us: 1.34x faster                                                 |
| deepcopy_reduce                  | 1.82 us                                                    | 1.50 us: 1.21x faster                                                 |
| async_tree_eager_io              | 766 ms                                                     | 640 ms: 1.20x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 676 ms: 1.14x faster                                                  |
| generators                       | 22.9 ms                                                    | 20.6 ms: 1.11x faster                                                 |
| async_tree_io_tg                 | 565 ms                                                     | 509 ms: 1.11x faster                                                  |
| async_tree_none_tg               | 198 ms                                                     | 183 ms: 1.08x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 240 ms: 1.08x faster                                                  |
| mdp                              | 1.53 sec                                                   | 1.42 sec: 1.08x faster                                                |
| async_tree_none                  | 209 ms                                                     | 195 ms: 1.07x faster                                                  |
| async_tree_memoization_tg        | 240 ms                                                     | 228 ms: 1.05x faster                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 453 ms: 1.03x faster                                                  |
| async_tree_io                    | 563 ms                                                     | 547 ms: 1.03x faster                                                  |
| go                               | 101 ms                                                     | 97.7 ms: 1.03x faster                                                 |
| create_gc_cycles                 | 897 us                                                     | 878 us: 1.02x faster                                                  |
| richards_super                   | 35.2 ms                                                    | 34.6 ms: 1.02x faster                                                 |
| dulwich_log                      | 27.6 ms                                                    | 27.1 ms: 1.02x faster                                                 |
| scimark_sor                      | 94.9 ms                                                    | 93.2 ms: 1.02x faster                                                 |
| coverage                         | 45.0 ms                                                    | 44.3 ms: 1.02x faster                                                 |
| regex_effbot                     | 2.58 ms                                                    | 2.55 ms: 1.01x faster                                                 |
| deltablue                        | 2.14 ms                                                    | 2.12 ms: 1.01x faster                                                 |
| pathlib                          | 23.3 ms                                                    | 23.1 ms: 1.01x faster                                                 |
| thrift                           | 435 us                                                     | 432 us: 1.01x faster                                                  |
| richards                         | 31.8 ms                                                    | 31.6 ms: 1.01x faster                                                 |
| float                            | 48.6 ms                                                    | 48.4 ms: 1.00x faster                                                 |
| logging_silent                   | 60.1 ns                                                    | 60.0 ns: 1.00x faster                                                 |
| hexiom                           | 4.06 ms                                                    | 4.06 ms: 1.00x faster                                                 |
| scimark_lu                       | 66.9 ms                                                    | 67.0 ms: 1.00x slower                                                 |
| pyflate                          | 321 ms                                                     | 321 ms: 1.00x slower                                                  |
| logging_simple                   | 3.04 us                                                    | 3.05 us: 1.00x slower                                                 |
| mako                             | 6.99 ms                                                    | 7.02 ms: 1.00x slower                                                 |
| regex_dna                        | 149 ms                                                     | 150 ms: 1.00x slower                                                  |
| gc_traversal                     | 2.45 ms                                                    | 2.46 ms: 1.01x slower                                                 |
| spectral_norm                    | 66.4 ms                                                    | 66.8 ms: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 361 ms: 1.01x slower                                                  |
| tomli_loads                      | 1.47 sec                                                   | 1.48 sec: 1.01x slower                                                |
| regex_v8                         | 17.3 ms                                                    | 17.4 ms: 1.01x slower                                                 |
| json                             | 2.93 ms                                                    | 2.96 ms: 1.01x slower                                                 |
| html5lib                         | 31.2 ms                                                    | 31.5 ms: 1.01x slower                                                 |
| raytrace                         | 147 ms                                                     | 148 ms: 1.01x slower                                                  |
| pprint_safe_repr                 | 465 ms                                                     | 470 ms: 1.01x slower                                                  |
| bench_thread_pool                | 447 us                                                     | 452 us: 1.01x slower                                                  |
| genshi_xml                       | 29.9 ms                                                    | 30.3 ms: 1.01x slower                                                 |
| pprint_pformat                   | 947 ms                                                     | 958 ms: 1.01x slower                                                  |
| sympy_integrate                  | 10.3 ms                                                    | 10.5 ms: 1.01x slower                                                 |
| xml_etree_generate               | 52.7 ms                                                    | 53.4 ms: 1.01x slower                                                 |
| genshi_text                      | 13.9 ms                                                    | 14.1 ms: 1.01x slower                                                 |
| pycparser                        | 632 ms                                                     | 642 ms: 1.02x slower                                                  |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.10 sec: 1.02x slower                                                |
| python_startup                   | 15.2 ms                                                    | 15.4 ms: 1.02x slower                                                 |
| unpickle_pure_python             | 141 us                                                     | 143 us: 1.02x slower                                                  |
| 2to3                             | 161 ms                                                     | 164 ms: 1.02x slower                                                  |
| coroutines                       | 15.8 ms                                                    | 16.1 ms: 1.02x slower                                                 |
| json_loads                       | 16.8 us                                                    | 17.2 us: 1.02x slower                                                 |
| crypto_pyaes                     | 49.5 ms                                                    | 50.4 ms: 1.02x slower                                                 |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.2 ms: 1.02x slower                                                 |
| scimark_monte_carlo              | 42.5 ms                                                    | 43.3 ms: 1.02x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 337 ms: 1.02x slower                                                  |
| logging_format                   | 3.31 us                                                    | 3.38 us: 1.02x slower                                                 |
| nqueens                          | 52.2 ms                                                    | 53.3 ms: 1.02x slower                                                 |
| sqlglot_parse                    | 732 us                                                     | 748 us: 1.02x slower                                                  |
| scimark_fft                      | 181 ms                                                     | 185 ms: 1.02x slower                                                  |
| sqlglot_optimize                 | 30.9 ms                                                    | 31.6 ms: 1.02x slower                                                 |
| sqlglot_transpile                | 891 us                                                     | 911 us: 1.02x slower                                                  |
| xml_etree_process                | 37.1 ms                                                    | 37.9 ms: 1.02x slower                                                 |
| sympy_str                        | 131 ms                                                     | 135 ms: 1.02x slower                                                  |
| bench_mp_pool                    | 47.2 ms                                                    | 48.3 ms: 1.02x slower                                                 |
| meteor_contest                   | 70.3 ms                                                    | 72.1 ms: 1.03x slower                                                 |
| sympy_expand                     | 226 ms                                                     | 232 ms: 1.03x slower                                                  |
| sympy_sum                        | 69.2 ms                                                    | 71.0 ms: 1.03x slower                                                 |
| django_template                  | 19.4 ms                                                    | 19.9 ms: 1.03x slower                                                 |
| pickle_pure_python               | 179 us                                                     | 184 us: 1.03x slower                                                  |
| sqlglot_normalize                | 166 ms                                                     | 171 ms: 1.03x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 62.3 ms: 1.03x slower                                                 |
| dask                             | 221 ms                                                     | 230 ms: 1.04x slower                                                  |
| python_startup_no_site           | 12.3 ms                                                    | 12.8 ms: 1.04x slower                                                 |
| docutils                         | 1.44 sec                                                   | 1.49 sec: 1.04x slower                                                |
| xml_etree_iterparse              | 71.5 ms                                                    | 74.3 ms: 1.04x slower                                                 |
| xml_etree_parse                  | 106 ms                                                     | 111 ms: 1.05x slower                                                  |
| json_dumps                       | 6.23 ms                                                    | 6.54 ms: 1.05x slower                                                 |
| chaos                            | 34.0 ms                                                    | 36.0 ms: 1.06x slower                                                 |
| fannkuch                         | 248 ms                                                     | 263 ms: 1.06x slower                                                  |
| typing_runtime_protocols         | 87.6 us                                                    | 94.2 us: 1.08x slower                                                 |
| comprehensions                   | 10.2 us                                                    | 10.9 us: 1.08x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.01x faster                                                          |

Benchmark hidden because not significant (14): async_tree_cpu_io_mixed_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_generators, scimark_sparse_mat_mult, regex_compile, asyncio_websockets, pidigits, asyncio_tcp_ssl, telco, nbody, tornado_http, asyncio_tcp, pylint
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.11% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.38x