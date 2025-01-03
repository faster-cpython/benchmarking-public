# Results vs. base

- fork: eendebakpt
- ref: 05f479c7b36947e5f3e9
- machine: darwin-arm64
- commit hash: 05f479c
- commit date: 2025-01-02
- overall geometric mean: 1.007x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250102-darwin-arm64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-darwin-arm64-eendebakpt-05f479c7b36947e5f3e9-3.14.0a3+-05f479c |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 161 ms                                                                 | 160 ms: 1.01x faster                                                       |
| docutils       | 1.40 sec                                                               | 1.38 sec: 1.01x faster                                                     |
| html5lib       | 29.2 ms                                                                | 28.8 ms: 1.01x faster                                                      |
| sphinx         | 564 ms                                                                 | 554 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                       | bm-20250102-darwin-arm64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-darwin-arm64-eendebakpt-05f479c7b36947e5f3e9-3.14.0a3+-05f479c |
|---------------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_eager_memoization_tg | 124 ms                                                                 | 121 ms: 1.02x faster                                                       |
| async_tree_eager_memoization    | 141 ms                                                                 | 140 ms: 1.01x faster                                                       |
| async_tree_eager                | 61.5 ms                                                                | 61.1 ms: 1.01x faster                                                      |
| asyncio_websockets              | 242 ms                                                                 | 242 ms: 1.00x slower                                                       |
| coroutines                      | 16.0 ms                                                                | 16.1 ms: 1.01x slower                                                      |
| async_tree_io_tg                | 352 ms                                                                 | 360 ms: 1.02x slower                                                       |
| Geometric mean                  | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (13): async_tree_none, async_tree_io, async_tree_memoization, async_tree_none_tg, async_tree_eager_io_tg, async_generators, async_tree_memoization_tg, async_tree_eager_io, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_tg, async_tree_cpu_io_mixed, async_tree_eager_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250102-darwin-arm64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-darwin-arm64-eendebakpt-05f479c7b36947e5f3e9-3.14.0a3+-05f479c |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 46.3 ms                                                                | 46.9 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250102-darwin-arm64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-darwin-arm64-eendebakpt-05f479c7b36947e5f3e9-3.14.0a3+-05f479c |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 66.7 ms                                                                | 65.0 ms: 1.03x faster                                                      |
| regex_dna      | 135 ms                                                                 | 137 ms: 1.01x slower                                                       |
| regex_effbot   | 2.05 ms                                                                | 2.08 ms: 1.01x slower                                                      |
| regex_v8       | 15.7 ms                                                                | 16.0 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250102-darwin-arm64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-darwin-arm64-eendebakpt-05f479c7b36947e5f3e9-3.14.0a3+-05f479c |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_process    | 38.0 ms                                                                | 37.5 ms: 1.01x faster                                                      |
| xml_etree_generate   | 52.2 ms                                                                | 51.6 ms: 1.01x faster                                                      |
| tomli_loads          | 1.20 sec                                                               | 1.19 sec: 1.01x faster                                                     |
| json_dumps           | 7.28 ms                                                                | 7.23 ms: 1.01x faster                                                      |
| unpickle_pure_python | 136 us                                                                 | 136 us: 1.00x faster                                                       |
| pickle_pure_python   | 196 us                                                                 | 196 us: 1.00x slower                                                       |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (3): json_loads, xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250102-darwin-arm64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-darwin-arm64-eendebakpt-05f479c7b36947e5f3e9-3.14.0a3+-05f479c |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 12.6 ms                                                                | 12.3 ms: 1.03x faster                                                      |
| python_startup         | 17.3 ms                                                                | 17.0 ms: 1.01x faster                                                      |
| Geometric mean         | (ref)                                                                  | 1.02x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250102-darwin-arm64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-darwin-arm64-eendebakpt-05f479c7b36947e5f3e9-3.14.0a3+-05f479c |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 20.9 ms                                                                | 20.3 ms: 1.03x faster                                                      |
| genshi_text     | 13.5 ms                                                                | 13.1 ms: 1.03x faster                                                      |
| genshi_xml      | 28.2 ms                                                                | 28.0 ms: 1.01x faster                                                      |
| mako            | 6.95 ms                                                                | 7.13 ms: 1.03x slower                                                      |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                               |

All benchmarks:
===============

| Benchmark                       | bm-20250102-darwin-arm64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-darwin-arm64-eendebakpt-05f479c7b36947e5f3e9-3.14.0a3+-05f479c |
|---------------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| sqlglot_optimize                | 32.5 ms                                                                | 31.1 ms: 1.04x faster                                                      |
| sqlglot_normalize               | 178 ms                                                                 | 171 ms: 1.04x faster                                                       |
| telco                           | 4.55 ms                                                                | 4.40 ms: 1.03x faster                                                      |
| django_template                 | 20.9 ms                                                                | 20.3 ms: 1.03x faster                                                      |
| comprehensions                  | 12.4 us                                                                | 12.1 us: 1.03x faster                                                      |
| sympy_expand                    | 233 ms                                                                 | 226 ms: 1.03x faster                                                       |
| python_startup_no_site          | 12.6 ms                                                                | 12.3 ms: 1.03x faster                                                      |
| bpe_tokeniser                   | 2.97 sec                                                               | 2.89 sec: 1.03x faster                                                     |
| nqueens                         | 55.9 ms                                                                | 54.4 ms: 1.03x faster                                                      |
| genshi_text                     | 13.5 ms                                                                | 13.1 ms: 1.03x faster                                                      |
| sympy_integrate                 | 11.1 ms                                                                | 10.8 ms: 1.03x faster                                                      |
| regex_compile                   | 66.7 ms                                                                | 65.0 ms: 1.03x faster                                                      |
| generators                      | 23.0 ms                                                                | 22.5 ms: 1.02x faster                                                      |
| async_tree_eager_memoization_tg | 124 ms                                                                 | 121 ms: 1.02x faster                                                       |
| typing_runtime_protocols        | 94.7 us                                                                | 92.8 us: 1.02x faster                                                      |
| deepcopy                        | 149 us                                                                 | 146 us: 1.02x faster                                                       |
| chaos                           | 37.9 ms                                                                | 37.2 ms: 1.02x faster                                                      |
| sphinx                          | 564 ms                                                                 | 554 ms: 1.02x faster                                                       |
| sympy_sum                       | 73.0 ms                                                                | 71.7 ms: 1.02x faster                                                      |
| many_optionals                  | 440 us                                                                 | 432 us: 1.02x faster                                                       |
| deltablue                       | 2.34 ms                                                                | 2.30 ms: 1.02x faster                                                      |
| thrift                          | 434 us                                                                 | 427 us: 1.02x faster                                                       |
| sympy_str                       | 138 ms                                                                 | 135 ms: 1.02x faster                                                       |
| sqlalchemy_imperative           | 6.44 ms                                                                | 6.34 ms: 1.02x faster                                                      |
| sqlglot_transpile               | 926 us                                                                 | 912 us: 1.02x faster                                                       |
| html5lib                        | 29.2 ms                                                                | 28.8 ms: 1.01x faster                                                      |
| sqlalchemy_declarative          | 57.9 ms                                                                | 57.2 ms: 1.01x faster                                                      |
| logging_format                  | 3.47 us                                                                | 3.42 us: 1.01x faster                                                      |
| python_startup                  | 17.3 ms                                                                | 17.0 ms: 1.01x faster                                                      |
| xml_etree_process               | 38.0 ms                                                                | 37.5 ms: 1.01x faster                                                      |
| mdp                             | 1.49 sec                                                               | 1.47 sec: 1.01x faster                                                     |
| deepcopy_reduce                 | 1.55 us                                                                | 1.53 us: 1.01x faster                                                      |
| logging_silent                  | 65.7 ns                                                                | 64.9 ns: 1.01x faster                                                      |
| xml_etree_generate              | 52.2 ms                                                                | 51.6 ms: 1.01x faster                                                      |
| tomli_loads                     | 1.20 sec                                                               | 1.19 sec: 1.01x faster                                                     |
| docutils                        | 1.40 sec                                                               | 1.38 sec: 1.01x faster                                                     |
| go                              | 77.9 ms                                                                | 77.1 ms: 1.01x faster                                                      |
| 2to3                            | 161 ms                                                                 | 160 ms: 1.01x faster                                                       |
| logging_simple                  | 3.16 us                                                                | 3.13 us: 1.01x faster                                                      |
| sqlite_synth                    | 1.54 us                                                                | 1.52 us: 1.01x faster                                                      |
| genshi_xml                      | 28.2 ms                                                                | 28.0 ms: 1.01x faster                                                      |
| fannkuch                        | 246 ms                                                                 | 245 ms: 1.01x faster                                                       |
| async_tree_eager_memoization    | 141 ms                                                                 | 140 ms: 1.01x faster                                                       |
| bench_thread_pool               | 470 us                                                                 | 468 us: 1.01x faster                                                       |
| json_dumps                      | 7.28 ms                                                                | 7.23 ms: 1.01x faster                                                      |
| scimark_fft                     | 172 ms                                                                 | 171 ms: 1.01x faster                                                       |
| async_tree_eager                | 61.5 ms                                                                | 61.1 ms: 1.01x faster                                                      |
| pyflate                         | 291 ms                                                                 | 289 ms: 1.01x faster                                                       |
| spectral_norm                   | 61.7 ms                                                                | 61.4 ms: 1.00x faster                                                      |
| sqlglot_parse                   | 764 us                                                                 | 760 us: 1.00x faster                                                       |
| subparsers                      | 11.8 ms                                                                | 11.8 ms: 1.00x faster                                                      |
| raytrace                        | 168 ms                                                                 | 168 ms: 1.00x faster                                                       |
| crypto_pyaes                    | 53.0 ms                                                                | 52.8 ms: 1.00x faster                                                      |
| pprint_pformat                  | 914 ms                                                                 | 912 ms: 1.00x faster                                                       |
| unpickle_pure_python            | 136 us                                                                 | 136 us: 1.00x faster                                                       |
| scimark_sor                     | 78.5 ms                                                                | 78.6 ms: 1.00x slower                                                      |
| scimark_sparse_mat_mult         | 2.67 ms                                                                | 2.67 ms: 1.00x slower                                                      |
| connected_components            | 298 ms                                                                 | 299 ms: 1.00x slower                                                       |
| pickle_pure_python              | 196 us                                                                 | 196 us: 1.00x slower                                                       |
| asyncio_websockets              | 242 ms                                                                 | 242 ms: 1.00x slower                                                       |
| richards_super                  | 35.1 ms                                                                | 35.2 ms: 1.00x slower                                                      |
| scimark_lu                      | 72.0 ms                                                                | 72.3 ms: 1.00x slower                                                      |
| meteor_contest                  | 71.1 ms                                                                | 71.5 ms: 1.00x slower                                                      |
| coroutines                      | 16.0 ms                                                                | 16.1 ms: 1.01x slower                                                      |
| richards                        | 31.4 ms                                                                | 31.7 ms: 1.01x slower                                                      |
| json                            | 2.85 ms                                                                | 2.87 ms: 1.01x slower                                                      |
| coverage                        | 45.0 ms                                                                | 45.4 ms: 1.01x slower                                                      |
| regex_dna                       | 135 ms                                                                 | 137 ms: 1.01x slower                                                       |
| regex_effbot                    | 2.05 ms                                                                | 2.08 ms: 1.01x slower                                                      |
| float                           | 46.3 ms                                                                | 46.9 ms: 1.01x slower                                                      |
| regex_v8                        | 15.7 ms                                                                | 16.0 ms: 1.02x slower                                                      |
| async_tree_io_tg                | 352 ms                                                                 | 360 ms: 1.02x slower                                                       |
| mako                            | 6.95 ms                                                                | 7.13 ms: 1.03x slower                                                      |
| Geometric mean                  | (ref)                                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (32): async_tree_none, async_tree_io, pylint, pathlib, async_tree_memoization, k_core, async_tree_none_tg, bench_mp_pool, pycparser, dulwich_log, mypy2, async_tree_eager_io_tg, hexiom, pprint_safe_repr, async_generators, async_tree_memoization_tg, create_gc_cycles, async_tree_eager_io, nbody, async_tree_eager_cpu_io_mixed_tg, pidigits, shortest_path, async_tree_eager_tg, async_tree_cpu_io_mixed, scimark_monte_carlo, json_loads, async_tree_eager_cpu_io_mixed, deepcopy_memo, async_tree_cpu_io_mixed_tg, gc_traversal, xml_etree_parse, xml_etree_iterparse

- Geometric mean (including insignificant results): 1.007x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x