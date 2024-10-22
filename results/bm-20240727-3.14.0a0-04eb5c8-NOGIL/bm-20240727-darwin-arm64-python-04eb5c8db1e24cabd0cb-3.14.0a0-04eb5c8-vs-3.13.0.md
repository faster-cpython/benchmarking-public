# Results vs. 3.13.0

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: darwin-arm64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.30x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x slower
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 248 ms: 1.39x slower                                                  |
| docutils       | 1.44 sec                                               | 1.79 sec: 1.24x slower                                                |
| html5lib       | 36.6 ms                                                | 51.2 ms: 1.40x slower                                                 |
| tornado_http   | 77.2 ms                                                | 94.5 ms: 1.23x slower                                                 |
| Geometric mean | (ref)                                                  | 1.31x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| asyncio_tcp                      | 457 ms                                                 | 350 ms: 1.31x faster                                                  |
| async_tree_memoization_tg        | 291 ms                                                 | 256 ms: 1.13x faster                                                  |
| async_tree_eager_io              | 513 ms                                                 | 484 ms: 1.06x faster                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 462 ms: 1.03x faster                                                  |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.23 sec: 1.03x faster                                                |
| async_tree_none_tg               | 198 ms                                                 | 201 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 456 ms: 1.02x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 522 ms: 1.03x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 364 ms: 1.05x slower                                                  |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 483 ms: 1.05x slower                                                  |
| async_tree_memoization           | 270 ms                                                 | 284 ms: 1.05x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 396 ms: 1.06x slower                                                  |
| async_tree_none                  | 212 ms                                                 | 229 ms: 1.08x slower                                                  |
| async_tree_eager_memoization     | 169 ms                                                 | 185 ms: 1.09x slower                                                  |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 157 ms: 1.13x slower                                                  |
| async_generators                 | 294 ms                                                 | 336 ms: 1.14x slower                                                  |
| coroutines                       | 19.8 ms                                                | 23.1 ms: 1.17x slower                                                 |
| async_tree_eager                 | 70.5 ms                                                | 105 ms: 1.49x slower                                                  |
| async_tree_eager_tg              | 48.4 ms                                                | 73.3 ms: 1.51x slower                                                 |
| asyncio_websockets               | 241 ms                                                 | 403 ms: 1.67x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.08x slower                                                          |

