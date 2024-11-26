# Results vs. base

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: linux-x86_64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.010x slower
- HPT reliability: 67.33%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240914-3.14.0a0-401fff7/bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json | results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 281 ms                                                                                                                | 309 ms: 1.10x slower                                                                                                      |
| docutils       | 2.90 sec                                                                                                              | 3.16 sec: 1.09x slower                                                                                                    |
| html5lib       | 71.1 ms                                                                                                               | 71.3 ms: 1.00x slower                                                                                                     |
| tornado_http   | 116 ms                                                                                                                | 121 ms: 1.04x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                 | 1.06x slower                                                                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | results/bm-20240914-3.14.0a0-401fff7/bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json | results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json |
|---------------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 392 ms                                                                                                                | 389 ms: 1.01x faster                                                                                                      |
| asyncio_tcp_ssl           | 1.57 sec                                                                                                              | 1.58 sec: 1.00x slower                                                                                                    |
| asyncio_tcp               | 375 ms                                                                                                                | 376 ms: 1.00x slower                                                                                                      |
| asyncio_websockets        | 387 ms                                                                                                                | 397 ms: 1.02x slower                                                                                                      |
| async_tree_io_tg          | 783 ms                                                                                                                | 818 ms: 1.04x slower                                                                                                      |
| async_generators          | 358 ms                                                                                                                | 386 ms: 1.08x slower                                                                                                      |
| Geometric mean            | (ref)                                                                                                                 | 1.01x slower                                                                                                              |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none_tg, coroutines, async_tree_none, async_tree_io, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240914-3.14.0a0-401fff7/bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json | results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 85.8 ms                                                                                                               | 78.7 ms: 1.09x faster                                                                                                     |
| float          | 80.7 ms                                                                                                               | 74.2 ms: 1.09x faster                                                                                                     |
| pidigits       | 252 ms                                                                                                                | 250 ms: 1.01x faster                                                                                                      |
| Geometric mean | (ref)                                                                                                                 | 1.06x faster                                                                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240914-3.14.0a0-401fff7/bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json | results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                                                                               | 25.8 ms: 1.02x faster                                                                                                     |
| regex_effbot   | 3.45 ms                                                                                                               | 3.61 ms: 1.05x slower                                                                                                     |
| regex_compile  | 138 ms                                                                                                                | 146 ms: 1.05x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                 | 1.02x slower                                                                                                              |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240914-3.14.0a0-401fff7/bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json | results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 2.56 sec                                                                                                              | 2.09 sec: 1.22x faster                                                                                                    |
| pickle_list          | 4.64 us                                                                                                               | 4.22 us: 1.10x faster                                                                                                     |
| pickle_dict          | 33.5 us                                                                                                               | 30.7 us: 1.09x faster                                                                                                     |
| xml_etree_generate   | 84.5 ms                                                                                                               | 78.5 ms: 1.08x faster                                                                                                     |
| xml_etree_process    | 60.1 ms                                                                                                               | 55.8 ms: 1.08x faster                                                                                                     |
| json_loads           | 25.3 us                                                                                                               | 24.5 us: 1.03x faster                                                                                                     |
| xml_etree_iterparse  | 100 ms                                                                                                                | 97.4 ms: 1.03x faster                                                                                                     |
| unpickle_pure_python | 217 us                                                                                                                | 214 us: 1.01x faster                                                                                                      |
| json_dumps           | 10.8 ms                                                                                                               | 10.8 ms: 1.00x slower                                                                                                     |
| pickle_pure_python   | 322 us                                                                                                                | 326 us: 1.01x slower                                                                                                      |
| unpickle             | 15.0 us                                                                                                               | 15.2 us: 1.02x slower                                                                                                     |
| unpickle_list        | 4.60 us                                                                                                               | 4.69 us: 1.02x slower                                                                                                     |
| Geometric mean       | (ref)                                                                                                                 | 1.04x faster                                                                                                              |

Benchmark hidden because not significant (2): pickle, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240914-3.14.0a0-401fff7/bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json | results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.95 ms                                                                                                               | 8.93 ms: 1.00x faster                                                                                                     |
| Geometric mean         | (ref)                                                                                                                 | 1.00x faster                                                                                                              |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240914-3.14.0a0-401fff7/bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json | results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                                                                               | 9.18 ms: 1.13x faster                                                                                                     |
| django_template | 39.0 ms                                                                                                               | 41.6 ms: 1.07x slower                                                                                                     |
| genshi_text     | 24.3 ms                                                                                                               | 29.3 ms: 1.21x slower                                                                                                     |
| genshi_xml      | 53.4 ms                                                                                                               | 66.1 ms: 1.24x slower                                                                                                     |
| Geometric mean  | (ref)                                                                                                                 | 1.09x slower                                                                                                              |

All benchmarks:
===============

