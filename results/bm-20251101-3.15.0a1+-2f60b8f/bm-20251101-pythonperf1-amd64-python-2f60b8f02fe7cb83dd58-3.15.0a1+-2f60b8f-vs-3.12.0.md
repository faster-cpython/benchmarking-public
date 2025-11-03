# Results vs. 3.12.0

- fork: python
- ref: 2f60b8f02fe7cb83dd58
- machine: windows-amd64
- commit hash: 2f60b8f
- commit date: 2025-11-01
- overall geometric mean: 1.102x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 220 ms: 1.01x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.62 sec: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 374 ms: 2.06x faster                                                        |
| async_tree_io              | 731 ms                                                      | 371 ms: 1.97x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 191 ms: 1.92x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 159 ms: 1.80x faster                                                        |
| async_tree_none            | 291 ms                                                      | 169 ms: 1.73x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 198 ms: 1.72x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 321 ms: 1.52x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 338 ms: 1.49x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.77x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 44.3 ms: 1.28x faster                                                       |
| nbody          | 71.9 ms                                                     | 65.2 ms: 1.10x faster                                                       |
| pidigits       | 152 ms                                                      | 144 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 81.7 ms: 1.07x faster                                                       |
| regex_dna      | 126 ms                                                      | 121 ms: 1.05x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 59.4 ms: 1.10x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 88.5 ms: 1.05x faster                                                       |
| json_dumps           | 5.70 ms                                                     | 5.54 ms: 1.03x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 55.4 ms: 1.01x faster                                                       |
| unpickle_pure_python | 133 us                                                      | 134 us: 1.01x slower                                                        |
| unpickle             | 8.18 us                                                     | 8.29 us: 1.01x slower                                                       |
| unpickle_list        | 2.75 us                                                     | 2.80 us: 1.02x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.40 sec: 1.02x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.2 us: 1.02x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 38.9 ms: 1.03x slower                                                       |
| pickle_dict          | 18.4 us                                                     | 19.5 us: 1.06x slower                                                       |
| pickle               | 7.43 us                                                     | 8.07 us: 1.09x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 215 us: 1.10x slower                                                        |
| pickle_list          | 2.83 us                                                     | 3.20 us: 1.13x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.4 ms: 1.19x slower                                                       |
| python_startup         | 19.5 ms                                                     | 25.8 ms: 1.32x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.73 ms: 1.05x faster                                                       |
| django_template | 22.9 ms                                                     | 23.9 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.01x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 28.8 ms: 2.79x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 374 ms: 2.06x faster                                                        |
| async_tree_io              | 731 ms                                                      | 371 ms: 1.97x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 191 ms: 1.92x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 159 ms: 1.80x faster                                                        |
| async_tree_none            | 291 ms                                                      | 169 ms: 1.73x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 198 ms: 1.72x faster                                                        |
| mdp                        | 1.37 sec                                                    | 826 ms: 1.66x faster                                                        |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.29 sec: 1.62x faster                                                      |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 321 ms: 1.52x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 338 ms: 1.49x faster                                                        |
| deepcopy                   | 238 us                                                      | 165 us: 1.45x faster                                                        |
| deepcopy_memo              | 23.7 us                                                     | 17.2 us: 1.38x faster                                                       |
| asyncio_tcp                | 487 ms                                                      | 379 ms: 1.28x faster                                                        |
| float                      | 56.8 ms                                                     | 44.3 ms: 1.28x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.2 us: 1.26x faster                                                       |
| go                         | 91.6 ms                                                     | 77.3 ms: 1.18x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.77 us: 1.18x faster                                                       |
| generators                 | 22.5 ms                                                     | 19.8 ms: 1.14x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.59 us: 1.11x faster                                                       |
| scimark_fft                | 184 ms                                                      | 167 ms: 1.10x faster                                                        |
| nbody                      | 71.9 ms                                                     | 65.2 ms: 1.10x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 59.4 ms: 1.10x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 56.0 ns: 1.08x faster                                                       |
| raytrace                   | 192 ms                                                      | 179 ms: 1.07x faster                                                        |
| dulwich_log                | 44.3 ms                                                     | 41.3 ms: 1.07x faster                                                       |
| chaos                      | 43.3 ms                                                     | 40.4 ms: 1.07x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 81.7 ms: 1.07x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.40 ms: 1.07x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 41.0 ms: 1.07x faster                                                       |
| pidigits                   | 152 ms                                                      | 144 ms: 1.06x faster                                                        |
| mako                       | 7.09 ms                                                     | 6.73 ms: 1.05x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 488 ms: 1.05x faster                                                        |
| xml_etree_parse            | 93.0 ms                                                     | 88.5 ms: 1.05x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 997 ms: 1.05x faster                                                        |
| sympy_sum                  | 91.5 ms                                                     | 87.4 ms: 1.05x faster                                                       |
| json                       | 3.05 ms                                                     | 2.92 ms: 1.05x faster                                                       |
| regex_dna                  | 126 ms                                                      | 121 ms: 1.05x faster                                                        |
| logging_simple             | 6.28 us                                                     | 6.05 us: 1.04x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 64.5 ms: 1.04x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 12.5 ms: 1.04x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 76.4 ms: 1.03x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                       |
| sympy_str                  | 175 ms                                                      | 170 ms: 1.03x faster                                                        |
| json_dumps                 | 5.70 ms                                                     | 5.54 ms: 1.03x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.54 us: 1.03x faster                                                       |
| async_generators           | 239 ms                                                      | 233 ms: 1.03x faster                                                        |
| pyflate                    | 295 ms                                                      | 288 ms: 1.02x faster                                                        |
| docutils                   | 1.66 sec                                                    | 1.62 sec: 1.02x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 73.1 ms: 1.02x faster                                                       |
| richards_super             | 32.1 ms                                                     | 31.6 ms: 1.02x faster                                                       |
| richards                   | 28.4 ms                                                     | 28.0 ms: 1.02x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 47.8 ms: 1.01x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 55.4 ms: 1.01x faster                                                       |
| 2to3                       | 218 ms                                                      | 220 ms: 1.01x slower                                                        |
| unpickle_pure_python       | 133 us                                                      | 134 us: 1.01x slower                                                        |
| unpack_sequence            | 37.5 ns                                                     | 37.9 ns: 1.01x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.29 us: 1.01x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 63.6 ms: 1.01x slower                                                       |
| coroutines                 | 14.3 ms                                                     | 14.5 ms: 1.01x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 59.9 ms: 1.02x slower                                                       |
| unpickle_list              | 2.75 us                                                     | 2.80 us: 1.02x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.18 ms: 1.02x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.40 sec: 1.02x slower                                                      |
| sympy_expand               | 284 ms                                                      | 290 ms: 1.02x slower                                                        |
| json_loads                 | 13.9 us                                                     | 14.2 us: 1.02x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.26 ms: 1.03x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 38.9 ms: 1.03x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.23 ms: 1.03x slower                                                       |
| django_template            | 22.9 ms                                                     | 23.9 ms: 1.04x slower                                                       |
| pickle_dict                | 18.4 us                                                     | 19.5 us: 1.06x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 102 us: 1.08x slower                                                        |
| pickle                     | 7.43 us                                                     | 8.07 us: 1.09x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 215 us: 1.10x slower                                                        |
| fannkuch                   | 247 ms                                                      | 274 ms: 1.11x slower                                                        |
| pickle_list                | 2.83 us                                                     | 3.20 us: 1.13x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 19.4 ms: 1.19x slower                                                       |
| coverage                   | 40.8 ms                                                     | 49.9 ms: 1.22x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 90.9 ms: 1.31x slower                                                       |
| python_startup             | 19.5 ms                                                     | 25.8 ms: 1.32x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.10 ms: 1.38x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.31 ms: 1.74x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.09x faster                                                                |

Benchmark hidden because not significant (3): pycparser, bench_thread_pool, regex_v8
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20251101-3.15.0a1+-2f60b8f/bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.102x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown