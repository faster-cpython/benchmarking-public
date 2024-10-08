# Results vs. base

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: 639e7c2
- commit date: 2024-07-16
- overall geometric mean: 1.00x faster
- HPT reliability: 70.75%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240715-linux-x86_64-python-8b209fd4f8a9bf960388-3.14.0a0-8b209fd | bm-20240716-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-639e7c2 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 271 ms                                                                | 276 ms: 1.02x slower                                                      |
| docutils       | 2.84 sec                                                              | 2.92 sec: 1.03x slower                                                    |
| html5lib       | 64.0 ms                                                               | 66.4 ms: 1.04x slower                                                     |
| tornado_http   | 93.1 ms                                                               | 92.2 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240715-linux-x86_64-python-8b209fd4f8a9bf960388-3.14.0a0-8b209fd | bm-20240716-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-639e7c2 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io              | 862 ms                                                                | 830 ms: 1.04x faster                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                                | 536 ms: 1.01x faster                                                      |
| Geometric mean             | (ref)                                                                 | 1.02x faster                                                              |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed, async_tree_none, async_tree_io_tg, async_tree_none_tg, async_tree_memoization_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240715-linux-x86_64-python-8b209fd4f8a9bf960388-3.14.0a0-8b209fd | bm-20240716-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-639e7c2 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 70.6 ms                                                               | 69.9 ms: 1.01x faster                                                     |
| pidigits       | 185 ms                                                                | 186 ms: 1.00x slower                                                      |
| nbody          | 79.6 ms                                                               | 80.8 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240715-linux-x86_64-python-8b209fd4f8a9bf960388-3.14.0a0-8b209fd | bm-20240716-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-639e7c2 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 24.2 ms                                                               | 23.9 ms: 1.01x faster                                                     |
| regex_effbot   | 3.58 ms                                                               | 3.64 ms: 1.02x slower                                                     |
| regex_dna      | 225 ms                                                                | 230 ms: 1.03x slower                                                      |
| regex_compile  | 133 ms                                                                | 138 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240715-linux-x86_64-python-8b209fd4f8a9bf960388-3.14.0a0-8b209fd | bm-20240716-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-639e7c2 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_pure_python | 218 us                                                                | 214 us: 1.02x faster                                                      |
| tomli_loads          | 1.93 sec                                                              | 1.90 sec: 1.02x faster                                                    |
| pickle_pure_python   | 297 us                                                                | 301 us: 1.01x slower                                                      |
| json_loads           | 27.5 us                                                               | 27.8 us: 1.01x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                              |

