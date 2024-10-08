# Results vs. base

- fork: mdboom
- ref: simplify_richcompare
- machine: darwin-arm64
- commit hash: 2fa7b0e
- commit date: 2024-09-04
- overall geometric mean: 1.00x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 187 ms                                                                | 160 ms: 1.17x faster                                                  |
| docutils       | 1.45 sec                                                              | 1.45 sec: 1.00x slower                                                |
| html5lib       | 29.9 ms                                                               | 30.1 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| coroutines       | 16.1 ms                                                               | 16.1 ms: 1.00x slower                                                 |
| async_tree_io    | 594 ms                                                                | 597 ms: 1.00x slower                                                  |
| async_generators | 279 ms                                                                | 282 ms: 1.01x slower                                                  |
| Geometric mean   | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (18): async_tree_eager_cpu_io_mixed, async_tree_none, async_tree_memoization_tg, async_tree_eager_tg, async_tree_cpu_io_mixed_tg, asyncio_tcp_ssl, async_tree_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_memoization_tg, asyncio_websockets, async_tree_memoization, async_tree_none_tg, async_tree_eager, async_tree_eager_io, async_tree_eager_memoization, async_tree_eager_io_tg, asyncio_tcp, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 281 ms                                                                | 282 ms: 1.00x slower                                                  |
| float          | 48.5 ms                                                               | 48.7 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.48 ms                                                               | 2.46 ms: 1.01x faster                                                 |
| regex_dna      | 147 ms                                                                | 146 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (2): regex_v8, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|--------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps         | 6.40 ms                                                               | 6.44 ms: 1.01x slower                                                 |
| pickle_pure_python | 182 us                                                                | 183 us: 1.01x slower                                                  |
| xml_etree_process  | 37.5 ms                                                               | 37.9 ms: 1.01x slower                                                 |
| xml_etree_generate | 53.3 ms                                                               | 53.9 ms: 1.01x slower                                                 |
| Geometric mean     | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (5): unpickle_pure_python, json_loads, xml_etree_iterparse, tomli_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 13.8 ms                                                               | 13.5 ms: 1.02x faster                                                 |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                          |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 13.9 ms                                                               | 13.8 ms: 1.01x faster                                                 |
| genshi_xml      | 30.3 ms                                                               | 30.4 ms: 1.00x slower                                                 |
| django_template | 19.9 ms                                                               | 20.0 ms: 1.00x slower                                                 |
| mako            | 6.96 ms                                                               | 7.10 ms: 1.02x slower                                                 |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                          |

All benchmarks:
===============

| Benchmark                | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3                     | 187 ms                                                                | 160 ms: 1.17x faster                                                  |
| python_startup_no_site   | 13.8 ms                                                               | 13.5 ms: 1.02x faster                                                 |
| telco                    | 4.82 ms                                                               | 4.75 ms: 1.01x faster                                                 |
| mdp                      | 1.44 sec                                                              | 1.43 sec: 1.01x faster                                                |
| regex_effbot             | 2.48 ms                                                               | 2.46 ms: 1.01x faster                                                 |
| regex_dna                | 147 ms                                                                | 146 ms: 1.01x faster                                                  |
| fannkuch                 | 263 ms                                                                | 261 ms: 1.01x faster                                                  |
| genshi_text              | 13.9 ms                                                               | 13.8 ms: 1.01x faster                                                 |
| richards_super           | 35.2 ms                                                               | 35.1 ms: 1.01x faster                                                 |
| scimark_sparse_mat_mult  | 2.78 ms                                                               | 2.77 ms: 1.01x faster                                                 |
| scimark_sor              | 93.2 ms                                                               | 92.8 ms: 1.00x faster                                                 |
| generators               | 20.4 ms                                                               | 20.4 ms: 1.00x faster                                                 |
| pprint_safe_repr         | 454 ms                                                                | 453 ms: 1.00x faster                                                  |
| richards                 | 31.4 ms                                                               | 31.3 ms: 1.00x faster                                                 |
| go                       | 79.2 ms                                                               | 79.0 ms: 1.00x faster                                                 |
| scimark_fft              | 184 ms                                                                | 184 ms: 1.00x faster                                                  |
| pidigits                 | 281 ms                                                                | 282 ms: 1.00x slower                                                  |
| coroutines               | 16.1 ms                                                               | 16.1 ms: 1.00x slower                                                 |
| thrift                   | 420 us                                                                | 421 us: 1.00x slower                                                  |
| logging_simple           | 3.09 us                                                               | 3.10 us: 1.00x slower                                                 |
| crypto_pyaes             | 50.7 ms                                                               | 50.9 ms: 1.00x slower                                                 |
| logging_silent           | 60.9 ns                                                               | 61.1 ns: 1.00x slower                                                 |
| pprint_pformat           | 929 ms                                                                | 932 ms: 1.00x slower                                                  |
| docutils                 | 1.45 sec                                                              | 1.45 sec: 1.00x slower                                                |
| float                    | 48.5 ms                                                               | 48.7 ms: 1.00x slower                                                 |
| genshi_xml               | 30.3 ms                                                               | 30.4 ms: 1.00x slower                                                 |
| spectral_norm            | 67.2 ms                                                               | 67.4 ms: 1.00x slower                                                 |
| sympy_integrate          | 10.3 ms                                                               | 10.3 ms: 1.00x slower                                                 |
| gc_traversal             | 2.45 ms                                                               | 2.46 ms: 1.00x slower                                                 |
| django_template          | 19.9 ms                                                               | 20.0 ms: 1.00x slower                                                 |
| async_tree_io            | 594 ms                                                                | 597 ms: 1.00x slower                                                  |
| deepcopy_memo            | 16.6 us                                                               | 16.6 us: 1.00x slower                                                 |
| sympy_sum                | 68.7 ms                                                               | 69.0 ms: 1.01x slower                                                 |
| sqlglot_parse            | 737 us                                                                | 741 us: 1.01x slower                                                  |
| json_dumps               | 6.40 ms                                                               | 6.44 ms: 1.01x slower                                                 |
| chaos                    | 35.6 ms                                                               | 35.8 ms: 1.01x slower                                                 |
| html5lib                 | 29.9 ms                                                               | 30.1 ms: 1.01x slower                                                 |
| sqlglot_optimize         | 31.1 ms                                                               | 31.3 ms: 1.01x slower                                                 |
| pickle_pure_python       | 182 us                                                                | 183 us: 1.01x slower                                                  |
| sqlglot_transpile        | 897 us                                                                | 903 us: 1.01x slower                                                  |
| create_gc_cycles         | 892 us                                                                | 899 us: 1.01x slower                                                  |
| sympy_str                | 131 ms                                                                | 132 ms: 1.01x slower                                                  |
| logging_format           | 3.41 us                                                               | 3.44 us: 1.01x slower                                                 |
| bpe_tokeniser            | 3.12 sec                                                              | 3.15 sec: 1.01x slower                                                |
| async_generators         | 279 ms                                                                | 282 ms: 1.01x slower                                                  |
| bench_mp_pool            | 48.4 ms                                                               | 48.9 ms: 1.01x slower                                                 |
| hexiom                   | 4.05 ms                                                               | 4.09 ms: 1.01x slower                                                 |
| xml_etree_process        | 37.5 ms                                                               | 37.9 ms: 1.01x slower                                                 |
| sympy_expand             | 226 ms                                                                | 228 ms: 1.01x slower                                                  |
| pyflate                  | 320 ms                                                                | 324 ms: 1.01x slower                                                  |
| deepcopy                 | 143 us                                                                | 145 us: 1.01x slower                                                  |
| comprehensions           | 9.93 us                                                               | 10.1 us: 1.01x slower                                                 |
| xml_etree_generate       | 53.3 ms                                                               | 53.9 ms: 1.01x slower                                                 |
| dulwich_log              | 26.8 ms                                                               | 27.2 ms: 1.01x slower                                                 |
| scimark_lu               | 66.7 ms                                                               | 67.8 ms: 1.02x slower                                                 |
| pathlib                  | 23.6 ms                                                               | 24.1 ms: 1.02x slower                                                 |
| typing_runtime_protocols | 90.8 us                                                               | 92.6 us: 1.02x slower                                                 |
| mako                     | 6.96 ms                                                               | 7.10 ms: 1.02x slower                                                 |
| bench_thread_pool        | 436 us                                                                | 450 us: 1.03x slower                                                  |
| meteor_contest           | 71.5 ms                                                               | 74.2 ms: 1.04x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (38): async_tree_eager_cpu_io_mixed, unpickle_pure_python, async_tree_none, async_tree_memoization_tg, async_tree_eager_tg, json_loads, xml_etree_iterparse, async_tree_cpu_io_mixed_tg, asyncio_tcp_ssl, async_tree_cpu_io_mixed, deepcopy_reduce, json, nqueens, async_tree_eager_cpu_io_mixed_tg, scimark_monte_carlo, raytrace, async_tree_eager_memoization_tg, asyncio_websockets, nbody, regex_v8, deltablue, pycparser, coverage, async_tree_memoization, async_tree_none_tg, sqlglot_normalize, async_tree_eager, async_tree_eager_io, regex_compile, tomli_loads, async_tree_eager_memoization, xml_etree_parse, async_tree_eager_io_tg, python_startup, asyncio_tcp, pylint, tornado_http, async_tree_io_tg

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x