Benchmark hidden because not significant (1): async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 284 ms                                                 | 281 ms: 1.01x faster                                                  |
| float          | 56.2 ms                                                | 93.2 ms: 1.66x slower                                                 |
| nbody          | 73.9 ms                                                | 154 ms: 2.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.51x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 148 ms                                                 | 138 ms: 1.07x faster                                                  |
| regex_effbot   | 2.63 ms                                                | 2.59 ms: 1.01x faster                                                 |
| regex_v8       | 16.9 ms                                                | 17.5 ms: 1.03x slower                                                 |
| regex_compile  | 78.5 ms                                                | 122 ms: 1.56x slower                                                  |
| Geometric mean | (ref)                                                  | 1.10x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 109 ms                                                 | 97.3 ms: 1.12x faster                                                 |
| xml_etree_iterparse  | 74.2 ms                                                | 75.8 ms: 1.02x slower                                                 |
| json_loads           | 16.9 us                                                | 19.1 us: 1.13x slower                                                 |
| json_dumps           | 6.56 ms                                                | 7.90 ms: 1.20x slower                                                 |
| xml_etree_generate   | 56.6 ms                                                | 69.1 ms: 1.22x slower                                                 |
| tomli_loads          | 1.56 sec                                               | 2.03 sec: 1.30x slower                                                |
| xml_etree_process    | 40.9 ms                                                | 59.5 ms: 1.46x slower                                                 |
| pickle_pure_python   | 213 us                                                 | 342 us: 1.60x slower                                                  |
| unpickle_pure_python | 163 us                                                 | 268 us: 1.64x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.25x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                | 13.8 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 34.4 ms                                                | 50.6 ms: 1.47x slower                                                 |
| genshi_text     | 16.9 ms                                                | 25.4 ms: 1.51x slower                                                 |
| django_template | 22.2 ms                                                | 35.9 ms: 1.62x slower                                                 |
| mako            | 7.68 ms                                                | 13.6 ms: 1.77x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.59x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| sqlglot_normalize                | 189 ms                                                 | 106 ms: 1.78x faster                                                  |
| asyncio_tcp                      | 457 ms                                                 | 350 ms: 1.31x faster                                                  |
| gc_traversal                     | 2.48 ms                                                | 2.03 ms: 1.23x faster                                                 |
| create_gc_cycles                 | 803 us                                                 | 656 us: 1.22x faster                                                  |
| async_tree_memoization_tg        | 291 ms                                                 | 256 ms: 1.13x faster                                                  |
| xml_etree_parse                  | 109 ms                                                 | 97.3 ms: 1.12x faster                                                 |
| regex_dna                        | 148 ms                                                 | 138 ms: 1.07x faster                                                  |
| async_tree_eager_io              | 513 ms                                                 | 484 ms: 1.06x faster                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 462 ms: 1.03x faster                                                  |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.23 sec: 1.03x faster                                                |
| regex_effbot                     | 2.63 ms                                                | 2.59 ms: 1.01x faster                                                 |
| pidigits                         | 284 ms                                                 | 281 ms: 1.01x faster                                                  |
| python_startup_no_site           | 13.7 ms                                                | 13.8 ms: 1.01x slower                                                 |
| async_tree_none_tg               | 198 ms                                                 | 201 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 456 ms: 1.02x slower                                                  |
| xml_etree_iterparse              | 74.2 ms                                                | 75.8 ms: 1.02x slower                                                 |
| async_tree_io                    | 507 ms                                                 | 522 ms: 1.03x slower                                                  |
| regex_v8                         | 16.9 ms                                                | 17.5 ms: 1.03x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 364 ms: 1.05x slower                                                  |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 483 ms: 1.05x slower                                                  |
| async_tree_memoization           | 270 ms                                                 | 284 ms: 1.05x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 396 ms: 1.06x slower                                                  |
| deepcopy                         | 232 us                                                 | 249 us: 1.07x slower                                                  |
| async_tree_none                  | 212 ms                                                 | 229 ms: 1.08x slower                                                  |
| bench_mp_pool                    | 50.9 ms                                                | 55.4 ms: 1.09x slower                                                 |
| async_tree_eager_memoization     | 169 ms                                                 | 185 ms: 1.09x slower                                                  |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 157 ms: 1.13x slower                                                  |
| json_loads                       | 16.9 us                                                | 19.1 us: 1.13x slower                                                 |
| pathlib                          | 22.8 ms                                                | 25.9 ms: 1.14x slower                                                 |
| async_generators                 | 294 ms                                                 | 336 ms: 1.14x slower                                                  |
| json                             | 2.94 ms                                                | 3.37 ms: 1.15x slower                                                 |
| generators                       | 31.5 ms                                                | 36.2 ms: 1.15x slower                                                 |
| deepcopy_memo                    | 27.2 us                                                | 31.3 us: 1.15x slower                                                 |
| coroutines                       | 19.8 ms                                                | 23.1 ms: 1.17x slower                                                 |
| coverage                         | 46.1 ms                                                | 54.1 ms: 1.17x slower                                                 |
| telco                            | 4.80 ms                                                | 5.65 ms: 1.18x slower                                                 |
| pylint                           | 181 ms                                                 | 218 ms: 1.20x slower                                                  |
| json_dumps                       | 6.56 ms                                                | 7.90 ms: 1.20x slower                                                 |
| meteor_contest                   | 73.8 ms                                                | 88.8 ms: 1.20x slower                                                 |
| xml_etree_generate               | 56.6 ms                                                | 69.1 ms: 1.22x slower                                                 |
| tornado_http                     | 77.2 ms                                                | 94.5 ms: 1.23x slower                                                 |
| deepcopy_reduce                  | 2.06 us                                                | 2.53 us: 1.23x slower                                                 |
| nqueens                          | 62.9 ms                                                | 77.5 ms: 1.23x slower                                                 |
| mdp                              | 1.50 sec                                               | 1.85 sec: 1.23x slower                                                |
| docutils                         | 1.44 sec                                               | 1.79 sec: 1.24x slower                                                |
| bpe_tokeniser                    | 3.24 sec                                               | 4.03 sec: 1.24x slower                                                |
| fannkuch                         | 282 ms                                                 | 362 ms: 1.28x slower                                                  |
| tomli_loads                      | 1.56 sec                                               | 2.03 sec: 1.30x slower                                                |
| pycparser                        | 706 ms                                                 | 933 ms: 1.32x slower                                                  |
| scimark_fft                      | 201 ms                                                 | 266 ms: 1.32x slower                                                  |
| sympy_integrate                  | 11.3 ms                                                | 15.5 ms: 1.37x slower                                                 |
| pyflate                          | 351 ms                                                 | 482 ms: 1.37x slower                                                  |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 4.13 ms: 1.38x slower                                                 |
| 2to3                             | 178 ms                                                 | 248 ms: 1.39x slower                                                  |
| html5lib                         | 36.6 ms                                                | 51.2 ms: 1.40x slower                                                 |
| dulwich_log                      | 28.7 ms                                                | 41.0 ms: 1.43x slower                                                 |
| typing_runtime_protocols         | 101 us                                                 | 145 us: 1.44x slower                                                  |
| crypto_pyaes                     | 54.0 ms                                                | 78.3 ms: 1.45x slower                                                 |
| xml_etree_process                | 40.9 ms                                                | 59.5 ms: 1.46x slower                                                 |
| genshi_xml                       | 34.4 ms                                                | 50.6 ms: 1.47x slower                                                 |
| thrift                           | 466 us                                                 | 687 us: 1.48x slower                                                  |
| scimark_sor                      | 106 ms                                                 | 157 ms: 1.48x slower                                                  |
| async_tree_eager                 | 70.5 ms                                                | 105 ms: 1.49x slower                                                  |
| genshi_text                      | 16.9 ms                                                | 25.4 ms: 1.51x slower                                                 |
| async_tree_eager_tg              | 48.4 ms                                                | 73.3 ms: 1.51x slower                                                 |
| sqlglot_optimize                 | 34.9 ms                                                | 53.2 ms: 1.52x slower                                                 |
| richards                         | 35.4 ms                                                | 54.2 ms: 1.53x slower                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 77.4 ms: 1.53x slower                                                 |
| comprehensions                   | 12.2 us                                                | 18.9 us: 1.55x slower                                                 |
| regex_compile                    | 78.5 ms                                                | 122 ms: 1.56x slower                                                  |
| bench_thread_pool                | 506 us                                                 | 791 us: 1.56x slower                                                  |
| pprint_safe_repr                 | 531 ms                                                 | 836 ms: 1.57x slower                                                  |
| pprint_pformat                   | 1.08 sec                                               | 1.70 sec: 1.58x slower                                                |
| pickle_pure_python               | 213 us                                                 | 342 us: 1.60x slower                                                  |
| sympy_str                        | 145 ms                                                 | 234 ms: 1.61x slower                                                  |
| django_template                  | 22.2 ms                                                | 35.9 ms: 1.62x slower                                                 |
| richards_super                   | 39.1 ms                                                | 63.6 ms: 1.62x slower                                                 |
| hexiom                           | 4.85 ms                                                | 7.89 ms: 1.63x slower                                                 |
| unpickle_pure_python             | 163 us                                                 | 268 us: 1.64x slower                                                  |
| spectral_norm                    | 77.3 ms                                                | 128 ms: 1.65x slower                                                  |
| float                            | 56.2 ms                                                | 93.2 ms: 1.66x slower                                                 |
| go                               | 115 ms                                                 | 192 ms: 1.67x slower                                                  |
| asyncio_websockets               | 241 ms                                                 | 403 ms: 1.67x slower                                                  |
| logging_simple                   | 3.57 us                                                | 6.07 us: 1.70x slower                                                 |
| logging_format                   | 3.85 us                                                | 6.58 us: 1.71x slower                                                 |
| mako                             | 7.68 ms                                                | 13.6 ms: 1.77x slower                                                 |
| sympy_expand                     | 246 ms                                                 | 438 ms: 1.78x slower                                                  |
| chaos                            | 41.3 ms                                                | 75.5 ms: 1.83x slower                                                 |
| sympy_sum                        | 75.6 ms                                                | 139 ms: 1.84x slower                                                  |
| sqlglot_transpile                | 1.02 ms                                                | 1.89 ms: 1.85x slower                                                 |
| logging_silent                   | 69.9 ns                                                | 130 ns: 1.86x slower                                                  |
| sqlglot_parse                    | 856 us                                                 | 1.66 ms: 1.93x slower                                                 |
| scimark_lu                       | 76.5 ms                                                | 155 ms: 2.02x slower                                                  |
| raytrace                         | 182 ms                                                 | 368 ms: 2.03x slower                                                  |
| deltablue                        | 2.68 ms                                                | 5.55 ms: 2.07x slower                                                 |
| nbody                            | 73.9 ms                                                | 154 ms: 2.08x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.30x slower                                                          |

Benchmark hidden because not significant (2): async_tree_io_tg, python_startup
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.23x
- 95% likely to have a slowdown of 1.21x
- 99% likely to have a slowdown of 1.18x

# Memory
- memory change: 0.98x