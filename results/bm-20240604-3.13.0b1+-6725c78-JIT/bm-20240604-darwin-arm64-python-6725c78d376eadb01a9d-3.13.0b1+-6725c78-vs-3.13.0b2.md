# Results vs. 3.13.0b2

- fork: python
- ref: 6725c78d376eadb01a9d
- machine: darwin-arm64
- commit hash: 6725c78
- commit date: 2024-06-04
- overall geometric mean: 1.02x slower
- HPT reliability: 99.75%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.61x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 172 ms: 1.07x slower                                                   |
| chameleon      | 4.27 ms                                                    | 4.41 ms: 1.03x slower                                                  |
| docutils       | 1.44 sec                                                   | 1.50 sec: 1.05x slower                                                 |
| html5lib       | 31.2 ms                                                    | 31.9 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                      | 1.04x slower                                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 741 ms: 1.03x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 332 ms: 1.00x slower                                                   |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 361 ms: 1.01x slower                                                   |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.1 ms: 1.02x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 63.3 ms: 1.05x slower                                                  |
| Geometric mean                   | (ref)                                                      | 1.00x faster                                                           |

Benchmark hidden because not significant (11): async_tree_io_tg, async_tree_io, async_tree_eager_io_tg, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_eager_memoization_tg, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 47.4 ms: 1.03x faster                                                  |
| nbody          | 59.6 ms                                                    | 63.6 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                      | 1.01x slower                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.56 ms: 1.01x faster                                                  |
| regex_dna      | 149 ms                                                     | 149 ms: 1.00x faster                                                   |
| regex_v8       | 17.3 ms                                                    | 17.3 ms: 1.00x slower                                                  |
| regex_compile  | 68.5 ms                                                    | 72.7 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                      | 1.01x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                   | 1.25 sec: 1.17x faster                                                 |
| unpickle_pure_python | 141 us                                                     | 131 us: 1.08x faster                                                   |
| xml_etree_parse      | 106 ms                                                     | 102 ms: 1.04x faster                                                   |
| xml_etree_process    | 37.1 ms                                                    | 35.9 ms: 1.03x faster                                                  |
| pickle_pure_python   | 179 us                                                     | 173 us: 1.03x faster                                                   |
| xml_etree_generate   | 52.7 ms                                                    | 51.4 ms: 1.02x faster                                                  |
| json_dumps           | 6.23 ms                                                    | 6.11 ms: 1.02x faster                                                  |
| xml_etree_iterparse  | 71.5 ms                                                    | 70.3 ms: 1.02x faster                                                  |
| pickle_dict          | 18.3 us                                                    | 18.2 us: 1.00x faster                                                  |
| json_loads           | 16.8 us                                                    | 16.9 us: 1.00x slower                                                  |
| pickle_list          | 2.96 us                                                    | 2.99 us: 1.01x slower                                                  |
| Geometric mean       | (ref)                                                      | 1.03x faster                                                           |

