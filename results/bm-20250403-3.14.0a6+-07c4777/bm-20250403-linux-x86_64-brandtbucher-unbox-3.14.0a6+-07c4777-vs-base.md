# Results vs. base

- fork: brandtbucher
- ref: unbox
- machine: linux-x86_64
- commit hash: 07c4777
- commit date: 2025-04-03
- overall geometric mean: 1.016x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250403-linux-x86_64-brandtbucher-unbox-3.14.0a6+-07c4777 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 254 ms                                                                 | 260 ms: 1.02x slower                                          |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                  |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250403-linux-x86_64-brandtbucher-unbox-3.14.0a6+-07c4777 |
|---------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| coroutines                | 23.2 ms                                                                | 21.2 ms: 1.09x faster                                         |
| async_tree_none_tg        | 250 ms                                                                 | 254 ms: 1.01x slower                                          |
| async_tree_none           | 261 ms                                                                 | 265 ms: 1.02x slower                                          |
| async_tree_memoization_tg | 317 ms                                                                 | 323 ms: 1.02x slower                                          |
| async_tree_io             | 615 ms                                                                 | 631 ms: 1.03x slower                                          |
| async_tree_memoization    | 314 ms                                                                 | 322 ms: 1.03x slower                                          |
| async_tree_io_tg          | 614 ms                                                                 | 633 ms: 1.03x slower                                          |
| Geometric mean            | (ref)                                                                  | 1.00x slower                                                  |

Benchmark hidden because not significant (4): asyncio_websockets, async_generators, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250403-linux-x86_64-brandtbucher-unbox-3.14.0a6+-07c4777 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| pidigits       | 187 ms                                                                 | 187 ms: 1.00x slower                                          |
| nbody          | 96.9 ms                                                                | 100 ms: 1.03x slower                                          |
| float          | 69.5 ms                                                                | 74.1 ms: 1.07x slower                                         |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250403-linux-x86_64-brandtbucher-unbox-3.14.0a6+-07c4777 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_effbot   | 3.34 ms                                                                | 3.25 ms: 1.03x faster                                         |
| regex_v8       | 23.3 ms                                                                | 22.7 ms: 1.02x faster                                         |
| regex_dna      | 221 ms                                                                 | 220 ms: 1.01x faster                                          |
| regex_compile  | 126 ms                                                                 | 131 ms: 1.04x slower                                          |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250403-linux-x86_64-brandtbucher-unbox-3.14.0a6+-07c4777 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| tomli_loads          | 1.96 sec                                                               | 1.86 sec: 1.06x faster                                        |
| json_dumps           | 11.9 ms                                                                | 11.3 ms: 1.05x faster                                         |
| xml_etree_parse      | 141 ms                                                                 | 142 ms: 1.01x slower                                          |
| xml_etree_process    | 59.1 ms                                                                | 59.8 ms: 1.01x slower                                         |
| unpickle_pure_python | 218 us                                                                 | 222 us: 1.02x slower                                          |
| pickle_pure_python   | 315 us                                                                 | 323 us: 1.03x slower                                          |
| json_loads           | 29.6 us                                                                | 34.2 us: 1.16x slower                                         |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                  |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250403-linux-x86_64-brandtbucher-unbox-3.14.0a6+-07c4777 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup_no_site | 8.17 ms                                                                | 8.20 ms: 1.00x slower                                         |
| python_startup         | 13.1 ms                                                                | 13.1 ms: 1.00x slower                                         |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250403-linux-x86_64-brandtbucher-unbox-3.14.0a6+-07c4777 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| mako            | 11.4 ms                                                                | 11.6 ms: 1.02x slower                                         |
| genshi_xml      | 49.0 ms                                                                | 50.2 ms: 1.02x slower                                         |
| genshi_text     | 21.3 ms                                                                | 21.9 ms: 1.03x slower                                         |
| django_template | 31.3 ms                                                                | 32.4 ms: 1.03x slower                                         |
| Geometric mean  | (ref)                                                                  | 1.03x slower                                                  |

All benchmarks:
===============

