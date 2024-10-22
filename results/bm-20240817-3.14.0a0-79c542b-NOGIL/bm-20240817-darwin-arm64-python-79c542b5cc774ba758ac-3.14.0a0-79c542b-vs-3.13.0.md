# Results vs. 3.13.0

- fork: python
- ref: 79c542b5cc774ba758ac
- machine: darwin-arm64
- commit hash: 79c542b
- commit date: 2024-08-17
- overall geometric mean: 1.38x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 258 ms: 1.45x slower                                                  |
| docutils       | 1.44 sec                                               | 1.88 sec: 1.30x slower                                                |
| html5lib       | 36.6 ms                                                | 54.3 ms: 1.48x slower                                                 |
| tornado_http   | 77.2 ms                                                | 109 ms: 1.41x slower                                                  |
| Geometric mean | (ref)                                                  | 1.41x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| asyncio_tcp                      | 457 ms                                                 | 352 ms: 1.30x faster                                                  |
| async_tree_memoization_tg        | 291 ms                                                 | 279 ms: 1.04x faster                                                  |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.25 sec: 1.01x faster                                                |
| async_tree_eager_io              | 513 ms                                                 | 523 ms: 1.02x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 498 ms: 1.05x slower                                                  |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 476 ms: 1.07x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 374 ms: 1.07x slower                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 540 ms: 1.08x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 407 ms: 1.09x slower                                                  |
| async_tree_none_tg               | 198 ms                                                 | 216 ms: 1.09x slower                                                  |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 503 ms: 1.09x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 566 ms: 1.12x slower                                                  |
| async_tree_memoization           | 270 ms                                                 | 307 ms: 1.14x slower                                                  |
| async_tree_eager_memoization     | 169 ms                                                 | 194 ms: 1.15x slower                                                  |
| async_tree_none                  | 212 ms                                                 | 243 ms: 1.15x slower                                                  |
| async_generators                 | 294 ms                                                 | 345 ms: 1.17x slower                                                  |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 167 ms: 1.20x slower                                                  |
| coroutines                       | 19.8 ms                                                | 25.6 ms: 1.29x slower                                                 |
| async_tree_eager                 | 70.5 ms                                                | 110 ms: 1.57x slower                                                  |
| async_tree_eager_tg              | 48.4 ms                                                | 77.0 ms: 1.59x slower                                                 |
| asyncio_websockets               | 241 ms                                                 | 405 ms: 1.68x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.14x slower                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 284 ms                                                 | 281 ms: 1.01x faster                                                  |
| float          | 56.2 ms                                                | 103 ms: 1.84x slower                                                  |
| nbody          | 73.9 ms                                                | 158 ms: 2.13x slower                                                  |
| Geometric mean | (ref)                                                  | 1.57x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.46 ms: 1.07x faster                                                 |
| regex_dna      | 148 ms                                                 | 139 ms: 1.06x faster                                                  |
| regex_v8       | 16.9 ms                                                | 18.0 ms: 1.06x slower                                                 |
| regex_compile  | 78.5 ms                                                | 137 ms: 1.75x slower                                                  |
| Geometric mean | (ref)                                                  | 1.13x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 109 ms                                                 | 107 ms: 1.02x faster                                                  |
| xml_etree_iterparse  | 74.2 ms                                                | 84.8 ms: 1.14x slower                                                 |
| json_loads           | 16.9 us                                                | 19.5 us: 1.16x slower                                                 |
| json_dumps           | 6.56 ms                                                | 8.50 ms: 1.30x slower                                                 |
| xml_etree_generate   | 56.6 ms                                                | 77.8 ms: 1.37x slower                                                 |
| tomli_loads          | 1.56 sec                                               | 2.19 sec: 1.41x slower                                                |
| xml_etree_process    | 40.9 ms                                                | 66.5 ms: 1.63x slower                                                 |
| pickle_pure_python   | 213 us                                                 | 375 us: 1.76x slower                                                  |
| unpickle_pure_python | 163 us                                                 | 293 us: 1.79x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.37x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                | 13.6 ms: 1.01x faster                                                 |
| python_startup         | 17.0 ms                                                | 17.1 ms: 1.00x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 34.4 ms                                                | 55.9 ms: 1.63x slower                                                 |
| django_template | 22.2 ms                                                | 39.3 ms: 1.77x slower                                                 |
| genshi_text     | 16.9 ms                                                | 31.2 ms: 1.85x slower                                                 |
| mako            | 7.68 ms                                                | 14.5 ms: 1.89x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.78x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| sqlglot_normalize                | 189 ms                                                 | 121 ms: 1.56x faster                                                  |
| asyncio_tcp                      | 457 ms                                                 | 352 ms: 1.30x faster                                                  |
| gc_traversal                     | 2.48 ms                                                | 2.04 ms: 1.22x faster                                                 |
| create_gc_cycles                 | 803 us                                                 | 673 us: 1.19x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.46 ms: 1.07x faster                                                 |
| regex_dna                        | 148 ms                                                 | 139 ms: 1.06x faster                                                  |
| async_tree_memoization_tg        | 291 ms                                                 | 279 ms: 1.04x faster                                                  |
| xml_etree_parse                  | 109 ms                                                 | 107 ms: 1.02x faster                                                  |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.25 sec: 1.01x faster                                                |
| pidigits                         | 284 ms                                                 | 281 ms: 1.01x faster                                                  |
| python_startup_no_site           | 13.7 ms                                                | 13.6 ms: 1.01x faster                                                 |
| python_startup                   | 17.0 ms                                                | 17.1 ms: 1.00x slower                                                 |
| async_tree_eager_io              | 513 ms                                                 | 523 ms: 1.02x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 498 ms: 1.05x slower                                                  |
| regex_v8                         | 16.9 ms                                                | 18.0 ms: 1.06x slower                                                 |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 476 ms: 1.07x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 374 ms: 1.07x slower                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 540 ms: 1.08x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 407 ms: 1.09x slower                                                  |
| async_tree_none_tg               | 198 ms                                                 | 216 ms: 1.09x slower                                                  |
| bench_mp_pool                    | 50.9 ms                                                | 55.6 ms: 1.09x slower                                                 |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 503 ms: 1.09x slower                                                  |
| generators                       | 31.5 ms                                                | 35.1 ms: 1.12x slower                                                 |
| async_tree_io                    | 507 ms                                                 | 566 ms: 1.12x slower                                                  |
| async_tree_memoization           | 270 ms                                                 | 307 ms: 1.14x slower                                                  |
| xml_etree_iterparse              | 74.2 ms                                                | 84.8 ms: 1.14x slower                                                 |
| async_tree_eager_memoization     | 169 ms                                                 | 194 ms: 1.15x slower                                                  |
| async_tree_none                  | 212 ms                                                 | 243 ms: 1.15x slower                                                  |
| json_loads                       | 16.9 us                                                | 19.5 us: 1.16x slower                                                 |
| pathlib                          | 22.8 ms                                                | 26.6 ms: 1.17x slower                                                 |
| async_generators                 | 294 ms                                                 | 345 ms: 1.17x slower                                                  |
| json                             | 2.94 ms                                                | 3.45 ms: 1.17x slower                                                 |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 167 ms: 1.20x slower                                                  |
| deepcopy                         | 232 us                                                 | 285 us: 1.23x slower                                                  |
| telco                            | 4.80 ms                                                | 5.91 ms: 1.23x slower                                                 |
| meteor_contest                   | 73.8 ms                                                | 92.3 ms: 1.25x slower                                                 |
| mdp                              | 1.50 sec                                               | 1.88 sec: 1.25x slower                                                |
| pylint                           | 181 ms                                                 | 228 ms: 1.26x slower                                                  |
| nqueens                          | 62.9 ms                                                | 79.1 ms: 1.26x slower                                                 |
| fannkuch                         | 282 ms                                                 | 355 ms: 1.26x slower                                                  |
| coverage                         | 46.1 ms                                                | 59.2 ms: 1.28x slower                                                 |
| coroutines                       | 19.8 ms                                                | 25.6 ms: 1.29x slower                                                 |
| json_dumps                       | 6.56 ms                                                | 8.50 ms: 1.30x slower                                                 |
| docutils                         | 1.44 sec                                               | 1.88 sec: 1.30x slower                                                |
| deepcopy_memo                    | 27.2 us                                                | 36.6 us: 1.34x slower                                                 |
| bpe_tokeniser                    | 3.24 sec                                               | 4.45 sec: 1.37x slower                                                |
| xml_etree_generate               | 56.6 ms                                                | 77.8 ms: 1.37x slower                                                 |
| scimark_fft                      | 201 ms                                                 | 276 ms: 1.38x slower                                                  |
| pycparser                        | 706 ms                                                 | 974 ms: 1.38x slower                                                  |
| deepcopy_reduce                  | 2.06 us                                                | 2.87 us: 1.40x slower                                                 |
| tomli_loads                      | 1.56 sec                                               | 2.19 sec: 1.41x slower                                                |
| tornado_http                     | 77.2 ms                                                | 109 ms: 1.41x slower                                                  |
| pyflate                          | 351 ms                                                 | 498 ms: 1.42x slower                                                  |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 4.26 ms: 1.42x slower                                                 |
| sympy_integrate                  | 11.3 ms                                                | 16.3 ms: 1.44x slower                                                 |
| 2to3                             | 178 ms                                                 | 258 ms: 1.45x slower                                                  |
| crypto_pyaes                     | 54.0 ms                                                | 79.5 ms: 1.47x slower                                                 |
| html5lib                         | 36.6 ms                                                | 54.3 ms: 1.48x slower                                                 |
| dulwich_log                      | 28.7 ms                                                | 42.7 ms: 1.49x slower                                                 |
| scimark_sor                      | 106 ms                                                 | 165 ms: 1.56x slower                                                  |
| async_tree_eager                 | 70.5 ms                                                | 110 ms: 1.57x slower                                                  |
| thrift                           | 466 us                                                 | 738 us: 1.59x slower                                                  |
| async_tree_eager_tg              | 48.4 ms                                                | 77.0 ms: 1.59x slower                                                 |
| comprehensions                   | 12.2 us                                                | 19.4 us: 1.59x slower                                                 |
| bench_thread_pool                | 506 us                                                 | 811 us: 1.60x slower                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 81.3 ms: 1.61x slower                                                 |
| genshi_xml                       | 34.4 ms                                                | 55.9 ms: 1.63x slower                                                 |
| xml_etree_process                | 40.9 ms                                                | 66.5 ms: 1.63x slower                                                 |
| hexiom                           | 4.85 ms                                                | 8.06 ms: 1.66x slower                                                 |
| asyncio_websockets               | 241 ms                                                 | 405 ms: 1.68x slower                                                  |
| sympy_str                        | 145 ms                                                 | 247 ms: 1.70x slower                                                  |
| typing_runtime_protocols         | 101 us                                                 | 172 us: 1.70x slower                                                  |
| richards                         | 35.4 ms                                                | 61.8 ms: 1.74x slower                                                 |
| sqlglot_optimize                 | 34.9 ms                                                | 60.9 ms: 1.74x slower                                                 |
| regex_compile                    | 78.5 ms                                                | 137 ms: 1.75x slower                                                  |
| pprint_pformat                   | 1.08 sec                                               | 1.89 sec: 1.75x slower                                                |
| pprint_safe_repr                 | 531 ms                                                 | 930 ms: 1.75x slower                                                  |
| pickle_pure_python               | 213 us                                                 | 375 us: 1.76x slower                                                  |
| django_template                  | 22.2 ms                                                | 39.3 ms: 1.77x slower                                                 |
| go                               | 115 ms                                                 | 205 ms: 1.78x slower                                                  |
| unpickle_pure_python             | 163 us                                                 | 293 us: 1.79x slower                                                  |
| richards_super                   | 39.1 ms                                                | 70.3 ms: 1.80x slower                                                 |
| float                            | 56.2 ms                                                | 103 ms: 1.84x slower                                                  |
| logging_simple                   | 3.57 us                                                | 6.57 us: 1.84x slower                                                 |
| spectral_norm                    | 77.3 ms                                                | 143 ms: 1.85x slower                                                  |
| genshi_text                      | 16.9 ms                                                | 31.2 ms: 1.85x slower                                                 |
| logging_format                   | 3.85 us                                                | 7.12 us: 1.85x slower                                                 |
| sympy_expand                     | 246 ms                                                 | 464 ms: 1.88x slower                                                  |
| mako                             | 7.68 ms                                                | 14.5 ms: 1.89x slower                                                 |
| sympy_sum                        | 75.6 ms                                                | 145 ms: 1.92x slower                                                  |
| chaos                            | 41.3 ms                                                | 80.1 ms: 1.94x slower                                                 |
| logging_silent                   | 69.9 ns                                                | 136 ns: 1.95x slower                                                  |
| sqlglot_transpile                | 1.02 ms                                                | 2.01 ms: 1.97x slower                                                 |
| sqlglot_parse                    | 856 us                                                 | 1.75 ms: 2.05x slower                                                 |
| raytrace                         | 182 ms                                                 | 387 ms: 2.13x slower                                                  |
| nbody                            | 73.9 ms                                                | 158 ms: 2.13x slower                                                  |
| deltablue                        | 2.68 ms                                                | 5.90 ms: 2.20x slower                                                 |
| scimark_lu                       | 76.5 ms                                                | 174 ms: 2.27x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.38x slower                                                          |
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.29x
- 95% likely to have a slowdown of 1.27x
- 99% likely to have a slowdown of 1.25x

# Memory
- memory change: 0.99x