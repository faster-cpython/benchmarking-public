# Results vs. base

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: linux-aarch64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.113x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json | results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 294 ms                                                                                                            | 382 ms: 1.30x slower                                                                                                  |
| docutils       | 3.04 sec                                                                                                          | 3.93 sec: 1.29x slower                                                                                                |
| html5lib       | 63.7 ms                                                                                                           | 70.5 ms: 1.11x slower                                                                                                 |
| tornado_http   | 129 ms                                                                                                            | 151 ms: 1.17x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.21x slower                                                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json | results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json |
|---------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| async_tree_memoization    | 559 ms                                                                                                            | 571 ms: 1.02x slower                                                                                                  |
| async_tree_cpu_io_mixed   | 726 ms                                                                                                            | 743 ms: 1.02x slower                                                                                                  |
| async_tree_memoization_tg | 544 ms                                                                                                            | 558 ms: 1.03x slower                                                                                                  |
| async_tree_none_tg        | 416 ms                                                                                                            | 430 ms: 1.03x slower                                                                                                  |
| asyncio_tcp_ssl           | 2.16 sec                                                                                                          | 2.29 sec: 1.06x slower                                                                                                |
| async_tree_io             | 1.12 sec                                                                                                          | 1.19 sec: 1.06x slower                                                                                                |
| async_generators          | 474 ms                                                                                                            | 507 ms: 1.07x slower                                                                                                  |
| async_tree_none           | 422 ms                                                                                                            | 451 ms: 1.07x slower                                                                                                  |
| asyncio_tcp               | 551 ms                                                                                                            | 635 ms: 1.15x slower                                                                                                  |
| Geometric mean            | (ref)                                                                                                             | 1.04x slower                                                                                                          |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed_tg, async_tree_io_tg, coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json | results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| float          | 92.7 ms                                                                                                           | 88.0 ms: 1.05x faster                                                                                                 |
| nbody          | 109 ms                                                                                                            | 116 ms: 1.06x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.00x slower                                                                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json | results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                                                            | 246 ms: 1.03x faster                                                                                                  |
| regex_compile  | 126 ms                                                                                                            | 194 ms: 1.54x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.10x slower                                                                                                          |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json | results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 2.62 sec                                                                                                          | 2.64 sec: 1.01x slower                                                                                                |
| json_dumps           | 13.4 ms                                                                                                           | 13.5 ms: 1.01x slower                                                                                                 |
| unpickle_pure_python | 254 us                                                                                                            | 266 us: 1.05x slower                                                                                                  |
| xml_etree_parse      | 186 ms                                                                                                            | 198 ms: 1.06x slower                                                                                                  |
| pickle_pure_python   | 356 us                                                                                                            | 382 us: 1.07x slower                                                                                                  |
| Geometric mean       | (ref)                                                                                                             | 1.02x slower                                                                                                          |

Benchmark hidden because not significant (4): xml_etree_iterparse, xml_etree_process, json_loads, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json | results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.77 ms                                                                                                           | 8.96 ms: 1.02x slower                                                                                                 |
| python_startup         | 13.0 ms                                                                                                           | 13.3 ms: 1.02x slower                                                                                                 |
| Geometric mean         | (ref)                                                                                                             | 1.02x slower                                                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json | results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako            | 13.3 ms                                                                                                           | 13.1 ms: 1.01x faster                                                                                                 |
| django_template | 41.4 ms                                                                                                           | 51.0 ms: 1.23x slower                                                                                                 |
| genshi_text     | 27.5 ms                                                                                                           | 34.4 ms: 1.25x slower                                                                                                 |
| genshi_xml      | 60.0 ms                                                                                                           | 81.1 ms: 1.35x slower                                                                                                 |
| Geometric mean  | (ref)                                                                                                             | 1.20x slower                                                                                                          |

All benchmarks:
===============

| Benchmark                 | results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json | results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json |
|---------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| float                     | 92.7 ms                                                                                                           | 88.0 ms: 1.05x faster                                                                                                 |
| scimark_sor               | 157 ms                                                                                                            | 150 ms: 1.04x faster                                                                                                  |
| regex_dna                 | 254 ms                                                                                                            | 246 ms: 1.03x faster                                                                                                  |
| deepcopy_memo             | 38.2 us                                                                                                           | 37.4 us: 1.02x faster                                                                                                 |
| mako                      | 13.3 ms                                                                                                           | 13.1 ms: 1.01x faster                                                                                                 |
| tomli_loads               | 2.62 sec                                                                                                          | 2.64 sec: 1.01x slower                                                                                                |
| json_dumps                | 13.4 ms                                                                                                           | 13.5 ms: 1.01x slower                                                                                                 |
| bpe_tokeniser             | 5.87 sec                                                                                                          | 5.96 sec: 1.01x slower                                                                                                |
| thrift                    | 931 us                                                                                                            | 950 us: 1.02x slower                                                                                                  |
| async_tree_memoization    | 559 ms                                                                                                            | 571 ms: 1.02x slower                                                                                                  |
| python_startup_no_site    | 8.77 ms                                                                                                           | 8.96 ms: 1.02x slower                                                                                                 |
| async_tree_cpu_io_mixed   | 726 ms                                                                                                            | 743 ms: 1.02x slower                                                                                                  |
| python_startup            | 13.0 ms                                                                                                           | 13.3 ms: 1.02x slower                                                                                                 |
| async_tree_memoization_tg | 544 ms                                                                                                            | 558 ms: 1.03x slower                                                                                                  |
| mdp                       | 3.35 sec                                                                                                          | 3.45 sec: 1.03x slower                                                                                                |
| create_gc_cycles          | 2.29 ms                                                                                                           | 2.36 ms: 1.03x slower                                                                                                 |
| spectral_norm             | 141 ms                                                                                                            | 146 ms: 1.03x slower                                                                                                  |
| async_tree_none_tg        | 416 ms                                                                                                            | 430 ms: 1.03x slower                                                                                                  |
| pathlib                   | 21.0 ms                                                                                                           | 21.8 ms: 1.04x slower                                                                                                 |
| unpickle_pure_python      | 254 us                                                                                                            | 266 us: 1.05x slower                                                                                                  |
| logging_silent            | 131 ns                                                                                                            | 137 ns: 1.05x slower                                                                                                  |
| scimark_fft               | 439 ms                                                                                                            | 463 ms: 1.05x slower                                                                                                  |
| asyncio_tcp_ssl           | 2.16 sec                                                                                                          | 2.29 sec: 1.06x slower                                                                                                |
| async_tree_io             | 1.12 sec                                                                                                          | 1.19 sec: 1.06x slower                                                                                                |
| xml_etree_parse           | 186 ms                                                                                                            | 198 ms: 1.06x slower                                                                                                  |
| telco                     | 9.76 ms                                                                                                           | 10.4 ms: 1.06x slower                                                                                                 |
| logging_format            | 7.64 us                                                                                                           | 8.13 us: 1.06x slower                                                                                                 |
| scimark_sparse_mat_mult   | 6.40 ms                                                                                                           | 6.81 ms: 1.06x slower                                                                                                 |
| nbody                     | 109 ms                                                                                                            | 116 ms: 1.06x slower                                                                                                  |
| async_generators          | 474 ms                                                                                                            | 507 ms: 1.07x slower                                                                                                  |
| async_tree_none           | 422 ms                                                                                                            | 451 ms: 1.07x slower                                                                                                  |
| typing_runtime_protocols  | 193 us                                                                                                            | 207 us: 1.07x slower                                                                                                  |
| logging_simple            | 6.91 us                                                                                                           | 7.41 us: 1.07x slower                                                                                                 |
| pickle_pure_python        | 356 us                                                                                                            | 382 us: 1.07x slower                                                                                                  |
| crypto_pyaes              | 83.3 ms                                                                                                           | 89.4 ms: 1.07x slower                                                                                                 |
| bench_thread_pool         | 1.24 ms                                                                                                           | 1.33 ms: 1.08x slower                                                                                                 |
| bench_mp_pool             | 7.00 ms                                                                                                           | 7.59 ms: 1.08x slower                                                                                                 |
| deepcopy_reduce           | 3.51 us                                                                                                           | 3.83 us: 1.09x slower                                                                                                 |
| fannkuch                  | 465 ms                                                                                                            | 511 ms: 1.10x slower                                                                                                  |
| meteor_contest            | 112 ms                                                                                                            | 123 ms: 1.10x slower                                                                                                  |
| scimark_lu                | 135 ms                                                                                                            | 149 ms: 1.10x slower                                                                                                  |
| html5lib                  | 63.7 ms                                                                                                           | 70.5 ms: 1.11x slower                                                                                                 |
| deltablue                 | 3.92 ms                                                                                                           | 4.34 ms: 1.11x slower                                                                                                 |
| pyflate                   | 567 ms                                                                                                            | 630 ms: 1.11x slower                                                                                                  |
| scimark_monte_carlo       | 82.5 ms                                                                                                           | 92.2 ms: 1.12x slower                                                                                                 |
| asyncio_tcp               | 551 ms                                                                                                            | 635 ms: 1.15x slower                                                                                                  |
| tornado_http              | 129 ms                                                                                                            | 151 ms: 1.17x slower                                                                                                  |
| raytrace                  | 301 ms                                                                                                            | 353 ms: 1.17x slower                                                                                                  |
| deepcopy                  | 337 us                                                                                                            | 400 us: 1.19x slower                                                                                                  |
| sqlglot_normalize         | 127 ms                                                                                                            | 151 ms: 1.19x slower                                                                                                  |
| comprehensions            | 20.8 us                                                                                                           | 25.0 us: 1.20x slower                                                                                                 |
| django_template           | 41.4 ms                                                                                                           | 51.0 ms: 1.23x slower                                                                                                 |
| nqueens                   | 99.9 ms                                                                                                           | 125 ms: 1.25x slower                                                                                                  |
| richards                  | 54.3 ms                                                                                                           | 67.9 ms: 1.25x slower                                                                                                 |
| pycparser                 | 1.21 sec                                                                                                          | 1.52 sec: 1.25x slower                                                                                                |
| genshi_text               | 27.5 ms                                                                                                           | 34.4 ms: 1.25x slower                                                                                                 |
| richards_super            | 60.7 ms                                                                                                           | 76.3 ms: 1.26x slower                                                                                                 |
| sqlglot_parse             | 1.40 ms                                                                                                           | 1.77 ms: 1.26x slower                                                                                                 |
| sqlglot_transpile         | 1.73 ms                                                                                                           | 2.19 ms: 1.26x slower                                                                                                 |
| sqlglot_optimize          | 62.5 ms                                                                                                           | 79.4 ms: 1.27x slower                                                                                                 |
| docutils                  | 3.04 sec                                                                                                          | 3.93 sec: 1.29x slower                                                                                                |
| 2to3                      | 294 ms                                                                                                            | 382 ms: 1.30x slower                                                                                                  |
| chaos                     | 68.6 ms                                                                                                           | 91.5 ms: 1.34x slower                                                                                                 |
| sympy_expand              | 462 ms                                                                                                            | 619 ms: 1.34x slower                                                                                                  |
| genshi_xml                | 60.0 ms                                                                                                           | 81.1 ms: 1.35x slower                                                                                                 |
| pylint                    | 359 ms                                                                                                            | 489 ms: 1.36x slower                                                                                                  |
| go                        | 138 ms                                                                                                            | 188 ms: 1.37x slower                                                                                                  |
| sympy_str                 | 264 ms                                                                                                            | 364 ms: 1.38x slower                                                                                                  |
| pprint_pformat            | 1.90 sec                                                                                                          | 2.64 sec: 1.39x slower                                                                                                |
| pprint_safe_repr          | 915 ms                                                                                                            | 1.28 sec: 1.40x slower                                                                                                |
| sympy_integrate           | 20.6 ms                                                                                                           | 29.2 ms: 1.42x slower                                                                                                 |
| hexiom                    | 7.13 ms                                                                                                           | 10.3 ms: 1.44x slower                                                                                                 |
| dulwich_log               | 58.7 ms                                                                                                           | 85.3 ms: 1.45x slower                                                                                                 |
| sympy_sum                 | 141 ms                                                                                                            | 215 ms: 1.53x slower                                                                                                  |
| regex_compile             | 126 ms                                                                                                            | 194 ms: 1.54x slower                                                                                                  |
| generators                | 35.0 ms                                                                                                           | 56.9 ms: 1.63x slower                                                                                                 |
| Geometric mean            | (ref)                                                                                                             | 1.12x slower                                                                                                          |

Benchmark hidden because not significant (14): regex_effbot, xml_etree_iterparse, async_tree_cpu_io_mixed_tg, async_tree_io_tg, pidigits, coroutines, regex_v8, gc_traversal, xml_etree_process, json_loads, coverage, asyncio_websockets, xml_etree_generate, json

- Geometric mean (including insignificant results): 1.113x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.10x