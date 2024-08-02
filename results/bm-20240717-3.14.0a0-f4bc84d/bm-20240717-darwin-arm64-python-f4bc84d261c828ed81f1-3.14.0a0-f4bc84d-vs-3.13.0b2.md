# Results vs. 3.13.0b2

- fork: python
- ref: f4bc84d261c828ed81f1
- machine: darwin-arm64
- commit hash: f4bc84d
- commit date: 2024-07-17
- overall geometric mean: 1.01x faster
- HPT reliability: 94.09%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-darwin-arm64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 163 ms: 1.02x slower                                                  |
| docutils       | 1.44 sec                                                   | 1.45 sec: 1.01x slower                                                |
| html5lib       | 31.2 ms                                                    | 31.5 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                      | 1.01x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-darwin-arm64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg               | 198 ms                                                     | 175 ms: 1.13x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 231 ms: 1.12x faster                                                  |
| async_tree_io_tg                 | 565 ms                                                     | 509 ms: 1.11x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 696 ms: 1.10x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 191 ms: 1.09x faster                                                  |
| async_tree_eager_io              | 766 ms                                                     | 706 ms: 1.09x faster                                                  |
| async_tree_io                    | 563 ms                                                     | 532 ms: 1.06x faster                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 451 ms: 1.04x faster                                                  |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 123 ms: 1.02x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 332 ms: 1.00x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 64.1 ms: 1.06x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.04x faster                                                          |

