# Results vs. 3.12.0

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: windows-amd64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.069x faster
- HPT reliability: 98.86%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 221 ms: 1.02x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.71 sec: 1.03x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 404 ms: 1.91x faster                                                        |
| async_tree_io              | 731 ms                                                      | 414 ms: 1.77x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 214 ms: 1.71x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 173 ms: 1.65x faster                                                        |
| async_tree_none            | 291 ms                                                      | 183 ms: 1.59x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 215 ms: 1.58x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 342 ms: 1.47x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 341 ms: 1.44x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.63x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 60.0 ms: 1.20x faster                                                       |
| float          | 56.8 ms                                                     | 48.0 ms: 1.18x faster                                                       |
| pidigits       | 152 ms                                                      | 154 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.41 ms: 1.14x faster                                                       |
| regex_dna      | 126 ms                                                      | 113 ms: 1.12x faster                                                        |
| regex_compile  | 87.5 ms                                                     | 83.4 ms: 1.05x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 14.1 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 116 us: 1.15x faster                                                        |
| tomli_loads          | 1.37 sec                                                    | 1.20 sec: 1.14x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 50.7 ms: 1.10x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 89.9 ms: 1.03x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 36.7 ms: 1.03x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.6 ms: 1.02x faster                                                       |
| unpickle_list        | 2.75 us                                                     | 2.89 us: 1.05x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.65 us: 1.06x slower                                                       |
| pickle               | 7.43 us                                                     | 7.91 us: 1.06x slower                                                       |
| json_loads           | 13.9 us                                                     | 14.8 us: 1.06x slower                                                       |
| pickle_dict          | 18.4 us                                                     | 19.6 us: 1.07x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 213 us: 1.09x slower                                                        |
| pickle_list          | 2.83 us                                                     | 3.17 us: 1.12x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.70 ms: 1.18x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.0 ms: 1.17x slower                                                       |
| python_startup         | 19.5 ms                                                     | 24.6 ms: 1.27x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.22x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.25 ms: 1.35x faster                                                       |
| django_template | 22.9 ms                                                     | 25.5 ms: 1.11x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.10x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 29.7 ms: 2.71x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 404 ms: 1.91x faster                                                        |
| async_tree_io              | 731 ms                                                      | 414 ms: 1.77x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 214 ms: 1.71x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 173 ms: 1.65x faster                                                        |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.29 sec: 1.62x faster                                                      |
| async_tree_none            | 291 ms                                                      | 183 ms: 1.59x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 215 ms: 1.58x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 342 ms: 1.47x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 341 ms: 1.44x faster                                                        |
| mako                       | 7.09 ms                                                     | 5.25 ms: 1.35x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.0 us: 1.29x faster                                                       |
| deepcopy                   | 238 us                                                      | 185 us: 1.29x faster                                                        |
| asyncio_tcp                | 487 ms                                                      | 393 ms: 1.24x faster                                                        |
| scimark_fft                | 184 ms                                                      | 152 ms: 1.21x faster                                                        |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.11 ms: 1.21x faster                                                       |
| nbody                      | 71.9 ms                                                     | 60.0 ms: 1.20x faster                                                       |
| float                      | 56.8 ms                                                     | 48.0 ms: 1.18x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.53 us: 1.15x faster                                                       |
| unpickle_pure_python       | 133 us                                                      | 116 us: 1.15x faster                                                        |
| regex_effbot               | 1.62 ms                                                     | 1.41 ms: 1.14x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 20.7 us: 1.14x faster                                                       |
| generators                 | 22.5 ms                                                     | 19.8 ms: 1.14x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.20 sec: 1.14x faster                                                      |
| regex_dna                  | 126 ms                                                      | 113 ms: 1.12x faster                                                        |
| xml_etree_generate         | 55.8 ms                                                     | 50.7 ms: 1.10x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.93 us: 1.09x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.3 ms: 1.07x faster                                                       |
| pyflate                    | 295 ms                                                      | 278 ms: 1.06x faster                                                        |
| dulwich_log                | 44.3 ms                                                     | 42.1 ms: 1.05x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 83.4 ms: 1.05x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 999 ms: 1.05x faster                                                        |
| pprint_safe_repr           | 513 ms                                                      | 493 ms: 1.04x faster                                                        |
| fannkuch                   | 247 ms                                                      | 238 ms: 1.04x faster                                                        |
| xml_etree_parse            | 93.0 ms                                                     | 89.9 ms: 1.03x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 61.1 ms: 1.03x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 36.7 ms: 1.03x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 65.3 ms: 1.02x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.6 ms: 1.02x faster                                                       |
| async_generators           | 239 ms                                                      | 234 ms: 1.02x faster                                                        |
| go                         | 91.6 ms                                                     | 89.5 ms: 1.02x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 47.4 ms: 1.02x faster                                                       |
| chaos                      | 43.3 ms                                                     | 42.4 ms: 1.02x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 89.7 ms: 1.02x faster                                                       |
| json                       | 3.05 ms                                                     | 3.00 ms: 1.01x faster                                                       |
| regex_v8                   | 14.2 ms                                                     | 14.1 ms: 1.01x faster                                                       |
| sympy_str                  | 175 ms                                                      | 177 ms: 1.01x slower                                                        |
| pidigits                   | 152 ms                                                      | 154 ms: 1.01x slower                                                        |
| 2to3                       | 218 ms                                                      | 221 ms: 1.02x slower                                                        |
| logging_simple             | 6.28 us                                                     | 6.41 us: 1.02x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.71 sec: 1.03x slower                                                      |
| logging_format             | 6.72 us                                                     | 6.92 us: 1.03x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.4 ms: 1.03x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 831 us: 1.03x slower                                                        |
| sqlglot_transpile          | 1.02 ms                                                     | 1.06 ms: 1.03x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.25 ms: 1.04x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 195 ms: 1.05x slower                                                        |
| unpickle_list              | 2.75 us                                                     | 2.89 us: 1.05x slower                                                       |
| pycparser                  | 699 ms                                                      | 735 ms: 1.05x slower                                                        |
| sqlglot_optimize           | 34.5 ms                                                     | 36.3 ms: 1.05x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.65 us: 1.06x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.39 ms: 1.06x slower                                                       |
| richards_super             | 32.1 ms                                                     | 34.1 ms: 1.06x slower                                                       |
| pickle                     | 7.43 us                                                     | 7.91 us: 1.06x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.8 us: 1.06x slower                                                       |
| pickle_dict                | 18.4 us                                                     | 19.6 us: 1.07x slower                                                       |
| logging_silent             | 60.5 ns                                                     | 64.7 ns: 1.07x slower                                                       |
| richards                   | 28.4 ms                                                     | 30.5 ms: 1.07x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 47.1 ms: 1.08x slower                                                       |
| sympy_expand               | 284 ms                                                      | 306 ms: 1.08x slower                                                        |
| pickle_pure_python         | 195 us                                                      | 213 us: 1.09x slower                                                        |
| hexiom                     | 4.10 ms                                                     | 4.48 ms: 1.09x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 65.1 ms: 1.11x slower                                                       |
| django_template            | 22.9 ms                                                     | 25.5 ms: 1.11x slower                                                       |
| pickle_list                | 2.83 us                                                     | 3.17 us: 1.12x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.56 sec: 1.14x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 90.1 ms: 1.14x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 109 us: 1.14x slower                                                        |
| coverage                   | 40.8 ms                                                     | 47.6 ms: 1.17x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 19.0 ms: 1.17x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.70 ms: 1.18x slower                                                       |
| unpack_sequence            | 37.5 ns                                                     | 45.8 ns: 1.22x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 85.2 ms: 1.23x slower                                                       |
| python_startup             | 19.5 ms                                                     | 24.6 ms: 1.27x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.96 ms: 1.29x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.21 ms: 1.61x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.06x faster                                                                |

Benchmark hidden because not significant (3): bench_thread_pool, raytrace, meteor_contest
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (13) of results/bm-20250222-3.14.0a5+-5ec4bf8-JIT/bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.069x faster

# HPT report

- Reliability score: 98.86% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown