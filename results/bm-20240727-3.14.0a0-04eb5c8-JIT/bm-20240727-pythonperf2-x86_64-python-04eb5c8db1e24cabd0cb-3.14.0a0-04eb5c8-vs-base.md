# Results vs. base

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: linux-x86_64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.01x slower
- HPT reliability: 90.43%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                                                                                | 308 ms: 1.08x slower                                                                                                      |
| docutils       | 2.98 sec                                                                                                              | 3.15 sec: 1.06x slower                                                                                                    |
| html5lib       | 72.9 ms                                                                                                               | 70.6 ms: 1.03x faster                                                                                                     |
| tornado_http   | 117 ms                                                                                                                | 120 ms: 1.02x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                 | 1.03x slower                                                                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| async_tree_none  | 333 ms                                                                                                                | 323 ms: 1.03x faster                                                                                                      |
| asyncio_tcp_ssl  | 1.57 sec                                                                                                              | 1.58 sec: 1.00x slower                                                                                                    |
| asyncio_tcp      | 374 ms                                                                                                                | 376 ms: 1.01x slower                                                                                                      |
| async_tree_io_tg | 778 ms                                                                                                                | 789 ms: 1.02x slower                                                                                                      |
| coroutines       | 21.3 ms                                                                                                               | 21.7 ms: 1.02x slower                                                                                                     |
| async_generators | 367 ms                                                                                                                | 387 ms: 1.05x slower                                                                                                      |
| Geometric mean   | (ref)                                                                                                                 | 1.01x slower                                                                                                              |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed, asyncio_websockets, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_io, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| float          | 81.0 ms                                                                                                               | 74.5 ms: 1.09x faster                                                                                                     |
| nbody          | 86.7 ms                                                                                                               | 84.0 ms: 1.03x faster                                                                                                     |
| pidigits       | 253 ms                                                                                                                | 250 ms: 1.01x faster                                                                                                      |
| Geometric mean | (ref)                                                                                                                 | 1.04x faster                                                                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 140 ms                                                                                                                | 134 ms: 1.04x faster                                                                                                      |
| regex_v8       | 26.8 ms                                                                                                               | 27.1 ms: 1.01x slower                                                                                                     |
| regex_effbot   | 3.50 ms                                                                                                               | 3.60 ms: 1.03x slower                                                                                                     |
| regex_dna      | 242 ms                                                                                                                | 259 ms: 1.07x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                 | 1.02x slower                                                                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 105 ms                                                                                                                | 97.8 ms: 1.07x faster                                                                                                     |
| tomli_loads          | 2.20 sec                                                                                                              | 2.10 sec: 1.05x faster                                                                                                    |
| unpickle_pure_python | 218 us                                                                                                                | 211 us: 1.04x faster                                                                                                      |
| xml_etree_generate   | 85.0 ms                                                                                                               | 82.3 ms: 1.03x faster                                                                                                     |
| xml_etree_parse      | 145 ms                                                                                                                | 141 ms: 1.03x faster                                                                                                      |
| xml_etree_process    | 59.3 ms                                                                                                               | 57.6 ms: 1.03x faster                                                                                                     |
| json_dumps           | 10.9 ms                                                                                                               | 10.8 ms: 1.01x faster                                                                                                     |
| json_loads           | 25.7 us                                                                                                               | 25.5 us: 1.01x faster                                                                                                     |
| Geometric mean       | (ref)                                                                                                                 | 1.03x faster                                                                                                              |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 9.05 ms                                                                                                               | 9.06 ms: 1.00x slower                                                                                                     |
| Geometric mean         | (ref)                                                                                                                 | 1.00x slower                                                                                                              |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                                                                               | 9.07 ms: 1.15x faster                                                                                                     |
| django_template | 38.7 ms                                                                                                               | 41.4 ms: 1.07x slower                                                                                                     |
| genshi_xml      | 56.6 ms                                                                                                               | 64.5 ms: 1.14x slower                                                                                                     |
| genshi_text     | 25.1 ms                                                                                                               | 29.1 ms: 1.16x slower                                                                                                     |
| Geometric mean  | (ref)                                                                                                                 | 1.05x slower                                                                                                              |

All benchmarks:
===============

