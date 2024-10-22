# Results vs. 3.13.0

- fork: python
- ref: v3.13.0b4
- machine: darwin-arm64
- commit hash: 567c38b
- commit date: 2024-07-18
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 6.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 162 ms: 1.09x faster                                       |
| chameleon      | 5.08 ms                                                | 4.31 ms: 1.18x faster                                      |
| html5lib       | 36.6 ms                                                | 31.5 ms: 1.16x faster                                      |
| Geometric mean | (ref)                                                  | 1.12x faster                                               |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 15.9 ms: 1.25x faster                                      |
| async_tree_memoization_tg        | 291 ms                                                 | 240 ms: 1.21x faster                                       |
| async_tree_eager_tg              | 48.4 ms                                                | 41.6 ms: 1.17x faster                                      |
| async_tree_eager                 | 70.5 ms                                                | 61.1 ms: 1.15x faster                                      |
| async_tree_eager_memoization     | 169 ms                                                 | 150 ms: 1.13x faster                                       |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 126 ms: 1.10x faster                                       |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 331 ms: 1.05x faster                                       |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 359 ms: 1.04x faster                                       |
| async_generators                 | 294 ms                                                 | 282 ms: 1.04x faster                                       |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 469 ms: 1.02x slower                                       |
| async_tree_io                    | 507 ms                                                 | 557 ms: 1.10x slower                                       |
| async_tree_io_tg                 | 500 ms                                                 | 562 ms: 1.12x slower                                       |
| async_tree_eager_io              | 513 ms                                                 | 768 ms: 1.50x slower                                       |
| async_tree_eager_io_tg           | 477 ms                                                 | 766 ms: 1.61x slower                                       |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                       |
| Geometric mean                   | (ref)                                                  | 1.03x slower                                               |