| Benchmark                 | results/bm-20240914-3.14.0a0-401fff7/bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json | results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json |
|---------------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads               | 2.56 sec                                                                                                              | 2.09 sec: 1.22x faster                                                                                                    |
| scimark_sor               | 123 ms                                                                                                                | 103 ms: 1.19x faster                                                                                                      |
| spectral_norm             | 96.2 ms                                                                                                               | 81.4 ms: 1.18x faster                                                                                                     |
| mako                      | 10.4 ms                                                                                                               | 9.18 ms: 1.13x faster                                                                                                     |
| richards                  | 50.5 ms                                                                                                               | 44.7 ms: 1.13x faster                                                                                                     |
| pyflate                   | 503 ms                                                                                                                | 454 ms: 1.11x faster                                                                                                      |
| pickle_list               | 4.64 us                                                                                                               | 4.22 us: 1.10x faster                                                                                                     |
| deepcopy_memo             | 29.1 us                                                                                                               | 26.5 us: 1.10x faster                                                                                                     |
| nbody                     | 85.8 ms                                                                                                               | 78.7 ms: 1.09x faster                                                                                                     |
| pickle_dict               | 33.5 us                                                                                                               | 30.7 us: 1.09x faster                                                                                                     |
| float                     | 80.7 ms                                                                                                               | 74.2 ms: 1.09x faster                                                                                                     |
| richards_super            | 56.8 ms                                                                                                               | 52.4 ms: 1.08x faster                                                                                                     |
| xml_etree_generate        | 84.5 ms                                                                                                               | 78.5 ms: 1.08x faster                                                                                                     |
| xml_etree_process         | 60.1 ms                                                                                                               | 55.8 ms: 1.08x faster                                                                                                     |
| gc_traversal              | 4.65 ms                                                                                                               | 4.36 ms: 1.07x faster                                                                                                     |
| deltablue                 | 3.41 ms                                                                                                               | 3.23 ms: 1.05x faster                                                                                                     |
| crypto_pyaes              | 72.6 ms                                                                                                               | 69.7 ms: 1.04x faster                                                                                                     |
| bpe_tokeniser             | 4.97 sec                                                                                                              | 4.76 sec: 1.04x faster                                                                                                    |
| coverage                  | 82.7 ms                                                                                                               | 79.4 ms: 1.04x faster                                                                                                     |
| dulwich_log               | 67.0 ms                                                                                                               | 64.6 ms: 1.04x faster                                                                                                     |
| json_loads                | 25.3 us                                                                                                               | 24.5 us: 1.03x faster                                                                                                     |
| telco                     | 8.34 ms                                                                                                               | 8.08 ms: 1.03x faster                                                                                                     |
| xml_etree_iterparse       | 100 ms                                                                                                                | 97.4 ms: 1.03x faster                                                                                                     |
| pprint_safe_repr          | 803 ms                                                                                                                | 783 ms: 1.03x faster                                                                                                      |
| scimark_monte_carlo       | 68.8 ms                                                                                                               | 67.1 ms: 1.02x faster                                                                                                     |
| fannkuch                  | 366 ms                                                                                                                | 358 ms: 1.02x faster                                                                                                      |
| regex_v8                  | 26.2 ms                                                                                                               | 25.8 ms: 1.02x faster                                                                                                     |
| sqlite_synth              | 2.75 us                                                                                                               | 2.71 us: 1.02x faster                                                                                                     |
| pprint_pformat            | 1.65 sec                                                                                                              | 1.63 sec: 1.01x faster                                                                                                    |
| unpickle_pure_python      | 217 us                                                                                                                | 214 us: 1.01x faster                                                                                                      |
| scimark_fft               | 293 ms                                                                                                                | 290 ms: 1.01x faster                                                                                                      |
| json                      | 5.25 ms                                                                                                               | 5.20 ms: 1.01x faster                                                                                                     |
| async_tree_memoization_tg | 392 ms                                                                                                                | 389 ms: 1.01x faster                                                                                                      |
| pidigits                  | 252 ms                                                                                                                | 250 ms: 1.01x faster                                                                                                      |
| scimark_sparse_mat_mult   | 4.09 ms                                                                                                               | 4.06 ms: 1.01x faster                                                                                                     |
| meteor_contest            | 129 ms                                                                                                                | 128 ms: 1.01x faster                                                                                                      |
| python_startup_no_site    | 8.95 ms                                                                                                               | 8.93 ms: 1.00x faster                                                                                                     |
| html5lib                  | 71.1 ms                                                                                                               | 71.3 ms: 1.00x slower                                                                                                     |
| asyncio_tcp_ssl           | 1.57 sec                                                                                                              | 1.58 sec: 1.00x slower                                                                                                    |
| asyncio_tcp               | 375 ms                                                                                                                | 376 ms: 1.00x slower                                                                                                      |
| json_dumps                | 10.8 ms                                                                                                               | 10.8 ms: 1.00x slower                                                                                                     |
| pickle_pure_python        | 322 us                                                                                                                | 326 us: 1.01x slower                                                                                                      |
| unpickle                  | 15.0 us                                                                                                               | 15.2 us: 1.02x slower                                                                                                     |
| unpickle_list             | 4.60 us                                                                                                               | 4.69 us: 1.02x slower                                                                                                     |
| deepcopy                  | 286 us                                                                                                                | 292 us: 1.02x slower                                                                                                      |
| logging_silent            | 99.3 ns                                                                                                               | 101 ns: 1.02x slower                                                                                                      |
| asyncio_websockets        | 387 ms                                                                                                                | 397 ms: 1.02x slower                                                                                                      |
| scimark_lu                | 95.1 ms                                                                                                               | 97.5 ms: 1.03x slower                                                                                                     |
| logging_simple            | 6.35 us                                                                                                               | 6.53 us: 1.03x slower                                                                                                     |
| logging_format            | 6.98 us                                                                                                               | 7.20 us: 1.03x slower                                                                                                     |
| thrift                    | 857 us                                                                                                                | 885 us: 1.03x slower                                                                                                      |
| tornado_http              | 116 ms                                                                                                                | 121 ms: 1.04x slower                                                                                                      |
| async_tree_io_tg          | 783 ms                                                                                                                | 818 ms: 1.04x slower                                                                                                      |
| regex_effbot              | 3.45 ms                                                                                                               | 3.61 ms: 1.05x slower                                                                                                     |
| bench_mp_pool             | 4.77 ms                                                                                                               | 5.00 ms: 1.05x slower                                                                                                     |
| chaos                     | 62.2 ms                                                                                                               | 65.6 ms: 1.05x slower                                                                                                     |
| mdp                       | 2.47 sec                                                                                                              | 2.61 sec: 1.05x slower                                                                                                    |
| regex_compile             | 138 ms                                                                                                                | 146 ms: 1.05x slower                                                                                                      |
| sympy_expand              | 497 ms                                                                                                                | 525 ms: 1.05x slower                                                                                                      |
| sqlglot_parse             | 1.40 ms                                                                                                               | 1.48 ms: 1.05x slower                                                                                                     |
| comprehensions            | 17.3 us                                                                                                               | 18.3 us: 1.06x slower                                                                                                     |
| sympy_str                 | 290 ms                                                                                                                | 308 ms: 1.06x slower                                                                                                      |
| django_template           | 39.0 ms                                                                                                               | 41.6 ms: 1.07x slower                                                                                                     |
| bench_thread_pool         | 863 us                                                                                                                | 922 us: 1.07x slower                                                                                                      |
| pycparser                 | 1.21 sec                                                                                                              | 1.30 sec: 1.07x slower                                                                                                    |
| sqlglot_normalize         | 119 ms                                                                                                                | 128 ms: 1.07x slower                                                                                                      |
| sqlglot_transpile         | 1.80 ms                                                                                                               | 1.93 ms: 1.07x slower                                                                                                     |
| async_generators          | 358 ms                                                                                                                | 386 ms: 1.08x slower                                                                                                      |
| typing_runtime_protocols  | 171 us                                                                                                                | 186 us: 1.09x slower                                                                                                      |
| docutils                  | 2.90 sec                                                                                                              | 3.16 sec: 1.09x slower                                                                                                    |
| hexiom                    | 6.36 ms                                                                                                               | 6.95 ms: 1.09x slower                                                                                                     |
| nqueens                   | 88.7 ms                                                                                                               | 97.0 ms: 1.09x slower                                                                                                     |
| go                        | 137 ms                                                                                                                | 150 ms: 1.10x slower                                                                                                      |
| sympy_sum                 | 152 ms                                                                                                                | 167 ms: 1.10x slower                                                                                                      |
| 2to3                      | 281 ms                                                                                                                | 309 ms: 1.10x slower                                                                                                      |
| sqlglot_optimize          | 58.8 ms                                                                                                               | 65.0 ms: 1.11x slower                                                                                                     |
| sympy_integrate           | 23.0 ms                                                                                                               | 26.3 ms: 1.14x slower                                                                                                     |
| raytrace                  | 270 ms                                                                                                                | 313 ms: 1.16x slower                                                                                                      |
| pylint                    | 348 ms                                                                                                                | 408 ms: 1.17x slower                                                                                                      |
| genshi_text               | 24.3 ms                                                                                                               | 29.3 ms: 1.21x slower                                                                                                     |
| genshi_xml                | 53.4 ms                                                                                                               | 66.1 ms: 1.24x slower                                                                                                     |
| generators                | 28.9 ms                                                                                                               | 36.5 ms: 1.26x slower                                                                                                     |
| unpack_sequence           | 49.6 ns                                                                                                               | 87.7 ns: 1.77x slower                                                                                                     |
| Geometric mean            | (ref)                                                                                                                 | 1.02x slower                                                                                                              |

Benchmark hidden because not significant (14): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none_tg, pickle, pathlib, xml_etree_parse, coroutines, python_startup, deepcopy_reduce, create_gc_cycles, async_tree_none, async_tree_io, regex_dna, async_tree_memoization

- Geometric mean (including insignificant results): 1.010x slower
# HPT report

- Reliability score: 67.33% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.08x