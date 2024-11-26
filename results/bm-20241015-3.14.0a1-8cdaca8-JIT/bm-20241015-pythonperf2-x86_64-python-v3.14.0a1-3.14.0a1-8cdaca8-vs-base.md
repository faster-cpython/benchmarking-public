# Results vs. base

- fork: python
- ref: v3.14.0a1
- machine: linux-x86_64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.028x slower
- HPT reliability: 99.87%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json | results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json |
|----------------|:----------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------:|
| 2to3           | 282 ms                                                                                                     | 314 ms: 1.11x slower                                                                                           |
| docutils       | 2.90 sec                                                                                                   | 3.17 sec: 1.09x slower                                                                                         |
| html5lib       | 71.1 ms                                                                                                    | 69.2 ms: 1.03x faster                                                                                          |
| sphinx         | 1.12 sec                                                                                                   | 1.26 sec: 1.12x slower                                                                                         |
| tornado_http   | 117 ms                                                                                                     | 123 ms: 1.06x slower                                                                                           |
| Geometric mean | (ref)                                                                                                      | 1.07x slower                                                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json | results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json |
|---------------------------|:----------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 386 ms                                                                                                     | 373 ms: 1.03x faster                                                                                           |
| asyncio_websockets        | 385 ms                                                                                                     | 381 ms: 1.01x faster                                                                                           |
| asyncio_tcp_ssl           | 1.58 sec                                                                                                   | 1.58 sec: 1.00x slower                                                                                         |
| asyncio_tcp               | 371 ms                                                                                                     | 377 ms: 1.01x slower                                                                                           |
| async_tree_io             | 827 ms                                                                                                     | 846 ms: 1.02x slower                                                                                           |
| coroutines                | 21.1 ms                                                                                                    | 21.6 ms: 1.03x slower                                                                                          |
| async_tree_cpu_io_mixed   | 558 ms                                                                                                     | 574 ms: 1.03x slower                                                                                           |
| async_tree_io_tg          | 837 ms                                                                                                     | 865 ms: 1.03x slower                                                                                           |
| async_generators          | 364 ms                                                                                                     | 379 ms: 1.04x slower                                                                                           |
| Geometric mean            | (ref)                                                                                                      | 1.01x slower                                                                                                   |

Benchmark hidden because not significant (4): async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json | results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json |
|----------------|:----------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------:|
| nbody          | 90.1 ms                                                                                                    | 83.7 ms: 1.08x faster                                                                                          |
| float          | 82.2 ms                                                                                                    | 79.3 ms: 1.04x faster                                                                                          |
| pidigits       | 252 ms                                                                                                     | 251 ms: 1.00x faster                                                                                           |
| Geometric mean | (ref)                                                                                                      | 1.04x faster                                                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json | results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json |
|----------------|:----------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 243 ms                                                                                                     | 233 ms: 1.04x faster                                                                                           |
| regex_v8       | 24.7 ms                                                                                                    | 25.0 ms: 1.01x slower                                                                                          |
| regex_effbot   | 3.43 ms                                                                                                    | 3.57 ms: 1.04x slower                                                                                          |
| regex_compile  | 139 ms                                                                                                     | 150 ms: 1.08x slower                                                                                           |
| Geometric mean | (ref)                                                                                                      | 1.02x slower                                                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json | results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json |
|----------------------|:----------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 2.50 sec                                                                                                   | 2.12 sec: 1.18x faster                                                                                         |
| xml_etree_generate   | 85.2 ms                                                                                                    | 80.6 ms: 1.06x faster                                                                                          |
| xml_etree_process    | 60.0 ms                                                                                                    | 57.7 ms: 1.04x faster                                                                                          |
| json_loads           | 25.3 us                                                                                                    | 24.6 us: 1.03x faster                                                                                          |
| unpickle             | 15.2 us                                                                                                    | 14.9 us: 1.02x faster                                                                                          |
| xml_etree_iterparse  | 102 ms                                                                                                     | 99.5 ms: 1.02x faster                                                                                          |
| json_dumps           | 11.4 ms                                                                                                    | 11.2 ms: 1.02x faster                                                                                          |
| unpickle_list        | 4.58 us                                                                                                    | 4.67 us: 1.02x slower                                                                                          |
| pickle               | 10.5 us                                                                                                    | 10.7 us: 1.02x slower                                                                                          |
| unpickle_pure_python | 214 us                                                                                                     | 221 us: 1.03x slower                                                                                           |
| pickle_pure_python   | 320 us                                                                                                     | 333 us: 1.04x slower                                                                                           |
| pickle_dict          | 31.0 us                                                                                                    | 32.9 us: 1.06x slower                                                                                          |
| pickle_list          | 4.31 us                                                                                                    | 4.66 us: 1.08x slower                                                                                          |
| Geometric mean       | (ref)                                                                                                      | 1.01x faster                                                                                                   |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json | results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json |
|------------------------|:----------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------:|
| python_startup         | 15.0 ms                                                                                                    | 14.9 ms: 1.00x faster                                                                                          |
| python_startup_no_site | 8.96 ms                                                                                                    | 9.01 ms: 1.01x slower                                                                                          |
| Geometric mean         | (ref)                                                                                                      | 1.00x slower                                                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json | results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json |
|-----------------|:----------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------:|
| mako            | 10.7 ms                                                                                                    | 9.52 ms: 1.13x faster                                                                                          |
| django_template | 41.0 ms                                                                                                    | 42.9 ms: 1.04x slower                                                                                          |
| genshi_text     | 25.0 ms                                                                                                    | 28.0 ms: 1.12x slower                                                                                          |
| genshi_xml      | 54.4 ms                                                                                                    | 62.1 ms: 1.14x slower                                                                                          |
| Geometric mean  | (ref)                                                                                                      | 1.04x slower                                                                                                   |

