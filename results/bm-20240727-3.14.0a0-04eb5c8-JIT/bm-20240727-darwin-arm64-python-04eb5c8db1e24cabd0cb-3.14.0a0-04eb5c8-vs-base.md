# Results vs. base

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: darwin-arm64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.02x slower
- HPT reliability: 99.68%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 163 ms                                                                                                          | 171 ms: 1.05x slower                                                                                                |
| docutils       | 1.49 sec                                                                                                        | 1.53 sec: 1.03x slower                                                                                              |
| html5lib       | 31.5 ms                                                                                                         | 30.6 ms: 1.03x faster                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.02x slower                                                                                                        |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|----------------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| async_tree_eager_cpu_io_mixed_tg | 333 ms                                                                                                          | 332 ms: 1.00x faster                                                                                                |
| async_generators                 | 281 ms                                                                                                          | 292 ms: 1.04x slower                                                                                                |
| Geometric mean                   | (ref)                                                                                                           | 1.00x slower                                                                                                        |

Benchmark hidden because not significant (19): async_tree_io_tg, async_tree_none_tg, async_tree_eager_io, async_tree_io, async_tree_eager_memoization_tg, async_tree_none, async_tree_eager_cpu_io_mixed, async_tree_eager_io_tg, async_tree_cpu_io_mixed_tg, coroutines, asyncio_websockets, async_tree_memoization, async_tree_eager_tg, async_tree_eager, asyncio_tcp_ssl, async_tree_eager_memoization, async_tree_cpu_io_mixed, async_tree_memoization_tg, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| float          | 48.1 ms                                                                                                         | 45.9 ms: 1.05x faster                                                                                               |
| pidigits       | 281 ms                                                                                                          | 282 ms: 1.00x slower                                                                                                |
| nbody          | 61.7 ms                                                                                                         | 63.0 ms: 1.02x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.01x faster                                                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 149 ms                                                                                                          | 149 ms: 1.00x faster                                                                                                |
| regex_effbot   | 2.54 ms                                                                                                         | 2.56 ms: 1.01x slower                                                                                               |
| regex_compile  | 68.4 ms                                                                                                         | 72.8 ms: 1.06x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.02x slower                                                                                                        |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.48 sec                                                                                                        | 1.24 sec: 1.19x faster                                                                                              |
| unpickle_pure_python | 144 us                                                                                                          | 133 us: 1.08x faster                                                                                                |
| pickle_pure_python   | 182 us                                                                                                          | 171 us: 1.06x faster                                                                                                |
| xml_etree_process    | 37.4 ms                                                                                                         | 35.4 ms: 1.06x faster                                                                                               |
| xml_etree_iterparse  | 72.6 ms                                                                                                         | 70.9 ms: 1.02x faster                                                                                               |
| xml_etree_parse      | 106 ms                                                                                                          | 104 ms: 1.02x faster                                                                                                |
| xml_etree_generate   | 53.0 ms                                                                                                         | 52.0 ms: 1.02x faster                                                                                               |
| Geometric mean       | (ref)                                                                                                           | 1.05x faster                                                                                                        |

Benchmark hidden because not significant (2): json_loads, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                                                                         | 15.3 ms: 1.01x slower                                                                                               |
| python_startup_no_site | 12.5 ms                                                                                                         | 12.7 ms: 1.02x slower                                                                                               |
| Geometric mean         | (ref)                                                                                                           | 1.01x slower                                                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| mako            | 7.04 ms                                                                                                         | 6.39 ms: 1.10x faster                                                                                               |
| django_template | 19.7 ms                                                                                                         | 21.1 ms: 1.07x slower                                                                                               |
| genshi_text     | 14.2 ms                                                                                                         | 16.5 ms: 1.16x slower                                                                                               |
| genshi_xml      | 30.3 ms                                                                                                         | 40.4 ms: 1.33x slower                                                                                               |
| Geometric mean  | (ref)                                                                                                           | 1.11x slower                                                                                                        |

All benchmarks:
===============

