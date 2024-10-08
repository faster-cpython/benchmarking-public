# Results vs. base

- fork: brandtbucher
- ref: invalidate_side_exit
- machine: linux-x86_64
- commit hash: eb895df
- commit date: 2024-07-16
- overall geometric mean: 1.00x slower
- HPT reliability: 77.11%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240715-linux-x86_64-python-8b209fd4f8a9bf960388-3.14.0a0-8b209fd | bm-20240716-linux-x86_64-brandtbucher-invalidate_side_exit-3.14.0a0-eb895df |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 2.84 sec                                                              | 2.86 sec: 1.01x slower                                                      |
| html5lib       | 64.0 ms                                                               | 65.5 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_io_tg, async_tree_none_tg, async_tree_none, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240715-linux-x86_64-python-8b209fd4f8a9bf960388-3.14.0a0-8b209fd | bm-20240716-linux-x86_64-brandtbucher-invalidate_side_exit-3.14.0a0-eb895df |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 70.6 ms                                                               | 70.0 ms: 1.01x faster                                                       |
| pidigits       | 185 ms                                                                | 186 ms: 1.00x slower                                                        |
| nbody          | 79.6 ms                                                               | 80.2 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240715-linux-x86_64-python-8b209fd4f8a9bf960388-3.14.0a0-8b209fd | bm-20240716-linux-x86_64-brandtbucher-invalidate_side_exit-3.14.0a0-eb895df |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 133 ms                                                                | 135 ms: 1.01x slower                                                        |
| regex_dna      | 225 ms                                                                | 229 ms: 1.02x slower                                                        |
| regex_v8       | 24.2 ms                                                               | 24.9 ms: 1.03x slower                                                       |
| regex_effbot   | 3.58 ms                                                               | 3.71 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240715-linux-x86_64-python-8b209fd4f8a9bf960388-3.14.0a0-8b209fd | bm-20240716-linux-x86_64-brandtbucher-invalidate_side_exit-3.14.0a0-eb895df |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 218 us                                                                | 216 us: 1.01x faster                                                        |
| json_loads           | 27.5 us                                                               | 27.3 us: 1.00x faster                                                       |
| xml_etree_iterparse  | 99.4 ms                                                               | 99.0 ms: 1.00x faster                                                       |
| json_dumps           | 10.4 ms                                                               | 10.6 ms: 1.02x slower                                                       |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (5): pickle_pure_python, xml_etree_generate, xml_etree_process, xml_etree_parse, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240715-linux-x86_64-python-8b209fd4f8a9bf960388-3.14.0a0-8b209fd | bm-20240716-linux-x86_64-brandtbucher-invalidate_side_exit-3.14.0a0-eb895df |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.16 ms                                                               | 7.18 ms: 1.00x slower                                                       |
| python_startup         | 10.6 ms                                                               | 10.6 ms: 1.00x slower                                                       |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240715-linux-x86_64-python-8b209fd4f8a9bf960388-3.14.0a0-8b209fd | bm-20240716-linux-x86_64-brandtbucher-invalidate_side_exit-3.14.0a0-eb895df |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.75 ms                                                               | 9.71 ms: 1.00x faster                                                       |
| django_template | 35.5 ms                                                               | 35.9 ms: 1.01x slower                                                       |
| genshi_text     | 24.8 ms                                                               | 25.2 ms: 1.01x slower                                                       |
| genshi_xml      | 55.4 ms                                                               | 56.7 ms: 1.02x slower                                                       |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                                |

All benchmarks:
===============

