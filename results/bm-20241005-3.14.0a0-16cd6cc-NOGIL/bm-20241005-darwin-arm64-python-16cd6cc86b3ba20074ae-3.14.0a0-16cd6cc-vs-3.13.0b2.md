# Results vs. 3.13.0b2

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: darwin-arm64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.37x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x slower
- Memory change: 0.53x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 249 ms: 1.55x slower                                                  |
| docutils       | 1.44 sec                                                   | 1.76 sec: 1.23x slower                                                |
| html5lib       | 31.2 ms                                                    | 53.2 ms: 1.71x slower                                                 |
| tornado_http   | 66.7 ms                                                    | 104 ms: 1.57x slower                                                  |
| Geometric mean | (ref)                                                      | 1.50x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io_tg           | 768 ms                                                     | 465 ms: 1.65x faster                                                  |
| async_tree_eager_io              | 766 ms                                                     | 490 ms: 1.56x faster                                                  |
| async_tree_io_tg                 | 565 ms                                                     | 501 ms: 1.13x faster                                                  |
| async_tree_io                    | 563 ms                                                     | 530 ms: 1.06x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 466 ms: 1.03x slower                                                  |
| async_tree_none_tg               | 198 ms                                                     | 207 ms: 1.05x slower                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 490 ms: 1.05x slower                                                  |
| async_tree_memoization_tg        | 240 ms                                                     | 266 ms: 1.11x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 398 ms: 1.11x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 370 ms: 1.12x slower                                                  |
| async_tree_none                  | 209 ms                                                     | 235 ms: 1.12x slower                                                  |
| async_tree_memoization           | 260 ms                                                     | 292 ms: 1.13x slower                                                  |
| async_tree_eager_memoization     | 152 ms                                                     | 187 ms: 1.23x slower                                                  |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 162 ms: 1.29x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 106 ms: 1.75x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 75.5 ms: 1.83x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.08x slower                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 282 ms                                                     | 281 ms: 1.00x faster                                                  |
| float          | 48.6 ms                                                    | 93.0 ms: 1.91x slower                                                 |
| nbody          | 59.6 ms                                                    | 154 ms: 2.59x slower                                                  |
| Geometric mean | (ref)                                                      | 1.70x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.51 ms: 1.03x faster                                                 |
| regex_dna      | 149 ms                                                     | 146 ms: 1.02x faster                                                  |
| regex_v8       | 17.3 ms                                                    | 17.4 ms: 1.01x slower                                                 |
| regex_compile  | 68.5 ms                                                    | 119 ms: 1.74x slower                                                  |
| Geometric mean | (ref)                                                      | 1.14x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle               | 7.48 us                                                    | 7.03 us: 1.06x faster                                                 |
| xml_etree_parse      | 106 ms                                                     | 104 ms: 1.01x faster                                                  |
| pickle_list          | 2.96 us                                                    | 2.97 us: 1.00x slower                                                 |
| pickle_dict          | 18.3 us                                                    | 18.5 us: 1.01x slower                                                 |
| unpickle             | 9.12 us                                                    | 9.46 us: 1.04x slower                                                 |
| xml_etree_iterparse  | 71.5 ms                                                    | 75.9 ms: 1.06x slower                                                 |
| json_loads           | 16.8 us                                                    | 18.5 us: 1.10x slower                                                 |
| unpickle_list        | 2.88 us                                                    | 3.26 us: 1.13x slower                                                 |
| json_dumps           | 6.23 ms                                                    | 7.91 ms: 1.27x slower                                                 |
| xml_etree_generate   | 52.7 ms                                                    | 67.9 ms: 1.29x slower                                                 |
| tomli_loads          | 1.47 sec                                                   | 1.99 sec: 1.36x slower                                                |
| xml_etree_process    | 37.1 ms                                                    | 56.3 ms: 1.52x slower                                                 |
| unpickle_pure_python | 141 us                                                     | 262 us: 1.86x slower                                                  |
| pickle_pure_python   | 179 us                                                     | 346 us: 1.94x slower                                                  |
| Geometric mean       | (ref)                                                      | 1.22x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 12.3 ms                                                    | 13.9 ms: 1.13x slower                                                 |
| python_startup         | 15.2 ms                                                    | 17.4 ms: 1.15x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.14x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 29.9 ms                                                    | 49.8 ms: 1.66x slower                                                 |
| genshi_text     | 13.9 ms                                                    | 24.7 ms: 1.77x slower                                                 |
| django_template | 19.4 ms                                                    | 36.1 ms: 1.86x slower                                                 |
| mako            | 6.99 ms                                                    | 13.3 ms: 1.91x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.80x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| asyncio_websockets               | 409 ms                                                     | 239 ms: 1.71x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 465 ms: 1.65x faster                                                  |
| sqlglot_normalize                | 166 ms                                                     | 103 ms: 1.61x faster                                                  |
| async_tree_eager_io              | 766 ms                                                     | 490 ms: 1.56x faster                                                  |
| create_gc_cycles                 | 897 us                                                     | 679 us: 1.32x faster                                                  |
| gc_traversal                     | 2.45 ms                                                    | 2.05 ms: 1.19x faster                                                 |
| async_tree_io_tg                 | 565 ms                                                     | 501 ms: 1.13x faster                                                  |
| pickle                           | 7.48 us                                                    | 7.03 us: 1.06x faster                                                 |
| async_tree_io                    | 563 ms                                                     | 530 ms: 1.06x faster                                                  |
| asyncio_tcp_ssl                  | 1.29 sec                                                   | 1.23 sec: 1.05x faster                                                |
| regex_effbot                     | 2.58 ms                                                    | 2.51 ms: 1.03x faster                                                 |
| regex_dna                        | 149 ms                                                     | 146 ms: 1.02x faster                                                  |
| sqlite_synth                     | 1.55 us                                                    | 1.52 us: 1.02x faster                                                 |
| xml_etree_parse                  | 106 ms                                                     | 104 ms: 1.01x faster                                                  |
| pidigits                         | 282 ms                                                     | 281 ms: 1.00x faster                                                  |
| pickle_list                      | 2.96 us                                                    | 2.97 us: 1.00x slower                                                 |
| regex_v8                         | 17.3 ms                                                    | 17.4 ms: 1.01x slower                                                 |
| pickle_dict                      | 18.3 us                                                    | 18.5 us: 1.01x slower                                                 |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 466 ms: 1.03x slower                                                  |
| unpickle                         | 9.12 us                                                    | 9.46 us: 1.04x slower                                                 |
| async_tree_none_tg               | 198 ms                                                     | 207 ms: 1.05x slower                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 490 ms: 1.05x slower                                                  |
| xml_etree_iterparse              | 71.5 ms                                                    | 75.9 ms: 1.06x slower                                                 |
| pathlib                          | 23.3 ms                                                    | 25.1 ms: 1.08x slower                                                 |
| json_loads                       | 16.8 us                                                    | 18.5 us: 1.10x slower                                                 |
| async_tree_memoization_tg        | 240 ms                                                     | 266 ms: 1.11x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 398 ms: 1.11x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 370 ms: 1.12x slower                                                  |
| async_tree_none                  | 209 ms                                                     | 235 ms: 1.12x slower                                                  |
| async_tree_memoization           | 260 ms                                                     | 292 ms: 1.13x slower                                                  |
| unpickle_list                    | 2.88 us                                                    | 3.26 us: 1.13x slower                                                 |
| python_startup_no_site           | 12.3 ms                                                    | 13.9 ms: 1.13x slower                                                 |
| json                             | 2.93 ms                                                    | 3.33 ms: 1.14x slower                                                 |
| python_startup                   | 15.2 ms                                                    | 17.4 ms: 1.15x slower                                                 |
| telco                            | 4.60 ms                                                    | 5.42 ms: 1.18x slower                                                 |
| async_generators                 | 281 ms                                                     | 332 ms: 1.18x slower                                                  |
| deepcopy                         | 204 us                                                     | 243 us: 1.19x slower                                                  |
| coverage                         | 45.0 ms                                                    | 54.4 ms: 1.21x slower                                                 |
| bench_mp_pool                    | 47.2 ms                                                    | 57.2 ms: 1.21x slower                                                 |
| mdp                              | 1.53 sec                                                   | 1.88 sec: 1.23x slower                                                |
| docutils                         | 1.44 sec                                                   | 1.76 sec: 1.23x slower                                                |
| async_tree_eager_memoization     | 152 ms                                                     | 187 ms: 1.23x slower                                                  |
| meteor_contest                   | 70.3 ms                                                    | 88.9 ms: 1.26x slower                                                 |
| json_dumps                       | 6.23 ms                                                    | 7.91 ms: 1.27x slower                                                 |
| pylint                           | 170 ms                                                     | 217 ms: 1.28x slower                                                  |
| xml_etree_generate               | 52.7 ms                                                    | 67.9 ms: 1.29x slower                                                 |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 162 ms: 1.29x slower                                                  |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.97 sec: 1.30x slower                                                |
| deepcopy_reduce                  | 1.82 us                                                    | 2.45 us: 1.34x slower                                                 |
| deepcopy_memo                    | 22.6 us                                                    | 30.6 us: 1.35x slower                                                 |
| tomli_loads                      | 1.47 sec                                                   | 1.99 sec: 1.36x slower                                                |
| fannkuch                         | 248 ms                                                     | 354 ms: 1.43x slower                                                  |
| pycparser                        | 632 ms                                                     | 915 ms: 1.45x slower                                                  |
| nqueens                          | 52.2 ms                                                    | 76.4 ms: 1.46x slower                                                 |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 4.07 ms: 1.47x slower                                                 |
| scimark_fft                      | 181 ms                                                     | 266 ms: 1.47x slower                                                  |
| dulwich_log                      | 27.6 ms                                                    | 40.9 ms: 1.49x slower                                                 |
| xml_etree_process                | 37.1 ms                                                    | 56.3 ms: 1.52x slower                                                 |
| pyflate                          | 321 ms                                                     | 490 ms: 1.53x slower                                                  |
| generators                       | 22.9 ms                                                    | 35.0 ms: 1.53x slower                                                 |
| thrift                           | 435 us                                                     | 667 us: 1.53x slower                                                  |
| 2to3                             | 161 ms                                                     | 249 ms: 1.55x slower                                                  |
| coroutines                       | 15.8 ms                                                    | 24.7 ms: 1.56x slower                                                 |
| tornado_http                     | 66.7 ms                                                    | 104 ms: 1.57x slower                                                  |
| crypto_pyaes                     | 49.5 ms                                                    | 77.8 ms: 1.57x slower                                                 |
| sympy_integrate                  | 10.3 ms                                                    | 16.3 ms: 1.57x slower                                                 |
| typing_runtime_protocols         | 87.6 us                                                    | 142 us: 1.62x slower                                                  |
| genshi_xml                       | 29.9 ms                                                    | 49.8 ms: 1.66x slower                                                 |
| sqlglot_optimize                 | 30.9 ms                                                    | 51.6 ms: 1.67x slower                                                 |
| html5lib                         | 31.2 ms                                                    | 53.2 ms: 1.71x slower                                                 |
| scimark_sor                      | 94.9 ms                                                    | 164 ms: 1.73x slower                                                  |
| regex_compile                    | 68.5 ms                                                    | 119 ms: 1.74x slower                                                  |
| pprint_safe_repr                 | 465 ms                                                     | 810 ms: 1.74x slower                                                  |
| pprint_pformat                   | 947 ms                                                     | 1.65 sec: 1.74x slower                                                |
| richards                         | 31.8 ms                                                    | 55.6 ms: 1.75x slower                                                 |
| async_tree_eager                 | 60.3 ms                                                    | 106 ms: 1.75x slower                                                  |
| genshi_text                      | 13.9 ms                                                    | 24.7 ms: 1.77x slower                                                 |
| sympy_str                        | 131 ms                                                     | 233 ms: 1.78x slower                                                  |
| bench_thread_pool                | 447 us                                                     | 798 us: 1.79x slower                                                  |
| spectral_norm                    | 66.4 ms                                                    | 119 ms: 1.80x slower                                                  |
| go                               | 101 ms                                                     | 182 ms: 1.81x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 75.5 ms: 1.83x slower                                                 |
| richards_super                   | 35.2 ms                                                    | 64.7 ms: 1.84x slower                                                 |
| comprehensions                   | 10.2 us                                                    | 18.7 us: 1.84x slower                                                 |
| scimark_monte_carlo              | 42.5 ms                                                    | 78.4 ms: 1.85x slower                                                 |
| django_template                  | 19.4 ms                                                    | 36.1 ms: 1.86x slower                                                 |
| unpickle_pure_python             | 141 us                                                     | 262 us: 1.86x slower                                                  |
| sympy_expand                     | 226 ms                                                     | 427 ms: 1.89x slower                                                  |
| mako                             | 6.99 ms                                                    | 13.3 ms: 1.91x slower                                                 |
| hexiom                           | 4.06 ms                                                    | 7.74 ms: 1.91x slower                                                 |
| float                            | 48.6 ms                                                    | 93.0 ms: 1.91x slower                                                 |
| pickle_pure_python               | 179 us                                                     | 346 us: 1.94x slower                                                  |
| logging_simple                   | 3.04 us                                                    | 6.10 us: 2.01x slower                                                 |
| logging_format                   | 3.31 us                                                    | 6.64 us: 2.01x slower                                                 |
| sympy_sum                        | 69.2 ms                                                    | 141 ms: 2.03x slower                                                  |
| sqlglot_transpile                | 891 us                                                     | 1.90 ms: 2.13x slower                                                 |
| scimark_lu                       | 66.9 ms                                                    | 145 ms: 2.17x slower                                                  |
| chaos                            | 34.0 ms                                                    | 74.7 ms: 2.20x slower                                                 |
| logging_silent                   | 60.1 ns                                                    | 136 ns: 2.26x slower                                                  |
| sqlglot_parse                    | 732 us                                                     | 1.65 ms: 2.26x slower                                                 |
| raytrace                         | 147 ms                                                     | 373 ms: 2.54x slower                                                  |
| nbody                            | 59.6 ms                                                    | 154 ms: 2.59x slower                                                  |
| deltablue                        | 2.14 ms                                                    | 5.61 ms: 2.62x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.37x slower                                                          |

Benchmark hidden because not significant (1): asyncio_tcp
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241005-3.14.0a0-16cd6cc-NOGIL/bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.26x
- 95% likely to have a slowdown of 1.24x
- 99% likely to have a slowdown of 1.21x

# Memory
- memory change: 0.53x