All benchmarks:
===============

| Benchmark                 | results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json | results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json |
|---------------------------|:----------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------:|
| tomli_loads               | 2.50 sec                                                                                                   | 2.12 sec: 1.18x faster                                                                                         |
| mako                      | 10.7 ms                                                                                                    | 9.52 ms: 1.13x faster                                                                                          |
| nbody                     | 90.1 ms                                                                                                    | 83.7 ms: 1.08x faster                                                                                          |
| scimark_sor               | 111 ms                                                                                                     | 103 ms: 1.08x faster                                                                                           |
| richards                  | 49.5 ms                                                                                                    | 46.6 ms: 1.06x faster                                                                                          |
| xml_etree_generate        | 85.2 ms                                                                                                    | 80.6 ms: 1.06x faster                                                                                          |
| telco                     | 8.23 ms                                                                                                    | 7.80 ms: 1.05x faster                                                                                          |
| dulwich_log               | 67.5 ms                                                                                                    | 64.5 ms: 1.05x faster                                                                                          |
| regex_dna                 | 243 ms                                                                                                     | 233 ms: 1.04x faster                                                                                           |
| logging_silent            | 98.0 ns                                                                                                    | 93.9 ns: 1.04x faster                                                                                          |
| deltablue                 | 3.44 ms                                                                                                    | 3.30 ms: 1.04x faster                                                                                          |
| coverage                  | 82.6 ms                                                                                                    | 79.2 ms: 1.04x faster                                                                                          |
| xml_etree_process         | 60.0 ms                                                                                                    | 57.7 ms: 1.04x faster                                                                                          |
| richards_super            | 55.6 ms                                                                                                    | 53.6 ms: 1.04x faster                                                                                          |
| float                     | 82.2 ms                                                                                                    | 79.3 ms: 1.04x faster                                                                                          |
| async_tree_memoization_tg | 386 ms                                                                                                     | 373 ms: 1.03x faster                                                                                           |
| spectral_norm             | 96.0 ms                                                                                                    | 93.0 ms: 1.03x faster                                                                                          |
| html5lib                  | 71.1 ms                                                                                                    | 69.2 ms: 1.03x faster                                                                                          |
| json_loads                | 25.3 us                                                                                                    | 24.6 us: 1.03x faster                                                                                          |
| bpe_tokeniser             | 4.86 sec                                                                                                   | 4.74 sec: 1.02x faster                                                                                         |
| unpickle                  | 15.2 us                                                                                                    | 14.9 us: 1.02x faster                                                                                          |
| create_gc_cycles          | 2.97 ms                                                                                                    | 2.90 ms: 1.02x faster                                                                                          |
| gc_traversal              | 5.32 ms                                                                                                    | 5.21 ms: 1.02x faster                                                                                          |
| xml_etree_iterparse       | 102 ms                                                                                                     | 99.5 ms: 1.02x faster                                                                                          |
| json_dumps                | 11.4 ms                                                                                                    | 11.2 ms: 1.02x faster                                                                                          |
| crypto_pyaes              | 73.4 ms                                                                                                    | 72.2 ms: 1.02x faster                                                                                          |
| json                      | 5.16 ms                                                                                                    | 5.08 ms: 1.02x faster                                                                                          |
| asyncio_websockets        | 385 ms                                                                                                     | 381 ms: 1.01x faster                                                                                           |
| pprint_safe_repr          | 803 ms                                                                                                     | 798 ms: 1.01x faster                                                                                           |
| pidigits                  | 252 ms                                                                                                     | 251 ms: 1.00x faster                                                                                           |
| python_startup            | 15.0 ms                                                                                                    | 14.9 ms: 1.00x faster                                                                                          |
| asyncio_tcp_ssl           | 1.58 sec                                                                                                   | 1.58 sec: 1.00x slower                                                                                         |
| python_startup_no_site    | 8.96 ms                                                                                                    | 9.01 ms: 1.01x slower                                                                                          |
| pyflate                   | 469 ms                                                                                                     | 473 ms: 1.01x slower                                                                                           |
| logging_simple            | 6.57 us                                                                                                    | 6.62 us: 1.01x slower                                                                                          |
| pprint_pformat            | 1.63 sec                                                                                                   | 1.64 sec: 1.01x slower                                                                                         |
| logging_format            | 7.14 us                                                                                                    | 7.21 us: 1.01x slower                                                                                          |
| regex_v8                  | 24.7 ms                                                                                                    | 25.0 ms: 1.01x slower                                                                                          |
| scimark_fft               | 286 ms                                                                                                     | 290 ms: 1.01x slower                                                                                           |
| asyncio_tcp               | 371 ms                                                                                                     | 377 ms: 1.01x slower                                                                                           |
| scimark_lu                | 94.2 ms                                                                                                    | 95.5 ms: 1.01x slower                                                                                          |
| deepcopy_memo             | 29.4 us                                                                                                    | 29.9 us: 1.02x slower                                                                                          |
| fannkuch                  | 354 ms                                                                                                     | 361 ms: 1.02x slower                                                                                           |
| unpickle_list             | 4.58 us                                                                                                    | 4.67 us: 1.02x slower                                                                                          |
| pickle                    | 10.5 us                                                                                                    | 10.7 us: 1.02x slower                                                                                          |
| async_tree_io             | 827 ms                                                                                                     | 846 ms: 1.02x slower                                                                                           |
| thrift                    | 873 us                                                                                                     | 894 us: 1.02x slower                                                                                           |
| coroutines                | 21.1 ms                                                                                                    | 21.6 ms: 1.03x slower                                                                                          |
| async_tree_cpu_io_mixed   | 558 ms                                                                                                     | 574 ms: 1.03x slower                                                                                           |
| unpickle_pure_python      | 214 us                                                                                                     | 221 us: 1.03x slower                                                                                           |
| async_tree_io_tg          | 837 ms                                                                                                     | 865 ms: 1.03x slower                                                                                           |
| mdp                       | 2.51 sec                                                                                                   | 2.59 sec: 1.03x slower                                                                                         |
| pycparser                 | 1.25 sec                                                                                                   | 1.29 sec: 1.04x slower                                                                                         |
| pickle_pure_python        | 320 us                                                                                                     | 333 us: 1.04x slower                                                                                           |
| typing_runtime_protocols  | 173 us                                                                                                     | 180 us: 1.04x slower                                                                                           |
| regex_effbot              | 3.43 ms                                                                                                    | 3.57 ms: 1.04x slower                                                                                          |
| async_generators          | 364 ms                                                                                                     | 379 ms: 1.04x slower                                                                                           |
| django_template           | 41.0 ms                                                                                                    | 42.9 ms: 1.04x slower                                                                                          |
| scimark_monte_carlo       | 65.4 ms                                                                                                    | 68.4 ms: 1.05x slower                                                                                          |
| bench_thread_pool         | 908 us                                                                                                     | 950 us: 1.05x slower                                                                                           |
| deepcopy_reduce           | 2.96 us                                                                                                    | 3.10 us: 1.05x slower                                                                                          |
| scimark_sparse_mat_mult   | 4.06 ms                                                                                                    | 4.26 ms: 1.05x slower                                                                                          |
| tornado_http              | 117 ms                                                                                                     | 123 ms: 1.06x slower                                                                                           |
| pickle_dict               | 31.0 us                                                                                                    | 32.9 us: 1.06x slower                                                                                          |
| sympy_expand              | 498 ms                                                                                                     | 530 ms: 1.06x slower                                                                                           |
| meteor_contest            | 125 ms                                                                                                     | 133 ms: 1.06x slower                                                                                           |
| deepcopy                  | 289 us                                                                                                     | 309 us: 1.07x slower                                                                                           |
| sqlglot_parse             | 1.39 ms                                                                                                    | 1.50 ms: 1.08x slower                                                                                          |
| comprehensions            | 17.4 us                                                                                                    | 18.8 us: 1.08x slower                                                                                          |
| pickle_list               | 4.31 us                                                                                                    | 4.66 us: 1.08x slower                                                                                          |
| regex_compile             | 139 ms                                                                                                     | 150 ms: 1.08x slower                                                                                           |
| sympy_str                 | 293 ms                                                                                                     | 319 ms: 1.09x slower                                                                                           |
| docutils                  | 2.90 sec                                                                                                   | 3.17 sec: 1.09x slower                                                                                         |
| chaos                     | 60.7 ms                                                                                                    | 66.5 ms: 1.10x slower                                                                                          |
| 2to3                      | 282 ms                                                                                                     | 314 ms: 1.11x slower                                                                                           |
| sqlglot_transpile         | 1.77 ms                                                                                                    | 1.98 ms: 1.12x slower                                                                                          |
| sqlglot_normalize         | 118 ms                                                                                                     | 132 ms: 1.12x slower                                                                                           |
| genshi_text               | 25.0 ms                                                                                                    | 28.0 ms: 1.12x slower                                                                                          |
| sphinx                    | 1.12 sec                                                                                                   | 1.26 sec: 1.12x slower                                                                                         |
| sympy_sum                 | 153 ms                                                                                                     | 173 ms: 1.13x slower                                                                                           |
| hexiom                    | 6.24 ms                                                                                                    | 7.11 ms: 1.14x slower                                                                                          |
| genshi_xml                | 54.4 ms                                                                                                    | 62.1 ms: 1.14x slower                                                                                          |
| go                        | 133 ms                                                                                                     | 152 ms: 1.15x slower                                                                                           |
| sympy_integrate           | 23.4 ms                                                                                                    | 27.3 ms: 1.17x slower                                                                                          |
| raytrace                  | 270 ms                                                                                                     | 315 ms: 1.17x slower                                                                                           |
| nqueens                   | 88.0 ms                                                                                                    | 104 ms: 1.18x slower                                                                                           |
| sqlglot_optimize          | 59.1 ms                                                                                                    | 69.7 ms: 1.18x slower                                                                                          |
| pylint                    | 345 ms                                                                                                     | 423 ms: 1.23x slower                                                                                           |
| generators                | 29.3 ms                                                                                                    | 39.4 ms: 1.34x slower                                                                                          |
| unpack_sequence           | 58.9 ns                                                                                                    | 89.6 ns: 1.52x slower                                                                                          |
| Geometric mean            | (ref)                                                                                                      | 1.03x slower                                                                                                   |

Benchmark hidden because not significant (8): async_tree_memoization, async_tree_cpu_io_mixed_tg, sqlite_synth, async_tree_none_tg, pathlib, async_tree_none, xml_etree_parse, bench_mp_pool

- Geometric mean (including insignificant results): 1.028x slower
# HPT report

- Reliability score: 99.87% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.06x