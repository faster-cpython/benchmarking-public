# Results vs. base

- fork: brandtbucher
- ref: justin_unlikely
- machine: linux-x86_64
- commit hash: 15229e0
- commit date: 2024-10-17
- overall geometric mean: 1.00x faster
- HPT reliability: 76.46%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 278 ms                                                                 | 278 ms: 1.00x faster                                                    |
| docutils       | 2.91 sec                                                               | 2.92 sec: 1.00x slower                                                  |
| html5lib       | 64.6 ms                                                                | 63.4 ms: 1.02x faster                                                   |
| tornado_http   | 95.0 ms                                                                | 95.4 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                            |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| asyncio_tcp_ssl  | 1.80 sec                                                               | 1.80 sec: 1.00x slower                                                  |
| async_tree_io_tg | 967 ms                                                                 | 974 ms: 1.01x slower                                                    |
| asyncio_tcp      | 494 ms                                                                 | 500 ms: 1.01x slower                                                    |
| async_generators | 455 ms                                                                 | 461 ms: 1.01x slower                                                    |
| Geometric mean   | (ref)                                                                  | 1.00x slower                                                            |

Benchmark hidden because not significant (9): async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, coroutines, async_tree_memoization_tg, async_tree_memoization, asyncio_websockets, async_tree_none_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 83.0 ms                                                                | 80.9 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                            |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 24.2 ms                                                                | 24.5 ms: 1.01x slower                                                   |
| regex_dna      | 210 ms                                                                 | 216 ms: 1.03x slower                                                    |
| regex_effbot   | 3.64 ms                                                                | 3.78 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                            |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 314 us                                                                 | 309 us: 1.02x faster                                                    |
| xml_etree_parse      | 148 ms                                                                 | 146 ms: 1.02x faster                                                    |
| json_dumps           | 11.0 ms                                                                | 10.9 ms: 1.01x faster                                                   |
| xml_etree_iterparse  | 99.7 ms                                                                | 99.1 ms: 1.01x faster                                                   |
| unpickle_pure_python | 217 us                                                                 | 215 us: 1.01x faster                                                    |
| pickle               | 11.9 us                                                                | 11.8 us: 1.00x faster                                                   |
| pickle_dict          | 35.5 us                                                                | 35.8 us: 1.01x slower                                                   |
| pickle_list          | 5.12 us                                                                | 5.16 us: 1.01x slower                                                   |
| tomli_loads          | 1.89 sec                                                               | 1.91 sec: 1.01x slower                                                  |
| unpickle             | 14.2 us                                                                | 14.9 us: 1.06x slower                                                   |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                            |

Benchmark hidden because not significant (4): json_loads, xml_etree_process, unpickle_list, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 7.09 ms                                                                | 7.09 ms: 1.00x slower                                                   |
| python_startup         | 11.9 ms                                                                | 11.9 ms: 1.00x slower                                                   |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 10.2 ms                                                                | 9.93 ms: 1.03x faster                                                   |
| genshi_xml      | 60.8 ms                                                                | 59.7 ms: 1.02x faster                                                   |
| genshi_text     | 25.9 ms                                                                | 25.5 ms: 1.02x faster                                                   |
| django_template | 36.2 ms                                                                | 36.9 ms: 1.02x slower                                                   |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                            |

All benchmarks:
===============

