# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0
- machine: darwin-arm64
- commit hash: 60403a5
- commit date: 2024-10-07
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: 0.43x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 178 ms: 1.10x slower                                   |
| chameleon      | 4.27 ms                                                    | 5.08 ms: 1.19x slower                                  |
| docutils       | 1.44 sec                                                   | 1.44 sec: 1.01x slower                                 |
| html5lib       | 31.2 ms                                                    | 36.6 ms: 1.18x slower                                  |
| Geometric mean | (ref)                                                      | 1.12x slower                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|----------------------------------|:----------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_eager_io_tg           | 768 ms                                                     | 477 ms: 1.61x faster                                   |
| async_tree_eager_io              | 766 ms                                                     | 513 ms: 1.49x faster                                   |
| async_tree_io_tg                 | 565 ms                                                     | 500 ms: 1.13x faster                                   |
| async_tree_io                    | 563 ms                                                     | 507 ms: 1.11x faster                                   |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 460 ms: 1.02x faster                                   |
| async_tree_memoization           | 260 ms                                                     | 270 ms: 1.04x slower                                   |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 375 ms: 1.05x slower                                   |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 348 ms: 1.05x slower                                   |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 139 ms: 1.11x slower                                   |
| async_tree_eager_memoization     | 152 ms                                                     | 169 ms: 1.11x slower                                   |
| async_tree_eager                 | 60.3 ms                                                    | 70.5 ms: 1.17x slower                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 48.4 ms: 1.17x slower                                  |
| async_tree_memoization_tg        | 240 ms                                                     | 291 ms: 1.21x slower                                   |
| Geometric mean                   | (ref)                                                      | 1.02x faster                                           |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------:|
| pidigits       | 282 ms                                                     | 284 ms: 1.01x slower                                   |
| float          | 48.6 ms                                                    | 56.2 ms: 1.16x slower                                  |
| nbody          | 59.6 ms                                                    | 73.9 ms: 1.24x slower                                  |
| Geometric mean | (ref)                                                      | 1.13x slower                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------:|
| regex_v8       | 17.3 ms                                                    | 16.9 ms: 1.02x faster                                  |
| regex_dna      | 149 ms                                                     | 148 ms: 1.01x faster                                   |
| regex_effbot   | 2.58 ms                                                    | 2.63 ms: 1.02x slower                                  |
| regex_compile  | 68.5 ms                                                    | 78.5 ms: 1.15x slower                                  |
| Geometric mean | (ref)                                                      | 1.03x slower                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|----------------------|:----------------------------------------------------------:|:------------------------------------------------------:|
| pickle               | 7.48 us                                                    | 7.36 us: 1.02x faster                                  |
| pickle_dict          | 18.3 us                                                    | 18.2 us: 1.01x faster                                  |
| pickle_list          | 2.96 us                                                    | 2.99 us: 1.01x slower                                  |
| unpickle_list        | 2.88 us                                                    | 2.93 us: 1.02x slower                                  |
| xml_etree_parse      | 106 ms                                                     | 109 ms: 1.03x slower                                   |
| xml_etree_iterparse  | 71.5 ms                                                    | 74.2 ms: 1.04x slower                                  |
| json_dumps           | 6.23 ms                                                    | 6.56 ms: 1.05x slower                                  |
| tomli_loads          | 1.47 sec                                                   | 1.56 sec: 1.06x slower                                 |
| xml_etree_generate   | 52.7 ms                                                    | 56.6 ms: 1.07x slower                                  |
| xml_etree_process    | 37.1 ms                                                    | 40.9 ms: 1.10x slower                                  |
| unpickle_pure_python | 141 us                                                     | 163 us: 1.16x slower                                   |
| pickle_pure_python   | 179 us                                                     | 213 us: 1.19x slower                                   |
| Geometric mean       | (ref)                                                      | 1.05x slower                                           |

