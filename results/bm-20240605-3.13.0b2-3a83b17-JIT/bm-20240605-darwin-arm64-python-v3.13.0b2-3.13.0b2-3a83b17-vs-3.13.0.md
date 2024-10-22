# Results vs. 3.13.0

- fork: python
- ref: v3.13.0b2
- machine: darwin-arm64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 6.79x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 173 ms: 1.03x faster                                       |
| chameleon      | 5.08 ms                                                | 4.41 ms: 1.15x faster                                      |
| docutils       | 1.44 sec                                               | 1.51 sec: 1.05x slower                                     |
| html5lib       | 36.6 ms                                                | 31.1 ms: 1.18x faster                                      |
| Geometric mean | (ref)                                                  | 1.09x faster                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.0 ms: 1.24x faster                                      |
| async_tree_memoization_tg        | 291 ms                                                 | 242 ms: 1.20x faster                                       |
| async_tree_eager_tg              | 48.4 ms                                                | 42.7 ms: 1.13x faster                                      |
| async_tree_eager                 | 70.5 ms                                                | 63.3 ms: 1.11x faster                                      |
| asyncio_tcp                      | 457 ms                                                 | 417 ms: 1.10x faster                                       |
| async_tree_eager_memoization     | 169 ms                                                 | 155 ms: 1.09x faster                                       |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 128 ms: 1.09x faster                                       |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 334 ms: 1.04x faster                                       |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 364 ms: 1.03x faster                                       |
| async_generators                 | 294 ms                                                 | 296 ms: 1.01x slower                                       |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.30 sec: 1.03x slower                                     |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 472 ms: 1.03x slower                                       |
| async_tree_io                    | 507 ms                                                 | 571 ms: 1.13x slower                                       |
| async_tree_io_tg                 | 500 ms                                                 | 570 ms: 1.14x slower                                       |
| async_tree_eager_io              | 513 ms                                                 | 761 ms: 1.48x slower                                       |
| async_tree_eager_io_tg           | 477 ms                                                 | 769 ms: 1.61x slower                                       |
| asyncio_websockets               | 241 ms                                                 | 409 ms: 1.70x slower                                       |
| Geometric mean                   | (ref)                                                  | 1.04x slower                                               |

Benchmark hidden because not significant (4): async_tree_memoization, async_tree_none, async_tree_none_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 56.2 ms                                                | 47.4 ms: 1.19x faster                                      |
| nbody          | 73.9 ms                                                | 63.5 ms: 1.17x faster                                      |
| pidigits       | 284 ms                                                 | 282 ms: 1.00x faster                                       |
| Geometric mean | (ref)                                                  | 1.12x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 71.9 ms: 1.09x faster                                      |
| regex_effbot   | 2.63 ms                                                | 2.58 ms: 1.02x faster                                      |
| regex_dna      | 148 ms                                                 | 149 ms: 1.01x slower                                       |
| regex_v8       | 16.9 ms                                                | 17.3 ms: 1.02x slower                                      |
| Geometric mean | (ref)                                                  | 1.02x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| tomli_loads          | 1.56 sec                                               | 1.24 sec: 1.26x faster                                     |
| unpickle_pure_python | 163 us                                                 | 132 us: 1.24x faster                                       |
| pickle_pure_python   | 213 us                                                 | 173 us: 1.23x faster                                       |
| xml_etree_process    | 40.9 ms                                                | 35.8 ms: 1.14x faster                                      |
| xml_etree_generate   | 56.6 ms                                                | 51.6 ms: 1.10x faster                                      |
| json_dumps           | 6.56 ms                                                | 6.17 ms: 1.06x faster                                      |
| xml_etree_iterparse  | 74.2 ms                                                | 70.5 ms: 1.05x faster                                      |
| xml_etree_parse      | 109 ms                                                 | 105 ms: 1.03x faster                                       |
| unpickle_list        | 2.93 us                                                | 2.88 us: 1.02x faster                                      |
| json_loads           | 16.9 us                                                | 16.9 us: 1.00x slower                                      |
| pickle_dict          | 18.2 us                                                | 18.2 us: 1.00x slower                                      |
| pickle               | 7.36 us                                                | 7.52 us: 1.02x slower                                      |
| Geometric mean       | (ref)                                                  | 1.07x faster                                               |

