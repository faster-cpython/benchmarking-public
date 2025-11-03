# Results vs. 3.12.0

- fork: python
- ref: 2f60b8f02fe7cb83dd58
- machine: windows-amd64
- commit hash: 2f60b8f
- commit date: 2025-11-01
- overall geometric mean: 1.169x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 213 ms: 1.02x faster                                                        |
| docutils       | 1.66 sec                                                    | 1.62 sec: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 366 ms: 2.11x faster                                                        |
| async_tree_io              | 731 ms                                                      | 360 ms: 2.03x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 192 ms: 1.91x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 154 ms: 1.86x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 190 ms: 1.79x faster                                                        |
| async_tree_none            | 291 ms                                                      | 164 ms: 1.78x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 321 ms: 1.52x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 330 ms: 1.52x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.80x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 38.9 ms: 1.46x faster                                                       |
| nbody          | 71.9 ms                                                     | 53.1 ms: 1.35x faster                                                       |
| pidigits       | 152 ms                                                      | 147 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                       | 1.27x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 77.5 ms: 1.13x faster                                                       |
| regex_dna      | 126 ms                                                      | 117 ms: 1.08x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 14.0 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 103 us: 1.30x faster                                                        |
| tomli_loads          | 1.37 sec                                                    | 1.06 sec: 1.29x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 56.6 ms: 1.15x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 48.6 ms: 1.15x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 34.2 ms: 1.10x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 85.3 ms: 1.09x faster                                                       |
| json_dumps           | 5.70 ms                                                     | 5.38 ms: 1.06x faster                                                       |
| pickle_pure_python   | 195 us                                                      | 193 us: 1.02x faster                                                        |
| pickle               | 7.43 us                                                     | 7.35 us: 1.01x faster                                                       |
| unpickle             | 8.18 us                                                     | 8.28 us: 1.01x slower                                                       |
| pickle_dict          | 18.4 us                                                     | 19.3 us: 1.05x slower                                                       |
| pickle_list          | 2.83 us                                                     | 3.25 us: 1.15x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.06x faster                                                                |

