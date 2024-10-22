# Results vs. 3.13.0

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: darwin-arm64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.03x faster
- HPT reliability: 97.77%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 180 ms: 1.01x slower                                                  |
| docutils       | 1.44 sec                                               | 1.61 sec: 1.11x slower                                                |
| html5lib       | 36.6 ms                                                | 32.8 ms: 1.12x faster                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.1 ms: 1.23x faster                                                 |
| async_tree_memoization_tg        | 291 ms                                                 | 245 ms: 1.18x faster                                                  |
| async_tree_eager_tg              | 48.4 ms                                                | 41.8 ms: 1.16x faster                                                 |
| async_tree_eager                 | 70.5 ms                                                | 63.3 ms: 1.11x faster                                                 |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 125 ms: 1.11x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 194 ms: 1.09x faster                                                  |
| async_tree_memoization           | 270 ms                                                 | 250 ms: 1.08x faster                                                  |
| async_tree_eager_memoization     | 169 ms                                                 | 160 ms: 1.06x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 338 ms: 1.03x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 365 ms: 1.03x faster                                                  |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.28 sec: 1.02x slower                                                |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 463 ms: 1.04x slower                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 553 ms: 1.11x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 594 ms: 1.17x slower                                                  |
| async_tree_eager_io              | 513 ms                                                 | 681 ms: 1.33x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 718 ms: 1.51x slower                                                  |
| asyncio_websockets               | 241 ms                                                 | 409 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.02x slower                                                          |

