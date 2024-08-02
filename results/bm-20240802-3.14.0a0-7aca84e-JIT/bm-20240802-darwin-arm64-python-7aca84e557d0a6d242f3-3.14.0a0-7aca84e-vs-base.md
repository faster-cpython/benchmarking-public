# Results vs. base

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: darwin-arm64
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.00x slower
- HPT reliability: 60.57%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark           | bm-20240802-darwin-arm64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|---------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| coroutines          | 16.2 ms                                                               | 16.1 ms: 1.00x faster                                                 |
| async_tree_eager_tg | 42.0 ms                                                               | 43.1 ms: 1.03x slower                                                 |
| async_tree_eager    | 62.2 ms                                                               | 64.0 ms: 1.03x slower                                                 |
| Geometric mean      | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (18): asyncio_tcp_ssl, async_tree_io, async_tree_memoization_tg, async_tree_none_tg, async_tree_eager_io_tg, async_tree_memoization, async_tree_io_tg, async_generators, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_eager_memoization_tg, async_tree_eager_io, async_tree_cpu_io_mixed, async_tree_none, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed, async_tree_eager_memoization, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240802-darwin-arm64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 62.8 ms                                                               | 62.7 ms: 1.00x faster                                                 |
| pidigits       | 282 ms                                                                | 281 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240802-darwin-arm64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 71.5 ms                                                               | 71.2 ms: 1.00x faster                                                 |
| regex_v8       | 17.2 ms                                                               | 17.2 ms: 1.00x slower                                                 |
| regex_effbot   | 2.57 ms                                                               | 2.58 ms: 1.01x slower                                                 |
| regex_dna      | 149 ms                                                                | 153 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240802-darwin-arm64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|--------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_generate | 51.9 ms                                                               | 51.7 ms: 1.00x faster                                                 |
| json_dumps         | 6.37 ms                                                               | 6.35 ms: 1.00x faster                                                 |
| json_loads         | 17.2 us                                                               | 17.3 us: 1.00x slower                                                 |
| tomli_loads        | 1.24 sec                                                              | 1.25 sec: 1.01x slower                                                |
| Geometric mean     | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (5): unpickle_pure_python, xml_etree_parse, xml_etree_process, pickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240802-darwin-arm64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                               | 13.1 ms: 1.05x faster                                                 |
| python_startup         | 16.7 ms                                                               | 16.1 ms: 1.04x faster                                                 |
| Geometric mean         | (ref)                                                                 | 1.04x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240802-darwin-arm64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 35.1 ms                                                               | 34.9 ms: 1.01x faster                                                 |
| django_template | 21.6 ms                                                               | 21.6 ms: 1.00x faster                                                 |
| genshi_text     | 14.7 ms                                                               | 14.7 ms: 1.00x slower                                                 |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20240802-darwin-arm64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site   | 13.7 ms                                                               | 13.1 ms: 1.05x faster                                                 |
| python_startup           | 16.7 ms                                                               | 16.1 ms: 1.04x faster                                                 |
| richards_super           | 35.1 ms                                                               | 34.2 ms: 1.03x faster                                                 |
| pprint_pformat           | 1000 ms                                                               | 982 ms: 1.02x faster                                                  |
| deepcopy_reduce          | 1.57 us                                                               | 1.54 us: 1.02x faster                                                 |
| pprint_safe_repr         | 489 ms                                                                | 483 ms: 1.01x faster                                                  |
| meteor_contest           | 71.7 ms                                                               | 71.0 ms: 1.01x faster                                                 |
| json                     | 2.94 ms                                                               | 2.91 ms: 1.01x faster                                                 |
| genshi_xml               | 35.1 ms                                                               | 34.9 ms: 1.01x faster                                                 |
| sympy_integrate          | 11.3 ms                                                               | 11.3 ms: 1.01x faster                                                 |
| thrift                   | 436 us                                                                | 433 us: 1.01x faster                                                  |
| logging_silent           | 61.3 ns                                                               | 61.0 ns: 1.01x faster                                                 |
| fannkuch                 | 250 ms                                                                | 249 ms: 1.01x faster                                                  |
| coverage                 | 44.9 ms                                                               | 44.7 ms: 1.01x faster                                                 |
| regex_compile            | 71.5 ms                                                               | 71.2 ms: 1.00x faster                                                 |
| bpe_tokeniser            | 3.02 sec                                                              | 3.01 sec: 1.00x faster                                                |
| xml_etree_generate       | 51.9 ms                                                               | 51.7 ms: 1.00x faster                                                 |
| raytrace                 | 161 ms                                                                | 160 ms: 1.00x faster                                                  |
| json_dumps               | 6.37 ms                                                               | 6.35 ms: 1.00x faster                                                 |
| sympy_str                | 142 ms                                                                | 142 ms: 1.00x faster                                                  |
| logging_format           | 3.32 us                                                               | 3.30 us: 1.00x faster                                                 |
| comprehensions           | 12.2 us                                                               | 12.2 us: 1.00x faster                                                 |
| create_gc_cycles         | 907 us                                                                | 904 us: 1.00x faster                                                  |
| richards                 | 31.0 ms                                                               | 30.9 ms: 1.00x faster                                                 |
| coroutines               | 16.2 ms                                                               | 16.1 ms: 1.00x faster                                                 |
| spectral_norm            | 68.5 ms                                                               | 68.3 ms: 1.00x faster                                                 |
| django_template          | 21.6 ms                                                               | 21.6 ms: 1.00x faster                                                 |
| nbody                    | 62.8 ms                                                               | 62.7 ms: 1.00x faster                                                 |
| pidigits                 | 282 ms                                                                | 281 ms: 1.00x faster                                                  |
| pyflate                  | 313 ms                                                                | 313 ms: 1.00x slower                                                  |
| scimark_sor              | 88.2 ms                                                               | 88.4 ms: 1.00x slower                                                 |
| hexiom                   | 4.42 ms                                                               | 4.43 ms: 1.00x slower                                                 |
| genshi_text              | 14.7 ms                                                               | 14.7 ms: 1.00x slower                                                 |
| regex_v8                 | 17.2 ms                                                               | 17.2 ms: 1.00x slower                                                 |
| crypto_pyaes             | 51.4 ms                                                               | 51.6 ms: 1.00x slower                                                 |
| json_loads               | 17.2 us                                                               | 17.3 us: 1.00x slower                                                 |
| deltablue                | 2.31 ms                                                               | 2.32 ms: 1.01x slower                                                 |
| go                       | 101 ms                                                                | 101 ms: 1.01x slower                                                  |
| regex_effbot             | 2.57 ms                                                               | 2.58 ms: 1.01x slower                                                 |
| dulwich_log              | 28.0 ms                                                               | 28.2 ms: 1.01x slower                                                 |
| tomli_loads              | 1.24 sec                                                              | 1.25 sec: 1.01x slower                                                |
| sqlglot_optimize         | 33.0 ms                                                               | 33.4 ms: 1.01x slower                                                 |
| deepcopy                 | 153 us                                                                | 154 us: 1.01x slower                                                  |
| typing_runtime_protocols | 96.7 us                                                               | 97.8 us: 1.01x slower                                                 |
| sqlglot_normalize        | 176 ms                                                                | 179 ms: 1.02x slower                                                  |
| scimark_lu               | 65.0 ms                                                               | 66.2 ms: 1.02x slower                                                 |
| pycparser                | 671 ms                                                                | 684 ms: 1.02x slower                                                  |
| deepcopy_memo            | 16.8 us                                                               | 17.2 us: 1.02x slower                                                 |
| regex_dna                | 149 ms                                                                | 153 ms: 1.03x slower                                                  |
| async_tree_eager_tg      | 42.0 ms                                                               | 43.1 ms: 1.03x slower                                                 |
| async_tree_eager         | 62.2 ms                                                               | 64.0 ms: 1.03x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (48): bench_mp_pool, asyncio_tcp_ssl, pathlib, unpickle_pure_python, sqlglot_parse, async_tree_io, float, logging_simple, xml_etree_parse, sympy_sum, async_tree_memoization_tg, scimark_monte_carlo, gc_traversal, scimark_fft, async_tree_none_tg, async_tree_eager_io_tg, pylint, 2to3, telco, async_tree_memoization, xml_etree_process, scimark_sparse_mat_mult, docutils, async_tree_io_tg, async_generators, chaos, mdp, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_eager_memoization_tg, async_tree_eager_io, dask, nqueens, html5lib, async_tree_cpu_io_mixed, sympy_expand, generators, async_tree_none, mako, bench_thread_pool, pickle_pure_python, async_tree_eager_cpu_io_mixed_tg, sqlglot_transpile, xml_etree_iterparse, async_tree_eager_cpu_io_mixed, tornado_http, async_tree_eager_memoization, asyncio_tcp

# HPT report

- Reliability score: 60.57% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x