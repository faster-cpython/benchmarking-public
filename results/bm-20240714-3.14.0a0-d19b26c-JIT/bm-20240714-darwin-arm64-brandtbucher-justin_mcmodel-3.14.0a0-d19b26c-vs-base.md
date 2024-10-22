# Results vs. base

- fork: brandtbucher
- ref: justin_mcmodel
- machine: darwin-arm64
- commit hash: d19b26c
- commit date: 2024-07-14
- overall geometric mean: 1.00x slower
- HPT reliability: 63.55%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-darwin-arm64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 171 ms                                                                | 172 ms: 1.01x slower                                                  |
| docutils       | 1.52 sec                                                              | 1.51 sec: 1.00x faster                                                |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark           | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-darwin-arm64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|---------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager    | 63.6 ms                                                               | 64.2 ms: 1.01x slower                                                 |
| async_tree_eager_tg | 41.2 ms                                                               | 41.7 ms: 1.01x slower                                                 |
| Geometric mean      | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (14): async_tree_io, async_tree_memoization, async_tree_eager_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_eager_cpu_io_mixed, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_io, async_tree_io_tg, async_tree_eager_io_tg, async_tree_memoization_tg, async_tree_eager_memoization_tg, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-darwin-arm64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 47.2 ms                                                               | 47.4 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-darwin-arm64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 73.5 ms                                                               | 72.9 ms: 1.01x faster                                                 |
| regex_dna      | 150 ms                                                                | 149 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-darwin-arm64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|---------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_iterparse | 71.3 ms                                                               | 70.7 ms: 1.01x faster                                                 |
| json_dumps          | 6.39 ms                                                               | 6.41 ms: 1.00x slower                                                 |
| json_loads          | 17.3 us                                                               | 17.4 us: 1.00x slower                                                 |
| tomli_loads         | 1.24 sec                                                              | 1.28 sec: 1.03x slower                                                |
| Geometric mean      | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (5): xml_etree_generate, pickle_pure_python, unpickle_pure_python, xml_etree_parse, xml_etree_process

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-darwin-arm64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 6.50 ms                                                               | 6.53 ms: 1.00x slower                                                 |
| genshi_text     | 15.8 ms                                                               | 15.9 ms: 1.01x slower                                                 |
| genshi_xml      | 39.9 ms                                                               | 40.3 ms: 1.01x slower                                                 |
| django_template | 21.8 ms                                                               | 22.2 ms: 1.02x slower                                                 |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                          |

All benchmarks:
===============

| Benchmark                | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-darwin-arm64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| richards                 | 31.1 ms                                                               | 30.7 ms: 1.01x faster                                                 |
| sympy_str                | 140 ms                                                                | 138 ms: 1.01x faster                                                  |
| sympy_sum                | 73.7 ms                                                               | 73.0 ms: 1.01x faster                                                 |
| xml_etree_iterparse      | 71.3 ms                                                               | 70.7 ms: 1.01x faster                                                 |
| deepcopy_reduce          | 1.56 us                                                               | 1.54 us: 1.01x faster                                                 |
| typing_runtime_protocols | 96.7 us                                                               | 95.9 us: 1.01x faster                                                 |
| sqlglot_transpile        | 1.00 ms                                                               | 994 us: 1.01x faster                                                  |
| raytrace                 | 166 ms                                                                | 164 ms: 1.01x faster                                                  |
| regex_compile            | 73.5 ms                                                               | 72.9 ms: 1.01x faster                                                 |
| telco                    | 4.64 ms                                                               | 4.61 ms: 1.01x faster                                                 |
| logging_format           | 3.37 us                                                               | 3.35 us: 1.01x faster                                                 |
| nqueens                  | 57.9 ms                                                               | 57.6 ms: 1.01x faster                                                 |
| regex_dna                | 150 ms                                                                | 149 ms: 1.01x faster                                                  |
| crypto_pyaes             | 52.2 ms                                                               | 51.9 ms: 1.01x faster                                                 |
| docutils                 | 1.52 sec                                                              | 1.51 sec: 1.00x faster                                                |
| sqlglot_parse            | 831 us                                                                | 827 us: 1.00x faster                                                  |
| sympy_expand             | 241 ms                                                                | 240 ms: 1.00x faster                                                  |
| sympy_integrate          | 11.0 ms                                                               | 11.0 ms: 1.00x faster                                                 |
| logging_simple           | 3.04 us                                                               | 3.03 us: 1.00x faster                                                 |
| sqlglot_normalize        | 179 ms                                                                | 178 ms: 1.00x faster                                                  |
| scimark_sparse_mat_mult  | 3.03 ms                                                               | 3.02 ms: 1.00x faster                                                 |
| sqlglot_optimize         | 33.2 ms                                                               | 33.1 ms: 1.00x faster                                                 |
| scimark_monte_carlo      | 43.9 ms                                                               | 43.9 ms: 1.00x faster                                                 |
| logging_silent           | 61.7 ns                                                               | 61.9 ns: 1.00x slower                                                 |
| scimark_sor              | 102 ms                                                                | 102 ms: 1.00x slower                                                  |
| json_dumps               | 6.39 ms                                                               | 6.41 ms: 1.00x slower                                                 |
| float                    | 47.2 ms                                                               | 47.4 ms: 1.00x slower                                                 |
| json_loads               | 17.3 us                                                               | 17.4 us: 1.00x slower                                                 |
| mako                     | 6.50 ms                                                               | 6.53 ms: 1.00x slower                                                 |
| 2to3                     | 171 ms                                                                | 172 ms: 1.01x slower                                                  |
| coverage                 | 45.9 ms                                                               | 46.2 ms: 1.01x slower                                                 |
| genshi_text              | 15.8 ms                                                               | 15.9 ms: 1.01x slower                                                 |
| pprint_pformat           | 989 ms                                                                | 998 ms: 1.01x slower                                                  |
| genshi_xml               | 39.9 ms                                                               | 40.3 ms: 1.01x slower                                                 |
| async_tree_eager         | 63.6 ms                                                               | 64.2 ms: 1.01x slower                                                 |
| mdp                      | 1.45 sec                                                              | 1.47 sec: 1.01x slower                                                |
| async_tree_eager_tg      | 41.2 ms                                                               | 41.7 ms: 1.01x slower                                                 |
| pprint_safe_repr         | 481 ms                                                                | 488 ms: 1.01x slower                                                  |
| fannkuch                 | 244 ms                                                                | 248 ms: 1.02x slower                                                  |
| django_template          | 21.8 ms                                                               | 22.2 ms: 1.02x slower                                                 |
| tomli_loads              | 1.24 sec                                                              | 1.28 sec: 1.03x slower                                                |
| asyncio_tcp              | 398 ms                                                                | 430 ms: 1.08x slower                                                  |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (56): async_tree_io, comprehensions, pylint, html5lib, pyflate, spectral_norm, richards_super, generators, deltablue, bench_thread_pool, async_generators, scimark_fft, pycparser, async_tree_memoization, go, thrift, coroutines, async_tree_eager_cpu_io_mixed_tg, xml_etree_generate, deepcopy, scimark_lu, async_tree_cpu_io_mixed, async_tree_none, pickle_pure_python, gc_traversal, meteor_contest, deepcopy_memo, asyncio_websockets, hexiom, create_gc_cycles, regex_v8, async_tree_eager_cpu_io_mixed, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_io, tornado_http, unpickle_pure_python, dask, xml_etree_parse, bpe_tokeniser, pidigits, nbody, chaos, xml_etree_process, async_tree_io_tg, python_startup, async_tree_eager_io_tg, regex_effbot, async_tree_memoization_tg, python_startup_no_site, async_tree_eager_memoization_tg, bench_mp_pool, pathlib, json, async_tree_eager_memoization, asyncio_tcp_ssl

# HPT report

- Reliability score: 63.55% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.98x