Benchmark hidden because not significant (5): async_tree_eager_memoization, async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed, async_tree_memoization_tg, async_tree_eager_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-darwin-arm64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 282 ms                                                     | 281 ms: 1.00x faster                                                  |
| float          | 48.6 ms                                                    | 48.8 ms: 1.00x slower                                                 |
| nbody          | 59.6 ms                                                    | 62.2 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                      | 1.02x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-darwin-arm64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 17.3 ms                                                    | 17.1 ms: 1.01x faster                                                 |
| regex_effbot   | 2.58 ms                                                    | 2.57 ms: 1.01x faster                                                 |
| regex_compile  | 68.5 ms                                                    | 68.3 ms: 1.00x faster                                                 |
| regex_dna      | 149 ms                                                     | 149 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                      | 1.01x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-darwin-arm64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_generate   | 52.7 ms                                                    | 53.1 ms: 1.01x slower                                                 |
| unpickle_pure_python | 141 us                                                     | 142 us: 1.01x slower                                                  |
| xml_etree_iterparse  | 71.5 ms                                                    | 72.4 ms: 1.01x slower                                                 |
| tomli_loads          | 1.47 sec                                                   | 1.49 sec: 1.01x slower                                                |
| pickle_pure_python   | 179 us                                                     | 181 us: 1.01x slower                                                  |
| xml_etree_process    | 37.1 ms                                                    | 37.8 ms: 1.02x slower                                                 |
| json_loads           | 16.8 us                                                    | 17.2 us: 1.02x slower                                                 |
| xml_etree_parse      | 106 ms                                                     | 108 ms: 1.02x slower                                                  |
| json_dumps           | 6.23 ms                                                    | 6.53 ms: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.02x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-darwin-arm64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 12.3 ms                                                    | 10.8 ms: 1.14x faster                                                 |
| python_startup         | 15.2 ms                                                    | 13.6 ms: 1.12x faster                                                 |
| Geometric mean         | (ref)                                                      | 1.13x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-darwin-arm64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 13.9 ms                                                    | 14.0 ms: 1.01x slower                                                 |
| mako            | 6.99 ms                                                    | 7.05 ms: 1.01x slower                                                 |
| genshi_xml      | 29.9 ms                                                    | 30.3 ms: 1.01x slower                                                 |
| django_template | 19.4 ms                                                    | 19.8 ms: 1.02x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-darwin-arm64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                         | 204 us                                                     | 145 us: 1.41x faster                                                  |
| deepcopy_memo                    | 22.6 us                                                    | 16.8 us: 1.34x faster                                                 |
| deepcopy_reduce                  | 1.82 us                                                    | 1.50 us: 1.22x faster                                                 |
| python_startup_no_site           | 12.3 ms                                                    | 10.8 ms: 1.14x faster                                                 |
| async_tree_none_tg               | 198 ms                                                     | 175 ms: 1.13x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 231 ms: 1.12x faster                                                  |
| python_startup                   | 15.2 ms                                                    | 13.6 ms: 1.12x faster                                                 |
| async_tree_io_tg                 | 565 ms                                                     | 509 ms: 1.11x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 696 ms: 1.10x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 191 ms: 1.09x faster                                                  |
| async_tree_eager_io              | 766 ms                                                     | 706 ms: 1.09x faster                                                  |
| mdp                              | 1.53 sec                                                   | 1.42 sec: 1.08x faster                                                |
| async_tree_io                    | 563 ms                                                     | 532 ms: 1.06x faster                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 451 ms: 1.04x faster                                                  |
| bench_mp_pool                    | 47.2 ms                                                    | 45.9 ms: 1.03x faster                                                 |
| richards_super                   | 35.2 ms                                                    | 34.3 ms: 1.02x faster                                                 |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 123 ms: 1.02x faster                                                  |
| deltablue                        | 2.14 ms                                                    | 2.10 ms: 1.02x faster                                                 |
| asyncio_tcp_ssl                  | 1.29 sec                                                   | 1.27 sec: 1.02x faster                                                |
| go                               | 101 ms                                                     | 98.9 ms: 1.02x faster                                                 |
| logging_silent                   | 60.1 ns                                                    | 59.1 ns: 1.02x faster                                                 |
| richards                         | 31.8 ms                                                    | 31.4 ms: 1.01x faster                                                 |
| pathlib                          | 23.3 ms                                                    | 23.1 ms: 1.01x faster                                                 |
| regex_v8                         | 17.3 ms                                                    | 17.1 ms: 1.01x faster                                                 |
| regex_effbot                     | 2.58 ms                                                    | 2.57 ms: 1.01x faster                                                 |
| generators                       | 22.9 ms                                                    | 22.7 ms: 1.01x faster                                                 |
| thrift                           | 435 us                                                     | 433 us: 1.00x faster                                                  |
| pyflate                          | 321 ms                                                     | 320 ms: 1.00x faster                                                  |
| telco                            | 4.60 ms                                                    | 4.59 ms: 1.00x faster                                                 |
| regex_compile                    | 68.5 ms                                                    | 68.3 ms: 1.00x faster                                                 |
| regex_dna                        | 149 ms                                                     | 149 ms: 1.00x faster                                                  |
| asyncio_websockets               | 409 ms                                                     | 408 ms: 1.00x faster                                                  |
| pidigits                         | 282 ms                                                     | 281 ms: 1.00x faster                                                  |
| coverage                         | 45.0 ms                                                    | 45.1 ms: 1.00x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 332 ms: 1.00x slower                                                  |
| float                            | 48.6 ms                                                    | 48.8 ms: 1.00x slower                                                 |
| pprint_pformat                   | 947 ms                                                     | 952 ms: 1.01x slower                                                  |
| pprint_safe_repr                 | 465 ms                                                     | 467 ms: 1.01x slower                                                  |
| genshi_text                      | 13.9 ms                                                    | 14.0 ms: 1.01x slower                                                 |
| sympy_integrate                  | 10.3 ms                                                    | 10.4 ms: 1.01x slower                                                 |
| xml_etree_generate               | 52.7 ms                                                    | 53.1 ms: 1.01x slower                                                 |
| async_generators                 | 281 ms                                                     | 283 ms: 1.01x slower                                                  |
| sqlglot_transpile                | 891 us                                                     | 899 us: 1.01x slower                                                  |
| json                             | 2.93 ms                                                    | 2.96 ms: 1.01x slower                                                 |
| mako                             | 6.99 ms                                                    | 7.05 ms: 1.01x slower                                                 |
| docutils                         | 1.44 sec                                                   | 1.45 sec: 1.01x slower                                                |
| unpickle_pure_python             | 141 us                                                     | 142 us: 1.01x slower                                                  |
| sqlglot_parse                    | 732 us                                                     | 739 us: 1.01x slower                                                  |
| html5lib                         | 31.2 ms                                                    | 31.5 ms: 1.01x slower                                                 |
| logging_format                   | 3.31 us                                                    | 3.35 us: 1.01x slower                                                 |
| hexiom                           | 4.06 ms                                                    | 4.11 ms: 1.01x slower                                                 |
| raytrace                         | 147 ms                                                     | 149 ms: 1.01x slower                                                  |
| xml_etree_iterparse              | 71.5 ms                                                    | 72.4 ms: 1.01x slower                                                 |
| meteor_contest                   | 70.3 ms                                                    | 71.2 ms: 1.01x slower                                                 |
| genshi_xml                       | 29.9 ms                                                    | 30.3 ms: 1.01x slower                                                 |
| spectral_norm                    | 66.4 ms                                                    | 67.2 ms: 1.01x slower                                                 |
| bench_thread_pool                | 447 us                                                     | 453 us: 1.01x slower                                                  |
| tomli_loads                      | 1.47 sec                                                   | 1.49 sec: 1.01x slower                                                |
| pickle_pure_python               | 179 us                                                     | 181 us: 1.01x slower                                                  |
| 2to3                             | 161 ms                                                     | 163 ms: 1.02x slower                                                  |
| pycparser                        | 632 ms                                                     | 643 ms: 1.02x slower                                                  |
| scimark_sor                      | 94.9 ms                                                    | 96.5 ms: 1.02x slower                                                 |
| sqlglot_optimize                 | 30.9 ms                                                    | 31.4 ms: 1.02x slower                                                 |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.11 sec: 1.02x slower                                                |
| sympy_sum                        | 69.2 ms                                                    | 70.5 ms: 1.02x slower                                                 |
| xml_etree_process                | 37.1 ms                                                    | 37.8 ms: 1.02x slower                                                 |
| coroutines                       | 15.8 ms                                                    | 16.2 ms: 1.02x slower                                                 |
| json_loads                       | 16.8 us                                                    | 17.2 us: 1.02x slower                                                 |
| scimark_monte_carlo              | 42.5 ms                                                    | 43.3 ms: 1.02x slower                                                 |
| xml_etree_parse                  | 106 ms                                                     | 108 ms: 1.02x slower                                                  |
| django_template                  | 19.4 ms                                                    | 19.8 ms: 1.02x slower                                                 |
| sympy_str                        | 131 ms                                                     | 134 ms: 1.02x slower                                                  |
| sqlglot_normalize                | 166 ms                                                     | 169 ms: 1.02x slower                                                  |
| crypto_pyaes                     | 49.5 ms                                                    | 50.6 ms: 1.02x slower                                                 |
| sympy_expand                     | 226 ms                                                     | 232 ms: 1.03x slower                                                  |
| nqueens                          | 52.2 ms                                                    | 54.0 ms: 1.03x slower                                                 |
| scimark_fft                      | 181 ms                                                     | 187 ms: 1.04x slower                                                  |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.89 ms: 1.04x slower                                                 |
| nbody                            | 59.6 ms                                                    | 62.2 ms: 1.04x slower                                                 |
| json_dumps                       | 6.23 ms                                                    | 6.53 ms: 1.05x slower                                                 |
| chaos                            | 34.0 ms                                                    | 35.7 ms: 1.05x slower                                                 |
| fannkuch                         | 248 ms                                                     | 262 ms: 1.05x slower                                                  |
| scimark_lu                       | 66.9 ms                                                    | 70.7 ms: 1.06x slower                                                 |
| async_tree_eager                 | 60.3 ms                                                    | 64.1 ms: 1.06x slower                                                 |
| comprehensions                   | 10.2 us                                                    | 10.8 us: 1.07x slower                                                 |
| typing_runtime_protocols         | 87.6 us                                                    | 94.7 us: 1.08x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.01x faster                                                          |

Benchmark hidden because not significant (11): async_tree_eager_memoization, async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed, tornado_http, logging_simple, create_gc_cycles, gc_traversal, async_tree_memoization_tg, async_tree_eager_tg, pylint, asyncio_tcp
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 94.09% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.99x