| Benchmark                        | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|----------------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| tomli_loads                      | 1.48 sec                                                                                                        | 1.24 sec: 1.19x faster                                                                                              |
| mako                             | 7.04 ms                                                                                                         | 6.39 ms: 1.10x faster                                                                                               |
| unpickle_pure_python             | 144 us                                                                                                          | 133 us: 1.08x faster                                                                                                |
| fannkuch                         | 266 ms                                                                                                          | 249 ms: 1.07x faster                                                                                                |
| pickle_pure_python               | 182 us                                                                                                          | 171 us: 1.06x faster                                                                                                |
| xml_etree_process                | 37.4 ms                                                                                                         | 35.4 ms: 1.06x faster                                                                                               |
| logging_simple                   | 3.08 us                                                                                                         | 2.94 us: 1.05x faster                                                                                               |
| float                            | 48.1 ms                                                                                                         | 45.9 ms: 1.05x faster                                                                                               |
| logging_format                   | 3.39 us                                                                                                         | 3.24 us: 1.05x faster                                                                                               |
| richards                         | 31.6 ms                                                                                                         | 30.2 ms: 1.04x faster                                                                                               |
| pyflate                          | 322 ms                                                                                                          | 310 ms: 1.04x faster                                                                                                |
| deepcopy_memo                    | 17.0 us                                                                                                         | 16.5 us: 1.03x faster                                                                                               |
| html5lib                         | 31.5 ms                                                                                                         | 30.6 ms: 1.03x faster                                                                                               |
| bpe_tokeniser                    | 3.10 sec                                                                                                        | 3.02 sec: 1.03x faster                                                                                              |
| xml_etree_iterparse              | 72.6 ms                                                                                                         | 70.9 ms: 1.02x faster                                                                                               |
| xml_etree_parse                  | 106 ms                                                                                                          | 104 ms: 1.02x faster                                                                                                |
| richards_super                   | 34.6 ms                                                                                                         | 33.9 ms: 1.02x faster                                                                                               |
| xml_etree_generate               | 53.0 ms                                                                                                         | 52.0 ms: 1.02x faster                                                                                               |
| json                             | 2.94 ms                                                                                                         | 2.89 ms: 1.02x faster                                                                                               |
| meteor_contest                   | 71.9 ms                                                                                                         | 71.0 ms: 1.01x faster                                                                                               |
| regex_dna                        | 149 ms                                                                                                          | 149 ms: 1.00x faster                                                                                                |
| async_tree_eager_cpu_io_mixed_tg | 333 ms                                                                                                          | 332 ms: 1.00x faster                                                                                                |
| pidigits                         | 281 ms                                                                                                          | 282 ms: 1.00x slower                                                                                                |
| gc_traversal                     | 2.46 ms                                                                                                         | 2.46 ms: 1.00x slower                                                                                               |
| telco                            | 4.55 ms                                                                                                         | 4.57 ms: 1.00x slower                                                                                               |
| create_gc_cycles                 | 903 us                                                                                                          | 907 us: 1.00x slower                                                                                                |
| thrift                           | 432 us                                                                                                          | 434 us: 1.01x slower                                                                                                |
| scimark_monte_carlo              | 42.5 ms                                                                                                         | 42.7 ms: 1.01x slower                                                                                               |
| python_startup                   | 15.2 ms                                                                                                         | 15.3 ms: 1.01x slower                                                                                               |
| regex_effbot                     | 2.54 ms                                                                                                         | 2.56 ms: 1.01x slower                                                                                               |
| scimark_fft                      | 182 ms                                                                                                          | 184 ms: 1.01x slower                                                                                                |
| mdp                              | 1.42 sec                                                                                                        | 1.44 sec: 1.01x slower                                                                                              |
| typing_runtime_protocols         | 93.7 us                                                                                                         | 95.1 us: 1.01x slower                                                                                               |
| pprint_safe_repr                 | 470 ms                                                                                                          | 477 ms: 1.02x slower                                                                                                |
| spectral_norm                    | 65.9 ms                                                                                                         | 66.9 ms: 1.02x slower                                                                                               |
| crypto_pyaes                     | 50.6 ms                                                                                                         | 51.4 ms: 1.02x slower                                                                                               |
| go                               | 98.1 ms                                                                                                         | 99.7 ms: 1.02x slower                                                                                               |
| python_startup_no_site           | 12.5 ms                                                                                                         | 12.7 ms: 1.02x slower                                                                                               |
| pprint_pformat                   | 955 ms                                                                                                          | 974 ms: 1.02x slower                                                                                                |
| nbody                            | 61.7 ms                                                                                                         | 63.0 ms: 1.02x slower                                                                                               |
| coverage                         | 44.2 ms                                                                                                         | 45.1 ms: 1.02x slower                                                                                               |
| logging_silent                   | 59.7 ns                                                                                                         | 61.0 ns: 1.02x slower                                                                                               |
| docutils                         | 1.49 sec                                                                                                        | 1.53 sec: 1.03x slower                                                                                              |
| scimark_sparse_mat_mult          | 2.79 ms                                                                                                         | 2.87 ms: 1.03x slower                                                                                               |
| dulwich_log                      | 27.2 ms                                                                                                         | 28.2 ms: 1.04x slower                                                                                               |
| async_generators                 | 281 ms                                                                                                          | 292 ms: 1.04x slower                                                                                                |
| pycparser                        | 643 ms                                                                                                          | 670 ms: 1.04x slower                                                                                                |
| sympy_str                        | 133 ms                                                                                                          | 139 ms: 1.04x slower                                                                                                |
| sqlglot_normalize                | 168 ms                                                                                                          | 175 ms: 1.04x slower                                                                                                |
| sympy_sum                        | 70.0 ms                                                                                                         | 73.1 ms: 1.04x slower                                                                                               |
| deepcopy_reduce                  | 1.49 us                                                                                                         | 1.56 us: 1.04x slower                                                                                               |
| deepcopy                         | 145 us                                                                                                          | 151 us: 1.04x slower                                                                                                |
| generators                       | 20.6 ms                                                                                                         | 21.5 ms: 1.05x slower                                                                                               |
| bench_thread_pool                | 449 us                                                                                                          | 470 us: 1.05x slower                                                                                                |
| scimark_sor                      | 95.1 ms                                                                                                         | 99.6 ms: 1.05x slower                                                                                               |
| sympy_expand                     | 229 ms                                                                                                          | 240 ms: 1.05x slower                                                                                                |
| 2to3                             | 163 ms                                                                                                          | 171 ms: 1.05x slower                                                                                                |
| sqlglot_optimize                 | 31.2 ms                                                                                                         | 32.8 ms: 1.05x slower                                                                                               |
| nqueens                          | 53.6 ms                                                                                                         | 56.6 ms: 1.06x slower                                                                                               |
| bench_mp_pool                    | 48.1 ms                                                                                                         | 50.9 ms: 1.06x slower                                                                                               |
| hexiom                           | 4.12 ms                                                                                                         | 4.38 ms: 1.06x slower                                                                                               |
| regex_compile                    | 68.4 ms                                                                                                         | 72.8 ms: 1.06x slower                                                                                               |
| sympy_integrate                  | 10.4 ms                                                                                                         | 11.1 ms: 1.07x slower                                                                                               |
| django_template                  | 19.7 ms                                                                                                         | 21.1 ms: 1.07x slower                                                                                               |
| deltablue                        | 2.11 ms                                                                                                         | 2.27 ms: 1.08x slower                                                                                               |
| raytrace                         | 147 ms                                                                                                          | 160 ms: 1.09x slower                                                                                                |
| sqlglot_transpile                | 905 us                                                                                                          | 996 us: 1.10x slower                                                                                                |
| chaos                            | 34.9 ms                                                                                                         | 38.5 ms: 1.10x slower                                                                                               |
| sqlglot_parse                    | 742 us                                                                                                          | 820 us: 1.11x slower                                                                                                |
| comprehensions                   | 10.9 us                                                                                                         | 12.3 us: 1.13x slower                                                                                               |
| scimark_lu                       | 69.5 ms                                                                                                         | 79.6 ms: 1.15x slower                                                                                               |
| genshi_text                      | 14.2 ms                                                                                                         | 16.5 ms: 1.16x slower                                                                                               |
| genshi_xml                       | 30.3 ms                                                                                                         | 40.4 ms: 1.33x slower                                                                                               |
| Geometric mean                   | (ref)                                                                                                           | 1.02x slower                                                                                                        |

Benchmark hidden because not significant (26): async_tree_io_tg, async_tree_none_tg, async_tree_eager_io, regex_v8, async_tree_io, async_tree_eager_memoization_tg, async_tree_none, async_tree_eager_cpu_io_mixed, async_tree_eager_io_tg, async_tree_cpu_io_mixed_tg, coroutines, pathlib, asyncio_websockets, json_loads, async_tree_memoization, json_dumps, async_tree_eager_tg, async_tree_eager, asyncio_tcp_ssl, async_tree_eager_memoization, async_tree_cpu_io_mixed, async_tree_memoization_tg, dask, tornado_http, asyncio_tcp, pylint

# HPT report

- Reliability score: 99.68% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.12x