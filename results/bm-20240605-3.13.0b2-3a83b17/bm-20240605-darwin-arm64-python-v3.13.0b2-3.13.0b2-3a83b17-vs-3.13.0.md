# Results vs. 3.13.0

- fork: python
- ref: v3.13.0b2
- machine: darwin-arm64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 6.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 161 ms: 1.10x faster                                       |
| chameleon      | 5.08 ms                                                | 4.27 ms: 1.19x faster                                      |
| docutils       | 1.44 sec                                               | 1.44 sec: 1.01x faster                                     |
| html5lib       | 36.6 ms                                                | 31.2 ms: 1.18x faster                                      |
| Geometric mean | (ref)                                                  | 1.12x faster                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 15.8 ms: 1.25x faster                                      |
| async_tree_memoization_tg        | 291 ms                                                 | 240 ms: 1.21x faster                                       |
| async_tree_eager_tg              | 48.4 ms                                                | 41.4 ms: 1.17x faster                                      |
| async_tree_eager                 | 70.5 ms                                                | 60.3 ms: 1.17x faster                                      |
| asyncio_tcp                      | 457 ms                                                 | 402 ms: 1.14x faster                                       |
| async_tree_eager_memoization     | 169 ms                                                 | 152 ms: 1.11x faster                                       |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 126 ms: 1.11x faster                                       |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 331 ms: 1.05x faster                                       |
| async_generators                 | 294 ms                                                 | 281 ms: 1.05x faster                                       |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 358 ms: 1.05x faster                                       |
| async_tree_memoization           | 270 ms                                                 | 260 ms: 1.04x faster                                       |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 467 ms: 1.02x slower                                       |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.29 sec: 1.02x slower                                     |
| async_tree_io                    | 507 ms                                                 | 563 ms: 1.11x slower                                       |
| async_tree_io_tg                 | 500 ms                                                 | 565 ms: 1.13x slower                                       |
| async_tree_eager_io              | 513 ms                                                 | 766 ms: 1.49x slower                                       |
| async_tree_eager_io_tg           | 477 ms                                                 | 768 ms: 1.61x slower                                       |
| asyncio_websockets               | 241 ms                                                 | 409 ms: 1.69x slower                                       |
| Geometric mean                   | (ref)                                                  | 1.02x slower                                               |

Benchmark hidden because not significant (3): async_tree_none, async_tree_none_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 73.9 ms                                                | 59.6 ms: 1.24x faster                                      |
| float          | 56.2 ms                                                | 48.6 ms: 1.16x faster                                      |
| pidigits       | 284 ms                                                 | 282 ms: 1.01x faster                                       |
| Geometric mean | (ref)                                                  | 1.13x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 68.5 ms: 1.15x faster                                      |
| regex_effbot   | 2.63 ms                                                | 2.58 ms: 1.02x faster                                      |
| regex_dna      | 148 ms                                                 | 149 ms: 1.01x slower                                       |
| regex_v8       | 16.9 ms                                                | 17.3 ms: 1.02x slower                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 213 us                                                 | 179 us: 1.19x faster                                       |
| unpickle_pure_python | 163 us                                                 | 141 us: 1.16x faster                                       |
| xml_etree_process    | 40.9 ms                                                | 37.1 ms: 1.10x faster                                      |
| xml_etree_generate   | 56.6 ms                                                | 52.7 ms: 1.07x faster                                      |
| tomli_loads          | 1.56 sec                                               | 1.47 sec: 1.06x faster                                     |
| json_dumps           | 6.56 ms                                                | 6.23 ms: 1.05x faster                                      |
| xml_etree_iterparse  | 74.2 ms                                                | 71.5 ms: 1.04x faster                                      |
| xml_etree_parse      | 109 ms                                                 | 106 ms: 1.03x faster                                       |
| unpickle_list        | 2.93 us                                                | 2.88 us: 1.02x faster                                      |
| pickle_list          | 2.99 us                                                | 2.96 us: 1.01x faster                                      |
| pickle_dict          | 18.2 us                                                | 18.3 us: 1.01x slower                                      |
| pickle               | 7.36 us                                                | 7.48 us: 1.02x slower                                      |
| Geometric mean       | (ref)                                                  | 1.05x faster                                               |

