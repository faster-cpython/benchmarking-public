# Results vs. 3.12.0

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: windows-amd64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.058x faster
- HPT reliability: 97.95%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 225 ms: 1.03x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.74 sec: 1.05x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 403 ms: 1.91x faster                                                        |
| async_tree_io              | 731 ms                                                      | 419 ms: 1.75x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 215 ms: 1.71x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 174 ms: 1.64x faster                                                        |
| async_tree_none            | 291 ms                                                      | 186 ms: 1.57x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 222 ms: 1.53x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 345 ms: 1.45x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 342 ms: 1.43x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.62x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 57.1 ms: 1.26x faster                                                       |
| float          | 56.8 ms                                                     | 46.1 ms: 1.23x faster                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 117 ms: 1.08x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.51 ms: 1.07x faster                                                       |
| regex_compile  | 87.5 ms                                                     | 82.2 ms: 1.06x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 15.0 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 113 us: 1.17x faster                                                        |
| tomli_loads          | 1.37 sec                                                    | 1.19 sec: 1.15x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 50.8 ms: 1.10x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 61.1 ms: 1.07x faster                                                       |
| unpickle_list        | 2.75 us                                                     | 2.63 us: 1.05x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 90.1 ms: 1.03x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 36.7 ms: 1.03x faster                                                       |
| pickle_dict          | 18.4 us                                                     | 18.0 us: 1.02x faster                                                       |
| unpickle             | 8.18 us                                                     | 8.51 us: 1.04x slower                                                       |
| pickle               | 7.43 us                                                     | 7.81 us: 1.05x slower                                                       |
| pickle_list          | 2.83 us                                                     | 3.00 us: 1.06x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 217 us: 1.11x slower                                                        |
| json_loads           | 13.9 us                                                     | 15.5 us: 1.11x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.69 ms: 1.17x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.00x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.7 ms: 1.21x slower                                                       |
| python_startup         | 19.5 ms                                                     | 26.4 ms: 1.36x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.28x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.24 ms: 1.35x faster                                                       |
| django_template | 22.9 ms                                                     | 25.8 ms: 1.13x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.10x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 403 ms: 1.91x faster                                                        |
| async_tree_io              | 731 ms                                                      | 419 ms: 1.75x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 215 ms: 1.71x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 174 ms: 1.64x faster                                                        |
| async_tree_none            | 291 ms                                                      | 186 ms: 1.57x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 222 ms: 1.53x faster                                                        |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.44 sec: 1.46x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 345 ms: 1.45x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 342 ms: 1.43x faster                                                        |
| mako                       | 7.09 ms                                                     | 5.24 ms: 1.35x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 62.1 ms: 1.30x faster                                                       |
| deepcopy                   | 238 us                                                      | 186 us: 1.28x faster                                                        |
| comprehensions             | 14.1 us                                                     | 11.2 us: 1.26x faster                                                       |
| nbody                      | 71.9 ms                                                     | 57.1 ms: 1.26x faster                                                       |
| scimark_fft                | 184 ms                                                      | 148 ms: 1.25x faster                                                        |
| float                      | 56.8 ms                                                     | 46.1 ms: 1.23x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.09 ms: 1.23x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 19.4 us: 1.22x faster                                                       |
| unpickle_pure_python       | 133 us                                                      | 113 us: 1.17x faster                                                        |
| spectral_norm              | 66.9 ms                                                     | 57.9 ms: 1.16x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.19 sec: 1.15x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.54 us: 1.14x faster                                                       |
| generators                 | 22.5 ms                                                     | 20.2 ms: 1.12x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 12.8 ms: 1.11x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 50.8 ms: 1.10x faster                                                       |
| pyflate                    | 295 ms                                                      | 273 ms: 1.08x faster                                                        |
| regex_dna                  | 126 ms                                                      | 117 ms: 1.08x faster                                                        |
| deepcopy_reduce            | 2.09 us                                                     | 1.95 us: 1.08x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 975 ms: 1.07x faster                                                        |
| regex_effbot               | 1.62 ms                                                     | 1.51 ms: 1.07x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.1 ms: 1.07x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 82.2 ms: 1.06x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 45.8 ms: 1.06x faster                                                       |
| go                         | 91.6 ms                                                     | 87.6 ms: 1.05x faster                                                       |
| unpickle_list              | 2.75 us                                                     | 2.63 us: 1.05x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 42.5 ms: 1.04x faster                                                       |
| chaos                      | 43.3 ms                                                     | 41.7 ms: 1.04x faster                                                       |
| fannkuch                   | 247 ms                                                      | 239 ms: 1.03x faster                                                        |
| xml_etree_parse            | 93.0 ms                                                     | 90.1 ms: 1.03x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 36.7 ms: 1.03x faster                                                       |
| pickle_dict                | 18.4 us                                                     | 18.0 us: 1.02x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 59.5 ns: 1.02x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 62.0 ms: 1.01x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 90.5 ms: 1.01x faster                                                       |
| sympy_str                  | 175 ms                                                      | 177 ms: 1.01x slower                                                        |
| raytrace                   | 192 ms                                                      | 195 ms: 1.01x slower                                                        |
| meteor_contest             | 74.6 ms                                                     | 75.8 ms: 1.02x slower                                                       |
| logging_format             | 6.72 us                                                     | 6.83 us: 1.02x slower                                                       |
| pycparser                  | 699 ms                                                      | 713 ms: 1.02x slower                                                        |
| logging_simple             | 6.28 us                                                     | 6.41 us: 1.02x slower                                                       |
| json                       | 3.05 ms                                                     | 3.12 ms: 1.02x slower                                                       |
| 2to3                       | 218 ms                                                      | 225 ms: 1.03x slower                                                        |
| scimark_monte_carlo        | 43.7 ms                                                     | 45.4 ms: 1.04x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 61.1 ms: 1.04x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.06 ms: 1.04x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.51 us: 1.04x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.5 ms: 1.04x slower                                                       |
| richards                   | 28.4 ms                                                     | 29.7 ms: 1.04x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.74 sec: 1.05x slower                                                      |
| richards_super             | 32.1 ms                                                     | 33.6 ms: 1.05x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 842 us: 1.05x slower                                                        |
| pickle                     | 7.43 us                                                     | 7.81 us: 1.05x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 15.0 ms: 1.06x slower                                                       |
| pickle_list                | 2.83 us                                                     | 3.00 us: 1.06x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 84.2 ms: 1.07x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.42 ms: 1.08x slower                                                       |
| sympy_expand               | 284 ms                                                      | 307 ms: 1.08x slower                                                        |
| deltablue                  | 2.16 ms                                                     | 2.34 ms: 1.08x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 203 ms: 1.09x slower                                                        |
| sqlglot_optimize           | 34.5 ms                                                     | 37.6 ms: 1.09x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.55 ms: 1.10x slower                                                       |
| asyncio_tcp                | 487 ms                                                      | 541 ms: 1.11x slower                                                        |
| pickle_pure_python         | 195 us                                                      | 217 us: 1.11x slower                                                        |
| json_loads                 | 13.9 us                                                     | 15.5 us: 1.11x slower                                                       |
| django_template            | 22.9 ms                                                     | 25.8 ms: 1.13x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 108 us: 1.14x slower                                                        |
| unpack_sequence            | 37.5 ns                                                     | 43.6 ns: 1.16x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.60 sec: 1.17x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 6.69 ms: 1.17x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 19.7 ms: 1.21x slower                                                       |
| coverage                   | 40.8 ms                                                     | 49.6 ms: 1.21x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 89.9 ms: 1.30x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.05 ms: 1.35x slower                                                       |
| python_startup             | 19.5 ms                                                     | 26.4 ms: 1.36x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.24 ms: 1.65x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                                |

Benchmark hidden because not significant (4): pprint_safe_repr, bench_thread_pool, pidigits, async_generators
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (13) of results/bm-20250208-3.14.0a4+-29f8a67-JIT/bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.058x faster

# HPT report

- Reliability score: 97.95% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown