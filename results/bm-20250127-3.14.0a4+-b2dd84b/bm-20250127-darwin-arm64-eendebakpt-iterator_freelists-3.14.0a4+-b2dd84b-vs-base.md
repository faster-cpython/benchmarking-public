# Results vs. base

- fork: eendebakpt
- ref: iterator_freelists
- machine: darwin-arm64
- commit hash: b2dd84b
- commit date: 2025-01-27
- overall geometric mean: 1.003x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250127-darwin-arm64-python-7ec17429d462aee071c0-3.14.0a4+-7ec1742 | bm-20250127-darwin-arm64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 160 ms                                                                 | 187 ms: 1.17x slower                                                     |
| docutils       | 1.41 sec                                                               | 1.40 sec: 1.01x faster                                                   |
| sphinx         | 568 ms                                                                 | 559 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                             |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                    | bm-20250127-darwin-arm64-python-7ec17429d462aee071c0-3.14.0a4+-7ec1742 | bm-20250127-darwin-arm64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|------------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io                | 372 ms                                                                 | 360 ms: 1.03x faster                                                     |
| async_tree_none              | 161 ms                                                                 | 159 ms: 1.01x faster                                                     |
| async_tree_eager_io_tg       | 374 ms                                                                 | 371 ms: 1.01x faster                                                     |
| async_generators             | 250 ms                                                                 | 247 ms: 1.01x faster                                                     |
| async_tree_eager_memoization | 141 ms                                                                 | 140 ms: 1.01x faster                                                     |
| async_tree_cpu_io_mixed      | 416 ms                                                                 | 419 ms: 1.01x slower                                                     |
| async_tree_memoization       | 196 ms                                                                 | 198 ms: 1.01x slower                                                     |
| Geometric mean               | (ref)                                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (12): async_tree_io_tg, async_tree_none_tg, async_tree_memoization_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_io, asyncio_websockets, coroutines, async_tree_eager_cpu_io_mixed_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250127-darwin-arm64-python-7ec17429d462aee071c0-3.14.0a4+-7ec1742 | bm-20250127-darwin-arm64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 68.5 ms                                                                | 68.1 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250127-darwin-arm64-python-7ec17429d462aee071c0-3.14.0a4+-7ec1742 | bm-20250127-darwin-arm64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 140 ms                                                                 | 140 ms: 1.00x faster                                                     |
| regex_compile  | 66.0 ms                                                                | 66.2 ms: 1.00x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                             |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250127-darwin-arm64-python-7ec17429d462aee071c0-3.14.0a4+-7ec1742 | bm-20250127-darwin-arm64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|--------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_process  | 38.4 ms                                                                | 38.0 ms: 1.01x faster                                                    |
| xml_etree_generate | 52.6 ms                                                                | 52.3 ms: 1.01x faster                                                    |
| json_dumps         | 7.23 ms                                                                | 7.40 ms: 1.02x slower                                                    |
| Geometric mean     | (ref)                                                                  | 1.00x slower                                                             |

Benchmark hidden because not significant (6): xml_etree_parse, xml_etree_iterparse, pickle_pure_python, unpickle_pure_python, tomli_loads, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250127-darwin-arm64-python-7ec17429d462aee071c0-3.14.0a4+-7ec1742 | bm-20250127-darwin-arm64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup | 19.8 ms                                                                | 19.6 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250127-darwin-arm64-python-7ec17429d462aee071c0-3.14.0a4+-7ec1742 | bm-20250127-darwin-arm64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 20.9 ms                                                                | 20.3 ms: 1.03x faster                                                    |
| genshi_text     | 13.2 ms                                                                | 13.1 ms: 1.01x faster                                                    |
| genshi_xml      | 28.1 ms                                                                | 28.0 ms: 1.00x faster                                                    |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                    | bm-20250127-darwin-arm64-python-7ec17429d462aee071c0-3.14.0a4+-7ec1742 | bm-20250127-darwin-arm64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|------------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io                | 372 ms                                                                 | 360 ms: 1.03x faster                                                     |
| comprehensions               | 12.1 us                                                                | 11.8 us: 1.03x faster                                                    |
| bpe_tokeniser                | 2.93 sec                                                               | 2.85 sec: 1.03x faster                                                   |
| django_template              | 20.9 ms                                                                | 20.3 ms: 1.03x faster                                                    |
| typing_runtime_protocols     | 94.0 us                                                                | 92.0 us: 1.02x faster                                                    |
| richards_super               | 35.5 ms                                                                | 34.9 ms: 1.02x faster                                                    |
| sqlglot_optimize             | 32.5 ms                                                                | 31.9 ms: 1.02x faster                                                    |
| sympy_expand                 | 233 ms                                                                 | 229 ms: 1.02x faster                                                     |
| sqlglot_normalize            | 179 ms                                                                 | 176 ms: 1.02x faster                                                     |
| sqlalchemy_declarative       | 58.6 ms                                                                | 57.6 ms: 1.02x faster                                                    |
| sphinx                       | 568 ms                                                                 | 559 ms: 1.02x faster                                                     |
| many_optionals               | 438 us                                                                 | 431 us: 1.02x faster                                                     |
| go                           | 78.1 ms                                                                | 77.0 ms: 1.01x faster                                                    |
| async_tree_none              | 161 ms                                                                 | 159 ms: 1.01x faster                                                     |
| meteor_contest               | 70.9 ms                                                                | 70.1 ms: 1.01x faster                                                    |
| thrift                       | 432 us                                                                 | 427 us: 1.01x faster                                                     |
| sympy_integrate              | 11.1 ms                                                                | 11.0 ms: 1.01x faster                                                    |
| sympy_sum                    | 73.4 ms                                                                | 72.6 ms: 1.01x faster                                                    |
| logging_simple               | 3.18 us                                                                | 3.15 us: 1.01x faster                                                    |
| async_tree_eager_io_tg       | 374 ms                                                                 | 371 ms: 1.01x faster                                                     |
| docutils                     | 1.41 sec                                                               | 1.40 sec: 1.01x faster                                                   |
| dulwich_log                  | 27.1 ms                                                                | 26.8 ms: 1.01x faster                                                    |
| xml_etree_process            | 38.4 ms                                                                | 38.0 ms: 1.01x faster                                                    |
| async_generators             | 250 ms                                                                 | 247 ms: 1.01x faster                                                     |
| richards                     | 31.6 ms                                                                | 31.3 ms: 1.01x faster                                                    |
| deltablue                    | 2.31 ms                                                                | 2.29 ms: 1.01x faster                                                    |
| chaos                        | 37.5 ms                                                                | 37.1 ms: 1.01x faster                                                    |
| sympy_str                    | 137 ms                                                                 | 136 ms: 1.01x faster                                                     |
| sqlite_synth                 | 1.54 us                                                                | 1.52 us: 1.01x faster                                                    |
| bench_thread_pool            | 472 us                                                                 | 468 us: 1.01x faster                                                     |
| fannkuch                     | 244 ms                                                                 | 242 ms: 1.01x faster                                                     |
| python_startup               | 19.8 ms                                                                | 19.6 ms: 1.01x faster                                                    |
| pprint_safe_repr             | 458 ms                                                                 | 455 ms: 1.01x faster                                                     |
| genshi_text                  | 13.2 ms                                                                | 13.1 ms: 1.01x faster                                                    |
| logging_format               | 3.49 us                                                                | 3.47 us: 1.01x faster                                                    |
| sqlalchemy_imperative        | 6.43 ms                                                                | 6.39 ms: 1.01x faster                                                    |
| async_tree_eager_memoization | 141 ms                                                                 | 140 ms: 1.01x faster                                                     |
| scimark_lu                   | 72.2 ms                                                                | 71.8 ms: 1.01x faster                                                    |
| bench_mp_pool                | 60.9 ms                                                                | 60.5 ms: 1.01x faster                                                    |
| nbody                        | 68.5 ms                                                                | 68.1 ms: 1.01x faster                                                    |
| pyflate                      | 289 ms                                                                 | 287 ms: 1.01x faster                                                     |
| raytrace                     | 169 ms                                                                 | 168 ms: 1.01x faster                                                     |
| xml_etree_generate           | 52.6 ms                                                                | 52.3 ms: 1.01x faster                                                    |
| nqueens                      | 56.8 ms                                                                | 56.5 ms: 1.01x faster                                                    |
| deepcopy                     | 147 us                                                                 | 147 us: 1.00x faster                                                     |
| genshi_xml                   | 28.1 ms                                                                | 28.0 ms: 1.00x faster                                                    |
| hexiom                       | 4.19 ms                                                                | 4.18 ms: 1.00x faster                                                    |
| scimark_sor                  | 77.2 ms                                                                | 77.0 ms: 1.00x faster                                                    |
| scimark_monte_carlo          | 42.3 ms                                                                | 42.2 ms: 1.00x faster                                                    |
| regex_dna                    | 140 ms                                                                 | 140 ms: 1.00x faster                                                     |
| scimark_sparse_mat_mult      | 2.63 ms                                                                | 2.64 ms: 1.00x slower                                                    |
| scimark_fft                  | 171 ms                                                                 | 172 ms: 1.00x slower                                                     |
| regex_compile                | 66.0 ms                                                                | 66.2 ms: 1.00x slower                                                    |
| generators                   | 22.2 ms                                                                | 22.4 ms: 1.01x slower                                                    |
| async_tree_cpu_io_mixed      | 416 ms                                                                 | 419 ms: 1.01x slower                                                     |
| telco                        | 4.52 ms                                                                | 4.56 ms: 1.01x slower                                                    |
| async_tree_memoization       | 196 ms                                                                 | 198 ms: 1.01x slower                                                     |
| json                         | 2.97 ms                                                                | 3.01 ms: 1.01x slower                                                    |
| pathlib                      | 22.3 ms                                                                | 22.7 ms: 1.02x slower                                                    |
| json_dumps                   | 7.23 ms                                                                | 7.40 ms: 1.02x slower                                                    |
| logging_silent               | 64.6 ns                                                                | 66.6 ns: 1.03x slower                                                    |
| 2to3                         | 160 ms                                                                 | 187 ms: 1.17x slower                                                     |
| Geometric mean               | (ref)                                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (43): pylint, xml_etree_parse, async_tree_io_tg, async_tree_none_tg, pycparser, async_tree_memoization_tg, subparsers, xml_etree_iterparse, coverage, async_tree_eager_memoization_tg, float, async_tree_eager_tg, async_tree_eager, deepcopy_memo, python_startup_no_site, async_tree_eager_cpu_io_mixed, dask, create_gc_cycles, pprint_pformat, spectral_norm, shortest_path, async_tree_eager_io, pickle_pure_python, unpickle_pure_python, crypto_pyaes, regex_v8, regex_effbot, pidigits, asyncio_websockets, deepcopy_reduce, mako, coroutines, sqlglot_parse, html5lib, sqlglot_transpile, async_tree_eager_cpu_io_mixed_tg, connected_components, tomli_loads, mdp, async_tree_cpu_io_mixed_tg, json_loads, gc_traversal, k_core

- Geometric mean (including insignificant results): 1.003x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x