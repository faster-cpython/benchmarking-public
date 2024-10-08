# Results vs. 3.13.0b2

- fork: python
- ref: a2bec77d25b11f50362a
- machine: darwin-arm64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.42x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 250 ms: 1.56x slower                                                  |
| docutils       | 1.44 sec                                                   | 1.80 sec: 1.25x slower                                                |
| html5lib       | 31.2 ms                                                    | 52.4 ms: 1.68x slower                                                 |
| tornado_http   | 66.7 ms                                                    | 96.0 ms: 1.44x slower                                                 |
| Geometric mean | (ref)                                                      | 1.47x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io_tg           | 768 ms                                                     | 468 ms: 1.64x faster                                                  |
| async_tree_eager_io              | 766 ms                                                     | 493 ms: 1.55x faster                                                  |
| async_tree_io_tg                 | 565 ms                                                     | 507 ms: 1.11x faster                                                  |
| async_tree_io                    | 563 ms                                                     | 538 ms: 1.05x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 465 ms: 1.03x slower                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 491 ms: 1.05x slower                                                  |
| async_tree_none_tg               | 198 ms                                                     | 208 ms: 1.05x slower                                                  |
| async_tree_memoization_tg        | 240 ms                                                     | 265 ms: 1.11x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 367 ms: 1.11x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 398 ms: 1.11x slower                                                  |
| async_tree_none                  | 209 ms                                                     | 235 ms: 1.12x slower                                                  |
| async_tree_memoization           | 260 ms                                                     | 292 ms: 1.13x slower                                                  |
| async_tree_eager_memoization     | 152 ms                                                     | 185 ms: 1.22x slower                                                  |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 158 ms: 1.26x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 106 ms: 1.75x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 74.0 ms: 1.79x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.08x slower                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 282 ms                                                     | 281 ms: 1.00x faster                                                  |
| float          | 48.6 ms                                                    | 96.6 ms: 1.99x slower                                                 |
| nbody          | 59.6 ms                                                    | 159 ms: 2.67x slower                                                  |
| Geometric mean | (ref)                                                      | 1.74x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 149 ms                                                     | 139 ms: 1.07x faster                                                  |
| regex_effbot   | 2.58 ms                                                    | 2.43 ms: 1.06x faster                                                 |
| regex_v8       | 17.3 ms                                                    | 17.5 ms: 1.02x slower                                                 |
| regex_compile  | 68.5 ms                                                    | 125 ms: 1.82x slower                                                  |
| Geometric mean | (ref)                                                      | 1.13x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 106 ms                                                     | 98.9 ms: 1.07x faster                                                 |
| xml_etree_iterparse  | 71.5 ms                                                    | 76.8 ms: 1.07x slower                                                 |
| json_loads           | 16.8 us                                                    | 19.3 us: 1.15x slower                                                 |
| json_dumps           | 6.23 ms                                                    | 8.14 ms: 1.31x slower                                                 |
| xml_etree_generate   | 52.7 ms                                                    | 70.7 ms: 1.34x slower                                                 |
| tomli_loads          | 1.47 sec                                                   | 2.06 sec: 1.41x slower                                                |
| xml_etree_process    | 37.1 ms                                                    | 60.9 ms: 1.64x slower                                                 |
| unpickle_pure_python | 141 us                                                     | 269 us: 1.91x slower                                                  |
| pickle_pure_python   | 179 us                                                     | 346 us: 1.94x slower                                                  |
| Geometric mean       | (ref)                                                      | 1.37x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 12.3 ms                                                    | 14.0 ms: 1.14x slower                                                 |
| python_startup         | 15.2 ms                                                    | 17.3 ms: 1.14x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.14x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 29.9 ms                                                    | 51.6 ms: 1.73x slower                                                 |
| django_template | 19.4 ms                                                    | 35.9 ms: 1.85x slower                                                 |
| genshi_text     | 13.9 ms                                                    | 25.8 ms: 1.85x slower                                                 |
| mako            | 6.99 ms                                                    | 13.4 ms: 1.92x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.84x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io_tg           | 768 ms                                                     | 468 ms: 1.64x faster                                                  |
| async_tree_eager_io              | 766 ms                                                     | 493 ms: 1.55x faster                                                  |
| sqlglot_normalize                | 166 ms                                                     | 109 ms: 1.52x faster                                                  |
| create_gc_cycles                 | 897 us                                                     | 665 us: 1.35x faster                                                  |
| gc_traversal                     | 2.45 ms                                                    | 2.11 ms: 1.16x faster                                                 |
| asyncio_tcp                      | 402 ms                                                     | 353 ms: 1.14x faster                                                  |
| async_tree_io_tg                 | 565 ms                                                     | 507 ms: 1.11x faster                                                  |
| regex_dna                        | 149 ms                                                     | 139 ms: 1.07x faster                                                  |
| xml_etree_parse                  | 106 ms                                                     | 98.9 ms: 1.07x faster                                                 |
| regex_effbot                     | 2.58 ms                                                    | 2.43 ms: 1.06x faster                                                 |
| async_tree_io                    | 563 ms                                                     | 538 ms: 1.05x faster                                                  |
| asyncio_tcp_ssl                  | 1.29 sec                                                   | 1.24 sec: 1.04x faster                                                |
| asyncio_websockets               | 409 ms                                                     | 406 ms: 1.01x faster                                                  |
| pidigits                         | 282 ms                                                     | 281 ms: 1.00x faster                                                  |
| regex_v8                         | 17.3 ms                                                    | 17.5 ms: 1.02x slower                                                 |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 465 ms: 1.03x slower                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 491 ms: 1.05x slower                                                  |
| async_tree_none_tg               | 198 ms                                                     | 208 ms: 1.05x slower                                                  |
| xml_etree_iterparse              | 71.5 ms                                                    | 76.8 ms: 1.07x slower                                                 |
| async_tree_memoization_tg        | 240 ms                                                     | 265 ms: 1.11x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 367 ms: 1.11x slower                                                  |
| pathlib                          | 23.3 ms                                                    | 25.9 ms: 1.11x slower                                                 |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 398 ms: 1.11x slower                                                  |
| async_tree_none                  | 209 ms                                                     | 235 ms: 1.12x slower                                                  |
| async_tree_memoization           | 260 ms                                                     | 292 ms: 1.13x slower                                                  |
| python_startup_no_site           | 12.3 ms                                                    | 14.0 ms: 1.14x slower                                                 |
| python_startup                   | 15.2 ms                                                    | 17.3 ms: 1.14x slower                                                 |
| json_loads                       | 16.8 us                                                    | 19.3 us: 1.15x slower                                                 |
| bench_mp_pool                    | 47.2 ms                                                    | 54.6 ms: 1.16x slower                                                 |
| json                             | 2.93 ms                                                    | 3.42 ms: 1.17x slower                                                 |
| telco                            | 4.60 ms                                                    | 5.53 ms: 1.20x slower                                                 |
| async_tree_eager_memoization     | 152 ms                                                     | 185 ms: 1.22x slower                                                  |
| async_generators                 | 281 ms                                                     | 343 ms: 1.22x slower                                                  |
| mdp                              | 1.53 sec                                                   | 1.88 sec: 1.23x slower                                                |
| deepcopy                         | 204 us                                                     | 252 us: 1.24x slower                                                  |
| docutils                         | 1.44 sec                                                   | 1.80 sec: 1.25x slower                                                |
| coverage                         | 45.0 ms                                                    | 56.5 ms: 1.26x slower                                                 |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 158 ms: 1.26x slower                                                  |
| pylint                           | 170 ms                                                     | 218 ms: 1.28x slower                                                  |
| meteor_contest                   | 70.3 ms                                                    | 91.5 ms: 1.30x slower                                                 |
| json_dumps                       | 6.23 ms                                                    | 8.14 ms: 1.31x slower                                                 |
| xml_etree_generate               | 52.7 ms                                                    | 70.7 ms: 1.34x slower                                                 |
| bpe_tokeniser                    | 3.05 sec                                                   | 4.12 sec: 1.35x slower                                                |
| deepcopy_memo                    | 22.6 us                                                    | 30.9 us: 1.37x slower                                                 |
| deepcopy_reduce                  | 1.82 us                                                    | 2.55 us: 1.40x slower                                                 |
| tomli_loads                      | 1.47 sec                                                   | 2.06 sec: 1.41x slower                                                |
| tornado_http                     | 66.7 ms                                                    | 96.0 ms: 1.44x slower                                                 |
| fannkuch                         | 248 ms                                                     | 359 ms: 1.45x slower                                                  |
| coroutines                       | 15.8 ms                                                    | 23.1 ms: 1.46x slower                                                 |
| pyflate                          | 321 ms                                                     | 482 ms: 1.50x slower                                                  |
| pycparser                        | 632 ms                                                     | 955 ms: 1.51x slower                                                  |
| nqueens                          | 52.2 ms                                                    | 79.2 ms: 1.52x slower                                                 |
| sympy_integrate                  | 10.3 ms                                                    | 15.8 ms: 1.52x slower                                                 |
| scimark_fft                      | 181 ms                                                     | 277 ms: 1.53x slower                                                  |
| 2to3                             | 161 ms                                                     | 250 ms: 1.56x slower                                                  |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 4.35 ms: 1.57x slower                                                 |
| crypto_pyaes                     | 49.5 ms                                                    | 79.5 ms: 1.61x slower                                                 |
| generators                       | 22.9 ms                                                    | 37.0 ms: 1.61x slower                                                 |
| thrift                           | 435 us                                                     | 706 us: 1.62x slower                                                  |
| xml_etree_process                | 37.1 ms                                                    | 60.9 ms: 1.64x slower                                                 |
| html5lib                         | 31.2 ms                                                    | 52.4 ms: 1.68x slower                                                 |
| scimark_sor                      | 94.9 ms                                                    | 160 ms: 1.69x slower                                                  |
| typing_runtime_protocols         | 87.6 us                                                    | 149 us: 1.70x slower                                                  |
| genshi_xml                       | 29.9 ms                                                    | 51.6 ms: 1.73x slower                                                 |
| async_tree_eager                 | 60.3 ms                                                    | 106 ms: 1.75x slower                                                  |
| sqlglot_optimize                 | 30.9 ms                                                    | 54.4 ms: 1.76x slower                                                 |
| bench_thread_pool                | 447 us                                                     | 790 us: 1.77x slower                                                  |
| richards                         | 31.8 ms                                                    | 56.8 ms: 1.78x slower                                                 |
| async_tree_eager_tg              | 41.4 ms                                                    | 74.0 ms: 1.79x slower                                                 |
| sympy_str                        | 131 ms                                                     | 238 ms: 1.81x slower                                                  |
| regex_compile                    | 68.5 ms                                                    | 125 ms: 1.82x slower                                                  |
| pprint_pformat                   | 947 ms                                                     | 1.73 sec: 1.83x slower                                                |
| pprint_safe_repr                 | 465 ms                                                     | 851 ms: 1.83x slower                                                  |
| spectral_norm                    | 66.4 ms                                                    | 122 ms: 1.83x slower                                                  |
| django_template                  | 19.4 ms                                                    | 35.9 ms: 1.85x slower                                                 |
| genshi_text                      | 13.9 ms                                                    | 25.8 ms: 1.85x slower                                                 |
| richards_super                   | 35.2 ms                                                    | 66.5 ms: 1.89x slower                                                 |
| scimark_monte_carlo              | 42.5 ms                                                    | 80.5 ms: 1.89x slower                                                 |
| comprehensions                   | 10.2 us                                                    | 19.3 us: 1.90x slower                                                 |
| unpickle_pure_python             | 141 us                                                     | 269 us: 1.91x slower                                                  |
| mako                             | 6.99 ms                                                    | 13.4 ms: 1.92x slower                                                 |
| pickle_pure_python               | 179 us                                                     | 346 us: 1.94x slower                                                  |
| sympy_expand                     | 226 ms                                                     | 444 ms: 1.97x slower                                                  |
| hexiom                           | 4.06 ms                                                    | 8.02 ms: 1.98x slower                                                 |
| float                            | 48.6 ms                                                    | 96.6 ms: 1.99x slower                                                 |
| go                               | 101 ms                                                     | 200 ms: 1.99x slower                                                  |
| logging_simple                   | 3.04 us                                                    | 6.16 us: 2.02x slower                                                 |
| logging_format                   | 3.31 us                                                    | 6.72 us: 2.03x slower                                                 |
| sympy_sum                        | 69.2 ms                                                    | 141 ms: 2.04x slower                                                  |
| sqlglot_transpile                | 891 us                                                     | 1.95 ms: 2.19x slower                                                 |
| logging_silent                   | 60.1 ns                                                    | 135 ns: 2.24x slower                                                  |
| chaos                            | 34.0 ms                                                    | 76.5 ms: 2.25x slower                                                 |
| sqlglot_parse                    | 732 us                                                     | 1.71 ms: 2.33x slower                                                 |
| scimark_lu                       | 66.9 ms                                                    | 159 ms: 2.38x slower                                                  |
| raytrace                         | 147 ms                                                     | 373 ms: 2.54x slower                                                  |
| nbody                            | 59.6 ms                                                    | 159 ms: 2.67x slower                                                  |
| deltablue                        | 2.14 ms                                                    | 5.76 ms: 2.69x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.42x slower                                                          |
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.26x
- 95% likely to have a slowdown of 1.25x
- 99% likely to have a slowdown of 1.22x

# Memory
- memory change: 1.10x