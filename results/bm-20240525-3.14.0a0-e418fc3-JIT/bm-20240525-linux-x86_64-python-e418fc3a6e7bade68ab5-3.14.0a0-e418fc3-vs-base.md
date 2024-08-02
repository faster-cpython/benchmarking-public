# Results vs. base

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: linux-x86_64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.00x slower
- HPT reliability: 90.42%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 271 ms                                                                                                          | 279 ms: 1.03x slower                                                                                                |
| chameleon      | 7.01 ms                                                                                                         | 7.04 ms: 1.01x slower                                                                                               |
| docutils       | 2.78 sec                                                                                                        | 2.95 sec: 1.06x slower                                                                                              |
| html5lib       | 67.1 ms                                                                                                         | 68.1 ms: 1.01x slower                                                                                               |
| tornado_http   | 93.9 ms                                                                                                         | 97.0 ms: 1.03x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.03x slower                                                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|--------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| async_tree_none_tg | 352 ms                                                                                                          | 334 ms: 1.05x faster                                                                                                |
| Geometric mean     | (ref)                                                                                                           | 1.01x faster                                                                                                        |

Benchmark hidden because not significant (7): async_tree_io_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| float          | 77.2 ms                                                                                                         | 72.2 ms: 1.07x faster                                                                                               |
| nbody          | 84.6 ms                                                                                                         | 80.8 ms: 1.05x faster                                                                                               |
| pidigits       | 190 ms                                                                                                          | 188 ms: 1.01x faster                                                                                                |
| Geometric mean | (ref)                                                                                                           | 1.04x faster                                                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 3.75 ms                                                                                                         | 3.72 ms: 1.01x faster                                                                                               |
| regex_v8       | 24.8 ms                                                                                                         | 25.1 ms: 1.01x slower                                                                                               |
| regex_compile  | 134 ms                                                                                                          | 138 ms: 1.03x slower                                                                                                |
| regex_dna      | 222 ms                                                                                                          | 229 ms: 1.04x slower                                                                                                |
| Geometric mean | (ref)                                                                                                           | 1.02x slower                                                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 2.15 sec                                                                                                        | 1.96 sec: 1.09x faster                                                                                              |
| xml_etree_parse      | 159 ms                                                                                                          | 150 ms: 1.06x faster                                                                                                |
| xml_etree_generate   | 86.2 ms                                                                                                         | 81.8 ms: 1.05x faster                                                                                               |
| xml_etree_iterparse  | 106 ms                                                                                                          | 101 ms: 1.05x faster                                                                                                |
| json_dumps           | 10.8 ms                                                                                                         | 10.3 ms: 1.05x faster                                                                                               |
| xml_etree_process    | 59.9 ms                                                                                                         | 57.8 ms: 1.04x faster                                                                                               |
| pickle_list          | 5.20 us                                                                                                         | 5.07 us: 1.02x faster                                                                                               |
| pickle_dict          | 35.7 us                                                                                                         | 35.9 us: 1.01x slower                                                                                               |
| pickle               | 11.7 us                                                                                                         | 11.9 us: 1.02x slower                                                                                               |
| unpickle_pure_python | 214 us                                                                                                          | 224 us: 1.05x slower                                                                                                |
| Geometric mean       | (ref)                                                                                                           | 1.02x faster                                                                                                        |

Benchmark hidden because not significant (4): unpickle_list, json_loads, pickle_pure_python, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                                                                         | 11.1 ms: 1.04x slower                                                                                               |
| python_startup_no_site | 7.09 ms                                                                                                         | 7.59 ms: 1.07x slower                                                                                               |
| Geometric mean         | (ref)                                                                                                           | 1.06x slower                                                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| mako            | 11.0 ms                                                                                                         | 9.82 ms: 1.12x faster                                                                                               |
| django_template | 35.3 ms                                                                                                         | 36.0 ms: 1.02x slower                                                                                               |
| genshi_text     | 23.7 ms                                                                                                         | 25.0 ms: 1.05x slower                                                                                               |
| genshi_xml      | 51.3 ms                                                                                                         | 57.4 ms: 1.12x slower                                                                                               |
| Geometric mean  | (ref)                                                                                                           | 1.02x slower                                                                                                        |

All benchmarks:
===============

