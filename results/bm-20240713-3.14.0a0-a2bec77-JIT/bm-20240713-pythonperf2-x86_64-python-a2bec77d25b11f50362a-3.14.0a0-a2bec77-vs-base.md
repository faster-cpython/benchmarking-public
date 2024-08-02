# Results vs. base

- fork: python
- ref: a2bec77d25b11f50362a
- machine: linux-x86_64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.01x slower
- HPT reliability: 96.97%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 289 ms                                                                                                                | 306 ms: 1.06x slower                                                                                                      |
| docutils       | 2.96 sec                                                                                                              | 3.10 sec: 1.05x slower                                                                                                    |
| html5lib       | 74.0 ms                                                                                                               | 70.8 ms: 1.04x faster                                                                                                     |
| tornado_http   | 117 ms                                                                                                                | 121 ms: 1.04x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                 | 1.03x slower                                                                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|---------------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 383 ms                                                                                                                | 390 ms: 1.02x slower                                                                                                      |
| async_tree_memoization    | 403 ms                                                                                                                | 414 ms: 1.03x slower                                                                                                      |
| async_tree_io_tg          | 776 ms                                                                                                                | 805 ms: 1.04x slower                                                                                                      |
| Geometric mean            | (ref)                                                                                                                 | 1.02x slower                                                                                                              |

Benchmark hidden because not significant (5): async_tree_cpu_io_mixed, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| float          | 80.6 ms                                                                                                               | 75.1 ms: 1.07x faster                                                                                                     |
| nbody          | 88.3 ms                                                                                                               | 82.6 ms: 1.07x faster                                                                                                     |
| pidigits       | 253 ms                                                                                                                | 251 ms: 1.01x faster                                                                                                      |
| Geometric mean | (ref)                                                                                                                 | 1.05x faster                                                                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                                                                               | 25.6 ms: 1.02x faster                                                                                                     |
| regex_dna      | 240 ms                                                                                                                | 235 ms: 1.02x faster                                                                                                      |
| regex_compile  | 140 ms                                                                                                                | 138 ms: 1.01x faster                                                                                                      |
| Geometric mean | (ref)                                                                                                                 | 1.02x faster                                                                                                              |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark           | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|---------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads         | 2.25 sec                                                                                                              | 2.09 sec: 1.07x faster                                                                                                    |
| pickle_pure_python  | 325 us                                                                                                                | 312 us: 1.04x faster                                                                                                      |
| xml_etree_iterparse | 104 ms                                                                                                                | 99.8 ms: 1.04x faster                                                                                                     |
| xml_etree_generate  | 84.6 ms                                                                                                               | 82.5 ms: 1.03x faster                                                                                                     |
| xml_etree_process   | 59.2 ms                                                                                                               | 58.0 ms: 1.02x faster                                                                                                     |
| xml_etree_parse     | 146 ms                                                                                                                | 143 ms: 1.02x faster                                                                                                      |
| json_loads          | 25.4 us                                                                                                               | 25.3 us: 1.00x faster                                                                                                     |
| json_dumps          | 10.9 ms                                                                                                               | 11.0 ms: 1.01x slower                                                                                                     |
| Geometric mean      | (ref)                                                                                                                 | 1.02x faster                                                                                                              |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                                                                               | 13.4 ms: 1.00x slower                                                                                                     |
| python_startup_no_site | 9.01 ms                                                                                                               | 9.06 ms: 1.01x slower                                                                                                     |
| Geometric mean         | (ref)                                                                                                                 | 1.00x slower                                                                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| mako            | 10.5 ms                                                                                                               | 9.22 ms: 1.14x faster                                                                                                     |
| django_template | 38.3 ms                                                                                                               | 43.3 ms: 1.13x slower                                                                                                     |
| genshi_text     | 25.0 ms                                                                                                               | 28.7 ms: 1.15x slower                                                                                                     |
| genshi_xml      | 54.6 ms                                                                                                               | 64.7 ms: 1.19x slower                                                                                                     |
| Geometric mean  | (ref)                                                                                                                 | 1.08x slower                                                                                                              |

All benchmarks:
===============

