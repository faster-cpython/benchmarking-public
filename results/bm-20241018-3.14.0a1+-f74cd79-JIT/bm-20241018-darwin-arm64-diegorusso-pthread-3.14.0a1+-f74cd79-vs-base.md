# Results vs. base

- fork: diegorusso
- ref: pthread
- machine: darwin-arm64
- commit hash: f74cd79
- commit date: 2024-10-18
- overall geometric mean: 1.00x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241017-darwin-arm64-python-37986e830ba25d2c3829-3.14.0a1+-37986e8 | bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1+-f74cd79 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 183 ms                                                                 | 182 ms: 1.01x faster                                          |
| docutils       | 1.57 sec                                                               | 1.57 sec: 1.00x faster                                        |
| html5lib       | 34.1 ms                                                                | 34.0 ms: 1.00x faster                                         |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                  |

Benchmark hidden because not significant (2): sphinx, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241017-darwin-arm64-python-37986e830ba25d2c3829-3.14.0a1+-37986e8 | bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1+-f74cd79 |
|----------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_eager_tg              | 43.0 ms                                                                | 42.5 ms: 1.01x faster                                         |
| async_tree_eager                 | 64.5 ms                                                                | 64.0 ms: 1.01x faster                                         |
| coroutines                       | 16.6 ms                                                                | 16.5 ms: 1.01x faster                                         |
| async_tree_none                  | 200 ms                                                                 | 198 ms: 1.01x faster                                          |
| async_generators                 | 295 ms                                                                 | 293 ms: 1.01x faster                                          |
| async_tree_eager_cpu_io_mixed_tg | 336 ms                                                                 | 336 ms: 1.00x faster                                          |
| Geometric mean                   | (ref)                                                                  | 1.00x faster                                                  |

Benchmark hidden because not significant (13): async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_eager_cpu_io_mixed, async_tree_io, async_tree_io_tg, asyncio_websockets, async_tree_none_tg, async_tree_eager_io_tg, async_tree_eager_io, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241017-darwin-arm64-python-37986e830ba25d2c3829-3.14.0a1+-37986e8 | bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1+-f74cd79 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| pidigits       | 283 ms                                                                 | 283 ms: 1.00x faster                                          |
| nbody          | 65.4 ms                                                                | 65.3 ms: 1.00x faster                                         |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                  |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241017-darwin-arm64-python-37986e830ba25d2c3829-3.14.0a1+-37986e8 | bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1+-f74cd79 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 74.6 ms                                                                | 74.4 ms: 1.00x faster                                         |
| regex_v8       | 16.8 ms                                                                | 16.8 ms: 1.00x faster                                         |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                  |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241017-darwin-arm64-python-37986e830ba25d2c3829-3.14.0a1+-37986e8 | bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1+-f74cd79 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| json_dumps           | 7.14 ms                                                                | 7.08 ms: 1.01x faster                                         |
| unpickle_pure_python | 133 us                                                                 | 132 us: 1.01x faster                                          |
| json_loads           | 16.5 us                                                                | 16.4 us: 1.01x faster                                         |
| pickle_pure_python   | 180 us                                                                 | 180 us: 1.00x faster                                          |
| xml_etree_process    | 34.7 ms                                                                | 34.8 ms: 1.00x slower                                         |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                  |

