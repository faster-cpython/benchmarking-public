# Results vs. 3.13.0b2

- fork: python
- ref: e913d2c87f1ae4e7a4ae
- machine: darwin-arm64
- commit hash: e913d2c
- commit date: 2024-08-15
- overall geometric mean: 1.00x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.66x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 190 ms: 1.18x slower                                                  |
| docutils       | 1.44 sec                                                   | 1.48 sec: 1.03x slower                                                |
| html5lib       | 31.2 ms                                                    | 31.6 ms: 1.02x slower                                                 |
| tornado_http   | 66.7 ms                                                    | 82.7 ms: 1.24x slower                                                 |
| Geometric mean | (ref)                                                      | 1.11x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 643 ms: 1.19x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 676 ms: 1.14x faster                                                  |
| async_tree_none_tg               | 198 ms                                                     | 183 ms: 1.08x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 243 ms: 1.07x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 197 ms: 1.06x faster                                                  |
| async_tree_memoization_tg        | 240 ms                                                     | 229 ms: 1.04x faster                                                  |
| async_tree_io_tg                 | 565 ms                                                     | 543 ms: 1.04x faster                                                  |
| async_tree_io                    | 563 ms                                                     | 550 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 458 ms: 1.02x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 365 ms: 1.02x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.2 ms: 1.02x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 338 ms: 1.02x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 63.0 ms: 1.05x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.03x faster                                                          |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed_tg, async_tree_eager_memoization_tg, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 282 ms                                                     | 282 ms: 1.00x faster                                                  |
| float          | 48.6 ms                                                    | 48.8 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                      | 1.00x slower                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.47 ms: 1.05x faster                                                 |
| regex_v8       | 17.3 ms                                                    | 16.6 ms: 1.04x faster                                                 |
| regex_dna      | 149 ms                                                     | 145 ms: 1.03x faster                                                  |
| regex_compile  | 68.5 ms                                                    | 69.2 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                      | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                   | 1.49 sec: 1.02x slower                                                |
| json_loads           | 16.8 us                                                    | 17.2 us: 1.02x slower                                                 |
| xml_etree_generate   | 52.7 ms                                                    | 54.0 ms: 1.02x slower                                                 |
| unpickle_pure_python | 141 us                                                     | 145 us: 1.03x slower                                                  |
| xml_etree_process    | 37.1 ms                                                    | 38.6 ms: 1.04x slower                                                 |
| xml_etree_parse      | 106 ms                                                     | 110 ms: 1.04x slower                                                  |
| pickle_pure_python   | 179 us                                                     | 187 us: 1.05x slower                                                  |
| xml_etree_iterparse  | 71.5 ms                                                    | 74.8 ms: 1.05x slower                                                 |
| json_dumps           | 6.23 ms                                                    | 6.52 ms: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.04x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 16.4 ms: 1.08x slower                                                 |
| python_startup_no_site | 12.3 ms                                                    | 13.4 ms: 1.09x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.08x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 29.9 ms                                                    | 30.6 ms: 1.02x slower                                                 |
| genshi_text     | 13.9 ms                                                    | 14.2 ms: 1.02x slower                                                 |
| mako            | 6.99 ms                                                    | 7.20 ms: 1.03x slower                                                 |
| django_template | 19.4 ms                                                    | 20.2 ms: 1.04x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.03x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                         | 204 us                                                     | 148 us: 1.38x faster                                                  |
| deepcopy_memo                    | 22.6 us                                                    | 17.4 us: 1.30x faster                                                 |
| deepcopy_reduce                  | 1.82 us                                                    | 1.51 us: 1.21x faster                                                 |
| async_tree_eager_io              | 766 ms                                                     | 643 ms: 1.19x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 676 ms: 1.14x faster                                                  |
| generators                       | 22.9 ms                                                    | 20.7 ms: 1.10x faster                                                 |
| async_tree_none_tg               | 198 ms                                                     | 183 ms: 1.08x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 243 ms: 1.07x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 197 ms: 1.06x faster                                                  |
| mdp                              | 1.53 sec                                                   | 1.45 sec: 1.06x faster                                                |
| regex_effbot                     | 2.58 ms                                                    | 2.47 ms: 1.05x faster                                                 |
| async_tree_memoization_tg        | 240 ms                                                     | 229 ms: 1.04x faster                                                  |
| async_tree_io_tg                 | 565 ms                                                     | 543 ms: 1.04x faster                                                  |
| regex_v8                         | 17.3 ms                                                    | 16.6 ms: 1.04x faster                                                 |
| regex_dna                        | 149 ms                                                     | 145 ms: 1.03x faster                                                  |
| go                               | 101 ms                                                     | 98.1 ms: 1.03x faster                                                 |
| async_tree_io                    | 563 ms                                                     | 550 ms: 1.02x faster                                                  |
| dulwich_log                      | 27.6 ms                                                    | 27.0 ms: 1.02x faster                                                 |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 458 ms: 1.02x faster                                                  |
| scimark_sor                      | 94.9 ms                                                    | 93.6 ms: 1.01x faster                                                 |
| richards_super                   | 35.2 ms                                                    | 34.9 ms: 1.01x faster                                                 |
| thrift                           | 435 us                                                     | 432 us: 1.01x faster                                                  |
| richards                         | 31.8 ms                                                    | 31.7 ms: 1.01x faster                                                 |
| telco                            | 4.60 ms                                                    | 4.59 ms: 1.00x faster                                                 |
| asyncio_websockets               | 409 ms                                                     | 408 ms: 1.00x faster                                                  |
| pidigits                         | 282 ms                                                     | 282 ms: 1.00x faster                                                  |
| pyflate                          | 321 ms                                                     | 321 ms: 1.00x slower                                                  |
| bench_thread_pool                | 447 us                                                     | 448 us: 1.00x slower                                                  |
| float                            | 48.6 ms                                                    | 48.8 ms: 1.00x slower                                                 |
| async_generators                 | 281 ms                                                     | 282 ms: 1.00x slower                                                  |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.79 ms: 1.00x slower                                                 |
| coverage                         | 45.0 ms                                                    | 45.2 ms: 1.01x slower                                                 |
| deltablue                        | 2.14 ms                                                    | 2.15 ms: 1.01x slower                                                 |
| pathlib                          | 23.3 ms                                                    | 23.6 ms: 1.01x slower                                                 |
| regex_compile                    | 68.5 ms                                                    | 69.2 ms: 1.01x slower                                                 |
| gc_traversal                     | 2.45 ms                                                    | 2.48 ms: 1.01x slower                                                 |
| json                             | 2.93 ms                                                    | 2.96 ms: 1.01x slower                                                 |
| pycparser                        | 632 ms                                                     | 640 ms: 1.01x slower                                                  |
| raytrace                         | 147 ms                                                     | 149 ms: 1.01x slower                                                  |
| scimark_lu                       | 66.9 ms                                                    | 67.9 ms: 1.01x slower                                                 |
| html5lib                         | 31.2 ms                                                    | 31.6 ms: 1.02x slower                                                 |
| sqlglot_parse                    | 732 us                                                     | 746 us: 1.02x slower                                                  |
| tomli_loads                      | 1.47 sec                                                   | 1.49 sec: 1.02x slower                                                |
| hexiom                           | 4.06 ms                                                    | 4.14 ms: 1.02x slower                                                 |
| logging_simple                   | 3.04 us                                                    | 3.10 us: 1.02x slower                                                 |
| scimark_fft                      | 181 ms                                                     | 184 ms: 1.02x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 365 ms: 1.02x slower                                                  |
| json_loads                       | 16.8 us                                                    | 17.2 us: 1.02x slower                                                 |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.2 ms: 1.02x slower                                                 |
| genshi_xml                       | 29.9 ms                                                    | 30.6 ms: 1.02x slower                                                 |
| genshi_text                      | 13.9 ms                                                    | 14.2 ms: 1.02x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 338 ms: 1.02x slower                                                  |
| sympy_integrate                  | 10.3 ms                                                    | 10.6 ms: 1.02x slower                                                 |
| crypto_pyaes                     | 49.5 ms                                                    | 50.6 ms: 1.02x slower                                                 |
| nqueens                          | 52.2 ms                                                    | 53.4 ms: 1.02x slower                                                 |
| xml_etree_generate               | 52.7 ms                                                    | 54.0 ms: 1.02x slower                                                 |
| logging_format                   | 3.31 us                                                    | 3.39 us: 1.03x slower                                                 |
| scimark_monte_carlo              | 42.5 ms                                                    | 43.5 ms: 1.03x slower                                                 |
| sqlglot_transpile                | 891 us                                                     | 913 us: 1.03x slower                                                  |
| spectral_norm                    | 66.4 ms                                                    | 68.1 ms: 1.03x slower                                                 |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.13 sec: 1.03x slower                                                |
| coroutines                       | 15.8 ms                                                    | 16.3 ms: 1.03x slower                                                 |
| docutils                         | 1.44 sec                                                   | 1.48 sec: 1.03x slower                                                |
| meteor_contest                   | 70.3 ms                                                    | 72.4 ms: 1.03x slower                                                 |
| sympy_str                        | 131 ms                                                     | 135 ms: 1.03x slower                                                  |
| logging_silent                   | 60.1 ns                                                    | 62.0 ns: 1.03x slower                                                 |
| mako                             | 6.99 ms                                                    | 7.20 ms: 1.03x slower                                                 |
| unpickle_pure_python             | 141 us                                                     | 145 us: 1.03x slower                                                  |
| sympy_sum                        | 69.2 ms                                                    | 71.5 ms: 1.03x slower                                                 |
| bench_mp_pool                    | 47.2 ms                                                    | 48.8 ms: 1.03x slower                                                 |
| pprint_safe_repr                 | 465 ms                                                     | 481 ms: 1.03x slower                                                  |
| sympy_expand                     | 226 ms                                                     | 233 ms: 1.03x slower                                                  |
| pprint_pformat                   | 947 ms                                                     | 980 ms: 1.03x slower                                                  |
| django_template                  | 19.4 ms                                                    | 20.2 ms: 1.04x slower                                                 |
| xml_etree_process                | 37.1 ms                                                    | 38.6 ms: 1.04x slower                                                 |
| sqlglot_normalize                | 166 ms                                                     | 173 ms: 1.04x slower                                                  |
| sqlglot_optimize                 | 30.9 ms                                                    | 32.2 ms: 1.04x slower                                                 |
| xml_etree_parse                  | 106 ms                                                     | 110 ms: 1.04x slower                                                  |
| chaos                            | 34.0 ms                                                    | 35.5 ms: 1.04x slower                                                 |
| async_tree_eager                 | 60.3 ms                                                    | 63.0 ms: 1.05x slower                                                 |
| pickle_pure_python               | 179 us                                                     | 187 us: 1.05x slower                                                  |
| xml_etree_iterparse              | 71.5 ms                                                    | 74.8 ms: 1.05x slower                                                 |
| json_dumps                       | 6.23 ms                                                    | 6.52 ms: 1.05x slower                                                 |
| fannkuch                         | 248 ms                                                     | 262 ms: 1.06x slower                                                  |
| comprehensions                   | 10.2 us                                                    | 10.9 us: 1.08x slower                                                 |
| python_startup                   | 15.2 ms                                                    | 16.4 ms: 1.08x slower                                                 |
| python_startup_no_site           | 12.3 ms                                                    | 13.4 ms: 1.09x slower                                                 |
| typing_runtime_protocols         | 87.6 us                                                    | 96.2 us: 1.10x slower                                                 |
| 2to3                             | 161 ms                                                     | 190 ms: 1.18x slower                                                  |
| tornado_http                     | 66.7 ms                                                    | 82.7 ms: 1.24x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.00x slower                                                          |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed_tg, nbody, create_gc_cycles, asyncio_tcp_ssl, async_tree_eager_memoization_tg, async_tree_eager_memoization, asyncio_tcp, pylint
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.66x