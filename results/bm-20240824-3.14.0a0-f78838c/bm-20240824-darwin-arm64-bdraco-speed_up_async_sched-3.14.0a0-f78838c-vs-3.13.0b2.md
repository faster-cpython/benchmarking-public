# Results vs. 3.13.0b2

- fork: bdraco
- ref: speed_up_async_sched
- machine: darwin-arm64
- commit hash: f78838c
- commit date: 2024-08-24
- overall geometric mean: 1.00x faster
- HPT reliability: 93.06%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.65x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 160 ms: 1.01x faster                                                  |
| docutils       | 1.44 sec                                                   | 1.47 sec: 1.02x slower                                                |
| tornado_http   | 66.7 ms                                                    | 85.2 ms: 1.28x slower                                                 |
| Geometric mean | (ref)                                                      | 1.07x slower                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 699 ms: 1.10x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 192 ms: 1.09x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 243 ms: 1.07x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 742 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 457 ms: 1.02x faster                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 60.8 ms: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 337 ms: 1.02x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.2 ms: 1.02x slower                                                 |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 129 ms: 1.03x slower                                                  |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 465 ms: 1.03x slower                                                  |
| async_tree_io                    | 563 ms                                                     | 598 ms: 1.06x slower                                                  |
| async_tree_io_tg                 | 565 ms                                                     | 606 ms: 1.07x slower                                                  |
| Geometric mean                   | (ref)                                                      | 1.00x faster                                                          |

