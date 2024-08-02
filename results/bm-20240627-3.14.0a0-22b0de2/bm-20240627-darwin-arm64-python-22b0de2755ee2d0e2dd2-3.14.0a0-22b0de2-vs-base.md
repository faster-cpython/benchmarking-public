# Results vs. base

- fork: python
- ref: 22b0de2755ee2d0e2dd2
- machine: darwin-arm64
- commit hash: 22b0de2
- commit date: 2024-06-27
- overall geometric mean: 1.01x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240626-darwin-arm64-python-d611c4c8e9893c081696-3.14.0a0-d611c4c | bm-20240627-darwin-arm64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 167 ms                                                                | 188 ms: 1.13x slower                                                  |
| docutils       | 1.52 sec                                                              | 1.49 sec: 1.02x faster                                                |
| html5lib       | 31.5 ms                                                               | 31.8 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240626-darwin-arm64-python-d611c4c8e9893c081696-3.14.0a0-d611c4c | bm-20240627-darwin-arm64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                                | 332 ms: 1.00x slower                                                  |
| async_tree_cpu_io_mixed_tg       | 445 ms                                                                | 447 ms: 1.00x slower                                                  |
| async_tree_eager                 | 61.6 ms                                                               | 62.5 ms: 1.01x slower                                                 |
| async_tree_eager_tg              | 40.5 ms                                                               | 41.4 ms: 1.02x slower                                                 |
| async_tree_io                    | 522 ms                                                                | 539 ms: 1.03x slower                                                  |
| Geometric mean                   | (ref)                                                                 | 1.01x slower                                                          |