Benchmark hidden because not significant (4): xml_etree_generate, tomli_loads, xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241017-darwin-arm64-python-37986e830ba25d2c3829-3.14.0a1+-37986e8 | bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1+-f74cd79 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup_no_site | 12.5 ms                                                                | 11.9 ms: 1.05x faster                                         |
| python_startup         | 16.2 ms                                                                | 15.7 ms: 1.03x faster                                         |
| Geometric mean         | (ref)                                                                  | 1.04x faster                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241017-darwin-arm64-python-37986e830ba25d2c3829-3.14.0a1+-37986e8 | bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1+-f74cd79 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| genshi_xml      | 41.8 ms                                                                | 41.0 ms: 1.02x faster                                         |
| genshi_text     | 16.5 ms                                                                | 16.3 ms: 1.01x faster                                         |
| django_template | 22.8 ms                                                                | 22.6 ms: 1.01x faster                                         |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                  |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                        | bm-20241017-darwin-arm64-python-37986e830ba25d2c3829-3.14.0a1+-37986e8 | bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1+-f74cd79 |
|----------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup_no_site           | 12.5 ms                                                                | 11.9 ms: 1.05x faster                                         |
| python_startup                   | 16.2 ms                                                                | 15.7 ms: 1.03x faster                                         |
| genshi_xml                       | 41.8 ms                                                                | 41.0 ms: 1.02x faster                                         |
| pyflate                          | 331 ms                                                                 | 325 ms: 1.02x faster                                          |
| coverage                         | 44.3 ms                                                                | 43.5 ms: 1.02x faster                                         |
| genshi_text                      | 16.5 ms                                                                | 16.3 ms: 1.01x faster                                         |
| scimark_sor                      | 87.2 ms                                                                | 86.1 ms: 1.01x faster                                         |
| scimark_lu                       | 65.9 ms                                                                | 65.0 ms: 1.01x faster                                         |
| sympy_sum                        | 79.7 ms                                                                | 78.8 ms: 1.01x faster                                         |
| sqlglot_optimize                 | 37.1 ms                                                                | 36.7 ms: 1.01x faster                                         |
| async_tree_eager_tg              | 43.0 ms                                                                | 42.5 ms: 1.01x faster                                         |
| nqueens                          | 59.4 ms                                                                | 58.7 ms: 1.01x faster                                         |
| spectral_norm                    | 70.0 ms                                                                | 69.3 ms: 1.01x faster                                         |
| django_template                  | 22.8 ms                                                                | 22.6 ms: 1.01x faster                                         |
| logging_format                   | 3.41 us                                                                | 3.38 us: 1.01x faster                                         |
| hexiom                           | 5.01 ms                                                                | 4.96 ms: 1.01x faster                                         |
| json_dumps                       | 7.14 ms                                                                | 7.08 ms: 1.01x faster                                         |
| sqlglot_transpile                | 1.06 ms                                                                | 1.05 ms: 1.01x faster                                         |
| sympy_str                        | 152 ms                                                                 | 151 ms: 1.01x faster                                          |
| sqlglot_parse                    | 871 us                                                                 | 865 us: 1.01x faster                                          |
| async_tree_eager                 | 64.5 ms                                                                | 64.0 ms: 1.01x faster                                         |
| 2to3                             | 183 ms                                                                 | 182 ms: 1.01x faster                                          |
| meteor_contest                   | 75.1 ms                                                                | 74.5 ms: 1.01x faster                                         |
| coroutines                       | 16.6 ms                                                                | 16.5 ms: 1.01x faster                                         |
| pylint                           | 179 ms                                                                 | 178 ms: 1.01x faster                                          |
| async_tree_none                  | 200 ms                                                                 | 198 ms: 1.01x faster                                          |
| scimark_monte_carlo              | 46.1 ms                                                                | 45.8 ms: 1.01x faster                                         |
| async_generators                 | 295 ms                                                                 | 293 ms: 1.01x faster                                          |
| logging_silent                   | 70.5 ns                                                                | 70.1 ns: 1.01x faster                                         |
| go                               | 99.0 ms                                                                | 98.4 ms: 1.01x faster                                         |
| comprehensions                   | 13.2 us                                                                | 13.1 us: 1.01x faster                                         |
| raytrace                         | 174 ms                                                                 | 173 ms: 1.01x faster                                          |
| unpickle_pure_python             | 133 us                                                                 | 132 us: 1.01x faster                                          |
| json_loads                       | 16.5 us                                                                | 16.4 us: 1.01x faster                                         |
| scimark_sparse_mat_mult          | 3.20 ms                                                                | 3.18 ms: 1.00x faster                                         |
| thrift                           | 422 us                                                                 | 420 us: 1.00x faster                                          |
| html5lib                         | 34.1 ms                                                                | 34.0 ms: 1.00x faster                                         |
| deepcopy                         | 152 us                                                                 | 152 us: 1.00x faster                                          |
| docutils                         | 1.57 sec                                                               | 1.57 sec: 1.00x faster                                        |
| regex_compile                    | 74.6 ms                                                                | 74.4 ms: 1.00x faster                                         |
| crypto_pyaes                     | 54.1 ms                                                                | 53.9 ms: 1.00x faster                                         |
| pickle_pure_python               | 180 us                                                                 | 180 us: 1.00x faster                                          |
| bench_thread_pool                | 477 us                                                                 | 476 us: 1.00x faster                                          |
| sympy_expand                     | 247 ms                                                                 | 247 ms: 1.00x faster                                          |
| pidigits                         | 283 ms                                                                 | 283 ms: 1.00x faster                                          |
| nbody                            | 65.4 ms                                                                | 65.3 ms: 1.00x faster                                         |
| regex_v8                         | 16.8 ms                                                                | 16.8 ms: 1.00x faster                                         |
| async_tree_eager_cpu_io_mixed_tg | 336 ms                                                                 | 336 ms: 1.00x faster                                          |
| bpe_tokeniser                    | 3.04 sec                                                               | 3.05 sec: 1.00x slower                                        |
| dulwich_log                      | 28.9 ms                                                                | 29.0 ms: 1.00x slower                                         |
| xml_etree_process                | 34.7 ms                                                                | 34.8 ms: 1.00x slower                                         |
| sqlglot_normalize                | 185 ms                                                                 | 186 ms: 1.01x slower                                          |
| pprint_safe_repr                 | 501 ms                                                                 | 504 ms: 1.01x slower                                          |
| bench_mp_pool                    | 60.0 ms                                                                | 60.5 ms: 1.01x slower                                         |
| mdp                              | 1.54 sec                                                               | 1.55 sec: 1.01x slower                                        |
| pprint_pformat                   | 999 ms                                                                 | 1.01 sec: 1.01x slower                                        |
| fannkuch                         | 264 ms                                                                 | 268 ms: 1.01x slower                                          |
| telco                            | 4.53 ms                                                                | 4.58 ms: 1.01x slower                                         |
| richards_super                   | 37.9 ms                                                                | 39.5 ms: 1.04x slower                                         |
| richards                         | 34.0 ms                                                                | 35.7 ms: 1.05x slower                                         |
| Geometric mean                   | (ref)                                                                  | 1.00x faster                                                  |

Benchmark hidden because not significant (37): async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_cpu_io_mixed_tg, generators, async_tree_memoization, sphinx, async_tree_memoization_tg, async_tree_eager_cpu_io_mixed, sympy_integrate, logging_simple, pycparser, mako, gc_traversal, async_tree_io, xml_etree_generate, scimark_fft, async_tree_io_tg, asyncio_websockets, float, deepcopy_memo, deltablue, tomli_loads, async_tree_none_tg, regex_effbot, chaos, deepcopy_reduce, regex_dna, xml_etree_iterparse, xml_etree_parse, create_gc_cycles, async_tree_eager_io_tg, async_tree_eager_io, json, async_tree_cpu_io_mixed, typing_runtime_protocols, pathlib, tornado_http

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x