# Results vs. 3.13.0b2

- fork: python
- ref: fe85a8291d9aa11c9ce9
- machine: darwin-arm64
- commit hash: fe85a82
- commit date: 2024-08-26
- overall geometric mean: 1.00x faster
- HPT reliability: 98.12%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.51x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-darwin-arm64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 184 ms: 1.14x slower                                                  |
| docutils       | 1.44 sec                                                   | 1.47 sec: 1.02x slower                                                |
| tornado_http   | 66.7 ms                                                    | 81.9 ms: 1.23x slower                                                 |
| Geometric mean | (ref)                                                      | 1.09x slower                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-darwin-arm64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 680 ms: 1.13x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 194 ms: 1.08x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 714 ms: 1.08x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 248 ms: 1.05x faster                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 60.6 ms: 1.00x slower                                                 |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.7 ms: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 336 ms: 1.01x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 364 ms: 1.02x slower                                                  |
| async_tree_io                    | 563 ms                                                     | 592 ms: 1.05x slower                                                  |
| Geometric mean                   | (ref)                                                      | 1.01x faster                                                          |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed, async_tree_eager_memoization_tg, async_tree_none_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-darwin-arm64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 59.6 ms                                                    | 59.4 ms: 1.00x faster                                                 |
| pidigits       | 282 ms                                                     | 282 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                      | 1.00x faster                                                          |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-darwin-arm64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.46 ms: 1.05x faster                                                 |
| regex_v8       | 17.3 ms                                                    | 16.6 ms: 1.04x faster                                                 |
| regex_dna      | 149 ms                                                     | 145 ms: 1.03x faster                                                  |
| regex_compile  | 68.5 ms                                                    | 66.9 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                      | 1.04x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-darwin-arm64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_generate   | 52.7 ms                                                    | 53.1 ms: 1.01x slower                                                 |
| xml_etree_process    | 37.1 ms                                                    | 37.4 ms: 1.01x slower                                                 |
| tomli_loads          | 1.47 sec                                                   | 1.48 sec: 1.01x slower                                                |
| json_dumps           | 6.23 ms                                                    | 6.32 ms: 1.01x slower                                                 |
| unpickle_pure_python | 141 us                                                     | 143 us: 1.02x slower                                                  |
| pickle_pure_python   | 179 us                                                     | 182 us: 1.02x slower                                                  |
| json_loads           | 16.8 us                                                    | 17.2 us: 1.02x slower                                                 |
| xml_etree_iterparse  | 71.5 ms                                                    | 74.1 ms: 1.04x slower                                                 |
| xml_etree_parse      | 106 ms                                                     | 111 ms: 1.05x slower                                                  |
| Geometric mean       | (ref)                                                      | 1.02x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-darwin-arm64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 16.0 ms: 1.06x slower                                                 |
| python_startup_no_site | 12.3 ms                                                    | 13.2 ms: 1.07x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-darwin-arm64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 6.95 ms: 1.01x faster                                                 |
| genshi_text     | 13.9 ms                                                    | 13.9 ms: 1.00x faster                                                 |
| genshi_xml      | 29.9 ms                                                    | 30.2 ms: 1.01x slower                                                 |
| django_template | 19.4 ms                                                    | 19.7 ms: 1.02x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.00x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-darwin-arm64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                         | 204 us                                                     | 143 us: 1.43x faster                                                  |
| deepcopy_memo                    | 22.6 us                                                    | 16.9 us: 1.34x faster                                                 |
| deepcopy_reduce                  | 1.82 us                                                    | 1.50 us: 1.21x faster                                                 |
| async_tree_eager_io              | 766 ms                                                     | 680 ms: 1.13x faster                                                  |
| generators                       | 22.9 ms                                                    | 20.5 ms: 1.11x faster                                                 |
| mdp                              | 1.53 sec                                                   | 1.42 sec: 1.08x faster                                                |
| async_tree_none                  | 209 ms                                                     | 194 ms: 1.08x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 714 ms: 1.08x faster                                                  |
| richards_super                   | 35.2 ms                                                    | 33.3 ms: 1.06x faster                                                 |
| regex_effbot                     | 2.58 ms                                                    | 2.46 ms: 1.05x faster                                                 |
| richards                         | 31.8 ms                                                    | 30.4 ms: 1.05x faster                                                 |
| async_tree_memoization           | 260 ms                                                     | 248 ms: 1.05x faster                                                  |
| regex_v8                         | 17.3 ms                                                    | 16.6 ms: 1.04x faster                                                 |
| thrift                           | 435 us                                                     | 418 us: 1.04x faster                                                  |
| pprint_safe_repr                 | 465 ms                                                     | 451 ms: 1.03x faster                                                  |
| regex_dna                        | 149 ms                                                     | 145 ms: 1.03x faster                                                  |
| dulwich_log                      | 27.6 ms                                                    | 26.9 ms: 1.02x faster                                                 |
| regex_compile                    | 68.5 ms                                                    | 66.9 ms: 1.02x faster                                                 |
| scimark_sor                      | 94.9 ms                                                    | 92.8 ms: 1.02x faster                                                 |
| pprint_pformat                   | 947 ms                                                     | 928 ms: 1.02x faster                                                  |
| comprehensions                   | 10.2 us                                                    | 9.99 us: 1.02x faster                                                 |
| coverage                         | 45.0 ms                                                    | 44.6 ms: 1.01x faster                                                 |
| asyncio_tcp_ssl                  | 1.29 sec                                                   | 1.28 sec: 1.01x faster                                                |
| mako                             | 6.99 ms                                                    | 6.95 ms: 1.01x faster                                                 |
| genshi_text                      | 13.9 ms                                                    | 13.9 ms: 1.00x faster                                                 |
| nbody                            | 59.6 ms                                                    | 59.4 ms: 1.00x faster                                                 |
| pidigits                         | 282 ms                                                     | 282 ms: 1.00x faster                                                  |
| hexiom                           | 4.06 ms                                                    | 4.07 ms: 1.00x slower                                                 |
| async_tree_eager                 | 60.3 ms                                                    | 60.6 ms: 1.00x slower                                                 |
| json                             | 2.93 ms                                                    | 2.95 ms: 1.01x slower                                                 |
| create_gc_cycles                 | 897 us                                                     | 903 us: 1.01x slower                                                  |
| xml_etree_generate               | 52.7 ms                                                    | 53.1 ms: 1.01x slower                                                 |
| sqlglot_optimize                 | 30.9 ms                                                    | 31.1 ms: 1.01x slower                                                 |
| sympy_expand                     | 226 ms                                                     | 228 ms: 1.01x slower                                                  |
| xml_etree_process                | 37.1 ms                                                    | 37.4 ms: 1.01x slower                                                 |
| genshi_xml                       | 29.9 ms                                                    | 30.2 ms: 1.01x slower                                                 |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.7 ms: 1.01x slower                                                 |
| spectral_norm                    | 66.4 ms                                                    | 67.0 ms: 1.01x slower                                                 |
| sqlglot_normalize                | 166 ms                                                     | 167 ms: 1.01x slower                                                  |
| raytrace                         | 147 ms                                                     | 149 ms: 1.01x slower                                                  |
| tomli_loads                      | 1.47 sec                                                   | 1.48 sec: 1.01x slower                                                |
| pycparser                        | 632 ms                                                     | 641 ms: 1.01x slower                                                  |
| async_generators                 | 281 ms                                                     | 285 ms: 1.01x slower                                                  |
| json_dumps                       | 6.23 ms                                                    | 6.32 ms: 1.01x slower                                                 |
| logging_silent                   | 60.1 ns                                                    | 61.0 ns: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 336 ms: 1.01x slower                                                  |
| django_template                  | 19.4 ms                                                    | 19.7 ms: 1.02x slower                                                 |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 364 ms: 1.02x slower                                                  |
| sqlglot_transpile                | 891 us                                                     | 904 us: 1.02x slower                                                  |
| logging_simple                   | 3.04 us                                                    | 3.09 us: 1.02x slower                                                 |
| coroutines                       | 15.8 ms                                                    | 16.1 ms: 1.02x slower                                                 |
| scimark_monte_carlo              | 42.5 ms                                                    | 43.2 ms: 1.02x slower                                                 |
| unpickle_pure_python             | 141 us                                                     | 143 us: 1.02x slower                                                  |
| scimark_lu                       | 66.9 ms                                                    | 68.1 ms: 1.02x slower                                                 |
| scimark_fft                      | 181 ms                                                     | 184 ms: 1.02x slower                                                  |
| docutils                         | 1.44 sec                                                   | 1.47 sec: 1.02x slower                                                |
| nqueens                          | 52.2 ms                                                    | 53.3 ms: 1.02x slower                                                 |
| sqlglot_parse                    | 732 us                                                     | 747 us: 1.02x slower                                                  |
| pickle_pure_python               | 179 us                                                     | 182 us: 1.02x slower                                                  |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.12 sec: 1.02x slower                                                |
| meteor_contest                   | 70.3 ms                                                    | 71.9 ms: 1.02x slower                                                 |
| json_loads                       | 16.8 us                                                    | 17.2 us: 1.02x slower                                                 |
| logging_format                   | 3.31 us                                                    | 3.39 us: 1.02x slower                                                 |
| bench_mp_pool                    | 47.2 ms                                                    | 48.3 ms: 1.02x slower                                                 |
| telco                            | 4.60 ms                                                    | 4.72 ms: 1.03x slower                                                 |
| crypto_pyaes                     | 49.5 ms                                                    | 51.1 ms: 1.03x slower                                                 |
| xml_etree_iterparse              | 71.5 ms                                                    | 74.1 ms: 1.04x slower                                                 |
| typing_runtime_protocols         | 87.6 us                                                    | 91.0 us: 1.04x slower                                                 |
| chaos                            | 34.0 ms                                                    | 35.7 ms: 1.05x slower                                                 |
| async_tree_io                    | 563 ms                                                     | 592 ms: 1.05x slower                                                  |
| go                               | 101 ms                                                     | 106 ms: 1.05x slower                                                  |
| xml_etree_parse                  | 106 ms                                                     | 111 ms: 1.05x slower                                                  |
| fannkuch                         | 248 ms                                                     | 262 ms: 1.06x slower                                                  |
| python_startup                   | 15.2 ms                                                    | 16.0 ms: 1.06x slower                                                 |
| python_startup_no_site           | 12.3 ms                                                    | 13.2 ms: 1.07x slower                                                 |
| 2to3                             | 161 ms                                                     | 184 ms: 1.14x slower                                                  |
| tornado_http                     | 66.7 ms                                                    | 81.9 ms: 1.23x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.00x faster                                                          |

Benchmark hidden because not significant (21): async_tree_cpu_io_mixed, async_tree_eager_memoization_tg, sympy_sum, async_tree_none_tg, asyncio_websockets, deltablue, async_tree_io_tg, pyflate, float, html5lib, sympy_integrate, pathlib, bench_thread_pool, sympy_str, gc_traversal, scimark_sparse_mat_mult, asyncio_tcp, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_memoization, pylint
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 98.12% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.51x