Benchmark hidden because not significant (4): async_tree_memoization_tg, async_tree_eager_memoization, async_tree_none_tg, async_tree_eager_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 59.6 ms                                                    | 59.4 ms: 1.00x faster                                                 |
| pidigits       | 282 ms                                                     | 282 ms: 1.00x faster                                                  |
| float          | 48.6 ms                                                    | 48.9 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                      | 1.00x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.46 ms: 1.05x faster                                                 |
| regex_v8       | 17.3 ms                                                    | 16.5 ms: 1.05x faster                                                 |
| regex_dna      | 149 ms                                                     | 145 ms: 1.03x faster                                                  |
| regex_compile  | 68.5 ms                                                    | 66.9 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                      | 1.04x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_generate   | 52.7 ms                                                    | 53.2 ms: 1.01x slower                                                 |
| json_dumps           | 6.23 ms                                                    | 6.30 ms: 1.01x slower                                                 |
| tomli_loads          | 1.47 sec                                                   | 1.48 sec: 1.01x slower                                                |
| pickle_pure_python   | 179 us                                                     | 181 us: 1.01x slower                                                  |
| xml_etree_process    | 37.1 ms                                                    | 37.7 ms: 1.02x slower                                                 |
| unpickle_pure_python | 141 us                                                     | 143 us: 1.02x slower                                                  |
| json_loads           | 16.8 us                                                    | 17.2 us: 1.02x slower                                                 |
| xml_etree_iterparse  | 71.5 ms                                                    | 73.8 ms: 1.03x slower                                                 |
| xml_etree_parse      | 106 ms                                                     | 110 ms: 1.04x slower                                                  |
| Geometric mean       | (ref)                                                      | 1.02x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 16.5 ms: 1.09x slower                                                 |
| python_startup_no_site | 12.3 ms                                                    | 13.5 ms: 1.10x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.09x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 13.9 ms                                                    | 13.8 ms: 1.01x faster                                                 |
| mako            | 6.99 ms                                                    | 6.94 ms: 1.01x faster                                                 |
| genshi_xml      | 29.9 ms                                                    | 30.1 ms: 1.01x slower                                                 |
| django_template | 19.4 ms                                                    | 19.7 ms: 1.02x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.00x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                         | 204 us                                                     | 144 us: 1.42x faster                                                  |
| deepcopy_memo                    | 22.6 us                                                    | 16.9 us: 1.34x faster                                                 |
| deepcopy_reduce                  | 1.82 us                                                    | 1.51 us: 1.21x faster                                                 |
| generators                       | 22.9 ms                                                    | 20.4 ms: 1.12x faster                                                 |
| async_tree_eager_io              | 766 ms                                                     | 699 ms: 1.10x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 192 ms: 1.09x faster                                                  |
| mdp                              | 1.53 sec                                                   | 1.43 sec: 1.07x faster                                                |
| async_tree_memoization           | 260 ms                                                     | 243 ms: 1.07x faster                                                  |
| richards_super                   | 35.2 ms                                                    | 33.4 ms: 1.05x faster                                                 |
| regex_effbot                     | 2.58 ms                                                    | 2.46 ms: 1.05x faster                                                 |
| richards                         | 31.8 ms                                                    | 30.4 ms: 1.05x faster                                                 |
| regex_v8                         | 17.3 ms                                                    | 16.5 ms: 1.05x faster                                                 |
| async_tree_eager_io_tg           | 768 ms                                                     | 742 ms: 1.03x faster                                                  |
| thrift                           | 435 us                                                     | 423 us: 1.03x faster                                                  |
| regex_dna                        | 149 ms                                                     | 145 ms: 1.03x faster                                                  |
| regex_compile                    | 68.5 ms                                                    | 66.9 ms: 1.02x faster                                                 |
| comprehensions                   | 10.2 us                                                    | 9.93 us: 1.02x faster                                                 |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 457 ms: 1.02x faster                                                  |
| dulwich_log                      | 27.6 ms                                                    | 27.1 ms: 1.02x faster                                                 |
| pprint_pformat                   | 947 ms                                                     | 930 ms: 1.02x faster                                                  |
| asyncio_tcp_ssl                  | 1.29 sec                                                   | 1.27 sec: 1.02x faster                                                |
| scimark_sor                      | 94.9 ms                                                    | 93.3 ms: 1.02x faster                                                 |
| pprint_safe_repr                 | 465 ms                                                     | 457 ms: 1.02x faster                                                  |
| coverage                         | 45.0 ms                                                    | 44.3 ms: 1.02x faster                                                 |
| 2to3                             | 161 ms                                                     | 160 ms: 1.01x faster                                                  |
| genshi_text                      | 13.9 ms                                                    | 13.8 ms: 1.01x faster                                                 |
| mako                             | 6.99 ms                                                    | 6.94 ms: 1.01x faster                                                 |
| nbody                            | 59.6 ms                                                    | 59.4 ms: 1.00x faster                                                 |
| deltablue                        | 2.14 ms                                                    | 2.13 ms: 1.00x faster                                                 |
| scimark_lu                       | 66.9 ms                                                    | 66.7 ms: 1.00x faster                                                 |
| sympy_integrate                  | 10.3 ms                                                    | 10.3 ms: 1.00x faster                                                 |
| pidigits                         | 282 ms                                                     | 282 ms: 1.00x faster                                                  |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.78 ms: 1.00x slower                                                 |
| genshi_xml                       | 29.9 ms                                                    | 30.1 ms: 1.01x slower                                                 |
| bench_thread_pool                | 447 us                                                     | 449 us: 1.01x slower                                                  |
| float                            | 48.6 ms                                                    | 48.9 ms: 1.01x slower                                                 |
| gc_traversal                     | 2.45 ms                                                    | 2.47 ms: 1.01x slower                                                 |
| sqlglot_transpile                | 891 us                                                     | 897 us: 1.01x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 60.8 ms: 1.01x slower                                                 |
| pathlib                          | 23.3 ms                                                    | 23.5 ms: 1.01x slower                                                 |
| sqlglot_parse                    | 732 us                                                     | 739 us: 1.01x slower                                                  |
| create_gc_cycles                 | 897 us                                                     | 906 us: 1.01x slower                                                  |
| xml_etree_generate               | 52.7 ms                                                    | 53.2 ms: 1.01x slower                                                 |
| logging_simple                   | 3.04 us                                                    | 3.07 us: 1.01x slower                                                 |
| sqlglot_optimize                 | 30.9 ms                                                    | 31.2 ms: 1.01x slower                                                 |
| json_dumps                       | 6.23 ms                                                    | 6.30 ms: 1.01x slower                                                 |
| tomli_loads                      | 1.47 sec                                                   | 1.48 sec: 1.01x slower                                                |
| sqlglot_normalize                | 166 ms                                                     | 168 ms: 1.01x slower                                                  |
| raytrace                         | 147 ms                                                     | 149 ms: 1.01x slower                                                  |
| pickle_pure_python               | 179 us                                                     | 181 us: 1.01x slower                                                  |
| coroutines                       | 15.8 ms                                                    | 16.1 ms: 1.01x slower                                                 |
| pycparser                        | 632 ms                                                     | 643 ms: 1.02x slower                                                  |
| django_template                  | 19.4 ms                                                    | 19.7 ms: 1.02x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 337 ms: 1.02x slower                                                  |
| logging_silent                   | 60.1 ns                                                    | 61.2 ns: 1.02x slower                                                 |
| xml_etree_process                | 37.1 ms                                                    | 37.7 ms: 1.02x slower                                                 |
| docutils                         | 1.44 sec                                                   | 1.47 sec: 1.02x slower                                                |
| unpickle_pure_python             | 141 us                                                     | 143 us: 1.02x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.2 ms: 1.02x slower                                                 |
| scimark_monte_carlo              | 42.5 ms                                                    | 43.3 ms: 1.02x slower                                                 |
| spectral_norm                    | 66.4 ms                                                    | 67.7 ms: 1.02x slower                                                 |
| nqueens                          | 52.2 ms                                                    | 53.3 ms: 1.02x slower                                                 |
| json_loads                       | 16.8 us                                                    | 17.2 us: 1.02x slower                                                 |
| scimark_fft                      | 181 ms                                                     | 185 ms: 1.02x slower                                                  |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.13 sec: 1.02x slower                                                |
| logging_format                   | 3.31 us                                                    | 3.40 us: 1.03x slower                                                 |
| json                             | 2.93 ms                                                    | 3.01 ms: 1.03x slower                                                 |
| crypto_pyaes                     | 49.5 ms                                                    | 50.9 ms: 1.03x slower                                                 |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 129 ms: 1.03x slower                                                  |
| meteor_contest                   | 70.3 ms                                                    | 72.5 ms: 1.03x slower                                                 |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 465 ms: 1.03x slower                                                  |
| bench_mp_pool                    | 47.2 ms                                                    | 48.7 ms: 1.03x slower                                                 |
| xml_etree_iterparse              | 71.5 ms                                                    | 73.8 ms: 1.03x slower                                                 |
| typing_runtime_protocols         | 87.6 us                                                    | 90.9 us: 1.04x slower                                                 |
| telco                            | 4.60 ms                                                    | 4.78 ms: 1.04x slower                                                 |
| xml_etree_parse                  | 106 ms                                                     | 110 ms: 1.04x slower                                                  |
| fannkuch                         | 248 ms                                                     | 260 ms: 1.05x slower                                                  |
| chaos                            | 34.0 ms                                                    | 35.7 ms: 1.05x slower                                                 |
| go                               | 101 ms                                                     | 106 ms: 1.05x slower                                                  |
| async_tree_io                    | 563 ms                                                     | 598 ms: 1.06x slower                                                  |
| async_tree_io_tg                 | 565 ms                                                     | 606 ms: 1.07x slower                                                  |
| python_startup                   | 15.2 ms                                                    | 16.5 ms: 1.09x slower                                                 |
| python_startup_no_site           | 12.3 ms                                                    | 13.5 ms: 1.10x slower                                                 |
| tornado_http                     | 66.7 ms                                                    | 85.2 ms: 1.28x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.00x faster                                                          |

Benchmark hidden because not significant (14): async_tree_memoization_tg, async_tree_eager_memoization, sympy_sum, sympy_str, asyncio_websockets, async_generators, hexiom, pyflate, sympy_expand, html5lib, async_tree_none_tg, async_tree_eager_cpu_io_mixed, asyncio_tcp, pylint
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 93.06% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.65x