| Benchmark                | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|--------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| scimark_sparse_mat_mult  | 5.09 ms                                                                                                         | 4.21 ms: 1.21x faster                                                                                               |
| richards                 | 48.6 ms                                                                                                         | 41.7 ms: 1.17x faster                                                                                               |
| scimark_fft              | 359 ms                                                                                                          | 309 ms: 1.16x faster                                                                                                |
| richards_super           | 54.8 ms                                                                                                         | 48.0 ms: 1.14x faster                                                                                               |
| spectral_norm            | 113 ms                                                                                                          | 100 ms: 1.13x faster                                                                                                |
| mako                     | 11.0 ms                                                                                                         | 9.82 ms: 1.12x faster                                                                                               |
| fannkuch                 | 394 ms                                                                                                          | 356 ms: 1.11x faster                                                                                                |
| crypto_pyaes             | 74.4 ms                                                                                                         | 67.4 ms: 1.10x faster                                                                                               |
| tomli_loads              | 2.15 sec                                                                                                        | 1.96 sec: 1.09x faster                                                                                              |
| scimark_monte_carlo      | 67.0 ms                                                                                                         | 62.1 ms: 1.08x faster                                                                                               |
| mdp                      | 2.76 sec                                                                                                        | 2.57 sec: 1.07x faster                                                                                              |
| float                    | 77.2 ms                                                                                                         | 72.2 ms: 1.07x faster                                                                                               |
| xml_etree_parse          | 159 ms                                                                                                          | 150 ms: 1.06x faster                                                                                                |
| telco                    | 8.59 ms                                                                                                         | 8.12 ms: 1.06x faster                                                                                               |
| async_tree_none_tg       | 352 ms                                                                                                          | 334 ms: 1.05x faster                                                                                                |
| xml_etree_generate       | 86.2 ms                                                                                                         | 81.8 ms: 1.05x faster                                                                                               |
| xml_etree_iterparse      | 106 ms                                                                                                          | 101 ms: 1.05x faster                                                                                                |
| json_dumps               | 10.8 ms                                                                                                         | 10.3 ms: 1.05x faster                                                                                               |
| nbody                    | 84.6 ms                                                                                                         | 80.8 ms: 1.05x faster                                                                                               |
| sqlite_synth             | 2.98 us                                                                                                         | 2.86 us: 1.04x faster                                                                                               |
| pyflate                  | 472 ms                                                                                                          | 455 ms: 1.04x faster                                                                                                |
| xml_etree_process        | 59.9 ms                                                                                                         | 57.8 ms: 1.04x faster                                                                                               |
| pprint_pformat           | 1.52 sec                                                                                                        | 1.47 sec: 1.03x faster                                                                                              |
| pickle_list              | 5.20 us                                                                                                         | 5.07 us: 1.02x faster                                                                                               |
| logging_format           | 6.43 us                                                                                                         | 6.29 us: 1.02x faster                                                                                               |
| logging_simple           | 5.80 us                                                                                                         | 5.67 us: 1.02x faster                                                                                               |
| pprint_safe_repr         | 741 ms                                                                                                          | 725 ms: 1.02x faster                                                                                                |
| coroutines               | 23.4 ms                                                                                                         | 22.9 ms: 1.02x faster                                                                                               |
| sqlglot_parse            | 1.33 ms                                                                                                         | 1.31 ms: 1.01x faster                                                                                               |
| chaos                    | 60.4 ms                                                                                                         | 59.7 ms: 1.01x faster                                                                                               |
| regex_effbot             | 3.75 ms                                                                                                         | 3.72 ms: 1.01x faster                                                                                               |
| pidigits                 | 190 ms                                                                                                          | 188 ms: 1.01x faster                                                                                                |
| meteor_contest           | 109 ms                                                                                                          | 108 ms: 1.00x faster                                                                                                |
| chameleon                | 7.01 ms                                                                                                         | 7.04 ms: 1.01x slower                                                                                               |
| pickle_dict              | 35.7 us                                                                                                         | 35.9 us: 1.01x slower                                                                                               |
| bench_mp_pool            | 24.0 ms                                                                                                         | 24.1 ms: 1.01x slower                                                                                               |
| asyncio_tcp_ssl          | 1.85 sec                                                                                                        | 1.86 sec: 1.01x slower                                                                                              |
| comprehensions           | 16.5 us                                                                                                         | 16.6 us: 1.01x slower                                                                                               |
| json                     | 5.28 ms                                                                                                         | 5.32 ms: 1.01x slower                                                                                               |
| gc_traversal             | 3.81 ms                                                                                                         | 3.85 ms: 1.01x slower                                                                                               |
| regex_v8                 | 24.8 ms                                                                                                         | 25.1 ms: 1.01x slower                                                                                               |
| thrift                   | 805 us                                                                                                          | 816 us: 1.01x slower                                                                                                |
| pathlib                  | 16.2 ms                                                                                                         | 16.4 ms: 1.01x slower                                                                                               |
| html5lib                 | 67.1 ms                                                                                                         | 68.1 ms: 1.01x slower                                                                                               |
| pickle                   | 11.7 us                                                                                                         | 11.9 us: 1.02x slower                                                                                               |
| django_template          | 35.3 ms                                                                                                         | 36.0 ms: 1.02x slower                                                                                               |
| dask                     | 368 ms                                                                                                          | 376 ms: 1.02x slower                                                                                                |
| deepcopy_reduce          | 3.28 us                                                                                                         | 3.35 us: 1.02x slower                                                                                               |
| async_generators         | 452 ms                                                                                                          | 462 ms: 1.02x slower                                                                                                |
| asyncio_tcp              | 508 ms                                                                                                          | 520 ms: 1.02x slower                                                                                                |
| sqlglot_optimize         | 55.0 ms                                                                                                         | 56.4 ms: 1.03x slower                                                                                               |
| regex_compile            | 134 ms                                                                                                          | 138 ms: 1.03x slower                                                                                                |
| create_gc_cycles         | 1.79 ms                                                                                                         | 1.84 ms: 1.03x slower                                                                                               |
| 2to3                     | 271 ms                                                                                                          | 279 ms: 1.03x slower                                                                                                |
| go                       | 144 ms                                                                                                          | 148 ms: 1.03x slower                                                                                                |
| coverage                 | 91.1 ms                                                                                                         | 94.0 ms: 1.03x slower                                                                                               |
| flaskblogging            | 8.92 ms                                                                                                         | 9.20 ms: 1.03x slower                                                                                               |
| tornado_http             | 93.9 ms                                                                                                         | 97.0 ms: 1.03x slower                                                                                               |
| sqlglot_normalize        | 110 ms                                                                                                          | 114 ms: 1.03x slower                                                                                                |
| scimark_sor              | 133 ms                                                                                                          | 138 ms: 1.03x slower                                                                                                |
| regex_dna                | 222 ms                                                                                                          | 229 ms: 1.04x slower                                                                                                |
| typing_runtime_protocols | 166 us                                                                                                          | 173 us: 1.04x slower                                                                                                |
| bench_thread_pool        | 830 us                                                                                                          | 867 us: 1.04x slower                                                                                                |
| python_startup           | 10.6 ms                                                                                                         | 11.1 ms: 1.04x slower                                                                                               |
| pycparser                | 1.16 sec                                                                                                        | 1.22 sec: 1.05x slower                                                                                              |
| unpickle_pure_python     | 214 us                                                                                                          | 224 us: 1.05x slower                                                                                                |
| genshi_text              | 23.7 ms                                                                                                         | 25.0 ms: 1.05x slower                                                                                               |
| dulwich_log              | 65.7 ms                                                                                                         | 69.3 ms: 1.05x slower                                                                                               |
| docutils                 | 2.78 sec                                                                                                        | 2.95 sec: 1.06x slower                                                                                              |
| nqueens                  | 81.8 ms                                                                                                         | 86.6 ms: 1.06x slower                                                                                               |
| raytrace                 | 262 ms                                                                                                          | 278 ms: 1.06x slower                                                                                                |
| generators               | 28.6 ms                                                                                                         | 30.4 ms: 1.06x slower                                                                                               |
| python_startup_no_site   | 7.09 ms                                                                                                         | 7.59 ms: 1.07x slower                                                                                               |
| hexiom                   | 6.12 ms                                                                                                         | 6.56 ms: 1.07x slower                                                                                               |
| sympy_expand             | 474 ms                                                                                                          | 509 ms: 1.07x slower                                                                                                |
| logging_silent           | 101 ns                                                                                                          | 108 ns: 1.07x slower                                                                                                |
| scimark_lu               | 113 ms                                                                                                          | 122 ms: 1.08x slower                                                                                                |
| sympy_str                | 281 ms                                                                                                          | 303 ms: 1.08x slower                                                                                                |
| sympy_integrate          | 20.4 ms                                                                                                         | 22.6 ms: 1.11x slower                                                                                               |
| sympy_sum                | 154 ms                                                                                                          | 171 ms: 1.11x slower                                                                                                |
| pylint                   | 318 ms                                                                                                          | 353 ms: 1.11x slower                                                                                                |
| genshi_xml               | 51.3 ms                                                                                                         | 57.4 ms: 1.12x slower                                                                                               |
| deltablue                | 3.26 ms                                                                                                         | 3.72 ms: 1.14x slower                                                                                               |
| Geometric mean           | (ref)                                                                                                           | 1.00x slower                                                                                                        |

Benchmark hidden because not significant (15): async_tree_io_tg, async_tree_memoization_tg, deepcopy_memo, async_tree_cpu_io_mixed_tg, unpickle_list, asyncio_websockets, sqlglot_transpile, json_loads, async_tree_cpu_io_mixed, pickle_pure_python, deepcopy, async_tree_memoization, unpickle, async_tree_none, async_tree_io

# HPT report

- Reliability score: 90.42% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.08x