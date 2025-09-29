# Results vs. base

- fork: python
- ref: 48d0d0dd9733eae4935f
- machine: linux-x86_64
- commit hash: 48d0d0d
- commit date: 2025-09-26
- overall geometric mean: 1.003x slower
- HPT reliability: 99.11%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250926-3.15.0a0-48d0d0d/bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json | results/bm-20250926-3.15.0a0-48d0d0d-JIT/bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 278 ms                                                                                                                | 284 ms: 1.02x slower                                                                                                      |
| docutils       | 2.85 sec                                                                                                              | 2.88 sec: 1.01x slower                                                                                                    |
| html5lib       | 64.9 ms                                                                                                               | 65.9 ms: 1.02x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                                 | 1.02x slower                                                                                                              |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | results/bm-20250926-3.15.0a0-48d0d0d/bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json | results/bm-20250926-3.15.0a0-48d0d0d-JIT/bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json |
|---------------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| asyncio_tcp_ssl           | 1.58 sec                                                                                                              | 1.59 sec: 1.00x slower                                                                                                    |
| async_tree_io             | 614 ms                                                                                                                | 619 ms: 1.01x slower                                                                                                      |
| async_tree_memoization_tg | 331 ms                                                                                                                | 334 ms: 1.01x slower                                                                                                      |
| asyncio_tcp               | 368 ms                                                                                                                | 371 ms: 1.01x slower                                                                                                      |
| async_tree_none_tg        | 271 ms                                                                                                                | 274 ms: 1.01x slower                                                                                                      |
| async_tree_none           | 271 ms                                                                                                                | 275 ms: 1.01x slower                                                                                                      |
| async_generators          | 422 ms                                                                                                                | 438 ms: 1.04x slower                                                                                                      |
| coroutines                | 21.9 ms                                                                                                               | 22.8 ms: 1.04x slower                                                                                                     |
| Geometric mean            | (ref)                                                                                                                 | 1.01x slower                                                                                                              |

