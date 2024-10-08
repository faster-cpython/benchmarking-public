# Results vs. 3.13.0b2

- fork: mdboom
- ref: simplify_richcompare
- machine: darwin-arm64
- commit hash: 2fa7b0e
- commit date: 2024-09-04
- overall geometric mean: 1.00x faster
- HPT reliability: 99.56%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.50x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| docutils       | 1.44 sec                                                   | 1.45 sec: 1.01x slower                                                |
| html5lib       | 31.2 ms                                                    | 30.1 ms: 1.04x faster                                                 |
| tornado_http   | 66.7 ms                                                    | 82.8 ms: 1.24x slower                                                 |
| Geometric mean | (ref)                                                      | 1.05x slower                                                          |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 680 ms: 1.13x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 193 ms: 1.08x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 716 ms: 1.07x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 250 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 458 ms: 1.02x faster                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 60.6 ms: 1.00x slower                                                 |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 361 ms: 1.01x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.8 ms: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 336 ms: 1.02x slower                                                  |
| async_tree_io                    | 563 ms                                                     | 597 ms: 1.06x slower                                                  |
| Geometric mean                   | (ref)                                                      | 1.01x faster                                                          |

Benchmark hidden because not significant (6): async_tree_eager_memoization_tg, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 59.6 ms                                                    | 59.4 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                      | 1.00x faster                                                          |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.46 ms: 1.05x faster                                                 |
| regex_v8       | 17.3 ms                                                    | 16.5 ms: 1.04x faster                                                 |
| regex_dna      | 149 ms                                                     | 146 ms: 1.02x faster                                                  |
| regex_compile  | 68.5 ms                                                    | 67.5 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                      | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                   | 1.48 sec: 1.01x slower                                                |
| unpickle_pure_python | 141 us                                                     | 142 us: 1.01x slower                                                  |
| json_loads           | 16.8 us                                                    | 17.2 us: 1.02x slower                                                 |
| xml_etree_generate   | 52.7 ms                                                    | 53.9 ms: 1.02x slower                                                 |
| xml_etree_process    | 37.1 ms                                                    | 37.9 ms: 1.02x slower                                                 |
| pickle_pure_python   | 179 us                                                     | 183 us: 1.03x slower                                                  |
| xml_etree_iterparse  | 71.5 ms                                                    | 73.9 ms: 1.03x slower                                                 |
| json_dumps           | 6.23 ms                                                    | 6.44 ms: 1.03x slower                                                 |
| xml_etree_parse      | 106 ms                                                     | 110 ms: 1.04x slower                                                  |
| Geometric mean       | (ref)                                                      | 1.03x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 16.6 ms: 1.10x slower                                                 |
| python_startup_no_site | 12.3 ms                                                    | 13.5 ms: 1.10x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.10x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 13.9 ms                                                    | 13.8 ms: 1.01x faster                                                 |
| genshi_xml      | 29.9 ms                                                    | 30.4 ms: 1.02x slower                                                 |
| mako            | 6.99 ms                                                    | 7.10 ms: 1.02x slower                                                 |
| django_template | 19.4 ms                                                    | 20.0 ms: 1.03x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                         | 204 us                                                     | 145 us: 1.40x faster                                                  |
| deepcopy_memo                    | 22.6 us                                                    | 16.6 us: 1.36x faster                                                 |
| go                               | 101 ms                                                     | 79.0 ms: 1.27x faster                                                 |
| deepcopy_reduce                  | 1.82 us                                                    | 1.51 us: 1.21x faster                                                 |
| async_tree_eager_io              | 766 ms                                                     | 680 ms: 1.13x faster                                                  |
| generators                       | 22.9 ms                                                    | 20.4 ms: 1.12x faster                                                 |
| async_tree_none                  | 209 ms                                                     | 193 ms: 1.08x faster                                                  |
| mdp                              | 1.53 sec                                                   | 1.43 sec: 1.08x faster                                                |
| async_tree_eager_io_tg           | 768 ms                                                     | 716 ms: 1.07x faster                                                  |
| regex_effbot                     | 2.58 ms                                                    | 2.46 ms: 1.05x faster                                                 |
| regex_v8                         | 17.3 ms                                                    | 16.5 ms: 1.04x faster                                                 |
| async_tree_memoization           | 260 ms                                                     | 250 ms: 1.04x faster                                                  |
| html5lib                         | 31.2 ms                                                    | 30.1 ms: 1.04x faster                                                 |
| thrift                           | 435 us                                                     | 421 us: 1.03x faster                                                  |
| pprint_safe_repr                 | 465 ms                                                     | 453 ms: 1.03x faster                                                  |
| regex_dna                        | 149 ms                                                     | 146 ms: 1.02x faster                                                  |
| scimark_sor                      | 94.9 ms                                                    | 92.8 ms: 1.02x faster                                                 |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 458 ms: 1.02x faster                                                  |
| pprint_pformat                   | 947 ms                                                     | 932 ms: 1.02x faster                                                  |
| richards                         | 31.8 ms                                                    | 31.3 ms: 1.02x faster                                                 |
| regex_compile                    | 68.5 ms                                                    | 67.5 ms: 1.01x faster                                                 |
| dulwich_log                      | 27.6 ms                                                    | 27.2 ms: 1.01x faster                                                 |
| coverage                         | 45.0 ms                                                    | 44.5 ms: 1.01x faster                                                 |
| comprehensions                   | 10.2 us                                                    | 10.1 us: 1.01x faster                                                 |
| genshi_text                      | 13.9 ms                                                    | 13.8 ms: 1.01x faster                                                 |
| asyncio_tcp_ssl                  | 1.29 sec                                                   | 1.28 sec: 1.01x faster                                                |
| richards_super                   | 35.2 ms                                                    | 35.1 ms: 1.00x faster                                                 |
| nbody                            | 59.6 ms                                                    | 59.4 ms: 1.00x faster                                                 |
| asyncio_websockets               | 409 ms                                                     | 408 ms: 1.00x faster                                                  |
| gc_traversal                     | 2.45 ms                                                    | 2.46 ms: 1.00x slower                                                 |
| async_tree_eager                 | 60.3 ms                                                    | 60.6 ms: 1.00x slower                                                 |
| deltablue                        | 2.14 ms                                                    | 2.15 ms: 1.00x slower                                                 |
| async_generators                 | 281 ms                                                     | 282 ms: 1.01x slower                                                  |
| sympy_str                        | 131 ms                                                     | 132 ms: 1.01x slower                                                  |
| tomli_loads                      | 1.47 sec                                                   | 1.48 sec: 1.01x slower                                                |
| bench_thread_pool                | 447 us                                                     | 450 us: 1.01x slower                                                  |
| json                             | 2.93 ms                                                    | 2.95 ms: 1.01x slower                                                 |
| hexiom                           | 4.06 ms                                                    | 4.09 ms: 1.01x slower                                                 |
| docutils                         | 1.44 sec                                                   | 1.45 sec: 1.01x slower                                                |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 361 ms: 1.01x slower                                                  |
| pyflate                          | 321 ms                                                     | 324 ms: 1.01x slower                                                  |
| pycparser                        | 632 ms                                                     | 639 ms: 1.01x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.8 ms: 1.01x slower                                                 |
| sqlglot_optimize                 | 30.9 ms                                                    | 31.3 ms: 1.01x slower                                                 |
| sympy_expand                     | 226 ms                                                     | 228 ms: 1.01x slower                                                  |
| sqlglot_normalize                | 166 ms                                                     | 168 ms: 1.01x slower                                                  |
| unpickle_pure_python             | 141 us                                                     | 142 us: 1.01x slower                                                  |
| sqlglot_parse                    | 732 us                                                     | 741 us: 1.01x slower                                                  |
| raytrace                         | 147 ms                                                     | 149 ms: 1.01x slower                                                  |
| scimark_lu                       | 66.9 ms                                                    | 67.8 ms: 1.01x slower                                                 |
| sqlglot_transpile                | 891 us                                                     | 903 us: 1.01x slower                                                  |
| coroutines                       | 15.8 ms                                                    | 16.1 ms: 1.02x slower                                                 |
| genshi_xml                       | 29.9 ms                                                    | 30.4 ms: 1.02x slower                                                 |
| spectral_norm                    | 66.4 ms                                                    | 67.4 ms: 1.02x slower                                                 |
| mako                             | 6.99 ms                                                    | 7.10 ms: 1.02x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 336 ms: 1.02x slower                                                  |
| logging_silent                   | 60.1 ns                                                    | 61.1 ns: 1.02x slower                                                 |
| scimark_fft                      | 181 ms                                                     | 184 ms: 1.02x slower                                                  |
| logging_simple                   | 3.04 us                                                    | 3.10 us: 1.02x slower                                                 |
| scimark_monte_carlo              | 42.5 ms                                                    | 43.3 ms: 1.02x slower                                                 |
| nqueens                          | 52.2 ms                                                    | 53.3 ms: 1.02x slower                                                 |
| json_loads                       | 16.8 us                                                    | 17.2 us: 1.02x slower                                                 |
| xml_etree_generate               | 52.7 ms                                                    | 53.9 ms: 1.02x slower                                                 |
| xml_etree_process                | 37.1 ms                                                    | 37.9 ms: 1.02x slower                                                 |
| pickle_pure_python               | 179 us                                                     | 183 us: 1.03x slower                                                  |
| crypto_pyaes                     | 49.5 ms                                                    | 50.9 ms: 1.03x slower                                                 |
| django_template                  | 19.4 ms                                                    | 20.0 ms: 1.03x slower                                                 |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.15 sec: 1.03x slower                                                |
| telco                            | 4.60 ms                                                    | 4.75 ms: 1.03x slower                                                 |
| pathlib                          | 23.3 ms                                                    | 24.1 ms: 1.03x slower                                                 |
| xml_etree_iterparse              | 71.5 ms                                                    | 73.9 ms: 1.03x slower                                                 |
| json_dumps                       | 6.23 ms                                                    | 6.44 ms: 1.03x slower                                                 |
| bench_mp_pool                    | 47.2 ms                                                    | 48.9 ms: 1.04x slower                                                 |
| logging_format                   | 3.31 us                                                    | 3.44 us: 1.04x slower                                                 |
| xml_etree_parse                  | 106 ms                                                     | 110 ms: 1.04x slower                                                  |
| fannkuch                         | 248 ms                                                     | 261 ms: 1.05x slower                                                  |
| chaos                            | 34.0 ms                                                    | 35.8 ms: 1.05x slower                                                 |
| meteor_contest                   | 70.3 ms                                                    | 74.2 ms: 1.06x slower                                                 |
| typing_runtime_protocols         | 87.6 us                                                    | 92.6 us: 1.06x slower                                                 |
| async_tree_io                    | 563 ms                                                     | 597 ms: 1.06x slower                                                  |
| python_startup                   | 15.2 ms                                                    | 16.6 ms: 1.10x slower                                                 |
| python_startup_no_site           | 12.3 ms                                                    | 13.5 ms: 1.10x slower                                                 |
| tornado_http                     | 66.7 ms                                                    | 82.8 ms: 1.24x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.00x faster                                                          |

Benchmark hidden because not significant (15): async_tree_eager_memoization_tg, 2to3, sympy_sum, scimark_sparse_mat_mult, sympy_integrate, pidigits, float, create_gc_cycles, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_eager_memoization, asyncio_tcp, pylint
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.56% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.50x