Benchmark hidden because not significant (2): unpickle, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 17.0 ms                                                | 15.2 ms: 1.12x faster                                      |
| python_startup_no_site | 13.7 ms                                                | 12.3 ms: 1.11x faster                                      |
| Geometric mean         | (ref)                                                  | 1.12x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 13.9 ms: 1.21x faster                                      |
| genshi_xml      | 34.4 ms                                                | 29.9 ms: 1.15x faster                                      |
| django_template | 22.2 ms                                                | 19.4 ms: 1.14x faster                                      |
| mako            | 7.68 ms                                                | 6.99 ms: 1.10x faster                                      |
| Geometric mean  | (ref)                                                  | 1.15x faster                                               |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| generators                       | 31.5 ms                                                | 22.9 ms: 1.38x faster                                      |
| gunicorn                         | 1.31 ms                                                | 1.04 ms: 1.27x faster                                      |
| aiohttp                          | 1.26 ms                                                | 997 us: 1.26x faster                                       |
| deltablue                        | 2.68 ms                                                | 2.14 ms: 1.25x faster                                      |
| coroutines                       | 19.8 ms                                                | 15.8 ms: 1.25x faster                                      |
| nbody                            | 73.9 ms                                                | 59.6 ms: 1.24x faster                                      |
| raytrace                         | 182 ms                                                 | 147 ms: 1.24x faster                                       |
| async_tree_memoization_tg        | 291 ms                                                 | 240 ms: 1.21x faster                                       |
| chaos                            | 41.3 ms                                                | 34.0 ms: 1.21x faster                                      |
| genshi_text                      | 16.9 ms                                                | 13.9 ms: 1.21x faster                                      |
| deepcopy_memo                    | 27.2 us                                                | 22.6 us: 1.20x faster                                      |
| nqueens                          | 62.9 ms                                                | 52.2 ms: 1.20x faster                                      |
| comprehensions                   | 12.2 us                                                | 10.2 us: 1.20x faster                                      |
| hexiom                           | 4.85 ms                                                | 4.06 ms: 1.20x faster                                      |
| pickle_pure_python               | 213 us                                                 | 179 us: 1.19x faster                                       |
| chameleon                        | 5.08 ms                                                | 4.27 ms: 1.19x faster                                      |
| scimark_monte_carlo              | 50.4 ms                                                | 42.5 ms: 1.19x faster                                      |
| html5lib                         | 36.6 ms                                                | 31.2 ms: 1.18x faster                                      |
| logging_simple                   | 3.57 us                                                | 3.04 us: 1.17x faster                                      |
| async_tree_eager_tg              | 48.4 ms                                                | 41.4 ms: 1.17x faster                                      |
| sqlglot_parse                    | 856 us                                                 | 732 us: 1.17x faster                                       |
| async_tree_eager                 | 70.5 ms                                                | 60.3 ms: 1.17x faster                                      |
| logging_format                   | 3.85 us                                                | 3.31 us: 1.16x faster                                      |
| spectral_norm                    | 77.3 ms                                                | 66.4 ms: 1.16x faster                                      |
| logging_silent                   | 69.9 ns                                                | 60.1 ns: 1.16x faster                                      |
| unpickle_pure_python             | 163 us                                                 | 141 us: 1.16x faster                                       |
| float                            | 56.2 ms                                                | 48.6 ms: 1.16x faster                                      |
| typing_runtime_protocols         | 101 us                                                 | 87.6 us: 1.15x faster                                      |
| dask                             | 255 ms                                                 | 221 ms: 1.15x faster                                       |
| sqlglot_transpile                | 1.02 ms                                                | 891 us: 1.15x faster                                       |
| genshi_xml                       | 34.4 ms                                                | 29.9 ms: 1.15x faster                                      |
| regex_compile                    | 78.5 ms                                                | 68.5 ms: 1.15x faster                                      |
| scimark_lu                       | 76.5 ms                                                | 66.9 ms: 1.14x faster                                      |
| django_template                  | 22.2 ms                                                | 19.4 ms: 1.14x faster                                      |
| go                               | 115 ms                                                 | 101 ms: 1.14x faster                                       |
| pprint_safe_repr                 | 531 ms                                                 | 465 ms: 1.14x faster                                       |
| pprint_pformat                   | 1.08 sec                                               | 947 ms: 1.14x faster                                       |
| deepcopy                         | 232 us                                                 | 204 us: 1.14x faster                                       |
| sqlglot_normalize                | 189 ms                                                 | 166 ms: 1.14x faster                                       |
| asyncio_tcp                      | 457 ms                                                 | 402 ms: 1.14x faster                                       |
| fannkuch                         | 282 ms                                                 | 248 ms: 1.13x faster                                       |
| bench_thread_pool                | 506 us                                                 | 447 us: 1.13x faster                                       |
| deepcopy_reduce                  | 2.06 us                                                | 1.82 us: 1.13x faster                                      |
| sqlglot_optimize                 | 34.9 ms                                                | 30.9 ms: 1.13x faster                                      |
| python_startup                   | 17.0 ms                                                | 15.2 ms: 1.12x faster                                      |
| pycparser                        | 706 ms                                                 | 632 ms: 1.12x faster                                       |
| scimark_sor                      | 106 ms                                                 | 94.9 ms: 1.11x faster                                      |
| richards                         | 35.4 ms                                                | 31.8 ms: 1.11x faster                                      |
| richards_super                   | 39.1 ms                                                | 35.2 ms: 1.11x faster                                      |
| scimark_fft                      | 201 ms                                                 | 181 ms: 1.11x faster                                       |
| async_tree_eager_memoization     | 169 ms                                                 | 152 ms: 1.11x faster                                       |
| python_startup_no_site           | 13.7 ms                                                | 12.3 ms: 1.11x faster                                      |
| sympy_str                        | 145 ms                                                 | 131 ms: 1.11x faster                                       |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 126 ms: 1.11x faster                                       |
| 2to3                             | 178 ms                                                 | 161 ms: 1.10x faster                                       |
| xml_etree_process                | 40.9 ms                                                | 37.1 ms: 1.10x faster                                      |
| mako                             | 7.68 ms                                                | 6.99 ms: 1.10x faster                                      |
| sympy_integrate                  | 11.3 ms                                                | 10.3 ms: 1.10x faster                                      |
| pyflate                          | 351 ms                                                 | 321 ms: 1.09x faster                                       |
| sympy_sum                        | 75.6 ms                                                | 69.2 ms: 1.09x faster                                      |
| crypto_pyaes                     | 54.0 ms                                                | 49.5 ms: 1.09x faster                                      |
| sympy_expand                     | 246 ms                                                 | 226 ms: 1.09x faster                                       |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.77 ms: 1.08x faster                                      |
| bench_mp_pool                    | 50.9 ms                                                | 47.2 ms: 1.08x faster                                      |
| xml_etree_generate               | 56.6 ms                                                | 52.7 ms: 1.07x faster                                      |
| thrift                           | 466 us                                                 | 435 us: 1.07x faster                                       |
| tomli_loads                      | 1.56 sec                                               | 1.47 sec: 1.06x faster                                     |
| bpe_tokeniser                    | 3.24 sec                                               | 3.05 sec: 1.06x faster                                     |
| json_dumps                       | 6.56 ms                                                | 6.23 ms: 1.05x faster                                      |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 331 ms: 1.05x faster                                       |
| meteor_contest                   | 73.8 ms                                                | 70.3 ms: 1.05x faster                                      |
| async_generators                 | 294 ms                                                 | 281 ms: 1.05x faster                                       |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 358 ms: 1.05x faster                                       |
| telco                            | 4.80 ms                                                | 4.60 ms: 1.04x faster                                      |
| mypy2                            | 396 ms                                                 | 379 ms: 1.04x faster                                       |
| dulwich_log                      | 28.7 ms                                                | 27.6 ms: 1.04x faster                                      |
| async_tree_memoization           | 270 ms                                                 | 260 ms: 1.04x faster                                       |
| xml_etree_iterparse              | 74.2 ms                                                | 71.5 ms: 1.04x faster                                      |
| xml_etree_parse                  | 109 ms                                                 | 106 ms: 1.03x faster                                       |
| coverage                         | 46.1 ms                                                | 45.0 ms: 1.02x faster                                      |
| regex_effbot                     | 2.63 ms                                                | 2.58 ms: 1.02x faster                                      |
| unpickle_list                    | 2.93 us                                                | 2.88 us: 1.02x faster                                      |
| gc_traversal                     | 2.48 ms                                                | 2.45 ms: 1.01x faster                                      |
| pickle_list                      | 2.99 us                                                | 2.96 us: 1.01x faster                                      |
| pidigits                         | 284 ms                                                 | 282 ms: 1.01x faster                                       |
| docutils                         | 1.44 sec                                               | 1.44 sec: 1.01x faster                                     |
| sqlite_synth                     | 1.54 us                                                | 1.55 us: 1.00x slower                                      |
| pickle_dict                      | 18.2 us                                                | 18.3 us: 1.01x slower                                      |
| regex_dna                        | 148 ms                                                 | 149 ms: 1.01x slower                                       |
| pickle                           | 7.36 us                                                | 7.48 us: 1.02x slower                                      |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 467 ms: 1.02x slower                                       |
| regex_v8                         | 16.9 ms                                                | 17.3 ms: 1.02x slower                                      |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.29 sec: 1.02x slower                                     |
| mdp                              | 1.50 sec                                               | 1.53 sec: 1.02x slower                                     |
| pathlib                          | 22.8 ms                                                | 23.3 ms: 1.02x slower                                      |
| async_tree_io                    | 507 ms                                                 | 563 ms: 1.11x slower                                       |
| create_gc_cycles                 | 803 us                                                 | 897 us: 1.12x slower                                       |
| async_tree_io_tg                 | 500 ms                                                 | 565 ms: 1.13x slower                                       |
| flaskblogging                    | 2.89 ms                                                | 3.61 ms: 1.25x slower                                      |
| async_tree_eager_io              | 513 ms                                                 | 766 ms: 1.49x slower                                       |
| async_tree_eager_io_tg           | 477 ms                                                 | 768 ms: 1.61x slower                                       |
| asyncio_websockets               | 241 ms                                                 | 409 ms: 1.69x slower                                       |
| Geometric mean                   | (ref)                                                  | 1.08x faster                                               |

Benchmark hidden because not significant (8): tornado_http, pylint, async_tree_none, async_tree_none_tg, json, unpickle, json_loads, async_tree_cpu_io_mixed_tg
Ignored benchmarks (1) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 6.17x