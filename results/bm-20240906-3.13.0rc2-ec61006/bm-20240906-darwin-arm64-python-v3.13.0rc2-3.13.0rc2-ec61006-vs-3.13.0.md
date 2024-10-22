# Results vs. 3.13.0

- fork: python
- ref: v3.13.0rc2
- machine: darwin-arm64
- commit hash: ec61006
- commit date: 2024-09-06
- overall geometric mean: 1.06x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 162 ms: 1.10x faster                                         |
| chameleon      | 5.08 ms                                                | 4.37 ms: 1.16x faster                                        |
| docutils       | 1.44 sec                                               | 1.47 sec: 1.02x slower                                       |
| html5lib       | 36.6 ms                                                | 31.9 ms: 1.15x faster                                        |
| Geometric mean | (ref)                                                  | 1.05x faster                                                 |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.0 ms: 1.24x faster                                        |
| async_tree_memoization_tg        | 291 ms                                                 | 240 ms: 1.21x faster                                         |
| async_tree_eager_tg              | 48.4 ms                                                | 41.8 ms: 1.16x faster                                        |
| async_tree_eager                 | 70.5 ms                                                | 61.9 ms: 1.14x faster                                        |
| asyncio_tcp                      | 457 ms                                                 | 408 ms: 1.12x faster                                         |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 128 ms: 1.09x faster                                         |
| async_tree_eager_memoization     | 169 ms                                                 | 156 ms: 1.08x faster                                         |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 334 ms: 1.04x faster                                         |
| async_generators                 | 294 ms                                                 | 285 ms: 1.03x faster                                         |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 363 ms: 1.03x faster                                         |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.29 sec: 1.02x slower                                       |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 473 ms: 1.03x slower                                         |
| async_tree_io                    | 507 ms                                                 | 559 ms: 1.10x slower                                         |
| async_tree_io_tg                 | 500 ms                                                 | 557 ms: 1.11x slower                                         |
| async_tree_eager_io              | 513 ms                                                 | 767 ms: 1.50x slower                                         |
| async_tree_eager_io_tg           | 477 ms                                                 | 772 ms: 1.62x slower                                         |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                         |
| Geometric mean                   | (ref)                                                  | 1.03x slower                                                 |

