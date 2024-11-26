# Results vs. base

- fork: brandtbucher
- ref: justin_likely
- machine: darwin-arm64
- commit hash: bad9944
- commit date: 2024-10-18
- overall geometric mean: 1.001x faster
- HPT reliability: 97.29%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 188 ms                                                                 | 183 ms: 1.03x faster                                                  |
| docutils       | 1.57 sec                                                               | 1.58 sec: 1.00x slower                                                |
| html5lib       | 34.3 ms                                                                | 33.9 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (2): sphinx, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager | 64.3 ms                                                                | 63.4 ms: 1.01x faster                                                 |
| async_generators | 293 ms                                                                 | 292 ms: 1.00x faster                                                  |
| async_tree_io_tg | 612 ms                                                                 | 611 ms: 1.00x faster                                                  |
| Geometric mean   | (ref)                                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (18): async_tree_memoization, coroutines, async_tree_eager_memoization, async_tree_memoization_tg, async_tree_none, async_tree_io, async_tree_eager_io, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_eager_cpu_io_mixed, async_tree_eager_memoization_tg, asyncio_websockets, async_tree_eager_tg, async_tree_eager_io_tg, async_tree_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, asyncio_tcp, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 48.5 ms                                                                | 48.2 ms: 1.01x faster                                                 |
| pidigits       | 283 ms                                                                 | 283 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 152 ms                                                                 | 149 ms: 1.02x faster                                                  |
| regex_effbot   | 2.68 ms                                                                | 2.65 ms: 1.01x faster                                                 |
| regex_compile  | 75.9 ms                                                                | 75.4 ms: 1.01x faster                                                 |
| regex_v8       | 17.1 ms                                                                | 17.0 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_list          | 2.89 us                                                                | 2.87 us: 1.01x faster                                                 |
| json_loads           | 16.6 us                                                                | 16.5 us: 1.00x faster                                                 |
| pickle_pure_python   | 179 us                                                                 | 179 us: 1.00x faster                                                  |
| xml_etree_generate   | 50.5 ms                                                                | 50.6 ms: 1.00x slower                                                 |
| unpickle_pure_python | 132 us                                                                 | 132 us: 1.00x slower                                                  |
| pickle               | 7.30 us                                                                | 7.34 us: 1.01x slower                                                 |
| unpickle             | 9.00 us                                                                | 9.06 us: 1.01x slower                                                 |
| xml_etree_process    | 34.6 ms                                                                | 34.9 ms: 1.01x slower                                                 |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (6): tomli_loads, xml_etree_parse, unpickle_list, json_dumps, pickle_dict, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 14.9 ms                                                                | 14.7 ms: 1.01x faster                                                 |
| python_startup         | 19.1 ms                                                                | 18.9 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.8 ms                                                                | 16.1 ms: 1.04x faster                                                 |
| genshi_xml      | 43.3 ms                                                                | 42.1 ms: 1.03x faster                                                 |
| django_template | 23.0 ms                                                                | 22.7 ms: 1.01x faster                                                 |
| Geometric mean  | (ref)                                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|-------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text             | 16.8 ms                                                                | 16.1 ms: 1.04x faster                                                 |
| genshi_xml              | 43.3 ms                                                                | 42.1 ms: 1.03x faster                                                 |
| 2to3                    | 188 ms                                                                 | 183 ms: 1.03x faster                                                  |
| pprint_safe_repr        | 500 ms                                                                 | 490 ms: 1.02x faster                                                  |
| regex_dna               | 152 ms                                                                 | 149 ms: 1.02x faster                                                  |
| go                      | 99.5 ms                                                                | 97.9 ms: 1.02x faster                                                 |
| async_tree_eager        | 64.3 ms                                                                | 63.4 ms: 1.01x faster                                                 |
| json                    | 2.88 ms                                                                | 2.84 ms: 1.01x faster                                                 |
| django_template         | 23.0 ms                                                                | 22.7 ms: 1.01x faster                                                 |
| python_startup_no_site  | 14.9 ms                                                                | 14.7 ms: 1.01x faster                                                 |
| sqlglot_normalize       | 186 ms                                                                 | 184 ms: 1.01x faster                                                  |
| sqlglot_optimize        | 37.7 ms                                                                | 37.2 ms: 1.01x faster                                                 |
| html5lib                | 34.3 ms                                                                | 33.9 ms: 1.01x faster                                                 |
| scimark_sparse_mat_mult | 3.19 ms                                                                | 3.16 ms: 1.01x faster                                                 |
| sqlglot_parse           | 879 us                                                                 | 871 us: 1.01x faster                                                  |
| sympy_sum               | 80.0 ms                                                                | 79.2 ms: 1.01x faster                                                 |
| python_startup          | 19.1 ms                                                                | 18.9 ms: 1.01x faster                                                 |
| regex_effbot            | 2.68 ms                                                                | 2.65 ms: 1.01x faster                                                 |
| scimark_lu              | 65.1 ms                                                                | 64.6 ms: 1.01x faster                                                 |
| pickle_list             | 2.89 us                                                                | 2.87 us: 1.01x faster                                                 |
| bench_thread_pool       | 476 us                                                                 | 473 us: 1.01x faster                                                  |
| chaos                   | 41.6 ms                                                                | 41.3 ms: 1.01x faster                                                 |
| regex_compile           | 75.9 ms                                                                | 75.4 ms: 1.01x faster                                                 |
| sqlite_synth            | 1.54 us                                                                | 1.54 us: 1.01x faster                                                 |
| bench_mp_pool           | 62.4 ms                                                                | 62.0 ms: 1.01x faster                                                 |
| spectral_norm           | 69.8 ms                                                                | 69.4 ms: 1.01x faster                                                 |
| float                   | 48.5 ms                                                                | 48.2 ms: 1.01x faster                                                 |
| dulwich_log             | 28.8 ms                                                                | 28.7 ms: 1.00x faster                                                 |
| scimark_fft             | 191 ms                                                                 | 190 ms: 1.00x faster                                                  |
| bpe_tokeniser           | 3.05 sec                                                               | 3.03 sec: 1.00x faster                                                |
| json_loads              | 16.6 us                                                                | 16.5 us: 1.00x faster                                                 |
| regex_v8                | 17.1 ms                                                                | 17.0 ms: 1.00x faster                                                 |
| pickle_pure_python      | 179 us                                                                 | 179 us: 1.00x faster                                                  |
| async_generators        | 293 ms                                                                 | 292 ms: 1.00x faster                                                  |
| sympy_integrate         | 12.6 ms                                                                | 12.6 ms: 1.00x faster                                                 |
| crypto_pyaes            | 53.8 ms                                                                | 53.7 ms: 1.00x faster                                                 |
| async_tree_io_tg        | 612 ms                                                                 | 611 ms: 1.00x faster                                                  |
| pidigits                | 283 ms                                                                 | 283 ms: 1.00x faster                                                  |
| hexiom                  | 4.93 ms                                                                | 4.94 ms: 1.00x slower                                                 |
| sympy_expand            | 246 ms                                                                 | 247 ms: 1.00x slower                                                  |
| xml_etree_generate      | 50.5 ms                                                                | 50.6 ms: 1.00x slower                                                 |
| scimark_sor             | 85.7 ms                                                                | 85.9 ms: 1.00x slower                                                 |
| unpickle_pure_python    | 132 us                                                                 | 132 us: 1.00x slower                                                  |
| pyflate                 | 325 ms                                                                 | 326 ms: 1.00x slower                                                  |
| docutils                | 1.57 sec                                                               | 1.58 sec: 1.00x slower                                                |
| pickle                  | 7.30 us                                                                | 7.34 us: 1.01x slower                                                 |
| deltablue               | 2.40 ms                                                                | 2.41 ms: 1.01x slower                                                 |
| logging_format          | 3.38 us                                                                | 3.40 us: 1.01x slower                                                 |
| coverage                | 43.5 ms                                                                | 43.8 ms: 1.01x slower                                                 |
| pycparser               | 678 ms                                                                 | 683 ms: 1.01x slower                                                  |
| unpickle                | 9.00 us                                                                | 9.06 us: 1.01x slower                                                 |
| thrift                  | 421 us                                                                 | 424 us: 1.01x slower                                                  |
| deepcopy_memo           | 16.9 us                                                                | 17.0 us: 1.01x slower                                                 |
| nqueens                 | 58.2 ms                                                                | 58.6 ms: 1.01x slower                                                 |
| telco                   | 4.53 ms                                                                | 4.57 ms: 1.01x slower                                                 |
| logging_simple          | 3.10 us                                                                | 3.12 us: 1.01x slower                                                 |
| create_gc_cycles        | 1.31 ms                                                                | 1.32 ms: 1.01x slower                                                 |
| xml_etree_process       | 34.6 ms                                                                | 34.9 ms: 1.01x slower                                                 |
| mdp                     | 1.54 sec                                                               | 1.56 sec: 1.01x slower                                                |
| raytrace                | 172 ms                                                                 | 174 ms: 1.01x slower                                                  |
| deepcopy_reduce         | 1.52 us                                                                | 1.55 us: 1.02x slower                                                 |
| fannkuch                | 261 ms                                                                 | 266 ms: 1.02x slower                                                  |
| richards_super          | 37.4 ms                                                                | 39.3 ms: 1.05x slower                                                 |
| richards                | 33.7 ms                                                                | 35.6 ms: 1.06x slower                                                 |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (42): async_tree_memoization, coroutines, async_tree_eager_memoization, async_tree_memoization_tg, async_tree_none, async_tree_io, tomli_loads, async_tree_eager_io, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_eager_cpu_io_mixed, pylint, xml_etree_parse, gc_traversal, pathlib, async_tree_eager_memoization_tg, meteor_contest, asyncio_websockets, async_tree_eager_tg, async_tree_eager_io_tg, nbody, pprint_pformat, comprehensions, async_tree_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, scimark_monte_carlo, mako, sqlglot_transpile, generators, unpickle_list, asyncio_tcp, json_dumps, logging_silent, sphinx, pickle_dict, deepcopy, unpack_sequence, sympy_str, typing_runtime_protocols, xml_etree_iterparse, asyncio_tcp_ssl, tornado_http

- Geometric mean (including insignificant results): 1.001x faster
# HPT report

- Reliability score: 97.29% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x