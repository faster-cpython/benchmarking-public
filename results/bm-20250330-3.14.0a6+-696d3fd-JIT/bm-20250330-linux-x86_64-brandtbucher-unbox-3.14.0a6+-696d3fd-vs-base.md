# Results vs. base

- fork: brandtbucher
- ref: unbox
- machine: linux-x86_64
- commit hash: 696d3fd
- commit date: 2025-03-30
- overall geometric mean: 1.054x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 2.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 262 ms                                                                 | 272 ms: 1.04x slower                                          |
| docutils       | 2.66 sec                                                               | 2.77 sec: 1.04x slower                                        |
| html5lib       | 63.2 ms                                                                | 64.5 ms: 1.02x slower                                         |
| sphinx         | 1.02 sec                                                               | 1.05 sec: 1.03x slower                                        |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|---------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| coroutines                | 23.1 ms                                                                | 21.9 ms: 1.06x faster                                         |
| async_tree_cpu_io_mixed   | 488 ms                                                                 | 494 ms: 1.01x slower                                          |
| async_generators          | 412 ms                                                                 | 418 ms: 1.02x slower                                          |
| async_tree_memoization_tg | 315 ms                                                                 | 322 ms: 1.02x slower                                          |
| async_tree_none           | 261 ms                                                                 | 267 ms: 1.02x slower                                          |
| async_tree_memoization    | 314 ms                                                                 | 328 ms: 1.05x slower                                          |
| Geometric mean            | (ref)                                                                  | 1.01x slower                                                  |

Benchmark hidden because not significant (5): async_tree_cpu_io_mixed_tg, async_tree_io_tg, asyncio_websockets, async_tree_none_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| pidigits       | 185 ms                                                                 | 188 ms: 1.01x slower                                          |
| nbody          | 84.7 ms                                                                | 107 ms: 1.27x slower                                          |
| float          | 62.7 ms                                                                | 81.0 ms: 1.29x slower                                         |
| Geometric mean | (ref)                                                                  | 1.18x slower                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_dna      | 215 ms                                                                 | 209 ms: 1.03x faster                                          |
| regex_effbot   | 3.16 ms                                                                | 3.26 ms: 1.03x slower                                         |
| regex_v8       | 22.2 ms                                                                | 23.2 ms: 1.04x slower                                         |
| regex_compile  | 128 ms                                                                 | 137 ms: 1.08x slower                                          |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| tomli_loads          | 1.87 sec                                                               | 1.85 sec: 1.01x faster                                        |
| xml_etree_iterparse  | 98.3 ms                                                                | 99.1 ms: 1.01x slower                                         |
| json_loads           | 29.5 us                                                                | 29.8 us: 1.01x slower                                         |
| xml_etree_process    | 56.4 ms                                                                | 59.1 ms: 1.05x slower                                         |
| xml_etree_generate   | 79.7 ms                                                                | 84.5 ms: 1.06x slower                                         |
| pickle_pure_python   | 322 us                                                                 | 342 us: 1.06x slower                                          |
| unpickle_pure_python | 214 us                                                                 | 236 us: 1.10x slower                                          |
| Geometric mean       | (ref)                                                                  | 1.03x slower                                                  |

Benchmark hidden because not significant (2): json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup_no_site | 8.17 ms                                                                | 8.22 ms: 1.01x slower                                         |
| python_startup         | 13.1 ms                                                                | 13.2 ms: 1.01x slower                                         |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| django_template | 32.2 ms                                                                | 33.5 ms: 1.04x slower                                         |
| genshi_text     | 21.1 ms                                                                | 22.1 ms: 1.05x slower                                         |
| genshi_xml      | 49.6 ms                                                                | 52.1 ms: 1.05x slower                                         |
| mako            | 10.9 ms                                                                | 11.6 ms: 1.06x slower                                         |
| Geometric mean  | (ref)                                                                  | 1.05x slower                                                  |

All benchmarks:
===============

