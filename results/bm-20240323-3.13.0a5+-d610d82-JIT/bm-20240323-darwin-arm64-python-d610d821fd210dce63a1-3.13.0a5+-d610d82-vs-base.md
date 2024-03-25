# Results vs. base

- fork: python
- ref: d610d821fd210dce63a1
- machine: darwin-arm64
- commit hash: d610d82
- commit date: 2024-03-23
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.40x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240323-3.13.0a5+-d610d82/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json | results/bm-20240323-3.13.0a5+-d610d82-JIT/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 164 ms                                                                                                            | 176 ms: 1.07x slower                                                                                                  |
| chameleon      | 4.46 ms                                                                                                           | 4.41 ms: 1.01x faster                                                                                                 |
| docutils       | 1.48 sec                                                                                                          | 1.54 sec: 1.04x slower                                                                                                |
| html5lib       | 34.0 ms                                                                                                           | 32.0 ms: 1.06x faster                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.00x slower                                                                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | results/bm-20240323-3.13.0a5+-d610d82/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json | results/bm-20240323-3.13.0a5+-d610d82-JIT/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json |
|-------------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| async_tree_eager_tg           | 44.6 ms                                                                                                           | 44.7 ms: 1.00x slower                                                                                                 |
| async_tree_eager_cpu_io_mixed | 354 ms                                                                                                            | 356 ms: 1.01x slower                                                                                                  |
| async_tree_eager              | 64.3 ms                                                                                                           | 66.3 ms: 1.03x slower                                                                                                 |
| Geometric mean                | (ref)                                                                                                             | 1.00x slower                                                                                                          |

Benchmark hidden because not significant (13): async_tree_eager_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_io_tg, async_tree_none_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_none, async_tree_eager_io, async_tree_io, async_tree_memoization, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240323-3.13.0a5+-d610d82/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json | results/bm-20240323-3.13.0a5+-d610d82-JIT/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| float          | 51.2 ms                                                                                                           | 49.2 ms: 1.04x faster                                                                                                 |
| nbody          | 71.0 ms                                                                                                           | 70.2 ms: 1.01x faster                                                                                                 |
| pidigits       | 283 ms                                                                                                            | 282 ms: 1.00x faster                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.02x faster                                                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240323-3.13.0a5+-d610d82/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json | results/bm-20240323-3.13.0a5+-d610d82-JIT/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 152 ms                                                                                                            | 145 ms: 1.04x faster                                                                                                  |
| regex_v8       | 16.9 ms                                                                                                           | 16.9 ms: 1.00x slower                                                                                                 |
| regex_effbot   | 2.54 ms                                                                                                           | 2.55 ms: 1.00x slower                                                                                                 |
| regex_compile  | 70.0 ms                                                                                                           | 83.5 ms: 1.19x slower                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.04x slower                                                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240323-3.13.0a5+-d610d82/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json | results/bm-20240323-3.13.0a5+-d610d82-JIT/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.52 sec                                                                                                          | 1.28 sec: 1.18x faster                                                                                                |
| unpickle_pure_python | 148 us                                                                                                            | 142 us: 1.04x faster                                                                                                  |
| xml_etree_process    | 37.5 ms                                                                                                           | 36.7 ms: 1.02x faster                                                                                                 |
| xml_etree_generate   | 54.6 ms                                                                                                           | 54.0 ms: 1.01x faster                                                                                                 |
| pickle_pure_python   | 185 us                                                                                                            | 183 us: 1.01x faster                                                                                                  |
| pickle               | 7.25 us                                                                                                           | 7.20 us: 1.01x faster                                                                                                 |
| pickle_dict          | 18.1 us                                                                                                           | 18.1 us: 1.00x slower                                                                                                 |
| xml_etree_iterparse  | 69.6 ms                                                                                                           | 70.0 ms: 1.01x slower                                                                                                 |
| unpickle             | 9.17 us                                                                                                           | 9.25 us: 1.01x slower                                                                                                 |
| Geometric mean       | (ref)                                                                                                             | 1.02x faster                                                                                                          |

