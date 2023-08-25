
# Results vs. base

- fork: brandtbucher
- ref: tracing
- machine: linux-x86_64
- commit hash: 930262f
- commit date: 2023-08-05
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230804-linux-x86_64-python-2c25bd82f46df72c89ca-3.13.0a0-2c25bd8 | bm-20230805-linux-x86_64-brandtbucher-tracing-3.13.0a0-930262f |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| docutils       | 2.66 sec                                                              | 2.79 sec: 1.05x slower                                         |
| tornado_http   | 95.6 ms                                                               | 98.2 ms: 1.03x slower                                          |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230804-linux-x86_64-python-2c25bd82f46df72c89ca-3.13.0a0-2c25bd8 | bm-20230805-linux-x86_64-brandtbucher-tracing-3.13.0a0-930262f |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| pidigits       | 189 ms                                                                | 201 ms: 1.06x slower                                           |
| float          | 78.7 ms                                                               | 85.2 ms: 1.08x slower                                          |
| nbody          | 88.9 ms                                                               | 112 ms: 1.26x slower                                           |
| Geometric mean | (ref)                                                                 | 1.13x slower                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230804-linux-x86_64-python-2c25bd82f46df72c89ca-3.13.0a0-2c25bd8 | bm-20230805-linux-x86_64-brandtbucher-tracing-3.13.0a0-930262f |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_v8       | 22.6 ms                                                               | 21.6 ms: 1.05x faster                                          |
| regex_effbot   | 3.67 ms                                                               | 3.54 ms: 1.04x faster                                          |
| regex_dna      | 215 ms                                                                | 208 ms: 1.03x faster                                           |
| regex_compile  | 137 ms                                                                | 156 ms: 1.14x slower                                           |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230804-linux-x86_64-python-2c25bd82f46df72c89ca-3.13.0a0-2c25bd8 | bm-20230805-linux-x86_64-brandtbucher-tracing-3.13.0a0-930262f |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| unpickle             | 15.1 us                                                               | 15.0 us: 1.01x faster                                          |
| json_loads           | 25.6 us                                                               | 25.4 us: 1.01x faster                                          |
| xml_etree_generate   | 84.3 ms                                                               | 86.1 ms: 1.02x slower                                          |
| unpickle_list        | 5.17 us                                                               | 5.30 us: 1.03x slower                                          |
| xml_etree_process    | 58.2 ms                                                               | 59.7 ms: 1.03x slower                                          |
| xml_etree_iterparse  | 103 ms                                                                | 106 ms: 1.03x slower                                           |
| pickle_list          | 4.51 us                                                               | 4.64 us: 1.03x slower                                          |
| pickle_dict          | 31.8 us                                                               | 32.8 us: 1.03x slower                                          |
| pickle_pure_python   | 294 us                                                                | 303 us: 1.03x slower                                           |
| json_dumps           | 9.72 ms                                                               | 10.1 ms: 1.03x slower                                          |
| pickle               | 10.4 us                                                               | 10.8 us: 1.04x slower                                          |
| unpickle_pure_python | 212 us                                                                | 225 us: 1.06x slower                                           |
| tomli_loads          | 2.31 sec                                                              | 2.66 sec: 1.15x slower                                         |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                   |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230804-linux-x86_64-python-2c25bd82f46df72c89ca-3.13.0a0-2c25bd8 | bm-20230805-linux-x86_64-brandtbucher-tracing-3.13.0a0-930262f |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup_no_site | 6.87 ms                                                               | 6.83 ms: 1.01x faster                                          |
| python_startup         | 9.38 ms                                                               | 9.34 ms: 1.00x faster                                          |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230804-linux-x86_64-python-2c25bd82f46df72c89ca-3.13.0a0-2c25bd8 | bm-20230805-linux-x86_64-brandtbucher-tracing-3.13.0a0-930262f |
|-----------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| mako      | 10.8 ms                                                               | 12.4 ms: 1.15x slower                                          |

All benchmarks:
===============

| Benchmark                | bm-20230804-linux-x86_64-python-2c25bd82f46df72c89ca-3.13.0a0-2c25bd8 | bm-20230805-linux-x86_64-brandtbucher-tracing-3.13.0a0-930262f |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_v8                 | 22.6 ms                                                               | 21.6 ms: 1.05x faster                                          |
| regex_effbot             | 3.67 ms                                                               | 3.54 ms: 1.04x faster                                          |
| regex_dna                | 215 ms                                                                | 208 ms: 1.03x faster                                           |
| create_gc_cycles         | 1.51 ms                                                               | 1.49 ms: 1.01x faster                                          |
| unpickle                 | 15.1 us                                                               | 15.0 us: 1.01x faster                                          |
| json_loads               | 25.6 us                                                               | 25.4 us: 1.01x faster                                          |
| coroutines               | 21.6 ms                                                               | 21.5 ms: 1.01x faster                                          |
| python_startup_no_site   | 6.87 ms                                                               | 6.83 ms: 1.01x faster                                          |
| python_startup           | 9.38 ms                                                               | 9.34 ms: 1.00x faster                                          |
| async_tree_io            | 1.20 sec                                                              | 1.20 sec: 1.00x slower                                         |
| asyncio_tcp_ssl          | 1.79 sec                                                              | 1.81 sec: 1.01x slower                                         |
| async_tree_none          | 488 ms                                                                | 493 ms: 1.01x slower                                           |
| deepcopy_reduce          | 3.17 us                                                               | 3.21 us: 1.01x slower                                          |
| unpack_sequence          | 45.4 ns                                                               | 46.1 ns: 1.01x slower                                          |
| async_tree_cpu_io_mixed  | 724 ms                                                                | 736 ms: 1.02x slower                                           |
| generators               | 28.4 ms                                                               | 28.9 ms: 1.02x slower                                          |
| asyncio_tcp              | 484 ms                                                                | 492 ms: 1.02x slower                                           |
| sqlite_synth             | 2.74 us                                                               | 2.79 us: 1.02x slower                                          |
| coverage                 | 92.7 ms                                                               | 94.5 ms: 1.02x slower                                          |
| richards                 | 48.1 ms                                                               | 49.1 ms: 1.02x slower                                          |
| gc_traversal             | 3.98 ms                                                               | 4.06 ms: 1.02x slower                                          |
| xml_etree_generate       | 84.3 ms                                                               | 86.1 ms: 1.02x slower                                          |
| richards_super           | 54.5 ms                                                               | 55.7 ms: 1.02x slower                                          |
| async_tree_memoization   | 589 ms                                                                | 602 ms: 1.02x slower                                           |
| unpickle_list            | 5.17 us                                                               | 5.30 us: 1.03x slower                                          |
| xml_etree_process        | 58.2 ms                                                               | 59.7 ms: 1.03x slower                                          |
| logging_silent           | 103 ns                                                                | 106 ns: 1.03x slower                                           |
| tornado_http             | 95.6 ms                                                               | 98.2 ms: 1.03x slower                                          |
| xml_etree_iterparse      | 103 ms                                                                | 106 ms: 1.03x slower                                           |
| pickle_list              | 4.51 us                                                               | 4.64 us: 1.03x slower                                          |
| pickle_dict              | 31.8 us                                                               | 32.8 us: 1.03x slower                                          |
| pathlib                  | 18.3 ms                                                               | 18.9 ms: 1.03x slower                                          |
| pycparser                | 1.16 sec                                                              | 1.20 sec: 1.03x slower                                         |
| pickle_pure_python       | 294 us                                                                | 303 us: 1.03x slower                                           |
| json_dumps               | 9.72 ms                                                               | 10.1 ms: 1.03x slower                                          |
| typing_runtime_protocols | 149 us                                                                | 154 us: 1.04x slower                                           |
| async_generators         | 449 ms                                                                | 466 ms: 1.04x slower                                           |
| pickle                   | 10.4 us                                                               | 10.8 us: 1.04x slower                                          |
| deepcopy                 | 353 us                                                                | 367 us: 1.04x slower                                           |
| sqlglot_transpile        | 1.60 ms                                                               | 1.66 ms: 1.04x slower                                          |
| scimark_monte_carlo      | 66.8 ms                                                               | 69.5 ms: 1.04x slower                                          |
| dask                     | 517 ms                                                                | 538 ms: 1.04x slower                                           |
| sqlglot_parse            | 1.28 ms                                                               | 1.34 ms: 1.04x slower                                          |
| docutils                 | 2.66 sec                                                              | 2.79 sec: 1.05x slower                                         |
| logging_simple           | 5.90 us                                                               | 6.18 us: 1.05x slower                                          |
| sqlglot_normalize        | 104 ms                                                                | 110 ms: 1.05x slower                                           |
| spectral_norm            | 106 ms                                                                | 111 ms: 1.05x slower                                           |
| scimark_sor              | 119 ms                                                                | 126 ms: 1.05x slower                                           |
| mypy2                    | 337 ms                                                                | 354 ms: 1.05x slower                                           |
| bench_thread_pool        | 822 us                                                                | 866 us: 1.05x slower                                           |
| dulwich_log              | 65.4 ms                                                               | 69.0 ms: 1.05x slower                                          |
| sqlglot_optimize         | 52.4 ms                                                               | 55.4 ms: 1.06x slower                                          |
| unpickle_pure_python     | 212 us                                                                | 225 us: 1.06x slower                                           |
| pidigits                 | 189 ms                                                                | 201 ms: 1.06x slower                                           |
| raytrace                 | 269 ms                                                                | 288 ms: 1.07x slower                                           |
| mdp                      | 2.53 sec                                                              | 2.71 sec: 1.07x slower                                         |
| scimark_lu               | 111 ms                                                                | 119 ms: 1.07x slower                                           |
| logging_format           | 6.41 us                                                               | 6.89 us: 1.08x slower                                          |
| go                       | 138 ms                                                                | 149 ms: 1.08x slower                                           |
| float                    | 78.7 ms                                                               | 85.2 ms: 1.08x slower                                          |
| pprint_safe_repr         | 712 ms                                                                | 771 ms: 1.08x slower                                           |
| pprint_pformat           | 1.46 sec                                                              | 1.58 sec: 1.09x slower                                         |
| deltablue                | 3.18 ms                                                               | 3.47 ms: 1.09x slower                                          |
| crypto_pyaes             | 70.4 ms                                                               | 77.0 ms: 1.09x slower                                          |
| scimark_fft              | 358 ms                                                                | 404 ms: 1.13x slower                                           |
| meteor_contest           | 106 ms                                                                | 120 ms: 1.14x slower                                           |
| regex_compile            | 137 ms                                                                | 156 ms: 1.14x slower                                           |
| deepcopy_memo            | 37.5 us                                                               | 42.9 us: 1.15x slower                                          |
| tomli_loads              | 2.31 sec                                                              | 2.66 sec: 1.15x slower                                         |
| mako                     | 10.8 ms                                                               | 12.4 ms: 1.15x slower                                          |
| chaos                    | 59.0 ms                                                               | 71.2 ms: 1.21x slower                                          |
| pyflate                  | 438 ms                                                                | 533 ms: 1.22x slower                                           |
| scimark_sparse_mat_mult  | 4.73 ms                                                               | 5.79 ms: 1.22x slower                                          |
| comprehensions           | 20.2 us                                                               | 25.3 us: 1.25x slower                                          |
| nbody                    | 88.9 ms                                                               | 112 ms: 1.26x slower                                           |
| fannkuch                 | 388 ms                                                                | 490 ms: 1.26x slower                                           |
| nqueens                  | 79.5 ms                                                               | 101 ms: 1.27x slower                                           |
| hexiom                   | 6.02 ms                                                               | 7.93 ms: 1.32x slower                                          |
| Geometric mean           | (ref)                                                                 | 1.06x slower                                                   |

Benchmark hidden because not significant (4): xml_etree_parse, bench_mp_pool, json, telco


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x
