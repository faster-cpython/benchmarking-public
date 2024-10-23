# Results vs. base

- fork: nick-arm
- ref: codecache_rwx
- machine: linux-x86_64
- commit hash: 7b3da21
- commit date: 2024-10-21
- overall geometric mean: 1.01x faster
- HPT reliability: 99.95%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241021-linux-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 277 ms                                                                 | 271 ms: 1.02x faster                                                |
| docutils       | 2.94 sec                                                               | 2.88 sec: 1.02x faster                                              |
| html5lib       | 66.5 ms                                                                | 67.1 ms: 1.01x slower                                               |
| sphinx         | 1.17 sec                                                               | 1.14 sec: 1.03x faster                                              |
| tornado_http   | 94.3 ms                                                                | 94.0 ms: 1.00x faster                                               |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241021-linux-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| coroutines                 | 23.1 ms                                                                | 22.8 ms: 1.02x faster                                               |
| async_generators           | 456 ms                                                                 | 449 ms: 1.01x faster                                                |
| async_tree_cpu_io_mixed_tg | 563 ms                                                                 | 557 ms: 1.01x faster                                                |
| async_tree_io_tg           | 972 ms                                                                 | 963 ms: 1.01x faster                                                |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed, asyncio_websockets, async_tree_memoization, async_tree_memoization_tg, async_tree_io, async_tree_none_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241021-linux-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 83.8 ms                                                                | 82.4 ms: 1.02x faster                                               |
| float          | 75.9 ms                                                                | 75.6 ms: 1.00x faster                                               |
| pidigits       | 187 ms                                                                 | 187 ms: 1.00x slower                                                |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241021-linux-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_dna      | 225 ms                                                                 | 212 ms: 1.06x faster                                                |
| regex_effbot   | 3.83 ms                                                                | 3.65 ms: 1.05x faster                                               |
| regex_v8       | 25.5 ms                                                                | 24.4 ms: 1.05x faster                                               |
| regex_compile  | 138 ms                                                                 | 135 ms: 1.03x faster                                                |
| Geometric mean | (ref)                                                                  | 1.05x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241021-linux-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|--------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps         | 11.1 ms                                                                | 10.8 ms: 1.03x faster                                               |
| json_loads         | 27.0 us                                                                | 26.6 us: 1.02x faster                                               |
| xml_etree_generate | 77.8 ms                                                                | 78.3 ms: 1.01x slower                                               |
| tomli_loads        | 1.90 sec                                                               | 1.92 sec: 1.01x slower                                              |
| Geometric mean     | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (5): pickle_pure_python, xml_etree_parse, unpickle_pure_python, xml_etree_iterparse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241021-linux-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 7.10 ms                                                                | 7.08 ms: 1.00x faster                                               |
| python_startup         | 11.8 ms                                                                | 11.8 ms: 1.00x faster                                               |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241021-linux-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 60.7 ms                                                                | 58.4 ms: 1.04x faster                                               |
| django_template | 36.0 ms                                                                | 35.4 ms: 1.02x faster                                               |
| mako            | 10.1 ms                                                                | 10.0 ms: 1.01x faster                                               |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241021-linux-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| richards                   | 43.2 ms                                                                | 37.1 ms: 1.16x faster                                               |
| richards_super             | 48.2 ms                                                                | 43.8 ms: 1.10x faster                                               |
| regex_dna                  | 225 ms                                                                 | 212 ms: 1.06x faster                                                |
| pprint_safe_repr           | 729 ms                                                                 | 689 ms: 1.06x faster                                                |
| pycparser                  | 1.19 sec                                                               | 1.13 sec: 1.05x faster                                              |
| pprint_pformat             | 1.50 sec                                                               | 1.43 sec: 1.05x faster                                              |
| regex_effbot               | 3.83 ms                                                                | 3.65 ms: 1.05x faster                                               |
| regex_v8                   | 25.5 ms                                                                | 24.4 ms: 1.05x faster                                               |
| genshi_xml                 | 60.7 ms                                                                | 58.4 ms: 1.04x faster                                               |
| sphinx                     | 1.17 sec                                                               | 1.14 sec: 1.03x faster                                              |
| json_dumps                 | 11.1 ms                                                                | 10.8 ms: 1.03x faster                                               |
| sqlglot_optimize           | 59.8 ms                                                                | 58.3 ms: 1.03x faster                                               |
| regex_compile              | 138 ms                                                                 | 135 ms: 1.03x faster                                                |
| 2to3                       | 277 ms                                                                 | 271 ms: 1.02x faster                                                |
| pyflate                    | 456 ms                                                                 | 447 ms: 1.02x faster                                                |
| fannkuch                   | 383 ms                                                                 | 375 ms: 1.02x faster                                                |
| scimark_monte_carlo        | 64.8 ms                                                                | 63.5 ms: 1.02x faster                                               |
| docutils                   | 2.94 sec                                                               | 2.88 sec: 1.02x faster                                              |
| django_template            | 36.0 ms                                                                | 35.4 ms: 1.02x faster                                               |
| comprehensions             | 17.0 us                                                                | 16.7 us: 1.02x faster                                               |
| nbody                      | 83.8 ms                                                                | 82.4 ms: 1.02x faster                                               |
| sympy_str                  | 301 ms                                                                 | 296 ms: 1.02x faster                                                |
| json_loads                 | 27.0 us                                                                | 26.6 us: 1.02x faster                                               |
| coroutines                 | 23.1 ms                                                                | 22.8 ms: 1.02x faster                                               |
| json                       | 5.01 ms                                                                | 4.93 ms: 1.02x faster                                               |
| sympy_integrate            | 23.4 ms                                                                | 23.1 ms: 1.02x faster                                               |
| deepcopy_memo              | 29.6 us                                                                | 29.2 us: 1.02x faster                                               |
| go                         | 132 ms                                                                 | 130 ms: 1.01x faster                                                |
| sqlglot_transpile          | 1.69 ms                                                                | 1.67 ms: 1.01x faster                                               |
| async_generators           | 456 ms                                                                 | 449 ms: 1.01x faster                                                |
| sympy_expand               | 500 ms                                                                 | 494 ms: 1.01x faster                                                |
| bench_mp_pool              | 84.3 ms                                                                | 83.4 ms: 1.01x faster                                               |
| raytrace                   | 275 ms                                                                 | 272 ms: 1.01x faster                                                |
| generators                 | 35.5 ms                                                                | 35.1 ms: 1.01x faster                                               |
| chaos                      | 59.2 ms                                                                | 58.6 ms: 1.01x faster                                               |
| sqlglot_parse              | 1.34 ms                                                                | 1.32 ms: 1.01x faster                                               |
| deepcopy                   | 269 us                                                                 | 266 us: 1.01x faster                                                |
| async_tree_cpu_io_mixed_tg | 563 ms                                                                 | 557 ms: 1.01x faster                                                |
| deltablue                  | 3.27 ms                                                                | 3.24 ms: 1.01x faster                                               |
| async_tree_io_tg           | 972 ms                                                                 | 963 ms: 1.01x faster                                                |
| sympy_sum                  | 175 ms                                                                 | 174 ms: 1.01x faster                                                |
| hexiom                     | 6.96 ms                                                                | 6.91 ms: 1.01x faster                                               |
| mako                       | 10.1 ms                                                                | 10.0 ms: 1.01x faster                                               |
| create_gc_cycles           | 2.68 ms                                                                | 2.67 ms: 1.01x faster                                               |
| sqlglot_normalize          | 114 ms                                                                 | 113 ms: 1.00x faster                                                |
| float                      | 75.9 ms                                                                | 75.6 ms: 1.00x faster                                               |
| mdp                        | 2.55 sec                                                               | 2.54 sec: 1.00x faster                                              |
| dulwich_log                | 66.8 ms                                                                | 66.5 ms: 1.00x faster                                               |
| tornado_http               | 94.3 ms                                                                | 94.0 ms: 1.00x faster                                               |
| python_startup_no_site     | 7.10 ms                                                                | 7.08 ms: 1.00x faster                                               |
| bpe_tokeniser              | 4.43 sec                                                               | 4.42 sec: 1.00x faster                                              |
| python_startup             | 11.8 ms                                                                | 11.8 ms: 1.00x faster                                               |
| pidigits                   | 187 ms                                                                 | 187 ms: 1.00x slower                                                |
| bench_thread_pool          | 876 us                                                                 | 879 us: 1.00x slower                                                |
| scimark_sor                | 118 ms                                                                 | 119 ms: 1.00x slower                                                |
| xml_etree_generate         | 77.8 ms                                                                | 78.3 ms: 1.01x slower                                               |
| scimark_lu                 | 113 ms                                                                 | 114 ms: 1.01x slower                                                |
| crypto_pyaes               | 67.9 ms                                                                | 68.4 ms: 1.01x slower                                               |
| html5lib                   | 66.5 ms                                                                | 67.1 ms: 1.01x slower                                               |
| meteor_contest             | 108 ms                                                                 | 109 ms: 1.01x slower                                                |
| scimark_fft                | 318 ms                                                                 | 322 ms: 1.01x slower                                                |
| tomli_loads                | 1.90 sec                                                               | 1.92 sec: 1.01x slower                                              |
| typing_runtime_protocols   | 164 us                                                                 | 166 us: 1.01x slower                                                |
| spectral_norm              | 114 ms                                                                 | 116 ms: 1.01x slower                                                |
| logging_simple             | 5.46 us                                                                | 5.57 us: 1.02x slower                                               |
| thrift                     | 783 us                                                                 | 800 us: 1.02x slower                                                |
| pathlib                    | 15.8 ms                                                                | 16.1 ms: 1.02x slower                                               |
| gc_traversal               | 4.62 ms                                                                | 4.74 ms: 1.03x slower                                               |
| nqueens                    | 86.2 ms                                                                | 89.4 ms: 1.04x slower                                               |
| scimark_sparse_mat_mult    | 4.55 ms                                                                | 4.77 ms: 1.05x slower                                               |
| logging_silent             | 97.2 ns                                                                | 102 ns: 1.05x slower                                                |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (18): pylint, pickle_pure_python, xml_etree_parse, async_tree_cpu_io_mixed, deepcopy_reduce, telco, logging_format, unpickle_pure_python, asyncio_websockets, xml_etree_iterparse, xml_etree_process, coverage, async_tree_memoization, genshi_text, async_tree_memoization_tg, async_tree_io, async_tree_none_tg, async_tree_none

# HPT report

- Reliability score: 99.95% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x