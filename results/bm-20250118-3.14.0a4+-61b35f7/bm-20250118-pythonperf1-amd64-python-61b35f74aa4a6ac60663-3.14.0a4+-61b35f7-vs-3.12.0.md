# Results vs. 3.12.0

- fork: python
- ref: 61b35f74aa4a6ac60663
- machine: windows-amd64
- commit hash: 61b35f7
- commit date: 2025-01-18
- overall geometric mean: 1.028x slower
- HPT reliability: 99.78%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 237 ms: 1.09x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.70 sec: 1.03x slower                                                      |
| Geometric mean | (ref)                                                       | 1.06x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 421 ms: 1.83x faster                                                        |
| async_tree_io              | 731 ms                                                      | 432 ms: 1.69x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 220 ms: 1.66x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 181 ms: 1.58x faster                                                        |
| async_tree_none            | 291 ms                                                      | 196 ms: 1.49x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 236 ms: 1.44x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 351 ms: 1.43x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 356 ms: 1.37x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.55x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 53.1 ms: 1.07x faster                                                       |
| pidigits       | 152 ms                                                      | 147 ms: 1.04x faster                                                        |
| nbody          | 71.9 ms                                                     | 80.9 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                       | 1.00x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 117 ms: 1.08x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.53 ms: 1.06x faster                                                       |
| regex_compile  | 87.5 ms                                                     | 93.6 ms: 1.07x slower                                                       |
| regex_v8       | 14.2 ms                                                     | 16.1 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 88.8 ms: 1.05x faster                                                       |
| pickle_dict          | 18.4 us                                                     | 18.0 us: 1.02x faster                                                       |
| unpickle_list        | 2.75 us                                                     | 2.77 us: 1.01x slower                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 66.2 ms: 1.02x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.47 us: 1.04x slower                                                       |
| pickle               | 7.43 us                                                     | 7.91 us: 1.06x slower                                                       |
| json_loads           | 13.9 us                                                     | 14.9 us: 1.07x slower                                                       |
| pickle_list          | 2.83 us                                                     | 3.06 us: 1.08x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.49 sec: 1.09x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 63.3 ms: 1.13x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 45.3 ms: 1.20x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 240 us: 1.23x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 7.00 ms: 1.23x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 164 us: 1.23x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.0 ms: 1.11x slower                                                       |
| python_startup         | 19.5 ms                                                     | 24.2 ms: 1.24x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.17x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 7.26 ms: 1.02x slower                                                       |
| django_template | 22.9 ms                                                     | 27.3 ms: 1.19x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.10x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 421 ms: 1.83x faster                                                        |
| async_tree_io              | 731 ms                                                      | 432 ms: 1.69x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 220 ms: 1.66x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 181 ms: 1.58x faster                                                        |
| async_tree_none            | 291 ms                                                      | 196 ms: 1.49x faster                                                        |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.43 sec: 1.47x faster                                                      |
| async_tree_memoization     | 339 ms                                                      | 236 ms: 1.44x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 351 ms: 1.43x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 356 ms: 1.37x faster                                                        |
| deepcopy                   | 238 us                                                      | 196 us: 1.22x faster                                                        |
| sqlite_synth               | 1.76 us                                                     | 1.61 us: 1.09x faster                                                       |
| regex_dna                  | 126 ms                                                      | 117 ms: 1.08x faster                                                        |
| comprehensions             | 14.1 us                                                     | 13.1 us: 1.08x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.95 us: 1.07x faster                                                       |
| float                      | 56.8 ms                                                     | 53.1 ms: 1.07x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.53 ms: 1.06x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 22.5 us: 1.05x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 88.8 ms: 1.05x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 64.1 ms: 1.04x faster                                                       |
| pidigits                   | 152 ms                                                      | 147 ms: 1.04x faster                                                        |
| pathlib                    | 80.5 ms                                                     | 78.1 ms: 1.03x faster                                                       |
| pickle_dict                | 18.4 us                                                     | 18.0 us: 1.02x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 43.4 ms: 1.02x faster                                                       |
| json                       | 3.05 ms                                                     | 3.01 ms: 1.01x faster                                                       |
| async_generators           | 239 ms                                                      | 237 ms: 1.01x faster                                                        |
| unpickle_list              | 2.75 us                                                     | 2.77 us: 1.01x slower                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 66.2 ms: 1.02x slower                                                       |
| chaos                      | 43.3 ms                                                     | 44.1 ms: 1.02x slower                                                       |
| mako                       | 7.09 ms                                                     | 7.26 ms: 1.02x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.70 sec: 1.03x slower                                                      |
| sympy_str                  | 175 ms                                                      | 181 ms: 1.03x slower                                                        |
| unpickle                   | 8.18 us                                                     | 8.47 us: 1.04x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.66 ms: 1.04x slower                                                       |
| generators                 | 22.5 ms                                                     | 23.5 ms: 1.04x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 77.9 ms: 1.04x slower                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 50.7 ms: 1.05x slower                                                       |
| go                         | 91.6 ms                                                     | 96.0 ms: 1.05x slower                                                       |
| logging_simple             | 6.28 us                                                     | 6.61 us: 1.05x slower                                                       |
| logging_format             | 6.72 us                                                     | 7.12 us: 1.06x slower                                                       |
| pickle                     | 7.43 us                                                     | 7.91 us: 1.06x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.8 ms: 1.07x slower                                                       |
| scimark_fft                | 184 ms                                                      | 197 ms: 1.07x slower                                                        |
| regex_compile              | 87.5 ms                                                     | 93.6 ms: 1.07x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.9 us: 1.07x slower                                                       |
| pickle_list                | 2.83 us                                                     | 3.06 us: 1.08x slower                                                       |
| sympy_expand               | 284 ms                                                      | 309 ms: 1.09x slower                                                        |
| 2to3                       | 218 ms                                                      | 237 ms: 1.09x slower                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.49 sec: 1.09x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 37.6 ms: 1.09x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 204 ms: 1.09x slower                                                        |
| pycparser                  | 699 ms                                                      | 764 ms: 1.09x slower                                                        |
| nqueens                    | 62.8 ms                                                     | 68.7 ms: 1.09x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.15 sec: 1.10x slower                                                      |
| unpack_sequence            | 37.5 ns                                                     | 41.4 ns: 1.10x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 18.0 ms: 1.11x slower                                                       |
| pyflate                    | 295 ms                                                      | 326 ms: 1.11x slower                                                        |
| pprint_safe_repr           | 513 ms                                                      | 573 ms: 1.12x slower                                                        |
| raytrace                   | 192 ms                                                      | 215 ms: 1.12x slower                                                        |
| nbody                      | 71.9 ms                                                     | 80.9 ms: 1.13x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 16.1 ms: 1.13x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 63.3 ms: 1.13x slower                                                       |
| coroutines                 | 14.3 ms                                                     | 16.2 ms: 1.14x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.16 ms: 1.14x slower                                                       |
| asyncio_tcp                | 487 ms                                                      | 556 ms: 1.14x slower                                                        |
| scimark_monte_carlo        | 43.7 ms                                                     | 49.9 ms: 1.14x slower                                                       |
| fannkuch                   | 247 ms                                                      | 288 ms: 1.17x slower                                                        |
| scimark_lu                 | 58.9 ms                                                     | 69.0 ms: 1.17x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.84 ms: 1.17x slower                                                       |
| richards                   | 28.4 ms                                                     | 33.3 ms: 1.17x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 946 us: 1.18x slower                                                        |
| richards_super             | 32.1 ms                                                     | 37.8 ms: 1.18x slower                                                       |
| django_template            | 22.9 ms                                                     | 27.3 ms: 1.19x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.58 ms: 1.19x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 45.3 ms: 1.20x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.92 ms: 1.20x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.65 sec: 1.21x slower                                                      |
| coverage                   | 40.8 ms                                                     | 49.7 ms: 1.22x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 240 us: 1.23x slower                                                        |
| json_dumps                 | 5.70 ms                                                     | 7.00 ms: 1.23x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 117 us: 1.23x slower                                                        |
| unpickle_pure_python       | 133 us                                                      | 164 us: 1.23x slower                                                        |
| python_startup             | 19.5 ms                                                     | 24.2 ms: 1.24x slower                                                       |
| logging_silent             | 60.5 ns                                                     | 75.3 ns: 1.25x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 98.3 ms: 1.25x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 88.2 ms: 1.28x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.97 ms: 1.29x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.20 ms: 1.60x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                                |

Benchmark hidden because not significant (2): bench_thread_pool, sympy_sum
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (13) of results/bm-20250118-3.14.0a4+-61b35f7/bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.028x slower

# HPT report

- Reliability score: 99.78% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown