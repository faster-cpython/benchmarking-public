# Results vs. 3.13.0

- fork: python
- ref: v3.13.0rc1
- machine: darwin-arm64
- commit hash: e4a3e78
- commit date: 2024-07-31
- overall geometric mean: 1.07x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 160 ms: 1.11x faster                                         |
| chameleon      | 5.08 ms                                                | 4.36 ms: 1.16x faster                                        |
| docutils       | 1.44 sec                                               | 1.45 sec: 1.01x slower                                       |
| html5lib       | 36.6 ms                                                | 31.7 ms: 1.16x faster                                        |
| Geometric mean | (ref)                                                  | 1.11x faster                                                 |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.0 ms: 1.24x faster                                        |
| async_tree_memoization_tg        | 291 ms                                                 | 240 ms: 1.21x faster                                         |
| async_tree_eager_tg              | 48.4 ms                                                | 41.7 ms: 1.16x faster                                        |
| async_tree_eager                 | 70.5 ms                                                | 61.5 ms: 1.15x faster                                        |
| asyncio_tcp                      | 457 ms                                                 | 414 ms: 1.10x faster                                         |
| async_tree_eager_memoization     | 169 ms                                                 | 153 ms: 1.10x faster                                         |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 126 ms: 1.10x faster                                         |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 332 ms: 1.05x faster                                         |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 360 ms: 1.04x faster                                         |
| async_generators                 | 294 ms                                                 | 283 ms: 1.04x faster                                         |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 468 ms: 1.02x slower                                         |
| async_tree_io                    | 507 ms                                                 | 555 ms: 1.10x slower                                         |
| async_tree_io_tg                 | 500 ms                                                 | 564 ms: 1.13x slower                                         |
| async_tree_eager_io              | 513 ms                                                 | 763 ms: 1.49x slower                                         |
| async_tree_eager_io_tg           | 477 ms                                                 | 762 ms: 1.60x slower                                         |
| asyncio_websockets               | 241 ms                                                 | 409 ms: 1.69x slower                                         |
| Geometric mean                   | (ref)                                                  | 1.02x slower                                                 |

