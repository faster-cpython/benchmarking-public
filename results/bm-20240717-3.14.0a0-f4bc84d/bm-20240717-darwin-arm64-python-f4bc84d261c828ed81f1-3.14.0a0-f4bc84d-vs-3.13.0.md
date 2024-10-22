# Results vs. 3.13.0

- fork: python
- ref: f4bc84d261c828ed81f1
- machine: darwin-arm64
- commit hash: f4bc84d
- commit date: 2024-07-17
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 6.59x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-darwin-arm64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 163 ms: 1.09x faster                                                  |
| docutils       | 1.44 sec                                               | 1.45 sec: 1.01x slower                                                |
| html5lib       | 36.6 ms                                                | 31.5 ms: 1.16x faster                                                 |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-darwin-arm64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.2 ms: 1.22x faster                                                 |
| async_tree_memoization_tg        | 291 ms                                                 | 240 ms: 1.21x faster                                                  |
| async_tree_memoization           | 270 ms                                                 | 231 ms: 1.17x faster                                                  |
| async_tree_eager_tg              | 48.4 ms                                                | 41.5 ms: 1.17x faster                                                 |
| async_tree_eager_memoization     | 169 ms                                                 | 149 ms: 1.14x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 175 ms: 1.14x faster                                                  |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 123 ms: 1.13x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 191 ms: 1.11x faster                                                  |
| asyncio_tcp                      | 457 ms                                                 | 414 ms: 1.10x faster                                                  |
| async_tree_eager                 | 70.5 ms                                                | 64.1 ms: 1.10x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 357 ms: 1.05x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 332 ms: 1.05x faster                                                  |
| async_generators                 | 294 ms                                                 | 283 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 451 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 445 ms: 1.00x faster                                                  |
| async_tree_io                    | 507 ms                                                 | 532 ms: 1.05x slower                                                  |
| async_tree_eager_io              | 513 ms                                                 | 706 ms: 1.38x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 696 ms: 1.46x slower                                                  |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (2): asyncio_tcp_ssl, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-darwin-arm64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 73.9 ms                                                | 62.2 ms: 1.19x faster                                                 |
| float          | 56.2 ms                                                | 48.8 ms: 1.15x faster                                                 |
| pidigits       | 284 ms                                                 | 281 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-darwin-arm64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 68.3 ms: 1.15x faster                                                 |
| regex_effbot   | 2.63 ms                                                | 2.57 ms: 1.02x faster                                                 |
| regex_dna      | 148 ms                                                 | 149 ms: 1.01x slower                                                  |
| regex_v8       | 16.9 ms                                                | 17.1 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-darwin-arm64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 213 us                                                 | 181 us: 1.18x faster                                                  |
| unpickle_pure_python | 163 us                                                 | 142 us: 1.15x faster                                                  |
| xml_etree_process    | 40.9 ms                                                | 37.8 ms: 1.08x faster                                                 |
| xml_etree_generate   | 56.6 ms                                                | 53.1 ms: 1.07x faster                                                 |
| tomli_loads          | 1.56 sec                                               | 1.49 sec: 1.05x faster                                                |
| xml_etree_iterparse  | 74.2 ms                                                | 72.4 ms: 1.02x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 108 ms: 1.01x faster                                                  |
| json_dumps           | 6.56 ms                                                | 6.53 ms: 1.01x faster                                                 |
| json_loads           | 16.9 us                                                | 17.2 us: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-darwin-arm64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                | 10.8 ms: 1.26x faster                                                 |
| python_startup         | 17.0 ms                                                | 13.6 ms: 1.25x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.26x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-darwin-arm64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 14.0 ms: 1.21x faster                                                 |
| genshi_xml      | 34.4 ms                                                | 30.3 ms: 1.13x faster                                                 |
| django_template | 22.2 ms                                                | 19.8 ms: 1.12x faster                                                 |
| mako            | 7.68 ms                                                | 7.05 ms: 1.09x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.14x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-darwin-arm64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo                    | 27.2 us                                                | 16.8 us: 1.62x faster                                                 |
| deepcopy                         | 232 us                                                 | 145 us: 1.60x faster                                                  |
| generators                       | 31.5 ms                                                | 22.7 ms: 1.39x faster                                                 |
| deepcopy_reduce                  | 2.06 us                                                | 1.50 us: 1.38x faster                                                 |
| deltablue                        | 2.68 ms                                                | 2.10 ms: 1.28x faster                                                 |
| python_startup_no_site           | 13.7 ms                                                | 10.8 ms: 1.26x faster                                                 |
| python_startup                   | 17.0 ms                                                | 13.6 ms: 1.25x faster                                                 |
| coroutines                       | 19.8 ms                                                | 16.2 ms: 1.22x faster                                                 |
| raytrace                         | 182 ms                                                 | 149 ms: 1.22x faster                                                  |
| async_tree_memoization_tg        | 291 ms                                                 | 240 ms: 1.21x faster                                                  |
| genshi_text                      | 16.9 ms                                                | 14.0 ms: 1.21x faster                                                 |
| nbody                            | 73.9 ms                                                | 62.2 ms: 1.19x faster                                                 |
| logging_silent                   | 69.9 ns                                                | 59.1 ns: 1.18x faster                                                 |
| hexiom                           | 4.85 ms                                                | 4.11 ms: 1.18x faster                                                 |
| logging_simple                   | 3.57 us                                                | 3.04 us: 1.18x faster                                                 |
| pickle_pure_python               | 213 us                                                 | 181 us: 1.18x faster                                                  |
| async_tree_memoization           | 270 ms                                                 | 231 ms: 1.17x faster                                                  |
| async_tree_eager_tg              | 48.4 ms                                                | 41.5 ms: 1.17x faster                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 43.3 ms: 1.16x faster                                                 |
| nqueens                          | 62.9 ms                                                | 54.0 ms: 1.16x faster                                                 |
| html5lib                         | 36.6 ms                                                | 31.5 ms: 1.16x faster                                                 |
| go                               | 115 ms                                                 | 98.9 ms: 1.16x faster                                                 |
| sqlglot_parse                    | 856 us                                                 | 739 us: 1.16x faster                                                  |
| chaos                            | 41.3 ms                                                | 35.7 ms: 1.16x faster                                                 |
| float                            | 56.2 ms                                                | 48.8 ms: 1.15x faster                                                 |
| logging_format                   | 3.85 us                                                | 3.35 us: 1.15x faster                                                 |
| unpickle_pure_python             | 163 us                                                 | 142 us: 1.15x faster                                                  |
| spectral_norm                    | 77.3 ms                                                | 67.2 ms: 1.15x faster                                                 |
| regex_compile                    | 78.5 ms                                                | 68.3 ms: 1.15x faster                                                 |
| richards_super                   | 39.1 ms                                                | 34.3 ms: 1.14x faster                                                 |
| sqlglot_transpile                | 1.02 ms                                                | 899 us: 1.14x faster                                                  |
| async_tree_eager_memoization     | 169 ms                                                 | 149 ms: 1.14x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 175 ms: 1.14x faster                                                  |
| pprint_safe_repr                 | 531 ms                                                 | 467 ms: 1.14x faster                                                  |
| genshi_xml                       | 34.4 ms                                                | 30.3 ms: 1.13x faster                                                 |
| pprint_pformat                   | 1.08 sec                                               | 952 ms: 1.13x faster                                                  |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 123 ms: 1.13x faster                                                  |
| richards                         | 35.4 ms                                                | 31.4 ms: 1.13x faster                                                 |
| comprehensions                   | 12.2 us                                                | 10.8 us: 1.12x faster                                                 |
| django_template                  | 22.2 ms                                                | 19.8 ms: 1.12x faster                                                 |
| bench_thread_pool                | 506 us                                                 | 453 us: 1.12x faster                                                  |
| sqlglot_normalize                | 189 ms                                                 | 169 ms: 1.12x faster                                                  |
| sqlglot_optimize                 | 34.9 ms                                                | 31.4 ms: 1.11x faster                                                 |
| bench_mp_pool                    | 50.9 ms                                                | 45.9 ms: 1.11x faster                                                 |
| async_tree_none                  | 212 ms                                                 | 191 ms: 1.11x faster                                                  |
| asyncio_tcp                      | 457 ms                                                 | 414 ms: 1.10x faster                                                  |
| async_tree_eager                 | 70.5 ms                                                | 64.1 ms: 1.10x faster                                                 |
| pyflate                          | 351 ms                                                 | 320 ms: 1.10x faster                                                  |
| pycparser                        | 706 ms                                                 | 643 ms: 1.10x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 96.5 ms: 1.10x faster                                                 |
| mako                             | 7.68 ms                                                | 7.05 ms: 1.09x faster                                                 |
| sympy_integrate                  | 11.3 ms                                                | 10.4 ms: 1.09x faster                                                 |
| 2to3                             | 178 ms                                                 | 163 ms: 1.09x faster                                                  |
| sympy_str                        | 145 ms                                                 | 134 ms: 1.08x faster                                                  |
| scimark_lu                       | 76.5 ms                                                | 70.7 ms: 1.08x faster                                                 |
| xml_etree_process                | 40.9 ms                                                | 37.8 ms: 1.08x faster                                                 |
| fannkuch                         | 282 ms                                                 | 262 ms: 1.08x faster                                                  |
| thrift                           | 466 us                                                 | 433 us: 1.07x faster                                                  |
| sympy_sum                        | 75.6 ms                                                | 70.5 ms: 1.07x faster                                                 |
| scimark_fft                      | 201 ms                                                 | 187 ms: 1.07x faster                                                  |
| crypto_pyaes                     | 54.0 ms                                                | 50.6 ms: 1.07x faster                                                 |
| typing_runtime_protocols         | 101 us                                                 | 94.7 us: 1.07x faster                                                 |
| xml_etree_generate               | 56.6 ms                                                | 53.1 ms: 1.07x faster                                                 |
| sympy_expand                     | 246 ms                                                 | 232 ms: 1.06x faster                                                  |
| mdp                              | 1.50 sec                                               | 1.42 sec: 1.06x faster                                                |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 357 ms: 1.05x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 332 ms: 1.05x faster                                                  |
| tomli_loads                      | 1.56 sec                                               | 1.49 sec: 1.05x faster                                                |
| telco                            | 4.80 ms                                                | 4.59 ms: 1.05x faster                                                 |
| bpe_tokeniser                    | 3.24 sec                                               | 3.11 sec: 1.04x faster                                                |
| async_generators                 | 294 ms                                                 | 283 ms: 1.04x faster                                                  |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.89 ms: 1.04x faster                                                 |
| meteor_contest                   | 73.8 ms                                                | 71.2 ms: 1.04x faster                                                 |
| regex_effbot                     | 2.63 ms                                                | 2.57 ms: 1.02x faster                                                 |
| xml_etree_iterparse              | 74.2 ms                                                | 72.4 ms: 1.02x faster                                                 |
| coverage                         | 46.1 ms                                                | 45.1 ms: 1.02x faster                                                 |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 451 ms: 1.02x faster                                                  |
| gc_traversal                     | 2.48 ms                                                | 2.45 ms: 1.01x faster                                                 |
| xml_etree_parse                  | 109 ms                                                 | 108 ms: 1.01x faster                                                  |
| pidigits                         | 284 ms                                                 | 281 ms: 1.01x faster                                                  |
| json_dumps                       | 6.56 ms                                                | 6.53 ms: 1.01x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 445 ms: 1.00x faster                                                  |
| docutils                         | 1.44 sec                                               | 1.45 sec: 1.01x slower                                                |
| json                             | 2.94 ms                                                | 2.96 ms: 1.01x slower                                                 |
| regex_dna                        | 148 ms                                                 | 149 ms: 1.01x slower                                                  |
| regex_v8                         | 16.9 ms                                                | 17.1 ms: 1.01x slower                                                 |
| pathlib                          | 22.8 ms                                                | 23.1 ms: 1.01x slower                                                 |
| json_loads                       | 16.9 us                                                | 17.2 us: 1.02x slower                                                 |
| async_tree_io                    | 507 ms                                                 | 532 ms: 1.05x slower                                                  |
| create_gc_cycles                 | 803 us                                                 | 896 us: 1.12x slower                                                  |
| async_tree_eager_io              | 513 ms                                                 | 706 ms: 1.38x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 696 ms: 1.46x slower                                                  |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (4): tornado_http, pylint, asyncio_tcp_ssl, async_tree_io_tg
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 6.59x