Benchmark hidden because not significant (5): xml_etree_process, xml_etree_generate, xml_etree_iterparse, json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240715-linux-x86_64-python-8b209fd4f8a9bf960388-3.14.0a0-8b209fd | bm-20240716-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-639e7c2 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 7.16 ms                                                               | 7.15 ms: 1.00x faster                                                     |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                              |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240715-linux-x86_64-python-8b209fd4f8a9bf960388-3.14.0a0-8b209fd | bm-20240716-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-639e7c2 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 35.5 ms                                                               | 35.1 ms: 1.01x faster                                                     |
| mako            | 9.75 ms                                                               | 9.73 ms: 1.00x faster                                                     |
| genshi_text     | 24.8 ms                                                               | 25.1 ms: 1.01x slower                                                     |
| genshi_xml      | 55.4 ms                                                               | 57.3 ms: 1.03x slower                                                     |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20240715-linux-x86_64-python-8b209fd4f8a9bf960388-3.14.0a0-8b209fd | bm-20240716-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-639e7c2 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| richards_super             | 48.0 ms                                                               | 40.9 ms: 1.18x faster                                                     |
| richards                   | 41.1 ms                                                               | 35.7 ms: 1.15x faster                                                     |
| scimark_lu                 | 124 ms                                                                | 117 ms: 1.06x faster                                                      |
| deepcopy                   | 275 us                                                                | 263 us: 1.05x faster                                                      |
| deepcopy_reduce            | 2.75 us                                                               | 2.63 us: 1.05x faster                                                     |
| scimark_sparse_mat_mult    | 4.48 ms                                                               | 4.29 ms: 1.04x faster                                                     |
| deltablue                  | 3.57 ms                                                               | 3.43 ms: 1.04x faster                                                     |
| async_tree_io              | 862 ms                                                                | 830 ms: 1.04x faster                                                      |
| scimark_sor                | 130 ms                                                                | 126 ms: 1.04x faster                                                      |
| deepcopy_memo              | 28.2 us                                                               | 27.3 us: 1.03x faster                                                     |
| gc_traversal               | 3.65 ms                                                               | 3.55 ms: 1.03x faster                                                     |
| scimark_fft                | 317 ms                                                                | 309 ms: 1.02x faster                                                      |
| unpickle_pure_python       | 218 us                                                                | 214 us: 1.02x faster                                                      |
| dulwich_log                | 67.2 ms                                                               | 65.9 ms: 1.02x faster                                                     |
| logging_silent             | 106 ns                                                                | 104 ns: 1.02x faster                                                      |
| create_gc_cycles           | 1.77 ms                                                               | 1.74 ms: 1.02x faster                                                     |
| tomli_loads                | 1.93 sec                                                              | 1.90 sec: 1.02x faster                                                    |
| chaos                      | 58.7 ms                                                               | 57.7 ms: 1.02x faster                                                     |
| regex_v8                   | 24.2 ms                                                               | 23.9 ms: 1.01x faster                                                     |
| logging_format             | 6.18 us                                                               | 6.10 us: 1.01x faster                                                     |
| async_tree_cpu_io_mixed_tg | 543 ms                                                                | 536 ms: 1.01x faster                                                      |
| django_template            | 35.5 ms                                                               | 35.1 ms: 1.01x faster                                                     |
| sympy_str                  | 292 ms                                                                | 289 ms: 1.01x faster                                                      |
| float                      | 70.6 ms                                                               | 69.9 ms: 1.01x faster                                                     |
| tornado_http               | 93.1 ms                                                               | 92.2 ms: 1.01x faster                                                     |
| logging_simple             | 5.56 us                                                               | 5.51 us: 1.01x faster                                                     |
| bench_thread_pool          | 832 us                                                                | 825 us: 1.01x faster                                                      |
| async_generators           | 462 ms                                                                | 458 ms: 1.01x faster                                                      |
| asyncio_tcp                | 507 ms                                                                | 503 ms: 1.01x faster                                                      |
| crypto_pyaes               | 67.9 ms                                                               | 67.3 ms: 1.01x faster                                                     |
| raytrace                   | 271 ms                                                                | 269 ms: 1.01x faster                                                      |
| asyncio_tcp_ssl            | 1.81 sec                                                              | 1.80 sec: 1.00x faster                                                    |
| mako                       | 9.75 ms                                                               | 9.73 ms: 1.00x faster                                                     |
| python_startup_no_site     | 7.16 ms                                                               | 7.15 ms: 1.00x faster                                                     |
| pidigits                   | 185 ms                                                                | 186 ms: 1.00x slower                                                      |
| go                         | 143 ms                                                                | 144 ms: 1.00x slower                                                      |
| sqlglot_normalize          | 111 ms                                                                | 111 ms: 1.00x slower                                                      |
| sympy_sum                  | 165 ms                                                                | 166 ms: 1.01x slower                                                      |
| sympy_expand               | 491 ms                                                                | 495 ms: 1.01x slower                                                      |
| pathlib                    | 16.0 ms                                                               | 16.1 ms: 1.01x slower                                                     |
| pycparser                  | 1.13 sec                                                              | 1.14 sec: 1.01x slower                                                    |
| coverage                   | 93.7 ms                                                               | 94.8 ms: 1.01x slower                                                     |
| pickle_pure_python         | 297 us                                                                | 301 us: 1.01x slower                                                      |
| genshi_text                | 24.8 ms                                                               | 25.1 ms: 1.01x slower                                                     |
| json_loads                 | 27.5 us                                                               | 27.8 us: 1.01x slower                                                     |
| fannkuch                   | 359 ms                                                                | 364 ms: 1.01x slower                                                      |
| coroutines                 | 22.4 ms                                                               | 22.7 ms: 1.01x slower                                                     |
| typing_runtime_protocols   | 167 us                                                                | 170 us: 1.01x slower                                                      |
| nbody                      | 79.6 ms                                                               | 80.8 ms: 1.02x slower                                                     |
| sqlglot_parse              | 1.27 ms                                                               | 1.29 ms: 1.02x slower                                                     |
| regex_effbot               | 3.58 ms                                                               | 3.64 ms: 1.02x slower                                                     |
| 2to3                       | 271 ms                                                                | 276 ms: 1.02x slower                                                      |
| comprehensions             | 16.4 us                                                               | 16.7 us: 1.02x slower                                                     |
| regex_dna                  | 225 ms                                                                | 230 ms: 1.03x slower                                                      |
| docutils                   | 2.84 sec                                                              | 2.92 sec: 1.03x slower                                                    |
| sqlglot_optimize           | 55.2 ms                                                               | 56.8 ms: 1.03x slower                                                     |
| sqlglot_transpile          | 1.59 ms                                                               | 1.64 ms: 1.03x slower                                                     |
| scimark_monte_carlo        | 61.2 ms                                                               | 63.0 ms: 1.03x slower                                                     |
| pprint_safe_repr           | 712 ms                                                                | 735 ms: 1.03x slower                                                      |
| hexiom                     | 6.55 ms                                                               | 6.77 ms: 1.03x slower                                                     |
| genshi_xml                 | 55.4 ms                                                               | 57.3 ms: 1.03x slower                                                     |
| html5lib                   | 64.0 ms                                                               | 66.4 ms: 1.04x slower                                                     |
| regex_compile              | 133 ms                                                                | 138 ms: 1.04x slower                                                      |
| meteor_contest             | 105 ms                                                                | 109 ms: 1.04x slower                                                      |
| pprint_pformat             | 1.45 sec                                                              | 1.52 sec: 1.05x slower                                                    |
| pyflate                    | 432 ms                                                                | 454 ms: 1.05x slower                                                      |
| mdp                        | 2.53 sec                                                              | 2.77 sec: 1.09x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                              |

Benchmark hidden because not significant (24): async_tree_cpu_io_mixed, async_tree_none, async_tree_io_tg, async_tree_none_tg, async_tree_memoization_tg, async_tree_memoization, dask, xml_etree_process, xml_etree_generate, xml_etree_iterparse, thrift, json_dumps, sympy_integrate, spectral_norm, python_startup, bpe_tokeniser, asyncio_websockets, bench_mp_pool, json, telco, nqueens, generators, xml_etree_parse, pylint

# HPT report

- Reliability score: 70.75% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x