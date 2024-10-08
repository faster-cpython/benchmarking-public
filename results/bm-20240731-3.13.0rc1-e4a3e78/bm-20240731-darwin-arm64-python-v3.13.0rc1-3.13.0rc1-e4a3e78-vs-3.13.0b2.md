# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0rc1
- machine: darwin-arm64
- commit hash: e4a3e78
- commit date: 2024-07-31
- overall geometric mean: 1.01x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.39x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| chameleon      | 4.27 ms                                                    | 4.36 ms: 1.02x slower                                        |
| docutils       | 1.44 sec                                                   | 1.45 sec: 1.01x slower                                       |
| html5lib       | 31.2 ms                                                    | 31.7 ms: 1.02x slower                                        |
| Geometric mean | (ref)                                                      | 1.01x slower                                                 |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 332 ms: 1.00x slower                                         |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 360 ms: 1.01x slower                                         |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.7 ms: 1.01x slower                                        |
| async_tree_eager                 | 60.3 ms                                                    | 61.5 ms: 1.02x slower                                        |
| Geometric mean                   | (ref)                                                      | 1.00x slower                                                 |

Benchmark hidden because not significant (12): async_tree_io, async_tree_eager_io_tg, async_tree_eager_io, async_tree_none_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_eager_memoization_tg, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 48.5 ms: 1.00x faster                                        |
| pidigits       | 282 ms                                                     | 283 ms: 1.00x slower                                         |
| nbody          | 59.6 ms                                                    | 60.6 ms: 1.02x slower                                        |
| Geometric mean | (ref)                                                      | 1.01x slower                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| regex_v8       | 17.3 ms                                                    | 17.3 ms: 1.00x slower                                        |
| regex_effbot   | 2.58 ms                                                    | 2.59 ms: 1.00x slower                                        |
| regex_compile  | 68.5 ms                                                    | 69.3 ms: 1.01x slower                                        |
| regex_dna      | 149 ms                                                     | 151 ms: 1.01x slower                                         |
| Geometric mean | (ref)                                                      | 1.01x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| xml_etree_iterparse  | 71.5 ms                                                    | 72.0 ms: 1.01x slower                                        |
| xml_etree_generate   | 52.7 ms                                                    | 53.2 ms: 1.01x slower                                        |
| unpickle_pure_python | 141 us                                                     | 143 us: 1.02x slower                                         |
| pickle_pure_python   | 179 us                                                     | 182 us: 1.02x slower                                         |
| xml_etree_process    | 37.1 ms                                                    | 38.0 ms: 1.03x slower                                        |
| Geometric mean       | (ref)                                                      | 1.01x slower                                                 |

