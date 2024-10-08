# Results vs. base

- fork: brandtbucher
- ref: tier_two_improvement
- machine: darwin-arm64
- commit hash: bbb07e8
- commit date: 2024-07-13
- overall geometric mean: 1.00x slower
- HPT reliability: 87.96%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-darwin-arm64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 1.52 sec                                                              | 1.51 sec: 1.01x faster                                                      |
| html5lib       | 31.2 ms                                                               | 30.9 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-darwin-arm64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg       | 447 ms                                                                | 449 ms: 1.00x slower                                                        |
| async_tree_eager_cpu_io_mixed    | 357 ms                                                                | 361 ms: 1.01x slower                                                        |
| async_tree_eager_cpu_io_mixed_tg | 332 ms                                                                | 335 ms: 1.01x slower                                                        |
| async_tree_io                    | 519 ms                                                                | 535 ms: 1.03x slower                                                        |
| Geometric mean                   | (ref)                                                                 | 1.01x slower                                                                |

Benchmark hidden because not significant (12): async_tree_memoization, async_tree_eager_tg, async_tree_eager, async_tree_eager_io_tg, async_tree_eager_io, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, async_tree_eager_memoization, async_tree_none, async_tree_cpu_io_mixed, async_tree_eager_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-darwin-arm64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 47.2 ms                                                               | 47.6 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-darwin-arm64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 150 ms                                                                | 149 ms: 1.00x faster                                                        |
| regex_v8       | 17.2 ms                                                               | 17.3 ms: 1.00x slower                                                       |
| regex_effbot   | 2.56 ms                                                               | 2.57 ms: 1.00x slower                                                       |
| regex_compile  | 73.5 ms                                                               | 73.8 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-darwin-arm64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 71.3 ms                                                               | 70.5 ms: 1.01x faster                                                       |
| tomli_loads          | 1.24 sec                                                              | 1.23 sec: 1.01x faster                                                      |
| xml_etree_process    | 36.5 ms                                                               | 36.4 ms: 1.00x faster                                                       |
| xml_etree_generate   | 52.5 ms                                                               | 52.4 ms: 1.00x faster                                                       |
| json_dumps           | 6.39 ms                                                               | 6.41 ms: 1.00x slower                                                       |
| pickle_pure_python   | 175 us                                                                | 175 us: 1.00x slower                                                        |
| unpickle_pure_python | 132 us                                                                | 133 us: 1.01x slower                                                        |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (2): xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-darwin-arm64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 12.7 ms                                                               | 12.8 ms: 1.01x slower                                                       |
| python_startup         | 15.3 ms                                                               | 15.4 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-darwin-arm64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 21.8 ms                                                               | 21.6 ms: 1.01x faster                                                       |
| mako            | 6.50 ms                                                               | 6.47 ms: 1.00x faster                                                       |
| genshi_text     | 15.8 ms                                                               | 16.3 ms: 1.03x slower                                                       |
| Geometric mean  | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                        | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-darwin-arm64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| generators                       | 23.2 ms                                                               | 22.4 ms: 1.04x faster                                                       |
| bpe_tokeniser                    | 3.12 sec                                                              | 3.04 sec: 1.03x faster                                                      |
| coroutines                       | 16.2 ms                                                               | 15.8 ms: 1.02x faster                                                       |
| telco                            | 4.64 ms                                                               | 4.55 ms: 1.02x faster                                                       |
| pyflate                          | 319 ms                                                                | 314 ms: 1.02x faster                                                        |
| meteor_contest                   | 72.7 ms                                                               | 71.6 ms: 1.02x faster                                                       |
| xml_etree_iterparse              | 71.3 ms                                                               | 70.5 ms: 1.01x faster                                                       |
| django_template                  | 21.8 ms                                                               | 21.6 ms: 1.01x faster                                                       |
| html5lib                         | 31.2 ms                                                               | 30.9 ms: 1.01x faster                                                       |
| coverage                         | 45.9 ms                                                               | 45.5 ms: 1.01x faster                                                       |
| create_gc_cycles                 | 913 us                                                                | 905 us: 1.01x faster                                                        |
| sympy_sum                        | 73.7 ms                                                               | 73.1 ms: 1.01x faster                                                       |
| tomli_loads                      | 1.24 sec                                                              | 1.23 sec: 1.01x faster                                                      |
| richards                         | 31.1 ms                                                               | 30.9 ms: 1.01x faster                                                       |
| scimark_sor                      | 102 ms                                                                | 101 ms: 1.01x faster                                                        |
| docutils                         | 1.52 sec                                                              | 1.51 sec: 1.01x faster                                                      |
| richards_super                   | 34.7 ms                                                               | 34.5 ms: 1.01x faster                                                       |
| crypto_pyaes                     | 52.2 ms                                                               | 51.9 ms: 1.01x faster                                                       |
| xml_etree_process                | 36.5 ms                                                               | 36.4 ms: 1.00x faster                                                       |
| raytrace                         | 166 ms                                                                | 165 ms: 1.00x faster                                                        |
| mako                             | 6.50 ms                                                               | 6.47 ms: 1.00x faster                                                       |
| regex_dna                        | 150 ms                                                                | 149 ms: 1.00x faster                                                        |
| hexiom                           | 4.40 ms                                                               | 4.39 ms: 1.00x faster                                                       |
| go                               | 101 ms                                                                | 101 ms: 1.00x faster                                                        |
| xml_etree_generate               | 52.5 ms                                                               | 52.4 ms: 1.00x faster                                                       |
| async_generators                 | 295 ms                                                                | 294 ms: 1.00x faster                                                        |
| sqlglot_normalize                | 179 ms                                                                | 179 ms: 1.00x faster                                                        |
| asyncio_websockets               | 409 ms                                                                | 410 ms: 1.00x slower                                                        |
| scimark_lu                       | 82.6 ms                                                               | 82.8 ms: 1.00x slower                                                       |
| regex_v8                         | 17.2 ms                                                               | 17.3 ms: 1.00x slower                                                       |
| regex_effbot                     | 2.56 ms                                                               | 2.57 ms: 1.00x slower                                                       |
| json_dumps                       | 6.39 ms                                                               | 6.41 ms: 1.00x slower                                                       |
| pickle_pure_python               | 175 us                                                                | 175 us: 1.00x slower                                                        |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                                | 449 ms: 1.00x slower                                                        |
| regex_compile                    | 73.5 ms                                                               | 73.8 ms: 1.00x slower                                                       |
| sympy_integrate                  | 11.0 ms                                                               | 11.1 ms: 1.01x slower                                                       |
| fannkuch                         | 244 ms                                                                | 246 ms: 1.01x slower                                                        |
| sqlglot_optimize                 | 33.2 ms                                                               | 33.4 ms: 1.01x slower                                                       |
| chaos                            | 39.3 ms                                                               | 39.6 ms: 1.01x slower                                                       |
| sqlglot_parse                    | 831 us                                                                | 836 us: 1.01x slower                                                        |
| deepcopy                         | 152 us                                                                | 153 us: 1.01x slower                                                        |
| sympy_str                        | 140 ms                                                                | 141 ms: 1.01x slower                                                        |
| sqlglot_transpile                | 1.00 ms                                                               | 1.01 ms: 1.01x slower                                                       |
| scimark_fft                      | 191 ms                                                                | 192 ms: 1.01x slower                                                        |
| python_startup_no_site           | 12.7 ms                                                               | 12.8 ms: 1.01x slower                                                       |
| sympy_expand                     | 241 ms                                                                | 243 ms: 1.01x slower                                                        |
| float                            | 47.2 ms                                                               | 47.6 ms: 1.01x slower                                                       |
| logging_silent                   | 61.7 ns                                                               | 62.2 ns: 1.01x slower                                                       |
| python_startup                   | 15.3 ms                                                               | 15.4 ms: 1.01x slower                                                       |
| async_tree_eager_cpu_io_mixed    | 357 ms                                                                | 361 ms: 1.01x slower                                                        |
| pycparser                        | 675 ms                                                                | 682 ms: 1.01x slower                                                        |
| async_tree_eager_cpu_io_mixed_tg | 332 ms                                                                | 335 ms: 1.01x slower                                                        |
| logging_simple                   | 3.04 us                                                               | 3.07 us: 1.01x slower                                                       |
| unpickle_pure_python             | 132 us                                                                | 133 us: 1.01x slower                                                        |
| async_tree_io                    | 519 ms                                                                | 535 ms: 1.03x slower                                                        |
| genshi_text                      | 15.8 ms                                                               | 16.3 ms: 1.03x slower                                                       |
| mdp                              | 1.45 sec                                                              | 1.56 sec: 1.07x slower                                                      |
| Geometric mean                   | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (41): bench_thread_pool, pylint, deepcopy_reduce, xml_etree_parse, pprint_pformat, genshi_xml, async_tree_memoization, deepcopy_memo, async_tree_eager_tg, thrift, spectral_norm, async_tree_eager, scimark_monte_carlo, deltablue, 2to3, tornado_http, scimark_sparse_mat_mult, nqueens, logging_format, gc_traversal, nbody, pprint_safe_repr, comprehensions, json, pidigits, async_tree_eager_io_tg, json_loads, async_tree_eager_io, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, pathlib, async_tree_eager_memoization, async_tree_none, typing_runtime_protocols, async_tree_cpu_io_mixed, dask, async_tree_eager_memoization_tg, bench_mp_pool, asyncio_tcp_ssl, asyncio_tcp

# HPT report

- Reliability score: 87.96% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x