Benchmark hidden because not significant (5): async_tree_cpu_io_mixed, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250926-3.15.0a0-48d0d0d/bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json | results/bm-20250926-3.15.0a0-48d0d0d-JIT/bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| pidigits       | 254 ms                                                                                                                | 254 ms: 1.00x faster                                                                                                      |
| float          | 67.3 ms                                                                                                               | 68.4 ms: 1.02x slower                                                                                                     |
| nbody          | 91.2 ms                                                                                                               | 97.7 ms: 1.07x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                                 | 1.03x slower                                                                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250926-3.15.0a0-48d0d0d/bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json | results/bm-20250926-3.15.0a0-48d0d0d-JIT/bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 23.5 ms                                                                                                               | 23.4 ms: 1.00x faster                                                                                                     |
| regex_dna      | 222 ms                                                                                                                | 231 ms: 1.04x slower                                                                                                      |
| regex_effbot   | 3.42 ms                                                                                                               | 3.67 ms: 1.07x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                                 | 1.03x slower                                                                                                              |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250926-3.15.0a0-48d0d0d/bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json | results/bm-20250926-3.15.0a0-48d0d0d-JIT/bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 206 us                                                                                                                | 193 us: 1.07x faster                                                                                                      |
| tomli_loads          | 1.98 sec                                                                                                              | 1.89 sec: 1.05x faster                                                                                                    |
| xml_etree_process    | 57.6 ms                                                                                                               | 55.3 ms: 1.04x faster                                                                                                     |
| xml_etree_parse      | 146 ms                                                                                                                | 142 ms: 1.03x faster                                                                                                      |
| xml_etree_generate   | 82.5 ms                                                                                                               | 80.0 ms: 1.03x faster                                                                                                     |
| unpickle_list        | 5.07 us                                                                                                               | 4.97 us: 1.02x faster                                                                                                     |
| xml_etree_iterparse  | 99.3 ms                                                                                                               | 97.6 ms: 1.02x faster                                                                                                     |
| pickle               | 12.5 us                                                                                                               | 12.3 us: 1.01x faster                                                                                                     |
| json_dumps           | 9.92 ms                                                                                                               | 10.0 ms: 1.01x slower                                                                                                     |
| pickle_dict          | 33.5 us                                                                                                               | 33.9 us: 1.01x slower                                                                                                     |
| json_loads           | 26.1 us                                                                                                               | 26.4 us: 1.01x slower                                                                                                     |
| unpickle             | 14.6 us                                                                                                               | 15.0 us: 1.03x slower                                                                                                     |
| pickle_list          | 4.84 us                                                                                                               | 4.98 us: 1.03x slower                                                                                                     |
| Geometric mean       | (ref)                                                                                                                 | 1.01x faster                                                                                                              |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250926-3.15.0a0-48d0d0d/bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json | results/bm-20250926-3.15.0a0-48d0d0d-JIT/bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 15.4 ms                                                                                                               | 15.5 ms: 1.00x slower                                                                                                     |
| python_startup_no_site | 8.83 ms                                                                                                               | 8.88 ms: 1.01x slower                                                                                                     |
| Geometric mean         | (ref)                                                                                                                 | 1.00x slower                                                                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250926-3.15.0a0-48d0d0d/bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json | results/bm-20250926-3.15.0a0-48d0d0d-JIT/bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| mako            | 10.8 ms                                                                                                               | 9.90 ms: 1.09x faster                                                                                                     |
| django_template | 34.6 ms                                                                                                               | 35.0 ms: 1.01x slower                                                                                                     |
| genshi_xml      | 52.4 ms                                                                                                               | 53.6 ms: 1.02x slower                                                                                                     |
| Geometric mean  | (ref)                                                                                                                 | 1.01x faster                                                                                                              |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                 | results/bm-20250926-3.15.0a0-48d0d0d/bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json | results/bm-20250926-3.15.0a0-48d0d0d-JIT/bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json |
|---------------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| richards                  | 44.6 ms                                                                                                               | 38.2 ms: 1.17x faster                                                                                                     |
| richards_super            | 50.4 ms                                                                                                               | 44.5 ms: 1.13x faster                                                                                                     |
| deepcopy_memo             | 25.3 us                                                                                                               | 23.3 us: 1.09x faster                                                                                                     |
| mako                      | 10.8 ms                                                                                                               | 9.90 ms: 1.09x faster                                                                                                     |
| unpickle_pure_python      | 206 us                                                                                                                | 193 us: 1.07x faster                                                                                                      |
| tomli_loads               | 1.98 sec                                                                                                              | 1.89 sec: 1.05x faster                                                                                                    |
| xml_etree_process         | 57.6 ms                                                                                                               | 55.3 ms: 1.04x faster                                                                                                     |
| pycparser                 | 1.23 sec                                                                                                              | 1.19 sec: 1.03x faster                                                                                                    |
| xml_etree_parse           | 146 ms                                                                                                                | 142 ms: 1.03x faster                                                                                                      |
| pyflate                   | 405 ms                                                                                                                | 392 ms: 1.03x faster                                                                                                      |
| k_core                    | 2.08 sec                                                                                                              | 2.01 sec: 1.03x faster                                                                                                    |
| xml_etree_generate        | 82.5 ms                                                                                                               | 80.0 ms: 1.03x faster                                                                                                     |
| connected_components      | 424 ms                                                                                                                | 411 ms: 1.03x faster                                                                                                      |
| unpickle_list             | 5.07 us                                                                                                               | 4.97 us: 1.02x faster                                                                                                     |
| bpe_tokeniser             | 4.65 sec                                                                                                              | 4.56 sec: 1.02x faster                                                                                                    |
| shortest_path             | 453 ms                                                                                                                | 446 ms: 1.02x faster                                                                                                      |
| xml_etree_iterparse       | 99.3 ms                                                                                                               | 97.6 ms: 1.02x faster                                                                                                     |
| pprint_safe_repr          | 743 ms                                                                                                                | 731 ms: 1.02x faster                                                                                                      |
| pprint_pformat            | 1.51 sec                                                                                                              | 1.49 sec: 1.02x faster                                                                                                    |
| scimark_fft               | 279 ms                                                                                                                | 275 ms: 1.01x faster                                                                                                      |
| pickle                    | 12.5 us                                                                                                               | 12.3 us: 1.01x faster                                                                                                     |
| crypto_pyaes              | 76.5 ms                                                                                                               | 75.8 ms: 1.01x faster                                                                                                     |
| dulwich_log               | 59.0 ms                                                                                                               | 58.6 ms: 1.01x faster                                                                                                     |
| regex_v8                  | 23.5 ms                                                                                                               | 23.4 ms: 1.00x faster                                                                                                     |
| pidigits                  | 254 ms                                                                                                                | 254 ms: 1.00x faster                                                                                                      |
| asyncio_tcp_ssl           | 1.58 sec                                                                                                              | 1.59 sec: 1.00x slower                                                                                                    |
| scimark_sor               | 101 ms                                                                                                                | 102 ms: 1.00x slower                                                                                                      |
| python_startup            | 15.4 ms                                                                                                               | 15.5 ms: 1.00x slower                                                                                                     |
| spectral_norm             | 85.9 ms                                                                                                               | 86.3 ms: 1.00x slower                                                                                                     |
| python_startup_no_site    | 8.83 ms                                                                                                               | 8.88 ms: 1.01x slower                                                                                                     |
| chaos                     | 58.8 ms                                                                                                               | 59.1 ms: 1.01x slower                                                                                                     |
| deepcopy_reduce           | 2.91 us                                                                                                               | 2.93 us: 1.01x slower                                                                                                     |
| logging_simple            | 5.86 us                                                                                                               | 5.90 us: 1.01x slower                                                                                                     |
| async_tree_io             | 614 ms                                                                                                                | 619 ms: 1.01x slower                                                                                                      |
| async_tree_memoization_tg | 331 ms                                                                                                                | 334 ms: 1.01x slower                                                                                                      |
| json_dumps                | 9.92 ms                                                                                                               | 10.0 ms: 1.01x slower                                                                                                     |
| sympy_sum                 | 150 ms                                                                                                                | 151 ms: 1.01x slower                                                                                                      |
| typing_runtime_protocols  | 167 us                                                                                                                | 169 us: 1.01x slower                                                                                                      |
| asyncio_tcp               | 368 ms                                                                                                                | 371 ms: 1.01x slower                                                                                                      |
| mdp                       | 1.27 sec                                                                                                              | 1.29 sec: 1.01x slower                                                                                                    |
| async_tree_none_tg        | 271 ms                                                                                                                | 274 ms: 1.01x slower                                                                                                      |
| subparsers                | 44.2 ms                                                                                                               | 44.7 ms: 1.01x slower                                                                                                     |
| django_template           | 34.6 ms                                                                                                               | 35.0 ms: 1.01x slower                                                                                                     |
| pickle_dict               | 33.5 us                                                                                                               | 33.9 us: 1.01x slower                                                                                                     |
| deltablue                 | 3.17 ms                                                                                                               | 3.21 ms: 1.01x slower                                                                                                     |
| docutils                  | 2.85 sec                                                                                                              | 2.88 sec: 1.01x slower                                                                                                    |
| json_loads                | 26.1 us                                                                                                               | 26.4 us: 1.01x slower                                                                                                     |
| logging_format            | 6.43 us                                                                                                               | 6.51 us: 1.01x slower                                                                                                     |
| deepcopy                  | 264 us                                                                                                                | 268 us: 1.01x slower                                                                                                      |
| async_tree_none           | 271 ms                                                                                                                | 275 ms: 1.01x slower                                                                                                      |
| float                     | 67.3 ms                                                                                                               | 68.4 ms: 1.02x slower                                                                                                     |
| coverage                  | 80.2 ms                                                                                                               | 81.4 ms: 1.02x slower                                                                                                     |
| sqlglot_v2_transpile      | 1.68 ms                                                                                                               | 1.70 ms: 1.02x slower                                                                                                     |
| html5lib                  | 64.9 ms                                                                                                               | 65.9 ms: 1.02x slower                                                                                                     |
| many_optionals            | 1.22 ms                                                                                                               | 1.24 ms: 1.02x slower                                                                                                     |
| nqueens                   | 90.1 ms                                                                                                               | 91.6 ms: 1.02x slower                                                                                                     |
| sqlglot_v2_normalize      | 112 ms                                                                                                                | 114 ms: 1.02x slower                                                                                                      |
| meteor_contest            | 118 ms                                                                                                                | 121 ms: 1.02x slower                                                                                                      |
| go                        | 117 ms                                                                                                                | 119 ms: 1.02x slower                                                                                                      |
| pathlib                   | 15.0 ms                                                                                                               | 15.3 ms: 1.02x slower                                                                                                     |
| sqlglot_v2_parse          | 1.28 ms                                                                                                               | 1.31 ms: 1.02x slower                                                                                                     |
| json                      | 5.33 ms                                                                                                               | 5.45 ms: 1.02x slower                                                                                                     |
| sympy_integrate           | 21.8 ms                                                                                                               | 22.3 ms: 1.02x slower                                                                                                     |
| create_gc_cycles          | 2.83 ms                                                                                                               | 2.90 ms: 1.02x slower                                                                                                     |
| genshi_xml                | 52.4 ms                                                                                                               | 53.6 ms: 1.02x slower                                                                                                     |
| 2to3                      | 278 ms                                                                                                                | 284 ms: 1.02x slower                                                                                                      |
| sqlglot_v2_optimize       | 56.4 ms                                                                                                               | 57.8 ms: 1.02x slower                                                                                                     |
| hexiom                    | 5.77 ms                                                                                                               | 5.92 ms: 1.03x slower                                                                                                     |
| scimark_sparse_mat_mult   | 4.62 ms                                                                                                               | 4.74 ms: 1.03x slower                                                                                                     |
| sympy_str                 | 283 ms                                                                                                                | 291 ms: 1.03x slower                                                                                                      |
| unpickle                  | 14.6 us                                                                                                               | 15.0 us: 1.03x slower                                                                                                     |
| pickle_list               | 4.84 us                                                                                                               | 4.98 us: 1.03x slower                                                                                                     |
| thrift                    | 830 us                                                                                                                | 855 us: 1.03x slower                                                                                                      |
| sympy_expand              | 481 ms                                                                                                                | 498 ms: 1.04x slower                                                                                                      |
| scimark_monte_carlo       | 59.3 ms                                                                                                               | 61.5 ms: 1.04x slower                                                                                                     |
| async_generators          | 422 ms                                                                                                                | 438 ms: 1.04x slower                                                                                                      |
| coroutines                | 21.9 ms                                                                                                               | 22.8 ms: 1.04x slower                                                                                                     |
| regex_dna                 | 222 ms                                                                                                                | 231 ms: 1.04x slower                                                                                                      |
| raytrace                  | 271 ms                                                                                                                | 284 ms: 1.04x slower                                                                                                      |
| fannkuch                  | 351 ms                                                                                                                | 368 ms: 1.05x slower                                                                                                      |
| comprehensions            | 16.3 us                                                                                                               | 17.4 us: 1.07x slower                                                                                                     |
| generators                | 28.1 ms                                                                                                               | 30.0 ms: 1.07x slower                                                                                                     |
| nbody                     | 91.2 ms                                                                                                               | 97.7 ms: 1.07x slower                                                                                                     |
| regex_effbot              | 3.42 ms                                                                                                               | 3.67 ms: 1.07x slower                                                                                                     |
| gc_traversal              | 6.25 ms                                                                                                               | 6.73 ms: 1.08x slower                                                                                                     |
| unpack_sequence           | 42.7 ns                                                                                                               | 53.2 ns: 1.25x slower                                                                                                     |
| Geometric mean            | (ref)                                                                                                                 | 1.01x slower                                                                                                              |

Benchmark hidden because not significant (17): telco, genshi_text, pickle_pure_python, djangocms, async_tree_cpu_io_mixed, bench_thread_pool, logging_silent, regex_compile, asyncio_websockets, sqlite_synth, scimark_lu, async_tree_cpu_io_mixed_tg, async_tree_memoization, pylint, sphinx, async_tree_io_tg, bench_mp_pool

- Geometric mean (including insignificant results): 1.003x slower

# HPT report

- Reliability score: 99.11% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x