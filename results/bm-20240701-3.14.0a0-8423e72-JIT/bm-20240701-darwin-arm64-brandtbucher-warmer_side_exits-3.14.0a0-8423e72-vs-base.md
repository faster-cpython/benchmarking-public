# Results vs. base

- fork: brandtbucher
- ref: warmer_side_exits
- machine: darwin-arm64
- commit hash: 8423e72
- commit date: 2024-07-01
- overall geometric mean: 1.00x slower
- HPT reliability: 82.62%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240701-darwin-arm64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240701-darwin-arm64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 177 ms                                                                | 181 ms: 1.03x slower                                                     |
| docutils       | 1.58 sec                                                              | 1.52 sec: 1.04x faster                                                   |
| html5lib       | 30.7 ms                                                               | 31.6 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                             |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240701-darwin-arm64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240701-darwin-arm64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_eager_tg        | 42.1 ms                                                               | 41.9 ms: 1.00x faster                                                    |
| async_tree_cpu_io_mixed_tg | 447 ms                                                                | 449 ms: 1.00x slower                                                     |
| async_tree_eager           | 64.7 ms                                                               | 66.0 ms: 1.02x slower                                                    |
| async_tree_io              | 508 ms                                                                | 529 ms: 1.04x slower                                                     |
| Geometric mean             | (ref)                                                                 | 1.00x slower                                                             |

Benchmark hidden because not significant (12): async_tree_io_tg, async_tree_eager_memoization_tg, async_tree_memoization, async_tree_eager_io, async_tree_none, async_tree_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_cpu_io_mixed, async_tree_memoization_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240701-darwin-arm64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240701-darwin-arm64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 47.2 ms                                                               | 47.1 ms: 1.00x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                             |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240701-darwin-arm64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240701-darwin-arm64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 150 ms                                                                | 150 ms: 1.00x faster                                                     |
| regex_effbot   | 2.57 ms                                                               | 2.59 ms: 1.00x slower                                                    |
| regex_v8       | 17.2 ms                                                               | 17.4 ms: 1.01x slower                                                    |
| regex_compile  | 73.6 ms                                                               | 74.3 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240701-darwin-arm64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240701-darwin-arm64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                                | 124 us: 1.08x faster                                                     |
| xml_etree_iterparse  | 72.0 ms                                                               | 71.2 ms: 1.01x faster                                                    |
| xml_etree_process    | 36.2 ms                                                               | 36.0 ms: 1.00x faster                                                    |
| json_loads           | 17.3 us                                                               | 17.2 us: 1.00x faster                                                    |
| json_dumps           | 6.43 ms                                                               | 6.45 ms: 1.00x slower                                                    |
| pickle_pure_python   | 174 us                                                                | 176 us: 1.01x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (3): xml_etree_parse, tomli_loads, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240701-darwin-arm64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240701-darwin-arm64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 20.7 ms                                                               | 21.0 ms: 1.02x slower                                                    |
| python_startup_no_site | 14.1 ms                                                               | 14.5 ms: 1.03x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.03x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240701-darwin-arm64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240701-darwin-arm64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 40.7 ms                                                               | 39.3 ms: 1.04x faster                                                    |
| genshi_text     | 16.6 ms                                                               | 16.3 ms: 1.01x faster                                                    |
| mako            | 6.54 ms                                                               | 6.50 ms: 1.01x faster                                                    |
| django_template | 21.3 ms                                                               | 21.5 ms: 1.01x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20240701-darwin-arm64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240701-darwin-arm64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python       | 133 us                                                                | 124 us: 1.08x faster                                                     |
| richards_super             | 34.1 ms                                                               | 32.5 ms: 1.05x faster                                                    |
| richards                   | 30.6 ms                                                               | 29.1 ms: 1.05x faster                                                    |
| genshi_xml                 | 40.7 ms                                                               | 39.3 ms: 1.04x faster                                                    |
| docutils                   | 1.58 sec                                                              | 1.52 sec: 1.04x faster                                                   |
| pprint_safe_repr           | 485 ms                                                                | 473 ms: 1.02x faster                                                     |
| deepcopy_reduce            | 1.57 us                                                               | 1.53 us: 1.02x faster                                                    |
| pprint_pformat             | 996 ms                                                                | 976 ms: 1.02x faster                                                     |
| genshi_text                | 16.6 ms                                                               | 16.3 ms: 1.01x faster                                                    |
| xml_etree_iterparse        | 72.0 ms                                                               | 71.2 ms: 1.01x faster                                                    |
| scimark_monte_carlo        | 44.6 ms                                                               | 44.2 ms: 1.01x faster                                                    |
| typing_runtime_protocols   | 98.4 us                                                               | 97.5 us: 1.01x faster                                                    |
| deepcopy                   | 152 us                                                                | 151 us: 1.01x faster                                                     |
| bpe_tokeniser              | 3.14 sec                                                              | 3.12 sec: 1.01x faster                                                   |
| thrift                     | 437 us                                                                | 435 us: 1.01x faster                                                     |
| mako                       | 6.54 ms                                                               | 6.50 ms: 1.01x faster                                                    |
| async_tree_eager_tg        | 42.1 ms                                                               | 41.9 ms: 1.00x faster                                                    |
| xml_etree_process          | 36.2 ms                                                               | 36.0 ms: 1.00x faster                                                    |
| json_loads                 | 17.3 us                                                               | 17.2 us: 1.00x faster                                                    |
| sympy_str                  | 140 ms                                                                | 139 ms: 1.00x faster                                                     |
| coroutines                 | 16.2 ms                                                               | 16.2 ms: 1.00x faster                                                    |
| telco                      | 4.55 ms                                                               | 4.54 ms: 1.00x faster                                                    |
| float                      | 47.2 ms                                                               | 47.1 ms: 1.00x faster                                                    |
| spectral_norm              | 68.9 ms                                                               | 68.7 ms: 1.00x faster                                                    |
| regex_dna                  | 150 ms                                                                | 150 ms: 1.00x faster                                                     |
| create_gc_cycles           | 903 us                                                                | 906 us: 1.00x slower                                                     |
| scimark_fft                | 191 ms                                                                | 191 ms: 1.00x slower                                                     |
| json_dumps                 | 6.43 ms                                                               | 6.45 ms: 1.00x slower                                                    |
| async_tree_cpu_io_mixed_tg | 447 ms                                                                | 449 ms: 1.00x slower                                                     |
| regex_effbot               | 2.57 ms                                                               | 2.59 ms: 1.00x slower                                                    |
| sqlglot_parse              | 828 us                                                                | 833 us: 1.01x slower                                                     |
| chaos                      | 39.6 ms                                                               | 39.8 ms: 1.01x slower                                                    |
| sqlglot_normalize          | 178 ms                                                                | 180 ms: 1.01x slower                                                     |
| logging_silent             | 62.0 ns                                                               | 62.4 ns: 1.01x slower                                                    |
| logging_format             | 3.36 us                                                               | 3.39 us: 1.01x slower                                                    |
| pickle_pure_python         | 174 us                                                                | 176 us: 1.01x slower                                                     |
| nqueens                    | 58.1 ms                                                               | 58.6 ms: 1.01x slower                                                    |
| scimark_sor                | 102 ms                                                                | 103 ms: 1.01x slower                                                     |
| regex_v8                   | 17.2 ms                                                               | 17.4 ms: 1.01x slower                                                    |
| regex_compile              | 73.6 ms                                                               | 74.3 ms: 1.01x slower                                                    |
| sympy_sum                  | 73.6 ms                                                               | 74.4 ms: 1.01x slower                                                    |
| sympy_expand               | 240 ms                                                                | 243 ms: 1.01x slower                                                     |
| raytrace                   | 163 ms                                                                | 165 ms: 1.01x slower                                                     |
| sqlglot_transpile          | 994 us                                                                | 1.01 ms: 1.01x slower                                                    |
| django_template            | 21.3 ms                                                               | 21.5 ms: 1.01x slower                                                    |
| hexiom                     | 4.43 ms                                                               | 4.48 ms: 1.01x slower                                                    |
| go                         | 101 ms                                                                | 102 ms: 1.01x slower                                                     |
| sqlglot_optimize           | 33.3 ms                                                               | 33.8 ms: 1.01x slower                                                    |
| python_startup             | 20.7 ms                                                               | 21.0 ms: 1.02x slower                                                    |
| async_tree_eager           | 64.7 ms                                                               | 66.0 ms: 1.02x slower                                                    |
| fannkuch                   | 245 ms                                                                | 249 ms: 1.02x slower                                                     |
| 2to3                       | 177 ms                                                                | 181 ms: 1.03x slower                                                     |
| html5lib                   | 30.7 ms                                                               | 31.6 ms: 1.03x slower                                                    |
| deltablue                  | 2.32 ms                                                               | 2.39 ms: 1.03x slower                                                    |
| python_startup_no_site     | 14.1 ms                                                               | 14.5 ms: 1.03x slower                                                    |
| async_tree_io              | 508 ms                                                                | 529 ms: 1.04x slower                                                     |
| Geometric mean             | (ref)                                                                 | 1.00x slower                                                             |

Benchmark hidden because not significant (42): async_tree_io_tg, tornado_http, xml_etree_parse, json, pathlib, nbody, async_tree_eager_memoization_tg, deepcopy_memo, meteor_contest, crypto_pyaes, scimark_sparse_mat_mult, tomli_loads, async_tree_memoization, async_tree_eager_io, async_tree_none, async_tree_cpu_io_mixed, comprehensions, async_tree_eager_cpu_io_mixed_tg, asyncio_websockets, pidigits, async_tree_eager_io_tg, xml_etree_generate, mdp, gc_traversal, logging_simple, bench_thread_pool, async_tree_eager_memoization, pyflate, async_generators, scimark_lu, async_tree_eager_cpu_io_mixed, generators, async_tree_memoization_tg, sympy_integrate, asyncio_tcp_ssl, pycparser, coverage, async_tree_none_tg, dask, pylint, bench_mp_pool, asyncio_tcp

# HPT report

- Reliability score: 82.62% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.04x