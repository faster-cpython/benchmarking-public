# Results vs. base

- fork: Fidget-Spinner
- ref: fix_unsafe_refcounti
- machine: linux-x86_64
- commit hash: 8278d07
- commit date: 2024-10-12
- overall geometric mean: 1.00x faster
- HPT reliability: 99.80%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241011-linux-x86_64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 | bm-20241012-linux-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                | 252 ms: 1.01x faster                                                            |
| html5lib       | 63.2 ms                                                               | 61.9 ms: 1.02x faster                                                           |
| tornado_http   | 90.4 ms                                                               | 89.9 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241011-linux-x86_64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 | bm-20241012-linux-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| coroutines       | 23.9 ms                                                               | 23.2 ms: 1.03x faster                                                           |
| async_generators | 435 ms                                                                | 431 ms: 1.01x faster                                                            |
| asyncio_tcp_ssl  | 1.79 sec                                                              | 1.79 sec: 1.00x faster                                                          |
| Geometric mean   | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (10): async_tree_none, async_tree_none_tg, async_tree_memoization_tg, async_tree_io_tg, async_tree_memoization, async_tree_io, asyncio_tcp, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241011-linux-x86_64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 | bm-20241012-linux-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                | 187 ms: 1.00x faster                                                            |
| nbody          | 88.3 ms                                                               | 88.9 ms: 1.01x slower                                                           |
| float          | 77.0 ms                                                               | 77.8 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241011-linux-x86_64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 | bm-20241012-linux-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.74 ms                                                               | 3.61 ms: 1.04x faster                                                           |
| regex_dna      | 224 ms                                                                | 217 ms: 1.03x faster                                                            |
| regex_compile  | 129 ms                                                                | 128 ms: 1.01x faster                                                            |
| regex_v8       | 24.8 ms                                                               | 24.9 ms: 1.00x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241011-linux-x86_64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 | bm-20241012-linux-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.14 sec                                                              | 2.10 sec: 1.02x faster                                                          |
| unpickle_pure_python | 219 us                                                                | 215 us: 1.02x faster                                                            |
| pickle               | 11.6 us                                                               | 11.4 us: 1.02x faster                                                           |
| pickle_pure_python   | 309 us                                                                | 306 us: 1.01x faster                                                            |
| pickle_dict          | 34.7 us                                                               | 34.5 us: 1.01x faster                                                           |
| xml_etree_generate   | 85.0 ms                                                               | 85.5 ms: 1.01x slower                                                           |
| json_loads           | 26.7 us                                                               | 26.8 us: 1.01x slower                                                           |
| json_dumps           | 11.7 ms                                                               | 11.8 ms: 1.01x slower                                                           |
| xml_etree_process    | 58.7 ms                                                               | 59.4 ms: 1.01x slower                                                           |
| pickle_list          | 5.06 us                                                               | 5.14 us: 1.02x slower                                                           |
| unpickle_list        | 5.22 us                                                               | 5.43 us: 1.04x slower                                                           |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_iterparse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241011-linux-x86_64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 | bm-20241012-linux-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.6 ms: 1.00x slower                                                           |
| python_startup_no_site | 7.01 ms                                                               | 7.03 ms: 1.00x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241011-linux-x86_64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 | bm-20241012-linux-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 12.0 ms                                                               | 11.5 ms: 1.04x faster                                                           |
| genshi_xml      | 50.0 ms                                                               | 49.3 ms: 1.01x faster                                                           |
| django_template | 34.1 ms                                                               | 33.8 ms: 1.01x faster                                                           |
| Geometric mean  | (ref)                                                                 | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20241011-linux-x86_64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 | bm-20241012-linux-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| spectral_norm            | 115 ms                                                                | 109 ms: 1.06x faster                                                            |
| mako                     | 12.0 ms                                                               | 11.5 ms: 1.04x faster                                                           |
| go                       | 124 ms                                                                | 119 ms: 1.04x faster                                                            |
| unpack_sequence          | 52.2 ns                                                               | 50.4 ns: 1.04x faster                                                           |
| regex_effbot             | 3.74 ms                                                               | 3.61 ms: 1.04x faster                                                           |
| regex_dna                | 224 ms                                                                | 217 ms: 1.03x faster                                                            |
| deltablue                | 3.30 ms                                                               | 3.21 ms: 1.03x faster                                                           |
| coroutines               | 23.9 ms                                                               | 23.2 ms: 1.03x faster                                                           |
| comprehensions           | 17.0 us                                                               | 16.6 us: 1.02x faster                                                           |
| html5lib                 | 63.2 ms                                                               | 61.9 ms: 1.02x faster                                                           |
| tomli_loads              | 2.14 sec                                                              | 2.10 sec: 1.02x faster                                                          |
| raytrace                 | 267 ms                                                                | 262 ms: 1.02x faster                                                            |
| unpickle_pure_python     | 219 us                                                                | 215 us: 1.02x faster                                                            |
| chaos                    | 60.1 ms                                                               | 58.9 ms: 1.02x faster                                                           |
| pickle                   | 11.6 us                                                               | 11.4 us: 1.02x faster                                                           |
| scimark_sor              | 126 ms                                                                | 124 ms: 1.02x faster                                                            |
| generators               | 26.8 ms                                                               | 26.3 ms: 1.02x faster                                                           |
| pycparser                | 1.15 sec                                                              | 1.13 sec: 1.02x faster                                                          |
| logging_simple           | 5.71 us                                                               | 5.63 us: 1.02x faster                                                           |
| pprint_pformat           | 1.51 sec                                                              | 1.48 sec: 1.02x faster                                                          |
| genshi_xml               | 50.0 ms                                                               | 49.3 ms: 1.01x faster                                                           |
| fannkuch                 | 404 ms                                                                | 399 ms: 1.01x faster                                                            |
| sqlite_synth             | 2.89 us                                                               | 2.86 us: 1.01x faster                                                           |
| json                     | 5.11 ms                                                               | 5.06 ms: 1.01x faster                                                           |
| bpe_tokeniser            | 4.72 sec                                                              | 4.67 sec: 1.01x faster                                                          |
| django_template          | 34.1 ms                                                               | 33.8 ms: 1.01x faster                                                           |
| sympy_sum                | 148 ms                                                                | 147 ms: 1.01x faster                                                            |
| async_generators         | 435 ms                                                                | 431 ms: 1.01x faster                                                            |
| 2to3                     | 254 ms                                                                | 252 ms: 1.01x faster                                                            |
| pickle_pure_python       | 309 us                                                                | 306 us: 1.01x faster                                                            |
| sympy_expand             | 455 ms                                                                | 451 ms: 1.01x faster                                                            |
| regex_compile            | 129 ms                                                                | 128 ms: 1.01x faster                                                            |
| pickle_dict              | 34.7 us                                                               | 34.5 us: 1.01x faster                                                           |
| pprint_safe_repr         | 731 ms                                                                | 727 ms: 1.01x faster                                                            |
| sympy_integrate          | 19.9 ms                                                               | 19.8 ms: 1.01x faster                                                           |
| tornado_http             | 90.4 ms                                                               | 89.9 ms: 1.01x faster                                                           |
| deepcopy                 | 263 us                                                                | 262 us: 1.01x faster                                                            |
| hexiom                   | 6.32 ms                                                               | 6.29 ms: 1.00x faster                                                           |
| deepcopy_memo            | 30.9 us                                                               | 30.7 us: 1.00x faster                                                           |
| bench_thread_pool        | 846 us                                                                | 844 us: 1.00x faster                                                            |
| sqlglot_optimize         | 53.2 ms                                                               | 53.1 ms: 1.00x faster                                                           |
| asyncio_tcp_ssl          | 1.79 sec                                                              | 1.79 sec: 1.00x faster                                                          |
| pidigits                 | 187 ms                                                                | 187 ms: 1.00x faster                                                            |
| python_startup           | 10.5 ms                                                               | 10.6 ms: 1.00x slower                                                           |
| python_startup_no_site   | 7.01 ms                                                               | 7.03 ms: 1.00x slower                                                           |
| regex_v8                 | 24.8 ms                                                               | 24.9 ms: 1.00x slower                                                           |
| sqlglot_transpile        | 1.58 ms                                                               | 1.58 ms: 1.00x slower                                                           |
| xml_etree_generate       | 85.0 ms                                                               | 85.5 ms: 1.01x slower                                                           |
| sqlglot_parse            | 1.28 ms                                                               | 1.29 ms: 1.01x slower                                                           |
| json_loads               | 26.7 us                                                               | 26.8 us: 1.01x slower                                                           |
| nbody                    | 88.3 ms                                                               | 88.9 ms: 1.01x slower                                                           |
| pathlib                  | 16.0 ms                                                               | 16.1 ms: 1.01x slower                                                           |
| meteor_contest           | 106 ms                                                                | 107 ms: 1.01x slower                                                            |
| json_dumps               | 11.7 ms                                                               | 11.8 ms: 1.01x slower                                                           |
| float                    | 77.0 ms                                                               | 77.8 ms: 1.01x slower                                                           |
| xml_etree_process        | 58.7 ms                                                               | 59.4 ms: 1.01x slower                                                           |
| crypto_pyaes             | 72.1 ms                                                               | 73.0 ms: 1.01x slower                                                           |
| mdp                      | 2.54 sec                                                              | 2.57 sec: 1.01x slower                                                          |
| scimark_fft              | 358 ms                                                                | 363 ms: 1.02x slower                                                            |
| pickle_list              | 5.06 us                                                               | 5.14 us: 1.02x slower                                                           |
| pyflate                  | 461 ms                                                                | 468 ms: 1.02x slower                                                            |
| typing_runtime_protocols | 159 us                                                                | 162 us: 1.02x slower                                                            |
| unpickle_list            | 5.22 us                                                               | 5.43 us: 1.04x slower                                                           |
| scimark_sparse_mat_mult  | 4.57 ms                                                               | 4.92 ms: 1.08x slower                                                           |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (33): async_tree_none, async_tree_none_tg, async_tree_memoization_tg, logging_format, async_tree_io_tg, coverage, richards, scimark_lu, genshi_text, deepcopy_reduce, dulwich_log, sympy_str, bench_mp_pool, scimark_monte_carlo, async_tree_memoization, create_gc_cycles, pylint, sqlglot_normalize, async_tree_io, xml_etree_parse, richards_super, gc_traversal, docutils, nqueens, xml_etree_iterparse, asyncio_tcp, thrift, telco, asyncio_websockets, async_tree_cpu_io_mixed_tg, logging_silent, async_tree_cpu_io_mixed, unpickle

# HPT report

- Reliability score: 99.80% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x