# Results vs. 3.13.0b2

- fork: python
- ref: 79c542b5cc774ba758ac
- machine: darwin-arm64
- commit hash: 79c542b
- commit date: 2024-08-17
- overall geometric mean: 1.01x faster
- HPT reliability: 91.12%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.44x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| docutils       | 1.44 sec                                                   | 1.47 sec: 1.02x slower                                                |
| html5lib       | 31.2 ms                                                    | 31.4 ms: 1.01x slower                                                 |
| tornado_http   | 66.7 ms                                                    | 86.5 ms: 1.30x slower                                                 |
| Geometric mean | (ref)                                                      | 1.08x slower                                                          |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 617 ms: 1.24x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 653 ms: 1.18x faster                                                  |
| async_tree_io_tg                 | 565 ms                                                     | 505 ms: 1.12x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 192 ms: 1.09x faster                                                  |
| async_tree_none_tg               | 198 ms                                                     | 182 ms: 1.09x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 241 ms: 1.08x faster                                                  |
| async_tree_memoization_tg        | 240 ms                                                     | 228 ms: 1.05x faster                                                  |
| async_tree_io                    | 563 ms                                                     | 539 ms: 1.05x faster                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 453 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 438 ms: 1.03x faster                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.8 ms: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 336 ms: 1.02x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 62.0 ms: 1.03x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.05x faster                                                          |

