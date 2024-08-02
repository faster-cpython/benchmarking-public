# Results vs. base

- fork: python
- ref: c15f94d6fbc960790db3
- machine: darwin-arm64
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240608-3.13.0b2+-c15f94d/bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json | results/bm-20240608-3.13.0b2+-c15f94d-JIT/bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 160 ms                                                                                                            | 172 ms: 1.07x slower                                                                                                  |
| chameleon      | 4.33 ms                                                                                                           | 4.47 ms: 1.03x slower                                                                                                 |
| docutils       | 1.44 sec                                                                                                          | 1.50 sec: 1.05x slower                                                                                                |
| html5lib       | 31.2 ms                                                                                                           | 30.9 ms: 1.01x faster                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.03x slower                                                                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | results/bm-20240608-3.13.0b2+-c15f94d/bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json | results/bm-20240608-3.13.0b2+-c15f94d-JIT/bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json |
|----------------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                                                                            | 332 ms: 1.01x slower                                                                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                                                                            | 361 ms: 1.01x slower                                                                                                  |
| async_tree_eager_tg              | 41.0 ms                                                                                                           | 42.1 ms: 1.03x slower                                                                                                 |
| async_tree_eager                 | 60.6 ms                                                                                                           | 63.2 ms: 1.04x slower                                                                                                 |
| Geometric mean                   | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (12): async_tree_io_tg, async_tree_eager_io, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_none_tg, async_tree_memoization_tg, async_tree_memoization, async_tree_none, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240608-3.13.0b2+-c15f94d/bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json | results/bm-20240608-3.13.0b2+-c15f94d-JIT/bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| float          | 48.3 ms                                                                                                           | 47.5 ms: 1.02x faster                                                                                                 |
| nbody          | 59.7 ms                                                                                                           | 63.7 ms: 1.07x slower                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.02x slower                                                                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240608-3.13.0b2+-c15f94d/bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json | results/bm-20240608-3.13.0b2+-c15f94d-JIT/bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 151 ms                                                                                                            | 149 ms: 1.01x faster                                                                                                  |
| regex_effbot   | 2.58 ms                                                                                                           | 2.56 ms: 1.01x faster                                                                                                 |
| regex_v8       | 17.2 ms                                                                                                           | 17.4 ms: 1.01x slower                                                                                                 |
| regex_compile  | 68.3 ms                                                                                                           | 72.5 ms: 1.06x slower                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240608-3.13.0b2+-c15f94d/bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json | results/bm-20240608-3.13.0b2+-c15f94d-JIT/bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                                                                          | 1.26 sec: 1.17x faster                                                                                                |
| unpickle_pure_python | 141 us                                                                                                            | 131 us: 1.07x faster                                                                                                  |
| pickle_pure_python   | 179 us                                                                                                            | 172 us: 1.04x faster                                                                                                  |
| xml_etree_process    | 36.9 ms                                                                                                           | 35.9 ms: 1.03x faster                                                                                                 |
| xml_etree_parse      | 104 ms                                                                                                            | 102 ms: 1.02x faster                                                                                                  |
| xml_etree_iterparse  | 71.1 ms                                                                                                           | 69.9 ms: 1.02x faster                                                                                                 |
| xml_etree_generate   | 52.5 ms                                                                                                           | 51.7 ms: 1.02x faster                                                                                                 |
| unpickle_list        | 2.91 us                                                                                                           | 2.88 us: 1.01x faster                                                                                                 |
| pickle               | 7.46 us                                                                                                           | 7.40 us: 1.01x faster                                                                                                 |
| json_dumps           | 6.21 ms                                                                                                           | 6.17 ms: 1.01x faster                                                                                                 |
| json_loads           | 16.9 us                                                                                                           | 16.9 us: 1.00x slower                                                                                                 |
| pickle_dict          | 18.3 us                                                                                                           | 18.4 us: 1.01x slower                                                                                                 |
| unpickle             | 9.13 us                                                                                                           | 9.20 us: 1.01x slower                                                                                                 |
| Geometric mean       | (ref)                                                                                                             | 1.03x faster                                                                                                          |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240608-3.13.0b2+-c15f94d/bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json | results/bm-20240608-3.13.0b2+-c15f94d-JIT/bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 14.4 ms                                                                                                           | 15.6 ms: 1.09x slower                                                                                                 |
| python_startup_no_site | 11.5 ms                                                                                                           | 12.7 ms: 1.11x slower                                                                                                 |
| Geometric mean         | (ref)                                                                                                             | 1.10x slower                                                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240608-3.13.0b2+-c15f94d/bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json | results/bm-20240608-3.13.0b2+-c15f94d-JIT/bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako            | 7.00 ms                                                                                                           | 6.37 ms: 1.10x faster                                                                                                 |
| django_template | 19.4 ms                                                                                                           | 21.3 ms: 1.10x slower                                                                                                 |
| genshi_text     | 13.8 ms                                                                                                           | 16.3 ms: 1.18x slower                                                                                                 |
| genshi_xml      | 30.1 ms                                                                                                           | 39.1 ms: 1.30x slower                                                                                                 |
| Geometric mean  | (ref)                                                                                                             | 1.11x slower                                                                                                          |

