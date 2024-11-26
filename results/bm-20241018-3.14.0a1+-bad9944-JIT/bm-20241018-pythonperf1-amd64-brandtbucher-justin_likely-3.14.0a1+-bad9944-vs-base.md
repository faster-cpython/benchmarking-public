# Results vs. base

- fork: brandtbucher
- ref: justin_likely
- machine: windows-amd64
- commit hash: bad9944
- commit date: 2024-10-18
- overall geometric mean: 1.006x slower
- HPT reliability: 99.03%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241017-pythonperf1-amd64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 1.92 sec                                                                    | 1.93 sec: 1.00x slower                                                     |
| tornado_http   | 98.2 ms                                                                     | 99.5 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                               |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241017-pythonperf1-amd64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| coroutines       | 14.5 ms                                                                     | 14.1 ms: 1.03x faster                                                      |
| async_generators | 269 ms                                                                      | 268 ms: 1.01x faster                                                       |
| asyncio_tcp_ssl  | 1.52 sec                                                                    | 1.54 sec: 1.01x slower                                                     |
| Geometric mean   | (ref)                                                                       | 1.00x faster                                                               |

Benchmark hidden because not significant (9): asyncio_tcp, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_io, async_tree_none_tg, async_tree_memoization, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241017-pythonperf1-amd64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 47.6 ms                                                                     | 46.5 ms: 1.02x faster                                                      |
| nbody          | 55.8 ms                                                                     | 55.0 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241017-pythonperf1-amd64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 93.7 ms                                                                     | 92.9 ms: 1.01x faster                                                      |
| regex_v8       | 14.5 ms                                                                     | 14.8 ms: 1.02x slower                                                      |
| regex_dna      | 115 ms                                                                      | 117 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241017-pythonperf1-amd64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 146 us                                                                      | 143 us: 1.02x faster                                                       |
| unpickle             | 9.13 us                                                                     | 8.99 us: 1.02x faster                                                      |
| unpickle_list        | 2.91 us                                                                     | 2.87 us: 1.01x faster                                                      |
| pickle_pure_python   | 200 us                                                                      | 198 us: 1.01x faster                                                       |
| tomli_loads          | 1.28 sec                                                                    | 1.29 sec: 1.01x slower                                                     |
| pickle               | 7.47 us                                                                     | 7.52 us: 1.01x slower                                                      |
| pickle_dict          | 17.9 us                                                                     | 18.0 us: 1.01x slower                                                      |
| xml_etree_iterparse  | 62.6 ms                                                                     | 63.5 ms: 1.01x slower                                                      |
| pickle_list          | 2.78 us                                                                     | 2.82 us: 1.01x slower                                                      |
| json_loads           | 14.1 us                                                                     | 14.4 us: 1.02x slower                                                      |
| xml_etree_generate   | 50.3 ms                                                                     | 51.5 ms: 1.02x slower                                                      |
| xml_etree_process    | 35.6 ms                                                                     | 36.5 ms: 1.03x slower                                                      |
| Geometric mean       | (ref)                                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (2): json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241017-pythonperf1-amd64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|-----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 46.5 ms                                                                     | 46.0 ms: 1.01x faster                                                      |
| mako            | 5.06 ms                                                                     | 5.13 ms: 1.01x slower                                                      |
| django_template | 27.2 ms                                                                     | 27.7 ms: 1.02x slower                                                      |
| Geometric mean  | (ref)                                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20241017-pythonperf1-amd64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|--------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| logging_silent           | 60.0 ns                                                                     | 56.1 ns: 1.07x faster                                                      |
| scimark_sor              | 67.4 ms                                                                     | 65.1 ms: 1.04x faster                                                      |
| coroutines               | 14.5 ms                                                                     | 14.1 ms: 1.03x faster                                                      |
| float                    | 47.6 ms                                                                     | 46.5 ms: 1.02x faster                                                      |
| deepcopy_reduce          | 1.92 us                                                                     | 1.88 us: 1.02x faster                                                      |
| unpickle_pure_python     | 146 us                                                                      | 143 us: 1.02x faster                                                       |
| spectral_norm            | 54.8 ms                                                                     | 53.9 ms: 1.02x faster                                                      |
| nbody                    | 55.8 ms                                                                     | 55.0 ms: 1.02x faster                                                      |
| unpickle                 | 9.13 us                                                                     | 8.99 us: 1.02x faster                                                      |
| go                       | 93.4 ms                                                                     | 92.0 ms: 1.01x faster                                                      |
| unpickle_list            | 2.91 us                                                                     | 2.87 us: 1.01x faster                                                      |
| create_gc_cycles         | 1.43 ms                                                                     | 1.41 ms: 1.01x faster                                                      |
| mdp                      | 1.55 sec                                                                    | 1.53 sec: 1.01x faster                                                     |
| deepcopy                 | 196 us                                                                      | 194 us: 1.01x faster                                                       |
| genshi_xml               | 46.5 ms                                                                     | 46.0 ms: 1.01x faster                                                      |
| regex_compile            | 93.7 ms                                                                     | 92.9 ms: 1.01x faster                                                      |
| pathlib                  | 81.4 ms                                                                     | 80.7 ms: 1.01x faster                                                      |
| raytrace                 | 215 ms                                                                      | 213 ms: 1.01x faster                                                       |
| pickle_pure_python       | 200 us                                                                      | 198 us: 1.01x faster                                                       |
| async_generators         | 269 ms                                                                      | 268 ms: 1.01x faster                                                       |
| crypto_pyaes             | 41.0 ms                                                                     | 40.8 ms: 1.00x faster                                                      |
| docutils                 | 1.92 sec                                                                    | 1.93 sec: 1.00x slower                                                     |
| richards_super           | 38.4 ms                                                                     | 38.6 ms: 1.01x slower                                                      |
| tomli_loads              | 1.28 sec                                                                    | 1.29 sec: 1.01x slower                                                     |
| fannkuch                 | 239 ms                                                                      | 240 ms: 1.01x slower                                                       |
| pickle                   | 7.47 us                                                                     | 7.52 us: 1.01x slower                                                      |
| sqlglot_transpile        | 1.20 ms                                                                     | 1.21 ms: 1.01x slower                                                      |
| hexiom                   | 5.21 ms                                                                     | 5.25 ms: 1.01x slower                                                      |
| richards                 | 34.0 ms                                                                     | 34.3 ms: 1.01x slower                                                      |
| pickle_dict              | 17.9 us                                                                     | 18.0 us: 1.01x slower                                                      |
| logging_format           | 6.62 us                                                                     | 6.67 us: 1.01x slower                                                      |
| meteor_contest           | 75.4 ms                                                                     | 76.0 ms: 1.01x slower                                                      |
| sqlglot_parse            | 900 us                                                                      | 908 us: 1.01x slower                                                       |
| deltablue                | 2.33 ms                                                                     | 2.35 ms: 1.01x slower                                                      |
| pyflate                  | 293 ms                                                                      | 296 ms: 1.01x slower                                                       |
| unpack_sequence          | 58.8 ns                                                                     | 59.5 ns: 1.01x slower                                                      |
| nqueens                  | 62.9 ms                                                                     | 63.7 ms: 1.01x slower                                                      |
| asyncio_tcp_ssl          | 1.52 sec                                                                    | 1.54 sec: 1.01x slower                                                     |
| tornado_http             | 98.2 ms                                                                     | 99.5 ms: 1.01x slower                                                      |
| mako                     | 5.06 ms                                                                     | 5.13 ms: 1.01x slower                                                      |
| xml_etree_iterparse      | 62.6 ms                                                                     | 63.5 ms: 1.01x slower                                                      |
| pickle_list              | 2.78 us                                                                     | 2.82 us: 1.01x slower                                                      |
| sympy_expand             | 327 ms                                                                      | 332 ms: 1.01x slower                                                       |
| sqlglot_optimize         | 42.7 ms                                                                     | 43.4 ms: 1.02x slower                                                      |
| scimark_fft              | 155 ms                                                                      | 157 ms: 1.02x slower                                                       |
| sympy_sum                | 103 ms                                                                      | 104 ms: 1.02x slower                                                       |
| thrift                   | 518 us                                                                      | 527 us: 1.02x slower                                                       |
| sqlglot_normalize        | 208 ms                                                                      | 212 ms: 1.02x slower                                                       |
| django_template          | 27.2 ms                                                                     | 27.7 ms: 1.02x slower                                                      |
| regex_v8                 | 14.5 ms                                                                     | 14.8 ms: 1.02x slower                                                      |
| regex_dna                | 115 ms                                                                      | 117 ms: 1.02x slower                                                       |
| bench_thread_pool        | 828 us                                                                      | 845 us: 1.02x slower                                                       |
| json_loads               | 14.1 us                                                                     | 14.4 us: 1.02x slower                                                      |
| xml_etree_generate       | 50.3 ms                                                                     | 51.5 ms: 1.02x slower                                                      |
| telco                    | 4.46 ms                                                                     | 4.56 ms: 1.02x slower                                                      |
| comprehensions           | 11.6 us                                                                     | 11.9 us: 1.02x slower                                                      |
| xml_etree_process        | 35.6 ms                                                                     | 36.5 ms: 1.03x slower                                                      |
| scimark_sparse_mat_mult  | 2.17 ms                                                                     | 2.23 ms: 1.03x slower                                                      |
| coverage                 | 47.7 ms                                                                     | 49.2 ms: 1.03x slower                                                      |
| deepcopy_memo            | 16.3 us                                                                     | 16.8 us: 1.03x slower                                                      |
| typing_runtime_protocols | 114 us                                                                      | 118 us: 1.04x slower                                                       |
| generators               | 23.1 ms                                                                     | 23.9 ms: 1.04x slower                                                      |
| pprint_pformat           | 916 ms                                                                      | 972 ms: 1.06x slower                                                       |
| pprint_safe_repr         | 444 ms                                                                      | 480 ms: 1.08x slower                                                       |
| Geometric mean           | (ref)                                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (32): html5lib, asyncio_tcp, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, pycparser, json, gc_traversal, json_dumps, pidigits, genshi_text, chaos, async_tree_io_tg, python_startup, sphinx, bench_mp_pool, scimark_lu, sqlite_synth, async_tree_io, scimark_monte_carlo, xml_etree_parse, dulwich_log, logging_simple, sympy_integrate, async_tree_none_tg, 2to3, async_tree_memoization, pylint, python_startup_no_site, regex_effbot, async_tree_none, sympy_str

- Geometric mean (including insignificant results): 1.006x slower
# HPT report

- Reliability score: 99.03% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown