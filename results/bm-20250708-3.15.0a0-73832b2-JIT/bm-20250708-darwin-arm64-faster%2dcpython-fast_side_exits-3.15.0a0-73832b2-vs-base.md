# Results vs. base

- fork: faster-cpython
- ref: fast_side_exits
- machine: darwin-arm64
- commit hash: 73832b2
- commit date: 2025-07-08
- overall geometric mean: 1.002x faster
- HPT reliability: 95.44%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250707-darwin-arm64-python-cb99d992774b67761441-3.15.0a0-cb99d99 | bm-20250708-darwin-arm64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 173 ms                                                                | 171 ms: 1.01x faster                                                       |
| docutils       | 1.47 sec                                                              | 1.46 sec: 1.01x faster                                                     |
| sphinx         | 590 ms                                                                | 583 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20250707-darwin-arm64-python-cb99d992774b67761441-3.15.0a0-cb99d99 | bm-20250708-darwin-arm64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_eager | 64.0 ms                                                               | 63.6 ms: 1.01x faster                                                      |
| async_generators | 278 ms                                                                | 283 ms: 1.02x slower                                                       |
| Geometric mean   | (ref)                                                                 | 1.00x faster                                                               |

Benchmark hidden because not significant (17): async_tree_none, async_tree_memoization, coroutines, asyncio_websockets, async_tree_eager_cpu_io_mixed_tg, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_eager_cpu_io_mixed, async_tree_io_tg, async_tree_eager_memoization, async_tree_io, async_tree_eager_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250707-darwin-arm64-python-cb99d992774b67761441-3.15.0a0-cb99d99 | bm-20250708-darwin-arm64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 75.4 ms                                                               | 75.6 ms: 1.00x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                               |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250707-darwin-arm64-python-cb99d992774b67761441-3.15.0a0-cb99d99 | bm-20250708-darwin-arm64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 143 ms                                                                | 138 ms: 1.03x faster                                                       |
| regex_v8       | 16.1 ms                                                               | 15.6 ms: 1.03x faster                                                      |
| regex_effbot   | 2.33 ms                                                               | 2.34 ms: 1.00x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                               |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250707-darwin-arm64-python-cb99d992774b67761441-3.15.0a0-cb99d99 | bm-20250708-darwin-arm64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.24 sec                                                              | 1.24 sec: 1.01x faster                                                     |
| json_dumps           | 6.59 ms                                                               | 6.55 ms: 1.01x faster                                                      |
| pickle_pure_python   | 210 us                                                                | 210 us: 1.00x faster                                                       |
| unpickle_pure_python | 134 us                                                                | 135 us: 1.00x slower                                                       |
| xml_etree_generate   | 50.6 ms                                                               | 50.8 ms: 1.00x slower                                                      |
| xml_etree_process    | 35.6 ms                                                               | 35.7 ms: 1.00x slower                                                      |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                               |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_iterparse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250707-darwin-arm64-python-cb99d992774b67761441-3.15.0a0-cb99d99 | bm-20250708-darwin-arm64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 18.9 ms                                                               | 18.9 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250707-darwin-arm64-python-cb99d992774b67761441-3.15.0a0-cb99d99 | bm-20250708-darwin-arm64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako           | 6.93 ms                                                               | 6.92 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                               |

Benchmark hidden because not significant (3): genshi_text, django_template, genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20250707-darwin-arm64-python-cb99d992774b67761441-3.15.0a0-cb99d99 | bm-20250708-darwin-arm64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| gc_traversal             | 3.35 ms                                                               | 3.19 ms: 1.05x faster                                                      |
| regex_dna                | 143 ms                                                                | 138 ms: 1.03x faster                                                       |
| richards_super           | 40.5 ms                                                               | 39.3 ms: 1.03x faster                                                      |
| fannkuch                 | 302 ms                                                                | 292 ms: 1.03x faster                                                       |
| regex_v8                 | 16.1 ms                                                               | 15.6 ms: 1.03x faster                                                      |
| spectral_norm            | 68.5 ms                                                               | 66.8 ms: 1.02x faster                                                      |
| richards                 | 35.9 ms                                                               | 35.2 ms: 1.02x faster                                                      |
| pycparser                | 706 ms                                                                | 692 ms: 1.02x faster                                                       |
| sphinx                   | 590 ms                                                                | 583 ms: 1.01x faster                                                       |
| many_optionals           | 479 us                                                                | 475 us: 1.01x faster                                                       |
| sqlglot_v2_normalize     | 69.6 ms                                                               | 68.9 ms: 1.01x faster                                                      |
| logging_format           | 3.75 us                                                               | 3.71 us: 1.01x faster                                                      |
| 2to3                     | 173 ms                                                                | 171 ms: 1.01x faster                                                       |
| sqlite_synth             | 1.59 us                                                               | 1.58 us: 1.01x faster                                                      |
| scimark_fft              | 200 ms                                                                | 198 ms: 1.01x faster                                                       |
| docutils                 | 1.47 sec                                                              | 1.46 sec: 1.01x faster                                                     |
| tomli_loads              | 1.24 sec                                                              | 1.24 sec: 1.01x faster                                                     |
| async_tree_eager         | 64.0 ms                                                               | 63.6 ms: 1.01x faster                                                      |
| json_dumps               | 6.59 ms                                                               | 6.55 ms: 1.01x faster                                                      |
| scimark_sparse_mat_mult  | 3.57 ms                                                               | 3.55 ms: 1.01x faster                                                      |
| python_startup           | 18.9 ms                                                               | 18.9 ms: 1.00x faster                                                      |
| shortest_path            | 338 ms                                                                | 337 ms: 1.00x faster                                                       |
| deepcopy_memo            | 19.6 us                                                               | 19.6 us: 1.00x faster                                                      |
| thrift                   | 443 us                                                                | 441 us: 1.00x faster                                                       |
| nqueens                  | 61.7 ms                                                               | 61.5 ms: 1.00x faster                                                      |
| pickle_pure_python       | 210 us                                                                | 210 us: 1.00x faster                                                       |
| mako                     | 6.93 ms                                                               | 6.92 ms: 1.00x faster                                                      |
| logging_silent           | 72.1 ns                                                               | 72.2 ns: 1.00x slower                                                      |
| regex_effbot             | 2.33 ms                                                               | 2.34 ms: 1.00x slower                                                      |
| bpe_tokeniser            | 3.07 sec                                                              | 3.07 sec: 1.00x slower                                                     |
| scimark_lu               | 82.0 ms                                                               | 82.2 ms: 1.00x slower                                                      |
| sqlglot_v2_parse         | 801 us                                                                | 803 us: 1.00x slower                                                       |
| nbody                    | 75.4 ms                                                               | 75.6 ms: 1.00x slower                                                      |
| unpickle_pure_python     | 134 us                                                                | 135 us: 1.00x slower                                                       |
| scimark_sor              | 88.4 ms                                                               | 88.7 ms: 1.00x slower                                                      |
| telco                    | 4.58 ms                                                               | 4.60 ms: 1.00x slower                                                      |
| go                       | 86.9 ms                                                               | 87.3 ms: 1.00x slower                                                      |
| xml_etree_generate       | 50.6 ms                                                               | 50.8 ms: 1.00x slower                                                      |
| xml_etree_process        | 35.6 ms                                                               | 35.7 ms: 1.00x slower                                                      |
| sympy_integrate          | 11.1 ms                                                               | 11.1 ms: 1.00x slower                                                      |
| dulwich_log              | 25.0 ms                                                               | 25.2 ms: 1.01x slower                                                      |
| logging_simple           | 3.42 us                                                               | 3.44 us: 1.01x slower                                                      |
| coverage                 | 48.2 ms                                                               | 48.5 ms: 1.01x slower                                                      |
| deltablue                | 2.60 ms                                                               | 2.62 ms: 1.01x slower                                                      |
| typing_runtime_protocols | 98.0 us                                                               | 98.9 us: 1.01x slower                                                      |
| sqlglot_v2_optimize      | 33.9 ms                                                               | 34.2 ms: 1.01x slower                                                      |
| pprint_safe_repr         | 527 ms                                                                | 532 ms: 1.01x slower                                                       |
| meteor_contest           | 76.8 ms                                                               | 77.5 ms: 1.01x slower                                                      |
| pprint_pformat           | 1.06 sec                                                              | 1.08 sec: 1.02x slower                                                     |
| async_generators         | 278 ms                                                                | 283 ms: 1.02x slower                                                       |
| comprehensions           | 12.0 us                                                               | 12.4 us: 1.03x slower                                                      |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                               |

Benchmark hidden because not significant (50): xml_etree_parse, async_tree_none, html5lib, xml_etree_iterparse, json, sympy_str, async_tree_memoization, coroutines, asyncio_websockets, async_tree_eager_cpu_io_mixed_tg, subparsers, async_tree_none_tg, k_core, async_tree_cpu_io_mixed, chaos, python_startup_no_site, async_tree_eager_cpu_io_mixed, async_tree_io_tg, genshi_text, async_tree_eager_memoization, async_tree_io, scimark_monte_carlo, deepcopy, async_tree_eager_tg, dask, json_loads, async_tree_cpu_io_mixed_tg, generators, pidigits, float, pyflate, connected_components, pathlib, async_tree_memoization_tg, crypto_pyaes, raytrace, mdp, sympy_expand, regex_compile, async_tree_eager_io_tg, django_template, async_tree_eager_memoization_tg, deepcopy_reduce, async_tree_eager_io, sqlglot_v2_transpile, hexiom, genshi_xml, sympy_sum, create_gc_cycles, pylint

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 95.44% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x