All benchmarks:
===============

| Benchmark                        | results/bm-20240608-3.13.0b2+-c15f94d/bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json | results/bm-20240608-3.13.0b2+-c15f94d-JIT/bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json |
|----------------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| tomli_loads                      | 1.47 sec                                                                                                          | 1.26 sec: 1.17x faster                                                                                                |
| asyncio_tcp                      | 423 ms                                                                                                            | 382 ms: 1.11x faster                                                                                                  |
| mako                             | 7.00 ms                                                                                                           | 6.37 ms: 1.10x faster                                                                                                 |
| unpickle_pure_python             | 141 us                                                                                                            | 131 us: 1.07x faster                                                                                                  |
| fannkuch                         | 248 ms                                                                                                            | 233 ms: 1.06x faster                                                                                                  |
| deepcopy_memo                    | 22.7 us                                                                                                           | 21.6 us: 1.05x faster                                                                                                 |
| pickle_pure_python               | 179 us                                                                                                            | 172 us: 1.04x faster                                                                                                  |
| xml_etree_process                | 36.9 ms                                                                                                           | 35.9 ms: 1.03x faster                                                                                                 |
| xml_etree_parse                  | 104 ms                                                                                                            | 102 ms: 1.02x faster                                                                                                  |
| pyflate                          | 319 ms                                                                                                            | 313 ms: 1.02x faster                                                                                                  |
| float                            | 48.3 ms                                                                                                           | 47.5 ms: 1.02x faster                                                                                                 |
| xml_etree_iterparse              | 71.1 ms                                                                                                           | 69.9 ms: 1.02x faster                                                                                                 |
| xml_etree_generate               | 52.5 ms                                                                                                           | 51.7 ms: 1.02x faster                                                                                                 |
| pprint_safe_repr                 | 466 ms                                                                                                            | 460 ms: 1.01x faster                                                                                                  |
| regex_dna                        | 151 ms                                                                                                            | 149 ms: 1.01x faster                                                                                                  |
| unpickle_list                    | 2.91 us                                                                                                           | 2.88 us: 1.01x faster                                                                                                 |
| html5lib                         | 31.2 ms                                                                                                           | 30.9 ms: 1.01x faster                                                                                                 |
| telco                            | 4.61 ms                                                                                                           | 4.56 ms: 1.01x faster                                                                                                 |
| pickle                           | 7.46 us                                                                                                           | 7.40 us: 1.01x faster                                                                                                 |
| json_dumps                       | 6.21 ms                                                                                                           | 6.17 ms: 1.01x faster                                                                                                 |
| regex_effbot                     | 2.58 ms                                                                                                           | 2.56 ms: 1.01x faster                                                                                                 |
| json_loads                       | 16.9 us                                                                                                           | 16.9 us: 1.00x slower                                                                                                 |
| gc_traversal                     | 2.46 ms                                                                                                           | 2.46 ms: 1.00x slower                                                                                                 |
| logging_simple                   | 3.05 us                                                                                                           | 3.06 us: 1.00x slower                                                                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                                                                            | 332 ms: 1.01x slower                                                                                                  |
| regex_v8                         | 17.2 ms                                                                                                           | 17.4 ms: 1.01x slower                                                                                                 |
| pickle_dict                      | 18.3 us                                                                                                           | 18.4 us: 1.01x slower                                                                                                 |
| logging_format                   | 3.32 us                                                                                                           | 3.35 us: 1.01x slower                                                                                                 |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                                                                            | 361 ms: 1.01x slower                                                                                                  |
| unpickle                         | 9.13 us                                                                                                           | 9.20 us: 1.01x slower                                                                                                 |
| create_gc_cycles                 | 898 us                                                                                                            | 906 us: 1.01x slower                                                                                                  |
| spectral_norm                    | 66.5 ms                                                                                                           | 67.2 ms: 1.01x slower                                                                                                 |
| coroutines                       | 15.9 ms                                                                                                           | 16.0 ms: 1.01x slower                                                                                                 |
| sqlite_synth                     | 1.55 us                                                                                                           | 1.57 us: 1.01x slower                                                                                                 |
| thrift                           | 432 us                                                                                                            | 437 us: 1.01x slower                                                                                                  |
| deepcopy_reduce                  | 1.82 us                                                                                                           | 1.84 us: 1.01x slower                                                                                                 |
| dask                             | 218 ms                                                                                                            | 221 ms: 1.01x slower                                                                                                  |
| coverage                         | 45.0 ms                                                                                                           | 45.9 ms: 1.02x slower                                                                                                 |
| meteor_contest                   | 70.3 ms                                                                                                           | 71.7 ms: 1.02x slower                                                                                                 |
| scimark_fft                      | 181 ms                                                                                                            | 185 ms: 1.02x slower                                                                                                  |
| deepcopy                         | 204 us                                                                                                            | 209 us: 1.02x slower                                                                                                  |
| generators                       | 22.8 ms                                                                                                           | 23.4 ms: 1.03x slower                                                                                                 |
| pathlib                          | 22.0 ms                                                                                                           | 22.6 ms: 1.03x slower                                                                                                 |
| async_tree_eager_tg              | 41.0 ms                                                                                                           | 42.1 ms: 1.03x slower                                                                                                 |
| mdp                              | 1.40 sec                                                                                                          | 1.44 sec: 1.03x slower                                                                                                |
| chameleon                        | 4.33 ms                                                                                                           | 4.47 ms: 1.03x slower                                                                                                 |
| richards                         | 31.7 ms                                                                                                           | 32.7 ms: 1.03x slower                                                                                                 |
| aiohttp                          | 1.01 ms                                                                                                           | 1.04 ms: 1.03x slower                                                                                                 |
| go                               | 100 ms                                                                                                            | 104 ms: 1.03x slower                                                                                                  |
| sympy_str                        | 132 ms                                                                                                            | 137 ms: 1.03x slower                                                                                                  |
| flaskblogging                    | 3.13 ms                                                                                                           | 3.24 ms: 1.04x slower                                                                                                 |
| logging_silent                   | 60.3 ns                                                                                                           | 62.6 ns: 1.04x slower                                                                                                 |
| gunicorn                         | 1.07 ms                                                                                                           | 1.11 ms: 1.04x slower                                                                                                 |
| sympy_sum                        | 69.0 ms                                                                                                           | 71.7 ms: 1.04x slower                                                                                                 |
| scimark_monte_carlo              | 42.5 ms                                                                                                           | 44.2 ms: 1.04x slower                                                                                                 |
| bench_thread_pool                | 458 us                                                                                                            | 477 us: 1.04x slower                                                                                                  |
| async_tree_eager                 | 60.6 ms                                                                                                           | 63.2 ms: 1.04x slower                                                                                                 |
| sympy_expand                     | 226 ms                                                                                                            | 235 ms: 1.04x slower                                                                                                  |
| docutils                         | 1.44 sec                                                                                                          | 1.50 sec: 1.05x slower                                                                                                |
| richards_super                   | 35.3 ms                                                                                                           | 36.9 ms: 1.05x slower                                                                                                 |
| crypto_pyaes                     | 49.4 ms                                                                                                           | 51.8 ms: 1.05x slower                                                                                                 |
| sympy_integrate                  | 10.4 ms                                                                                                           | 10.9 ms: 1.05x slower                                                                                                 |
| async_generators                 | 281 ms                                                                                                            | 296 ms: 1.05x slower                                                                                                  |
| scimark_sparse_mat_mult          | 2.77 ms                                                                                                           | 2.92 ms: 1.05x slower                                                                                                 |
| sqlglot_optimize                 | 31.0 ms                                                                                                           | 32.7 ms: 1.05x slower                                                                                                 |
| pycparser                        | 633 ms                                                                                                            | 668 ms: 1.06x slower                                                                                                  |
| bench_mp_pool                    | 46.9 ms                                                                                                           | 49.6 ms: 1.06x slower                                                                                                 |
| dulwich_log                      | 27.5 ms                                                                                                           | 29.2 ms: 1.06x slower                                                                                                 |
| typing_runtime_protocols         | 88.0 us                                                                                                           | 93.4 us: 1.06x slower                                                                                                 |
| regex_compile                    | 68.3 ms                                                                                                           | 72.5 ms: 1.06x slower                                                                                                 |
| scimark_sor                      | 94.9 ms                                                                                                           | 101 ms: 1.07x slower                                                                                                  |
| nbody                            | 59.7 ms                                                                                                           | 63.7 ms: 1.07x slower                                                                                                 |
| 2to3                             | 160 ms                                                                                                            | 172 ms: 1.07x slower                                                                                                  |
| pylint                           | 167 ms                                                                                                            | 180 ms: 1.07x slower                                                                                                  |
| mypy2                            | 376 ms                                                                                                            | 405 ms: 1.08x slower                                                                                                  |
| hexiom                           | 4.07 ms                                                                                                           | 4.38 ms: 1.08x slower                                                                                                 |
| nqueens                          | 52.5 ms                                                                                                           | 56.7 ms: 1.08x slower                                                                                                 |
| python_startup                   | 14.4 ms                                                                                                           | 15.6 ms: 1.09x slower                                                                                                 |
| django_template                  | 19.4 ms                                                                                                           | 21.3 ms: 1.10x slower                                                                                                 |
| python_startup_no_site           | 11.5 ms                                                                                                           | 12.7 ms: 1.11x slower                                                                                                 |
| raytrace                         | 147 ms                                                                                                            | 163 ms: 1.11x slower                                                                                                  |
| sqlglot_transpile                | 891 us                                                                                                            | 1.00 ms: 1.12x slower                                                                                                 |
| sqlglot_parse                    | 732 us                                                                                                            | 828 us: 1.13x slower                                                                                                  |
| chaos                            | 34.1 ms                                                                                                           | 39.2 ms: 1.15x slower                                                                                                 |
| deltablue                        | 2.14 ms                                                                                                           | 2.50 ms: 1.17x slower                                                                                                 |
| genshi_text                      | 13.8 ms                                                                                                           | 16.3 ms: 1.18x slower                                                                                                 |
| scimark_lu                       | 66.7 ms                                                                                                           | 79.0 ms: 1.18x slower                                                                                                 |
| comprehensions                   | 10.2 us                                                                                                           | 12.3 us: 1.21x slower                                                                                                 |
| genshi_xml                       | 30.1 ms                                                                                                           | 39.1 ms: 1.30x slower                                                                                                 |
| Geometric mean                   | (ref)                                                                                                             | 1.03x slower                                                                                                          |

Benchmark hidden because not significant (19): async_tree_io_tg, async_tree_eager_io, async_tree_io, asyncio_tcp_ssl, asyncio_websockets, pidigits, pprint_pformat, pickle_list, json, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_none_tg, async_tree_memoization_tg, async_tree_memoization, async_tree_none, async_tree_eager_memoization, tornado_http
Ignored benchmarks (1) of results/bm-20240608-3.13.0b2+-c15f94d/bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json: sqlglot_normalize

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.31x