Benchmark hidden because not significant (3): unpickle_list, unpickle, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 15.6 ms: 1.03x slower                                                  |
| python_startup_no_site | 12.3 ms                                                    | 12.7 ms: 1.03x slower                                                  |
| Geometric mean         | (ref)                                                      | 1.03x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 6.37 ms: 1.10x faster                                                  |
| django_template | 19.4 ms                                                    | 21.3 ms: 1.10x slower                                                  |
| genshi_text     | 13.9 ms                                                    | 16.0 ms: 1.15x slower                                                  |
| genshi_xml      | 29.9 ms                                                    | 39.5 ms: 1.32x slower                                                  |
| Geometric mean  | (ref)                                                      | 1.11x slower                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads                      | 1.47 sec                                                   | 1.25 sec: 1.17x faster                                                 |
| flaskblogging                    | 3.61 ms                                                    | 3.25 ms: 1.11x faster                                                  |
| mako                             | 6.99 ms                                                    | 6.37 ms: 1.10x faster                                                  |
| unpickle_pure_python             | 141 us                                                     | 131 us: 1.08x faster                                                   |
| mdp                              | 1.53 sec                                                   | 1.44 sec: 1.07x faster                                                 |
| fannkuch                         | 248 ms                                                     | 235 ms: 1.06x faster                                                   |
| deepcopy_memo                    | 22.6 us                                                    | 21.7 us: 1.04x faster                                                  |
| asyncio_tcp_ssl                  | 1.29 sec                                                   | 1.24 sec: 1.04x faster                                                 |
| xml_etree_parse                  | 106 ms                                                     | 102 ms: 1.04x faster                                                   |
| async_tree_eager_io              | 766 ms                                                     | 741 ms: 1.03x faster                                                   |
| xml_etree_process                | 37.1 ms                                                    | 35.9 ms: 1.03x faster                                                  |
| pickle_pure_python               | 179 us                                                     | 173 us: 1.03x faster                                                   |
| pathlib                          | 23.3 ms                                                    | 22.7 ms: 1.03x faster                                                  |
| float                            | 48.6 ms                                                    | 47.4 ms: 1.03x faster                                                  |
| xml_etree_generate               | 52.7 ms                                                    | 51.4 ms: 1.02x faster                                                  |
| pyflate                          | 321 ms                                                     | 314 ms: 1.02x faster                                                   |
| json_dumps                       | 6.23 ms                                                    | 6.11 ms: 1.02x faster                                                  |
| xml_etree_iterparse              | 71.5 ms                                                    | 70.3 ms: 1.02x faster                                                  |
| pprint_safe_repr                 | 465 ms                                                     | 459 ms: 1.01x faster                                                   |
| telco                            | 4.60 ms                                                    | 4.55 ms: 1.01x faster                                                  |
| richards                         | 31.8 ms                                                    | 31.5 ms: 1.01x faster                                                  |
| regex_effbot                     | 2.58 ms                                                    | 2.56 ms: 1.01x faster                                                  |
| deepcopy_reduce                  | 1.82 us                                                    | 1.82 us: 1.00x faster                                                  |
| pickle_dict                      | 18.3 us                                                    | 18.2 us: 1.00x faster                                                  |
| regex_dna                        | 149 ms                                                     | 149 ms: 1.00x faster                                                   |
| asyncio_websockets               | 409 ms                                                     | 408 ms: 1.00x faster                                                   |
| coroutines                       | 15.8 ms                                                    | 15.9 ms: 1.00x slower                                                  |
| coverage                         | 45.0 ms                                                    | 45.1 ms: 1.00x slower                                                  |
| json_loads                       | 16.8 us                                                    | 16.9 us: 1.00x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 332 ms: 1.00x slower                                                   |
| regex_v8                         | 17.3 ms                                                    | 17.3 ms: 1.00x slower                                                  |
| gc_traversal                     | 2.45 ms                                                    | 2.46 ms: 1.00x slower                                                  |
| generators                       | 22.9 ms                                                    | 23.0 ms: 1.00x slower                                                  |
| thrift                           | 435 us                                                     | 437 us: 1.00x slower                                                   |
| logging_simple                   | 3.04 us                                                    | 3.07 us: 1.01x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 361 ms: 1.01x slower                                                   |
| logging_format                   | 3.31 us                                                    | 3.35 us: 1.01x slower                                                  |
| spectral_norm                    | 66.4 ms                                                    | 67.1 ms: 1.01x slower                                                  |
| sqlite_synth                     | 1.55 us                                                    | 1.57 us: 1.01x slower                                                  |
| pickle_list                      | 2.96 us                                                    | 2.99 us: 1.01x slower                                                  |
| create_gc_cycles                 | 897 us                                                     | 909 us: 1.01x slower                                                   |
| deepcopy                         | 204 us                                                     | 207 us: 1.02x slower                                                   |
| meteor_contest                   | 70.3 ms                                                    | 71.5 ms: 1.02x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.1 ms: 1.02x slower                                                  |
| html5lib                         | 31.2 ms                                                    | 31.9 ms: 1.02x slower                                                  |
| scimark_fft                      | 181 ms                                                     | 186 ms: 1.03x slower                                                   |
| go                               | 101 ms                                                     | 103 ms: 1.03x slower                                                   |
| python_startup                   | 15.2 ms                                                    | 15.6 ms: 1.03x slower                                                  |
| python_startup_no_site           | 12.3 ms                                                    | 12.7 ms: 1.03x slower                                                  |
| chameleon                        | 4.27 ms                                                    | 4.41 ms: 1.03x slower                                                  |
| logging_silent                   | 60.1 ns                                                    | 62.2 ns: 1.03x slower                                                  |
| scimark_monte_carlo              | 42.5 ms                                                    | 44.0 ms: 1.04x slower                                                  |
| sympy_sum                        | 69.2 ms                                                    | 71.9 ms: 1.04x slower                                                  |
| aiohttp                          | 997 us                                                     | 1.04 ms: 1.04x slower                                                  |
| sympy_str                        | 131 ms                                                     | 137 ms: 1.04x slower                                                   |
| sympy_expand                     | 226 ms                                                     | 236 ms: 1.05x slower                                                   |
| docutils                         | 1.44 sec                                                   | 1.50 sec: 1.05x slower                                                 |
| crypto_pyaes                     | 49.5 ms                                                    | 51.9 ms: 1.05x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 63.3 ms: 1.05x slower                                                  |
| sympy_integrate                  | 10.3 ms                                                    | 10.9 ms: 1.05x slower                                                  |
| dulwich_log                      | 27.6 ms                                                    | 29.0 ms: 1.05x slower                                                  |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.92 ms: 1.05x slower                                                  |
| async_generators                 | 281 ms                                                     | 296 ms: 1.05x slower                                                   |
| sqlglot_optimize                 | 30.9 ms                                                    | 32.7 ms: 1.06x slower                                                  |
| bench_mp_pool                    | 47.2 ms                                                    | 49.9 ms: 1.06x slower                                                  |
| regex_compile                    | 68.5 ms                                                    | 72.7 ms: 1.06x slower                                                  |
| pycparser                        | 632 ms                                                     | 672 ms: 1.06x slower                                                   |
| typing_runtime_protocols         | 87.6 us                                                    | 93.1 us: 1.06x slower                                                  |
| mypy2                            | 379 ms                                                     | 404 ms: 1.06x slower                                                   |
| scimark_sor                      | 94.9 ms                                                    | 101 ms: 1.07x slower                                                   |
| nbody                            | 59.6 ms                                                    | 63.6 ms: 1.07x slower                                                  |
| 2to3                             | 161 ms                                                     | 172 ms: 1.07x slower                                                   |
| bench_thread_pool                | 447 us                                                     | 478 us: 1.07x slower                                                   |
| gunicorn                         | 1.04 ms                                                    | 1.11 ms: 1.07x slower                                                  |
| hexiom                           | 4.06 ms                                                    | 4.37 ms: 1.08x slower                                                  |
| nqueens                          | 52.2 ms                                                    | 56.8 ms: 1.09x slower                                                  |
| django_template                  | 19.4 ms                                                    | 21.3 ms: 1.10x slower                                                  |
| raytrace                         | 147 ms                                                     | 164 ms: 1.12x slower                                                   |
| sqlglot_transpile                | 891 us                                                     | 1.01 ms: 1.13x slower                                                  |
| sqlglot_parse                    | 732 us                                                     | 831 us: 1.14x slower                                                   |
| genshi_text                      | 13.9 ms                                                    | 16.0 ms: 1.15x slower                                                  |
| chaos                            | 34.0 ms                                                    | 39.1 ms: 1.15x slower                                                  |
| deltablue                        | 2.14 ms                                                    | 2.48 ms: 1.16x slower                                                  |
| scimark_lu                       | 66.9 ms                                                    | 78.7 ms: 1.18x slower                                                  |
| comprehensions                   | 10.2 us                                                    | 12.2 us: 1.20x slower                                                  |
| genshi_xml                       | 29.9 ms                                                    | 39.5 ms: 1.32x slower                                                  |
| Geometric mean                   | (ref)                                                      | 1.02x slower                                                           |

Benchmark hidden because not significant (22): async_tree_io_tg, async_tree_io, async_tree_eager_io_tg, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_memoization, unpickle_list, async_tree_none, async_tree_cpu_io_mixed_tg, unpickle, dask, richards_super, json, pidigits, pprint_pformat, pickle, async_tree_eager_memoization_tg, async_tree_eager_memoization, tornado_http, asyncio_tcp, pylint
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser, sqlglot_normalize

# HPT report

- Reliability score: 99.75% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.61x