Benchmark hidden because not significant (2): json_loads, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|------------------------|:----------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 12.3 ms                                                    | 13.7 ms: 1.11x slower                                  |
| python_startup         | 15.2 ms                                                    | 17.0 ms: 1.12x slower                                  |
| Geometric mean         | (ref)                                                      | 1.12x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|-----------------|:----------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 7.68 ms: 1.10x slower                                  |
| django_template | 19.4 ms                                                    | 22.2 ms: 1.14x slower                                  |
| genshi_xml      | 29.9 ms                                                    | 34.4 ms: 1.15x slower                                  |
| genshi_text     | 13.9 ms                                                    | 16.9 ms: 1.21x slower                                  |
| Geometric mean  | (ref)                                                      | 1.15x slower                                           |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|----------------------------------|:----------------------------------------------------------:|:------------------------------------------------------:|
| asyncio_websockets               | 409 ms                                                     | 241 ms: 1.69x faster                                   |
| async_tree_eager_io_tg           | 768 ms                                                     | 477 ms: 1.61x faster                                   |
| async_tree_eager_io              | 766 ms                                                     | 513 ms: 1.49x faster                                   |
| flaskblogging                    | 3.61 ms                                                    | 2.89 ms: 1.25x faster                                  |
| async_tree_io_tg                 | 565 ms                                                     | 500 ms: 1.13x faster                                   |
| create_gc_cycles                 | 897 us                                                     | 803 us: 1.12x faster                                   |
| async_tree_io                    | 563 ms                                                     | 507 ms: 1.11x faster                                   |
| pathlib                          | 23.3 ms                                                    | 22.8 ms: 1.02x faster                                  |
| mdp                              | 1.53 sec                                                   | 1.50 sec: 1.02x faster                                 |
| asyncio_tcp_ssl                  | 1.29 sec                                                   | 1.26 sec: 1.02x faster                                 |
| regex_v8                         | 17.3 ms                                                    | 16.9 ms: 1.02x faster                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 460 ms: 1.02x faster                                   |
| pickle                           | 7.48 us                                                    | 7.36 us: 1.02x faster                                  |
| regex_dna                        | 149 ms                                                     | 148 ms: 1.01x faster                                   |
| pickle_dict                      | 18.3 us                                                    | 18.2 us: 1.01x faster                                  |
| sqlite_synth                     | 1.55 us                                                    | 1.54 us: 1.00x faster                                  |
| docutils                         | 1.44 sec                                                   | 1.44 sec: 1.01x slower                                 |
| pidigits                         | 282 ms                                                     | 284 ms: 1.01x slower                                   |
| pickle_list                      | 2.96 us                                                    | 2.99 us: 1.01x slower                                  |
| gc_traversal                     | 2.45 ms                                                    | 2.48 ms: 1.01x slower                                  |
| unpickle_list                    | 2.88 us                                                    | 2.93 us: 1.02x slower                                  |
| regex_effbot                     | 2.58 ms                                                    | 2.63 ms: 1.02x slower                                  |
| coverage                         | 45.0 ms                                                    | 46.1 ms: 1.02x slower                                  |
| xml_etree_parse                  | 106 ms                                                     | 109 ms: 1.03x slower                                   |
| xml_etree_iterparse              | 71.5 ms                                                    | 74.2 ms: 1.04x slower                                  |
| async_tree_memoization           | 260 ms                                                     | 270 ms: 1.04x slower                                   |
| dulwich_log                      | 27.6 ms                                                    | 28.7 ms: 1.04x slower                                  |
| mypy2                            | 379 ms                                                     | 396 ms: 1.04x slower                                   |
| telco                            | 4.60 ms                                                    | 4.80 ms: 1.04x slower                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 375 ms: 1.05x slower                                   |
| async_generators                 | 281 ms                                                     | 294 ms: 1.05x slower                                   |
| meteor_contest                   | 70.3 ms                                                    | 73.8 ms: 1.05x slower                                  |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 348 ms: 1.05x slower                                   |
| json_dumps                       | 6.23 ms                                                    | 6.56 ms: 1.05x slower                                  |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.24 sec: 1.06x slower                                 |
| tomli_loads                      | 1.47 sec                                                   | 1.56 sec: 1.06x slower                                 |
| thrift                           | 435 us                                                     | 466 us: 1.07x slower                                   |
| xml_etree_generate               | 52.7 ms                                                    | 56.6 ms: 1.07x slower                                  |
| bench_mp_pool                    | 47.2 ms                                                    | 50.9 ms: 1.08x slower                                  |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.99 ms: 1.08x slower                                  |
| sympy_expand                     | 226 ms                                                     | 246 ms: 1.09x slower                                   |
| crypto_pyaes                     | 49.5 ms                                                    | 54.0 ms: 1.09x slower                                  |
| sympy_sum                        | 69.2 ms                                                    | 75.6 ms: 1.09x slower                                  |
| pyflate                          | 321 ms                                                     | 351 ms: 1.09x slower                                   |
| sympy_integrate                  | 10.3 ms                                                    | 11.3 ms: 1.10x slower                                  |
| mako                             | 6.99 ms                                                    | 7.68 ms: 1.10x slower                                  |
| xml_etree_process                | 37.1 ms                                                    | 40.9 ms: 1.10x slower                                  |
| 2to3                             | 161 ms                                                     | 178 ms: 1.10x slower                                   |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 139 ms: 1.11x slower                                   |
| sympy_str                        | 131 ms                                                     | 145 ms: 1.11x slower                                   |
| python_startup_no_site           | 12.3 ms                                                    | 13.7 ms: 1.11x slower                                  |
| async_tree_eager_memoization     | 152 ms                                                     | 169 ms: 1.11x slower                                   |
| scimark_fft                      | 181 ms                                                     | 201 ms: 1.11x slower                                   |
| richards_super                   | 35.2 ms                                                    | 39.1 ms: 1.11x slower                                  |
| richards                         | 31.8 ms                                                    | 35.4 ms: 1.11x slower                                  |
| scimark_sor                      | 94.9 ms                                                    | 106 ms: 1.11x slower                                   |
| pycparser                        | 632 ms                                                     | 706 ms: 1.12x slower                                   |
| python_startup                   | 15.2 ms                                                    | 17.0 ms: 1.12x slower                                  |
| sqlglot_optimize                 | 30.9 ms                                                    | 34.9 ms: 1.13x slower                                  |
| deepcopy_reduce                  | 1.82 us                                                    | 2.06 us: 1.13x slower                                  |
| bench_thread_pool                | 447 us                                                     | 506 us: 1.13x slower                                   |
| fannkuch                         | 248 ms                                                     | 282 ms: 1.13x slower                                   |
| asyncio_tcp                      | 402 ms                                                     | 457 ms: 1.14x slower                                   |
| sqlglot_normalize                | 166 ms                                                     | 189 ms: 1.14x slower                                   |
| deepcopy                         | 204 us                                                     | 232 us: 1.14x slower                                   |
| pprint_pformat                   | 947 ms                                                     | 1.08 sec: 1.14x slower                                 |
| pprint_safe_repr                 | 465 ms                                                     | 531 ms: 1.14x slower                                   |
| go                               | 101 ms                                                     | 115 ms: 1.14x slower                                   |
| django_template                  | 19.4 ms                                                    | 22.2 ms: 1.14x slower                                  |
| scimark_lu                       | 66.9 ms                                                    | 76.5 ms: 1.14x slower                                  |
| regex_compile                    | 68.5 ms                                                    | 78.5 ms: 1.15x slower                                  |
| genshi_xml                       | 29.9 ms                                                    | 34.4 ms: 1.15x slower                                  |
| sqlglot_transpile                | 891 us                                                     | 1.02 ms: 1.15x slower                                  |
| dask                             | 221 ms                                                     | 255 ms: 1.15x slower                                   |
| typing_runtime_protocols         | 87.6 us                                                    | 101 us: 1.15x slower                                   |
| float                            | 48.6 ms                                                    | 56.2 ms: 1.16x slower                                  |
| unpickle_pure_python             | 141 us                                                     | 163 us: 1.16x slower                                   |
| logging_silent                   | 60.1 ns                                                    | 69.9 ns: 1.16x slower                                  |
| spectral_norm                    | 66.4 ms                                                    | 77.3 ms: 1.16x slower                                  |
| logging_format                   | 3.31 us                                                    | 3.85 us: 1.16x slower                                  |
| async_tree_eager                 | 60.3 ms                                                    | 70.5 ms: 1.17x slower                                  |
| sqlglot_parse                    | 732 us                                                     | 856 us: 1.17x slower                                   |
| async_tree_eager_tg              | 41.4 ms                                                    | 48.4 ms: 1.17x slower                                  |
| logging_simple                   | 3.04 us                                                    | 3.57 us: 1.17x slower                                  |
| html5lib                         | 31.2 ms                                                    | 36.6 ms: 1.18x slower                                  |
| scimark_monte_carlo              | 42.5 ms                                                    | 50.4 ms: 1.19x slower                                  |
| chameleon                        | 4.27 ms                                                    | 5.08 ms: 1.19x slower                                  |
| pickle_pure_python               | 179 us                                                     | 213 us: 1.19x slower                                   |
| hexiom                           | 4.06 ms                                                    | 4.85 ms: 1.20x slower                                  |
| comprehensions                   | 10.2 us                                                    | 12.2 us: 1.20x slower                                  |
| nqueens                          | 52.2 ms                                                    | 62.9 ms: 1.20x slower                                  |
| deepcopy_memo                    | 22.6 us                                                    | 27.2 us: 1.20x slower                                  |
| genshi_text                      | 13.9 ms                                                    | 16.9 ms: 1.21x slower                                  |
| chaos                            | 34.0 ms                                                    | 41.3 ms: 1.21x slower                                  |
| async_tree_memoization_tg        | 240 ms                                                     | 291 ms: 1.21x slower                                   |
| raytrace                         | 147 ms                                                     | 182 ms: 1.24x slower                                   |
| nbody                            | 59.6 ms                                                    | 73.9 ms: 1.24x slower                                  |
| coroutines                       | 15.8 ms                                                    | 19.8 ms: 1.25x slower                                  |
| deltablue                        | 2.14 ms                                                    | 2.68 ms: 1.25x slower                                  |
| aiohttp                          | 997 us                                                     | 1.26 ms: 1.26x slower                                  |
| gunicorn                         | 1.04 ms                                                    | 1.31 ms: 1.27x slower                                  |
| generators                       | 22.9 ms                                                    | 31.5 ms: 1.38x slower                                  |
| Geometric mean                   | (ref)                                                      | 1.08x slower                                           |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed_tg, json_loads, unpickle, json, async_tree_none_tg, async_tree_none, pylint, tornado_http
Ignored benchmarks (1) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: 0.43x