| Benchmark               | bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal            | 4.84 ms                                                                | 4.45 ms: 1.09x faster                                                   |
| unpack_sequence         | 111 ns                                                                 | 106 ns: 1.05x faster                                                    |
| deepcopy_reduce         | 2.80 us                                                                | 2.71 us: 1.03x faster                                                   |
| mako                    | 10.2 ms                                                                | 9.93 ms: 1.03x faster                                                   |
| nbody                   | 83.0 ms                                                                | 80.9 ms: 1.03x faster                                                   |
| chaos                   | 59.1 ms                                                                | 57.9 ms: 1.02x faster                                                   |
| html5lib                | 64.6 ms                                                                | 63.4 ms: 1.02x faster                                                   |
| genshi_xml              | 60.8 ms                                                                | 59.7 ms: 1.02x faster                                                   |
| thrift                  | 798 us                                                                 | 783 us: 1.02x faster                                                    |
| pickle_pure_python      | 314 us                                                                 | 309 us: 1.02x faster                                                    |
| genshi_text             | 25.9 ms                                                                | 25.5 ms: 1.02x faster                                                   |
| scimark_sor             | 120 ms                                                                 | 118 ms: 1.02x faster                                                    |
| go                      | 135 ms                                                                 | 132 ms: 1.02x faster                                                    |
| xml_etree_parse         | 148 ms                                                                 | 146 ms: 1.02x faster                                                    |
| crypto_pyaes            | 67.4 ms                                                                | 66.4 ms: 1.02x faster                                                   |
| richards_super          | 47.7 ms                                                                | 47.0 ms: 1.02x faster                                                   |
| raytrace                | 280 ms                                                                 | 276 ms: 1.01x faster                                                    |
| deltablue               | 3.29 ms                                                                | 3.26 ms: 1.01x faster                                                   |
| logging_format          | 6.19 us                                                                | 6.12 us: 1.01x faster                                                   |
| deepcopy_memo           | 29.6 us                                                                | 29.3 us: 1.01x faster                                                   |
| hexiom                  | 7.05 ms                                                                | 6.98 ms: 1.01x faster                                                   |
| logging_simple          | 5.65 us                                                                | 5.59 us: 1.01x faster                                                   |
| pyflate                 | 455 ms                                                                 | 452 ms: 1.01x faster                                                    |
| create_gc_cycles        | 2.68 ms                                                                | 2.67 ms: 1.01x faster                                                   |
| json_dumps              | 11.0 ms                                                                | 10.9 ms: 1.01x faster                                                   |
| xml_etree_iterparse     | 99.7 ms                                                                | 99.1 ms: 1.01x faster                                                   |
| generators              | 35.4 ms                                                                | 35.3 ms: 1.01x faster                                                   |
| unpickle_pure_python    | 217 us                                                                 | 215 us: 1.01x faster                                                    |
| sqlglot_optimize        | 60.2 ms                                                                | 59.9 ms: 1.00x faster                                                   |
| comprehensions          | 16.9 us                                                                | 16.9 us: 1.00x faster                                                   |
| bench_thread_pool       | 881 us                                                                 | 878 us: 1.00x faster                                                    |
| pickle                  | 11.9 us                                                                | 11.8 us: 1.00x faster                                                   |
| scimark_fft             | 318 ms                                                                 | 317 ms: 1.00x faster                                                    |
| 2to3                    | 278 ms                                                                 | 278 ms: 1.00x faster                                                    |
| python_startup_no_site  | 7.09 ms                                                                | 7.09 ms: 1.00x slower                                                   |
| python_startup          | 11.9 ms                                                                | 11.9 ms: 1.00x slower                                                   |
| asyncio_tcp_ssl         | 1.80 sec                                                               | 1.80 sec: 1.00x slower                                                  |
| bpe_tokeniser           | 4.44 sec                                                               | 4.45 sec: 1.00x slower                                                  |
| tornado_http            | 95.0 ms                                                                | 95.4 ms: 1.00x slower                                                   |
| docutils                | 2.91 sec                                                               | 2.92 sec: 1.00x slower                                                  |
| meteor_contest          | 108 ms                                                                 | 109 ms: 1.00x slower                                                    |
| sympy_integrate         | 23.4 ms                                                                | 23.5 ms: 1.00x slower                                                   |
| scimark_sparse_mat_mult | 4.59 ms                                                                | 4.62 ms: 1.01x slower                                                   |
| async_tree_io_tg        | 967 ms                                                                 | 974 ms: 1.01x slower                                                    |
| logging_silent          | 99.3 ns                                                                | 100 ns: 1.01x slower                                                    |
| pickle_dict             | 35.5 us                                                                | 35.8 us: 1.01x slower                                                   |
| sympy_sum               | 175 ms                                                                 | 177 ms: 1.01x slower                                                    |
| pickle_list             | 5.12 us                                                                | 5.16 us: 1.01x slower                                                   |
| regex_v8                | 24.2 ms                                                                | 24.5 ms: 1.01x slower                                                   |
| tomli_loads             | 1.89 sec                                                               | 1.91 sec: 1.01x slower                                                  |
| asyncio_tcp             | 494 ms                                                                 | 500 ms: 1.01x slower                                                    |
| async_generators        | 455 ms                                                                 | 461 ms: 1.01x slower                                                    |
| pathlib                 | 15.9 ms                                                                | 16.1 ms: 1.01x slower                                                   |
| telco                   | 7.66 ms                                                                | 7.79 ms: 1.02x slower                                                   |
| django_template         | 36.2 ms                                                                | 36.9 ms: 1.02x slower                                                   |
| nqueens                 | 86.7 ms                                                                | 88.4 ms: 1.02x slower                                                   |
| pprint_pformat          | 1.48 sec                                                               | 1.51 sec: 1.02x slower                                                  |
| pycparser               | 1.15 sec                                                               | 1.18 sec: 1.02x slower                                                  |
| regex_dna               | 210 ms                                                                 | 216 ms: 1.03x slower                                                    |
| spectral_norm           | 113 ms                                                                 | 117 ms: 1.04x slower                                                    |
| regex_effbot            | 3.64 ms                                                                | 3.78 ms: 1.04x slower                                                   |
| unpickle                | 14.2 us                                                                | 14.9 us: 1.06x slower                                                   |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                            |

Benchmark hidden because not significant (36): pprint_safe_repr, async_tree_none, deepcopy, sqlglot_transpile, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, float, mdp, json_loads, richards, sqlglot_parse, bench_mp_pool, coroutines, pylint, regex_compile, sympy_expand, sympy_str, pidigits, async_tree_memoization_tg, json, scimark_monte_carlo, sphinx, sqlglot_normalize, dulwich_log, xml_etree_process, async_tree_memoization, unpickle_list, asyncio_websockets, scimark_lu, async_tree_none_tg, typing_runtime_protocols, coverage, xml_etree_generate, fannkuch, sqlite_synth, async_tree_io

# HPT report

- Reliability score: 76.46% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x