Benchmark hidden because not significant (2): json_loads, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.0 ms: 1.17x slower                                                       |
| python_startup         | 19.5 ms                                                     | 25.4 ms: 1.31x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.24x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.12 ms: 1.38x faster                                                       |
| django_template | 22.9 ms                                                     | 23.7 ms: 1.03x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.16x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 29.0 ms: 2.78x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 366 ms: 2.11x faster                                                        |
| async_tree_io              | 731 ms                                                      | 360 ms: 2.03x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 192 ms: 1.91x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 154 ms: 1.86x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 190 ms: 1.79x faster                                                        |
| async_tree_none            | 291 ms                                                      | 164 ms: 1.78x faster                                                        |
| mdp                        | 1.37 sec                                                    | 779 ms: 1.76x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 321 ms: 1.52x faster                                                        |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.38 sec: 1.52x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 330 ms: 1.52x faster                                                        |
| deepcopy                   | 238 us                                                      | 160 us: 1.49x faster                                                        |
| float                      | 56.8 ms                                                     | 38.9 ms: 1.46x faster                                                       |
| scimark_fft                | 184 ms                                                      | 132 ms: 1.39x faster                                                        |
| deepcopy_memo              | 23.7 us                                                     | 17.0 us: 1.39x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.2 us: 1.38x faster                                                       |
| mako                       | 7.09 ms                                                     | 5.12 ms: 1.38x faster                                                       |
| nbody                      | 71.9 ms                                                     | 53.1 ms: 1.35x faster                                                       |
| unpickle_pure_python       | 133 us                                                      | 103 us: 1.30x faster                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.06 sec: 1.29x faster                                                      |
| pprint_safe_repr           | 513 ms                                                      | 413 ms: 1.24x faster                                                        |
| pprint_pformat             | 1.05 sec                                                    | 854 ms: 1.22x faster                                                        |
| go                         | 91.6 ms                                                     | 75.0 ms: 1.22x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.73 us: 1.21x faster                                                       |
| pyflate                    | 295 ms                                                      | 246 ms: 1.20x faster                                                        |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.15 ms: 1.19x faster                                                       |
| fannkuch                   | 247 ms                                                      | 210 ms: 1.17x faster                                                        |
| generators                 | 22.5 ms                                                     | 19.2 ms: 1.17x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 56.6 ms: 1.15x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 48.6 ms: 1.15x faster                                                       |
| unpack_sequence            | 37.5 ns                                                     | 32.6 ns: 1.15x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.53 us: 1.15x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 38.9 ms: 1.14x faster                                                       |
| chaos                      | 43.3 ms                                                     | 38.2 ms: 1.13x faster                                                       |
| raytrace                   | 192 ms                                                      | 170 ms: 1.13x faster                                                        |
| regex_compile              | 87.5 ms                                                     | 77.5 ms: 1.13x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 54.8 ns: 1.10x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 34.2 ms: 1.10x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 39.9 ms: 1.10x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 85.3 ms: 1.09x faster                                                       |
| pycparser                  | 699 ms                                                      | 646 ms: 1.08x faster                                                        |
| regex_dna                  | 126 ms                                                      | 117 ms: 1.08x faster                                                        |
| meteor_contest             | 74.6 ms                                                     | 69.3 ms: 1.08x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 85.1 ms: 1.08x faster                                                       |
| logging_simple             | 6.28 us                                                     | 5.86 us: 1.07x faster                                                       |
| telco                      | 4.13 ms                                                     | 3.88 ms: 1.06x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 45.7 ms: 1.06x faster                                                       |
| richards_super             | 32.1 ms                                                     | 30.3 ms: 1.06x faster                                                       |
| hexiom                     | 4.10 ms                                                     | 3.87 ms: 1.06x faster                                                       |
| json_dumps                 | 5.70 ms                                                     | 5.38 ms: 1.06x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 59.4 ms: 1.06x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.36 us: 1.06x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 74.8 ms: 1.05x faster                                                       |
| richards                   | 28.4 ms                                                     | 27.0 ms: 1.05x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 64.0 ms: 1.05x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 12.4 ms: 1.04x faster                                                       |
| pidigits                   | 152 ms                                                      | 147 ms: 1.04x faster                                                        |
| bench_thread_pool          | 857 us                                                      | 826 us: 1.04x faster                                                        |
| sympy_str                  | 175 ms                                                      | 170 ms: 1.03x faster                                                        |
| scimark_lu                 | 58.9 ms                                                     | 57.4 ms: 1.03x faster                                                       |
| docutils                   | 1.66 sec                                                    | 1.62 sec: 1.02x faster                                                      |
| 2to3                       | 218 ms                                                      | 213 ms: 1.02x faster                                                        |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                       |
| regex_v8                   | 14.2 ms                                                     | 14.0 ms: 1.02x faster                                                       |
| json                       | 3.05 ms                                                     | 3.00 ms: 1.02x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 14.0 ms: 1.02x faster                                                       |
| pickle_pure_python         | 195 us                                                      | 193 us: 1.02x faster                                                        |
| pickle                     | 7.43 us                                                     | 7.35 us: 1.01x faster                                                       |
| unpickle                   | 8.18 us                                                     | 8.28 us: 1.01x slower                                                       |
| async_generators           | 239 ms                                                      | 243 ms: 1.01x slower                                                        |
| django_template            | 22.9 ms                                                     | 23.7 ms: 1.03x slower                                                       |
| pickle_dict                | 18.4 us                                                     | 19.3 us: 1.05x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 105 us: 1.11x slower                                                        |
| asyncio_tcp                | 487 ms                                                      | 541 ms: 1.11x slower                                                        |
| pickle_list                | 2.83 us                                                     | 3.25 us: 1.15x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 19.0 ms: 1.17x slower                                                       |
| coverage                   | 40.8 ms                                                     | 48.6 ms: 1.19x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 88.6 ms: 1.28x slower                                                       |
| python_startup             | 19.5 ms                                                     | 25.4 ms: 1.31x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.12 ms: 1.39x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.29 ms: 1.71x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.15x faster                                                                |

Benchmark hidden because not significant (4): json_loads, deltablue, unpickle_list, sympy_expand
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20251101-3.15.0a1+-2f60b8f-JIT/bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.169x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: unknown