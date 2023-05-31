
# Results vs. base

- fork: gvanrossum
- ref: split_ops
- machine: linux-x86_64
- commit hash: 3259d6e
- commit date: 2023-05-30
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230530-linux-x86_64-python-68c75c31536e8c879019-3.13.0a0-68c75c3 | bm-20230530-linux-x86_64-gvanrossum-split_ops-3.13.0a0-3259d6e |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| pidigits       | 197 ms                                                                | 197 ms: 1.00x faster                                           |
| nbody          | 87.6 ms                                                               | 89.1 ms: 1.02x slower                                          |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                   |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230530-linux-x86_64-python-68c75c31536e8c879019-3.13.0a0-68c75c3 | bm-20230530-linux-x86_64-gvanrossum-split_ops-3.13.0a0-3259d6e |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 144 ms                                                                | 146 ms: 1.01x slower                                           |
| regex_effbot   | 3.63 ms                                                               | 3.71 ms: 1.02x slower                                          |
| regex_v8       | 22.8 ms                                                               | 23.3 ms: 1.02x slower                                          |
| regex_dna      | 212 ms                                                                | 219 ms: 1.03x slower                                           |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20230530-linux-x86_64-python-68c75c31536e8c879019-3.13.0a0-68c75c3 | bm-20230530-linux-x86_64-gvanrossum-split_ops-3.13.0a0-3259d6e |
|---------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| pickle              | 10.8 us                                                               | 10.5 us: 1.03x faster                                          |
| pickle_list         | 4.60 us                                                               | 4.49 us: 1.02x faster                                          |
| pickle_dict         | 32.0 us                                                               | 31.7 us: 1.01x faster                                          |
| xml_etree_iterparse | 103 ms                                                                | 104 ms: 1.01x slower                                           |
| json_loads          | 24.8 us                                                               | 25.0 us: 1.01x slower                                          |
| pickle_pure_python  | 314 us                                                                | 317 us: 1.01x slower                                           |
| xml_etree_process   | 58.8 ms                                                               | 59.3 ms: 1.01x slower                                          |
| tomli_loads         | 2.18 sec                                                              | 2.24 sec: 1.02x slower                                         |
| unpickle            | 14.7 us                                                               | 15.1 us: 1.03x slower                                          |
| Geometric mean      | (ref)                                                                 | 1.00x slower                                                   |

Benchmark hidden because not significant (5): unpickle_list, xml_etree_parse, xml_etree_generate, unpickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20230530-linux-x86_64-python-68c75c31536e8c879019-3.13.0a0-68c75c3 | bm-20230530-linux-x86_64-gvanrossum-split_ops-3.13.0a0-3259d6e |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup | 9.33 ms                                                               | 9.33 ms: 1.00x faster                                          |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230530-linux-x86_64-python-68c75c31536e8c879019-3.13.0a0-68c75c3 | bm-20230530-linux-x86_64-gvanrossum-split_ops-3.13.0a0-3259d6e |
|-----------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| mako      | 10.5 ms                                                               | 10.7 ms: 1.02x slower                                          |

All benchmarks:
===============

