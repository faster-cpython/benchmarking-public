# Results vs. base

- fork: Fidget-Spinner
- ref: fix_unsafe_refcounti
- machine: linux-x86_64
- commit hash: 8278d07
- commit date: 2024-10-12
- overall geometric mean: 1.00x slower
- HPT reliability: 86.88%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241011-pythonperf2-x86_64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| html5lib       | 69.5 ms                                                                     | 70.1 ms: 1.01x slower                                                                 |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                          |

Benchmark hidden because not significant (3): 2to3, docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241011-pythonperf2-x86_64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_io_tg | 791 ms                                                                      | 783 ms: 1.01x faster                                                                  |
| asyncio_tcp      | 369 ms                                                                      | 371 ms: 1.00x slower                                                                  |
| coroutines       | 21.0 ms                                                                     | 21.5 ms: 1.02x slower                                                                 |
| async_generators | 360 ms                                                                      | 371 ms: 1.03x slower                                                                  |
| Geometric mean   | (ref)                                                                       | 1.01x slower                                                                          |

Benchmark hidden because not significant (9): async_tree_none_tg, async_tree_io, asyncio_tcp_ssl, async_tree_memoization_tg, asyncio_websockets, async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241011-pythonperf2-x86_64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| float          | 82.1 ms                                                                     | 80.6 ms: 1.02x faster                                                                 |
| pidigits       | 253 ms                                                                      | 252 ms: 1.00x faster                                                                  |
| nbody          | 86.8 ms                                                                     | 89.8 ms: 1.03x slower                                                                 |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241011-pythonperf2-x86_64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_effbot   | 3.49 ms                                                                     | 3.46 ms: 1.01x faster                                                                 |
| regex_compile  | 138 ms                                                                      | 140 ms: 1.01x slower                                                                  |
| regex_v8       | 24.6 ms                                                                     | 24.9 ms: 1.01x slower                                                                 |
| regex_dna      | 230 ms                                                                      | 242 ms: 1.05x slower                                                                  |
| Geometric mean | (ref)                                                                       | 1.02x slower                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241011-pythonperf2-x86_64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| pickle_dict          | 32.4 us                                                                     | 30.4 us: 1.06x faster                                                                 |
| json_loads           | 25.4 us                                                                     | 24.9 us: 1.02x faster                                                                 |
| xml_etree_generate   | 86.2 ms                                                                     | 84.9 ms: 1.02x faster                                                                 |
| unpickle_pure_python | 214 us                                                                      | 215 us: 1.01x slower                                                                  |
| xml_etree_iterparse  | 100 ms                                                                      | 101 ms: 1.01x slower                                                                  |
| pickle               | 10.5 us                                                                     | 10.6 us: 1.01x slower                                                                 |
| pickle_list          | 4.49 us                                                                     | 4.57 us: 1.02x slower                                                                 |
| unpickle_list        | 4.54 us                                                                     | 4.69 us: 1.03x slower                                                                 |
| unpickle             | 14.7 us                                                                     | 15.7 us: 1.07x slower                                                                 |
| Geometric mean       | (ref)                                                                       | 1.00x slower                                                                          |