Benchmark hidden because not significant (5): xml_etree_parse, unpickle_list, json_loads, json_dumps, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240323-3.13.0a5+-d610d82/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json | results/bm-20240323-3.13.0a5+-d610d82-JIT/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 14.9 ms                                                                                                           | 18.9 ms: 1.27x slower                                                                                                 |
| python_startup_no_site | 13.0 ms                                                                                                           | 17.1 ms: 1.31x slower                                                                                                 |
| Geometric mean         | (ref)                                                                                                             | 1.29x slower                                                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240323-3.13.0a5+-d610d82/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json | results/bm-20240323-3.13.0a5+-d610d82-JIT/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako            | 7.06 ms                                                                                                           | 6.89 ms: 1.03x faster                                                                                                 |
| genshi_text     | 14.4 ms                                                                                                           | 14.6 ms: 1.01x slower                                                                                                 |
| django_template | 20.3 ms                                                                                                           | 20.8 ms: 1.02x slower                                                                                                 |
| genshi_xml      | 31.2 ms                                                                                                           | 32.9 ms: 1.06x slower                                                                                                 |
| Geometric mean  | (ref)                                                                                                             | 1.02x slower                                                                                                          |

All benchmarks:
===============

| Benchmark                     | results/bm-20240323-3.13.0a5+-d610d82/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json | results/bm-20240323-3.13.0a5+-d610d82-JIT/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json |
|-------------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| tomli_loads                   | 1.52 sec                                                                                                          | 1.28 sec: 1.18x faster                                                                                                |
| html5lib                      | 34.0 ms                                                                                                           | 32.0 ms: 1.06x faster                                                                                                 |
| regex_dna                     | 152 ms                                                                                                            | 145 ms: 1.04x faster                                                                                                  |
| unpickle_pure_python          | 148 us                                                                                                            | 142 us: 1.04x faster                                                                                                  |
| float                         | 51.2 ms                                                                                                           | 49.2 ms: 1.04x faster                                                                                                 |
| richards                      | 32.3 ms                                                                                                           | 31.4 ms: 1.03x faster                                                                                                 |
| fannkuch                      | 266 ms                                                                                                            | 259 ms: 1.03x faster                                                                                                  |
| mako                          | 7.06 ms                                                                                                           | 6.89 ms: 1.03x faster                                                                                                 |
| xml_etree_process             | 37.5 ms                                                                                                           | 36.7 ms: 1.02x faster                                                                                                 |
| richards_super                | 35.7 ms                                                                                                           | 35.0 ms: 1.02x faster                                                                                                 |
| coverage                      | 47.2 ms                                                                                                           | 46.5 ms: 1.01x faster                                                                                                 |
| thrift                        | 442 us                                                                                                            | 436 us: 1.01x faster                                                                                                  |
| chameleon                     | 4.46 ms                                                                                                           | 4.41 ms: 1.01x faster                                                                                                 |
| nbody                         | 71.0 ms                                                                                                           | 70.2 ms: 1.01x faster                                                                                                 |
| xml_etree_generate            | 54.6 ms                                                                                                           | 54.0 ms: 1.01x faster                                                                                                 |
| logging_simple                | 3.29 us                                                                                                           | 3.26 us: 1.01x faster                                                                                                 |
| pickle_pure_python            | 185 us                                                                                                            | 183 us: 1.01x faster                                                                                                  |
| pickle                        | 7.25 us                                                                                                           | 7.20 us: 1.01x faster                                                                                                 |
| crypto_pyaes                  | 47.1 ms                                                                                                           | 46.9 ms: 1.01x faster                                                                                                 |
| logging_format                | 3.55 us                                                                                                           | 3.54 us: 1.00x faster                                                                                                 |
| coroutines                    | 17.3 ms                                                                                                           | 17.2 ms: 1.00x faster                                                                                                 |
| scimark_monte_carlo           | 44.6 ms                                                                                                           | 44.5 ms: 1.00x faster                                                                                                 |
| pidigits                      | 283 ms                                                                                                            | 282 ms: 1.00x faster                                                                                                  |
| regex_v8                      | 16.9 ms                                                                                                           | 16.9 ms: 1.00x slower                                                                                                 |
| async_tree_eager_tg           | 44.6 ms                                                                                                           | 44.7 ms: 1.00x slower                                                                                                 |
| pickle_dict                   | 18.1 us                                                                                                           | 18.1 us: 1.00x slower                                                                                                 |
| regex_effbot                  | 2.54 ms                                                                                                           | 2.55 ms: 1.00x slower                                                                                                 |
| telco                         | 4.53 ms                                                                                                           | 4.55 ms: 1.00x slower                                                                                                 |
| gc_traversal                  | 2.39 ms                                                                                                           | 2.40 ms: 1.00x slower                                                                                                 |
| xml_etree_iterparse           | 69.6 ms                                                                                                           | 70.0 ms: 1.01x slower                                                                                                 |
| async_tree_eager_cpu_io_mixed | 354 ms                                                                                                            | 356 ms: 1.01x slower                                                                                                  |
| logging_silent                | 65.1 ns                                                                                                           | 65.6 ns: 1.01x slower                                                                                                 |
| json                          | 2.93 ms                                                                                                           | 2.96 ms: 1.01x slower                                                                                                 |
| unpickle                      | 9.17 us                                                                                                           | 9.25 us: 1.01x slower                                                                                                 |
| create_gc_cycles              | 712 us                                                                                                            | 719 us: 1.01x slower                                                                                                  |
| scimark_fft                   | 197 ms                                                                                                            | 199 ms: 1.01x slower                                                                                                  |
| deepcopy                      | 213 us                                                                                                            | 215 us: 1.01x slower                                                                                                  |
| genshi_text                   | 14.4 ms                                                                                                           | 14.6 ms: 1.01x slower                                                                                                 |
| dask                          | 222 ms                                                                                                            | 225 ms: 1.01x slower                                                                                                  |
| pycparser                     | 661 ms                                                                                                            | 670 ms: 1.01x slower                                                                                                  |
| sqlite_synth                  | 1.56 us                                                                                                           | 1.59 us: 1.02x slower                                                                                                 |
| django_template               | 20.3 ms                                                                                                           | 20.8 ms: 1.02x slower                                                                                                 |
| sqlglot_parse                 | 748 us                                                                                                            | 768 us: 1.03x slower                                                                                                  |
| deepcopy_memo                 | 23.6 us                                                                                                           | 24.2 us: 1.03x slower                                                                                                 |
| sqlglot_normalize             | 171 ms                                                                                                            | 176 ms: 1.03x slower                                                                                                  |
| meteor_contest                | 71.2 ms                                                                                                           | 73.3 ms: 1.03x slower                                                                                                 |
| mdp                           | 1.52 sec                                                                                                          | 1.57 sec: 1.03x slower                                                                                                |
| bench_thread_pool             | 477 us                                                                                                            | 491 us: 1.03x slower                                                                                                  |
| sympy_expand                  | 228 ms                                                                                                            | 236 ms: 1.03x slower                                                                                                  |
| async_tree_eager              | 64.3 ms                                                                                                           | 66.3 ms: 1.03x slower                                                                                                 |
| sqlglot_transpile             | 909 us                                                                                                            | 938 us: 1.03x slower                                                                                                  |
| chaos                         | 36.9 ms                                                                                                           | 38.1 ms: 1.03x slower                                                                                                 |
| scimark_sparse_mat_mult       | 3.02 ms                                                                                                           | 3.12 ms: 1.03x slower                                                                                                 |
| docutils                      | 1.48 sec                                                                                                          | 1.54 sec: 1.04x slower                                                                                                |
| dulwich_log                   | 28.6 ms                                                                                                           | 29.6 ms: 1.04x slower                                                                                                 |
| pprint_safe_repr              | 478 ms                                                                                                            | 497 ms: 1.04x slower                                                                                                  |
| go                            | 101 ms                                                                                                            | 105 ms: 1.04x slower                                                                                                  |
| deltablue                     | 2.27 ms                                                                                                           | 2.36 ms: 1.04x slower                                                                                                 |
| aiohttp                       | 1.07 ms                                                                                                           | 1.11 ms: 1.04x slower                                                                                                 |
| spectral_norm                 | 71.3 ms                                                                                                           | 74.5 ms: 1.05x slower                                                                                                 |
| async_generators              | 286 ms                                                                                                            | 301 ms: 1.05x slower                                                                                                  |
| mypy2                         | 466 ms                                                                                                            | 490 ms: 1.05x slower                                                                                                  |
| pprint_pformat                | 972 ms                                                                                                            | 1.02 sec: 1.05x slower                                                                                                |
| genshi_xml                    | 31.2 ms                                                                                                           | 32.9 ms: 1.06x slower                                                                                                 |
| sympy_str                     | 132 ms                                                                                                            | 140 ms: 1.06x slower                                                                                                  |
| sqlglot_optimize              | 31.9 ms                                                                                                           | 33.7 ms: 1.06x slower                                                                                                 |
| scimark_sor                   | 100 ms                                                                                                            | 107 ms: 1.07x slower                                                                                                  |
| 2to3                          | 164 ms                                                                                                            | 176 ms: 1.07x slower                                                                                                  |
| comprehensions                | 11.2 us                                                                                                           | 12.0 us: 1.07x slower                                                                                                 |
| gunicorn                      | 1.08 ms                                                                                                           | 1.16 ms: 1.07x slower                                                                                                 |
| sympy_sum                     | 70.0 ms                                                                                                           | 76.0 ms: 1.08x slower                                                                                                 |
| sympy_integrate               | 10.3 ms                                                                                                           | 11.2 ms: 1.09x slower                                                                                                 |
| nqueens                       | 55.9 ms                                                                                                           | 61.2 ms: 1.09x slower                                                                                                 |
| bench_mp_pool                 | 45.1 ms                                                                                                           | 51.2 ms: 1.13x slower                                                                                                 |
| raytrace                      | 156 ms                                                                                                            | 178 ms: 1.14x slower                                                                                                  |
| hexiom                        | 4.20 ms                                                                                                           | 4.86 ms: 1.16x slower                                                                                                 |
| scimark_lu                    | 68.5 ms                                                                                                           | 81.0 ms: 1.18x slower                                                                                                 |
| regex_compile                 | 70.0 ms                                                                                                           | 83.5 ms: 1.19x slower                                                                                                 |
| python_startup                | 14.9 ms                                                                                                           | 18.9 ms: 1.27x slower                                                                                                 |
| python_startup_no_site        | 13.0 ms                                                                                                           | 17.1 ms: 1.31x slower                                                                                                 |
| unpack_sequence               | 26.5 ns                                                                                                           | 113 ns: 4.25x slower                                                                                                  |
| Geometric mean                | (ref)                                                                                                             | 1.04x slower                                                                                                          |

Benchmark hidden because not significant (28): tornado_http, async_tree_eager_memoization_tg, xml_etree_parse, async_tree_cpu_io_mixed_tg, unpickle_list, async_tree_eager_io_tg, async_tree_io_tg, pathlib, async_tree_none_tg, asyncio_tcp_ssl, json_loads, json_dumps, generators, async_tree_eager_cpu_io_mixed_tg, pyflate, deepcopy_reduce, asyncio_websockets, async_tree_cpu_io_mixed, typing_runtime_protocols, pickle_list, async_tree_memoization_tg, async_tree_none, async_tree_eager_io, async_tree_io, async_tree_memoization, async_tree_eager_memoization, asyncio_tcp, pylint


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: 1.40x