| Benchmark                 | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|---------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| coroutines                | 23.1 ms                                                                | 21.9 ms: 1.06x faster                                         |
| gc_traversal              | 5.03 ms                                                                | 4.82 ms: 1.04x faster                                         |
| regex_dna                 | 215 ms                                                                 | 209 ms: 1.03x faster                                          |
| tomli_loads               | 1.87 sec                                                               | 1.85 sec: 1.01x faster                                        |
| create_gc_cycles          | 2.48 ms                                                                | 2.49 ms: 1.00x slower                                         |
| python_startup_no_site    | 8.17 ms                                                                | 8.22 ms: 1.01x slower                                         |
| python_startup            | 13.1 ms                                                                | 13.2 ms: 1.01x slower                                         |
| pathlib                   | 16.6 ms                                                                | 16.8 ms: 1.01x slower                                         |
| xml_etree_iterparse       | 98.3 ms                                                                | 99.1 ms: 1.01x slower                                         |
| json_loads                | 29.5 us                                                                | 29.8 us: 1.01x slower                                         |
| async_tree_cpu_io_mixed   | 488 ms                                                                 | 494 ms: 1.01x slower                                          |
| pidigits                  | 185 ms                                                                 | 188 ms: 1.01x slower                                          |
| bench_mp_pool             | 83.0 ms                                                                | 84.3 ms: 1.02x slower                                         |
| async_generators          | 412 ms                                                                 | 418 ms: 1.02x slower                                          |
| coverage                  | 84.6 ms                                                                | 86.1 ms: 1.02x slower                                         |
| bench_thread_pool         | 883 us                                                                 | 899 us: 1.02x slower                                          |
| k_core                    | 2.31 sec                                                               | 2.35 sec: 1.02x slower                                        |
| html5lib                  | 63.2 ms                                                                | 64.5 ms: 1.02x slower                                         |
| bpe_tokeniser             | 4.56 sec                                                               | 4.66 sec: 1.02x slower                                        |
| async_tree_memoization_tg | 315 ms                                                                 | 322 ms: 1.02x slower                                          |
| async_tree_none           | 261 ms                                                                 | 267 ms: 1.02x slower                                          |
| sqlite_synth              | 2.75 us                                                                | 2.83 us: 1.03x slower                                         |
| sphinx                    | 1.02 sec                                                               | 1.05 sec: 1.03x slower                                        |
| pylint                    | 282 ms                                                                 | 290 ms: 1.03x slower                                          |
| dulwich_log               | 60.3 ms                                                                | 62.2 ms: 1.03x slower                                         |
| sqlglot_v2_normalize      | 109 ms                                                                 | 112 ms: 1.03x slower                                          |
| sqlalchemy_declarative    | 132 ms                                                                 | 136 ms: 1.03x slower                                          |
| sqlalchemy_imperative     | 17.1 ms                                                                | 17.7 ms: 1.03x slower                                         |
| sqlglot_v2_optimize       | 54.6 ms                                                                | 56.4 ms: 1.03x slower                                         |
| shortest_path             | 496 ms                                                                 | 513 ms: 1.03x slower                                          |
| regex_effbot              | 3.16 ms                                                                | 3.26 ms: 1.03x slower                                         |
| many_optionals            | 971 us                                                                 | 1.01 ms: 1.04x slower                                         |
| sympy_sum                 | 150 ms                                                                 | 156 ms: 1.04x slower                                          |
| 2to3                      | 262 ms                                                                 | 272 ms: 1.04x slower                                          |
| chaos                     | 59.0 ms                                                                | 61.3 ms: 1.04x slower                                         |
| connected_components      | 454 ms                                                                 | 472 ms: 1.04x slower                                          |
| django_template           | 32.2 ms                                                                | 33.5 ms: 1.04x slower                                         |
| docutils                  | 2.66 sec                                                               | 2.77 sec: 1.04x slower                                        |
| sympy_str                 | 274 ms                                                                 | 286 ms: 1.04x slower                                          |
| regex_v8                  | 22.2 ms                                                                | 23.2 ms: 1.04x slower                                         |
| deepcopy                  | 262 us                                                                 | 274 us: 1.04x slower                                          |
| sqlglot_v2_transpile      | 1.59 ms                                                                | 1.66 ms: 1.05x slower                                         |
| logging_format            | 6.12 us                                                                | 6.40 us: 1.05x slower                                         |
| async_tree_memoization    | 314 ms                                                                 | 328 ms: 1.05x slower                                          |
| subparsers                | 21.0 ms                                                                | 21.9 ms: 1.05x slower                                         |
| sympy_integrate           | 19.8 ms                                                                | 20.7 ms: 1.05x slower                                         |
| genshi_text               | 21.1 ms                                                                | 22.1 ms: 1.05x slower                                         |
| xml_etree_process         | 56.4 ms                                                                | 59.1 ms: 1.05x slower                                         |
| sympy_expand              | 475 ms                                                                 | 498 ms: 1.05x slower                                          |
| genshi_xml                | 49.6 ms                                                                | 52.1 ms: 1.05x slower                                         |
| telco                     | 7.77 ms                                                                | 8.19 ms: 1.05x slower                                         |
| meteor_contest            | 108 ms                                                                 | 114 ms: 1.06x slower                                          |
| pprint_safe_repr          | 773 ms                                                                 | 817 ms: 1.06x slower                                          |
| sqlglot_v2_parse          | 1.28 ms                                                                | 1.35 ms: 1.06x slower                                         |
| logging_simple            | 5.54 us                                                                | 5.85 us: 1.06x slower                                         |
| xml_etree_generate        | 79.7 ms                                                                | 84.5 ms: 1.06x slower                                         |
| pickle_pure_python        | 322 us                                                                 | 342 us: 1.06x slower                                          |
| deepcopy_memo             | 29.0 us                                                                | 30.8 us: 1.06x slower                                         |
| mako                      | 10.9 ms                                                                | 11.6 ms: 1.06x slower                                         |
| deepcopy_reduce           | 2.72 us                                                                | 2.89 us: 1.06x slower                                         |
| generators                | 27.9 ms                                                                | 29.7 ms: 1.07x slower                                         |
| pprint_pformat            | 1.60 sec                                                               | 1.71 sec: 1.07x slower                                        |
| fannkuch                  | 418 ms                                                                 | 448 ms: 1.07x slower                                          |
| mdp                       | 1.24 sec                                                               | 1.33 sec: 1.07x slower                                        |
| nqueens                   | 83.5 ms                                                                | 89.7 ms: 1.07x slower                                         |
| regex_compile             | 128 ms                                                                 | 137 ms: 1.08x slower                                          |
| typing_runtime_protocols  | 168 us                                                                 | 181 us: 1.08x slower                                          |
| raytrace                  | 270 ms                                                                 | 291 ms: 1.08x slower                                          |
| scimark_monte_carlo       | 67.0 ms                                                                | 72.6 ms: 1.08x slower                                         |
| scimark_lu                | 116 ms                                                                 | 126 ms: 1.09x slower                                          |
| comprehensions            | 18.8 us                                                                | 20.5 us: 1.09x slower                                         |
| pycparser                 | 1.14 sec                                                               | 1.25 sec: 1.10x slower                                        |
| hexiom                    | 6.73 ms                                                                | 7.41 ms: 1.10x slower                                         |
| unpickle_pure_python      | 214 us                                                                 | 236 us: 1.10x slower                                          |
| pyflate                   | 429 ms                                                                 | 478 ms: 1.12x slower                                          |
| scimark_sor               | 120 ms                                                                 | 134 ms: 1.12x slower                                          |
| richards_super            | 40.7 ms                                                                | 45.8 ms: 1.13x slower                                         |
| richards                  | 35.3 ms                                                                | 40.4 ms: 1.14x slower                                         |
| crypto_pyaes              | 75.3 ms                                                                | 88.5 ms: 1.17x slower                                         |
| deltablue                 | 3.04 ms                                                                | 3.58 ms: 1.18x slower                                         |
| go                        | 126 ms                                                                 | 150 ms: 1.19x slower                                          |
| scimark_fft               | 310 ms                                                                 | 390 ms: 1.26x slower                                          |
| nbody                     | 84.7 ms                                                                | 107 ms: 1.27x slower                                          |
| float                     | 62.7 ms                                                                | 81.0 ms: 1.29x slower                                         |
| spectral_norm             | 93.8 ms                                                                | 127 ms: 1.35x slower                                          |
| scimark_sparse_mat_mult   | 4.56 ms                                                                | 6.18 ms: 1.36x slower                                         |
| Geometric mean            | (ref)                                                                  | 1.06x slower                                                  |

Benchmark hidden because not significant (9): async_tree_cpu_io_mixed_tg, async_tree_io_tg, json_dumps, logging_silent, asyncio_websockets, xml_etree_parse, json, async_tree_none_tg, async_tree_io

- Geometric mean (including insignificant results): 1.054x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 2.09x