Benchmark hidden because not significant (4): tomli_loads, json_dumps, xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|------------------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 15.4 ms: 1.01x slower                                        |
| python_startup_no_site | 12.3 ms                                                    | 12.7 ms: 1.03x slower                                        |
| Geometric mean         | (ref)                                                      | 1.02x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|-----------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_text     | 13.9 ms                                                    | 14.0 ms: 1.00x slower                                        |
| genshi_xml      | 29.9 ms                                                    | 30.1 ms: 1.01x slower                                        |
| django_template | 19.4 ms                                                    | 20.0 ms: 1.03x slower                                        |
| mako            | 6.99 ms                                                    | 7.23 ms: 1.03x slower                                        |
| Geometric mean  | (ref)                                                      | 1.02x slower                                                 |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| mdp                              | 1.53 sec                                                   | 1.43 sec: 1.08x faster                                       |
| asyncio_tcp_ssl                  | 1.29 sec                                                   | 1.27 sec: 1.02x faster                                       |
| create_gc_cycles                 | 897 us                                                     | 880 us: 1.02x faster                                         |
| richards_super                   | 35.2 ms                                                    | 34.7 ms: 1.01x faster                                        |
| json                             | 2.93 ms                                                    | 2.90 ms: 1.01x faster                                        |
| dulwich_log                      | 27.6 ms                                                    | 27.3 ms: 1.01x faster                                        |
| richards                         | 31.8 ms                                                    | 31.6 ms: 1.01x faster                                        |
| float                            | 48.6 ms                                                    | 48.5 ms: 1.00x faster                                        |
| meteor_contest                   | 70.3 ms                                                    | 70.4 ms: 1.00x slower                                        |
| regex_v8                         | 17.3 ms                                                    | 17.3 ms: 1.00x slower                                        |
| pidigits                         | 282 ms                                                     | 283 ms: 1.00x slower                                         |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.06 sec: 1.00x slower                                       |
| scimark_sor                      | 94.9 ms                                                    | 95.2 ms: 1.00x slower                                        |
| regex_effbot                     | 2.58 ms                                                    | 2.59 ms: 1.00x slower                                        |
| genshi_text                      | 13.9 ms                                                    | 14.0 ms: 1.00x slower                                        |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 332 ms: 1.00x slower                                         |
| gc_traversal                     | 2.45 ms                                                    | 2.46 ms: 1.00x slower                                        |
| genshi_xml                       | 29.9 ms                                                    | 30.1 ms: 1.01x slower                                        |
| deepcopy_reduce                  | 1.82 us                                                    | 1.83 us: 1.01x slower                                        |
| deltablue                        | 2.14 ms                                                    | 2.15 ms: 1.01x slower                                        |
| xml_etree_iterparse              | 71.5 ms                                                    | 72.0 ms: 1.01x slower                                        |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 360 ms: 1.01x slower                                         |
| pprint_pformat                   | 947 ms                                                     | 953 ms: 1.01x slower                                         |
| deepcopy                         | 204 us                                                     | 205 us: 1.01x slower                                         |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.7 ms: 1.01x slower                                        |
| telco                            | 4.60 ms                                                    | 4.64 ms: 1.01x slower                                        |
| sympy_integrate                  | 10.3 ms                                                    | 10.4 ms: 1.01x slower                                        |
| async_generators                 | 281 ms                                                     | 283 ms: 1.01x slower                                         |
| coroutines                       | 15.8 ms                                                    | 16.0 ms: 1.01x slower                                        |
| pycparser                        | 632 ms                                                     | 638 ms: 1.01x slower                                         |
| hexiom                           | 4.06 ms                                                    | 4.10 ms: 1.01x slower                                        |
| sympy_str                        | 131 ms                                                     | 133 ms: 1.01x slower                                         |
| scimark_monte_carlo              | 42.5 ms                                                    | 42.9 ms: 1.01x slower                                        |
| sympy_expand                     | 226 ms                                                     | 228 ms: 1.01x slower                                         |
| raytrace                         | 147 ms                                                     | 148 ms: 1.01x slower                                         |
| sqlglot_normalize                | 166 ms                                                     | 167 ms: 1.01x slower                                         |
| docutils                         | 1.44 sec                                                   | 1.45 sec: 1.01x slower                                       |
| typing_runtime_protocols         | 87.6 us                                                    | 88.5 us: 1.01x slower                                        |
| xml_etree_generate               | 52.7 ms                                                    | 53.2 ms: 1.01x slower                                        |
| pprint_safe_repr                 | 465 ms                                                     | 469 ms: 1.01x slower                                         |
| crypto_pyaes                     | 49.5 ms                                                    | 50.0 ms: 1.01x slower                                        |
| regex_compile                    | 68.5 ms                                                    | 69.3 ms: 1.01x slower                                        |
| logging_format                   | 3.31 us                                                    | 3.35 us: 1.01x slower                                        |
| regex_dna                        | 149 ms                                                     | 151 ms: 1.01x slower                                         |
| sqlglot_parse                    | 732 us                                                     | 741 us: 1.01x slower                                         |
| sqlglot_optimize                 | 30.9 ms                                                    | 31.3 ms: 1.01x slower                                        |
| logging_silent                   | 60.1 ns                                                    | 60.9 ns: 1.01x slower                                        |
| python_startup                   | 15.2 ms                                                    | 15.4 ms: 1.01x slower                                        |
| chaos                            | 34.0 ms                                                    | 34.5 ms: 1.01x slower                                        |
| sympy_sum                        | 69.2 ms                                                    | 70.2 ms: 1.01x slower                                        |
| sqlglot_transpile                | 891 us                                                     | 904 us: 1.01x slower                                         |
| spectral_norm                    | 66.4 ms                                                    | 67.4 ms: 1.02x slower                                        |
| scimark_lu                       | 66.9 ms                                                    | 67.9 ms: 1.02x slower                                        |
| unpickle_pure_python             | 141 us                                                     | 143 us: 1.02x slower                                         |
| nbody                            | 59.6 ms                                                    | 60.6 ms: 1.02x slower                                        |
| html5lib                         | 31.2 ms                                                    | 31.7 ms: 1.02x slower                                        |
| scimark_fft                      | 181 ms                                                     | 184 ms: 1.02x slower                                         |
| logging_simple                   | 3.04 us                                                    | 3.10 us: 1.02x slower                                        |
| pathlib                          | 23.3 ms                                                    | 23.8 ms: 1.02x slower                                        |
| pickle_pure_python               | 179 us                                                     | 182 us: 1.02x slower                                         |
| async_tree_eager                 | 60.3 ms                                                    | 61.5 ms: 1.02x slower                                        |
| nqueens                          | 52.2 ms                                                    | 53.3 ms: 1.02x slower                                        |
| fannkuch                         | 248 ms                                                     | 254 ms: 1.02x slower                                         |
| chameleon                        | 4.27 ms                                                    | 4.36 ms: 1.02x slower                                        |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.84 ms: 1.02x slower                                        |
| xml_etree_process                | 37.1 ms                                                    | 38.0 ms: 1.03x slower                                        |
| django_template                  | 19.4 ms                                                    | 20.0 ms: 1.03x slower                                        |
| deepcopy_memo                    | 22.6 us                                                    | 23.2 us: 1.03x slower                                        |
| python_startup_no_site           | 12.3 ms                                                    | 12.7 ms: 1.03x slower                                        |
| mako                             | 6.99 ms                                                    | 7.23 ms: 1.03x slower                                        |
| bench_thread_pool                | 447 us                                                     | 463 us: 1.04x slower                                         |
| comprehensions                   | 10.2 us                                                    | 10.6 us: 1.05x slower                                        |
| mypy2                            | 379 ms                                                     | 455 ms: 1.20x slower                                         |
| Geometric mean                   | (ref)                                                      | 1.01x slower                                                 |

Benchmark hidden because not significant (28): async_tree_io, async_tree_eager_io_tg, dask, async_tree_eager_io, 2to3, tomli_loads, async_tree_none_tg, generators, async_tree_io_tg, json_dumps, thrift, asyncio_websockets, xml_etree_parse, pyflate, async_tree_memoization_tg, json_loads, coverage, async_tree_memoization, go, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_eager_memoization_tg, async_tree_eager_memoization, tornado_http, bench_mp_pool, asyncio_tcp, pylint
Ignored benchmarks (9) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.39x