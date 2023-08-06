
# Results vs. base

- fork: kumaraditya303
- ref: linked_list
- machine: linux-x86_64
- commit hash: 1d32835
- commit date: 2023-08-05
- overall geometric mean: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230805-linux-x86_64-python-85e5b1f5b806289744ef-3.13.0a0-85e5b1f | bm-20230805-linux-x86_64-kumaraditya303-linked_list-3.13.0a0-1d32835 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| docutils       | 2.65 sec                                                              | 2.66 sec: 1.00x slower                                               |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                         |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230805-linux-x86_64-python-85e5b1f5b806289744ef-3.13.0a0-85e5b1f | bm-20230805-linux-x86_64-kumaraditya303-linked_list-3.13.0a0-1d32835 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 94.5 ms                                                               | 87.4 ms: 1.08x faster                                                |
| pidigits       | 201 ms                                                                | 189 ms: 1.06x faster                                                 |
| float          | 80.3 ms                                                               | 79.4 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                                 | 1.05x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230805-linux-x86_64-python-85e5b1f5b806289744ef-3.13.0a0-85e5b1f | bm-20230805-linux-x86_64-kumaraditya303-linked_list-3.13.0a0-1d32835 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 136 ms: 1.01x faster                                                 |
| regex_effbot   | 3.48 ms                                                               | 3.47 ms: 1.00x faster                                                |
| regex_dna      | 203 ms                                                                | 209 ms: 1.03x slower                                                 |
| regex_v8       | 21.9 ms                                                               | 22.7 ms: 1.04x slower                                                |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230805-linux-x86_64-python-85e5b1f5b806289744ef-3.13.0a0-85e5b1f | bm-20230805-linux-x86_64-kumaraditya303-linked_list-3.13.0a0-1d32835 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pickle_dict          | 33.1 us                                                               | 31.5 us: 1.05x faster                                                |
| unpickle             | 14.9 us                                                               | 14.6 us: 1.02x faster                                                |
| unpickle_list        | 4.98 us                                                               | 4.92 us: 1.01x faster                                                |
| xml_etree_process    | 58.0 ms                                                               | 57.7 ms: 1.01x faster                                                |
| unpickle_pure_python | 212 us                                                                | 211 us: 1.00x faster                                                 |
| json_loads           | 25.4 us                                                               | 25.3 us: 1.00x faster                                                |
| tomli_loads          | 2.28 sec                                                              | 2.32 sec: 1.02x slower                                               |
| pickle               | 10.5 us                                                               | 10.7 us: 1.02x slower                                                |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                         |

Benchmark hidden because not significant (6): json_dumps, pickle_list, xml_etree_generate, xml_etree_iterparse, xml_etree_parse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230805-linux-x86_64-python-85e5b1f5b806289744ef-3.13.0a0-85e5b1f | bm-20230805-linux-x86_64-kumaraditya303-linked_list-3.13.0a0-1d32835 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.86 ms                                                               | 6.87 ms: 1.00x slower                                                |
| python_startup         | 9.38 ms                                                               | 9.40 ms: 1.00x slower                                                |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230805-linux-x86_64-python-85e5b1f5b806289744ef-3.13.0a0-85e5b1f | bm-20230805-linux-x86_64-kumaraditya303-linked_list-3.13.0a0-1d32835 |
|-----------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako      | 10.7 ms                                                               | 10.9 ms: 1.02x slower                                                |

All benchmarks:
===============

