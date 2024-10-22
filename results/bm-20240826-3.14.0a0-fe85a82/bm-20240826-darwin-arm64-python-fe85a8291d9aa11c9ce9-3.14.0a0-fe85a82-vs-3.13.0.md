# Results vs. 3.13.0

- fork: python
- ref: fe85a8291d9aa11c9ce9
- machine: darwin-arm64
- commit hash: fe85a82
- commit date: 2024-08-26
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-darwin-arm64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 184 ms: 1.03x slower                                                  |
| docutils       | 1.44 sec                                               | 1.47 sec: 1.01x slower                                                |
| html5lib       | 36.6 ms                                                | 31.2 ms: 1.18x faster                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-darwin-arm64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.1 ms: 1.23x faster                                                 |
| async_tree_memoization_tg        | 291 ms                                                 | 243 ms: 1.20x faster                                                  |
| async_tree_eager                 | 70.5 ms                                                | 60.6 ms: 1.16x faster                                                 |
| async_tree_eager_tg              | 48.4 ms                                                | 41.7 ms: 1.16x faster                                                 |
| asyncio_tcp                      | 457 ms                                                 | 403 ms: 1.13x faster                                                  |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 125 ms: 1.11x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 194 ms: 1.09x faster                                                  |
| async_tree_memoization           | 270 ms                                                 | 248 ms: 1.09x faster                                                  |
| async_tree_eager_memoization     | 169 ms                                                 | 156 ms: 1.09x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 336 ms: 1.04x faster                                                  |
| async_generators                 | 294 ms                                                 | 285 ms: 1.03x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 364 ms: 1.03x faster                                                  |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.28 sec: 1.01x slower                                                |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 457 ms: 1.02x slower                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 564 ms: 1.13x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 592 ms: 1.17x slower                                                  |
| async_tree_eager_io              | 513 ms                                                 | 680 ms: 1.33x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 714 ms: 1.50x slower                                                  |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (2): async_tree_none_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-darwin-arm64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 73.9 ms                                                | 59.4 ms: 1.24x faster                                                 |
| float          | 56.2 ms                                                | 48.6 ms: 1.16x faster                                                 |
| pidigits       | 284 ms                                                 | 282 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-darwin-arm64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 66.9 ms: 1.17x faster                                                 |
| regex_effbot   | 2.63 ms                                                | 2.46 ms: 1.07x faster                                                 |
| regex_v8       | 16.9 ms                                                | 16.6 ms: 1.02x faster                                                 |
| regex_dna      | 148 ms                                                 | 145 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-darwin-arm64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 213 us                                                 | 182 us: 1.17x faster                                                  |
| unpickle_pure_python | 163 us                                                 | 143 us: 1.14x faster                                                  |
| xml_etree_process    | 40.9 ms                                                | 37.4 ms: 1.09x faster                                                 |
| xml_etree_generate   | 56.6 ms                                                | 53.1 ms: 1.07x faster                                                 |
| tomli_loads          | 1.56 sec                                               | 1.48 sec: 1.05x faster                                                |
| json_dumps           | 6.56 ms                                                | 6.32 ms: 1.04x faster                                                 |
| json_loads           | 16.9 us                                                | 17.2 us: 1.02x slower                                                 |
| xml_etree_parse      | 109 ms                                                 | 111 ms: 1.02x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-darwin-arm64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.0 ms                                                | 16.0 ms: 1.06x faster                                                 |
| python_startup_no_site | 13.7 ms                                                | 13.2 ms: 1.04x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-darwin-arm64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 13.9 ms: 1.22x faster                                                 |
| genshi_xml      | 34.4 ms                                                | 30.2 ms: 1.14x faster                                                 |
| django_template | 22.2 ms                                                | 19.7 ms: 1.13x faster                                                 |
| mako            | 7.68 ms                                                | 6.95 ms: 1.11x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.15x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-darwin-arm64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                         | 232 us                                                 | 143 us: 1.62x faster                                                  |
| deepcopy_memo                    | 27.2 us                                                | 16.9 us: 1.61x faster                                                 |
| generators                       | 31.5 ms                                                | 20.5 ms: 1.53x faster                                                 |
| deepcopy_reduce                  | 2.06 us                                                | 1.50 us: 1.37x faster                                                 |
| deltablue                        | 2.68 ms                                                | 2.14 ms: 1.25x faster                                                 |
| nbody                            | 73.9 ms                                                | 59.4 ms: 1.24x faster                                                 |
| coroutines                       | 19.8 ms                                                | 16.1 ms: 1.23x faster                                                 |
| raytrace                         | 182 ms                                                 | 149 ms: 1.22x faster                                                  |
| comprehensions                   | 12.2 us                                                | 9.99 us: 1.22x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 13.9 ms: 1.22x faster                                                 |
| async_tree_memoization_tg        | 291 ms                                                 | 243 ms: 1.20x faster                                                  |
| hexiom                           | 4.85 ms                                                | 4.07 ms: 1.19x faster                                                 |
| nqueens                          | 62.9 ms                                                | 53.3 ms: 1.18x faster                                                 |
| pprint_safe_repr                 | 531 ms                                                 | 451 ms: 1.18x faster                                                  |
| html5lib                         | 36.6 ms                                                | 31.2 ms: 1.18x faster                                                 |
| richards_super                   | 39.1 ms                                                | 33.3 ms: 1.18x faster                                                 |
| regex_compile                    | 78.5 ms                                                | 66.9 ms: 1.17x faster                                                 |
| pickle_pure_python               | 213 us                                                 | 182 us: 1.17x faster                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 43.2 ms: 1.17x faster                                                 |
| richards                         | 35.4 ms                                                | 30.4 ms: 1.17x faster                                                 |
| async_tree_eager                 | 70.5 ms                                                | 60.6 ms: 1.16x faster                                                 |
| pprint_pformat                   | 1.08 sec                                               | 928 ms: 1.16x faster                                                  |
| async_tree_eager_tg              | 48.4 ms                                                | 41.7 ms: 1.16x faster                                                 |
| float                            | 56.2 ms                                                | 48.6 ms: 1.16x faster                                                 |
| chaos                            | 41.3 ms                                                | 35.7 ms: 1.16x faster                                                 |
| logging_simple                   | 3.57 us                                                | 3.09 us: 1.16x faster                                                 |
| spectral_norm                    | 77.3 ms                                                | 67.0 ms: 1.15x faster                                                 |
| sqlglot_parse                    | 856 us                                                 | 747 us: 1.15x faster                                                  |
| logging_silent                   | 69.9 ns                                                | 61.0 ns: 1.14x faster                                                 |
| unpickle_pure_python             | 163 us                                                 | 143 us: 1.14x faster                                                  |
| genshi_xml                       | 34.4 ms                                                | 30.2 ms: 1.14x faster                                                 |
| scimark_sor                      | 106 ms                                                 | 92.8 ms: 1.14x faster                                                 |
| logging_format                   | 3.85 us                                                | 3.39 us: 1.14x faster                                                 |
| asyncio_tcp                      | 457 ms                                                 | 403 ms: 1.13x faster                                                  |
| sqlglot_transpile                | 1.02 ms                                                | 904 us: 1.13x faster                                                  |
| bench_thread_pool                | 506 us                                                 | 447 us: 1.13x faster                                                  |
| sqlglot_normalize                | 189 ms                                                 | 167 ms: 1.13x faster                                                  |
| django_template                  | 22.2 ms                                                | 19.7 ms: 1.13x faster                                                 |
| scimark_lu                       | 76.5 ms                                                | 68.1 ms: 1.12x faster                                                 |
| sqlglot_optimize                 | 34.9 ms                                                | 31.1 ms: 1.12x faster                                                 |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 125 ms: 1.11x faster                                                  |
| thrift                           | 466 us                                                 | 418 us: 1.11x faster                                                  |
| typing_runtime_protocols         | 101 us                                                 | 91.0 us: 1.11x faster                                                 |
| mako                             | 7.68 ms                                                | 6.95 ms: 1.11x faster                                                 |
| sympy_str                        | 145 ms                                                 | 132 ms: 1.11x faster                                                  |
| pycparser                        | 706 ms                                                 | 641 ms: 1.10x faster                                                  |
| sympy_sum                        | 75.6 ms                                                | 69.0 ms: 1.10x faster                                                 |
| pyflate                          | 351 ms                                                 | 321 ms: 1.10x faster                                                  |
| sympy_integrate                  | 11.3 ms                                                | 10.3 ms: 1.09x faster                                                 |
| xml_etree_process                | 40.9 ms                                                | 37.4 ms: 1.09x faster                                                 |
| scimark_fft                      | 201 ms                                                 | 184 ms: 1.09x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 194 ms: 1.09x faster                                                  |
| async_tree_memoization           | 270 ms                                                 | 248 ms: 1.09x faster                                                  |
| go                               | 115 ms                                                 | 106 ms: 1.09x faster                                                  |
| async_tree_eager_memoization     | 169 ms                                                 | 156 ms: 1.09x faster                                                  |
| sympy_expand                     | 246 ms                                                 | 228 ms: 1.08x faster                                                  |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.78 ms: 1.08x faster                                                 |
| fannkuch                         | 282 ms                                                 | 262 ms: 1.08x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 26.9 ms: 1.07x faster                                                 |
| regex_effbot                     | 2.63 ms                                                | 2.46 ms: 1.07x faster                                                 |
| xml_etree_generate               | 56.6 ms                                                | 53.1 ms: 1.07x faster                                                 |
| python_startup                   | 17.0 ms                                                | 16.0 ms: 1.06x faster                                                 |
| crypto_pyaes                     | 54.0 ms                                                | 51.1 ms: 1.06x faster                                                 |
| mdp                              | 1.50 sec                                               | 1.42 sec: 1.06x faster                                                |
| bench_mp_pool                    | 50.9 ms                                                | 48.3 ms: 1.05x faster                                                 |
| tomli_loads                      | 1.56 sec                                               | 1.48 sec: 1.05x faster                                                |
| bpe_tokeniser                    | 3.24 sec                                               | 3.12 sec: 1.04x faster                                                |
| json_dumps                       | 6.56 ms                                                | 6.32 ms: 1.04x faster                                                 |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 336 ms: 1.04x faster                                                  |
| python_startup_no_site           | 13.7 ms                                                | 13.2 ms: 1.04x faster                                                 |
| coverage                         | 46.1 ms                                                | 44.6 ms: 1.03x faster                                                 |
| async_generators                 | 294 ms                                                 | 285 ms: 1.03x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 364 ms: 1.03x faster                                                  |
| meteor_contest                   | 73.8 ms                                                | 71.9 ms: 1.03x faster                                                 |
| regex_v8                         | 16.9 ms                                                | 16.6 ms: 1.02x faster                                                 |
| telco                            | 4.80 ms                                                | 4.72 ms: 1.02x faster                                                 |
| regex_dna                        | 148 ms                                                 | 145 ms: 1.02x faster                                                  |
| gc_traversal                     | 2.48 ms                                                | 2.45 ms: 1.01x faster                                                 |
| pidigits                         | 284 ms                                                 | 282 ms: 1.01x faster                                                  |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.28 sec: 1.01x slower                                                |
| docutils                         | 1.44 sec                                               | 1.47 sec: 1.01x slower                                                |
| json_loads                       | 16.9 us                                                | 17.2 us: 1.02x slower                                                 |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 457 ms: 1.02x slower                                                  |
| pathlib                          | 22.8 ms                                                | 23.3 ms: 1.02x slower                                                 |
| xml_etree_parse                  | 109 ms                                                 | 111 ms: 1.02x slower                                                  |
| 2to3                             | 178 ms                                                 | 184 ms: 1.03x slower                                                  |
| create_gc_cycles                 | 803 us                                                 | 903 us: 1.12x slower                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 564 ms: 1.13x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 592 ms: 1.17x slower                                                  |
| async_tree_eager_io              | 513 ms                                                 | 680 ms: 1.33x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 714 ms: 1.50x slower                                                  |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (6): async_tree_none_tg, xml_etree_iterparse, async_tree_cpu_io_mixed, json, pylint, tornado_http
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 0.99x