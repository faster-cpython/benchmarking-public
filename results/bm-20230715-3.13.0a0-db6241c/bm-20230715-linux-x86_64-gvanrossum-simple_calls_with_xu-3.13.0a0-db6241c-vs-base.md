
# Results vs. base

- fork: gvanrossum
- ref: simple_calls_with_xu
- machine: linux-x86_64
- commit hash: db6241c
- commit date: 2023-07-15
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230715-linux-x86_64-python-d46a42fd8e8915e03cc2-3.13.0a0-d46a42f | bm-20230715-linux-x86_64-gvanrossum-simple_calls_with_xu-3.13.0a0-db6241c |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 2.65 sec                                                              | 2.75 sec: 1.04x slower                                                    |
| tornado_http   | 96.8 ms                                                               | 98.2 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230715-linux-x86_64-python-d46a42fd8e8915e03cc2-3.13.0a0-d46a42f | bm-20230715-linux-x86_64-gvanrossum-simple_calls_with_xu-3.13.0a0-db6241c |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 197 ms                                                                | 192 ms: 1.03x faster                                                      |
| float          | 80.2 ms                                                               | 85.6 ms: 1.07x slower                                                     |
| nbody          | 87.9 ms                                                               | 100 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230715-linux-x86_64-python-d46a42fd8e8915e03cc2-3.13.0a0-d46a42f | bm-20230715-linux-x86_64-gvanrossum-simple_calls_with_xu-3.13.0a0-db6241c |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 215 ms                                                                | 210 ms: 1.02x faster                                                      |
| regex_v8       | 22.4 ms                                                               | 22.3 ms: 1.00x faster                                                     |
| regex_effbot   | 3.55 ms                                                               | 3.54 ms: 1.00x faster                                                     |
| regex_compile  | 137 ms                                                                | 151 ms: 1.10x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230715-linux-x86_64-python-d46a42fd8e8915e03cc2-3.13.0a0-d46a42f | bm-20230715-linux-x86_64-gvanrossum-simple_calls_with_xu-3.13.0a0-db6241c |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_list        | 5.08 us                                                               | 4.93 us: 1.03x faster                                                     |
| pickle_pure_python   | 304 us                                                                | 302 us: 1.01x faster                                                      |
| pickle_dict          | 31.2 us                                                               | 31.3 us: 1.00x slower                                                     |
| json_loads           | 25.7 us                                                               | 26.0 us: 1.01x slower                                                     |
| json_dumps           | 9.74 ms                                                               | 9.84 ms: 1.01x slower                                                     |
| pickle_list          | 4.64 us                                                               | 4.73 us: 1.02x slower                                                     |
| pickle               | 10.7 us                                                               | 11.0 us: 1.02x slower                                                     |
| xml_etree_process    | 57.8 ms                                                               | 59.2 ms: 1.02x slower                                                     |
| xml_etree_iterparse  | 104 ms                                                                | 106 ms: 1.03x slower                                                      |
| xml_etree_generate   | 84.4 ms                                                               | 86.7 ms: 1.03x slower                                                     |
| unpickle_pure_python | 214 us                                                                | 226 us: 1.06x slower                                                      |
| tomli_loads          | 2.33 sec                                                              | 2.68 sec: 1.15x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                              |

Benchmark hidden because not significant (2): unpickle, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230715-linux-x86_64-python-d46a42fd8e8915e03cc2-3.13.0a0-d46a42f | bm-20230715-linux-x86_64-gvanrossum-simple_calls_with_xu-3.13.0a0-db6241c |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.68 ms                                                               | 6.71 ms: 1.00x slower                                                     |
| python_startup         | 9.18 ms                                                               | 9.24 ms: 1.01x slower                                                     |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230715-linux-x86_64-python-d46a42fd8e8915e03cc2-3.13.0a0-d46a42f | bm-20230715-linux-x86_64-gvanrossum-simple_calls_with_xu-3.13.0a0-db6241c |
|-----------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 10.7 ms                                                               | 12.2 ms: 1.14x slower                                                     |

All benchmarks:
===============

| Benchmark                | bm-20230715-linux-x86_64-python-d46a42fd8e8915e03cc2-3.13.0a0-d46a42f | bm-20230715-linux-x86_64-gvanrossum-simple_calls_with_xu-3.13.0a0-db6241c |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| gc_traversal             | 3.98 ms                                                               | 3.73 ms: 1.07x faster                                                     |
| unpickle_list            | 5.08 us                                                               | 4.93 us: 1.03x faster                                                     |
| pidigits                 | 197 ms                                                                | 192 ms: 1.03x faster                                                      |
| regex_dna                | 215 ms                                                                | 210 ms: 1.02x faster                                                      |
| pickle_pure_python       | 304 us                                                                | 302 us: 1.01x faster                                                      |
| regex_v8                 | 22.4 ms                                                               | 22.3 ms: 1.00x faster                                                     |
| regex_effbot             | 3.55 ms                                                               | 3.54 ms: 1.00x faster                                                     |
| python_startup_no_site   | 6.68 ms                                                               | 6.71 ms: 1.00x slower                                                     |
| pickle_dict              | 31.2 us                                                               | 31.3 us: 1.00x slower                                                     |
| asyncio_tcp_ssl          | 1.79 sec                                                              | 1.80 sec: 1.01x slower                                                    |
| python_startup           | 9.18 ms                                                               | 9.24 ms: 1.01x slower                                                     |
| asyncio_tcp              | 508 ms                                                                | 511 ms: 1.01x slower                                                      |
| richards                 | 48.5 ms                                                               | 48.8 ms: 1.01x slower                                                     |
| logging_silent           | 102 ns                                                                | 102 ns: 1.01x slower                                                      |
| json_loads               | 25.7 us                                                               | 26.0 us: 1.01x slower                                                     |
| json_dumps               | 9.74 ms                                                               | 9.84 ms: 1.01x slower                                                     |
| dulwich_log              | 65.9 ms                                                               | 66.6 ms: 1.01x slower                                                     |
| async_tree_none          | 480 ms                                                                | 485 ms: 1.01x slower                                                      |
| tornado_http             | 96.8 ms                                                               | 98.2 ms: 1.01x slower                                                     |
| telco                    | 7.20 ms                                                               | 7.31 ms: 1.01x slower                                                     |
| generators               | 28.1 ms                                                               | 28.5 ms: 1.01x slower                                                     |
| async_tree_memoization   | 583 ms                                                                | 592 ms: 1.01x slower                                                      |
| deepcopy_reduce          | 3.16 us                                                               | 3.21 us: 1.01x slower                                                     |
| json                     | 4.93 ms                                                               | 5.02 ms: 1.02x slower                                                     |
| unpack_sequence          | 46.0 ns                                                               | 46.9 ns: 1.02x slower                                                     |
| pathlib                  | 18.8 ms                                                               | 19.1 ms: 1.02x slower                                                     |
| pickle_list              | 4.64 us                                                               | 4.73 us: 1.02x slower                                                     |
| pickle                   | 10.7 us                                                               | 11.0 us: 1.02x slower                                                     |
| sqlglot_parse            | 1.29 ms                                                               | 1.32 ms: 1.02x slower                                                     |
| pprint_pformat           | 1.49 sec                                                              | 1.53 sec: 1.02x slower                                                    |
| xml_etree_process        | 57.8 ms                                                               | 59.2 ms: 1.02x slower                                                     |
| sqlite_synth             | 2.73 us                                                               | 2.80 us: 1.02x slower                                                     |
| dask                     | 518 ms                                                                | 531 ms: 1.03x slower                                                      |
| xml_etree_iterparse      | 104 ms                                                                | 106 ms: 1.03x slower                                                      |
| sqlglot_transpile        | 1.61 ms                                                               | 1.66 ms: 1.03x slower                                                     |
| xml_etree_generate       | 84.4 ms                                                               | 86.7 ms: 1.03x slower                                                     |
| mypy2                    | 337 ms                                                                | 347 ms: 1.03x slower                                                      |
| deepcopy                 | 353 us                                                                | 364 us: 1.03x slower                                                      |
| scimark_monte_carlo      | 67.1 ms                                                               | 69.2 ms: 1.03x slower                                                     |
| logging_simple           | 5.84 us                                                               | 6.03 us: 1.03x slower                                                     |
| scimark_sor              | 120 ms                                                                | 124 ms: 1.03x slower                                                      |
| pprint_safe_repr         | 727 ms                                                                | 752 ms: 1.03x slower                                                      |
| docutils                 | 2.65 sec                                                              | 2.75 sec: 1.04x slower                                                    |
| sqlglot_normalize        | 106 ms                                                                | 109 ms: 1.04x slower                                                      |
| typing_runtime_protocols | 146 us                                                                | 152 us: 1.04x slower                                                      |
| bench_thread_pool        | 815 us                                                                | 848 us: 1.04x slower                                                      |
| logging_format           | 6.46 us                                                               | 6.73 us: 1.04x slower                                                     |
| async_generators         | 446 ms                                                                | 465 ms: 1.04x slower                                                      |
| raytrace                 | 269 ms                                                                | 280 ms: 1.04x slower                                                      |
| sqlglot_optimize         | 52.9 ms                                                               | 55.3 ms: 1.04x slower                                                     |
| scimark_lu               | 113 ms                                                                | 118 ms: 1.04x slower                                                      |
| pycparser                | 1.14 sec                                                              | 1.20 sec: 1.05x slower                                                    |
| unpickle_pure_python     | 214 us                                                                | 226 us: 1.06x slower                                                      |
| crypto_pyaes             | 71.3 ms                                                               | 75.4 ms: 1.06x slower                                                     |
| go                       | 138 ms                                                                | 146 ms: 1.06x slower                                                      |
| spectral_norm            | 107 ms                                                                | 113 ms: 1.06x slower                                                      |
| chaos                    | 59.6 ms                                                               | 63.4 ms: 1.06x slower                                                     |
| pyflate                  | 453 ms                                                                | 482 ms: 1.06x slower                                                      |
| float                    | 80.2 ms                                                               | 85.6 ms: 1.07x slower                                                     |
| regex_compile            | 137 ms                                                                | 151 ms: 1.10x slower                                                      |
| meteor_contest           | 105 ms                                                                | 117 ms: 1.11x slower                                                      |
| mdp                      | 2.56 sec                                                              | 2.83 sec: 1.11x slower                                                    |
| scimark_fft              | 351 ms                                                                | 390 ms: 1.11x slower                                                      |
| nbody                    | 87.9 ms                                                               | 100 ms: 1.14x slower                                                      |
| mako                     | 10.7 ms                                                               | 12.2 ms: 1.14x slower                                                     |
| deepcopy_memo            | 37.9 us                                                               | 43.1 us: 1.14x slower                                                     |
| tomli_loads              | 2.33 sec                                                              | 2.68 sec: 1.15x slower                                                    |
| deltablue                | 3.20 ms                                                               | 3.70 ms: 1.16x slower                                                     |
| fannkuch                 | 390 ms                                                                | 477 ms: 1.22x slower                                                      |
| comprehensions           | 20.4 us                                                               | 25.1 us: 1.23x slower                                                     |
| hexiom                   | 6.04 ms                                                               | 7.57 ms: 1.25x slower                                                     |
| nqueens                  | 79.9 ms                                                               | 101 ms: 1.26x slower                                                      |
| scimark_sparse_mat_mult  | 4.73 ms                                                               | 6.45 ms: 1.36x slower                                                     |
| Geometric mean           | (ref)                                                                 | 1.04x slower                                                              |

Benchmark hidden because not significant (9): unpickle, xml_etree_parse, bench_mp_pool, async_tree_io, coverage, create_gc_cycles, richards_super, async_tree_cpu_io_mixed, coroutines


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x