Benchmark hidden because not significant (5): json_dumps, tomli_loads, pickle_pure_python, xml_etree_process, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241011-pythonperf2-x86_64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 13.4 ms                                                                     | 13.4 ms: 1.00x faster                                                                 |
| python_startup_no_site | 8.99 ms                                                                     | 8.96 ms: 1.00x faster                                                                 |
| Geometric mean         | (ref)                                                                       | 1.00x faster                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241011-pythonperf2-x86_64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|-----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 10.7 ms                                                                     | 10.8 ms: 1.01x slower                                                                 |
| genshi_text     | 24.3 ms                                                                     | 24.6 ms: 1.01x slower                                                                 |
| django_template | 41.0 ms                                                                     | 42.7 ms: 1.04x slower                                                                 |
| Geometric mean  | (ref)                                                                       | 1.02x slower                                                                          |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20241011-pythonperf2-x86_64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|--------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| unpack_sequence          | 53.9 ns                                                                     | 49.1 ns: 1.10x faster                                                                 |
| pickle_dict              | 32.4 us                                                                     | 30.4 us: 1.06x faster                                                                 |
| richards_super           | 58.4 ms                                                                     | 56.2 ms: 1.04x faster                                                                 |
| richards                 | 51.1 ms                                                                     | 49.3 ms: 1.04x faster                                                                 |
| go                       | 141 ms                                                                      | 137 ms: 1.03x faster                                                                  |
| pycparser                | 1.25 sec                                                                    | 1.21 sec: 1.03x faster                                                                |
| meteor_contest           | 126 ms                                                                      | 123 ms: 1.03x faster                                                                  |
| bench_thread_pool        | 905 us                                                                      | 888 us: 1.02x faster                                                                  |
| float                    | 82.1 ms                                                                     | 80.6 ms: 1.02x faster                                                                 |
| json_loads               | 25.4 us                                                                     | 24.9 us: 1.02x faster                                                                 |
| xml_etree_generate       | 86.2 ms                                                                     | 84.9 ms: 1.02x faster                                                                 |
| logging_format           | 7.19 us                                                                     | 7.08 us: 1.02x faster                                                                 |
| sympy_sum                | 153 ms                                                                      | 151 ms: 1.01x faster                                                                  |
| deepcopy                 | 291 us                                                                      | 287 us: 1.01x faster                                                                  |
| deepcopy_memo            | 30.0 us                                                                     | 29.6 us: 1.01x faster                                                                 |
| thrift                   | 886 us                                                                      | 876 us: 1.01x faster                                                                  |
| sqlglot_transpile        | 1.80 ms                                                                     | 1.78 ms: 1.01x faster                                                                 |
| mdp                      | 2.50 sec                                                                    | 2.47 sec: 1.01x faster                                                                |
| async_tree_io_tg         | 791 ms                                                                      | 783 ms: 1.01x faster                                                                  |
| pprint_safe_repr         | 792 ms                                                                      | 784 ms: 1.01x faster                                                                  |
| regex_effbot             | 3.49 ms                                                                     | 3.46 ms: 1.01x faster                                                                 |
| sqlglot_parse            | 1.42 ms                                                                     | 1.41 ms: 1.01x faster                                                                 |
| deltablue                | 3.42 ms                                                                     | 3.39 ms: 1.01x faster                                                                 |
| sqlite_synth             | 2.76 us                                                                     | 2.74 us: 1.01x faster                                                                 |
| sympy_str                | 292 ms                                                                      | 290 ms: 1.01x faster                                                                  |
| comprehensions           | 17.2 us                                                                     | 17.1 us: 1.01x faster                                                                 |
| sympy_integrate          | 23.5 ms                                                                     | 23.4 ms: 1.00x faster                                                                 |
| python_startup           | 13.4 ms                                                                     | 13.4 ms: 1.00x faster                                                                 |
| scimark_sparse_mat_mult  | 4.14 ms                                                                     | 4.13 ms: 1.00x faster                                                                 |
| python_startup_no_site   | 8.99 ms                                                                     | 8.96 ms: 1.00x faster                                                                 |
| pidigits                 | 253 ms                                                                      | 252 ms: 1.00x faster                                                                  |
| bpe_tokeniser            | 4.80 sec                                                                    | 4.80 sec: 1.00x slower                                                                |
| hexiom                   | 6.25 ms                                                                     | 6.26 ms: 1.00x slower                                                                 |
| asyncio_tcp              | 369 ms                                                                      | 371 ms: 1.00x slower                                                                  |
| unpickle_pure_python     | 214 us                                                                      | 215 us: 1.01x slower                                                                  |
| telco                    | 7.82 ms                                                                     | 7.88 ms: 1.01x slower                                                                 |
| nqueens                  | 89.3 ms                                                                     | 90.0 ms: 1.01x slower                                                                 |
| sqlglot_optimize         | 59.1 ms                                                                     | 59.5 ms: 1.01x slower                                                                 |
| mako                     | 10.7 ms                                                                     | 10.8 ms: 1.01x slower                                                                 |
| html5lib                 | 69.5 ms                                                                     | 70.1 ms: 1.01x slower                                                                 |
| scimark_sor              | 107 ms                                                                      | 108 ms: 1.01x slower                                                                  |
| genshi_text              | 24.3 ms                                                                     | 24.6 ms: 1.01x slower                                                                 |
| generators               | 29.0 ms                                                                     | 29.3 ms: 1.01x slower                                                                 |
| scimark_fft              | 295 ms                                                                      | 298 ms: 1.01x slower                                                                  |
| chaos                    | 62.9 ms                                                                     | 63.5 ms: 1.01x slower                                                                 |
| pathlib                  | 15.6 ms                                                                     | 15.8 ms: 1.01x slower                                                                 |
| xml_etree_iterparse      | 100 ms                                                                      | 101 ms: 1.01x slower                                                                  |
| spectral_norm            | 95.5 ms                                                                     | 96.5 ms: 1.01x slower                                                                 |
| pickle                   | 10.5 us                                                                     | 10.6 us: 1.01x slower                                                                 |
| json                     | 5.33 ms                                                                     | 5.39 ms: 1.01x slower                                                                 |
| regex_compile            | 138 ms                                                                      | 140 ms: 1.01x slower                                                                  |
| regex_v8                 | 24.6 ms                                                                     | 24.9 ms: 1.01x slower                                                                 |
| sqlglot_normalize        | 118 ms                                                                      | 119 ms: 1.01x slower                                                                  |
| create_gc_cycles         | 2.03 ms                                                                     | 2.06 ms: 1.02x slower                                                                 |
| typing_runtime_protocols | 172 us                                                                      | 175 us: 1.02x slower                                                                  |
| pickle_list              | 4.49 us                                                                     | 4.57 us: 1.02x slower                                                                 |
| coroutines               | 21.0 ms                                                                     | 21.5 ms: 1.02x slower                                                                 |
| crypto_pyaes             | 71.4 ms                                                                     | 73.1 ms: 1.02x slower                                                                 |
| scimark_monte_carlo      | 64.5 ms                                                                     | 66.4 ms: 1.03x slower                                                                 |
| async_generators         | 360 ms                                                                      | 371 ms: 1.03x slower                                                                  |
| unpickle_list            | 4.54 us                                                                     | 4.69 us: 1.03x slower                                                                 |
| nbody                    | 86.8 ms                                                                     | 89.8 ms: 1.03x slower                                                                 |
| django_template          | 41.0 ms                                                                     | 42.7 ms: 1.04x slower                                                                 |
| regex_dna                | 230 ms                                                                      | 242 ms: 1.05x slower                                                                  |
| unpickle                 | 14.7 us                                                                     | 15.7 us: 1.07x slower                                                                 |
| gc_traversal             | 4.42 ms                                                                     | 4.74 ms: 1.07x slower                                                                 |
| Geometric mean           | (ref)                                                                       | 1.00x slower                                                                          |

Benchmark hidden because not significant (31): raytrace, pyflate, tornado_http, pylint, logging_simple, pprint_pformat, scimark_lu, json_dumps, tomli_loads, sympy_expand, fannkuch, 2to3, pickle_pure_python, async_tree_none_tg, async_tree_io, asyncio_tcp_ssl, dulwich_log, logging_silent, xml_etree_process, docutils, xml_etree_parse, async_tree_memoization_tg, asyncio_websockets, async_tree_memoization, coverage, async_tree_none, deepcopy_reduce, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, genshi_xml, bench_mp_pool

# HPT report

- Reliability score: 86.88% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x