| Benchmark                | bm-20230805-linux-x86_64-python-85e5b1f5b806289744ef-3.13.0a0-85e5b1f | bm-20230805-linux-x86_64-kumaraditya303-linked_list-3.13.0a0-1d32835 |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none          | 484 ms                                                                | 405 ms: 1.20x faster                                                 |
| async_tree_cpu_io_mixed  | 724 ms                                                                | 643 ms: 1.13x faster                                                 |
| async_tree_memoization   | 587 ms                                                                | 540 ms: 1.09x faster                                                 |
| nbody                    | 94.5 ms                                                               | 87.4 ms: 1.08x faster                                                |
| pidigits                 | 201 ms                                                                | 189 ms: 1.06x faster                                                 |
| pickle_dict              | 33.1 us                                                               | 31.5 us: 1.05x faster                                                |
| async_tree_io            | 1.19 sec                                                              | 1.14 sec: 1.04x faster                                               |
| richards                 | 47.9 ms                                                               | 46.3 ms: 1.04x faster                                                |
| crypto_pyaes             | 70.9 ms                                                               | 68.6 ms: 1.03x faster                                                |
| scimark_lu               | 112 ms                                                                | 109 ms: 1.03x faster                                                 |
| scimark_fft              | 360 ms                                                                | 350 ms: 1.03x faster                                                 |
| logging_format           | 6.59 us                                                               | 6.41 us: 1.03x faster                                                |
| spectral_norm            | 108 ms                                                                | 105 ms: 1.03x faster                                                 |
| richards_super           | 54.0 ms                                                               | 52.6 ms: 1.03x faster                                                |
| logging_silent           | 106 ns                                                                | 103 ns: 1.03x faster                                                 |
| pprint_pformat           | 1.48 sec                                                              | 1.45 sec: 1.02x faster                                               |
| unpickle                 | 14.9 us                                                               | 14.6 us: 1.02x faster                                                |
| fannkuch                 | 393 ms                                                                | 385 ms: 1.02x faster                                                 |
| pprint_safe_repr         | 723 ms                                                                | 709 ms: 1.02x faster                                                 |
| logging_simple           | 5.96 us                                                               | 5.84 us: 1.02x faster                                                |
| coverage                 | 94.8 ms                                                               | 93.1 ms: 1.02x faster                                                |
| raytrace                 | 271 ms                                                                | 267 ms: 1.02x faster                                                 |
| hexiom                   | 6.05 ms                                                               | 5.95 ms: 1.02x faster                                                |
| deepcopy_reduce          | 3.19 us                                                               | 3.15 us: 1.02x faster                                                |
| chaos                    | 60.1 ms                                                               | 59.2 ms: 1.02x faster                                                |
| float                    | 80.3 ms                                                               | 79.4 ms: 1.01x faster                                                |
| unpickle_list            | 4.98 us                                                               | 4.92 us: 1.01x faster                                                |
| sqlglot_parse            | 1.30 ms                                                               | 1.28 ms: 1.01x faster                                                |
| pathlib                  | 18.8 ms                                                               | 18.6 ms: 1.01x faster                                                |
| nqueens                  | 80.3 ms                                                               | 79.5 ms: 1.01x faster                                                |
| go                       | 136 ms                                                                | 135 ms: 1.01x faster                                                 |
| scimark_monte_carlo      | 67.4 ms                                                               | 66.8 ms: 1.01x faster                                                |
| scimark_sor              | 121 ms                                                                | 120 ms: 1.01x faster                                                 |
| typing_runtime_protocols | 148 us                                                                | 147 us: 1.01x faster                                                 |
| asyncio_tcp              | 486 ms                                                                | 483 ms: 1.01x faster                                                 |
| xml_etree_process        | 58.0 ms                                                               | 57.7 ms: 1.01x faster                                                |
| deepcopy                 | 354 us                                                                | 352 us: 1.01x faster                                                 |
| async_generators         | 453 ms                                                                | 450 ms: 1.01x faster                                                 |
| sqlglot_normalize        | 105 ms                                                                | 104 ms: 1.01x faster                                                 |
| regex_compile            | 137 ms                                                                | 136 ms: 1.01x faster                                                 |
| sqlglot_optimize         | 52.6 ms                                                               | 52.3 ms: 1.00x faster                                                |
| unpickle_pure_python     | 212 us                                                                | 211 us: 1.00x faster                                                 |
| asyncio_tcp_ssl          | 1.80 sec                                                              | 1.79 sec: 1.00x faster                                               |
| regex_effbot             | 3.48 ms                                                               | 3.47 ms: 1.00x faster                                                |
| bench_thread_pool        | 824 us                                                                | 821 us: 1.00x faster                                                 |
| coroutines               | 22.0 ms                                                               | 22.0 ms: 1.00x faster                                                |
| json_loads               | 25.4 us                                                               | 25.3 us: 1.00x faster                                                |
| python_startup_no_site   | 6.86 ms                                                               | 6.87 ms: 1.00x slower                                                |
| python_startup           | 9.38 ms                                                               | 9.40 ms: 1.00x slower                                                |
| docutils                 | 2.65 sec                                                              | 2.66 sec: 1.00x slower                                               |
| comprehensions           | 20.3 us                                                               | 20.4 us: 1.01x slower                                                |
| deltablue                | 3.18 ms                                                               | 3.20 ms: 1.01x slower                                                |
| telco                    | 7.74 ms                                                               | 7.83 ms: 1.01x slower                                                |
| tomli_loads              | 2.28 sec                                                              | 2.32 sec: 1.02x slower                                               |
| pickle                   | 10.5 us                                                               | 10.7 us: 1.02x slower                                                |
| pycparser                | 1.13 sec                                                              | 1.16 sec: 1.02x slower                                               |
| mako                     | 10.7 ms                                                               | 10.9 ms: 1.02x slower                                                |
| regex_dna                | 203 ms                                                                | 209 ms: 1.03x slower                                                 |
| scimark_sparse_mat_mult  | 4.57 ms                                                               | 4.71 ms: 1.03x slower                                                |
| regex_v8                 | 21.9 ms                                                               | 22.7 ms: 1.04x slower                                                |
| mdp                      | 2.54 sec                                                              | 2.68 sec: 1.06x slower                                               |
| gc_traversal             | 3.71 ms                                                               | 3.98 ms: 1.07x slower                                                |
| unpack_sequence          | 43.8 ns                                                               | 48.5 ns: 1.11x slower                                                |
| Geometric mean           | (ref)                                                                 | 1.01x faster                                                         |

Benchmark hidden because not significant (19): json, dask, sqlglot_transpile, json_dumps, tornado_http, pickle_list, pyflate, mypy2, dulwich_log, generators, meteor_contest, xml_etree_generate, create_gc_cycles, bench_mp_pool, xml_etree_iterparse, deepcopy_memo, xml_etree_parse, sqlite_synth, pickle_pure_python