Benchmark hidden because not significant (4): asyncio_tcp, async_tree_cpu_io_mixed, async_generators, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 56.2 ms                                                | 46.4 ms: 1.21x faster                                                 |
| nbody          | 73.9 ms                                                | 63.8 ms: 1.16x faster                                                 |
| pidigits       | 284 ms                                                 | 282 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.47 ms: 1.06x faster                                                 |
| regex_compile  | 78.5 ms                                                | 74.9 ms: 1.05x faster                                                 |
| regex_dna      | 148 ms                                                 | 145 ms: 1.02x faster                                                  |
| regex_v8       | 16.9 ms                                                | 16.6 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.56 sec                                               | 1.24 sec: 1.26x faster                                                |
| unpickle_pure_python | 163 us                                                 | 133 us: 1.23x faster                                                  |
| pickle_pure_python   | 213 us                                                 | 177 us: 1.20x faster                                                  |
| xml_etree_process    | 40.9 ms                                                | 34.6 ms: 1.18x faster                                                 |
| xml_etree_generate   | 56.6 ms                                                | 50.7 ms: 1.12x faster                                                 |
| json_dumps           | 6.56 ms                                                | 6.28 ms: 1.05x faster                                                 |
| xml_etree_iterparse  | 74.2 ms                                                | 71.9 ms: 1.03x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 110 ms: 1.01x slower                                                  |
| json_loads           | 16.9 us                                                | 17.3 us: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.0 ms                                                | 16.8 ms: 1.01x faster                                                 |
| python_startup_no_site | 13.7 ms                                                | 13.9 ms: 1.02x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.47 ms: 1.19x faster                                                 |
| django_template | 22.2 ms                                                | 22.1 ms: 1.00x faster                                                 |
| genshi_xml      | 34.4 ms                                                | 41.2 ms: 1.20x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo                    | 27.2 us                                                | 16.1 us: 1.69x faster                                                 |
| deepcopy                         | 232 us                                                 | 154 us: 1.51x faster                                                  |
| deepcopy_reduce                  | 2.06 us                                                | 1.49 us: 1.38x faster                                                 |
| generators                       | 31.5 ms                                                | 24.6 ms: 1.28x faster                                                 |
| tomli_loads                      | 1.56 sec                                               | 1.24 sec: 1.26x faster                                                |
| unpickle_pure_python             | 163 us                                                 | 133 us: 1.23x faster                                                  |
| coroutines                       | 19.8 ms                                                | 16.1 ms: 1.23x faster                                                 |
| float                            | 56.2 ms                                                | 46.4 ms: 1.21x faster                                                 |
| pickle_pure_python               | 213 us                                                 | 177 us: 1.20x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 88.7 ms: 1.19x faster                                                 |
| mako                             | 7.68 ms                                                | 6.47 ms: 1.19x faster                                                 |
| async_tree_memoization_tg        | 291 ms                                                 | 245 ms: 1.18x faster                                                  |
| xml_etree_process                | 40.9 ms                                                | 34.6 ms: 1.18x faster                                                 |
| logging_simple                   | 3.57 us                                                | 3.03 us: 1.18x faster                                                 |
| scimark_lu                       | 76.5 ms                                                | 65.7 ms: 1.16x faster                                                 |
| nbody                            | 73.9 ms                                                | 63.8 ms: 1.16x faster                                                 |
| async_tree_eager_tg              | 48.4 ms                                                | 41.8 ms: 1.16x faster                                                 |
| logging_format                   | 3.85 us                                                | 3.34 us: 1.15x faster                                                 |
| spectral_norm                    | 77.3 ms                                                | 68.3 ms: 1.13x faster                                                 |
| go                               | 115 ms                                                 | 102 ms: 1.13x faster                                                  |
| deltablue                        | 2.68 ms                                                | 2.39 ms: 1.12x faster                                                 |
| logging_silent                   | 69.9 ns                                                | 62.4 ns: 1.12x faster                                                 |
| html5lib                         | 36.6 ms                                                | 32.8 ms: 1.12x faster                                                 |
| xml_etree_generate               | 56.6 ms                                                | 50.7 ms: 1.12x faster                                                 |
| async_tree_eager                 | 70.5 ms                                                | 63.3 ms: 1.11x faster                                                 |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 125 ms: 1.11x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 194 ms: 1.09x faster                                                  |
| thrift                           | 466 us                                                 | 427 us: 1.09x faster                                                  |
| async_tree_memoization           | 270 ms                                                 | 250 ms: 1.08x faster                                                  |
| pyflate                          | 351 ms                                                 | 328 ms: 1.07x faster                                                  |
| fannkuch                         | 282 ms                                                 | 264 ms: 1.07x faster                                                  |
| bench_thread_pool                | 506 us                                                 | 474 us: 1.07x faster                                                  |
| typing_runtime_protocols         | 101 us                                                 | 95.0 us: 1.06x faster                                                 |
| regex_effbot                     | 2.63 ms                                                | 2.47 ms: 1.06x faster                                                 |
| async_tree_eager_memoization     | 169 ms                                                 | 160 ms: 1.06x faster                                                  |
| nqueens                          | 62.9 ms                                                | 59.5 ms: 1.06x faster                                                 |
| scimark_fft                      | 201 ms                                                 | 191 ms: 1.05x faster                                                  |
| regex_compile                    | 78.5 ms                                                | 74.9 ms: 1.05x faster                                                 |
| bpe_tokeniser                    | 3.24 sec                                               | 3.10 sec: 1.05x faster                                                |
| json_dumps                       | 6.56 ms                                                | 6.28 ms: 1.05x faster                                                 |
| raytrace                         | 182 ms                                                 | 174 ms: 1.04x faster                                                  |
| pprint_safe_repr                 | 531 ms                                                 | 511 ms: 1.04x faster                                                  |
| pprint_pformat                   | 1.08 sec                                               | 1.04 sec: 1.04x faster                                                |
| scimark_monte_carlo              | 50.4 ms                                                | 48.6 ms: 1.04x faster                                                 |
| crypto_pyaes                     | 54.0 ms                                                | 52.1 ms: 1.04x faster                                                 |
| pycparser                        | 706 ms                                                 | 681 ms: 1.04x faster                                                  |
| xml_etree_iterparse              | 74.2 ms                                                | 71.9 ms: 1.03x faster                                                 |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 338 ms: 1.03x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 365 ms: 1.03x faster                                                  |
| sqlglot_normalize                | 189 ms                                                 | 184 ms: 1.02x faster                                                  |
| chaos                            | 41.3 ms                                                | 40.4 ms: 1.02x faster                                                 |
| coverage                         | 46.1 ms                                                | 45.2 ms: 1.02x faster                                                 |
| regex_dna                        | 148 ms                                                 | 145 ms: 1.02x faster                                                  |
| regex_v8                         | 16.9 ms                                                | 16.6 ms: 1.02x faster                                                 |
| hexiom                           | 4.85 ms                                                | 4.78 ms: 1.02x faster                                                 |
| gc_traversal                     | 2.48 ms                                                | 2.46 ms: 1.01x faster                                                 |
| python_startup                   | 17.0 ms                                                | 16.8 ms: 1.01x faster                                                 |
| pidigits                         | 284 ms                                                 | 282 ms: 1.01x faster                                                  |
| django_template                  | 22.2 ms                                                | 22.1 ms: 1.00x faster                                                 |
| sympy_str                        | 145 ms                                                 | 145 ms: 1.00x faster                                                  |
| meteor_contest                   | 73.8 ms                                                | 73.8 ms: 1.00x slower                                                 |
| xml_etree_parse                  | 109 ms                                                 | 110 ms: 1.01x slower                                                  |
| telco                            | 4.80 ms                                                | 4.85 ms: 1.01x slower                                                 |
| 2to3                             | 178 ms                                                 | 180 ms: 1.01x slower                                                  |
| sympy_sum                        | 75.6 ms                                                | 76.4 ms: 1.01x slower                                                 |
| dulwich_log                      | 28.7 ms                                                | 29.1 ms: 1.01x slower                                                 |
| bench_mp_pool                    | 50.9 ms                                                | 51.6 ms: 1.01x slower                                                 |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.28 sec: 1.02x slower                                                |
| sympy_expand                     | 246 ms                                                 | 250 ms: 1.02x slower                                                  |
| python_startup_no_site           | 13.7 ms                                                | 13.9 ms: 1.02x slower                                                 |
| sqlglot_transpile                | 1.02 ms                                                | 1.05 ms: 1.02x slower                                                 |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 3.07 ms: 1.03x slower                                                 |
| json_loads                       | 16.9 us                                                | 17.3 us: 1.03x slower                                                 |
| pathlib                          | 22.8 ms                                                | 23.6 ms: 1.04x slower                                                 |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 463 ms: 1.04x slower                                                  |
| sqlglot_optimize                 | 34.9 ms                                                | 36.2 ms: 1.04x slower                                                 |
| mdp                              | 1.50 sec                                               | 1.57 sec: 1.04x slower                                                |
| sympy_integrate                  | 11.3 ms                                                | 11.9 ms: 1.05x slower                                                 |
| comprehensions                   | 12.2 us                                                | 12.8 us: 1.05x slower                                                 |
| async_tree_io_tg                 | 500 ms                                                 | 553 ms: 1.11x slower                                                  |
| docutils                         | 1.44 sec                                               | 1.61 sec: 1.11x slower                                                |
| create_gc_cycles                 | 803 us                                                 | 904 us: 1.13x slower                                                  |
| pylint                           | 181 ms                                                 | 207 ms: 1.14x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 594 ms: 1.17x slower                                                  |
| genshi_xml                       | 34.4 ms                                                | 41.2 ms: 1.20x slower                                                 |
| richards_super                   | 39.1 ms                                                | 49.7 ms: 1.27x slower                                                 |
| async_tree_eager_io              | 513 ms                                                 | 681 ms: 1.33x slower                                                  |
| richards                         | 35.4 ms                                                | 47.7 ms: 1.35x slower                                                 |
| async_tree_eager_io_tg           | 477 ms                                                 | 718 ms: 1.51x slower                                                  |
| asyncio_websockets               | 241 ms                                                 | 409 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (8): asyncio_tcp, genshi_text, async_tree_cpu_io_mixed, sqlglot_parse, async_generators, json, async_tree_none_tg, tornado_http
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 97.77% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x