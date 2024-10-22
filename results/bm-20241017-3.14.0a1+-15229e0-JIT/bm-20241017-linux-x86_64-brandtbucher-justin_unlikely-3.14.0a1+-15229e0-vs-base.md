# Results vs. base

- fork: brandtbucher
- ref: justin_unlikely
- machine: linux-x86_64
- commit hash: 15229e0
- commit date: 2024-10-17
- overall geometric mean: 1.00x faster
- HPT reliability: 50.44%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 2.91 sec                                                               | 2.92 sec: 1.00x slower                                                  |
| html5lib       | 64.7 ms                                                                | 63.4 ms: 1.02x faster                                                   |
| tornado_http   | 94.5 ms                                                                | 95.4 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                            |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| coroutines       | 23.0 ms                                                                | 22.8 ms: 1.01x faster                                                   |
| asyncio_tcp_ssl  | 1.81 sec                                                               | 1.80 sec: 1.00x faster                                                  |
| asyncio_tcp      | 498 ms                                                                 | 500 ms: 1.00x slower                                                    |
| async_generators | 453 ms                                                                 | 461 ms: 1.02x slower                                                    |
| Geometric mean   | (ref)                                                                  | 1.00x faster                                                            |

Benchmark hidden because not significant (9): async_tree_none, async_tree_none_tg, async_tree_memoization, async_tree_io, async_tree_io_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 75.6 ms                                                                | 75.3 ms: 1.00x faster                                                   |
| pidigits       | 186 ms                                                                 | 187 ms: 1.00x slower                                                    |
| nbody          | 80.1 ms                                                                | 80.9 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 25.5 ms                                                                | 24.5 ms: 1.04x faster                                                   |
| regex_effbot   | 3.81 ms                                                                | 3.78 ms: 1.01x faster                                                   |
| regex_dna      | 217 ms                                                                 | 216 ms: 1.01x faster                                                    |
| regex_compile  | 142 ms                                                                 | 141 ms: 1.00x faster                                                    |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|---------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_list       | 5.45 us                                                                | 5.30 us: 1.03x faster                                                   |
| pickle_pure_python  | 311 us                                                                 | 309 us: 1.01x faster                                                    |
| xml_etree_process   | 55.4 ms                                                                | 55.0 ms: 1.01x faster                                                   |
| xml_etree_generate  | 79.0 ms                                                                | 78.5 ms: 1.01x faster                                                   |
| xml_etree_iterparse | 99.5 ms                                                                | 99.1 ms: 1.00x faster                                                   |
| pickle              | 11.5 us                                                                | 11.8 us: 1.03x slower                                                   |
| pickle_list         | 5.02 us                                                                | 5.16 us: 1.03x slower                                                   |
| pickle_dict         | 33.6 us                                                                | 35.8 us: 1.06x slower                                                   |
| Geometric mean      | (ref)                                                                  | 1.01x slower                                                            |

Benchmark hidden because not significant (6): unpickle_pure_python, json_dumps, json_loads, tomli_loads, unpickle, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 7.08 ms                                                                | 7.09 ms: 1.00x slower                                                   |
| python_startup         | 11.9 ms                                                                | 11.9 ms: 1.00x slower                                                   |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 58.6 ms                                                                | 59.7 ms: 1.02x slower                                                   |
| django_template | 35.9 ms                                                                | 36.9 ms: 1.03x slower                                                   |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                            |

Benchmark hidden because not significant (2): mako, genshi_text

All benchmarks:
===============