| Benchmark                | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|--------------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| spectral_norm            | 96.2 ms                                                                                                               | 81.4 ms: 1.18x faster                                                                                                     |
| mako                     | 10.4 ms                                                                                                               | 9.07 ms: 1.15x faster                                                                                                     |
| richards                 | 51.4 ms                                                                                                               | 45.5 ms: 1.13x faster                                                                                                     |
| pyflate                  | 479 ms                                                                                                                | 433 ms: 1.11x faster                                                                                                      |
| richards_super           | 57.2 ms                                                                                                               | 52.3 ms: 1.09x faster                                                                                                     |
| float                    | 81.0 ms                                                                                                               | 74.5 ms: 1.09x faster                                                                                                     |
| scimark_monte_carlo      | 68.9 ms                                                                                                               | 64.3 ms: 1.07x faster                                                                                                     |
| xml_etree_iterparse      | 105 ms                                                                                                                | 97.8 ms: 1.07x faster                                                                                                     |
| deepcopy_memo            | 30.5 us                                                                                                               | 28.8 us: 1.06x faster                                                                                                     |
| crypto_pyaes             | 73.7 ms                                                                                                               | 69.9 ms: 1.05x faster                                                                                                     |
| pprint_safe_repr         | 838 ms                                                                                                                | 796 ms: 1.05x faster                                                                                                      |
| tomli_loads              | 2.20 sec                                                                                                              | 2.10 sec: 1.05x faster                                                                                                    |
| regex_compile            | 140 ms                                                                                                                | 134 ms: 1.04x faster                                                                                                      |
| scimark_fft              | 304 ms                                                                                                                | 292 ms: 1.04x faster                                                                                                      |
| pprint_pformat           | 1.71 sec                                                                                                              | 1.64 sec: 1.04x faster                                                                                                    |
| unpickle_pure_python     | 218 us                                                                                                                | 211 us: 1.04x faster                                                                                                      |
| nbody                    | 86.7 ms                                                                                                               | 84.0 ms: 1.03x faster                                                                                                     |
| html5lib                 | 72.9 ms                                                                                                               | 70.6 ms: 1.03x faster                                                                                                     |
| xml_etree_generate       | 85.0 ms                                                                                                               | 82.3 ms: 1.03x faster                                                                                                     |
| xml_etree_parse          | 145 ms                                                                                                                | 141 ms: 1.03x faster                                                                                                      |
| async_tree_none          | 333 ms                                                                                                                | 323 ms: 1.03x faster                                                                                                      |
| xml_etree_process        | 59.3 ms                                                                                                               | 57.6 ms: 1.03x faster                                                                                                     |
| coverage                 | 84.2 ms                                                                                                               | 81.9 ms: 1.03x faster                                                                                                     |
| fannkuch                 | 359 ms                                                                                                                | 351 ms: 1.03x faster                                                                                                      |
| bpe_tokeniser            | 4.91 sec                                                                                                              | 4.82 sec: 1.02x faster                                                                                                    |
| meteor_contest           | 129 ms                                                                                                                | 127 ms: 1.02x faster                                                                                                      |
| create_gc_cycles         | 1.98 ms                                                                                                               | 1.94 ms: 1.02x faster                                                                                                     |
| pidigits                 | 253 ms                                                                                                                | 250 ms: 1.01x faster                                                                                                      |
| telco                    | 8.11 ms                                                                                                               | 8.02 ms: 1.01x faster                                                                                                     |
| scimark_sparse_mat_mult  | 4.19 ms                                                                                                               | 4.16 ms: 1.01x faster                                                                                                     |
| json_dumps               | 10.9 ms                                                                                                               | 10.8 ms: 1.01x faster                                                                                                     |
| json_loads               | 25.7 us                                                                                                               | 25.5 us: 1.01x faster                                                                                                     |
| python_startup_no_site   | 9.05 ms                                                                                                               | 9.06 ms: 1.00x slower                                                                                                     |
| asyncio_tcp_ssl          | 1.57 sec                                                                                                              | 1.58 sec: 1.00x slower                                                                                                    |
| asyncio_tcp              | 374 ms                                                                                                                | 376 ms: 1.01x slower                                                                                                      |
| regex_v8                 | 26.8 ms                                                                                                               | 27.1 ms: 1.01x slower                                                                                                     |
| async_tree_io_tg         | 778 ms                                                                                                                | 789 ms: 1.02x slower                                                                                                      |
| pathlib                  | 16.0 ms                                                                                                               | 16.2 ms: 1.02x slower                                                                                                     |
| pycparser                | 1.22 sec                                                                                                              | 1.24 sec: 1.02x slower                                                                                                    |
| logging_simple           | 6.22 us                                                                                                               | 6.35 us: 1.02x slower                                                                                                     |
| logging_format           | 6.87 us                                                                                                               | 7.03 us: 1.02x slower                                                                                                     |
| coroutines               | 21.3 ms                                                                                                               | 21.7 ms: 1.02x slower                                                                                                     |
| sqlglot_parse            | 1.39 ms                                                                                                               | 1.42 ms: 1.02x slower                                                                                                     |
| tornado_http             | 117 ms                                                                                                                | 120 ms: 1.02x slower                                                                                                      |
| regex_effbot             | 3.50 ms                                                                                                               | 3.60 ms: 1.03x slower                                                                                                     |
| json                     | 5.41 ms                                                                                                               | 5.56 ms: 1.03x slower                                                                                                     |
| dask                     | 380 ms                                                                                                                | 392 ms: 1.03x slower                                                                                                      |
| mdp                      | 2.49 sec                                                                                                              | 2.57 sec: 1.03x slower                                                                                                    |
| deepcopy_reduce          | 2.91 us                                                                                                               | 3.02 us: 1.04x slower                                                                                                     |
| logging_silent           | 96.6 ns                                                                                                               | 100 ns: 1.04x slower                                                                                                      |
| hexiom                   | 6.34 ms                                                                                                               | 6.60 ms: 1.04x slower                                                                                                     |
| thrift                   | 866 us                                                                                                                | 903 us: 1.04x slower                                                                                                      |
| sympy_expand             | 502 ms                                                                                                                | 524 ms: 1.04x slower                                                                                                      |
| comprehensions           | 17.4 us                                                                                                               | 18.2 us: 1.04x slower                                                                                                     |
| sqlglot_transpile        | 1.76 ms                                                                                                               | 1.84 ms: 1.05x slower                                                                                                     |
| bench_thread_pool        | 861 us                                                                                                                | 902 us: 1.05x slower                                                                                                      |
| chaos                    | 62.8 ms                                                                                                               | 66.0 ms: 1.05x slower                                                                                                     |
| async_generators         | 367 ms                                                                                                                | 387 ms: 1.05x slower                                                                                                      |
| go                       | 158 ms                                                                                                                | 166 ms: 1.05x slower                                                                                                      |
| deepcopy                 | 292 us                                                                                                                | 308 us: 1.06x slower                                                                                                      |
| docutils                 | 2.98 sec                                                                                                              | 3.15 sec: 1.06x slower                                                                                                    |
| bench_mp_pool            | 4.61 ms                                                                                                               | 4.87 ms: 1.06x slower                                                                                                     |
| sympy_str                | 292 ms                                                                                                                | 310 ms: 1.06x slower                                                                                                      |
| deltablue                | 3.40 ms                                                                                                               | 3.61 ms: 1.06x slower                                                                                                     |
| regex_dna                | 242 ms                                                                                                                | 259 ms: 1.07x slower                                                                                                      |
| django_template          | 38.7 ms                                                                                                               | 41.4 ms: 1.07x slower                                                                                                     |
| typing_runtime_protocols | 175 us                                                                                                                | 188 us: 1.07x slower                                                                                                      |
| 2to3                     | 285 ms                                                                                                                | 308 ms: 1.08x slower                                                                                                      |
| sympy_sum                | 153 ms                                                                                                                | 166 ms: 1.08x slower                                                                                                      |
| nqueens                  | 88.1 ms                                                                                                               | 96.1 ms: 1.09x slower                                                                                                     |
| sqlglot_optimize         | 58.4 ms                                                                                                               | 63.8 ms: 1.09x slower                                                                                                     |
| raytrace                 | 274 ms                                                                                                                | 300 ms: 1.10x slower                                                                                                      |
| pylint                   | 346 ms                                                                                                                | 383 ms: 1.11x slower                                                                                                      |
| sympy_integrate          | 23.1 ms                                                                                                               | 25.6 ms: 1.11x slower                                                                                                     |
| sqlglot_normalize        | 118 ms                                                                                                                | 131 ms: 1.11x slower                                                                                                      |
| genshi_xml               | 56.6 ms                                                                                                               | 64.5 ms: 1.14x slower                                                                                                     |
| scimark_lu               | 98.6 ms                                                                                                               | 113 ms: 1.15x slower                                                                                                      |
| genshi_text              | 25.1 ms                                                                                                               | 29.1 ms: 1.16x slower                                                                                                     |
| scimark_sor              | 120 ms                                                                                                                | 142 ms: 1.18x slower                                                                                                      |
| Geometric mean           | (ref)                                                                                                                 | 1.01x slower                                                                                                              |

Benchmark hidden because not significant (11): async_tree_cpu_io_mixed, pickle_pure_python, gc_traversal, python_startup, asyncio_websockets, generators, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_io, async_tree_memoization

# HPT report

- Reliability score: 90.43% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.06x