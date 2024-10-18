# Results vs. base

- fork: brandtbucher
- ref: justin_likely
- machine: darwin-arm64
- commit hash: bad9944
- commit date: 2024-10-18
- overall geometric mean: 1.00x faster
- HPT reliability: 79.69%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 183 ms                                                                 | 183 ms: 1.00x slower                                                  |
| docutils       | 1.57 sec                                                               | 1.58 sec: 1.00x slower                                                |
| html5lib       | 34.3 ms                                                                | 33.9 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (2): sphinx, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager                 | 63.8 ms                                                                | 63.4 ms: 1.01x faster                                                 |
| async_generators                 | 294 ms                                                                 | 292 ms: 1.01x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 336 ms                                                                 | 337 ms: 1.00x slower                                                  |
| async_tree_eager_tg              | 42.6 ms                                                                | 42.8 ms: 1.00x slower                                                 |
| Geometric mean                   | (ref)                                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (17): async_tree_eager_memoization, coroutines, async_tree_memoization, async_tree_eager_io, async_tree_io_tg, asyncio_websockets, async_tree_eager_memoization_tg, async_tree_io, async_tree_none_tg, async_tree_memoization_tg, async_tree_eager_io_tg, async_tree_eager_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_cpu_io_mixed, asyncio_tcp_ssl, asyncio_tcp

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 76.1 ms                                                                | 75.4 ms: 1.01x faster                                                 |
| regex_dna      | 148 ms                                                                 | 149 ms: 1.01x slower                                                  |
| regex_v8       | 16.8 ms                                                                | 17.0 ms: 1.01x slower                                                 |
| regex_effbot   | 2.61 ms                                                                | 2.65 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_list          | 2.92 us                                                                | 2.87 us: 1.02x faster                                                 |
| json_dumps           | 7.22 ms                                                                | 7.13 ms: 1.01x faster                                                 |
| xml_etree_parse      | 108 ms                                                                 | 107 ms: 1.01x faster                                                  |
| pickle_pure_python   | 179 us                                                                 | 179 us: 1.00x faster                                                  |
| unpickle             | 9.09 us                                                                | 9.06 us: 1.00x faster                                                 |
| xml_etree_generate   | 50.4 ms                                                                | 50.6 ms: 1.00x slower                                                 |
| pickle               | 7.31 us                                                                | 7.34 us: 1.00x slower                                                 |
| xml_etree_process    | 34.7 ms                                                                | 34.9 ms: 1.01x slower                                                 |
| unpickle_pure_python | 131 us                                                                 | 132 us: 1.01x slower                                                  |
| unpickle_list        | 2.93 us                                                                | 2.97 us: 1.01x slower                                                 |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (4): tomli_loads, json_loads, xml_etree_iterparse, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 19.1 ms                                                                | 18.9 ms: 1.01x faster                                                 |
| python_startup_no_site | 14.8 ms                                                                | 14.7 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 17.3 ms                                                                | 16.1 ms: 1.07x faster                                                 |
| genshi_xml      | 43.2 ms                                                                | 42.1 ms: 1.02x faster                                                 |
| django_template | 23.1 ms                                                                | 22.7 ms: 1.02x faster                                                 |
| Geometric mean  | (ref)                                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                        | bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text                      | 17.3 ms                                                                | 16.1 ms: 1.07x faster                                                 |
| genshi_xml                       | 43.2 ms                                                                | 42.1 ms: 1.02x faster                                                 |
| sqlglot_normalize                | 188 ms                                                                 | 184 ms: 1.02x faster                                                  |
| django_template                  | 23.1 ms                                                                | 22.7 ms: 1.02x faster                                                 |
| pickle_list                      | 2.92 us                                                                | 2.87 us: 1.02x faster                                                 |
| json                             | 2.88 ms                                                                | 2.84 ms: 1.01x faster                                                 |
| go                               | 99.3 ms                                                                | 97.9 ms: 1.01x faster                                                 |
| scimark_sparse_mat_mult          | 3.20 ms                                                                | 3.16 ms: 1.01x faster                                                 |
| html5lib                         | 34.3 ms                                                                | 33.9 ms: 1.01x faster                                                 |
| json_dumps                       | 7.22 ms                                                                | 7.13 ms: 1.01x faster                                                 |
| xml_etree_parse                  | 108 ms                                                                 | 107 ms: 1.01x faster                                                  |
| python_startup                   | 19.1 ms                                                                | 18.9 ms: 1.01x faster                                                 |
| regex_compile                    | 76.1 ms                                                                | 75.4 ms: 1.01x faster                                                 |
| sympy_sum                        | 79.9 ms                                                                | 79.2 ms: 1.01x faster                                                 |
| python_startup_no_site           | 14.8 ms                                                                | 14.7 ms: 1.01x faster                                                 |
| sympy_integrate                  | 12.6 ms                                                                | 12.6 ms: 1.01x faster                                                 |
| async_tree_eager                 | 63.8 ms                                                                | 63.4 ms: 1.01x faster                                                 |
| hexiom                           | 4.97 ms                                                                | 4.94 ms: 1.01x faster                                                 |
| meteor_contest                   | 74.9 ms                                                                | 74.4 ms: 1.01x faster                                                 |
| async_generators                 | 294 ms                                                                 | 292 ms: 1.01x faster                                                  |
| sqlglot_transpile                | 1.07 ms                                                                | 1.06 ms: 1.01x faster                                                 |
| bpe_tokeniser                    | 3.05 sec                                                               | 3.03 sec: 1.01x faster                                                |
| sqlglot_optimize                 | 37.5 ms                                                                | 37.2 ms: 1.01x faster                                                 |
| pprint_safe_repr                 | 493 ms                                                                 | 490 ms: 1.01x faster                                                  |
| sympy_expand                     | 248 ms                                                                 | 247 ms: 1.00x faster                                                  |
| dulwich_log                      | 28.8 ms                                                                | 28.7 ms: 1.00x faster                                                 |
| pickle_pure_python               | 179 us                                                                 | 179 us: 1.00x faster                                                  |
| gc_traversal                     | 2.96 ms                                                                | 2.95 ms: 1.00x faster                                                 |
| scimark_fft                      | 191 ms                                                                 | 190 ms: 1.00x faster                                                  |
| bench_thread_pool                | 475 us                                                                 | 473 us: 1.00x faster                                                  |
| chaos                            | 41.5 ms                                                                | 41.3 ms: 1.00x faster                                                 |
| deepcopy                         | 155 us                                                                 | 155 us: 1.00x faster                                                  |
| logging_format                   | 3.41 us                                                                | 3.40 us: 1.00x faster                                                 |
| unpickle                         | 9.09 us                                                                | 9.06 us: 1.00x faster                                                 |
| create_gc_cycles                 | 1.32 ms                                                                | 1.32 ms: 1.00x faster                                                 |
| crypto_pyaes                     | 53.8 ms                                                                | 53.7 ms: 1.00x faster                                                 |
| scimark_monte_carlo              | 45.7 ms                                                                | 45.6 ms: 1.00x faster                                                 |
| sqlite_synth                     | 1.53 us                                                                | 1.54 us: 1.00x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 336 ms                                                                 | 337 ms: 1.00x slower                                                  |
| 2to3                             | 183 ms                                                                 | 183 ms: 1.00x slower                                                  |
| xml_etree_generate               | 50.4 ms                                                                | 50.6 ms: 1.00x slower                                                 |
| unpack_sequence                  | 76.0 ns                                                                | 76.2 ns: 1.00x slower                                                 |
| async_tree_eager_tg              | 42.6 ms                                                                | 42.8 ms: 1.00x slower                                                 |
| pickle                           | 7.31 us                                                                | 7.34 us: 1.00x slower                                                 |
| docutils                         | 1.57 sec                                                               | 1.58 sec: 1.00x slower                                                |
| fannkuch                         | 264 ms                                                                 | 266 ms: 1.01x slower                                                  |
| logging_simple                   | 3.10 us                                                                | 3.12 us: 1.01x slower                                                 |
| deepcopy_memo                    | 16.9 us                                                                | 17.0 us: 1.01x slower                                                 |
| deepcopy_reduce                  | 1.54 us                                                                | 1.55 us: 1.01x slower                                                 |
| thrift                           | 421 us                                                                 | 424 us: 1.01x slower                                                  |
| xml_etree_process                | 34.7 ms                                                                | 34.9 ms: 1.01x slower                                                 |
| regex_dna                        | 148 ms                                                                 | 149 ms: 1.01x slower                                                  |
| unpickle_pure_python             | 131 us                                                                 | 132 us: 1.01x slower                                                  |
| nqueens                          | 58.0 ms                                                                | 58.6 ms: 1.01x slower                                                 |
| pathlib                          | 21.9 ms                                                                | 22.2 ms: 1.01x slower                                                 |
| regex_v8                         | 16.8 ms                                                                | 17.0 ms: 1.01x slower                                                 |
| unpickle_list                    | 2.93 us                                                                | 2.97 us: 1.01x slower                                                 |
| regex_effbot                     | 2.61 ms                                                                | 2.65 ms: 1.02x slower                                                 |
| raytrace                         | 171 ms                                                                 | 174 ms: 1.02x slower                                                  |
| richards_super                   | 37.6 ms                                                                | 39.3 ms: 1.04x slower                                                 |
| richards                         | 33.8 ms                                                                | 35.6 ms: 1.05x slower                                                 |
| Geometric mean                   | (ref)                                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (45): tornado_http, generators, async_tree_eager_memoization, tomli_loads, coroutines, json_loads, spectral_norm, sympy_str, async_tree_memoization, mako, coverage, comprehensions, float, pidigits, async_tree_eager_io, pycparser, async_tree_io_tg, xml_etree_iterparse, telco, deltablue, asyncio_websockets, async_tree_eager_memoization_tg, nbody, pyflate, async_tree_io, sqlglot_parse, scimark_lu, async_tree_none_tg, bench_mp_pool, async_tree_memoization_tg, scimark_sor, async_tree_eager_io_tg, pprint_pformat, pickle_dict, mdp, async_tree_eager_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none, typing_runtime_protocols, logging_silent, async_tree_cpu_io_mixed, sphinx, asyncio_tcp_ssl, pylint, asyncio_tcp

# HPT report

- Reliability score: 79.69% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x