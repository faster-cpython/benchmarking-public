# Results vs. 3.13.0b2

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 315a933
- commit date: 2024-08-14
- overall geometric mean: 1.13x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: 0.46x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240814-darwin-arm64-python-main-3.14.0a0-315a933 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 161 ms                                                     | 186 ms: 1.16x slower                                  |
| docutils       | 1.44 sec                                                   | 1.70 sec: 1.19x slower                                |
| html5lib       | 31.2 ms                                                    | 35.3 ms: 1.13x slower                                 |
| tornado_http   | 66.7 ms                                                    | 70.9 ms: 1.06x slower                                 |
| Geometric mean | (ref)                                                      | 1.13x slower                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240814-darwin-arm64-python-main-3.14.0a0-315a933 |
|----------------------------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 654 ms: 1.17x faster                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 689 ms: 1.11x faster                                  |
| async_tree_io_tg                 | 565 ms                                                     | 525 ms: 1.08x faster                                  |
| async_tree_none_tg               | 198 ms                                                     | 190 ms: 1.04x faster                                  |
| async_tree_memoization           | 260 ms                                                     | 251 ms: 1.03x faster                                  |
| async_tree_none                  | 209 ms                                                     | 205 ms: 1.02x faster                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 459 ms: 1.02x faster                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 367 ms: 1.02x slower                                  |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 129 ms: 1.02x slower                                  |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 340 ms: 1.03x slower                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 44.8 ms: 1.08x slower                                 |
| async_tree_eager                 | 60.3 ms                                                    | 68.4 ms: 1.13x slower                                 |
| Geometric mean                   | (ref)                                                      | 1.01x faster                                          |

