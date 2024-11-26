# Results vs. base

- fork: brandtbucher
- ref: justin_unlikely
- machine: darwin-arm64
- commit hash: 15229e0
- commit date: 2024-10-17
- overall geometric mean: 1.001x slower
- HPT reliability: 96.17%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 188 ms                                                                 | 183 ms: 1.03x faster                                                    |
| docutils       | 1.57 sec                                                               | 1.58 sec: 1.00x slower                                                  |
| html5lib       | 34.3 ms                                                                | 34.0 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                            |

Benchmark hidden because not significant (2): sphinx, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark           | bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|---------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_eager    | 64.3 ms                                                                | 63.4 ms: 1.01x faster                                                   |
| async_tree_eager_tg | 42.8 ms                                                                | 42.4 ms: 1.01x faster                                                   |
| async_tree_io_tg    | 612 ms                                                                 | 613 ms: 1.00x slower                                                    |
| async_generators    | 293 ms                                                                 | 295 ms: 1.01x slower                                                    |
| Geometric mean      | (ref)                                                                  | 1.00x slower                                                            |

Benchmark hidden because not significant (17): async_tree_eager_memoization, async_tree_eager_cpu_io_mixed, async_tree_memoization_tg, async_tree_memoization, asyncio_websockets, async_tree_none, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_eager_memoization_tg, async_tree_eager_io_tg, async_tree_eager_io, async_tree_none_tg, coroutines, async_tree_eager_cpu_io_mixed_tg, asyncio_tcp, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 48.5 ms                                                                | 48.4 ms: 1.00x faster                                                   |
| nbody          | 65.3 ms                                                                | 65.5 ms: 1.00x slower                                                   |
| pidigits       | 283 ms                                                                 | 284 ms: 1.00x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 152 ms                                                                 | 148 ms: 1.03x faster                                                    |
| regex_effbot   | 2.68 ms                                                                | 2.63 ms: 1.02x faster                                                   |
| regex_v8       | 17.1 ms                                                                | 16.9 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                            |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|--------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_list        | 2.89 us                                                                | 2.86 us: 1.01x faster                                                   |
| pickle             | 7.30 us                                                                | 7.32 us: 1.00x slower                                                   |
| pickle_dict        | 18.2 us                                                                | 18.2 us: 1.00x slower                                                   |
| pickle_pure_python | 179 us                                                                 | 180 us: 1.01x slower                                                    |
| xml_etree_generate | 50.5 ms                                                                | 50.8 ms: 1.01x slower                                                   |
| xml_etree_process  | 34.6 ms                                                                | 35.0 ms: 1.01x slower                                                   |
| unpickle           | 9.00 us                                                                | 9.13 us: 1.01x slower                                                   |
| Geometric mean     | (ref)                                                                  | 1.00x slower                                                            |

Benchmark hidden because not significant (7): json_loads, unpickle_list, unpickle_pure_python, xml_etree_parse, json_dumps, xml_etree_iterparse, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 14.9 ms                                                                | 14.8 ms: 1.00x faster                                                   |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                            |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 43.3 ms                                                                | 42.9 ms: 1.01x faster                                                   |
| django_template | 23.0 ms                                                                | 22.8 ms: 1.01x faster                                                   |
| mako            | 6.46 ms                                                                | 6.48 ms: 1.00x slower                                                   |
| genshi_text     | 16.8 ms                                                                | 17.0 ms: 1.01x slower                                                   |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                            |

All benchmarks:
===============