Benchmark hidden because not significant (4): async_tree_memoization, async_tree_none_tg, async_tree_none, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 73.9 ms                                                | 60.6 ms: 1.22x faster                                        |
| float          | 56.2 ms                                                | 48.3 ms: 1.16x faster                                        |
| pidigits       | 284 ms                                                 | 282 ms: 1.00x faster                                         |
| Geometric mean | (ref)                                                  | 1.13x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 68.8 ms: 1.14x faster                                        |
| regex_effbot   | 2.63 ms                                                | 2.61 ms: 1.01x faster                                        |
| regex_dna      | 148 ms                                                 | 149 ms: 1.01x slower                                         |
| regex_v8       | 16.9 ms                                                | 17.4 ms: 1.03x slower                                        |
| Geometric mean | (ref)                                                  | 1.03x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python   | 213 us                                                 | 182 us: 1.17x faster                                         |
| unpickle_pure_python | 163 us                                                 | 142 us: 1.15x faster                                         |
| xml_etree_process    | 40.9 ms                                                | 37.6 ms: 1.09x faster                                        |
| tomli_loads          | 1.56 sec                                               | 1.46 sec: 1.07x faster                                       |
| xml_etree_generate   | 56.6 ms                                                | 53.1 ms: 1.07x faster                                        |
| json_dumps           | 6.56 ms                                                | 6.31 ms: 1.04x faster                                        |
| xml_etree_iterparse  | 74.2 ms                                                | 73.0 ms: 1.02x faster                                        |
| xml_etree_parse      | 109 ms                                                 | 107 ms: 1.01x faster                                         |
| json_loads           | 16.9 us                                                | 16.7 us: 1.01x faster                                        |
| unpickle_list        | 2.93 us                                                | 2.91 us: 1.01x faster                                        |
| unpickle             | 9.15 us                                                | 9.21 us: 1.01x slower                                        |
| pickle_list          | 2.99 us                                                | 3.01 us: 1.01x slower                                        |
| pickle_dict          | 18.2 us                                                | 18.4 us: 1.01x slower                                        |
| pickle               | 7.36 us                                                | 7.70 us: 1.05x slower                                        |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                | 13.7 ms: 1.01x slower                                        |
| python_startup         | 17.0 ms                                                | 17.2 ms: 1.01x slower                                        |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 14.1 ms: 1.20x faster                                        |
| genshi_xml      | 34.4 ms                                                | 30.2 ms: 1.14x faster                                        |
| django_template | 22.2 ms                                                | 19.8 ms: 1.12x faster                                        |
| mako            | 7.68 ms                                                | 7.08 ms: 1.09x faster                                        |
| Geometric mean  | (ref)                                                  | 1.14x faster                                                 |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| generators                       | 31.5 ms                                                | 22.9 ms: 1.37x faster                                        |
| unpack_sequence                  | 36.1 ns                                                | 26.7 ns: 1.35x faster                                        |
| deltablue                        | 2.68 ms                                                | 2.16 ms: 1.24x faster                                        |
| coroutines                       | 19.8 ms                                                | 16.0 ms: 1.24x faster                                        |
| raytrace                         | 182 ms                                                 | 149 ms: 1.22x faster                                         |
| nbody                            | 73.9 ms                                                | 60.6 ms: 1.22x faster                                        |
| async_tree_memoization_tg        | 291 ms                                                 | 240 ms: 1.21x faster                                         |
| chaos                            | 41.3 ms                                                | 34.4 ms: 1.20x faster                                        |
| genshi_text                      | 16.9 ms                                                | 14.1 ms: 1.20x faster                                        |
| nqueens                          | 62.9 ms                                                | 52.9 ms: 1.19x faster                                        |
| deepcopy_memo                    | 27.2 us                                                | 23.0 us: 1.19x faster                                        |
| scimark_monte_carlo              | 50.4 ms                                                | 42.8 ms: 1.18x faster                                        |
| pickle_pure_python               | 213 us                                                 | 182 us: 1.17x faster                                         |
| hexiom                           | 4.85 ms                                                | 4.16 ms: 1.17x faster                                        |
| chameleon                        | 5.08 ms                                                | 4.37 ms: 1.16x faster                                        |
| float                            | 56.2 ms                                                | 48.3 ms: 1.16x faster                                        |
| sqlglot_parse                    | 856 us                                                 | 739 us: 1.16x faster                                         |
| async_tree_eager_tg              | 48.4 ms                                                | 41.8 ms: 1.16x faster                                        |
| spectral_norm                    | 77.3 ms                                                | 67.0 ms: 1.15x faster                                        |
| logging_silent                   | 69.9 ns                                                | 60.7 ns: 1.15x faster                                        |
| unpickle_pure_python             | 163 us                                                 | 142 us: 1.15x faster                                         |
| gunicorn                         | 1.31 ms                                                | 1.14 ms: 1.15x faster                                        |
| html5lib                         | 36.6 ms                                                | 31.9 ms: 1.15x faster                                        |
| comprehensions                   | 12.2 us                                                | 10.6 us: 1.15x faster                                        |
| logging_simple                   | 3.57 us                                                | 3.12 us: 1.14x faster                                        |
| regex_compile                    | 78.5 ms                                                | 68.8 ms: 1.14x faster                                        |
| go                               | 115 ms                                                 | 101 ms: 1.14x faster                                         |
| genshi_xml                       | 34.4 ms                                                | 30.2 ms: 1.14x faster                                        |
| sqlglot_transpile                | 1.02 ms                                                | 899 us: 1.14x faster                                         |
| async_tree_eager                 | 70.5 ms                                                | 61.9 ms: 1.14x faster                                        |
| deepcopy                         | 232 us                                                 | 204 us: 1.14x faster                                         |
| logging_format                   | 3.85 us                                                | 3.39 us: 1.14x faster                                        |
| pprint_safe_repr                 | 531 ms                                                 | 468 ms: 1.13x faster                                         |
| pprint_pformat                   | 1.08 sec                                               | 953 ms: 1.13x faster                                         |
| richards_super                   | 39.1 ms                                                | 34.6 ms: 1.13x faster                                        |
| scimark_lu                       | 76.5 ms                                                | 67.6 ms: 1.13x faster                                        |
| deepcopy_reduce                  | 2.06 us                                                | 1.82 us: 1.13x faster                                        |
| typing_runtime_protocols         | 101 us                                                 | 89.7 us: 1.13x faster                                        |
| richards                         | 35.4 ms                                                | 31.5 ms: 1.13x faster                                        |
| sqlglot_normalize                | 189 ms                                                 | 168 ms: 1.12x faster                                         |
| django_template                  | 22.2 ms                                                | 19.8 ms: 1.12x faster                                        |
| asyncio_tcp                      | 457 ms                                                 | 408 ms: 1.12x faster                                         |
| sqlglot_optimize                 | 34.9 ms                                                | 31.3 ms: 1.12x faster                                        |
| scimark_sor                      | 106 ms                                                 | 95.5 ms: 1.11x faster                                        |
| pycparser                        | 706 ms                                                 | 641 ms: 1.10x faster                                         |
| bench_thread_pool                | 506 us                                                 | 460 us: 1.10x faster                                         |
| fannkuch                         | 282 ms                                                 | 257 ms: 1.10x faster                                         |
| 2to3                             | 178 ms                                                 | 162 ms: 1.10x faster                                         |
| sympy_str                        | 145 ms                                                 | 133 ms: 1.09x faster                                         |
| scimark_fft                      | 201 ms                                                 | 184 ms: 1.09x faster                                         |
| sympy_integrate                  | 11.3 ms                                                | 10.4 ms: 1.09x faster                                        |
| pyflate                          | 351 ms                                                 | 322 ms: 1.09x faster                                         |
| dask                             | 255 ms                                                 | 234 ms: 1.09x faster                                         |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 128 ms: 1.09x faster                                         |
| xml_etree_process                | 40.9 ms                                                | 37.6 ms: 1.09x faster                                        |
| mako                             | 7.68 ms                                                | 7.08 ms: 1.09x faster                                        |
| sympy_sum                        | 75.6 ms                                                | 69.8 ms: 1.08x faster                                        |
| async_tree_eager_memoization     | 169 ms                                                 | 156 ms: 1.08x faster                                         |
| crypto_pyaes                     | 54.0 ms                                                | 49.9 ms: 1.08x faster                                        |
| sympy_expand                     | 246 ms                                                 | 228 ms: 1.08x faster                                         |
| tomli_loads                      | 1.56 sec                                               | 1.46 sec: 1.07x faster                                       |
| thrift                           | 466 us                                                 | 435 us: 1.07x faster                                         |
| xml_etree_generate               | 56.6 ms                                                | 53.1 ms: 1.07x faster                                        |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.81 ms: 1.06x faster                                        |
| bpe_tokeniser                    | 3.24 sec                                               | 3.07 sec: 1.06x faster                                       |
| mdp                              | 1.50 sec                                               | 1.42 sec: 1.06x faster                                       |
| dulwich_log                      | 28.7 ms                                                | 27.3 ms: 1.05x faster                                        |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 334 ms: 1.04x faster                                         |
| json_dumps                       | 6.56 ms                                                | 6.31 ms: 1.04x faster                                        |
| bench_mp_pool                    | 50.9 ms                                                | 49.0 ms: 1.04x faster                                        |
| async_generators                 | 294 ms                                                 | 285 ms: 1.03x faster                                         |
| coverage                         | 46.1 ms                                                | 44.7 ms: 1.03x faster                                        |
| meteor_contest                   | 73.8 ms                                                | 71.6 ms: 1.03x faster                                        |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 363 ms: 1.03x faster                                         |
| telco                            | 4.80 ms                                                | 4.69 ms: 1.02x faster                                        |
| xml_etree_iterparse              | 74.2 ms                                                | 73.0 ms: 1.02x faster                                        |
| xml_etree_parse                  | 109 ms                                                 | 107 ms: 1.01x faster                                         |
| gc_traversal                     | 2.48 ms                                                | 2.46 ms: 1.01x faster                                        |
| json_loads                       | 16.9 us                                                | 16.7 us: 1.01x faster                                        |
| regex_effbot                     | 2.63 ms                                                | 2.61 ms: 1.01x faster                                        |
| unpickle_list                    | 2.93 us                                                | 2.91 us: 1.01x faster                                        |
| pidigits                         | 284 ms                                                 | 282 ms: 1.00x faster                                         |
| python_startup_no_site           | 13.7 ms                                                | 13.7 ms: 1.01x slower                                        |
| unpickle                         | 9.15 us                                                | 9.21 us: 1.01x slower                                        |
| pickle_list                      | 2.99 us                                                | 3.01 us: 1.01x slower                                        |
| python_startup                   | 17.0 ms                                                | 17.2 ms: 1.01x slower                                        |
| regex_dna                        | 148 ms                                                 | 149 ms: 1.01x slower                                         |
| pickle_dict                      | 18.2 us                                                | 18.4 us: 1.01x slower                                        |
| docutils                         | 1.44 sec                                               | 1.47 sec: 1.02x slower                                       |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.29 sec: 1.02x slower                                       |
| regex_v8                         | 16.9 ms                                                | 17.4 ms: 1.03x slower                                        |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 473 ms: 1.03x slower                                         |
| pickle                           | 7.36 us                                                | 7.70 us: 1.05x slower                                        |
| pathlib                          | 22.8 ms                                                | 24.6 ms: 1.08x slower                                        |
| async_tree_io                    | 507 ms                                                 | 559 ms: 1.10x slower                                         |
| async_tree_io_tg                 | 500 ms                                                 | 557 ms: 1.11x slower                                         |
| create_gc_cycles                 | 803 us                                                 | 898 us: 1.12x slower                                         |
| mypy2                            | 396 ms                                                 | 479 ms: 1.21x slower                                         |
| flaskblogging                    | 2.89 ms                                                | 3.96 ms: 1.37x slower                                        |
| async_tree_eager_io              | 513 ms                                                 | 767 ms: 1.50x slower                                         |
| async_tree_eager_io_tg           | 477 ms                                                 | 772 ms: 1.62x slower                                         |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                         |
| Geometric mean                   | (ref)                                                  | 1.06x faster                                                 |

Benchmark hidden because not significant (9): aiohttp, async_tree_memoization, pylint, async_tree_none_tg, sqlite_synth, json, async_tree_none, async_tree_cpu_io_mixed_tg, tornado_http

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 0.99x