| Benchmark                | bm-20240715-linux-x86_64-python-8b209fd4f8a9bf960388-3.14.0a0-8b209fd | bm-20240716-linux-x86_64-brandtbucher-invalidate_side_exit-3.14.0a0-eb895df |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| richards_super           | 48.0 ms                                                               | 46.5 ms: 1.03x faster                                                       |
| deltablue                | 3.57 ms                                                               | 3.48 ms: 1.03x faster                                                       |
| pycparser                | 1.13 sec                                                              | 1.10 sec: 1.02x faster                                                      |
| async_generators         | 462 ms                                                                | 455 ms: 1.01x faster                                                        |
| nqueens                  | 86.2 ms                                                               | 85.1 ms: 1.01x faster                                                       |
| richards                 | 41.1 ms                                                               | 40.6 ms: 1.01x faster                                                       |
| scimark_sor              | 130 ms                                                                | 129 ms: 1.01x faster                                                        |
| unpickle_pure_python     | 218 us                                                                | 216 us: 1.01x faster                                                        |
| scimark_fft              | 317 ms                                                                | 314 ms: 1.01x faster                                                        |
| scimark_sparse_mat_mult  | 4.48 ms                                                               | 4.44 ms: 1.01x faster                                                       |
| float                    | 70.6 ms                                                               | 70.0 ms: 1.01x faster                                                       |
| spectral_norm            | 102 ms                                                                | 102 ms: 1.01x faster                                                        |
| crypto_pyaes             | 67.9 ms                                                               | 67.4 ms: 1.01x faster                                                       |
| raytrace                 | 271 ms                                                                | 270 ms: 1.01x faster                                                        |
| sympy_integrate          | 21.8 ms                                                               | 21.7 ms: 1.01x faster                                                       |
| asyncio_tcp              | 507 ms                                                                | 504 ms: 1.01x faster                                                        |
| scimark_lu               | 124 ms                                                                | 123 ms: 1.01x faster                                                        |
| create_gc_cycles         | 1.77 ms                                                               | 1.76 ms: 1.00x faster                                                       |
| json_loads               | 27.5 us                                                               | 27.3 us: 1.00x faster                                                       |
| sympy_str                | 292 ms                                                                | 291 ms: 1.00x faster                                                        |
| xml_etree_iterparse      | 99.4 ms                                                               | 99.0 ms: 1.00x faster                                                       |
| mako                     | 9.75 ms                                                               | 9.71 ms: 1.00x faster                                                       |
| hexiom                   | 6.55 ms                                                               | 6.54 ms: 1.00x faster                                                       |
| asyncio_tcp_ssl          | 1.81 sec                                                              | 1.81 sec: 1.00x slower                                                      |
| pidigits                 | 185 ms                                                                | 186 ms: 1.00x slower                                                        |
| bench_thread_pool        | 832 us                                                                | 833 us: 1.00x slower                                                        |
| python_startup_no_site   | 7.16 ms                                                               | 7.18 ms: 1.00x slower                                                       |
| python_startup           | 10.6 ms                                                               | 10.6 ms: 1.00x slower                                                       |
| pathlib                  | 16.0 ms                                                               | 16.1 ms: 1.00x slower                                                       |
| sqlglot_normalize        | 111 ms                                                                | 112 ms: 1.00x slower                                                        |
| sqlglot_optimize         | 55.2 ms                                                               | 55.5 ms: 1.01x slower                                                       |
| sympy_expand             | 491 ms                                                                | 494 ms: 1.01x slower                                                        |
| dulwich_log              | 67.2 ms                                                               | 67.6 ms: 1.01x slower                                                       |
| docutils                 | 2.84 sec                                                              | 2.86 sec: 1.01x slower                                                      |
| nbody                    | 79.6 ms                                                               | 80.2 ms: 1.01x slower                                                       |
| comprehensions           | 16.4 us                                                               | 16.5 us: 1.01x slower                                                       |
| django_template          | 35.5 ms                                                               | 35.9 ms: 1.01x slower                                                       |
| logging_simple           | 5.56 us                                                               | 5.62 us: 1.01x slower                                                       |
| fannkuch                 | 359 ms                                                                | 363 ms: 1.01x slower                                                        |
| meteor_contest           | 105 ms                                                                | 106 ms: 1.01x slower                                                        |
| regex_compile            | 133 ms                                                                | 135 ms: 1.01x slower                                                        |
| typing_runtime_protocols | 167 us                                                                | 170 us: 1.01x slower                                                        |
| deepcopy_reduce          | 2.75 us                                                               | 2.79 us: 1.01x slower                                                       |
| genshi_text              | 24.8 ms                                                               | 25.2 ms: 1.01x slower                                                       |
| json                     | 5.11 ms                                                               | 5.19 ms: 1.02x slower                                                       |
| deepcopy_memo            | 28.2 us                                                               | 28.8 us: 1.02x slower                                                       |
| json_dumps               | 10.4 ms                                                               | 10.6 ms: 1.02x slower                                                       |
| regex_dna                | 225 ms                                                                | 229 ms: 1.02x slower                                                        |
| gc_traversal             | 3.65 ms                                                               | 3.74 ms: 1.02x slower                                                       |
| html5lib                 | 64.0 ms                                                               | 65.5 ms: 1.02x slower                                                       |
| genshi_xml               | 55.4 ms                                                               | 56.7 ms: 1.02x slower                                                       |
| regex_v8                 | 24.2 ms                                                               | 24.9 ms: 1.03x slower                                                       |
| regex_effbot             | 3.58 ms                                                               | 3.71 ms: 1.04x slower                                                       |
| mdp                      | 2.53 sec                                                              | 2.68 sec: 1.06x slower                                                      |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (37): deepcopy, chaos, telco, scimark_monte_carlo, coroutines, sympy_sum, pickle_pure_python, pylint, xml_etree_generate, async_tree_io_tg, xml_etree_process, logging_format, 2to3, async_tree_none_tg, logging_silent, bpe_tokeniser, tornado_http, thrift, async_tree_none, pyflate, async_tree_memoization_tg, bench_mp_pool, sqlglot_transpile, coverage, sqlglot_parse, async_tree_cpu_io_mixed, dask, xml_etree_parse, generators, asyncio_websockets, async_tree_memoization, go, async_tree_cpu_io_mixed_tg, pprint_pformat, pprint_safe_repr, tomli_loads, async_tree_io

# HPT report

- Reliability score: 77.11% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x