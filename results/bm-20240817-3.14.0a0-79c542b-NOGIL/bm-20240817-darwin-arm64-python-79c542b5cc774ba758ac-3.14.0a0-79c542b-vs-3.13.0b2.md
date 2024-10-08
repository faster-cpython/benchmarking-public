# Results vs. 3.13.0b2

- fork: python
- ref: 79c542b5cc774ba758ac
- machine: darwin-arm64
- commit hash: 79c542b
- commit date: 2024-08-17
- overall geometric mean: 1.49x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x slower
- Memory change: 0.48x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 258 ms: 1.60x slower                                                  |
| docutils       | 1.44 sec                                                   | 1.88 sec: 1.31x slower                                                |
| html5lib       | 31.2 ms                                                    | 54.3 ms: 1.74x slower                                                 |
| tornado_http   | 66.7 ms                                                    | 109 ms: 1.63x slower                                                  |
| Geometric mean | (ref)                                                      | 1.56x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io_tg           | 768 ms                                                     | 498 ms: 1.54x faster                                                  |
| async_tree_eager_io              | 766 ms                                                     | 523 ms: 1.46x faster                                                  |
| async_tree_io_tg                 | 565 ms                                                     | 540 ms: 1.05x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 476 ms: 1.06x slower                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 503 ms: 1.08x slower                                                  |
| async_tree_none_tg               | 198 ms                                                     | 216 ms: 1.09x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 374 ms: 1.13x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 407 ms: 1.14x slower                                                  |
| async_tree_none                  | 209 ms                                                     | 243 ms: 1.16x slower                                                  |
| async_tree_memoization_tg        | 240 ms                                                     | 279 ms: 1.16x slower                                                  |
| async_tree_memoization           | 260 ms                                                     | 307 ms: 1.18x slower                                                  |
| async_tree_eager_memoization     | 152 ms                                                     | 194 ms: 1.28x slower                                                  |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 167 ms: 1.33x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 110 ms: 1.83x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 77.0 ms: 1.86x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.12x slower                                                          |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 282 ms                                                     | 281 ms: 1.00x faster                                                  |
| float          | 48.6 ms                                                    | 103 ms: 2.13x slower                                                  |
| nbody          | 59.6 ms                                                    | 158 ms: 2.65x slower                                                  |
| Geometric mean | (ref)                                                      | 1.78x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 149 ms                                                     | 139 ms: 1.07x faster                                                  |
| regex_effbot   | 2.58 ms                                                    | 2.46 ms: 1.05x faster                                                 |
| regex_v8       | 17.3 ms                                                    | 18.0 ms: 1.04x slower                                                 |
| regex_compile  | 68.5 ms                                                    | 137 ms: 2.00x slower                                                  |
| Geometric mean | (ref)                                                      | 1.17x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 106 ms                                                     | 107 ms: 1.01x slower                                                  |
| json_loads           | 16.8 us                                                    | 19.5 us: 1.16x slower                                                 |
| xml_etree_iterparse  | 71.5 ms                                                    | 84.8 ms: 1.19x slower                                                 |
| json_dumps           | 6.23 ms                                                    | 8.50 ms: 1.36x slower                                                 |
| xml_etree_generate   | 52.7 ms                                                    | 77.8 ms: 1.48x slower                                                 |
| tomli_loads          | 1.47 sec                                                   | 2.19 sec: 1.49x slower                                                |
| xml_etree_process    | 37.1 ms                                                    | 66.5 ms: 1.80x slower                                                 |
| unpickle_pure_python | 141 us                                                     | 293 us: 2.08x slower                                                  |
| pickle_pure_python   | 179 us                                                     | 375 us: 2.10x slower                                                  |
| Geometric mean       | (ref)                                                      | 1.47x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 12.3 ms                                                    | 13.6 ms: 1.10x slower                                                 |
| python_startup         | 15.2 ms                                                    | 17.1 ms: 1.13x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.12x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 29.9 ms                                                    | 55.9 ms: 1.87x slower                                                 |
| django_template | 19.4 ms                                                    | 39.3 ms: 2.03x slower                                                 |
| mako            | 6.99 ms                                                    | 14.5 ms: 2.08x slower                                                 |
| genshi_text     | 13.9 ms                                                    | 31.2 ms: 2.24x slower                                                 |
| Geometric mean  | (ref)                                                      | 2.05x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io_tg           | 768 ms                                                     | 498 ms: 1.54x faster                                                  |
| async_tree_eager_io              | 766 ms                                                     | 523 ms: 1.46x faster                                                  |
| sqlglot_normalize                | 166 ms                                                     | 121 ms: 1.37x faster                                                  |
| create_gc_cycles                 | 897 us                                                     | 673 us: 1.33x faster                                                  |
| gc_traversal                     | 2.45 ms                                                    | 2.04 ms: 1.20x faster                                                 |
| asyncio_tcp                      | 402 ms                                                     | 352 ms: 1.14x faster                                                  |
| regex_dna                        | 149 ms                                                     | 139 ms: 1.07x faster                                                  |
| regex_effbot                     | 2.58 ms                                                    | 2.46 ms: 1.05x faster                                                 |
| async_tree_io_tg                 | 565 ms                                                     | 540 ms: 1.05x faster                                                  |
| asyncio_tcp_ssl                  | 1.29 sec                                                   | 1.25 sec: 1.03x faster                                                |
| asyncio_websockets               | 409 ms                                                     | 405 ms: 1.01x faster                                                  |
| pidigits                         | 282 ms                                                     | 281 ms: 1.00x faster                                                  |
| xml_etree_parse                  | 106 ms                                                     | 107 ms: 1.01x slower                                                  |
| regex_v8                         | 17.3 ms                                                    | 18.0 ms: 1.04x slower                                                 |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 476 ms: 1.06x slower                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 503 ms: 1.08x slower                                                  |
| async_tree_none_tg               | 198 ms                                                     | 216 ms: 1.09x slower                                                  |
| python_startup_no_site           | 12.3 ms                                                    | 13.6 ms: 1.10x slower                                                 |
| python_startup                   | 15.2 ms                                                    | 17.1 ms: 1.13x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 374 ms: 1.13x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 407 ms: 1.14x slower                                                  |
| pathlib                          | 23.3 ms                                                    | 26.6 ms: 1.14x slower                                                 |
| json_loads                       | 16.8 us                                                    | 19.5 us: 1.16x slower                                                 |
| async_tree_none                  | 209 ms                                                     | 243 ms: 1.16x slower                                                  |
| async_tree_memoization_tg        | 240 ms                                                     | 279 ms: 1.16x slower                                                  |
| json                             | 2.93 ms                                                    | 3.45 ms: 1.18x slower                                                 |
| bench_mp_pool                    | 47.2 ms                                                    | 55.6 ms: 1.18x slower                                                 |
| async_tree_memoization           | 260 ms                                                     | 307 ms: 1.18x slower                                                  |
| xml_etree_iterparse              | 71.5 ms                                                    | 84.8 ms: 1.19x slower                                                 |
| mdp                              | 1.53 sec                                                   | 1.88 sec: 1.23x slower                                                |
| async_generators                 | 281 ms                                                     | 345 ms: 1.23x slower                                                  |
| async_tree_eager_memoization     | 152 ms                                                     | 194 ms: 1.28x slower                                                  |
| telco                            | 4.60 ms                                                    | 5.91 ms: 1.28x slower                                                 |
| docutils                         | 1.44 sec                                                   | 1.88 sec: 1.31x slower                                                |
| meteor_contest                   | 70.3 ms                                                    | 92.3 ms: 1.31x slower                                                 |
| coverage                         | 45.0 ms                                                    | 59.2 ms: 1.32x slower                                                 |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 167 ms: 1.33x slower                                                  |
| pylint                           | 170 ms                                                     | 228 ms: 1.34x slower                                                  |
| json_dumps                       | 6.23 ms                                                    | 8.50 ms: 1.36x slower                                                 |
| deepcopy                         | 204 us                                                     | 285 us: 1.40x slower                                                  |
| fannkuch                         | 248 ms                                                     | 355 ms: 1.43x slower                                                  |
| bpe_tokeniser                    | 3.05 sec                                                   | 4.45 sec: 1.46x slower                                                |
| xml_etree_generate               | 52.7 ms                                                    | 77.8 ms: 1.48x slower                                                 |
| tomli_loads                      | 1.47 sec                                                   | 2.19 sec: 1.49x slower                                                |
| nqueens                          | 52.2 ms                                                    | 79.1 ms: 1.51x slower                                                 |
| scimark_fft                      | 181 ms                                                     | 276 ms: 1.53x slower                                                  |
| generators                       | 22.9 ms                                                    | 35.1 ms: 1.53x slower                                                 |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 4.26 ms: 1.54x slower                                                 |
| pycparser                        | 632 ms                                                     | 974 ms: 1.54x slower                                                  |
| dulwich_log                      | 27.6 ms                                                    | 42.7 ms: 1.55x slower                                                 |
| pyflate                          | 321 ms                                                     | 498 ms: 1.55x slower                                                  |
| sympy_integrate                  | 10.3 ms                                                    | 16.3 ms: 1.57x slower                                                 |
| deepcopy_reduce                  | 1.82 us                                                    | 2.87 us: 1.58x slower                                                 |
| 2to3                             | 161 ms                                                     | 258 ms: 1.60x slower                                                  |
| crypto_pyaes                     | 49.5 ms                                                    | 79.5 ms: 1.61x slower                                                 |
| coroutines                       | 15.8 ms                                                    | 25.6 ms: 1.62x slower                                                 |
| deepcopy_memo                    | 22.6 us                                                    | 36.6 us: 1.62x slower                                                 |
| tornado_http                     | 66.7 ms                                                    | 109 ms: 1.63x slower                                                  |
| thrift                           | 435 us                                                     | 738 us: 1.70x slower                                                  |
| scimark_sor                      | 94.9 ms                                                    | 165 ms: 1.74x slower                                                  |
| html5lib                         | 31.2 ms                                                    | 54.3 ms: 1.74x slower                                                 |
| xml_etree_process                | 37.1 ms                                                    | 66.5 ms: 1.80x slower                                                 |
| bench_thread_pool                | 447 us                                                     | 811 us: 1.82x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 110 ms: 1.83x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 77.0 ms: 1.86x slower                                                 |
| genshi_xml                       | 29.9 ms                                                    | 55.9 ms: 1.87x slower                                                 |
| sympy_str                        | 131 ms                                                     | 247 ms: 1.88x slower                                                  |
| comprehensions                   | 10.2 us                                                    | 19.4 us: 1.91x slower                                                 |
| scimark_monte_carlo              | 42.5 ms                                                    | 81.3 ms: 1.92x slower                                                 |
| richards                         | 31.8 ms                                                    | 61.8 ms: 1.94x slower                                                 |
| typing_runtime_protocols         | 87.6 us                                                    | 172 us: 1.97x slower                                                  |
| sqlglot_optimize                 | 30.9 ms                                                    | 60.9 ms: 1.97x slower                                                 |
| hexiom                           | 4.06 ms                                                    | 8.06 ms: 1.99x slower                                                 |
| pprint_pformat                   | 947 ms                                                     | 1.89 sec: 1.99x slower                                                |
| richards_super                   | 35.2 ms                                                    | 70.3 ms: 2.00x slower                                                 |
| pprint_safe_repr                 | 465 ms                                                     | 930 ms: 2.00x slower                                                  |
| regex_compile                    | 68.5 ms                                                    | 137 ms: 2.00x slower                                                  |
| django_template                  | 19.4 ms                                                    | 39.3 ms: 2.03x slower                                                 |
| go                               | 101 ms                                                     | 205 ms: 2.04x slower                                                  |
| sympy_expand                     | 226 ms                                                     | 464 ms: 2.05x slower                                                  |
| unpickle_pure_python             | 141 us                                                     | 293 us: 2.08x slower                                                  |
| mako                             | 6.99 ms                                                    | 14.5 ms: 2.08x slower                                                 |
| sympy_sum                        | 69.2 ms                                                    | 145 ms: 2.10x slower                                                  |
| pickle_pure_python               | 179 us                                                     | 375 us: 2.10x slower                                                  |
| float                            | 48.6 ms                                                    | 103 ms: 2.13x slower                                                  |
| spectral_norm                    | 66.4 ms                                                    | 143 ms: 2.15x slower                                                  |
| logging_format                   | 3.31 us                                                    | 7.12 us: 2.15x slower                                                 |
| logging_simple                   | 3.04 us                                                    | 6.57 us: 2.16x slower                                                 |
| genshi_text                      | 13.9 ms                                                    | 31.2 ms: 2.24x slower                                                 |
| sqlglot_transpile                | 891 us                                                     | 2.01 ms: 2.26x slower                                                 |
| logging_silent                   | 60.1 ns                                                    | 136 ns: 2.27x slower                                                  |
| chaos                            | 34.0 ms                                                    | 80.1 ms: 2.36x slower                                                 |
| sqlglot_parse                    | 732 us                                                     | 1.75 ms: 2.39x slower                                                 |
| scimark_lu                       | 66.9 ms                                                    | 174 ms: 2.60x slower                                                  |
| raytrace                         | 147 ms                                                     | 387 ms: 2.63x slower                                                  |
| nbody                            | 59.6 ms                                                    | 158 ms: 2.65x slower                                                  |
| deltablue                        | 2.14 ms                                                    | 5.90 ms: 2.76x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.49x slower                                                          |

Benchmark hidden because not significant (1): async_tree_io
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.32x
- 95% likely to have a slowdown of 1.30x
- 99% likely to have a slowdown of 1.24x

# Memory
- memory change: 0.48x