| Benchmark                 | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250403-linux-x86_64-brandtbucher-unbox-3.14.0a6+-07c4777 |
|---------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| coroutines                | 23.2 ms                                                                | 21.2 ms: 1.09x faster                                         |
| spectral_norm             | 99.5 ms                                                                | 92.5 ms: 1.08x faster                                         |
| tomli_loads               | 1.96 sec                                                               | 1.86 sec: 1.06x faster                                        |
| json_dumps                | 11.9 ms                                                                | 11.3 ms: 1.05x faster                                         |
| bpe_tokeniser             | 4.63 sec                                                               | 4.45 sec: 1.04x faster                                        |
| gc_traversal              | 5.06 ms                                                                | 4.91 ms: 1.03x faster                                         |
| regex_effbot              | 3.34 ms                                                                | 3.25 ms: 1.03x faster                                         |
| regex_v8                  | 23.3 ms                                                                | 22.7 ms: 1.02x faster                                         |
| connected_components      | 458 ms                                                                 | 453 ms: 1.01x faster                                          |
| shortest_path             | 498 ms                                                                 | 493 ms: 1.01x faster                                          |
| scimark_sor               | 119 ms                                                                 | 118 ms: 1.01x faster                                          |
| hexiom                    | 6.18 ms                                                                | 6.13 ms: 1.01x faster                                         |
| regex_dna                 | 221 ms                                                                 | 220 ms: 1.01x faster                                          |
| pathlib                   | 16.8 ms                                                                | 16.7 ms: 1.01x faster                                         |
| pidigits                  | 187 ms                                                                 | 187 ms: 1.00x slower                                          |
| python_startup_no_site    | 8.17 ms                                                                | 8.20 ms: 1.00x slower                                         |
| python_startup            | 13.1 ms                                                                | 13.1 ms: 1.00x slower                                         |
| bench_mp_pool             | 83.2 ms                                                                | 83.6 ms: 1.00x slower                                         |
| comprehensions            | 17.0 us                                                                | 17.2 us: 1.01x slower                                         |
| xml_etree_parse           | 141 ms                                                                 | 142 ms: 1.01x slower                                          |
| coverage                  | 84.0 ms                                                                | 84.7 ms: 1.01x slower                                         |
| logging_simple            | 5.59 us                                                                | 5.64 us: 1.01x slower                                         |
| sqlalchemy_imperative     | 16.8 ms                                                                | 17.0 ms: 1.01x slower                                         |
| pyflate                   | 456 ms                                                                 | 461 ms: 1.01x slower                                          |
| many_optionals            | 947 us                                                                 | 958 us: 1.01x slower                                          |
| xml_etree_process         | 59.1 ms                                                                | 59.8 ms: 1.01x slower                                         |
| mdp                       | 1.23 sec                                                               | 1.25 sec: 1.01x slower                                        |
| sqlalchemy_declarative    | 130 ms                                                                 | 132 ms: 1.01x slower                                          |
| async_tree_none_tg        | 250 ms                                                                 | 254 ms: 1.01x slower                                          |
| bench_thread_pool         | 871 us                                                                 | 885 us: 1.02x slower                                          |
| sqlglot_v2_optimize       | 53.2 ms                                                                | 54.0 ms: 1.02x slower                                         |
| sympy_integrate           | 19.5 ms                                                                | 19.8 ms: 1.02x slower                                         |
| sqlglot_v2_transpile      | 1.58 ms                                                                | 1.61 ms: 1.02x slower                                         |
| meteor_contest            | 107 ms                                                                 | 109 ms: 1.02x slower                                          |
| subparsers                | 20.8 ms                                                                | 21.2 ms: 1.02x slower                                         |
| async_tree_none           | 261 ms                                                                 | 265 ms: 1.02x slower                                          |
| typing_runtime_protocols  | 161 us                                                                 | 164 us: 1.02x slower                                          |
| sqlglot_v2_parse          | 1.27 ms                                                                | 1.29 ms: 1.02x slower                                         |
| sqlglot_v2_normalize      | 106 ms                                                                 | 108 ms: 1.02x slower                                          |
| mako                      | 11.4 ms                                                                | 11.6 ms: 1.02x slower                                         |
| unpickle_pure_python      | 218 us                                                                 | 222 us: 1.02x slower                                          |
| dulwich_log               | 58.3 ms                                                                | 59.4 ms: 1.02x slower                                         |
| richards                  | 44.4 ms                                                                | 45.3 ms: 1.02x slower                                         |
| sympy_str                 | 268 ms                                                                 | 274 ms: 1.02x slower                                          |
| async_tree_memoization_tg | 317 ms                                                                 | 323 ms: 1.02x slower                                          |
| 2to3                      | 254 ms                                                                 | 260 ms: 1.02x slower                                          |
| sympy_sum                 | 148 ms                                                                 | 151 ms: 1.02x slower                                          |
| fannkuch                  | 425 ms                                                                 | 435 ms: 1.02x slower                                          |
| sqlite_synth              | 2.78 us                                                                | 2.84 us: 1.02x slower                                         |
| sympy_expand              | 459 ms                                                                 | 470 ms: 1.02x slower                                          |
| genshi_xml                | 49.0 ms                                                                | 50.2 ms: 1.02x slower                                         |
| async_tree_io             | 615 ms                                                                 | 631 ms: 1.03x slower                                          |
| nqueens                   | 81.3 ms                                                                | 83.5 ms: 1.03x slower                                         |
| async_tree_memoization    | 314 ms                                                                 | 322 ms: 1.03x slower                                          |
| pickle_pure_python        | 315 us                                                                 | 323 us: 1.03x slower                                          |
| richards_super            | 50.2 ms                                                                | 51.6 ms: 1.03x slower                                         |
| pycparser                 | 1.17 sec                                                               | 1.20 sec: 1.03x slower                                        |
| generators                | 28.1 ms                                                                | 28.9 ms: 1.03x slower                                         |
| genshi_text               | 21.3 ms                                                                | 21.9 ms: 1.03x slower                                         |
| scimark_monte_carlo       | 66.2 ms                                                                | 68.2 ms: 1.03x slower                                         |
| async_tree_io_tg          | 614 ms                                                                 | 633 ms: 1.03x slower                                          |
| deepcopy                  | 252 us                                                                 | 260 us: 1.03x slower                                          |
| django_template           | 31.3 ms                                                                | 32.4 ms: 1.03x slower                                         |
| nbody                     | 96.9 ms                                                                | 100 ms: 1.03x slower                                          |
| raytrace                  | 262 ms                                                                 | 272 ms: 1.04x slower                                          |
| deepcopy_memo             | 29.3 us                                                                | 30.4 us: 1.04x slower                                         |
| regex_compile             | 126 ms                                                                 | 131 ms: 1.04x slower                                          |
| go                        | 113 ms                                                                 | 120 ms: 1.05x slower                                          |
| deltablue                 | 3.09 ms                                                                | 3.26 ms: 1.06x slower                                         |
| pprint_pformat            | 1.50 sec                                                               | 1.59 sec: 1.06x slower                                        |
| float                     | 69.5 ms                                                                | 74.1 ms: 1.07x slower                                         |
| pprint_safe_repr          | 730 ms                                                                 | 782 ms: 1.07x slower                                          |
| scimark_lu                | 114 ms                                                                 | 124 ms: 1.08x slower                                          |
| scimark_fft               | 350 ms                                                                 | 384 ms: 1.10x slower                                          |
| crypto_pyaes              | 74.8 ms                                                                | 82.1 ms: 1.10x slower                                         |
| scimark_sparse_mat_mult   | 4.68 ms                                                                | 5.15 ms: 1.10x slower                                         |
| json                      | 5.25 ms                                                                | 5.86 ms: 1.12x slower                                         |
| json_loads                | 29.6 us                                                                | 34.2 us: 1.16x slower                                         |
| Geometric mean            | (ref)                                                                  | 1.02x slower                                                  |

Benchmark hidden because not significant (17): logging_silent, chaos, asyncio_websockets, async_generators, xml_etree_generate, async_tree_cpu_io_mixed, html5lib, create_gc_cycles, telco, logging_format, docutils, deepcopy_reduce, async_tree_cpu_io_mixed_tg, xml_etree_iterparse, sphinx, k_core, pylint

- Geometric mean (including insignificant results): 1.016x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x