| Benchmark              | bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna              | 152 ms                                                                 | 148 ms: 1.03x faster                                                    |
| 2to3                   | 188 ms                                                                 | 183 ms: 1.03x faster                                                    |
| regex_effbot           | 2.68 ms                                                                | 2.63 ms: 1.02x faster                                                   |
| async_tree_eager       | 64.3 ms                                                                | 63.4 ms: 1.01x faster                                                   |
| go                     | 99.5 ms                                                                | 98.2 ms: 1.01x faster                                                   |
| async_tree_eager_tg    | 42.8 ms                                                                | 42.4 ms: 1.01x faster                                                   |
| regex_v8               | 17.1 ms                                                                | 16.9 ms: 1.01x faster                                                   |
| pickle_list            | 2.89 us                                                                | 2.86 us: 1.01x faster                                                   |
| bench_mp_pool          | 62.4 ms                                                                | 61.8 ms: 1.01x faster                                                   |
| genshi_xml             | 43.3 ms                                                                | 42.9 ms: 1.01x faster                                                   |
| pprint_safe_repr       | 500 ms                                                                 | 496 ms: 1.01x faster                                                    |
| comprehensions         | 13.1 us                                                                | 12.9 us: 1.01x faster                                                   |
| html5lib               | 34.3 ms                                                                | 34.0 ms: 1.01x faster                                                   |
| django_template        | 23.0 ms                                                                | 22.8 ms: 1.01x faster                                                   |
| sympy_sum              | 80.0 ms                                                                | 79.3 ms: 1.01x faster                                                   |
| scimark_lu             | 65.1 ms                                                                | 64.6 ms: 1.01x faster                                                   |
| sqlglot_parse          | 879 us                                                                 | 873 us: 1.01x faster                                                    |
| sqlglot_optimize       | 37.7 ms                                                                | 37.5 ms: 1.01x faster                                                   |
| logging_silent         | 70.2 ns                                                                | 69.9 ns: 1.00x faster                                                   |
| sqlite_synth           | 1.54 us                                                                | 1.54 us: 1.00x faster                                                   |
| python_startup_no_site | 14.9 ms                                                                | 14.8 ms: 1.00x faster                                                   |
| bench_thread_pool      | 476 us                                                                 | 475 us: 1.00x faster                                                    |
| float                  | 48.5 ms                                                                | 48.4 ms: 1.00x faster                                                   |
| async_tree_io_tg       | 612 ms                                                                 | 613 ms: 1.00x slower                                                    |
| scimark_fft            | 191 ms                                                                 | 191 ms: 1.00x slower                                                    |
| pickle                 | 7.30 us                                                                | 7.32 us: 1.00x slower                                                   |
| sympy_expand           | 246 ms                                                                 | 247 ms: 1.00x slower                                                    |
| docutils               | 1.57 sec                                                               | 1.58 sec: 1.00x slower                                                  |
| nbody                  | 65.3 ms                                                                | 65.5 ms: 1.00x slower                                                   |
| pidigits               | 283 ms                                                                 | 284 ms: 1.00x slower                                                    |
| mako                   | 6.46 ms                                                                | 6.48 ms: 1.00x slower                                                   |
| sympy_str              | 151 ms                                                                 | 151 ms: 1.00x slower                                                    |
| pickle_dict            | 18.2 us                                                                | 18.2 us: 1.00x slower                                                   |
| hexiom                 | 4.93 ms                                                                | 4.95 ms: 1.00x slower                                                   |
| sqlglot_transpile      | 1.06 ms                                                                | 1.07 ms: 1.00x slower                                                   |
| scimark_sor            | 85.7 ms                                                                | 86.1 ms: 1.00x slower                                                   |
| deltablue              | 2.40 ms                                                                | 2.41 ms: 1.00x slower                                                   |
| mdp                    | 1.54 sec                                                               | 1.55 sec: 1.00x slower                                                  |
| logging_format         | 3.38 us                                                                | 3.40 us: 1.00x slower                                                   |
| pickle_pure_python     | 179 us                                                                 | 180 us: 1.01x slower                                                    |
| crypto_pyaes           | 53.8 ms                                                                | 54.1 ms: 1.01x slower                                                   |
| raytrace               | 172 ms                                                                 | 173 ms: 1.01x slower                                                    |
| chaos                  | 41.6 ms                                                                | 41.8 ms: 1.01x slower                                                   |
| scimark_monte_carlo    | 45.6 ms                                                                | 45.9 ms: 1.01x slower                                                   |
| xml_etree_generate     | 50.5 ms                                                                | 50.8 ms: 1.01x slower                                                   |
| deepcopy               | 155 us                                                                 | 156 us: 1.01x slower                                                    |
| pycparser              | 678 ms                                                                 | 683 ms: 1.01x slower                                                    |
| genshi_text            | 16.8 ms                                                                | 17.0 ms: 1.01x slower                                                   |
| pyflate                | 325 ms                                                                 | 327 ms: 1.01x slower                                                    |
| async_generators       | 293 ms                                                                 | 295 ms: 1.01x slower                                                    |
| pathlib                | 22.2 ms                                                                | 22.4 ms: 1.01x slower                                                   |
| xml_etree_process      | 34.6 ms                                                                | 35.0 ms: 1.01x slower                                                   |
| unpack_sequence        | 76.1 ns                                                                | 77.0 ns: 1.01x slower                                                   |
| thrift                 | 421 us                                                                 | 426 us: 1.01x slower                                                    |
| pprint_pformat         | 1.00 sec                                                               | 1.02 sec: 1.01x slower                                                  |
| unpickle               | 9.00 us                                                                | 9.13 us: 1.01x slower                                                   |
| bpe_tokeniser          | 3.05 sec                                                               | 3.09 sec: 1.01x slower                                                  |
| fannkuch               | 261 ms                                                                 | 266 ms: 1.02x slower                                                    |
| deepcopy_reduce        | 1.52 us                                                                | 1.56 us: 1.02x slower                                                   |
| telco                  | 4.53 ms                                                                | 4.67 ms: 1.03x slower                                                   |
| richards_super         | 37.4 ms                                                                | 38.7 ms: 1.04x slower                                                   |
| richards               | 33.7 ms                                                                | 35.2 ms: 1.04x slower                                                   |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                            |

Benchmark hidden because not significant (44): generators, sphinx, json_loads, async_tree_eager_memoization, async_tree_eager_cpu_io_mixed, async_tree_memoization_tg, unpickle_list, async_tree_memoization, regex_compile, asyncio_websockets, spectral_norm, gc_traversal, async_tree_none, dulwich_log, json, async_tree_io, deepcopy_memo, async_tree_cpu_io_mixed_tg, coverage, scimark_sparse_mat_mult, async_tree_cpu_io_mixed, async_tree_eager_memoization_tg, unpickle_pure_python, async_tree_eager_io_tg, nqueens, xml_etree_parse, create_gc_cycles, json_dumps, sqlglot_normalize, meteor_contest, logging_simple, async_tree_eager_io, async_tree_none_tg, coroutines, async_tree_eager_cpu_io_mixed_tg, xml_etree_iterparse, python_startup, sympy_integrate, typing_runtime_protocols, tomli_loads, asyncio_tcp, asyncio_tcp_ssl, tornado_http, pylint

- Geometric mean (including insignificant results): 1.001x slower
# HPT report

- Reliability score: 96.17% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x