Benchmark hidden because not significant (6): async_tree_memoization, asyncio_tcp, async_tree_none, async_tree_none_tg, asyncio_tcp_ssl, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 73.9 ms                                                | 59.8 ms: 1.24x faster                                      |
| float          | 56.2 ms                                                | 48.7 ms: 1.15x faster                                      |
| pidigits       | 284 ms                                                 | 281 ms: 1.01x faster                                       |
| Geometric mean | (ref)                                                  | 1.13x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 68.4 ms: 1.15x faster                                      |
| regex_effbot   | 2.63 ms                                                | 2.57 ms: 1.02x faster                                      |
| regex_dna      | 148 ms                                                 | 149 ms: 1.01x slower                                       |
| regex_v8       | 16.9 ms                                                | 17.2 ms: 1.02x slower                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 213 us                                                 | 180 us: 1.18x faster                                       |
| unpickle_pure_python | 163 us                                                 | 142 us: 1.15x faster                                       |
| xml_etree_process    | 40.9 ms                                                | 37.3 ms: 1.10x faster                                      |
| xml_etree_generate   | 56.6 ms                                                | 53.0 ms: 1.07x faster                                      |
| tomli_loads          | 1.56 sec                                               | 1.48 sec: 1.05x faster                                     |
| json_dumps           | 6.56 ms                                                | 6.25 ms: 1.05x faster                                      |
| xml_etree_iterparse  | 74.2 ms                                                | 71.3 ms: 1.04x faster                                      |
| xml_etree_parse      | 109 ms                                                 | 105 ms: 1.04x faster                                       |
| json_loads           | 16.9 us                                                | 17.0 us: 1.01x slower                                      |
| Geometric mean       | (ref)                                                  | 1.07x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 17.0 ms                                                | 14.1 ms: 1.21x faster                                      |
| python_startup_no_site | 13.7 ms                                                | 11.3 ms: 1.20x faster                                      |
| Geometric mean         | (ref)                                                  | 1.21x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 13.8 ms: 1.22x faster                                      |
| genshi_xml      | 34.4 ms                                                | 29.8 ms: 1.16x faster                                      |
| django_template | 22.2 ms                                                | 19.5 ms: 1.14x faster                                      |
| mako            | 7.68 ms                                                | 7.00 ms: 1.10x faster                                      |
| Geometric mean  | (ref)                                                  | 1.15x faster                                               |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| generators                       | 31.5 ms                                                | 23.0 ms: 1.37x faster                                      |
| deltablue                        | 2.68 ms                                                | 2.15 ms: 1.25x faster                                      |
| coroutines                       | 19.8 ms                                                | 15.9 ms: 1.25x faster                                      |
| nbody                            | 73.9 ms                                                | 59.8 ms: 1.24x faster                                      |
| genshi_text                      | 16.9 ms                                                | 13.8 ms: 1.22x faster                                      |
| raytrace                         | 182 ms                                                 | 148 ms: 1.22x faster                                       |
| async_tree_memoization_tg        | 291 ms                                                 | 240 ms: 1.21x faster                                       |
| python_startup                   | 17.0 ms                                                | 14.1 ms: 1.21x faster                                      |
| python_startup_no_site           | 13.7 ms                                                | 11.3 ms: 1.20x faster                                      |
| deepcopy_memo                    | 27.2 us                                                | 22.7 us: 1.20x faster                                      |
| comprehensions                   | 12.2 us                                                | 10.2 us: 1.19x faster                                      |
| hexiom                           | 4.85 ms                                                | 4.07 ms: 1.19x faster                                      |
| chaos                            | 41.3 ms                                                | 34.7 ms: 1.19x faster                                      |
| nqueens                          | 62.9 ms                                                | 52.9 ms: 1.19x faster                                      |
| pickle_pure_python               | 213 us                                                 | 180 us: 1.18x faster                                       |
| scimark_monte_carlo              | 50.4 ms                                                | 42.6 ms: 1.18x faster                                      |
| chameleon                        | 5.08 ms                                                | 4.31 ms: 1.18x faster                                      |
| sqlglot_parse                    | 856 us                                                 | 730 us: 1.17x faster                                       |
| async_tree_eager_tg              | 48.4 ms                                                | 41.6 ms: 1.17x faster                                      |
| html5lib                         | 36.6 ms                                                | 31.5 ms: 1.16x faster                                      |
| logging_silent                   | 69.9 ns                                                | 60.1 ns: 1.16x faster                                      |
| dask                             | 255 ms                                                 | 220 ms: 1.16x faster                                       |
| spectral_norm                    | 77.3 ms                                                | 66.8 ms: 1.16x faster                                      |
| pprint_safe_repr                 | 531 ms                                                 | 459 ms: 1.16x faster                                       |
| genshi_xml                       | 34.4 ms                                                | 29.8 ms: 1.16x faster                                      |
| float                            | 56.2 ms                                                | 48.7 ms: 1.15x faster                                      |
| async_tree_eager                 | 70.5 ms                                                | 61.1 ms: 1.15x faster                                      |
| pprint_pformat                   | 1.08 sec                                               | 936 ms: 1.15x faster                                       |
| logging_simple                   | 3.57 us                                                | 3.11 us: 1.15x faster                                      |
| sqlglot_transpile                | 1.02 ms                                                | 892 us: 1.15x faster                                       |
| regex_compile                    | 78.5 ms                                                | 68.4 ms: 1.15x faster                                      |
| unpickle_pure_python             | 163 us                                                 | 142 us: 1.15x faster                                       |
| go                               | 115 ms                                                 | 100 ms: 1.15x faster                                       |
| scimark_lu                       | 76.5 ms                                                | 66.7 ms: 1.15x faster                                      |
| richards_super                   | 39.1 ms                                                | 34.3 ms: 1.14x faster                                      |
| deepcopy                         | 232 us                                                 | 204 us: 1.14x faster                                       |
| typing_runtime_protocols         | 101 us                                                 | 88.7 us: 1.14x faster                                      |
| sqlglot_normalize                | 189 ms                                                 | 166 ms: 1.14x faster                                       |
| django_template                  | 22.2 ms                                                | 19.5 ms: 1.14x faster                                      |
| richards                         | 35.4 ms                                                | 31.2 ms: 1.14x faster                                      |
| logging_format                   | 3.85 us                                                | 3.40 us: 1.13x faster                                      |
| sqlglot_optimize                 | 34.9 ms                                                | 30.8 ms: 1.13x faster                                      |
| deepcopy_reduce                  | 2.06 us                                                | 1.82 us: 1.13x faster                                      |
| async_tree_eager_memoization     | 169 ms                                                 | 150 ms: 1.13x faster                                       |
| pycparser                        | 706 ms                                                 | 630 ms: 1.12x faster                                       |
| scimark_fft                      | 201 ms                                                 | 181 ms: 1.11x faster                                       |
| scimark_sor                      | 106 ms                                                 | 95.0 ms: 1.11x faster                                      |
| fannkuch                         | 282 ms                                                 | 254 ms: 1.11x faster                                       |
| sympy_str                        | 145 ms                                                 | 132 ms: 1.10x faster                                       |
| bench_thread_pool                | 506 us                                                 | 460 us: 1.10x faster                                       |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 126 ms: 1.10x faster                                       |
| mako                             | 7.68 ms                                                | 7.00 ms: 1.10x faster                                      |
| sympy_integrate                  | 11.3 ms                                                | 10.3 ms: 1.10x faster                                      |
| sympy_expand                     | 246 ms                                                 | 225 ms: 1.10x faster                                       |
| xml_etree_process                | 40.9 ms                                                | 37.3 ms: 1.10x faster                                      |
| pyflate                          | 351 ms                                                 | 321 ms: 1.09x faster                                       |
| 2to3                             | 178 ms                                                 | 162 ms: 1.09x faster                                       |
| bench_mp_pool                    | 50.9 ms                                                | 46.5 ms: 1.09x faster                                      |
| sympy_sum                        | 75.6 ms                                                | 69.5 ms: 1.09x faster                                      |
| crypto_pyaes                     | 54.0 ms                                                | 50.0 ms: 1.08x faster                                      |
| thrift                           | 466 us                                                 | 433 us: 1.08x faster                                       |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.80 ms: 1.07x faster                                      |
| xml_etree_generate               | 56.6 ms                                                | 53.0 ms: 1.07x faster                                      |
| mdp                              | 1.50 sec                                               | 1.41 sec: 1.07x faster                                     |
| bpe_tokeniser                    | 3.24 sec                                               | 3.05 sec: 1.06x faster                                     |
| tomli_loads                      | 1.56 sec                                               | 1.48 sec: 1.05x faster                                     |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 331 ms: 1.05x faster                                       |
| dulwich_log                      | 28.7 ms                                                | 27.4 ms: 1.05x faster                                      |
| json_dumps                       | 6.56 ms                                                | 6.25 ms: 1.05x faster                                      |
| meteor_contest                   | 73.8 ms                                                | 70.5 ms: 1.05x faster                                      |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 359 ms: 1.04x faster                                       |
| async_generators                 | 294 ms                                                 | 282 ms: 1.04x faster                                       |
| xml_etree_iterparse              | 74.2 ms                                                | 71.3 ms: 1.04x faster                                      |
| xml_etree_parse                  | 109 ms                                                 | 105 ms: 1.04x faster                                       |
| telco                            | 4.80 ms                                                | 4.63 ms: 1.04x faster                                      |
| coverage                         | 46.1 ms                                                | 45.0 ms: 1.02x faster                                      |
| regex_effbot                     | 2.63 ms                                                | 2.57 ms: 1.02x faster                                      |
| gc_traversal                     | 2.48 ms                                                | 2.45 ms: 1.01x faster                                      |
| pidigits                         | 284 ms                                                 | 281 ms: 1.01x faster                                       |
| json                             | 2.94 ms                                                | 2.92 ms: 1.01x faster                                      |
| json_loads                       | 16.9 us                                                | 17.0 us: 1.01x slower                                      |
| regex_dna                        | 148 ms                                                 | 149 ms: 1.01x slower                                       |
| regex_v8                         | 16.9 ms                                                | 17.2 ms: 1.02x slower                                      |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 469 ms: 1.02x slower                                       |
| pathlib                          | 22.8 ms                                                | 23.7 ms: 1.04x slower                                      |
| create_gc_cycles                 | 803 us                                                 | 867 us: 1.08x slower                                       |
| async_tree_io                    | 507 ms                                                 | 557 ms: 1.10x slower                                       |
| async_tree_io_tg                 | 500 ms                                                 | 562 ms: 1.12x slower                                       |
| mypy2                            | 396 ms                                                 | 447 ms: 1.13x slower                                       |
| async_tree_eager_io              | 513 ms                                                 | 768 ms: 1.50x slower                                       |
| async_tree_eager_io_tg           | 477 ms                                                 | 766 ms: 1.61x slower                                       |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                       |
| Geometric mean                   | (ref)                                                  | 1.08x faster                                               |

Benchmark hidden because not significant (9): tornado_http, pylint, async_tree_memoization, asyncio_tcp, async_tree_none, docutils, async_tree_none_tg, asyncio_tcp_ssl, async_tree_cpu_io_mixed_tg
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 6.01x