Benchmark hidden because not significant (4): async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240814-darwin-arm64-python-main-3.14.0a0-315a933 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| pidigits       | 282 ms                                                     | 283 ms: 1.00x slower                                  |
| float          | 48.6 ms                                                    | 55.5 ms: 1.14x slower                                 |
| nbody          | 59.6 ms                                                    | 75.9 ms: 1.27x slower                                 |
| Geometric mean | (ref)                                                      | 1.13x slower                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240814-darwin-arm64-python-main-3.14.0a0-315a933 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.48 ms: 1.04x faster                                 |
| regex_dna      | 149 ms                                                     | 145 ms: 1.03x faster                                  |
| regex_v8       | 17.3 ms                                                    | 16.8 ms: 1.03x faster                                 |
| regex_compile  | 68.5 ms                                                    | 94.5 ms: 1.38x slower                                 |
| Geometric mean | (ref)                                                      | 1.06x slower                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240814-darwin-arm64-python-main-3.14.0a0-315a933 |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| json_loads           | 16.8 us                                                    | 17.3 us: 1.03x slower                                 |
| xml_etree_parse      | 106 ms                                                     | 111 ms: 1.05x slower                                  |
| json_dumps           | 6.23 ms                                                    | 6.65 ms: 1.07x slower                                 |
| tomli_loads          | 1.47 sec                                                   | 1.59 sec: 1.09x slower                                |
| xml_etree_iterparse  | 71.5 ms                                                    | 78.1 ms: 1.09x slower                                 |
| xml_etree_process    | 37.1 ms                                                    | 41.9 ms: 1.13x slower                                 |
| xml_etree_generate   | 52.7 ms                                                    | 60.5 ms: 1.15x slower                                 |
| unpickle_pure_python | 141 us                                                     | 165 us: 1.18x slower                                  |
| pickle_pure_python   | 179 us                                                     | 213 us: 1.19x slower                                  |
| Geometric mean       | (ref)                                                      | 1.11x slower                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240814-darwin-arm64-python-main-3.14.0a0-315a933 |
|------------------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 16.9 ms: 1.12x slower                                 |
| python_startup_no_site | 12.3 ms                                                    | 13.9 ms: 1.13x slower                                 |
| Geometric mean         | (ref)                                                      | 1.12x slower                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240814-darwin-arm64-python-main-3.14.0a0-315a933 |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| genshi_text     | 13.9 ms                                                    | 16.4 ms: 1.18x slower                                 |
| genshi_xml      | 29.9 ms                                                    | 35.6 ms: 1.19x slower                                 |
| django_template | 19.4 ms                                                    | 24.1 ms: 1.24x slower                                 |
| mako            | 6.99 ms                                                    | 9.09 ms: 1.30x slower                                 |
| Geometric mean  | (ref)                                                      | 1.23x slower                                          |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240814-darwin-arm64-python-main-3.14.0a0-315a933 |
|----------------------------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 654 ms: 1.17x faster                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 689 ms: 1.11x faster                                  |
| deepcopy                         | 204 us                                                     | 185 us: 1.11x faster                                  |
| async_tree_io_tg                 | 565 ms                                                     | 525 ms: 1.08x faster                                  |
| deepcopy_reduce                  | 1.82 us                                                    | 1.70 us: 1.07x faster                                 |
| regex_effbot                     | 2.58 ms                                                    | 2.48 ms: 1.04x faster                                 |
| async_tree_none_tg               | 198 ms                                                     | 190 ms: 1.04x faster                                  |
| async_tree_memoization           | 260 ms                                                     | 251 ms: 1.03x faster                                  |
| regex_dna                        | 149 ms                                                     | 145 ms: 1.03x faster                                  |
| regex_v8                         | 17.3 ms                                                    | 16.8 ms: 1.03x faster                                 |
| async_tree_none                  | 209 ms                                                     | 205 ms: 1.02x faster                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 459 ms: 1.02x faster                                  |
| asyncio_websockets               | 409 ms                                                     | 408 ms: 1.00x faster                                  |
| pidigits                         | 282 ms                                                     | 283 ms: 1.00x slower                                  |
| gc_traversal                     | 2.45 ms                                                    | 2.46 ms: 1.00x slower                                 |
| create_gc_cycles                 | 897 us                                                     | 902 us: 1.01x slower                                  |
| mdp                              | 1.53 sec                                                   | 1.55 sec: 1.01x slower                                |
| thrift                           | 435 us                                                     | 442 us: 1.01x slower                                  |
| pathlib                          | 23.3 ms                                                    | 23.7 ms: 1.02x slower                                 |
| coroutines                       | 15.8 ms                                                    | 16.2 ms: 1.02x slower                                 |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 367 ms: 1.02x slower                                  |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 129 ms: 1.02x slower                                  |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 340 ms: 1.03x slower                                  |
| json_loads                       | 16.8 us                                                    | 17.3 us: 1.03x slower                                 |
| dulwich_log                      | 27.6 ms                                                    | 28.5 ms: 1.03x slower                                 |
| json                             | 2.93 ms                                                    | 3.03 ms: 1.03x slower                                 |
| async_generators                 | 281 ms                                                     | 292 ms: 1.04x slower                                  |
| xml_etree_parse                  | 106 ms                                                     | 111 ms: 1.05x slower                                  |
| logging_simple                   | 3.04 us                                                    | 3.20 us: 1.05x slower                                 |
| logging_format                   | 3.31 us                                                    | 3.50 us: 1.06x slower                                 |
| bench_mp_pool                    | 47.2 ms                                                    | 50.1 ms: 1.06x slower                                 |
| tornado_http                     | 66.7 ms                                                    | 70.9 ms: 1.06x slower                                 |
| asyncio_tcp                      | 402 ms                                                     | 430 ms: 1.07x slower                                  |
| json_dumps                       | 6.23 ms                                                    | 6.65 ms: 1.07x slower                                 |
| async_tree_eager_tg              | 41.4 ms                                                    | 44.8 ms: 1.08x slower                                 |
| tomli_loads                      | 1.47 sec                                                   | 1.59 sec: 1.09x slower                                |
| xml_etree_iterparse              | 71.5 ms                                                    | 78.1 ms: 1.09x slower                                 |
| telco                            | 4.60 ms                                                    | 5.04 ms: 1.10x slower                                 |
| deepcopy_memo                    | 22.6 us                                                    | 25.1 us: 1.11x slower                                 |
| python_startup                   | 15.2 ms                                                    | 16.9 ms: 1.12x slower                                 |
| python_startup_no_site           | 12.3 ms                                                    | 13.9 ms: 1.13x slower                                 |
| go                               | 101 ms                                                     | 114 ms: 1.13x slower                                  |
| xml_etree_process                | 37.1 ms                                                    | 41.9 ms: 1.13x slower                                 |
| html5lib                         | 31.2 ms                                                    | 35.3 ms: 1.13x slower                                 |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.46 sec: 1.13x slower                                |
| async_tree_eager                 | 60.3 ms                                                    | 68.4 ms: 1.13x slower                                 |
| float                            | 48.6 ms                                                    | 55.5 ms: 1.14x slower                                 |
| xml_etree_generate               | 52.7 ms                                                    | 60.5 ms: 1.15x slower                                 |
| 2to3                             | 161 ms                                                     | 186 ms: 1.16x slower                                  |
| bench_thread_pool                | 447 us                                                     | 519 us: 1.16x slower                                  |
| pycparser                        | 632 ms                                                     | 739 ms: 1.17x slower                                  |
| meteor_contest                   | 70.3 ms                                                    | 82.6 ms: 1.17x slower                                 |
| unpickle_pure_python             | 141 us                                                     | 165 us: 1.18x slower                                  |
| raytrace                         | 147 ms                                                     | 173 ms: 1.18x slower                                  |
| genshi_text                      | 13.9 ms                                                    | 16.4 ms: 1.18x slower                                 |
| scimark_sor                      | 94.9 ms                                                    | 112 ms: 1.19x slower                                  |
| docutils                         | 1.44 sec                                                   | 1.70 sec: 1.19x slower                                |
| sympy_expand                     | 226 ms                                                     | 268 ms: 1.19x slower                                  |
| genshi_xml                       | 29.9 ms                                                    | 35.6 ms: 1.19x slower                                 |
| pickle_pure_python               | 179 us                                                     | 213 us: 1.19x slower                                  |
| pyflate                          | 321 ms                                                     | 387 ms: 1.21x slower                                  |
| scimark_lu                       | 66.9 ms                                                    | 81.5 ms: 1.22x slower                                 |
| pylint                           | 170 ms                                                     | 208 ms: 1.22x slower                                  |
| sqlglot_normalize                | 166 ms                                                     | 204 ms: 1.23x slower                                  |
| typing_runtime_protocols         | 87.6 us                                                    | 108 us: 1.24x slower                                  |
| sqlglot_optimize                 | 30.9 ms                                                    | 38.4 ms: 1.24x slower                                 |
| django_template                  | 19.4 ms                                                    | 24.1 ms: 1.24x slower                                 |
| pprint_safe_repr                 | 465 ms                                                     | 581 ms: 1.25x slower                                  |
| scimark_fft                      | 181 ms                                                     | 226 ms: 1.25x slower                                  |
| pprint_pformat                   | 947 ms                                                     | 1.19 sec: 1.25x slower                                |
| sympy_integrate                  | 10.3 ms                                                    | 13.0 ms: 1.25x slower                                 |
| crypto_pyaes                     | 49.5 ms                                                    | 62.6 ms: 1.27x slower                                 |
| sympy_str                        | 131 ms                                                     | 166 ms: 1.27x slower                                  |
| nbody                            | 59.6 ms                                                    | 75.9 ms: 1.27x slower                                 |
| sympy_sum                        | 69.2 ms                                                    | 88.3 ms: 1.28x slower                                 |
| richards_super                   | 35.2 ms                                                    | 45.2 ms: 1.28x slower                                 |
| richards                         | 31.8 ms                                                    | 41.0 ms: 1.29x slower                                 |
| sqlglot_parse                    | 732 us                                                     | 951 us: 1.30x slower                                  |
| mako                             | 6.99 ms                                                    | 9.09 ms: 1.30x slower                                 |
| nqueens                          | 52.2 ms                                                    | 67.9 ms: 1.30x slower                                 |
| sqlglot_transpile                | 891 us                                                     | 1.16 ms: 1.30x slower                                 |
| fannkuch                         | 248 ms                                                     | 326 ms: 1.31x slower                                  |
| chaos                            | 34.0 ms                                                    | 45.7 ms: 1.34x slower                                 |
| scimark_monte_carlo              | 42.5 ms                                                    | 57.2 ms: 1.35x slower                                 |
| regex_compile                    | 68.5 ms                                                    | 94.5 ms: 1.38x slower                                 |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 3.92 ms: 1.41x slower                                 |
| spectral_norm                    | 66.4 ms                                                    | 94.3 ms: 1.42x slower                                 |
| hexiom                           | 4.06 ms                                                    | 5.79 ms: 1.43x slower                                 |
| generators                       | 22.9 ms                                                    | 32.9 ms: 1.44x slower                                 |
| logging_silent                   | 60.1 ns                                                    | 90.6 ns: 1.51x slower                                 |
| deltablue                        | 2.14 ms                                                    | 3.29 ms: 1.54x slower                                 |
| comprehensions                   | 10.2 us                                                    | 16.9 us: 1.66x slower                                 |
| Geometric mean                   | (ref)                                                      | 1.13x slower                                          |

Benchmark hidden because not significant (6): async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, coverage, asyncio_tcp_ssl, async_tree_io, async_tree_eager_memoization
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: 0.46x