Benchmark hidden because not significant (5): async_tree_memoization, async_tree_none, async_tree_none_tg, asyncio_tcp_ssl, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 73.9 ms                                                | 60.6 ms: 1.22x faster                                        |
| float          | 56.2 ms                                                | 48.5 ms: 1.16x faster                                        |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                         |
| Geometric mean | (ref)                                                  | 1.12x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 69.3 ms: 1.13x faster                                        |
| regex_effbot   | 2.63 ms                                                | 2.59 ms: 1.01x faster                                        |
| regex_v8       | 16.9 ms                                                | 17.3 ms: 1.02x slower                                        |
| regex_dna      | 148 ms                                                 | 151 ms: 1.02x slower                                         |
| Geometric mean | (ref)                                                  | 1.02x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python   | 213 us                                                 | 182 us: 1.17x faster                                         |
| unpickle_pure_python | 163 us                                                 | 143 us: 1.14x faster                                         |
| xml_etree_process    | 40.9 ms                                                | 38.0 ms: 1.07x faster                                        |
| tomli_loads          | 1.56 sec                                               | 1.46 sec: 1.07x faster                                       |
| xml_etree_generate   | 56.6 ms                                                | 53.2 ms: 1.06x faster                                        |
| json_dumps           | 6.56 ms                                                | 6.22 ms: 1.05x faster                                        |
| xml_etree_iterparse  | 74.2 ms                                                | 72.0 ms: 1.03x faster                                        |
| xml_etree_parse      | 109 ms                                                 | 106 ms: 1.03x faster                                         |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                 |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 17.0 ms                                                | 15.4 ms: 1.11x faster                                        |
| python_startup_no_site | 13.7 ms                                                | 12.7 ms: 1.08x faster                                        |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 14.0 ms: 1.21x faster                                        |
| genshi_xml      | 34.4 ms                                                | 30.1 ms: 1.14x faster                                        |
| django_template | 22.2 ms                                                | 20.0 ms: 1.11x faster                                        |
| mako            | 7.68 ms                                                | 7.23 ms: 1.06x faster                                        |
| Geometric mean  | (ref)                                                  | 1.13x faster                                                 |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| generators                       | 31.5 ms                                                | 22.9 ms: 1.38x faster                                        |
| deltablue                        | 2.68 ms                                                | 2.15 ms: 1.25x faster                                        |
| coroutines                       | 19.8 ms                                                | 16.0 ms: 1.24x faster                                        |
| raytrace                         | 182 ms                                                 | 148 ms: 1.22x faster                                         |
| nbody                            | 73.9 ms                                                | 60.6 ms: 1.22x faster                                        |
| async_tree_memoization_tg        | 291 ms                                                 | 240 ms: 1.21x faster                                         |
| genshi_text                      | 16.9 ms                                                | 14.0 ms: 1.21x faster                                        |
| chaos                            | 41.3 ms                                                | 34.5 ms: 1.20x faster                                        |
| hexiom                           | 4.85 ms                                                | 4.10 ms: 1.18x faster                                        |
| nqueens                          | 62.9 ms                                                | 53.3 ms: 1.18x faster                                        |
| scimark_monte_carlo              | 50.4 ms                                                | 42.9 ms: 1.18x faster                                        |
| deepcopy_memo                    | 27.2 us                                                | 23.2 us: 1.17x faster                                        |
| pickle_pure_python               | 213 us                                                 | 182 us: 1.17x faster                                         |
| chameleon                        | 5.08 ms                                                | 4.36 ms: 1.16x faster                                        |
| async_tree_eager_tg              | 48.4 ms                                                | 41.7 ms: 1.16x faster                                        |
| float                            | 56.2 ms                                                | 48.5 ms: 1.16x faster                                        |
| dask                             | 255 ms                                                 | 220 ms: 1.16x faster                                         |
| sqlglot_parse                    | 856 us                                                 | 741 us: 1.16x faster                                         |
| html5lib                         | 36.6 ms                                                | 31.7 ms: 1.16x faster                                        |
| logging_simple                   | 3.57 us                                                | 3.10 us: 1.15x faster                                        |
| logging_format                   | 3.85 us                                                | 3.35 us: 1.15x faster                                        |
| logging_silent                   | 69.9 ns                                                | 60.9 ns: 1.15x faster                                        |
| comprehensions                   | 12.2 us                                                | 10.6 us: 1.15x faster                                        |
| spectral_norm                    | 77.3 ms                                                | 67.4 ms: 1.15x faster                                        |
| async_tree_eager                 | 70.5 ms                                                | 61.5 ms: 1.15x faster                                        |
| genshi_xml                       | 34.4 ms                                                | 30.1 ms: 1.14x faster                                        |
| unpickle_pure_python             | 163 us                                                 | 143 us: 1.14x faster                                         |
| typing_runtime_protocols         | 101 us                                                 | 88.5 us: 1.14x faster                                        |
| go                               | 115 ms                                                 | 101 ms: 1.14x faster                                         |
| regex_compile                    | 78.5 ms                                                | 69.3 ms: 1.13x faster                                        |
| sqlglot_transpile                | 1.02 ms                                                | 904 us: 1.13x faster                                         |
| pprint_pformat                   | 1.08 sec                                               | 953 ms: 1.13x faster                                         |
| deepcopy                         | 232 us                                                 | 205 us: 1.13x faster                                         |
| pprint_safe_repr                 | 531 ms                                                 | 469 ms: 1.13x faster                                         |
| richards_super                   | 39.1 ms                                                | 34.7 ms: 1.13x faster                                        |
| sqlglot_normalize                | 189 ms                                                 | 167 ms: 1.13x faster                                         |
| scimark_lu                       | 76.5 ms                                                | 67.9 ms: 1.13x faster                                        |
| deepcopy_reduce                  | 2.06 us                                                | 1.83 us: 1.12x faster                                        |
| richards                         | 35.4 ms                                                | 31.6 ms: 1.12x faster                                        |
| sqlglot_optimize                 | 34.9 ms                                                | 31.3 ms: 1.12x faster                                        |
| django_template                  | 22.2 ms                                                | 20.0 ms: 1.11x faster                                        |
| fannkuch                         | 282 ms                                                 | 254 ms: 1.11x faster                                         |
| scimark_sor                      | 106 ms                                                 | 95.2 ms: 1.11x faster                                        |
| 2to3                             | 178 ms                                                 | 160 ms: 1.11x faster                                         |
| python_startup                   | 17.0 ms                                                | 15.4 ms: 1.11x faster                                        |
| pycparser                        | 706 ms                                                 | 638 ms: 1.11x faster                                         |
| asyncio_tcp                      | 457 ms                                                 | 414 ms: 1.10x faster                                         |
| async_tree_eager_memoization     | 169 ms                                                 | 153 ms: 1.10x faster                                         |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 126 ms: 1.10x faster                                         |
| sympy_str                        | 145 ms                                                 | 133 ms: 1.10x faster                                         |
| pyflate                          | 351 ms                                                 | 321 ms: 1.09x faster                                         |
| bench_thread_pool                | 506 us                                                 | 463 us: 1.09x faster                                         |
| scimark_fft                      | 201 ms                                                 | 184 ms: 1.09x faster                                         |
| sympy_integrate                  | 11.3 ms                                                | 10.4 ms: 1.09x faster                                        |
| sympy_expand                     | 246 ms                                                 | 228 ms: 1.08x faster                                         |
| crypto_pyaes                     | 54.0 ms                                                | 50.0 ms: 1.08x faster                                        |
| python_startup_no_site           | 13.7 ms                                                | 12.7 ms: 1.08x faster                                        |
| sympy_sum                        | 75.6 ms                                                | 70.2 ms: 1.08x faster                                        |
| xml_etree_process                | 40.9 ms                                                | 38.0 ms: 1.07x faster                                        |
| thrift                           | 466 us                                                 | 435 us: 1.07x faster                                         |
| tomli_loads                      | 1.56 sec                                               | 1.46 sec: 1.07x faster                                       |
| xml_etree_generate               | 56.6 ms                                                | 53.2 ms: 1.06x faster                                        |
| mako                             | 7.68 ms                                                | 7.23 ms: 1.06x faster                                        |
| bench_mp_pool                    | 50.9 ms                                                | 47.9 ms: 1.06x faster                                        |
| bpe_tokeniser                    | 3.24 sec                                               | 3.06 sec: 1.06x faster                                       |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.84 ms: 1.05x faster                                        |
| json_dumps                       | 6.56 ms                                                | 6.22 ms: 1.05x faster                                        |
| dulwich_log                      | 28.7 ms                                                | 27.3 ms: 1.05x faster                                        |
| mdp                              | 1.50 sec                                               | 1.43 sec: 1.05x faster                                       |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 332 ms: 1.05x faster                                         |
| meteor_contest                   | 73.8 ms                                                | 70.4 ms: 1.05x faster                                        |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 360 ms: 1.04x faster                                         |
| async_generators                 | 294 ms                                                 | 283 ms: 1.04x faster                                         |
| telco                            | 4.80 ms                                                | 4.64 ms: 1.04x faster                                        |
| xml_etree_iterparse              | 74.2 ms                                                | 72.0 ms: 1.03x faster                                        |
| xml_etree_parse                  | 109 ms                                                 | 106 ms: 1.03x faster                                         |
| coverage                         | 46.1 ms                                                | 45.0 ms: 1.02x faster                                        |
| json                             | 2.94 ms                                                | 2.90 ms: 1.01x faster                                        |
| regex_effbot                     | 2.63 ms                                                | 2.59 ms: 1.01x faster                                        |
| gc_traversal                     | 2.48 ms                                                | 2.46 ms: 1.01x faster                                        |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                         |
| docutils                         | 1.44 sec                                               | 1.45 sec: 1.01x slower                                       |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 468 ms: 1.02x slower                                         |
| regex_v8                         | 16.9 ms                                                | 17.3 ms: 1.02x slower                                        |
| regex_dna                        | 148 ms                                                 | 151 ms: 1.02x slower                                         |
| pathlib                          | 22.8 ms                                                | 23.8 ms: 1.04x slower                                        |
| async_tree_io                    | 507 ms                                                 | 555 ms: 1.10x slower                                         |
| create_gc_cycles                 | 803 us                                                 | 880 us: 1.10x slower                                         |
| async_tree_io_tg                 | 500 ms                                                 | 564 ms: 1.13x slower                                         |
| mypy2                            | 396 ms                                                 | 455 ms: 1.15x slower                                         |
| async_tree_eager_io              | 513 ms                                                 | 763 ms: 1.49x slower                                         |
| async_tree_eager_io_tg           | 477 ms                                                 | 762 ms: 1.60x slower                                         |
| asyncio_websockets               | 241 ms                                                 | 409 ms: 1.69x slower                                         |
| Geometric mean                   | (ref)                                                  | 1.07x faster                                                 |

Benchmark hidden because not significant (8): tornado_http, async_tree_memoization, pylint, async_tree_none, async_tree_none_tg, json_loads, asyncio_tcp_ssl, async_tree_cpu_io_mixed_tg
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 0.98x