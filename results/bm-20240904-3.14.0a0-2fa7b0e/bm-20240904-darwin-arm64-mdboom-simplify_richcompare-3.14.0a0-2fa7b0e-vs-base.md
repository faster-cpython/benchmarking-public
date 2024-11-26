# Results vs. base

- fork: mdboom
- ref: simplify_richcompare
- machine: darwin-arm64
- commit hash: 2fa7b0e
- commit date: 2024-09-04
- overall geometric mean: 1.002x slower
- HPT reliability: 85.26%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark           | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|---------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_tg | 42.1 ms                                                               | 41.8 ms: 1.01x faster                                                 |
| coroutines          | 16.2 ms                                                               | 16.1 ms: 1.01x faster                                                 |
| async_tree_io       | 594 ms                                                                | 597 ms: 1.00x slower                                                  |
| Geometric mean      | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (18): asyncio_tcp, async_tree_none, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_memoization_tg, async_tree_eager_io_tg, async_tree_none_tg, async_tree_eager, async_tree_eager_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_eager_cpu_io_mixed, async_tree_eager_memoization, asyncio_websockets, async_tree_memoization, async_generators, async_tree_eager_io, asyncio_tcp_ssl, async_tree_io_tg

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.50 ms                                                               | 2.46 ms: 1.02x faster                                                 |
| regex_v8       | 16.6 ms                                                               | 16.5 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                          |

Benchmark hidden because not significant (2): regex_compile, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|--------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_loads         | 17.1 us                                                               | 17.2 us: 1.01x slower                                                 |
| xml_etree_generate | 53.5 ms                                                               | 53.9 ms: 1.01x slower                                                 |
| json_dumps         | 6.38 ms                                                               | 6.44 ms: 1.01x slower                                                 |
| pickle_pure_python | 182 us                                                                | 183 us: 1.01x slower                                                  |
| xml_etree_process  | 37.5 ms                                                               | 37.9 ms: 1.01x slower                                                 |
| Geometric mean     | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (4): unpickle_pure_python, tomli_loads, xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 13.6 ms                                                               | 13.5 ms: 1.01x faster                                                 |
| python_startup         | 16.5 ms                                                               | 16.6 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 13.9 ms                                                               | 13.8 ms: 1.01x faster                                                 |
| genshi_xml      | 30.3 ms                                                               | 30.4 ms: 1.00x slower                                                 |
| django_template | 19.9 ms                                                               | 20.0 ms: 1.01x slower                                                 |
| mako            | 6.94 ms                                                               | 7.10 ms: 1.02x slower                                                 |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                          |

All benchmarks:
===============

| Benchmark                | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| generators               | 20.8 ms                                                               | 20.4 ms: 1.02x faster                                                 |
| regex_effbot             | 2.50 ms                                                               | 2.46 ms: 1.02x faster                                                 |
| telco                    | 4.82 ms                                                               | 4.75 ms: 1.02x faster                                                 |
| richards_super           | 35.4 ms                                                               | 35.1 ms: 1.01x faster                                                 |
| scimark_sparse_mat_mult  | 2.79 ms                                                               | 2.77 ms: 1.01x faster                                                 |
| python_startup_no_site   | 13.6 ms                                                               | 13.5 ms: 1.01x faster                                                 |
| async_tree_eager_tg      | 42.1 ms                                                               | 41.8 ms: 1.01x faster                                                 |
| richards                 | 31.5 ms                                                               | 31.3 ms: 1.01x faster                                                 |
| coroutines               | 16.2 ms                                                               | 16.1 ms: 1.01x faster                                                 |
| genshi_text              | 13.9 ms                                                               | 13.8 ms: 1.01x faster                                                 |
| regex_v8                 | 16.6 ms                                                               | 16.5 ms: 1.00x faster                                                 |
| scimark_fft              | 185 ms                                                                | 184 ms: 1.00x faster                                                  |
| thrift                   | 422 us                                                                | 421 us: 1.00x faster                                                  |
| scimark_sor              | 93.1 ms                                                               | 92.8 ms: 1.00x faster                                                 |
| fannkuch                 | 262 ms                                                                | 261 ms: 1.00x faster                                                  |
| go                       | 79.1 ms                                                               | 79.0 ms: 1.00x faster                                                 |
| nqueens                  | 53.1 ms                                                               | 53.3 ms: 1.00x slower                                                 |
| sqlglot_parse            | 738 us                                                                | 741 us: 1.00x slower                                                  |
| deepcopy_reduce          | 1.50 us                                                               | 1.51 us: 1.00x slower                                                 |
| chaos                    | 35.7 ms                                                               | 35.8 ms: 1.00x slower                                                 |
| async_tree_io            | 594 ms                                                                | 597 ms: 1.00x slower                                                  |
| genshi_xml               | 30.3 ms                                                               | 30.4 ms: 1.00x slower                                                 |
| logging_silent           | 60.9 ns                                                               | 61.1 ns: 1.00x slower                                                 |
| pprint_pformat           | 928 ms                                                                | 932 ms: 1.00x slower                                                  |
| scimark_monte_carlo      | 43.1 ms                                                               | 43.3 ms: 1.00x slower                                                 |
| crypto_pyaes             | 50.6 ms                                                               | 50.9 ms: 1.01x slower                                                 |
| django_template          | 19.9 ms                                                               | 20.0 ms: 1.01x slower                                                 |
| python_startup           | 16.5 ms                                                               | 16.6 ms: 1.01x slower                                                 |
| spectral_norm            | 67.0 ms                                                               | 67.4 ms: 1.01x slower                                                 |
| hexiom                   | 4.07 ms                                                               | 4.09 ms: 1.01x slower                                                 |
| bpe_tokeniser            | 3.13 sec                                                              | 3.15 sec: 1.01x slower                                                |
| json_loads               | 17.1 us                                                               | 17.2 us: 1.01x slower                                                 |
| logging_simple           | 3.08 us                                                               | 3.10 us: 1.01x slower                                                 |
| sqlglot_transpile        | 897 us                                                                | 903 us: 1.01x slower                                                  |
| xml_etree_generate       | 53.5 ms                                                               | 53.9 ms: 1.01x slower                                                 |
| json_dumps               | 6.38 ms                                                               | 6.44 ms: 1.01x slower                                                 |
| pickle_pure_python       | 182 us                                                                | 183 us: 1.01x slower                                                  |
| dulwich_log              | 27.0 ms                                                               | 27.2 ms: 1.01x slower                                                 |
| sympy_str                | 131 ms                                                                | 132 ms: 1.01x slower                                                  |
| deepcopy_memo            | 16.5 us                                                               | 16.6 us: 1.01x slower                                                 |
| pyflate                  | 320 ms                                                                | 324 ms: 1.01x slower                                                  |
| comprehensions           | 9.95 us                                                               | 10.1 us: 1.01x slower                                                 |
| deepcopy                 | 144 us                                                                | 145 us: 1.01x slower                                                  |
| sympy_expand             | 226 ms                                                                | 228 ms: 1.01x slower                                                  |
| xml_etree_process        | 37.5 ms                                                               | 37.9 ms: 1.01x slower                                                 |
| typing_runtime_protocols | 91.3 us                                                               | 92.6 us: 1.01x slower                                                 |
| logging_format           | 3.39 us                                                               | 3.44 us: 1.02x slower                                                 |
| scimark_lu               | 66.6 ms                                                               | 67.8 ms: 1.02x slower                                                 |
| mako                     | 6.94 ms                                                               | 7.10 ms: 1.02x slower                                                 |
| pathlib                  | 23.5 ms                                                               | 24.1 ms: 1.02x slower                                                 |
| meteor_contest           | 72.2 ms                                                               | 74.2 ms: 1.03x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (47): asyncio_tcp, async_tree_none, async_tree_memoization_tg, unpickle_pure_python, async_tree_cpu_io_mixed_tg, tornado_http, async_tree_eager_memoization_tg, gc_traversal, tomli_loads, async_tree_eager_io_tg, async_tree_none_tg, pycparser, async_tree_eager, json, async_tree_eager_cpu_io_mixed_tg, docutils, deltablue, async_tree_cpu_io_mixed, async_tree_eager_cpu_io_mixed, mdp, nbody, regex_compile, pprint_safe_repr, async_tree_eager_memoization, asyncio_websockets, bench_thread_pool, async_tree_memoization, regex_dna, raytrace, pidigits, sympy_integrate, create_gc_cycles, bench_mp_pool, 2to3, async_generators, xml_etree_iterparse, sqlglot_normalize, async_tree_eager_io, coverage, pylint, float, html5lib, xml_etree_parse, sqlglot_optimize, asyncio_tcp_ssl, sympy_sum, async_tree_io_tg

- Geometric mean (including insignificant results): 1.002x slower
# HPT report

- Reliability score: 85.26% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x