| Benchmark              | bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                    | 2.75 sec                                                               | 2.54 sec: 1.09x faster                                                  |
| regex_v8               | 25.5 ms                                                                | 24.5 ms: 1.04x faster                                                   |
| unpickle_list          | 5.45 us                                                                | 5.30 us: 1.03x faster                                                   |
| chaos                  | 59.4 ms                                                                | 57.9 ms: 1.03x faster                                                   |
| gc_traversal           | 4.57 ms                                                                | 4.45 ms: 1.03x faster                                                   |
| logging_simple         | 5.74 us                                                                | 5.59 us: 1.03x faster                                                   |
| pycparser              | 1.20 sec                                                               | 1.18 sec: 1.02x faster                                                  |
| logging_format         | 6.26 us                                                                | 6.12 us: 1.02x faster                                                   |
| deepcopy_reduce        | 2.77 us                                                                | 2.71 us: 1.02x faster                                                   |
| html5lib               | 64.7 ms                                                                | 63.4 ms: 1.02x faster                                                   |
| scimark_sor            | 120 ms                                                                 | 118 ms: 1.02x faster                                                    |
| richards_super         | 47.8 ms                                                                | 47.0 ms: 1.02x faster                                                   |
| thrift                 | 794 us                                                                 | 783 us: 1.01x faster                                                    |
| comprehensions         | 17.1 us                                                                | 16.9 us: 1.01x faster                                                   |
| crypto_pyaes           | 67.2 ms                                                                | 66.4 ms: 1.01x faster                                                   |
| coroutines             | 23.0 ms                                                                | 22.8 ms: 1.01x faster                                                   |
| create_gc_cycles       | 2.69 ms                                                                | 2.67 ms: 1.01x faster                                                   |
| regex_effbot           | 3.81 ms                                                                | 3.78 ms: 1.01x faster                                                   |
| pickle_pure_python     | 311 us                                                                 | 309 us: 1.01x faster                                                    |
| generators             | 35.5 ms                                                                | 35.3 ms: 1.01x faster                                                   |
| deltablue              | 3.28 ms                                                                | 3.26 ms: 1.01x faster                                                   |
| xml_etree_process      | 55.4 ms                                                                | 55.0 ms: 1.01x faster                                                   |
| regex_dna              | 217 ms                                                                 | 216 ms: 1.01x faster                                                    |
| xml_etree_generate     | 79.0 ms                                                                | 78.5 ms: 1.01x faster                                                   |
| regex_compile          | 142 ms                                                                 | 141 ms: 1.00x faster                                                    |
| hexiom                 | 7.01 ms                                                                | 6.98 ms: 1.00x faster                                                   |
| xml_etree_iterparse    | 99.5 ms                                                                | 99.1 ms: 1.00x faster                                                   |
| asyncio_tcp_ssl        | 1.81 sec                                                               | 1.80 sec: 1.00x faster                                                  |
| float                  | 75.6 ms                                                                | 75.3 ms: 1.00x faster                                                   |
| python_startup_no_site | 7.08 ms                                                                | 7.09 ms: 1.00x slower                                                   |
| python_startup         | 11.9 ms                                                                | 11.9 ms: 1.00x slower                                                   |
| docutils               | 2.91 sec                                                               | 2.92 sec: 1.00x slower                                                  |
| asyncio_tcp            | 498 ms                                                                 | 500 ms: 1.00x slower                                                    |
| bench_thread_pool      | 875 us                                                                 | 878 us: 1.00x slower                                                    |
| pidigits               | 186 ms                                                                 | 187 ms: 1.00x slower                                                    |
| sqlglot_optimize       | 59.5 ms                                                                | 59.9 ms: 1.01x slower                                                   |
| unpack_sequence        | 105 ns                                                                 | 106 ns: 1.01x slower                                                    |
| pyflate                | 448 ms                                                                 | 452 ms: 1.01x slower                                                    |
| bpe_tokeniser          | 4.41 sec                                                               | 4.45 sec: 1.01x slower                                                  |
| tornado_http           | 94.5 ms                                                                | 95.4 ms: 1.01x slower                                                   |
| pathlib                | 15.9 ms                                                                | 16.1 ms: 1.01x slower                                                   |
| sqlglot_normalize      | 114 ms                                                                 | 115 ms: 1.01x slower                                                    |
| nbody                  | 80.1 ms                                                                | 80.9 ms: 1.01x slower                                                   |
| sympy_sum              | 175 ms                                                                 | 177 ms: 1.01x slower                                                    |
| logging_silent         | 98.9 ns                                                                | 100 ns: 1.01x slower                                                    |
| dulwich_log            | 66.2 ms                                                                | 67.0 ms: 1.01x slower                                                   |
| sqlite_synth           | 2.80 us                                                                | 2.84 us: 1.01x slower                                                   |
| async_generators       | 453 ms                                                                 | 461 ms: 1.02x slower                                                    |
| telco                  | 7.65 ms                                                                | 7.79 ms: 1.02x slower                                                   |
| genshi_xml             | 58.6 ms                                                                | 59.7 ms: 1.02x slower                                                   |
| django_template        | 35.9 ms                                                                | 36.9 ms: 1.03x slower                                                   |
| pickle                 | 11.5 us                                                                | 11.8 us: 1.03x slower                                                   |
| pickle_list            | 5.02 us                                                                | 5.16 us: 1.03x slower                                                   |
| fannkuch               | 383 ms                                                                 | 395 ms: 1.03x slower                                                    |
| spectral_norm          | 114 ms                                                                 | 117 ms: 1.03x slower                                                    |
| pprint_pformat         | 1.46 sec                                                               | 1.51 sec: 1.04x slower                                                  |
| pickle_dict            | 33.6 us                                                                | 35.8 us: 1.06x slower                                                   |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                            |

Benchmark hidden because not significant (41): json, async_tree_none, meteor_contest, async_tree_none_tg, mako, async_tree_memoization, deepcopy_memo, sympy_str, async_tree_io, coverage, go, nqueens, sympy_expand, scimark_lu, async_tree_io_tg, unpickle_pure_python, richards, typing_runtime_protocols, json_dumps, scimark_monte_carlo, scimark_fft, json_loads, sphinx, async_tree_memoization_tg, async_tree_cpu_io_mixed, sqlglot_transpile, deepcopy, sympy_integrate, pylint, 2to3, bench_mp_pool, sqlglot_parse, scimark_sparse_mat_mult, raytrace, asyncio_websockets, tomli_loads, unpickle, async_tree_cpu_io_mixed_tg, genshi_text, xml_etree_parse, pprint_safe_repr

# HPT report

- Reliability score: 50.44% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x