Benchmark hidden because not significant (3): async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 59.6 ms                                                    | 60.8 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                      | 1.01x slower                                                          |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.47 ms: 1.05x faster                                                 |
| regex_v8       | 17.3 ms                                                    | 16.6 ms: 1.04x faster                                                 |
| regex_dna      | 149 ms                                                     | 145 ms: 1.03x faster                                                  |
| regex_compile  | 68.5 ms                                                    | 68.0 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                      | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_process    | 37.1 ms                                                    | 37.3 ms: 1.01x slower                                                 |
| xml_etree_generate   | 52.7 ms                                                    | 53.1 ms: 1.01x slower                                                 |
| tomli_loads          | 1.47 sec                                                   | 1.48 sec: 1.01x slower                                                |
| unpickle_pure_python | 141 us                                                     | 143 us: 1.02x slower                                                  |
| pickle_pure_python   | 179 us                                                     | 182 us: 1.02x slower                                                  |
| json_dumps           | 6.23 ms                                                    | 6.38 ms: 1.02x slower                                                 |
| json_loads           | 16.8 us                                                    | 17.3 us: 1.03x slower                                                 |
| xml_etree_iterparse  | 71.5 ms                                                    | 74.8 ms: 1.05x slower                                                 |
| xml_etree_parse      | 106 ms                                                     | 111 ms: 1.05x slower                                                  |
| Geometric mean       | (ref)                                                      | 1.02x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 12.3 ms                                                    | 10.9 ms: 1.13x faster                                                 |
| python_startup         | 15.2 ms                                                    | 13.8 ms: 1.10x faster                                                 |
| Geometric mean         | (ref)                                                      | 1.11x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 6.96 ms: 1.00x faster                                                 |
| django_template | 19.4 ms                                                    | 19.6 ms: 1.01x slower                                                 |
| genshi_text     | 13.9 ms                                                    | 14.1 ms: 1.01x slower                                                 |
| genshi_xml      | 29.9 ms                                                    | 30.4 ms: 1.01x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                         | 204 us                                                     | 146 us: 1.40x faster                                                  |
| deepcopy_memo                    | 22.6 us                                                    | 17.1 us: 1.32x faster                                                 |
| async_tree_eager_io              | 766 ms                                                     | 617 ms: 1.24x faster                                                  |
| deepcopy_reduce                  | 1.82 us                                                    | 1.51 us: 1.20x faster                                                 |
| async_tree_eager_io_tg           | 768 ms                                                     | 653 ms: 1.18x faster                                                  |
| python_startup_no_site           | 12.3 ms                                                    | 10.9 ms: 1.13x faster                                                 |
| generators                       | 22.9 ms                                                    | 20.3 ms: 1.13x faster                                                 |
| async_tree_io_tg                 | 565 ms                                                     | 505 ms: 1.12x faster                                                  |
| python_startup                   | 15.2 ms                                                    | 13.8 ms: 1.10x faster                                                 |
| async_tree_none                  | 209 ms                                                     | 192 ms: 1.09x faster                                                  |
| async_tree_none_tg               | 198 ms                                                     | 182 ms: 1.09x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 241 ms: 1.08x faster                                                  |
| richards_super                   | 35.2 ms                                                    | 33.3 ms: 1.06x faster                                                 |
| richards                         | 31.8 ms                                                    | 30.3 ms: 1.05x faster                                                 |
| async_tree_memoization_tg        | 240 ms                                                     | 228 ms: 1.05x faster                                                  |
| regex_effbot                     | 2.58 ms                                                    | 2.47 ms: 1.05x faster                                                 |
| async_tree_io                    | 563 ms                                                     | 539 ms: 1.05x faster                                                  |
| go                               | 101 ms                                                     | 96.6 ms: 1.04x faster                                                 |
| regex_v8                         | 17.3 ms                                                    | 16.6 ms: 1.04x faster                                                 |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 453 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 438 ms: 1.03x faster                                                  |
| regex_dna                        | 149 ms                                                     | 145 ms: 1.03x faster                                                  |
| dulwich_log                      | 27.6 ms                                                    | 26.9 ms: 1.02x faster                                                 |
| comprehensions                   | 10.2 us                                                    | 10.0 us: 1.01x faster                                                 |
| deltablue                        | 2.14 ms                                                    | 2.11 ms: 1.01x faster                                                 |
| scimark_sor                      | 94.9 ms                                                    | 93.8 ms: 1.01x faster                                                 |
| thrift                           | 435 us                                                     | 432 us: 1.01x faster                                                  |
| regex_compile                    | 68.5 ms                                                    | 68.0 ms: 1.01x faster                                                 |
| asyncio_tcp_ssl                  | 1.29 sec                                                   | 1.28 sec: 1.01x faster                                                |
| telco                            | 4.60 ms                                                    | 4.58 ms: 1.01x faster                                                 |
| mako                             | 6.99 ms                                                    | 6.96 ms: 1.00x faster                                                 |
| pyflate                          | 321 ms                                                     | 321 ms: 1.00x slower                                                  |
| raytrace                         | 147 ms                                                     | 147 ms: 1.00x slower                                                  |
| pprint_safe_repr                 | 465 ms                                                     | 466 ms: 1.00x slower                                                  |
| logging_silent                   | 60.1 ns                                                    | 60.4 ns: 1.00x slower                                                 |
| pprint_pformat                   | 947 ms                                                     | 952 ms: 1.01x slower                                                  |
| async_generators                 | 281 ms                                                     | 282 ms: 1.01x slower                                                  |
| xml_etree_process                | 37.1 ms                                                    | 37.3 ms: 1.01x slower                                                 |
| bench_thread_pool                | 447 us                                                     | 450 us: 1.01x slower                                                  |
| xml_etree_generate               | 52.7 ms                                                    | 53.1 ms: 1.01x slower                                                 |
| pycparser                        | 632 ms                                                     | 638 ms: 1.01x slower                                                  |
| html5lib                         | 31.2 ms                                                    | 31.4 ms: 1.01x slower                                                 |
| coverage                         | 45.0 ms                                                    | 45.4 ms: 1.01x slower                                                 |
| hexiom                           | 4.06 ms                                                    | 4.10 ms: 1.01x slower                                                 |
| logging_simple                   | 3.04 us                                                    | 3.07 us: 1.01x slower                                                 |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.8 ms: 1.01x slower                                                 |
| tomli_loads                      | 1.47 sec                                                   | 1.48 sec: 1.01x slower                                                |
| sympy_integrate                  | 10.3 ms                                                    | 10.5 ms: 1.01x slower                                                 |
| sympy_expand                     | 226 ms                                                     | 228 ms: 1.01x slower                                                  |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.81 ms: 1.01x slower                                                 |
| django_template                  | 19.4 ms                                                    | 19.6 ms: 1.01x slower                                                 |
| sqlglot_optimize                 | 30.9 ms                                                    | 31.3 ms: 1.01x slower                                                 |
| spectral_norm                    | 66.4 ms                                                    | 67.2 ms: 1.01x slower                                                 |
| sqlglot_transpile                | 891 us                                                     | 902 us: 1.01x slower                                                  |
| genshi_text                      | 13.9 ms                                                    | 14.1 ms: 1.01x slower                                                 |
| scimark_lu                       | 66.9 ms                                                    | 67.8 ms: 1.01x slower                                                 |
| genshi_xml                       | 29.9 ms                                                    | 30.4 ms: 1.01x slower                                                 |
| sqlglot_normalize                | 166 ms                                                     | 168 ms: 1.02x slower                                                  |
| json                             | 2.93 ms                                                    | 2.98 ms: 1.02x slower                                                 |
| sympy_str                        | 131 ms                                                     | 134 ms: 1.02x slower                                                  |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.10 sec: 1.02x slower                                                |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 336 ms: 1.02x slower                                                  |
| sqlglot_parse                    | 732 us                                                     | 744 us: 1.02x slower                                                  |
| unpickle_pure_python             | 141 us                                                     | 143 us: 1.02x slower                                                  |
| sympy_sum                        | 69.2 ms                                                    | 70.4 ms: 1.02x slower                                                 |
| coroutines                       | 15.8 ms                                                    | 16.2 ms: 1.02x slower                                                 |
| docutils                         | 1.44 sec                                                   | 1.47 sec: 1.02x slower                                                |
| nbody                            | 59.6 ms                                                    | 60.8 ms: 1.02x slower                                                 |
| nqueens                          | 52.2 ms                                                    | 53.3 ms: 1.02x slower                                                 |
| pickle_pure_python               | 179 us                                                     | 182 us: 1.02x slower                                                  |
| meteor_contest                   | 70.3 ms                                                    | 71.9 ms: 1.02x slower                                                 |
| json_dumps                       | 6.23 ms                                                    | 6.38 ms: 1.02x slower                                                 |
| crypto_pyaes                     | 49.5 ms                                                    | 50.7 ms: 1.02x slower                                                 |
| scimark_monte_carlo              | 42.5 ms                                                    | 43.5 ms: 1.03x slower                                                 |
| scimark_fft                      | 181 ms                                                     | 185 ms: 1.03x slower                                                  |
| logging_format                   | 3.31 us                                                    | 3.40 us: 1.03x slower                                                 |
| json_loads                       | 16.8 us                                                    | 17.3 us: 1.03x slower                                                 |
| async_tree_eager                 | 60.3 ms                                                    | 62.0 ms: 1.03x slower                                                 |
| xml_etree_iterparse              | 71.5 ms                                                    | 74.8 ms: 1.05x slower                                                 |
| chaos                            | 34.0 ms                                                    | 35.8 ms: 1.05x slower                                                 |
| xml_etree_parse                  | 106 ms                                                     | 111 ms: 1.05x slower                                                  |
| typing_runtime_protocols         | 87.6 us                                                    | 93.2 us: 1.06x slower                                                 |
| fannkuch                         | 248 ms                                                     | 265 ms: 1.07x slower                                                  |
| tornado_http                     | 66.7 ms                                                    | 86.5 ms: 1.30x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.01x faster                                                          |

Benchmark hidden because not significant (14): bench_mp_pool, async_tree_eager_memoization, async_tree_eager_memoization_tg, create_gc_cycles, pidigits, asyncio_websockets, pathlib, float, gc_traversal, mdp, async_tree_eager_cpu_io_mixed, 2to3, asyncio_tcp, pylint
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 91.12% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.44x