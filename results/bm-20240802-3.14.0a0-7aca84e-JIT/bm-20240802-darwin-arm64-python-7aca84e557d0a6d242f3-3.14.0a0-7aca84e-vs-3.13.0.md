# Results vs. 3.13.0

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: darwin-arm64
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.07x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 174 ms: 1.02x faster                                                  |
| docutils       | 1.44 sec                                               | 1.54 sec: 1.06x slower                                                |
| html5lib       | 36.6 ms                                                | 30.9 ms: 1.18x faster                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 291 ms                                                 | 228 ms: 1.28x faster                                                  |
| coroutines                       | 19.8 ms                                                | 16.1 ms: 1.23x faster                                                 |
| async_tree_memoization           | 270 ms                                                 | 239 ms: 1.13x faster                                                  |
| async_tree_eager_tg              | 48.4 ms                                                | 43.1 ms: 1.12x faster                                                 |
| asyncio_tcp                      | 457 ms                                                 | 413 ms: 1.11x faster                                                  |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 126 ms: 1.10x faster                                                  |
| async_tree_eager                 | 70.5 ms                                                | 64.0 ms: 1.10x faster                                                 |
| async_tree_eager_memoization     | 169 ms                                                 | 154 ms: 1.10x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 182 ms: 1.09x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 194 ms: 1.09x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 337 ms: 1.03x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 363 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 453 ms: 1.02x faster                                                  |
| async_generators                 | 294 ms                                                 | 295 ms: 1.00x slower                                                  |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.29 sec: 1.02x slower                                                |
| async_tree_io                    | 507 ms                                                 | 544 ms: 1.07x slower                                                  |
| async_tree_eager_io              | 513 ms                                                 | 640 ms: 1.25x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 675 ms: 1.42x slower                                                  |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 56.2 ms                                                | 46.7 ms: 1.21x faster                                                 |
| nbody          | 73.9 ms                                                | 62.7 ms: 1.18x faster                                                 |
| pidigits       | 284 ms                                                 | 281 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 71.2 ms: 1.10x faster                                                 |
| regex_effbot   | 2.63 ms                                                | 2.58 ms: 1.02x faster                                                 |
| regex_v8       | 16.9 ms                                                | 17.2 ms: 1.02x slower                                                 |
| regex_dna      | 148 ms                                                 | 153 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.56 sec                                               | 1.25 sec: 1.25x faster                                                |
| unpickle_pure_python | 163 us                                                 | 131 us: 1.24x faster                                                  |
| pickle_pure_python   | 213 us                                                 | 174 us: 1.23x faster                                                  |
| xml_etree_process    | 40.9 ms                                                | 35.8 ms: 1.14x faster                                                 |
| xml_etree_generate   | 56.6 ms                                                | 51.7 ms: 1.10x faster                                                 |
| json_dumps           | 6.56 ms                                                | 6.35 ms: 1.03x faster                                                 |
| xml_etree_iterparse  | 74.2 ms                                                | 72.8 ms: 1.02x faster                                                 |
| json_loads           | 16.9 us                                                | 17.3 us: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.0 ms                                                | 16.1 ms: 1.06x faster                                                 |
| python_startup_no_site | 13.7 ms                                                | 13.1 ms: 1.04x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.46 ms: 1.19x faster                                                 |
| genshi_text     | 16.9 ms                                                | 14.7 ms: 1.15x faster                                                 |
| django_template | 22.2 ms                                                | 21.6 ms: 1.03x faster                                                 |
| genshi_xml      | 34.4 ms                                                | 34.9 ms: 1.01x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo                    | 27.2 us                                                | 17.2 us: 1.58x faster                                                 |
| deepcopy                         | 232 us                                                 | 154 us: 1.50x faster                                                  |
| deepcopy_reduce                  | 2.06 us                                                | 1.54 us: 1.33x faster                                                 |
| generators                       | 31.5 ms                                                | 24.6 ms: 1.28x faster                                                 |
| async_tree_memoization_tg        | 291 ms                                                 | 228 ms: 1.28x faster                                                  |
| tomli_loads                      | 1.56 sec                                               | 1.25 sec: 1.25x faster                                                |
| unpickle_pure_python             | 163 us                                                 | 131 us: 1.24x faster                                                  |
| coroutines                       | 19.8 ms                                                | 16.1 ms: 1.23x faster                                                 |
| pickle_pure_python               | 213 us                                                 | 174 us: 1.23x faster                                                  |
| float                            | 56.2 ms                                                | 46.7 ms: 1.21x faster                                                 |
| logging_simple                   | 3.57 us                                                | 2.99 us: 1.20x faster                                                 |
| scimark_sor                      | 106 ms                                                 | 88.4 ms: 1.20x faster                                                 |
| mako                             | 7.68 ms                                                | 6.46 ms: 1.19x faster                                                 |
| html5lib                         | 36.6 ms                                                | 30.9 ms: 1.18x faster                                                 |
| nbody                            | 73.9 ms                                                | 62.7 ms: 1.18x faster                                                 |
| logging_format                   | 3.85 us                                                | 3.30 us: 1.17x faster                                                 |
| scimark_lu                       | 76.5 ms                                                | 66.2 ms: 1.16x faster                                                 |
| deltablue                        | 2.68 ms                                                | 2.32 ms: 1.15x faster                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 43.8 ms: 1.15x faster                                                 |
| richards                         | 35.4 ms                                                | 30.9 ms: 1.15x faster                                                 |
| logging_silent                   | 69.9 ns                                                | 61.0 ns: 1.15x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 14.7 ms: 1.15x faster                                                 |
| richards_super                   | 39.1 ms                                                | 34.2 ms: 1.14x faster                                                 |
| xml_etree_process                | 40.9 ms                                                | 35.8 ms: 1.14x faster                                                 |
| go                               | 115 ms                                                 | 101 ms: 1.14x faster                                                  |
| fannkuch                         | 282 ms                                                 | 249 ms: 1.13x faster                                                  |
| spectral_norm                    | 77.3 ms                                                | 68.3 ms: 1.13x faster                                                 |
| raytrace                         | 182 ms                                                 | 160 ms: 1.13x faster                                                  |
| async_tree_memoization           | 270 ms                                                 | 239 ms: 1.13x faster                                                  |
| async_tree_eager_tg              | 48.4 ms                                                | 43.1 ms: 1.12x faster                                                 |
| pyflate                          | 351 ms                                                 | 313 ms: 1.12x faster                                                  |
| asyncio_tcp                      | 457 ms                                                 | 413 ms: 1.11x faster                                                  |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 126 ms: 1.10x faster                                                  |
| regex_compile                    | 78.5 ms                                                | 71.2 ms: 1.10x faster                                                 |
| async_tree_eager                 | 70.5 ms                                                | 64.0 ms: 1.10x faster                                                 |
| pprint_safe_repr                 | 531 ms                                                 | 483 ms: 1.10x faster                                                  |
| pprint_pformat                   | 1.08 sec                                               | 982 ms: 1.10x faster                                                  |
| hexiom                           | 4.85 ms                                                | 4.43 ms: 1.10x faster                                                 |
| xml_etree_generate               | 56.6 ms                                                | 51.7 ms: 1.10x faster                                                 |
| async_tree_eager_memoization     | 169 ms                                                 | 154 ms: 1.10x faster                                                  |
| dask                             | 255 ms                                                 | 233 ms: 1.09x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 182 ms: 1.09x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 194 ms: 1.09x faster                                                  |
| nqueens                          | 62.9 ms                                                | 57.8 ms: 1.09x faster                                                 |
| bpe_tokeniser                    | 3.24 sec                                               | 3.01 sec: 1.08x faster                                                |
| thrift                           | 466 us                                                 | 433 us: 1.08x faster                                                  |
| bench_thread_pool                | 506 us                                                 | 472 us: 1.07x faster                                                  |
| chaos                            | 41.3 ms                                                | 38.8 ms: 1.06x faster                                                 |
| scimark_fft                      | 201 ms                                                 | 189 ms: 1.06x faster                                                  |
| python_startup                   | 17.0 ms                                                | 16.1 ms: 1.06x faster                                                 |
| telco                            | 4.80 ms                                                | 4.56 ms: 1.05x faster                                                 |
| sqlglot_normalize                | 189 ms                                                 | 179 ms: 1.05x faster                                                  |
| crypto_pyaes                     | 54.0 ms                                                | 51.6 ms: 1.05x faster                                                 |
| sqlglot_optimize                 | 34.9 ms                                                | 33.4 ms: 1.05x faster                                                 |
| python_startup_no_site           | 13.7 ms                                                | 13.1 ms: 1.04x faster                                                 |
| meteor_contest                   | 73.8 ms                                                | 71.0 ms: 1.04x faster                                                 |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 337 ms: 1.03x faster                                                  |
| json_dumps                       | 6.56 ms                                                | 6.35 ms: 1.03x faster                                                 |
| typing_runtime_protocols         | 101 us                                                 | 97.8 us: 1.03x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 363 ms: 1.03x faster                                                  |
| coverage                         | 46.1 ms                                                | 44.7 ms: 1.03x faster                                                 |
| pycparser                        | 706 ms                                                 | 684 ms: 1.03x faster                                                  |
| django_template                  | 22.2 ms                                                | 21.6 ms: 1.03x faster                                                 |
| sympy_str                        | 145 ms                                                 | 142 ms: 1.03x faster                                                  |
| mdp                              | 1.50 sec                                               | 1.46 sec: 1.03x faster                                                |
| 2to3                             | 178 ms                                                 | 174 ms: 1.02x faster                                                  |
| xml_etree_iterparse              | 74.2 ms                                                | 72.8 ms: 1.02x faster                                                 |
| sympy_sum                        | 75.6 ms                                                | 74.2 ms: 1.02x faster                                                 |
| dulwich_log                      | 28.7 ms                                                | 28.2 ms: 1.02x faster                                                 |
| regex_effbot                     | 2.63 ms                                                | 2.58 ms: 1.02x faster                                                 |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 453 ms: 1.02x faster                                                  |
| sqlglot_parse                    | 856 us                                                 | 847 us: 1.01x faster                                                  |
| json                             | 2.94 ms                                                | 2.91 ms: 1.01x faster                                                 |
| pidigits                         | 284 ms                                                 | 281 ms: 1.01x faster                                                  |
| gc_traversal                     | 2.48 ms                                                | 2.47 ms: 1.01x faster                                                 |
| sympy_integrate                  | 11.3 ms                                                | 11.3 ms: 1.01x faster                                                 |
| sqlglot_transpile                | 1.02 ms                                                | 1.02 ms: 1.00x faster                                                 |
| async_generators                 | 294 ms                                                 | 295 ms: 1.00x slower                                                  |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 3.01 ms: 1.00x slower                                                 |
| genshi_xml                       | 34.4 ms                                                | 34.9 ms: 1.01x slower                                                 |
| regex_v8                         | 16.9 ms                                                | 17.2 ms: 1.02x slower                                                 |
| json_loads                       | 16.9 us                                                | 17.3 us: 1.02x slower                                                 |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.29 sec: 1.02x slower                                                |
| pathlib                          | 22.8 ms                                                | 23.5 ms: 1.03x slower                                                 |
| regex_dna                        | 148 ms                                                 | 153 ms: 1.04x slower                                                  |
| docutils                         | 1.44 sec                                               | 1.54 sec: 1.06x slower                                                |
| async_tree_io                    | 507 ms                                                 | 544 ms: 1.07x slower                                                  |
| create_gc_cycles                 | 803 us                                                 | 904 us: 1.13x slower                                                  |
| async_tree_eager_io              | 513 ms                                                 | 640 ms: 1.25x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 675 ms: 1.42x slower                                                  |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.07x faster                                                          |

Benchmark hidden because not significant (8): tornado_http, async_tree_cpu_io_mixed_tg, comprehensions, sympy_expand, bench_mp_pool, xml_etree_parse, async_tree_io_tg, pylint
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 0.98x