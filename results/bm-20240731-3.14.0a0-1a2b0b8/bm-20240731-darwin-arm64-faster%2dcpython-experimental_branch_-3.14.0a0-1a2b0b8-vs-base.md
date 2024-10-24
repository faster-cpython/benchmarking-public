# Results vs. base

- fork: faster-cpython
- ref: experimental_branch_
- machine: darwin-arm64
- commit hash: 1a2b0b8
- commit date: 2024-07-31
- overall geometric mean: 1.00x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240730-darwin-arm64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 162 ms                                                                | 163 ms: 1.01x slower                                                            |
| docutils       | 1.49 sec                                                              | 1.50 sec: 1.01x slower                                                          |
| html5lib       | 31.5 ms                                                               | 31.6 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240730-darwin-arm64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager                 | 63.0 ms                                                               | 61.7 ms: 1.02x faster                                                           |
| async_tree_eager_tg              | 42.9 ms                                                               | 42.3 ms: 1.01x faster                                                           |
| async_tree_eager_cpu_io_mixed_tg | 335 ms                                                                | 336 ms: 1.00x slower                                                            |
| async_generators                 | 282 ms                                                                | 283 ms: 1.00x slower                                                            |
| Geometric mean                   | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (17): asyncio_tcp, async_tree_eager_memoization, async_tree_eager_io, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_memoization_tg, coroutines, async_tree_eager_cpu_io_mixed, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none, async_tree_none_tg, asyncio_tcp_ssl, async_tree_io_tg, async_tree_eager_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240730-darwin-arm64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 58.9 ms                                                               | 59.1 ms: 1.00x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240730-darwin-arm64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 17.6 ms                                                               | 17.4 ms: 1.01x faster                                                           |
| regex_dna      | 152 ms                                                                | 150 ms: 1.01x faster                                                            |
| regex_compile  | 68.3 ms                                                               | 69.1 ms: 1.01x slower                                                           |
| regex_effbot   | 2.59 ms                                                               | 2.64 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240730-darwin-arm64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|--------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps         | 6.43 ms                                                               | 6.45 ms: 1.00x slower                                                           |
| json_loads         | 17.3 us                                                               | 17.4 us: 1.00x slower                                                           |
| xml_etree_generate | 53.3 ms                                                               | 53.7 ms: 1.01x slower                                                           |
| pickle_pure_python | 182 us                                                                | 185 us: 1.02x slower                                                            |
| Geometric mean     | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (5): tomli_loads, xml_etree_iterparse, xml_etree_process, unpickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240730-darwin-arm64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 15.3 ms                                                               | 15.5 ms: 1.01x slower                                                           |
| python_startup_no_site | 12.5 ms                                                               | 12.8 ms: 1.03x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.02x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240730-darwin-arm64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 14.0 ms                                                               | 14.1 ms: 1.01x slower                                                           |
| django_template | 19.7 ms                                                               | 19.9 ms: 1.01x slower                                                           |
| genshi_xml      | 30.2 ms                                                               | 30.5 ms: 1.01x slower                                                           |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                        | bm-20240730-darwin-arm64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| logging_format                   | 3.43 us                                                               | 3.35 us: 1.02x faster                                                           |
| async_tree_eager                 | 63.0 ms                                                               | 61.7 ms: 1.02x faster                                                           |
| regex_v8                         | 17.6 ms                                                               | 17.4 ms: 1.01x faster                                                           |
| regex_dna                        | 152 ms                                                                | 150 ms: 1.01x faster                                                            |
| logging_simple                   | 3.10 us                                                               | 3.05 us: 1.01x faster                                                           |
| async_tree_eager_tg              | 42.9 ms                                                               | 42.3 ms: 1.01x faster                                                           |
| logging_silent                   | 59.9 ns                                                               | 59.5 ns: 1.01x faster                                                           |
| dulwich_log                      | 27.3 ms                                                               | 27.2 ms: 1.00x faster                                                           |
| generators                       | 20.6 ms                                                               | 20.6 ms: 1.00x slower                                                           |
| scimark_lu                       | 70.3 ms                                                               | 70.5 ms: 1.00x slower                                                           |
| richards                         | 31.4 ms                                                               | 31.5 ms: 1.00x slower                                                           |
| nbody                            | 58.9 ms                                                               | 59.1 ms: 1.00x slower                                                           |
| raytrace                         | 149 ms                                                                | 149 ms: 1.00x slower                                                            |
| async_tree_eager_cpu_io_mixed_tg | 335 ms                                                                | 336 ms: 1.00x slower                                                            |
| scimark_monte_carlo              | 43.0 ms                                                               | 43.2 ms: 1.00x slower                                                           |
| gc_traversal                     | 2.45 ms                                                               | 2.46 ms: 1.00x slower                                                           |
| scimark_sparse_mat_mult          | 2.83 ms                                                               | 2.84 ms: 1.00x slower                                                           |
| json_dumps                       | 6.43 ms                                                               | 6.45 ms: 1.00x slower                                                           |
| sqlglot_transpile                | 905 us                                                                | 908 us: 1.00x slower                                                            |
| bench_thread_pool                | 451 us                                                                | 453 us: 1.00x slower                                                            |
| async_generators                 | 282 ms                                                                | 283 ms: 1.00x slower                                                            |
| json_loads                       | 17.3 us                                                               | 17.4 us: 1.00x slower                                                           |
| html5lib                         | 31.5 ms                                                               | 31.6 ms: 1.01x slower                                                           |
| nqueens                          | 53.5 ms                                                               | 53.8 ms: 1.01x slower                                                           |
| 2to3                             | 162 ms                                                                | 163 ms: 1.01x slower                                                            |
| sqlglot_optimize                 | 31.4 ms                                                               | 31.6 ms: 1.01x slower                                                           |
| deepcopy                         | 145 us                                                                | 146 us: 1.01x slower                                                            |
| deepcopy_reduce                  | 1.51 us                                                               | 1.52 us: 1.01x slower                                                           |
| genshi_text                      | 14.0 ms                                                               | 14.1 ms: 1.01x slower                                                           |
| django_template                  | 19.7 ms                                                               | 19.9 ms: 1.01x slower                                                           |
| pathlib                          | 23.3 ms                                                               | 23.5 ms: 1.01x slower                                                           |
| xml_etree_generate               | 53.3 ms                                                               | 53.7 ms: 1.01x slower                                                           |
| genshi_xml                       | 30.2 ms                                                               | 30.5 ms: 1.01x slower                                                           |
| pyflate                          | 322 ms                                                                | 324 ms: 1.01x slower                                                            |
| docutils                         | 1.49 sec                                                              | 1.50 sec: 1.01x slower                                                          |
| pprint_pformat                   | 958 ms                                                                | 967 ms: 1.01x slower                                                            |
| mdp                              | 1.43 sec                                                              | 1.44 sec: 1.01x slower                                                          |
| sympy_expand                     | 228 ms                                                                | 230 ms: 1.01x slower                                                            |
| sqlglot_parse                    | 741 us                                                                | 748 us: 1.01x slower                                                            |
| bpe_tokeniser                    | 3.10 sec                                                              | 3.13 sec: 1.01x slower                                                          |
| thrift                           | 432 us                                                                | 436 us: 1.01x slower                                                            |
| sympy_str                        | 134 ms                                                                | 135 ms: 1.01x slower                                                            |
| python_startup                   | 15.3 ms                                                               | 15.5 ms: 1.01x slower                                                           |
| hexiom                           | 4.08 ms                                                               | 4.12 ms: 1.01x slower                                                           |
| richards_super                   | 34.4 ms                                                               | 34.8 ms: 1.01x slower                                                           |
| scimark_sor                      | 96.3 ms                                                               | 97.4 ms: 1.01x slower                                                           |
| pprint_safe_repr                 | 470 ms                                                                | 475 ms: 1.01x slower                                                            |
| crypto_pyaes                     | 50.4 ms                                                               | 51.1 ms: 1.01x slower                                                           |
| sympy_integrate                  | 10.4 ms                                                               | 10.5 ms: 1.01x slower                                                           |
| regex_compile                    | 68.3 ms                                                               | 69.1 ms: 1.01x slower                                                           |
| spectral_norm                    | 66.7 ms                                                               | 67.6 ms: 1.01x slower                                                           |
| create_gc_cycles                 | 894 us                                                                | 906 us: 1.01x slower                                                            |
| sqlglot_normalize                | 169 ms                                                                | 171 ms: 1.01x slower                                                            |
| go                               | 97.4 ms                                                               | 98.8 ms: 1.01x slower                                                           |
| deepcopy_memo                    | 16.8 us                                                               | 17.1 us: 1.01x slower                                                           |
| pickle_pure_python               | 182 us                                                                | 185 us: 1.02x slower                                                            |
| sympy_sum                        | 70.5 ms                                                               | 71.6 ms: 1.02x slower                                                           |
| meteor_contest                   | 71.6 ms                                                               | 72.8 ms: 1.02x slower                                                           |
| deltablue                        | 2.10 ms                                                               | 2.13 ms: 1.02x slower                                                           |
| regex_effbot                     | 2.59 ms                                                               | 2.64 ms: 1.02x slower                                                           |
| json                             | 2.96 ms                                                               | 3.01 ms: 1.02x slower                                                           |
| comprehensions                   | 10.2 us                                                               | 10.4 us: 1.02x slower                                                           |
| python_startup_no_site           | 12.5 ms                                                               | 12.8 ms: 1.03x slower                                                           |
| telco                            | 4.60 ms                                                               | 4.79 ms: 1.04x slower                                                           |
| Geometric mean                   | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (35): asyncio_tcp, async_tree_eager_memoization, async_tree_eager_io, async_tree_io, scimark_fft, async_tree_cpu_io_mixed_tg, fannkuch, async_tree_eager_io_tg, chaos, async_tree_memoization_tg, coroutines, tomli_loads, async_tree_eager_cpu_io_mixed, float, pidigits, xml_etree_iterparse, mako, asyncio_websockets, async_tree_cpu_io_mixed, xml_etree_process, dask, async_tree_memoization, async_tree_none, tornado_http, async_tree_none_tg, asyncio_tcp_ssl, async_tree_io_tg, pycparser, typing_runtime_protocols, coverage, unpickle_pure_python, bench_mp_pool, async_tree_eager_memoization_tg, xml_etree_parse, pylint

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x