# Results vs. 3.12.0

- fork: python
- ref: 61b35f74aa4a6ac60663
- machine: windows-amd64
- commit hash: 61b35f7
- commit date: 2025-01-18
- overall geometric mean: 1.056x faster
- HPT reliability: 95.18%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 229 ms: 1.05x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.75 sec: 1.06x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 403 ms: 1.92x faster                                                        |
| async_tree_io              | 731 ms                                                      | 410 ms: 1.78x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 215 ms: 1.71x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 175 ms: 1.63x faster                                                        |
| async_tree_none            | 291 ms                                                      | 190 ms: 1.53x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 227 ms: 1.49x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 346 ms: 1.45x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 349 ms: 1.40x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.61x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 39.2 ms: 1.45x faster                                                       |
| nbody          | 71.9 ms                                                     | 57.9 ms: 1.24x faster                                                       |
| pidigits       | 152 ms                                                      | 146 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                       | 1.23x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.41 ms: 1.15x faster                                                       |
| regex_dna      | 126 ms                                                      | 112 ms: 1.13x faster                                                        |
| regex_compile  | 87.5 ms                                                     | 81.3 ms: 1.08x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 16.7 ms: 1.17x slower                                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 114 us: 1.17x faster                                                        |
| tomli_loads          | 1.37 sec                                                    | 1.20 sec: 1.14x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 50.6 ms: 1.10x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 59.8 ms: 1.09x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 88.4 ms: 1.05x faster                                                       |
| unpickle_list        | 2.75 us                                                     | 2.69 us: 1.02x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 37.0 ms: 1.02x faster                                                       |
| pickle_dict          | 18.4 us                                                     | 18.2 us: 1.01x faster                                                       |
| json_loads           | 13.9 us                                                     | 14.7 us: 1.05x slower                                                       |
| pickle               | 7.43 us                                                     | 7.84 us: 1.06x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.83 us: 1.08x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 216 us: 1.10x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 6.48 ms: 1.14x slower                                                       |
| pickle_list          | 2.83 us                                                     | 3.24 us: 1.15x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.00x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.9 ms: 1.10x slower                                                       |
| python_startup         | 19.5 ms                                                     | 24.1 ms: 1.24x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.17x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.10 ms: 1.39x faster                                                       |
| django_template | 22.9 ms                                                     | 27.6 ms: 1.20x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.07x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 403 ms: 1.92x faster                                                        |
| async_tree_io              | 731 ms                                                      | 410 ms: 1.78x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 215 ms: 1.71x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 175 ms: 1.63x faster                                                        |
| async_tree_none            | 291 ms                                                      | 190 ms: 1.53x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 227 ms: 1.49x faster                                                        |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.42 sec: 1.47x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 346 ms: 1.45x faster                                                        |
| float                      | 56.8 ms                                                     | 39.2 ms: 1.45x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 47.0 ms: 1.42x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 349 ms: 1.40x faster                                                        |
| mako                       | 7.09 ms                                                     | 5.10 ms: 1.39x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 17.3 us: 1.37x faster                                                       |
| deepcopy                   | 238 us                                                      | 188 us: 1.26x faster                                                        |
| scimark_sor                | 78.8 ms                                                     | 62.5 ms: 1.26x faster                                                       |
| nbody                      | 71.9 ms                                                     | 57.9 ms: 1.24x faster                                                       |
| scimark_fft                | 184 ms                                                      | 149 ms: 1.24x faster                                                        |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.08 ms: 1.23x faster                                                       |
| comprehensions             | 14.1 us                                                     | 12.0 us: 1.18x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 41.3 ms: 1.17x faster                                                       |
| unpickle_pure_python       | 133 us                                                      | 114 us: 1.17x faster                                                        |
| regex_effbot               | 1.62 ms                                                     | 1.41 ms: 1.15x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 38.1 ms: 1.15x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.20 sec: 1.14x faster                                                      |
| regex_dna                  | 126 ms                                                      | 112 ms: 1.13x faster                                                        |
| sqlite_synth               | 1.76 us                                                     | 1.57 us: 1.12x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.89 us: 1.10x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 50.6 ms: 1.10x faster                                                       |
| pyflate                    | 295 ms                                                      | 268 ms: 1.10x faster                                                        |
| dulwich_log                | 44.3 ms                                                     | 40.5 ms: 1.09x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 59.8 ms: 1.09x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 81.3 ms: 1.08x faster                                                       |
| chaos                      | 43.3 ms                                                     | 41.0 ms: 1.06x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 88.4 ms: 1.05x faster                                                       |
| fannkuch                   | 247 ms                                                      | 235 ms: 1.05x faster                                                        |
| pidigits                   | 152 ms                                                      | 146 ms: 1.04x faster                                                        |
| pprint_pformat             | 1.05 sec                                                    | 1.01 sec: 1.03x faster                                                      |
| json                       | 3.05 ms                                                     | 2.96 ms: 1.03x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 831 us: 1.03x faster                                                        |
| scimark_lu                 | 58.9 ms                                                     | 57.3 ms: 1.03x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 501 ms: 1.02x faster                                                        |
| pathlib                    | 80.5 ms                                                     | 78.5 ms: 1.02x faster                                                       |
| unpickle_list              | 2.75 us                                                     | 2.69 us: 1.02x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 37.0 ms: 1.02x faster                                                       |
| pickle_dict                | 18.4 us                                                     | 18.2 us: 1.01x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 60.1 ns: 1.01x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 74.9 ms: 1.00x slower                                                       |
| sympy_str                  | 175 ms                                                      | 178 ms: 1.02x slower                                                        |
| logging_format             | 6.72 us                                                     | 6.87 us: 1.02x slower                                                       |
| logging_simple             | 6.28 us                                                     | 6.43 us: 1.02x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 64.5 ms: 1.03x slower                                                       |
| go                         | 91.6 ms                                                     | 94.2 ms: 1.03x slower                                                       |
| pycparser                  | 699 ms                                                      | 721 ms: 1.03x slower                                                        |
| async_generators           | 239 ms                                                      | 248 ms: 1.04x slower                                                        |
| 2to3                       | 218 ms                                                      | 229 ms: 1.05x slower                                                        |
| sympy_integrate            | 13.0 ms                                                     | 13.6 ms: 1.05x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.7 us: 1.05x slower                                                       |
| pickle                     | 7.43 us                                                     | 7.84 us: 1.06x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.75 sec: 1.06x slower                                                      |
| coroutines                 | 14.3 ms                                                     | 15.1 ms: 1.06x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 853 us: 1.06x slower                                                        |
| telco                      | 4.13 ms                                                     | 4.38 ms: 1.06x slower                                                       |
| sympy_expand               | 284 ms                                                      | 304 ms: 1.07x slower                                                        |
| sqlglot_transpile          | 1.02 ms                                                     | 1.10 ms: 1.08x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.83 us: 1.08x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 17.9 ms: 1.10x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 216 us: 1.10x slower                                                        |
| raytrace                   | 192 ms                                                      | 213 ms: 1.11x slower                                                        |
| generators                 | 22.5 ms                                                     | 25.0 ms: 1.11x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 38.6 ms: 1.12x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 209 ms: 1.12x slower                                                        |
| deltablue                  | 2.16 ms                                                     | 2.43 ms: 1.12x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.48 ms: 1.14x slower                                                       |
| pickle_list                | 2.83 us                                                     | 3.24 us: 1.15x slower                                                       |
| asyncio_tcp                | 487 ms                                                      | 561 ms: 1.15x slower                                                        |
| mdp                        | 1.37 sec                                                    | 1.60 sec: 1.16x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 16.7 ms: 1.17x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 113 us: 1.18x slower                                                        |
| django_template            | 22.9 ms                                                     | 27.6 ms: 1.20x slower                                                       |
| python_startup             | 19.5 ms                                                     | 24.1 ms: 1.24x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 5.08 ms: 1.24x slower                                                       |
| coverage                   | 40.8 ms                                                     | 50.6 ms: 1.24x slower                                                       |
| richards_super             | 32.1 ms                                                     | 40.7 ms: 1.27x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 87.7 ms: 1.27x slower                                                       |
| richards                   | 28.4 ms                                                     | 36.1 ms: 1.27x slower                                                       |
| unpack_sequence            | 37.5 ns                                                     | 49.0 ns: 1.31x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.99 ms: 1.31x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.21 ms: 1.61x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                                |

Benchmark hidden because not significant (1): sympy_sum
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (13) of results/bm-20250118-3.14.0a4+-61b35f7-JIT/bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.056x faster

# HPT report

- Reliability score: 95.18% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown