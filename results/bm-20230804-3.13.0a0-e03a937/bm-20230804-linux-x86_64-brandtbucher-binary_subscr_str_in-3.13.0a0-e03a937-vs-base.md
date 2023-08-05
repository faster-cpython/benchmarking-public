
# Results vs. base

- fork: brandtbucher
- ref: binary_subscr_str_in
- machine: linux-x86_64
- commit hash: e03a937
- commit date: 2023-08-04
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230804-linux-x86_64-python-2c25bd82f46df72c89ca-3.13.0a0-2c25bd8 | bm-20230804-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-e03a937 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 2.66 sec                                                              | 2.65 sec: 1.00x faster                                                      |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230804-linux-x86_64-python-2c25bd82f46df72c89ca-3.13.0a0-2c25bd8 | bm-20230804-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-e03a937 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 189 ms                                                                | 189 ms: 1.00x faster                                                        |
| float          | 78.7 ms                                                               | 80.0 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230804-linux-x86_64-python-2c25bd82f46df72c89ca-3.13.0a0-2c25bd8 | bm-20230804-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-e03a937 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                               | 3.38 ms: 1.09x faster                                                       |
| regex_dna      | 215 ms                                                                | 202 ms: 1.06x faster                                                        |
| regex_v8       | 22.6 ms                                                               | 22.0 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                                |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230804-linux-x86_64-python-2c25bd82f46df72c89ca-3.13.0a0-2c25bd8 | bm-20230804-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-e03a937 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_dict          | 31.8 us                                                               | 30.4 us: 1.05x faster                                                       |
| pickle_list          | 4.51 us                                                               | 4.45 us: 1.01x faster                                                       |
| pickle               | 10.4 us                                                               | 10.3 us: 1.01x faster                                                       |
| unpickle_list        | 5.17 us                                                               | 5.15 us: 1.00x faster                                                       |
| unpickle_pure_python | 212 us                                                                | 213 us: 1.00x slower                                                        |
| xml_etree_process    | 58.2 ms                                                               | 58.5 ms: 1.00x slower                                                       |
| xml_etree_generate   | 84.3 ms                                                               | 84.7 ms: 1.01x slower                                                       |
| tomli_loads          | 2.31 sec                                                              | 2.37 sec: 1.03x slower                                                      |
| json_dumps           | 9.72 ms                                                               | 10.0 ms: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (5): json_loads, pickle_pure_python, xml_etree_iterparse, xml_etree_parse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230804-linux-x86_64-python-2c25bd82f46df72c89ca-3.13.0a0-2c25bd8 | bm-20230804-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-e03a937 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 6.87 ms                                                               | 6.89 ms: 1.00x slower                                                       |
| python_startup         | 9.38 ms                                                               | 9.43 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20230804-linux-x86_64-python-2c25bd82f46df72c89ca-3.13.0a0-2c25bd8 | bm-20230804-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-e03a937 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot             | 3.67 ms                                                               | 3.38 ms: 1.09x faster                                                       |
| regex_dna                | 215 ms                                                                | 202 ms: 1.06x faster                                                        |
| pickle_dict              | 31.8 us                                                               | 30.4 us: 1.05x faster                                                       |
| regex_v8                 | 22.6 ms                                                               | 22.0 ms: 1.03x faster                                                       |
| typing_runtime_protocols | 149 us                                                                | 146 us: 1.02x faster                                                        |
| scimark_lu               | 111 ms                                                                | 109 ms: 1.02x faster                                                        |
| sqlglot_parse            | 1.28 ms                                                               | 1.26 ms: 1.02x faster                                                       |
| sqlglot_transpile        | 1.60 ms                                                               | 1.57 ms: 1.02x faster                                                       |
| crypto_pyaes             | 70.4 ms                                                               | 69.4 ms: 1.01x faster                                                       |
| pickle_list              | 4.51 us                                                               | 4.45 us: 1.01x faster                                                       |
| meteor_contest           | 106 ms                                                                | 105 ms: 1.01x faster                                                        |
| async_tree_none          | 488 ms                                                                | 483 ms: 1.01x faster                                                        |
| scimark_fft              | 358 ms                                                                | 355 ms: 1.01x faster                                                        |
| pickle                   | 10.4 us                                                               | 10.3 us: 1.01x faster                                                       |
| async_tree_io            | 1.20 sec                                                              | 1.19 sec: 1.01x faster                                                      |
| generators               | 28.4 ms                                                               | 28.3 ms: 1.00x faster                                                       |
| unpickle_list            | 5.17 us                                                               | 5.15 us: 1.00x faster                                                       |
| docutils                 | 2.66 sec                                                              | 2.65 sec: 1.00x faster                                                      |
| pidigits                 | 189 ms                                                                | 189 ms: 1.00x faster                                                        |
| python_startup_no_site   | 6.87 ms                                                               | 6.89 ms: 1.00x slower                                                       |
| gc_traversal             | 3.98 ms                                                               | 4.00 ms: 1.00x slower                                                       |
| deepcopy                 | 353 us                                                                | 355 us: 1.00x slower                                                        |
| unpickle_pure_python     | 212 us                                                                | 213 us: 1.00x slower                                                        |
| xml_etree_process        | 58.2 ms                                                               | 58.5 ms: 1.00x slower                                                       |
| xml_etree_generate       | 84.3 ms                                                               | 84.7 ms: 1.01x slower                                                       |
| python_startup           | 9.38 ms                                                               | 9.43 ms: 1.01x slower                                                       |
| hexiom                   | 6.02 ms                                                               | 6.05 ms: 1.01x slower                                                       |
| bench_thread_pool        | 822 us                                                                | 826 us: 1.01x slower                                                        |
| create_gc_cycles         | 1.51 ms                                                               | 1.52 ms: 1.01x slower                                                       |
| raytrace                 | 269 ms                                                                | 271 ms: 1.01x slower                                                        |
| json                     | 4.77 ms                                                               | 4.81 ms: 1.01x slower                                                       |
| logging_simple           | 5.90 us                                                               | 5.94 us: 1.01x slower                                                       |
| scimark_monte_carlo      | 66.8 ms                                                               | 67.5 ms: 1.01x slower                                                       |
| sqlite_synth             | 2.74 us                                                               | 2.77 us: 1.01x slower                                                       |
| dask                     | 517 ms                                                                | 522 ms: 1.01x slower                                                        |
| pprint_safe_repr         | 712 ms                                                                | 720 ms: 1.01x slower                                                        |
| sqlglot_optimize         | 52.4 ms                                                               | 53.1 ms: 1.01x slower                                                       |
| scimark_sparse_mat_mult  | 4.73 ms                                                               | 4.79 ms: 1.01x slower                                                       |
| comprehensions           | 20.2 us                                                               | 20.5 us: 1.01x slower                                                       |
| coverage                 | 92.7 ms                                                               | 94.0 ms: 1.01x slower                                                       |
| go                       | 138 ms                                                                | 140 ms: 1.01x slower                                                        |
| pathlib                  | 18.3 ms                                                               | 18.6 ms: 1.01x slower                                                       |
| deepcopy_memo            | 37.5 us                                                               | 38.0 us: 1.01x slower                                                       |
| pprint_pformat           | 1.46 sec                                                              | 1.48 sec: 1.02x slower                                                      |
| nqueens                  | 79.5 ms                                                               | 80.8 ms: 1.02x slower                                                       |
| dulwich_log              | 65.4 ms                                                               | 66.5 ms: 1.02x slower                                                       |
| float                    | 78.7 ms                                                               | 80.0 ms: 1.02x slower                                                       |
| coroutines               | 21.6 ms                                                               | 22.0 ms: 1.02x slower                                                       |
| spectral_norm            | 106 ms                                                                | 108 ms: 1.02x slower                                                        |
| pycparser                | 1.16 sec                                                              | 1.18 sec: 1.02x slower                                                      |
| logging_format           | 6.41 us                                                               | 6.55 us: 1.02x slower                                                       |
| telco                    | 7.75 ms                                                               | 7.92 ms: 1.02x slower                                                       |
| sqlglot_normalize        | 104 ms                                                                | 107 ms: 1.02x slower                                                        |
| scimark_sor              | 119 ms                                                                | 122 ms: 1.02x slower                                                        |
| tomli_loads              | 2.31 sec                                                              | 2.37 sec: 1.03x slower                                                      |
| deepcopy_reduce          | 3.17 us                                                               | 3.26 us: 1.03x slower                                                       |
| json_dumps               | 9.72 ms                                                               | 10.0 ms: 1.03x slower                                                       |
| logging_silent           | 103 ns                                                                | 107 ns: 1.04x slower                                                        |
| pyflate                  | 438 ms                                                                | 455 ms: 1.04x slower                                                        |
| mdp                      | 2.53 sec                                                              | 2.69 sec: 1.06x slower                                                      |
| unpack_sequence          | 45.4 ns                                                               | 50.7 ns: 1.12x slower                                                       |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (21): async_tree_cpu_io_mixed, json_loads, fannkuch, asyncio_tcp, pickle_pure_python, regex_compile, bench_mp_pool, asyncio_tcp_ssl, mako, richards_super, richards, chaos, mypy2, xml_etree_iterparse, nbody, tornado_http, deltablue, xml_etree_parse, async_generators, async_tree_memoization, unpickle
