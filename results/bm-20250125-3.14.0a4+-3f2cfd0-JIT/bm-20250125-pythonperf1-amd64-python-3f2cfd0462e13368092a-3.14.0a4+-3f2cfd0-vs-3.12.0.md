# Results vs. 3.12.0

- fork: python
- ref: 3f2cfd0462e13368092a
- machine: windows-amd64
- commit hash: 3f2cfd0
- commit date: 2025-01-25
- overall geometric mean: 1.052x faster
- HPT reliability: 92.13%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 231 ms: 1.06x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.76 sec: 1.06x slower                                                      |
| Geometric mean | (ref)                                                       | 1.06x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 412 ms: 1.87x faster                                                        |
| async_tree_io              | 731 ms                                                      | 426 ms: 1.72x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 218 ms: 1.68x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 177 ms: 1.61x faster                                                        |
| async_tree_none            | 291 ms                                                      | 190 ms: 1.53x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 226 ms: 1.50x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 348 ms: 1.44x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 345 ms: 1.42x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.59x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 40.4 ms: 1.41x faster                                                       |
| nbody          | 71.9 ms                                                     | 55.9 ms: 1.29x faster                                                       |
| pidigits       | 152 ms                                                      | 146 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                       | 1.23x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 114 ms: 1.11x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.48 ms: 1.09x faster                                                       |
| regex_compile  | 87.5 ms                                                     | 84.6 ms: 1.03x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 15.1 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 112 us: 1.19x faster                                                        |
| tomli_loads          | 1.37 sec                                                    | 1.21 sec: 1.13x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 50.2 ms: 1.11x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 60.0 ms: 1.09x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 88.5 ms: 1.05x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 36.8 ms: 1.03x faster                                                       |
| pickle_dict          | 18.4 us                                                     | 18.3 us: 1.01x faster                                                       |
| unpickle_list        | 2.75 us                                                     | 2.80 us: 1.02x slower                                                       |
| pickle               | 7.43 us                                                     | 7.93 us: 1.07x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.86 us: 1.08x slower                                                       |
| pickle_list          | 2.83 us                                                     | 3.08 us: 1.09x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 213 us: 1.09x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 6.27 ms: 1.10x slower                                                       |
| json_loads           | 13.9 us                                                     | 16.0 us: 1.15x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.00x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.8 ms: 1.10x slower                                                       |
| python_startup         | 19.5 ms                                                     | 24.1 ms: 1.24x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.17x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.09 ms: 1.39x faster                                                       |
| django_template | 22.9 ms                                                     | 27.4 ms: 1.20x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.08x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 412 ms: 1.87x faster                                                        |
| async_tree_io              | 731 ms                                                      | 426 ms: 1.72x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 218 ms: 1.68x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 177 ms: 1.61x faster                                                        |
| async_tree_none            | 291 ms                                                      | 190 ms: 1.53x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 226 ms: 1.50x faster                                                        |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.43 sec: 1.47x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 348 ms: 1.44x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 345 ms: 1.42x faster                                                        |
| float                      | 56.8 ms                                                     | 40.4 ms: 1.41x faster                                                       |
| mako                       | 7.09 ms                                                     | 5.09 ms: 1.39x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 17.1 us: 1.39x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 49.2 ms: 1.36x faster                                                       |
| nbody                      | 71.9 ms                                                     | 55.9 ms: 1.29x faster                                                       |
| deepcopy                   | 238 us                                                      | 188 us: 1.27x faster                                                        |
| scimark_fft                | 184 ms                                                      | 146 ms: 1.26x faster                                                        |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.04 ms: 1.26x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 63.2 ms: 1.25x faster                                                       |
| unpickle_pure_python       | 133 us                                                      | 112 us: 1.19x faster                                                        |
| comprehensions             | 14.1 us                                                     | 11.9 us: 1.19x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 41.1 ms: 1.18x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 38.3 ms: 1.14x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.21 sec: 1.13x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.58 us: 1.12x faster                                                       |
| regex_dna                  | 126 ms                                                      | 114 ms: 1.11x faster                                                        |
| xml_etree_generate         | 55.8 ms                                                     | 50.2 ms: 1.11x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.89 us: 1.11x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.48 ms: 1.09x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 60.0 ms: 1.09x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 970 ms: 1.08x faster                                                        |
| pyflate                    | 295 ms                                                      | 277 ms: 1.06x faster                                                        |
| pprint_safe_repr           | 513 ms                                                      | 487 ms: 1.05x faster                                                        |
| xml_etree_parse            | 93.0 ms                                                     | 88.5 ms: 1.05x faster                                                       |
| pidigits                   | 152 ms                                                      | 146 ms: 1.04x faster                                                        |
| regex_compile              | 87.5 ms                                                     | 84.6 ms: 1.03x faster                                                       |
| scimark_lu                 | 58.9 ms                                                     | 56.9 ms: 1.03x faster                                                       |
| chaos                      | 43.3 ms                                                     | 42.0 ms: 1.03x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 43.1 ms: 1.03x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 36.8 ms: 1.03x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 78.5 ms: 1.02x faster                                                       |
| fannkuch                   | 247 ms                                                      | 241 ms: 1.02x faster                                                        |
| logging_silent             | 60.5 ns                                                     | 59.4 ns: 1.02x faster                                                       |
| pickle_dict                | 18.4 us                                                     | 18.3 us: 1.01x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 63.7 ms: 1.02x slower                                                       |
| coroutines                 | 14.3 ms                                                     | 14.5 ms: 1.02x slower                                                       |
| sympy_sum                  | 91.5 ms                                                     | 93.1 ms: 1.02x slower                                                       |
| unpickle_list              | 2.75 us                                                     | 2.80 us: 1.02x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 76.8 ms: 1.03x slower                                                       |
| logging_format             | 6.72 us                                                     | 6.92 us: 1.03x slower                                                       |
| logging_simple             | 6.28 us                                                     | 6.48 us: 1.03x slower                                                       |
| async_generators           | 239 ms                                                      | 248 ms: 1.04x slower                                                        |
| sympy_str                  | 175 ms                                                      | 182 ms: 1.04x slower                                                        |
| go                         | 91.6 ms                                                     | 95.4 ms: 1.04x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.6 ms: 1.05x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.34 ms: 1.05x slower                                                       |
| pycparser                  | 699 ms                                                      | 736 ms: 1.05x slower                                                        |
| 2to3                       | 218 ms                                                      | 231 ms: 1.06x slower                                                        |
| regex_v8                   | 14.2 ms                                                     | 15.1 ms: 1.06x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.76 sec: 1.06x slower                                                      |
| pickle                     | 7.43 us                                                     | 7.93 us: 1.07x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 869 us: 1.08x slower                                                        |
| unpickle                   | 8.18 us                                                     | 8.86 us: 1.08x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.11 ms: 1.09x slower                                                       |
| pickle_list                | 2.83 us                                                     | 3.08 us: 1.09x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 213 us: 1.09x slower                                                        |
| sympy_expand               | 284 ms                                                      | 311 ms: 1.09x slower                                                        |
| python_startup_no_site     | 16.2 ms                                                     | 17.8 ms: 1.10x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.27 ms: 1.10x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 208 ms: 1.11x slower                                                        |
| generators                 | 22.5 ms                                                     | 25.0 ms: 1.11x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 38.5 ms: 1.11x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.53 sec: 1.12x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.42 ms: 1.12x slower                                                       |
| asyncio_tcp                | 487 ms                                                      | 557 ms: 1.14x slower                                                        |
| unpack_sequence            | 37.5 ns                                                     | 43.0 ns: 1.15x slower                                                       |
| json_loads                 | 13.9 us                                                     | 16.0 us: 1.15x slower                                                       |
| coverage                   | 40.8 ms                                                     | 47.7 ms: 1.17x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 112 us: 1.18x slower                                                        |
| raytrace                   | 192 ms                                                      | 228 ms: 1.19x slower                                                        |
| django_template            | 22.9 ms                                                     | 27.4 ms: 1.20x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 5.05 ms: 1.23x slower                                                       |
| python_startup             | 19.5 ms                                                     | 24.1 ms: 1.24x slower                                                       |
| richards_super             | 32.1 ms                                                     | 40.6 ms: 1.27x slower                                                       |
| richards                   | 28.4 ms                                                     | 35.9 ms: 1.27x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 88.4 ms: 1.28x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.98 ms: 1.30x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.22 ms: 1.62x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                                |

Benchmark hidden because not significant (2): bench_thread_pool, json
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (13) of results/bm-20250125-3.14.0a4+-3f2cfd0-JIT/bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.052x faster

# HPT report

- Reliability score: 92.13% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown