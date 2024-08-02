# Results vs. base

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: darwin-arm64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 160 ms                                                                                                          | 172 ms: 1.07x slower                                                                                                |
| chameleon      | 4.33 ms                                                                                                         | 4.42 ms: 1.02x slower                                                                                               |
| docutils       | 1.44 sec                                                                                                        | 1.51 sec: 1.05x slower                                                                                              |
| html5lib       | 31.1 ms                                                                                                         | 31.0 ms: 1.00x faster                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.03x slower                                                                                                        |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|----------------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| async_tree_eager_cpu_io_mixed_tg | 332 ms                                                                                                          | 330 ms: 1.01x faster                                                                                                |
| async_tree_eager_tg              | 41.5 ms                                                                                                         | 42.3 ms: 1.02x slower                                                                                               |
| async_tree_eager                 | 61.0 ms                                                                                                         | 64.0 ms: 1.05x slower                                                                                               |
| Geometric mean                   | (ref)                                                                                                           | 1.01x slower                                                                                                        |

Benchmark hidden because not significant (13): async_tree_eager_io, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_eager_cpu_io_mixed, async_tree_eager_io_tg, async_tree_io_tg, async_tree_io, async_tree_memoization, async_tree_none, async_tree_none_tg, async_tree_memoization_tg, async_tree_eager_memoization_tg, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| float          | 48.7 ms                                                                                                         | 47.3 ms: 1.03x faster                                                                                               |
| pidigits       | 281 ms                                                                                                          | 282 ms: 1.00x slower                                                                                                |
| nbody          | 59.9 ms                                                                                                         | 63.7 ms: 1.06x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.01x slower                                                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 17.7 ms                                                                                                         | 17.5 ms: 1.01x faster                                                                                               |
| regex_dna      | 149 ms                                                                                                          | 149 ms: 1.00x faster                                                                                                |
| regex_effbot   | 2.56 ms                                                                                                         | 2.57 ms: 1.00x slower                                                                                               |
| regex_compile  | 68.3 ms                                                                                                         | 72.4 ms: 1.06x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.01x slower                                                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.45 sec                                                                                                        | 1.26 sec: 1.15x faster                                                                                              |
| unpickle_pure_python | 142 us                                                                                                          | 132 us: 1.07x faster                                                                                                |
| pickle_pure_python   | 180 us                                                                                                          | 172 us: 1.05x faster                                                                                                |
| xml_etree_process    | 36.8 ms                                                                                                         | 35.7 ms: 1.03x faster                                                                                               |
| xml_etree_iterparse  | 71.8 ms                                                                                                         | 70.2 ms: 1.02x faster                                                                                               |
| json_dumps           | 6.32 ms                                                                                                         | 6.19 ms: 1.02x faster                                                                                               |
| xml_etree_generate   | 51.8 ms                                                                                                         | 51.2 ms: 1.01x faster                                                                                               |
| pickle_dict          | 18.2 us                                                                                                         | 18.2 us: 1.00x faster                                                                                               |
| unpickle_list        | 2.86 us                                                                                                         | 2.89 us: 1.01x slower                                                                                               |
| pickle               | 7.36 us                                                                                                         | 7.44 us: 1.01x slower                                                                                               |
| xml_etree_parse      | 103 ms                                                                                                          | 104 ms: 1.01x slower                                                                                                |
| Geometric mean       | (ref)                                                                                                           | 1.02x faster                                                                                                        |

Benchmark hidden because not significant (3): unpickle, json_loads, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 14.9 ms                                                                                                         | 15.9 ms: 1.07x slower                                                                                               |
| python_startup_no_site | 12.2 ms                                                                                                         | 13.3 ms: 1.09x slower                                                                                               |
| Geometric mean         | (ref)                                                                                                           | 1.08x slower                                                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| mako            | 7.00 ms                                                                                                         | 6.37 ms: 1.10x faster                                                                                               |
| django_template | 19.6 ms                                                                                                         | 21.5 ms: 1.10x slower                                                                                               |
| genshi_text     | 13.8 ms                                                                                                         | 16.3 ms: 1.18x slower                                                                                               |
| genshi_xml      | 29.8 ms                                                                                                         | 39.3 ms: 1.32x slower                                                                                               |
| Geometric mean  | (ref)                                                                                                           | 1.12x slower                                                                                                        |

All benchmarks:
===============

| Benchmark                        | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|----------------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| tomli_loads                      | 1.45 sec                                                                                                        | 1.26 sec: 1.15x faster                                                                                              |
| mako                             | 7.00 ms                                                                                                         | 6.37 ms: 1.10x faster                                                                                               |
| unpickle_pure_python             | 142 us                                                                                                          | 132 us: 1.07x faster                                                                                                |
| fannkuch                         | 257 ms                                                                                                          | 244 ms: 1.05x faster                                                                                                |
| deepcopy_memo                    | 22.6 us                                                                                                         | 21.6 us: 1.05x faster                                                                                               |
| pickle_pure_python               | 180 us                                                                                                          | 172 us: 1.05x faster                                                                                                |
| float                            | 48.7 ms                                                                                                         | 47.3 ms: 1.03x faster                                                                                               |
| xml_etree_process                | 36.8 ms                                                                                                         | 35.7 ms: 1.03x faster                                                                                               |
| xml_etree_iterparse              | 71.8 ms                                                                                                         | 70.2 ms: 1.02x faster                                                                                               |
| json_dumps                       | 6.32 ms                                                                                                         | 6.19 ms: 1.02x faster                                                                                               |
| pyflate                          | 321 ms                                                                                                          | 315 ms: 1.02x faster                                                                                                |
| xml_etree_generate               | 51.8 ms                                                                                                         | 51.2 ms: 1.01x faster                                                                                               |
| regex_v8                         | 17.7 ms                                                                                                         | 17.5 ms: 1.01x faster                                                                                               |
| async_tree_eager_cpu_io_mixed_tg | 332 ms                                                                                                          | 330 ms: 1.01x faster                                                                                                |
| json                             | 2.93 ms                                                                                                         | 2.91 ms: 1.01x faster                                                                                               |
| pprint_safe_repr                 | 459 ms                                                                                                          | 457 ms: 1.00x faster                                                                                                |
| html5lib                         | 31.1 ms                                                                                                         | 31.0 ms: 1.00x faster                                                                                               |
| pickle_dict                      | 18.2 us                                                                                                         | 18.2 us: 1.00x faster                                                                                               |
| regex_dna                        | 149 ms                                                                                                          | 149 ms: 1.00x faster                                                                                                |
| pidigits                         | 281 ms                                                                                                          | 282 ms: 1.00x slower                                                                                                |
| gc_traversal                     | 2.46 ms                                                                                                         | 2.47 ms: 1.00x slower                                                                                               |
| spectral_norm                    | 67.2 ms                                                                                                         | 67.3 ms: 1.00x slower                                                                                               |
| regex_effbot                     | 2.56 ms                                                                                                         | 2.57 ms: 1.00x slower                                                                                               |
| pprint_pformat                   | 937 ms                                                                                                          | 940 ms: 1.00x slower                                                                                                |
| asyncio_websockets               | 408 ms                                                                                                          | 409 ms: 1.00x slower                                                                                                |
| coroutines                       | 15.9 ms                                                                                                         | 16.0 ms: 1.01x slower                                                                                               |
| logging_simple                   | 3.03 us                                                                                                         | 3.05 us: 1.01x slower                                                                                               |
| logging_format                   | 3.32 us                                                                                                         | 3.35 us: 1.01x slower                                                                                               |
| create_gc_cycles                 | 900 us                                                                                                          | 908 us: 1.01x slower                                                                                                |
| generators                       | 22.8 ms                                                                                                         | 23.0 ms: 1.01x slower                                                                                               |
| unpickle_list                    | 2.86 us                                                                                                         | 2.89 us: 1.01x slower                                                                                               |
| asyncio_tcp_ssl                  | 1.29 sec                                                                                                        | 1.30 sec: 1.01x slower                                                                                              |
| pickle                           | 7.36 us                                                                                                         | 7.44 us: 1.01x slower                                                                                               |
| deepcopy_reduce                  | 1.79 us                                                                                                         | 1.81 us: 1.01x slower                                                                                               |
| telco                            | 4.53 ms                                                                                                         | 4.59 ms: 1.01x slower                                                                                               |
| xml_etree_parse                  | 103 ms                                                                                                          | 104 ms: 1.01x slower                                                                                                |
| dask                             | 221 ms                                                                                                          | 224 ms: 1.02x slower                                                                                                |
| sqlite_synth                     | 1.54 us                                                                                                         | 1.56 us: 1.02x slower                                                                                               |
| scimark_fft                      | 181 ms                                                                                                          | 184 ms: 1.02x slower                                                                                                |
| async_tree_eager_tg              | 41.5 ms                                                                                                         | 42.3 ms: 1.02x slower                                                                                               |
| richards_super                   | 34.9 ms                                                                                                         | 35.6 ms: 1.02x slower                                                                                               |
| mdp                              | 1.48 sec                                                                                                        | 1.51 sec: 1.02x slower                                                                                              |
| thrift                           | 424 us                                                                                                          | 433 us: 1.02x slower                                                                                                |
| go                               | 100 ms                                                                                                          | 102 ms: 1.02x slower                                                                                                |
| chameleon                        | 4.33 ms                                                                                                         | 4.42 ms: 1.02x slower                                                                                               |
| deepcopy                         | 202 us                                                                                                          | 207 us: 1.02x slower                                                                                                |
| meteor_contest                   | 70.4 ms                                                                                                         | 72.5 ms: 1.03x slower                                                                                               |
| pathlib                          | 21.9 ms                                                                                                         | 22.5 ms: 1.03x slower                                                                                               |
| bench_thread_pool                | 463 us                                                                                                          | 480 us: 1.04x slower                                                                                                |
| crypto_pyaes                     | 49.8 ms                                                                                                         | 52.0 ms: 1.04x slower                                                                                               |
| sympy_expand                     | 227 ms                                                                                                          | 237 ms: 1.05x slower                                                                                                |
| scimark_sparse_mat_mult          | 2.79 ms                                                                                                         | 2.92 ms: 1.05x slower                                                                                               |
| sympy_str                        | 131 ms                                                                                                          | 137 ms: 1.05x slower                                                                                                |
| scimark_monte_carlo              | 42.3 ms                                                                                                         | 44.3 ms: 1.05x slower                                                                                               |
| typing_runtime_protocols         | 91.2 us                                                                                                         | 95.5 us: 1.05x slower                                                                                               |
| logging_silent                   | 60.0 ns                                                                                                         | 62.9 ns: 1.05x slower                                                                                               |
| scimark_sor                      | 95.4 ms                                                                                                         | 100 ms: 1.05x slower                                                                                                |
| async_tree_eager                 | 61.0 ms                                                                                                         | 64.0 ms: 1.05x slower                                                                                               |
| docutils                         | 1.44 sec                                                                                                        | 1.51 sec: 1.05x slower                                                                                              |
| async_generators                 | 279 ms                                                                                                          | 294 ms: 1.05x slower                                                                                                |
| pycparser                        | 632 ms                                                                                                          | 666 ms: 1.05x slower                                                                                                |
| sympy_integrate                  | 10.4 ms                                                                                                         | 10.9 ms: 1.06x slower                                                                                               |
| sympy_sum                        | 69.1 ms                                                                                                         | 73.1 ms: 1.06x slower                                                                                               |
| regex_compile                    | 68.3 ms                                                                                                         | 72.4 ms: 1.06x slower                                                                                               |
| sqlglot_optimize                 | 31.0 ms                                                                                                         | 32.9 ms: 1.06x slower                                                                                               |
| flaskblogging                    | 3.35 ms                                                                                                         | 3.57 ms: 1.06x slower                                                                                               |
| nbody                            | 59.9 ms                                                                                                         | 63.7 ms: 1.06x slower                                                                                               |
| python_startup                   | 14.9 ms                                                                                                         | 15.9 ms: 1.07x slower                                                                                               |
| 2to3                             | 160 ms                                                                                                          | 172 ms: 1.07x slower                                                                                                |
| bench_mp_pool                    | 46.5 ms                                                                                                         | 49.9 ms: 1.07x slower                                                                                               |
| hexiom                           | 4.08 ms                                                                                                         | 4.43 ms: 1.09x slower                                                                                               |
| nqueens                          | 52.8 ms                                                                                                         | 57.4 ms: 1.09x slower                                                                                               |
| python_startup_no_site           | 12.2 ms                                                                                                         | 13.3 ms: 1.09x slower                                                                                               |
| raytrace                         | 148 ms                                                                                                          | 162 ms: 1.09x slower                                                                                                |
| django_template                  | 19.6 ms                                                                                                         | 21.5 ms: 1.10x slower                                                                                               |
| chaos                            | 35.5 ms                                                                                                         | 39.2 ms: 1.10x slower                                                                                               |
| sqlglot_transpile                | 892 us                                                                                                          | 1.00 ms: 1.12x slower                                                                                               |
| sqlglot_parse                    | 732 us                                                                                                          | 826 us: 1.13x slower                                                                                                |
| deltablue                        | 2.14 ms                                                                                                         | 2.46 ms: 1.15x slower                                                                                               |
| comprehensions                   | 10.7 us                                                                                                         | 12.3 us: 1.15x slower                                                                                               |
| scimark_lu                       | 66.7 ms                                                                                                         | 78.1 ms: 1.17x slower                                                                                               |
| genshi_text                      | 13.8 ms                                                                                                         | 16.3 ms: 1.18x slower                                                                                               |
| genshi_xml                       | 29.8 ms                                                                                                         | 39.3 ms: 1.32x slower                                                                                               |
| Geometric mean                   | (ref)                                                                                                           | 1.03x slower                                                                                                        |

Benchmark hidden because not significant (21): richards, async_tree_eager_io, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, unpickle, async_tree_eager_cpu_io_mixed, async_tree_eager_io_tg, json_loads, async_tree_io_tg, pickle_list, coverage, async_tree_io, async_tree_memoization, async_tree_none, tornado_http, async_tree_none_tg, async_tree_memoization_tg, async_tree_eager_memoization_tg, async_tree_eager_memoization, asyncio_tcp, pylint
Ignored benchmarks (1) of results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json: sqlglot_normalize

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.31x