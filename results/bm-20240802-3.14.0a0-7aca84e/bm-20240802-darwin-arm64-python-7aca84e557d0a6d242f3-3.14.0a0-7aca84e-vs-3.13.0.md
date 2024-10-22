# Results vs. 3.13.0

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: darwin-arm64
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 164 ms: 1.09x faster                                                  |
| docutils       | 1.44 sec                                               | 1.49 sec: 1.03x slower                                                |
| html5lib       | 36.6 ms                                                | 31.5 ms: 1.16x faster                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 291 ms                                                 | 228 ms: 1.28x faster                                                  |
| coroutines                       | 19.8 ms                                                | 16.1 ms: 1.22x faster                                                 |
| async_tree_eager_tg              | 48.4 ms                                                | 42.2 ms: 1.15x faster                                                 |
| async_tree_eager                 | 70.5 ms                                                | 62.3 ms: 1.13x faster                                                 |
| asyncio_tcp                      | 457 ms                                                 | 405 ms: 1.13x faster                                                  |
| async_tree_memoization           | 270 ms                                                 | 240 ms: 1.13x faster                                                  |
| async_tree_eager_memoization     | 169 ms                                                 | 152 ms: 1.11x faster                                                  |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 125 ms: 1.11x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 195 ms: 1.09x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 183 ms: 1.09x faster                                                  |
| async_generators                 | 294 ms                                                 | 280 ms: 1.05x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 361 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 337 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 453 ms: 1.02x faster                                                  |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.29 sec: 1.02x slower                                                |
| async_tree_io                    | 507 ms                                                 | 547 ms: 1.08x slower                                                  |
| async_tree_eager_io              | 513 ms                                                 | 640 ms: 1.25x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 676 ms: 1.42x slower                                                  |
| asyncio_websockets               | 241 ms                                                 | 409 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 73.9 ms                                                | 59.6 ms: 1.24x faster                                                 |
| float          | 56.2 ms                                                | 48.4 ms: 1.16x faster                                                 |
| pidigits       | 284 ms                                                 | 282 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 68.4 ms: 1.15x faster                                                 |
| regex_effbot   | 2.63 ms                                                | 2.55 ms: 1.03x faster                                                 |
| regex_dna      | 148 ms                                                 | 150 ms: 1.02x slower                                                  |
| regex_v8       | 16.9 ms                                                | 17.4 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 213 us                                                 | 184 us: 1.16x faster                                                  |
| unpickle_pure_python | 163 us                                                 | 143 us: 1.14x faster                                                  |
| xml_etree_process    | 40.9 ms                                                | 37.9 ms: 1.08x faster                                                 |
| xml_etree_generate   | 56.6 ms                                                | 53.4 ms: 1.06x faster                                                 |
| tomli_loads          | 1.56 sec                                               | 1.48 sec: 1.05x faster                                                |
| json_dumps           | 6.56 ms                                                | 6.54 ms: 1.00x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 111 ms: 1.02x slower                                                  |
| json_loads           | 16.9 us                                                | 17.2 us: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.0 ms                                                | 15.4 ms: 1.10x faster                                                 |
| python_startup_no_site | 13.7 ms                                                | 12.8 ms: 1.07x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 14.1 ms: 1.20x faster                                                 |
| genshi_xml      | 34.4 ms                                                | 30.3 ms: 1.14x faster                                                 |
| django_template | 22.2 ms                                                | 19.9 ms: 1.11x faster                                                 |
| mako            | 7.68 ms                                                | 7.02 ms: 1.09x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.13x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo                    | 27.2 us                                                | 16.9 us: 1.61x faster                                                 |
| deepcopy                         | 232 us                                                 | 145 us: 1.60x faster                                                  |
| generators                       | 31.5 ms                                                | 20.6 ms: 1.53x faster                                                 |
| deepcopy_reduce                  | 2.06 us                                                | 1.50 us: 1.37x faster                                                 |
| async_tree_memoization_tg        | 291 ms                                                 | 228 ms: 1.28x faster                                                  |
| deltablue                        | 2.68 ms                                                | 2.12 ms: 1.27x faster                                                 |
| nbody                            | 73.9 ms                                                | 59.6 ms: 1.24x faster                                                 |
| coroutines                       | 19.8 ms                                                | 16.1 ms: 1.22x faster                                                 |
| raytrace                         | 182 ms                                                 | 148 ms: 1.22x faster                                                  |
| hexiom                           | 4.85 ms                                                | 4.06 ms: 1.20x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 14.1 ms: 1.20x faster                                                 |
| nqueens                          | 62.9 ms                                                | 53.3 ms: 1.18x faster                                                 |
| go                               | 115 ms                                                 | 97.7 ms: 1.18x faster                                                 |
| logging_simple                   | 3.57 us                                                | 3.05 us: 1.17x faster                                                 |
| logging_silent                   | 69.9 ns                                                | 60.0 ns: 1.17x faster                                                 |
| html5lib                         | 36.6 ms                                                | 31.5 ms: 1.16x faster                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 43.3 ms: 1.16x faster                                                 |
| float                            | 56.2 ms                                                | 48.4 ms: 1.16x faster                                                 |
| pickle_pure_python               | 213 us                                                 | 184 us: 1.16x faster                                                  |
| spectral_norm                    | 77.3 ms                                                | 66.8 ms: 1.16x faster                                                 |
| async_tree_eager_tg              | 48.4 ms                                                | 42.2 ms: 1.15x faster                                                 |
| regex_compile                    | 78.5 ms                                                | 68.4 ms: 1.15x faster                                                 |
| chaos                            | 41.3 ms                                                | 36.0 ms: 1.15x faster                                                 |
| sqlglot_parse                    | 856 us                                                 | 748 us: 1.14x faster                                                  |
| scimark_lu                       | 76.5 ms                                                | 67.0 ms: 1.14x faster                                                 |
| unpickle_pure_python             | 163 us                                                 | 143 us: 1.14x faster                                                  |
| logging_format                   | 3.85 us                                                | 3.38 us: 1.14x faster                                                 |
| genshi_xml                       | 34.4 ms                                                | 30.3 ms: 1.14x faster                                                 |
| scimark_sor                      | 106 ms                                                 | 93.2 ms: 1.13x faster                                                 |
| richards_super                   | 39.1 ms                                                | 34.6 ms: 1.13x faster                                                 |
| async_tree_eager                 | 70.5 ms                                                | 62.3 ms: 1.13x faster                                                 |
| pprint_safe_repr                 | 531 ms                                                 | 470 ms: 1.13x faster                                                  |
| asyncio_tcp                      | 457 ms                                                 | 405 ms: 1.13x faster                                                  |
| async_tree_memoization           | 270 ms                                                 | 240 ms: 1.13x faster                                                  |
| pprint_pformat                   | 1.08 sec                                               | 958 ms: 1.13x faster                                                  |
| sqlglot_transpile                | 1.02 ms                                                | 911 us: 1.12x faster                                                  |
| richards                         | 35.4 ms                                                | 31.6 ms: 1.12x faster                                                 |
| bench_thread_pool                | 506 us                                                 | 452 us: 1.12x faster                                                  |
| django_template                  | 22.2 ms                                                | 19.9 ms: 1.11x faster                                                 |
| comprehensions                   | 12.2 us                                                | 10.9 us: 1.11x faster                                                 |
| async_tree_eager_memoization     | 169 ms                                                 | 152 ms: 1.11x faster                                                  |
| dask                             | 255 ms                                                 | 230 ms: 1.11x faster                                                  |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 125 ms: 1.11x faster                                                  |
| sqlglot_optimize                 | 34.9 ms                                                | 31.6 ms: 1.10x faster                                                 |
| python_startup                   | 17.0 ms                                                | 15.4 ms: 1.10x faster                                                 |
| sqlglot_normalize                | 189 ms                                                 | 171 ms: 1.10x faster                                                  |
| pycparser                        | 706 ms                                                 | 642 ms: 1.10x faster                                                  |
| mako                             | 7.68 ms                                                | 7.02 ms: 1.09x faster                                                 |
| pyflate                          | 351 ms                                                 | 321 ms: 1.09x faster                                                  |
| scimark_fft                      | 201 ms                                                 | 185 ms: 1.09x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 195 ms: 1.09x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 183 ms: 1.09x faster                                                  |
| 2to3                             | 178 ms                                                 | 164 ms: 1.09x faster                                                  |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.77 ms: 1.08x faster                                                 |
| sympy_integrate                  | 11.3 ms                                                | 10.5 ms: 1.08x faster                                                 |
| sympy_str                        | 145 ms                                                 | 135 ms: 1.08x faster                                                  |
| thrift                           | 466 us                                                 | 432 us: 1.08x faster                                                  |
| xml_etree_process                | 40.9 ms                                                | 37.9 ms: 1.08x faster                                                 |
| typing_runtime_protocols         | 101 us                                                 | 94.2 us: 1.07x faster                                                 |
| fannkuch                         | 282 ms                                                 | 263 ms: 1.07x faster                                                  |
| crypto_pyaes                     | 54.0 ms                                                | 50.4 ms: 1.07x faster                                                 |
| python_startup_no_site           | 13.7 ms                                                | 12.8 ms: 1.07x faster                                                 |
| sympy_sum                        | 75.6 ms                                                | 71.0 ms: 1.06x faster                                                 |
| sympy_expand                     | 246 ms                                                 | 232 ms: 1.06x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 27.1 ms: 1.06x faster                                                 |
| xml_etree_generate               | 56.6 ms                                                | 53.4 ms: 1.06x faster                                                 |
| mdp                              | 1.50 sec                                               | 1.42 sec: 1.06x faster                                                |
| tomli_loads                      | 1.56 sec                                               | 1.48 sec: 1.05x faster                                                |
| bench_mp_pool                    | 50.9 ms                                                | 48.3 ms: 1.05x faster                                                 |
| async_generators                 | 294 ms                                                 | 280 ms: 1.05x faster                                                  |
| bpe_tokeniser                    | 3.24 sec                                               | 3.10 sec: 1.05x faster                                                |
| telco                            | 4.80 ms                                                | 4.60 ms: 1.04x faster                                                 |
| coverage                         | 46.1 ms                                                | 44.3 ms: 1.04x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 361 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 337 ms: 1.03x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.55 ms: 1.03x faster                                                 |
| meteor_contest                   | 73.8 ms                                                | 72.1 ms: 1.02x faster                                                 |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 453 ms: 1.02x faster                                                  |
| gc_traversal                     | 2.48 ms                                                | 2.46 ms: 1.01x faster                                                 |
| pidigits                         | 284 ms                                                 | 282 ms: 1.01x faster                                                  |
| json_dumps                       | 6.56 ms                                                | 6.54 ms: 1.00x faster                                                 |
| json                             | 2.94 ms                                                | 2.96 ms: 1.01x slower                                                 |
| pathlib                          | 22.8 ms                                                | 23.1 ms: 1.01x slower                                                 |
| regex_dna                        | 148 ms                                                 | 150 ms: 1.02x slower                                                  |
| xml_etree_parse                  | 109 ms                                                 | 111 ms: 1.02x slower                                                  |
| json_loads                       | 16.9 us                                                | 17.2 us: 1.02x slower                                                 |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.29 sec: 1.02x slower                                                |
| regex_v8                         | 16.9 ms                                                | 17.4 ms: 1.03x slower                                                 |
| docutils                         | 1.44 sec                                               | 1.49 sec: 1.03x slower                                                |
| async_tree_io                    | 507 ms                                                 | 547 ms: 1.08x slower                                                  |
| create_gc_cycles                 | 803 us                                                 | 878 us: 1.09x slower                                                  |
| async_tree_eager_io              | 513 ms                                                 | 640 ms: 1.25x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 676 ms: 1.42x slower                                                  |
| asyncio_websockets               | 241 ms                                                 | 409 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (5): tornado_http, async_tree_cpu_io_mixed_tg, xml_etree_iterparse, pylint, async_tree_io_tg
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 0.98x