Benchmark hidden because not significant (2): pickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 17.0 ms                                                | 16.4 ms: 1.04x faster                                      |
| python_startup_no_site | 13.7 ms                                                | 13.4 ms: 1.02x faster                                      |
| Geometric mean         | (ref)                                                  | 1.03x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.40 ms: 1.20x faster                                      |
| django_template | 22.2 ms                                                | 21.3 ms: 1.04x faster                                      |
| genshi_text     | 16.9 ms                                                | 16.4 ms: 1.03x faster                                      |
| genshi_xml      | 34.4 ms                                                | 39.3 ms: 1.14x slower                                      |
| Geometric mean  | (ref)                                                  | 1.03x faster                                               |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| generators                       | 31.5 ms                                                | 23.6 ms: 1.34x faster                                      |
| deepcopy_memo                    | 27.2 us                                                | 21.5 us: 1.27x faster                                      |
| tomli_loads                      | 1.56 sec                                               | 1.24 sec: 1.26x faster                                     |
| unpickle_pure_python             | 163 us                                                 | 132 us: 1.24x faster                                       |
| coroutines                       | 19.8 ms                                                | 16.0 ms: 1.24x faster                                      |
| pickle_pure_python               | 213 us                                                 | 173 us: 1.23x faster                                       |
| fannkuch                         | 282 ms                                                 | 233 ms: 1.21x faster                                       |
| mako                             | 7.68 ms                                                | 6.40 ms: 1.20x faster                                      |
| async_tree_memoization_tg        | 291 ms                                                 | 242 ms: 1.20x faster                                       |
| float                            | 56.2 ms                                                | 47.4 ms: 1.19x faster                                      |
| logging_simple                   | 3.57 us                                                | 3.02 us: 1.18x faster                                      |
| html5lib                         | 36.6 ms                                                | 31.1 ms: 1.18x faster                                      |
| nbody                            | 73.9 ms                                                | 63.5 ms: 1.17x faster                                      |
| logging_format                   | 3.85 us                                                | 3.33 us: 1.16x faster                                      |
| chameleon                        | 5.08 ms                                                | 4.41 ms: 1.15x faster                                      |
| scimark_monte_carlo              | 50.4 ms                                                | 44.0 ms: 1.15x faster                                      |
| gunicorn                         | 1.31 ms                                                | 1.15 ms: 1.14x faster                                      |
| spectral_norm                    | 77.3 ms                                                | 67.5 ms: 1.14x faster                                      |
| aiohttp                          | 1.26 ms                                                | 1.10 ms: 1.14x faster                                      |
| pprint_safe_repr                 | 531 ms                                                 | 464 ms: 1.14x faster                                       |
| dask                             | 255 ms                                                 | 223 ms: 1.14x faster                                       |
| xml_etree_process                | 40.9 ms                                                | 35.8 ms: 1.14x faster                                      |
| async_tree_eager_tg              | 48.4 ms                                                | 42.7 ms: 1.13x faster                                      |
| deepcopy_reduce                  | 2.06 us                                                | 1.82 us: 1.13x faster                                      |
| go                               | 115 ms                                                 | 102 ms: 1.13x faster                                       |
| pprint_pformat                   | 1.08 sec                                               | 958 ms: 1.13x faster                                       |
| deepcopy                         | 232 us                                                 | 208 us: 1.12x faster                                       |
| richards                         | 35.4 ms                                                | 31.7 ms: 1.12x faster                                      |
| raytrace                         | 182 ms                                                 | 163 ms: 1.12x faster                                       |
| hexiom                           | 4.85 ms                                                | 4.36 ms: 1.11x faster                                      |
| pyflate                          | 351 ms                                                 | 315 ms: 1.11x faster                                       |
| async_tree_eager                 | 70.5 ms                                                | 63.3 ms: 1.11x faster                                      |
| logging_silent                   | 69.9 ns                                                | 63.1 ns: 1.11x faster                                      |
| nqueens                          | 62.9 ms                                                | 56.8 ms: 1.11x faster                                      |
| richards_super                   | 39.1 ms                                                | 35.7 ms: 1.10x faster                                      |
| xml_etree_generate               | 56.6 ms                                                | 51.6 ms: 1.10x faster                                      |
| asyncio_tcp                      | 457 ms                                                 | 417 ms: 1.10x faster                                       |
| regex_compile                    | 78.5 ms                                                | 71.9 ms: 1.09x faster                                      |
| async_tree_eager_memoization     | 169 ms                                                 | 155 ms: 1.09x faster                                       |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 128 ms: 1.09x faster                                       |
| deltablue                        | 2.68 ms                                                | 2.47 ms: 1.09x faster                                      |
| scimark_fft                      | 201 ms                                                 | 185 ms: 1.08x faster                                       |
| typing_runtime_protocols         | 101 us                                                 | 93.5 us: 1.08x faster                                      |
| sqlglot_optimize                 | 34.9 ms                                                | 32.6 ms: 1.07x faster                                      |
| thrift                           | 466 us                                                 | 438 us: 1.06x faster                                       |
| json_dumps                       | 6.56 ms                                                | 6.17 ms: 1.06x faster                                      |
| sympy_str                        | 145 ms                                                 | 137 ms: 1.06x faster                                       |
| chaos                            | 41.3 ms                                                | 38.9 ms: 1.06x faster                                      |
| bench_thread_pool                | 506 us                                                 | 481 us: 1.05x faster                                       |
| scimark_sor                      | 106 ms                                                 | 100 ms: 1.05x faster                                       |
| xml_etree_iterparse              | 74.2 ms                                                | 70.5 ms: 1.05x faster                                      |
| mdp                              | 1.50 sec                                               | 1.43 sec: 1.05x faster                                     |
| pycparser                        | 706 ms                                                 | 672 ms: 1.05x faster                                       |
| bpe_tokeniser                    | 3.24 sec                                               | 3.09 sec: 1.05x faster                                     |
| sympy_expand                     | 246 ms                                                 | 236 ms: 1.05x faster                                       |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 334 ms: 1.04x faster                                       |
| crypto_pyaes                     | 54.0 ms                                                | 51.8 ms: 1.04x faster                                      |
| sympy_sum                        | 75.6 ms                                                | 72.4 ms: 1.04x faster                                      |
| python_startup                   | 17.0 ms                                                | 16.4 ms: 1.04x faster                                      |
| sympy_integrate                  | 11.3 ms                                                | 10.9 ms: 1.04x faster                                      |
| django_template                  | 22.2 ms                                                | 21.3 ms: 1.04x faster                                      |
| sqlglot_parse                    | 856 us                                                 | 826 us: 1.04x faster                                       |
| telco                            | 4.80 ms                                                | 4.64 ms: 1.04x faster                                      |
| xml_etree_parse                  | 109 ms                                                 | 105 ms: 1.03x faster                                       |
| meteor_contest                   | 73.8 ms                                                | 71.4 ms: 1.03x faster                                      |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 364 ms: 1.03x faster                                       |
| 2to3                             | 178 ms                                                 | 173 ms: 1.03x faster                                       |
| coverage                         | 46.1 ms                                                | 44.9 ms: 1.03x faster                                      |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.92 ms: 1.03x faster                                      |
| genshi_text                      | 16.9 ms                                                | 16.4 ms: 1.03x faster                                      |
| sqlglot_transpile                | 1.02 ms                                                | 1.00 ms: 1.02x faster                                      |
| regex_effbot                     | 2.63 ms                                                | 2.58 ms: 1.02x faster                                      |
| unpickle_list                    | 2.93 us                                                | 2.88 us: 1.02x faster                                      |
| python_startup_no_site           | 13.7 ms                                                | 13.4 ms: 1.02x faster                                      |
| gc_traversal                     | 2.48 ms                                                | 2.46 ms: 1.01x faster                                      |
| pidigits                         | 284 ms                                                 | 282 ms: 1.00x faster                                       |
| json_loads                       | 16.9 us                                                | 16.9 us: 1.00x slower                                      |
| pickle_dict                      | 18.2 us                                                | 18.2 us: 1.00x slower                                      |
| comprehensions                   | 12.2 us                                                | 12.2 us: 1.01x slower                                      |
| async_generators                 | 294 ms                                                 | 296 ms: 1.01x slower                                       |
| regex_dna                        | 148 ms                                                 | 149 ms: 1.01x slower                                       |
| sqlite_synth                     | 1.54 us                                                | 1.57 us: 1.02x slower                                      |
| regex_v8                         | 16.9 ms                                                | 17.3 ms: 1.02x slower                                      |
| pickle                           | 7.36 us                                                | 7.52 us: 1.02x slower                                      |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.30 sec: 1.03x slower                                     |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 472 ms: 1.03x slower                                       |
| pathlib                          | 22.8 ms                                                | 23.4 ms: 1.03x slower                                      |
| scimark_lu                       | 76.5 ms                                                | 78.6 ms: 1.03x slower                                      |
| mypy2                            | 396 ms                                                 | 408 ms: 1.03x slower                                       |
| docutils                         | 1.44 sec                                               | 1.51 sec: 1.05x slower                                     |
| create_gc_cycles                 | 803 us                                                 | 903 us: 1.12x slower                                       |
| async_tree_io                    | 507 ms                                                 | 571 ms: 1.13x slower                                       |
| async_tree_io_tg                 | 500 ms                                                 | 570 ms: 1.14x slower                                       |
| genshi_xml                       | 34.4 ms                                                | 39.3 ms: 1.14x slower                                      |
| flaskblogging                    | 2.89 ms                                                | 3.61 ms: 1.25x slower                                      |
| async_tree_eager_io              | 513 ms                                                 | 761 ms: 1.48x slower                                       |
| async_tree_eager_io_tg           | 477 ms                                                 | 769 ms: 1.61x slower                                       |
| asyncio_websockets               | 241 ms                                                 | 409 ms: 1.70x slower                                       |
| Geometric mean                   | (ref)                                                  | 1.05x faster                                               |

Benchmark hidden because not significant (11): tornado_http, async_tree_memoization, pickle_list, json, async_tree_none, dulwich_log, unpickle, bench_mp_pool, async_tree_none_tg, pylint, async_tree_cpu_io_mixed_tg
Ignored benchmarks (2) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: sqlglot_normalize, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 6.79x