| Benchmark                 | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|---------------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| spectral_norm             | 95.8 ms                                                                                                               | 82.5 ms: 1.16x faster                                                                                                     |
| richards                  | 51.5 ms                                                                                                               | 44.9 ms: 1.15x faster                                                                                                     |
| mako                      | 10.5 ms                                                                                                               | 9.22 ms: 1.14x faster                                                                                                     |
| richards_super            | 58.5 ms                                                                                                               | 53.0 ms: 1.10x faster                                                                                                     |
| pyflate                   | 490 ms                                                                                                                | 445 ms: 1.10x faster                                                                                                      |
| scimark_fft               | 315 ms                                                                                                                | 293 ms: 1.08x faster                                                                                                      |
| tomli_loads               | 2.25 sec                                                                                                              | 2.09 sec: 1.07x faster                                                                                                    |
| deepcopy_memo             | 29.8 us                                                                                                               | 27.7 us: 1.07x faster                                                                                                     |
| float                     | 80.6 ms                                                                                                               | 75.1 ms: 1.07x faster                                                                                                     |
| scimark_sparse_mat_mult   | 4.38 ms                                                                                                               | 4.09 ms: 1.07x faster                                                                                                     |
| nbody                     | 88.3 ms                                                                                                               | 82.6 ms: 1.07x faster                                                                                                     |
| fannkuch                  | 368 ms                                                                                                                | 346 ms: 1.06x faster                                                                                                      |
| scimark_monte_carlo       | 67.5 ms                                                                                                               | 64.2 ms: 1.05x faster                                                                                                     |
| html5lib                  | 74.0 ms                                                                                                               | 70.8 ms: 1.04x faster                                                                                                     |
| pickle_pure_python        | 325 us                                                                                                                | 312 us: 1.04x faster                                                                                                      |
| xml_etree_iterparse       | 104 ms                                                                                                                | 99.8 ms: 1.04x faster                                                                                                     |
| create_gc_cycles          | 1.99 ms                                                                                                               | 1.93 ms: 1.04x faster                                                                                                     |
| xml_etree_generate        | 84.6 ms                                                                                                               | 82.5 ms: 1.03x faster                                                                                                     |
| pprint_pformat            | 1.66 sec                                                                                                              | 1.62 sec: 1.02x faster                                                                                                    |
| regex_v8                  | 26.2 ms                                                                                                               | 25.6 ms: 1.02x faster                                                                                                     |
| regex_dna                 | 240 ms                                                                                                                | 235 ms: 1.02x faster                                                                                                      |
| xml_etree_process         | 59.2 ms                                                                                                               | 58.0 ms: 1.02x faster                                                                                                     |
| xml_etree_parse           | 146 ms                                                                                                                | 143 ms: 1.02x faster                                                                                                      |
| crypto_pyaes              | 71.7 ms                                                                                                               | 70.3 ms: 1.02x faster                                                                                                     |
| pprint_safe_repr          | 812 ms                                                                                                                | 796 ms: 1.02x faster                                                                                                      |
| dulwich_log               | 66.2 ms                                                                                                               | 65.3 ms: 1.01x faster                                                                                                     |
| regex_compile             | 140 ms                                                                                                                | 138 ms: 1.01x faster                                                                                                      |
| go                        | 166 ms                                                                                                                | 164 ms: 1.01x faster                                                                                                      |
| coroutines                | 21.2 ms                                                                                                               | 21.0 ms: 1.01x faster                                                                                                     |
| pidigits                  | 253 ms                                                                                                                | 251 ms: 1.01x faster                                                                                                      |
| gc_traversal              | 4.46 ms                                                                                                               | 4.44 ms: 1.01x faster                                                                                                     |
| json_loads                | 25.4 us                                                                                                               | 25.3 us: 1.00x faster                                                                                                     |
| python_startup            | 13.3 ms                                                                                                               | 13.4 ms: 1.00x slower                                                                                                     |
| asyncio_tcp_ssl           | 1.58 sec                                                                                                              | 1.58 sec: 1.00x slower                                                                                                    |
| python_startup_no_site    | 9.01 ms                                                                                                               | 9.06 ms: 1.01x slower                                                                                                     |
| pathlib                   | 16.2 ms                                                                                                               | 16.3 ms: 1.01x slower                                                                                                     |
| telco                     | 8.25 ms                                                                                                               | 8.34 ms: 1.01x slower                                                                                                     |
| logging_simple            | 6.39 us                                                                                                               | 6.47 us: 1.01x slower                                                                                                     |
| json_dumps                | 10.9 ms                                                                                                               | 11.0 ms: 1.01x slower                                                                                                     |
| json                      | 5.47 ms                                                                                                               | 5.54 ms: 1.01x slower                                                                                                     |
| bpe_tokeniser             | 5.05 sec                                                                                                              | 5.12 sec: 1.01x slower                                                                                                    |
| asyncio_tcp               | 374 ms                                                                                                                | 380 ms: 1.02x slower                                                                                                      |
| mdp                       | 2.49 sec                                                                                                              | 2.53 sec: 1.02x slower                                                                                                    |
| async_tree_memoization_tg | 383 ms                                                                                                                | 390 ms: 1.02x slower                                                                                                      |
| sqlglot_transpile         | 1.78 ms                                                                                                               | 1.81 ms: 1.02x slower                                                                                                     |
| coverage                  | 78.4 ms                                                                                                               | 80.2 ms: 1.02x slower                                                                                                     |
| async_tree_memoization    | 403 ms                                                                                                                | 414 ms: 1.03x slower                                                                                                      |
| logging_format            | 7.05 us                                                                                                               | 7.25 us: 1.03x slower                                                                                                     |
| thrift                    | 882 us                                                                                                                | 908 us: 1.03x slower                                                                                                      |
| logging_silent            | 98.8 ns                                                                                                               | 102 ns: 1.04x slower                                                                                                      |
| async_tree_io_tg          | 776 ms                                                                                                                | 805 ms: 1.04x slower                                                                                                      |
| dask                      | 386 ms                                                                                                                | 400 ms: 1.04x slower                                                                                                      |
| tornado_http              | 117 ms                                                                                                                | 121 ms: 1.04x slower                                                                                                      |
| meteor_contest            | 126 ms                                                                                                                | 131 ms: 1.04x slower                                                                                                      |
| deepcopy_reduce           | 2.93 us                                                                                                               | 3.05 us: 1.04x slower                                                                                                     |
| deltablue                 | 3.50 ms                                                                                                               | 3.66 ms: 1.05x slower                                                                                                     |
| docutils                  | 2.96 sec                                                                                                              | 3.10 sec: 1.05x slower                                                                                                    |
| sympy_expand              | 496 ms                                                                                                                | 521 ms: 1.05x slower                                                                                                      |
| async_generators          | 367 ms                                                                                                                | 386 ms: 1.05x slower                                                                                                      |
| sympy_str                 | 292 ms                                                                                                                | 308 ms: 1.05x slower                                                                                                      |
| generators                | 33.5 ms                                                                                                               | 35.3 ms: 1.05x slower                                                                                                     |
| 2to3                      | 289 ms                                                                                                                | 306 ms: 1.06x slower                                                                                                      |
| hexiom                    | 6.27 ms                                                                                                               | 6.66 ms: 1.06x slower                                                                                                     |
| bench_thread_pool         | 873 us                                                                                                                | 929 us: 1.06x slower                                                                                                      |
| comprehensions            | 17.1 us                                                                                                               | 18.3 us: 1.07x slower                                                                                                     |
| sympy_sum                 | 153 ms                                                                                                                | 164 ms: 1.07x slower                                                                                                      |
| sqlglot_optimize          | 58.9 ms                                                                                                               | 63.2 ms: 1.07x slower                                                                                                     |
| chaos                     | 61.4 ms                                                                                                               | 66.0 ms: 1.07x slower                                                                                                     |
| deepcopy                  | 284 us                                                                                                                | 305 us: 1.07x slower                                                                                                      |
| nqueens                   | 87.7 ms                                                                                                               | 94.8 ms: 1.08x slower                                                                                                     |
| sqlglot_normalize         | 118 ms                                                                                                                | 130 ms: 1.10x slower                                                                                                      |
| typing_runtime_protocols  | 171 us                                                                                                                | 189 us: 1.11x slower                                                                                                      |
| pylint                    | 335 ms                                                                                                                | 372 ms: 1.11x slower                                                                                                      |
| sympy_integrate           | 23.0 ms                                                                                                               | 25.5 ms: 1.11x slower                                                                                                     |
| raytrace                  | 269 ms                                                                                                                | 298 ms: 1.11x slower                                                                                                      |
| django_template           | 38.3 ms                                                                                                               | 43.3 ms: 1.13x slower                                                                                                     |
| genshi_text               | 25.0 ms                                                                                                               | 28.7 ms: 1.15x slower                                                                                                     |
| scimark_lu                | 98.4 ms                                                                                                               | 114 ms: 1.16x slower                                                                                                      |
| genshi_xml                | 54.6 ms                                                                                                               | 64.7 ms: 1.19x slower                                                                                                     |
| Geometric mean            | (ref)                                                                                                                 | 1.01x slower                                                                                                              |

Benchmark hidden because not significant (12): bench_mp_pool, pycparser, regex_effbot, sqlglot_parse, scimark_sor, asyncio_websockets, unpickle_pure_python, async_tree_cpu_io_mixed, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_none

# HPT report

- Reliability score: 96.97% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.06x