| Benchmark               | bm-20230530-linux-x86_64-python-68c75c31536e8c879019-3.13.0a0-68c75c3 | bm-20230530-linux-x86_64-gvanrossum-split_ops-3.13.0a0-3259d6e |
|-------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| gc_traversal            | 3.85 ms                                                               | 3.61 ms: 1.07x faster                                          |
| pickle                  | 10.8 us                                                               | 10.5 us: 1.03x faster                                          |
| pickle_list             | 4.60 us                                                               | 4.49 us: 1.02x faster                                          |
| pathlib                 | 18.8 ms                                                               | 18.7 ms: 1.01x faster                                          |
| pickle_dict             | 32.0 us                                                               | 31.7 us: 1.01x faster                                          |
| async_tree_io           | 1.23 sec                                                              | 1.22 sec: 1.00x faster                                         |
| asyncio_tcp_ssl         | 1.80 sec                                                              | 1.80 sec: 1.00x faster                                         |
| pidigits                | 197 ms                                                                | 197 ms: 1.00x faster                                           |
| python_startup          | 9.33 ms                                                               | 9.33 ms: 1.00x faster                                          |
| dulwich_log             | 68.0 ms                                                               | 68.3 ms: 1.00x slower                                          |
| comprehensions          | 20.5 us                                                               | 20.6 us: 1.00x slower                                          |
| sqlglot_parse           | 1.34 ms                                                               | 1.35 ms: 1.00x slower                                          |
| crypto_pyaes            | 78.4 ms                                                               | 78.8 ms: 1.01x slower                                          |
| pycparser               | 1.16 sec                                                              | 1.17 sec: 1.01x slower                                         |
| go                      | 135 ms                                                                | 136 ms: 1.01x slower                                           |
| xml_etree_iterparse     | 103 ms                                                                | 104 ms: 1.01x slower                                           |
| json_loads              | 24.8 us                                                               | 25.0 us: 1.01x slower                                          |
| deepcopy_memo           | 37.1 us                                                               | 37.4 us: 1.01x slower                                          |
| logging_silent          | 99.4 ns                                                               | 100 ns: 1.01x slower                                           |
| sqlglot_optimize        | 54.1 ms                                                               | 54.5 ms: 1.01x slower                                          |
| pickle_pure_python      | 314 us                                                                | 317 us: 1.01x slower                                           |
| xml_etree_process       | 58.8 ms                                                               | 59.3 ms: 1.01x slower                                          |
| mypy2                   | 343 ms                                                                | 347 ms: 1.01x slower                                           |
| deltablue               | 3.48 ms                                                               | 3.52 ms: 1.01x slower                                          |
| scimark_monte_carlo     | 71.5 ms                                                               | 72.3 ms: 1.01x slower                                          |
| telco                   | 6.83 ms                                                               | 6.90 ms: 1.01x slower                                          |
| coroutines              | 22.2 ms                                                               | 22.5 ms: 1.01x slower                                          |
| bench_thread_pool       | 824 us                                                                | 835 us: 1.01x slower                                           |
| regex_compile           | 144 ms                                                                | 146 ms: 1.01x slower                                           |
| fannkuch                | 387 ms                                                                | 393 ms: 1.01x slower                                           |
| pyflate                 | 441 ms                                                                | 447 ms: 1.01x slower                                           |
| richards_super          | 49.9 ms                                                               | 50.6 ms: 1.01x slower                                          |
| logging_format          | 6.89 us                                                               | 6.99 us: 1.01x slower                                          |
| sqlglot_normalize       | 109 ms                                                                | 111 ms: 1.02x slower                                           |
| nbody                   | 87.6 ms                                                               | 89.1 ms: 1.02x slower                                          |
| scimark_fft             | 347 ms                                                                | 353 ms: 1.02x slower                                           |
| mdp                     | 2.66 sec                                                              | 2.71 sec: 1.02x slower                                         |
| spectral_norm           | 106 ms                                                                | 108 ms: 1.02x slower                                           |
| scimark_sor             | 121 ms                                                                | 123 ms: 1.02x slower                                           |
| async_generators        | 446 ms                                                                | 456 ms: 1.02x slower                                           |
| mako                    | 10.5 ms                                                               | 10.7 ms: 1.02x slower                                          |
| regex_effbot            | 3.63 ms                                                               | 3.71 ms: 1.02x slower                                          |
| pprint_pformat          | 1.48 sec                                                              | 1.52 sec: 1.02x slower                                         |
| regex_v8                | 22.8 ms                                                               | 23.3 ms: 1.02x slower                                          |
| scimark_lu              | 111 ms                                                                | 114 ms: 1.02x slower                                           |
| tomli_loads             | 2.18 sec                                                              | 2.24 sec: 1.02x slower                                         |
| pprint_safe_repr        | 729 ms                                                                | 748 ms: 1.03x slower                                           |
| hexiom                  | 6.11 ms                                                               | 6.27 ms: 1.03x slower                                          |
| unpickle                | 14.7 us                                                               | 15.1 us: 1.03x slower                                          |
| richards                | 44.0 ms                                                               | 45.2 ms: 1.03x slower                                          |
| regex_dna               | 212 ms                                                                | 219 ms: 1.03x slower                                           |
| generators              | 30.4 ms                                                               | 31.5 ms: 1.03x slower                                          |
| scimark_sparse_mat_mult | 4.69 ms                                                               | 5.02 ms: 1.07x slower                                          |
| unpack_sequence         | 48.3 ns                                                               | 51.8 ns: 1.07x slower                                          |
| Geometric mean          | (ref)                                                                 | 1.01x slower                                                   |

Benchmark hidden because not significant (28): coverage, unpickle_list, async_tree_none, meteor_contest, create_gc_cycles, chaos, asyncio_tcp, async_tree_cpu_io_mixed, xml_etree_parse, deepcopy_reduce, bench_mp_pool, sqlite_synth, async_tree_memoization, python_startup_no_site, docutils, xml_etree_generate, unpickle_pure_python, dask, nqueens, float, deepcopy, raytrace, json_dumps, sqlglot_transpile, typing_runtime_protocols, json, logging_simple, tornado_http
