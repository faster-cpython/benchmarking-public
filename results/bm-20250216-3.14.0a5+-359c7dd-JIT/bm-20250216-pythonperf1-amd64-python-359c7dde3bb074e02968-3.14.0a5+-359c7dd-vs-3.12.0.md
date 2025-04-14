# Results vs. 3.12.0

- fork: python
- ref: 359c7dde3bb074e02968
- machine: windows-amd64
- commit hash: 359c7dd
- commit date: 2025-02-16
- overall geometric mean: 1.075x faster
- HPT reliability: 98.91%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 1.66 sec                                                    | 1.69 sec: 1.02x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 413 ms: 1.87x faster                                                        |
| async_tree_io              | 731 ms                                                      | 415 ms: 1.76x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 218 ms: 1.68x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 177 ms: 1.61x faster                                                        |
| async_tree_none            | 291 ms                                                      | 186 ms: 1.57x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 222 ms: 1.53x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 347 ms: 1.45x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 347 ms: 1.41x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.60x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 44.8 ms: 1.27x faster                                                       |
| nbody          | 71.9 ms                                                     | 59.8 ms: 1.20x faster                                                       |
| pidigits       | 152 ms                                                      | 150 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.45 ms: 1.12x faster                                                       |
| regex_dna      | 126 ms                                                      | 114 ms: 1.11x faster                                                        |
| regex_compile  | 87.5 ms                                                     | 82.7 ms: 1.06x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 14.5 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.21 sec: 1.13x faster                                                      |
| unpickle_pure_python | 133 us                                                      | 118 us: 1.12x faster                                                        |
| xml_etree_generate   | 55.8 ms                                                     | 51.5 ms: 1.09x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 61.1 ms: 1.07x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 89.1 ms: 1.04x faster                                                       |
| unpickle_list        | 2.75 us                                                     | 2.65 us: 1.04x faster                                                       |
| pickle_dict          | 18.4 us                                                     | 17.9 us: 1.03x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 37.0 ms: 1.02x faster                                                       |
| unpickle             | 8.18 us                                                     | 8.57 us: 1.05x slower                                                       |
| pickle_list          | 2.83 us                                                     | 2.97 us: 1.05x slower                                                       |
| pickle               | 7.43 us                                                     | 7.83 us: 1.05x slower                                                       |
| json_loads           | 13.9 us                                                     | 14.8 us: 1.06x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 209 us: 1.07x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 6.55 ms: 1.15x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.6 ms: 1.14x slower                                                       |
| python_startup         | 19.5 ms                                                     | 24.5 ms: 1.26x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.20x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.34 ms: 1.33x faster                                                       |
| django_template | 22.9 ms                                                     | 26.0 ms: 1.13x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.08x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 29.1 ms: 2.77x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 413 ms: 1.87x faster                                                        |
| async_tree_io              | 731 ms                                                      | 415 ms: 1.76x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 218 ms: 1.68x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 177 ms: 1.61x faster                                                        |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.31 sec: 1.61x faster                                                      |
| async_tree_none            | 291 ms                                                      | 186 ms: 1.57x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 222 ms: 1.53x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 347 ms: 1.45x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 347 ms: 1.41x faster                                                        |
| mako                       | 7.09 ms                                                     | 5.34 ms: 1.33x faster                                                       |
| deepcopy                   | 238 us                                                      | 184 us: 1.29x faster                                                        |
| comprehensions             | 14.1 us                                                     | 11.1 us: 1.27x faster                                                       |
| float                      | 56.8 ms                                                     | 44.8 ms: 1.27x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 19.0 us: 1.25x faster                                                       |
| scimark_fft                | 184 ms                                                      | 153 ms: 1.20x faster                                                        |
| nbody                      | 71.9 ms                                                     | 59.8 ms: 1.20x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.17 ms: 1.18x faster                                                       |
| asyncio_tcp                | 487 ms                                                      | 416 ms: 1.17x faster                                                        |
| sqlite_synth               | 1.76 us                                                     | 1.52 us: 1.16x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.21 sec: 1.13x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 118 us: 1.12x faster                                                        |
| spectral_norm              | 66.9 ms                                                     | 59.6 ms: 1.12x faster                                                       |
| generators                 | 22.5 ms                                                     | 20.1 ms: 1.12x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.45 ms: 1.12x faster                                                       |
| regex_dna                  | 126 ms                                                      | 114 ms: 1.11x faster                                                        |
| pyflate                    | 295 ms                                                      | 271 ms: 1.09x faster                                                        |
| xml_etree_generate         | 55.8 ms                                                     | 51.5 ms: 1.09x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.94 us: 1.08x faster                                                       |
| fannkuch                   | 247 ms                                                      | 230 ms: 1.07x faster                                                        |
| nqueens                    | 62.8 ms                                                     | 58.9 ms: 1.07x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.1 ms: 1.07x faster                                                       |
| go                         | 91.6 ms                                                     | 86.2 ms: 1.06x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 41.8 ms: 1.06x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 82.7 ms: 1.06x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 89.1 ms: 1.04x faster                                                       |
| unpickle_list              | 2.75 us                                                     | 2.65 us: 1.04x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 46.9 ms: 1.03x faster                                                       |
| chaos                      | 43.3 ms                                                     | 42.0 ms: 1.03x faster                                                       |
| pickle_dict                | 18.4 us                                                     | 17.9 us: 1.03x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 89.1 ms: 1.03x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.9 ms: 1.03x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 59.0 ns: 1.03x faster                                                       |
| async_generators           | 239 ms                                                      | 234 ms: 1.02x faster                                                        |
| xml_etree_process          | 37.7 ms                                                     | 37.0 ms: 1.02x faster                                                       |
| pidigits                   | 152 ms                                                      | 150 ms: 1.02x faster                                                        |
| pprint_pformat             | 1.05 sec                                                    | 1.03 sec: 1.01x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 73.7 ms: 1.01x faster                                                       |
| json                       | 3.05 ms                                                     | 3.01 ms: 1.01x faster                                                       |
| sympy_str                  | 175 ms                                                      | 176 ms: 1.01x slower                                                        |
| raytrace                   | 192 ms                                                      | 194 ms: 1.01x slower                                                        |
| logging_simple             | 6.28 us                                                     | 6.37 us: 1.01x slower                                                       |
| logging_format             | 6.72 us                                                     | 6.83 us: 1.02x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.69 sec: 1.02x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 14.5 ms: 1.02x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 44.6 ms: 1.02x slower                                                       |
| richards                   | 28.4 ms                                                     | 29.1 ms: 1.03x slower                                                       |
| richards_super             | 32.1 ms                                                     | 33.0 ms: 1.03x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.3 ms: 1.03x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 529 ms: 1.03x slower                                                        |
| deltablue                  | 2.16 ms                                                     | 2.23 ms: 1.03x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.28 ms: 1.04x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.57 us: 1.05x slower                                                       |
| pycparser                  | 699 ms                                                      | 732 ms: 1.05x slower                                                        |
| pickle_list                | 2.83 us                                                     | 2.97 us: 1.05x slower                                                       |
| pickle                     | 7.43 us                                                     | 7.83 us: 1.05x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.08 ms: 1.05x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 854 us: 1.06x slower                                                        |
| sqlglot_normalize          | 187 ms                                                      | 199 ms: 1.06x slower                                                        |
| json_loads                 | 13.9 us                                                     | 14.8 us: 1.06x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 36.8 ms: 1.07x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 63.0 ms: 1.07x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 84.3 ms: 1.07x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 209 us: 1.07x slower                                                        |
| sympy_expand               | 284 ms                                                      | 307 ms: 1.08x slower                                                        |
| telco                      | 4.13 ms                                                     | 4.47 ms: 1.08x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.54 sec: 1.12x slower                                                      |
| django_template            | 22.9 ms                                                     | 26.0 ms: 1.13x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 18.6 ms: 1.14x slower                                                       |
| unpack_sequence            | 37.5 ns                                                     | 42.9 ns: 1.15x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.55 ms: 1.15x slower                                                       |
| coverage                   | 40.8 ms                                                     | 47.5 ms: 1.16x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 111 us: 1.17x slower                                                        |
| bench_mp_pool              | 69.2 ms                                                     | 83.9 ms: 1.21x slower                                                       |
| python_startup             | 19.5 ms                                                     | 24.5 ms: 1.26x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.00 ms: 1.31x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.23 ms: 1.64x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.07x faster                                                                |

Benchmark hidden because not significant (2): bench_thread_pool, 2to3
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (13) of results/bm-20250216-3.14.0a5+-359c7dd-JIT/bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.075x faster

# HPT report

- Reliability score: 98.91% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown