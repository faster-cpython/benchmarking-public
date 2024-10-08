# Results vs. base

- fork: faster-cpython
- ref: experimental_branch_
- machine: darwin-arm64
- commit hash: 1a2b0b8
- commit date: 2024-07-31
- overall geometric mean: 1.01x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240730-darwin-arm64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| docutils       | 1.51 sec                                                              | 1.50 sec: 1.01x faster                                                          |
| html5lib       | 31.5 ms                                                               | 31.6 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark           | bm-20240730-darwin-arm64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|---------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager    | 61.5 ms                                                               | 61.7 ms: 1.00x slower                                                           |
| async_tree_eager_tg | 41.6 ms                                                               | 42.3 ms: 1.02x slower                                                           |
| Geometric mean      | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (19): asyncio_tcp_ssl, async_tree_eager_io, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_memoization_tg, asyncio_websockets, async_generators, async_tree_eager_cpu_io_mixed_tg, coroutines, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none, async_tree_eager_cpu_io_mixed, async_tree_eager_memoization, async_tree_io_tg, async_tree_eager_memoization_tg, async_tree_none_tg, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240730-darwin-arm64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 58.9 ms                                                               | 59.1 ms: 1.00x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240730-darwin-arm64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 151 ms                                                                | 150 ms: 1.01x faster                                                            |
| regex_v8       | 17.5 ms                                                               | 17.4 ms: 1.00x faster                                                           |
| regex_compile  | 68.5 ms                                                               | 69.1 ms: 1.01x slower                                                           |
| regex_effbot   | 2.57 ms                                                               | 2.64 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240730-darwin-arm64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|--------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads        | 1.49 sec                                                              | 1.50 sec: 1.01x slower                                                          |
| json_loads         | 17.2 us                                                               | 17.4 us: 1.01x slower                                                           |
| xml_etree_generate | 53.1 ms                                                               | 53.7 ms: 1.01x slower                                                           |
| json_dumps         | 6.38 ms                                                               | 6.45 ms: 1.01x slower                                                           |
| pickle_pure_python | 182 us                                                                | 185 us: 1.01x slower                                                            |
| xml_etree_process  | 37.4 ms                                                               | 37.9 ms: 1.01x slower                                                           |
| Geometric mean     | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (3): xml_etree_iterparse, unpickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240730-darwin-arm64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 15.4 ms                                                               | 15.5 ms: 1.00x slower                                                           |
| python_startup_no_site | 12.7 ms                                                               | 12.8 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240730-darwin-arm64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 7.08 ms                                                               | 6.98 ms: 1.01x faster                                                           |
| genshi_xml      | 30.3 ms                                                               | 30.5 ms: 1.01x slower                                                           |
| genshi_text     | 14.0 ms                                                               | 14.1 ms: 1.01x slower                                                           |
| django_template | 19.6 ms                                                               | 19.9 ms: 1.01x slower                                                           |
| Geometric mean  | (ref)                                                                 | 1.00x slower                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20240730-darwin-arm64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako                     | 7.08 ms                                                               | 6.98 ms: 1.01x faster                                                           |
| logging_format           | 3.38 us                                                               | 3.35 us: 1.01x faster                                                           |
| regex_dna                | 151 ms                                                                | 150 ms: 1.01x faster                                                            |
| docutils                 | 1.51 sec                                                              | 1.50 sec: 1.01x faster                                                          |
| logging_silent           | 59.8 ns                                                               | 59.5 ns: 1.01x faster                                                           |
| regex_v8                 | 17.5 ms                                                               | 17.4 ms: 1.00x faster                                                           |
| bench_thread_pool        | 452 us                                                                | 453 us: 1.00x slower                                                            |
| chaos                    | 35.6 ms                                                               | 35.7 ms: 1.00x slower                                                           |
| nbody                    | 58.9 ms                                                               | 59.1 ms: 1.00x slower                                                           |
| async_tree_eager         | 61.5 ms                                                               | 61.7 ms: 1.00x slower                                                           |
| scimark_fft              | 186 ms                                                                | 187 ms: 1.00x slower                                                            |
| scimark_lu               | 70.2 ms                                                               | 70.5 ms: 1.00x slower                                                           |
| python_startup           | 15.4 ms                                                               | 15.5 ms: 1.00x slower                                                           |
| richards                 | 31.4 ms                                                               | 31.5 ms: 1.00x slower                                                           |
| thrift                   | 434 us                                                                | 436 us: 1.00x slower                                                            |
| fannkuch                 | 266 ms                                                                | 267 ms: 1.00x slower                                                            |
| mdp                      | 1.44 sec                                                              | 1.44 sec: 1.00x slower                                                          |
| raytrace                 | 148 ms                                                                | 149 ms: 1.00x slower                                                            |
| generators               | 20.5 ms                                                               | 20.6 ms: 1.00x slower                                                           |
| deepcopy                 | 145 us                                                                | 146 us: 1.00x slower                                                            |
| html5lib                 | 31.5 ms                                                               | 31.6 ms: 1.01x slower                                                           |
| tomli_loads              | 1.49 sec                                                              | 1.50 sec: 1.01x slower                                                          |
| scimark_sparse_mat_mult  | 2.82 ms                                                               | 2.84 ms: 1.01x slower                                                           |
| pprint_pformat           | 960 ms                                                                | 967 ms: 1.01x slower                                                            |
| genshi_xml               | 30.3 ms                                                               | 30.5 ms: 1.01x slower                                                           |
| bpe_tokeniser            | 3.11 sec                                                              | 3.13 sec: 1.01x slower                                                          |
| create_gc_cycles         | 899 us                                                                | 906 us: 1.01x slower                                                            |
| sympy_str                | 134 ms                                                                | 135 ms: 1.01x slower                                                            |
| pprint_safe_repr         | 472 ms                                                                | 475 ms: 1.01x slower                                                            |
| genshi_text              | 14.0 ms                                                               | 14.1 ms: 1.01x slower                                                           |
| sqlglot_parse            | 741 us                                                                | 748 us: 1.01x slower                                                            |
| deltablue                | 2.11 ms                                                               | 2.13 ms: 1.01x slower                                                           |
| json_loads               | 17.2 us                                                               | 17.4 us: 1.01x slower                                                           |
| pyflate                  | 321 ms                                                                | 324 ms: 1.01x slower                                                            |
| regex_compile            | 68.5 ms                                                               | 69.1 ms: 1.01x slower                                                           |
| xml_etree_generate       | 53.1 ms                                                               | 53.7 ms: 1.01x slower                                                           |
| sympy_expand             | 228 ms                                                                | 230 ms: 1.01x slower                                                            |
| nqueens                  | 53.3 ms                                                               | 53.8 ms: 1.01x slower                                                           |
| pathlib                  | 23.2 ms                                                               | 23.5 ms: 1.01x slower                                                           |
| crypto_pyaes             | 50.5 ms                                                               | 51.1 ms: 1.01x slower                                                           |
| richards_super           | 34.5 ms                                                               | 34.8 ms: 1.01x slower                                                           |
| deepcopy_memo            | 16.9 us                                                               | 17.1 us: 1.01x slower                                                           |
| django_template          | 19.6 ms                                                               | 19.9 ms: 1.01x slower                                                           |
| spectral_norm            | 66.8 ms                                                               | 67.6 ms: 1.01x slower                                                           |
| json_dumps               | 6.38 ms                                                               | 6.45 ms: 1.01x slower                                                           |
| hexiom                   | 4.08 ms                                                               | 4.12 ms: 1.01x slower                                                           |
| go                       | 97.7 ms                                                               | 98.8 ms: 1.01x slower                                                           |
| sympy_integrate          | 10.4 ms                                                               | 10.5 ms: 1.01x slower                                                           |
| python_startup_no_site   | 12.7 ms                                                               | 12.8 ms: 1.01x slower                                                           |
| meteor_contest           | 71.9 ms                                                               | 72.8 ms: 1.01x slower                                                           |
| scimark_sor              | 96.2 ms                                                               | 97.4 ms: 1.01x slower                                                           |
| sqlglot_optimize         | 31.2 ms                                                               | 31.6 ms: 1.01x slower                                                           |
| deepcopy_reduce          | 1.50 us                                                               | 1.52 us: 1.01x slower                                                           |
| pickle_pure_python       | 182 us                                                                | 185 us: 1.01x slower                                                            |
| xml_etree_process        | 37.4 ms                                                               | 37.9 ms: 1.01x slower                                                           |
| async_tree_eager_tg      | 41.6 ms                                                               | 42.3 ms: 1.02x slower                                                           |
| sqlglot_normalize        | 168 ms                                                                | 171 ms: 1.02x slower                                                            |
| sympy_sum                | 70.2 ms                                                               | 71.6 ms: 1.02x slower                                                           |
| json                     | 2.95 ms                                                               | 3.01 ms: 1.02x slower                                                           |
| typing_runtime_protocols | 90.3 us                                                               | 92.2 us: 1.02x slower                                                           |
| coverage                 | 44.6 ms                                                               | 45.6 ms: 1.02x slower                                                           |
| comprehensions           | 10.2 us                                                               | 10.4 us: 1.02x slower                                                           |
| regex_effbot             | 2.57 ms                                                               | 2.64 ms: 1.02x slower                                                           |
| telco                    | 4.66 ms                                                               | 4.79 ms: 1.03x slower                                                           |
| Geometric mean           | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (35): asyncio_tcp_ssl, tornado_http, async_tree_eager_io, async_tree_io, async_tree_cpu_io_mixed_tg, logging_simple, async_tree_eager_io_tg, async_tree_memoization_tg, bench_mp_pool, asyncio_websockets, scimark_monte_carlo, dask, async_generators, async_tree_eager_cpu_io_mixed_tg, coroutines, pidigits, dulwich_log, float, gc_traversal, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none, async_tree_eager_cpu_io_mixed, xml_etree_iterparse, async_tree_eager_memoization, async_tree_io_tg, unpickle_pure_python, 2to3, async_tree_eager_memoization_tg, async_tree_none_tg, sqlglot_transpile, pycparser, pylint, xml_etree_parse, asyncio_tcp

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x