Benchmark hidden because not significant (11): async_tree_cpu_io_mixed, async_tree_eager_cpu_io_mixed, async_tree_eager_io, async_tree_memoization_tg, async_tree_memoization, async_tree_none_tg, async_tree_eager_io_tg, async_tree_io_tg, async_tree_eager_memoization_tg, async_tree_none, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240626-darwin-arm64-python-d611c4c8e9893c081696-3.14.0a0-d611c4c | bm-20240627-darwin-arm64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 62.0 ms                                                               | 60.0 ms: 1.03x faster                                                 |
| float          | 49.0 ms                                                               | 50.6 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240626-darwin-arm64-python-d611c4c8e9893c081696-3.14.0a0-d611c4c | bm-20240627-darwin-arm64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.59 ms                                                               | 2.54 ms: 1.02x faster                                                 |
| regex_dna      | 149 ms                                                                | 150 ms: 1.00x slower                                                  |
| regex_v8       | 17.2 ms                                                               | 17.3 ms: 1.01x slower                                                 |
| regex_compile  | 68.6 ms                                                               | 69.4 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240626-darwin-arm64-python-d611c4c8e9893c081696-3.14.0a0-d611c4c | bm-20240627-darwin-arm64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 6.50 ms                                                               | 6.46 ms: 1.01x faster                                                 |
| pickle_pure_python   | 184 us                                                                | 185 us: 1.00x slower                                                  |
| xml_etree_process    | 37.8 ms                                                               | 38.2 ms: 1.01x slower                                                 |
| xml_etree_generate   | 53.4 ms                                                               | 54.0 ms: 1.01x slower                                                 |
| unpickle_pure_python | 145 us                                                                | 146 us: 1.01x slower                                                  |
| json_loads           | 17.3 us                                                               | 17.6 us: 1.02x slower                                                 |
| tomli_loads          | 1.47 sec                                                              | 1.49 sec: 1.02x slower                                                |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                          |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240626-darwin-arm64-python-d611c4c8e9893c081696-3.14.0a0-d611c4c | bm-20240627-darwin-arm64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 20.9 ms                                                               | 21.5 ms: 1.03x slower                                                 |
| python_startup_no_site | 15.2 ms                                                               | 15.6 ms: 1.03x slower                                                 |
| Geometric mean         | (ref)                                                                 | 1.03x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240626-darwin-arm64-python-d611c4c8e9893c081696-3.14.0a0-d611c4c | bm-20240627-darwin-arm64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 13.9 ms                                                               | 13.9 ms: 1.01x slower                                                 |
| django_template | 19.9 ms                                                               | 20.0 ms: 1.01x slower                                                 |
| mako            | 6.92 ms                                                               | 7.12 ms: 1.03x slower                                                 |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                          |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                        | bm-20240626-darwin-arm64-python-d611c4c8e9893c081696-3.14.0a0-d611c4c | bm-20240627-darwin-arm64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody                            | 62.0 ms                                                               | 60.0 ms: 1.03x faster                                                 |
| sqlglot_optimize                 | 32.8 ms                                                               | 31.8 ms: 1.03x faster                                                 |
| docutils                         | 1.52 sec                                                              | 1.49 sec: 1.02x faster                                                |
| typing_runtime_protocols         | 94.6 us                                                               | 92.7 us: 1.02x faster                                                 |
| regex_effbot                     | 2.59 ms                                                               | 2.54 ms: 1.02x faster                                                 |
| raytrace                         | 150 ms                                                                | 148 ms: 1.01x faster                                                  |
| chaos                            | 35.6 ms                                                               | 35.3 ms: 1.01x faster                                                 |
| comprehensions                   | 10.9 us                                                               | 10.8 us: 1.01x faster                                                 |
| hexiom                           | 4.16 ms                                                               | 4.13 ms: 1.01x faster                                                 |
| scimark_sor                      | 96.6 ms                                                               | 95.8 ms: 1.01x faster                                                 |
| json_dumps                       | 6.50 ms                                                               | 6.46 ms: 1.01x faster                                                 |
| pyflate                          | 324 ms                                                                | 323 ms: 1.00x faster                                                  |
| generators                       | 22.8 ms                                                               | 22.7 ms: 1.00x faster                                                 |
| deltablue                        | 2.15 ms                                                               | 2.14 ms: 1.00x faster                                                 |
| gc_traversal                     | 2.46 ms                                                               | 2.46 ms: 1.00x faster                                                 |
| regex_dna                        | 149 ms                                                                | 150 ms: 1.00x slower                                                  |
| asyncio_websockets               | 409 ms                                                                | 410 ms: 1.00x slower                                                  |
| nqueens                          | 53.9 ms                                                               | 54.0 ms: 1.00x slower                                                 |
| go                               | 100 ms                                                                | 100 ms: 1.00x slower                                                  |
| crypto_pyaes                     | 50.3 ms                                                               | 50.5 ms: 1.00x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                                | 332 ms: 1.00x slower                                                  |
| bpe_tokeniser                    | 3.12 sec                                                              | 3.13 sec: 1.00x slower                                                |
| async_tree_cpu_io_mixed_tg       | 445 ms                                                                | 447 ms: 1.00x slower                                                  |
| mdp                              | 1.43 sec                                                              | 1.44 sec: 1.00x slower                                                |
| async_generators                 | 281 ms                                                                | 282 ms: 1.00x slower                                                  |
| pickle_pure_python               | 184 us                                                                | 185 us: 1.00x slower                                                  |
| logging_format                   | 3.38 us                                                               | 3.39 us: 1.00x slower                                                 |
| logging_silent                   | 60.7 ns                                                               | 61.0 ns: 1.00x slower                                                 |
| bench_thread_pool                | 452 us                                                                | 455 us: 1.01x slower                                                  |
| scimark_sparse_mat_mult          | 2.88 ms                                                               | 2.90 ms: 1.01x slower                                                 |
| create_gc_cycles                 | 882 us                                                                | 887 us: 1.01x slower                                                  |
| regex_v8                         | 17.2 ms                                                               | 17.3 ms: 1.01x slower                                                 |
| genshi_text                      | 13.9 ms                                                               | 13.9 ms: 1.01x slower                                                 |
| django_template                  | 19.9 ms                                                               | 20.0 ms: 1.01x slower                                                 |
| sympy_expand                     | 231 ms                                                                | 233 ms: 1.01x slower                                                  |
| meteor_contest                   | 71.7 ms                                                               | 72.2 ms: 1.01x slower                                                 |
| thrift                           | 432 us                                                                | 436 us: 1.01x slower                                                  |
| richards                         | 31.6 ms                                                               | 31.8 ms: 1.01x slower                                                 |
| logging_simple                   | 3.05 us                                                               | 3.08 us: 1.01x slower                                                 |
| xml_etree_process                | 37.8 ms                                                               | 38.2 ms: 1.01x slower                                                 |
| richards_super                   | 34.7 ms                                                               | 35.0 ms: 1.01x slower                                                 |
| scimark_monte_carlo              | 43.5 ms                                                               | 44.0 ms: 1.01x slower                                                 |
| html5lib                         | 31.5 ms                                                               | 31.8 ms: 1.01x slower                                                 |
| json                             | 2.98 ms                                                               | 3.01 ms: 1.01x slower                                                 |
| telco                            | 4.60 ms                                                               | 4.65 ms: 1.01x slower                                                 |
| spectral_norm                    | 67.6 ms                                                               | 68.4 ms: 1.01x slower                                                 |
| xml_etree_generate               | 53.4 ms                                                               | 54.0 ms: 1.01x slower                                                 |
| deepcopy                         | 146 us                                                                | 147 us: 1.01x slower                                                  |
| regex_compile                    | 68.6 ms                                                               | 69.4 ms: 1.01x slower                                                 |
| scimark_fft                      | 187 ms                                                                | 190 ms: 1.01x slower                                                  |
| unpickle_pure_python             | 145 us                                                                | 146 us: 1.01x slower                                                  |
| sympy_integrate                  | 10.4 ms                                                               | 10.6 ms: 1.01x slower                                                 |
| sympy_str                        | 134 ms                                                                | 136 ms: 1.01x slower                                                  |
| sqlglot_parse                    | 753 us                                                                | 763 us: 1.01x slower                                                  |
| async_tree_eager                 | 61.6 ms                                                               | 62.5 ms: 1.01x slower                                                 |
| coroutines                       | 16.1 ms                                                               | 16.3 ms: 1.01x slower                                                 |
| deepcopy_reduce                  | 1.50 us                                                               | 1.52 us: 1.02x slower                                                 |
| json_loads                       | 17.3 us                                                               | 17.6 us: 1.02x slower                                                 |
| tomli_loads                      | 1.47 sec                                                              | 1.49 sec: 1.02x slower                                                |
| sympy_sum                        | 70.4 ms                                                               | 71.7 ms: 1.02x slower                                                 |
| async_tree_eager_tg              | 40.5 ms                                                               | 41.4 ms: 1.02x slower                                                 |
| sqlglot_transpile                | 907 us                                                                | 929 us: 1.02x slower                                                  |
| fannkuch                         | 261 ms                                                                | 268 ms: 1.03x slower                                                  |
| pprint_pformat                   | 954 ms                                                                | 981 ms: 1.03x slower                                                  |
| mako                             | 6.92 ms                                                               | 7.12 ms: 1.03x slower                                                 |
| python_startup                   | 20.9 ms                                                               | 21.5 ms: 1.03x slower                                                 |
| python_startup_no_site           | 15.2 ms                                                               | 15.6 ms: 1.03x slower                                                 |
| deepcopy_memo                    | 16.5 us                                                               | 17.1 us: 1.03x slower                                                 |
| async_tree_io                    | 522 ms                                                                | 539 ms: 1.03x slower                                                  |
| float                            | 49.0 ms                                                               | 50.6 ms: 1.03x slower                                                 |
| pprint_safe_repr                 | 467 ms                                                                | 483 ms: 1.03x slower                                                  |
| scimark_lu                       | 69.9 ms                                                               | 72.4 ms: 1.04x slower                                                 |
| asyncio_tcp                      | 412 ms                                                                | 441 ms: 1.07x slower                                                  |
| 2to3                             | 167 ms                                                                | 188 ms: 1.13x slower                                                  |
| Geometric mean                   | (ref)                                                                 | 1.01x slower                                                          |

Benchmark hidden because not significant (24): xml_etree_parse, pathlib, genshi_xml, pidigits, sqlglot_normalize, coverage, async_tree_cpu_io_mixed, dask, bench_mp_pool, asyncio_tcp_ssl, async_tree_eager_cpu_io_mixed, xml_etree_iterparse, async_tree_eager_io, async_tree_memoization_tg, async_tree_memoization, pycparser, async_tree_none_tg, async_tree_eager_io_tg, async_tree_io_tg, async_tree_eager_memoization_tg, async_tree_none, async_tree_eager_memoization, pylint, tornado_http

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x