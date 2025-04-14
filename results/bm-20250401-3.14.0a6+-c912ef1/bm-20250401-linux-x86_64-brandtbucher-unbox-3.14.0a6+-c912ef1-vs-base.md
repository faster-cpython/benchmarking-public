# Results vs. base

- fork: brandtbucher
- ref: unbox
- machine: linux-x86_64
- commit hash: c912ef1
- commit date: 2025-04-01
- overall geometric mean: 1.021x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 254 ms                                                                 | 261 ms: 1.03x slower                                          |
| docutils       | 2.61 sec                                                               | 2.65 sec: 1.02x slower                                        |
| html5lib       | 62.7 ms                                                                | 63.9 ms: 1.02x slower                                         |
| sphinx         | 1.01 sec                                                               | 1.03 sec: 1.02x slower                                        |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| coroutines                 | 23.2 ms                                                                | 21.8 ms: 1.06x faster                                         |
| async_tree_cpu_io_mixed_tg | 477 ms                                                                 | 482 ms: 1.01x slower                                          |
| async_generators           | 395 ms                                                                 | 399 ms: 1.01x slower                                          |
| async_tree_cpu_io_mixed    | 490 ms                                                                 | 495 ms: 1.01x slower                                          |
| async_tree_none_tg         | 250 ms                                                                 | 257 ms: 1.03x slower                                          |
| async_tree_none            | 261 ms                                                                 | 268 ms: 1.03x slower                                          |
| async_tree_io              | 615 ms                                                                 | 634 ms: 1.03x slower                                          |
| async_tree_memoization_tg  | 317 ms                                                                 | 326 ms: 1.03x slower                                          |
| async_tree_memoization     | 314 ms                                                                 | 324 ms: 1.03x slower                                          |
| async_tree_io_tg           | 614 ms                                                                 | 640 ms: 1.04x slower                                          |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                  |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| pidigits       | 187 ms                                                                 | 189 ms: 1.01x slower                                          |
| nbody          | 96.9 ms                                                                | 102 ms: 1.05x slower                                          |
| float          | 69.5 ms                                                                | 75.4 ms: 1.08x slower                                         |
| Geometric mean | (ref)                                                                  | 1.05x slower                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_dna      | 221 ms                                                                 | 217 ms: 1.02x faster                                          |
| regex_effbot   | 3.34 ms                                                                | 3.44 ms: 1.03x slower                                         |
| regex_compile  | 126 ms                                                                 | 131 ms: 1.04x slower                                          |
| regex_v8       | 23.3 ms                                                                | 24.6 ms: 1.06x slower                                         |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| tomli_loads          | 1.96 sec                                                               | 1.88 sec: 1.04x faster                                        |
| json_dumps           | 11.9 ms                                                                | 11.6 ms: 1.02x faster                                         |
| xml_etree_iterparse  | 99.1 ms                                                                | 99.6 ms: 1.01x slower                                         |
| xml_etree_process    | 59.1 ms                                                                | 59.8 ms: 1.01x slower                                         |
| pickle_pure_python   | 315 us                                                                 | 326 us: 1.04x slower                                          |
| unpickle_pure_python | 218 us                                                                 | 226 us: 1.04x slower                                          |
| json_loads           | 29.6 us                                                                | 32.0 us: 1.08x slower                                         |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                  |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup_no_site | 8.17 ms                                                                | 8.22 ms: 1.01x slower                                         |
| python_startup         | 13.1 ms                                                                | 13.2 ms: 1.01x slower                                         |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| genshi_text     | 21.3 ms                                                                | 21.9 ms: 1.02x slower                                         |
| genshi_xml      | 49.0 ms                                                                | 50.4 ms: 1.03x slower                                         |
| django_template | 31.3 ms                                                                | 32.5 ms: 1.04x slower                                         |
| mako            | 11.4 ms                                                                | 12.0 ms: 1.06x slower                                         |
| Geometric mean  | (ref)                                                                  | 1.04x slower                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| spectral_norm              | 99.5 ms                                                                | 91.1 ms: 1.09x faster                                         |
| coroutines                 | 23.2 ms                                                                | 21.8 ms: 1.06x faster                                         |
| tomli_loads                | 1.96 sec                                                               | 1.88 sec: 1.04x faster                                        |
| bpe_tokeniser              | 4.63 sec                                                               | 4.48 sec: 1.03x faster                                        |
| json_dumps                 | 11.9 ms                                                                | 11.6 ms: 1.02x faster                                         |
| regex_dna                  | 221 ms                                                                 | 217 ms: 1.02x faster                                          |
| hexiom                     | 6.18 ms                                                                | 6.08 ms: 1.02x faster                                         |
| gc_traversal               | 5.06 ms                                                                | 4.99 ms: 1.01x faster                                         |
| chaos                      | 57.6 ms                                                                | 57.2 ms: 1.01x faster                                         |
| create_gc_cycles           | 2.49 ms                                                                | 2.47 ms: 1.00x faster                                         |
| bench_mp_pool              | 83.2 ms                                                                | 83.7 ms: 1.01x slower                                         |
| xml_etree_iterparse        | 99.1 ms                                                                | 99.6 ms: 1.01x slower                                         |
| python_startup_no_site     | 8.17 ms                                                                | 8.22 ms: 1.01x slower                                         |
| python_startup             | 13.1 ms                                                                | 13.2 ms: 1.01x slower                                         |
| deepcopy_reduce            | 2.70 us                                                                | 2.72 us: 1.01x slower                                         |
| mdp                        | 1.23 sec                                                               | 1.24 sec: 1.01x slower                                        |
| logging_format             | 6.20 us                                                                | 6.26 us: 1.01x slower                                         |
| sqlalchemy_imperative      | 16.8 ms                                                                | 17.0 ms: 1.01x slower                                         |
| async_tree_cpu_io_mixed_tg | 477 ms                                                                 | 482 ms: 1.01x slower                                          |
| async_generators           | 395 ms                                                                 | 399 ms: 1.01x slower                                          |
| pidigits                   | 187 ms                                                                 | 189 ms: 1.01x slower                                          |
| async_tree_cpu_io_mixed    | 490 ms                                                                 | 495 ms: 1.01x slower                                          |
| xml_etree_process          | 59.1 ms                                                                | 59.8 ms: 1.01x slower                                         |
| comprehensions             | 17.0 us                                                                | 17.3 us: 1.01x slower                                         |
| sympy_integrate            | 19.5 ms                                                                | 19.7 ms: 1.01x slower                                         |
| many_optionals             | 947 us                                                                 | 960 us: 1.01x slower                                          |
| sqlite_synth               | 2.78 us                                                                | 2.82 us: 1.01x slower                                         |
| sympy_expand               | 459 ms                                                                 | 466 ms: 1.01x slower                                          |
| bench_thread_pool          | 871 us                                                                 | 884 us: 1.01x slower                                          |
| docutils                   | 2.61 sec                                                               | 2.65 sec: 1.02x slower                                        |
| sqlalchemy_declarative     | 130 ms                                                                 | 132 ms: 1.02x slower                                          |
| sqlglot_v2_optimize        | 53.2 ms                                                                | 54.1 ms: 1.02x slower                                         |
| sympy_str                  | 268 ms                                                                 | 273 ms: 1.02x slower                                          |
| telco                      | 7.93 ms                                                                | 8.07 ms: 1.02x slower                                         |
| sphinx                     | 1.01 sec                                                               | 1.03 sec: 1.02x slower                                        |
| dulwich_log                | 58.3 ms                                                                | 59.4 ms: 1.02x slower                                         |
| html5lib                   | 62.7 ms                                                                | 63.9 ms: 1.02x slower                                         |
| sqlglot_v2_transpile       | 1.58 ms                                                                | 1.62 ms: 1.02x slower                                         |
| sqlglot_v2_parse           | 1.27 ms                                                                | 1.29 ms: 1.02x slower                                         |
| logging_simple             | 5.59 us                                                                | 5.71 us: 1.02x slower                                         |
| sqlglot_v2_normalize       | 106 ms                                                                 | 109 ms: 1.02x slower                                          |
| subparsers                 | 20.8 ms                                                                | 21.3 ms: 1.02x slower                                         |
| genshi_text                | 21.3 ms                                                                | 21.9 ms: 1.02x slower                                         |
| scimark_monte_carlo        | 66.2 ms                                                                | 67.9 ms: 1.03x slower                                         |
| nqueens                    | 81.3 ms                                                                | 83.5 ms: 1.03x slower                                         |
| async_tree_none_tg         | 250 ms                                                                 | 257 ms: 1.03x slower                                          |
| async_tree_none            | 261 ms                                                                 | 268 ms: 1.03x slower                                          |
| 2to3                       | 254 ms                                                                 | 261 ms: 1.03x slower                                          |
| sympy_sum                  | 148 ms                                                                 | 152 ms: 1.03x slower                                          |
| genshi_xml                 | 49.0 ms                                                                | 50.4 ms: 1.03x slower                                         |
| typing_runtime_protocols   | 161 us                                                                 | 166 us: 1.03x slower                                          |
| async_tree_io              | 615 ms                                                                 | 634 ms: 1.03x slower                                          |
| async_tree_memoization_tg  | 317 ms                                                                 | 326 ms: 1.03x slower                                          |
| shortest_path              | 498 ms                                                                 | 513 ms: 1.03x slower                                          |
| regex_effbot               | 3.34 ms                                                                | 3.44 ms: 1.03x slower                                         |
| generators                 | 28.1 ms                                                                | 29.0 ms: 1.03x slower                                         |
| raytrace                   | 262 ms                                                                 | 270 ms: 1.03x slower                                          |
| async_tree_memoization     | 314 ms                                                                 | 324 ms: 1.03x slower                                          |
| pickle_pure_python         | 315 us                                                                 | 326 us: 1.04x slower                                          |
| django_template            | 31.3 ms                                                                | 32.5 ms: 1.04x slower                                         |
| regex_compile              | 126 ms                                                                 | 131 ms: 1.04x slower                                          |
| richards                   | 44.4 ms                                                                | 46.1 ms: 1.04x slower                                         |
| unpickle_pure_python       | 218 us                                                                 | 226 us: 1.04x slower                                          |
| json                       | 5.25 ms                                                                | 5.47 ms: 1.04x slower                                         |
| deepcopy                   | 252 us                                                                 | 263 us: 1.04x slower                                          |
| async_tree_io_tg           | 614 ms                                                                 | 640 ms: 1.04x slower                                          |
| pprint_safe_repr           | 730 ms                                                                 | 762 ms: 1.04x slower                                          |
| pyflate                    | 456 ms                                                                 | 476 ms: 1.04x slower                                          |
| richards_super             | 50.2 ms                                                                | 52.5 ms: 1.05x slower                                         |
| pprint_pformat             | 1.50 sec                                                               | 1.57 sec: 1.05x slower                                        |
| nbody                      | 96.9 ms                                                                | 102 ms: 1.05x slower                                          |
| deepcopy_memo              | 29.3 us                                                                | 30.8 us: 1.05x slower                                         |
| go                         | 113 ms                                                                 | 120 ms: 1.05x slower                                          |
| mako                       | 11.4 ms                                                                | 12.0 ms: 1.06x slower                                         |
| regex_v8                   | 23.3 ms                                                                | 24.6 ms: 1.06x slower                                         |
| deltablue                  | 3.09 ms                                                                | 3.33 ms: 1.08x slower                                         |
| json_loads                 | 29.6 us                                                                | 32.0 us: 1.08x slower                                         |
| float                      | 69.5 ms                                                                | 75.4 ms: 1.08x slower                                         |
| scimark_fft                | 350 ms                                                                 | 384 ms: 1.10x slower                                          |
| scimark_lu                 | 114 ms                                                                 | 126 ms: 1.11x slower                                          |
| crypto_pyaes               | 74.8 ms                                                                | 82.8 ms: 1.11x slower                                         |
| scimark_sparse_mat_mult    | 4.68 ms                                                                | 5.29 ms: 1.13x slower                                         |
| Geometric mean             | (ref)                                                                  | 1.02x slower                                                  |

Benchmark hidden because not significant (13): connected_components, pathlib, scimark_sor, xml_etree_generate, logging_silent, asyncio_websockets, xml_etree_parse, fannkuch, k_core, meteor_contest, coverage, pycparser, pylint

- Geometric mean (including insignificant results): 1.021x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.00x