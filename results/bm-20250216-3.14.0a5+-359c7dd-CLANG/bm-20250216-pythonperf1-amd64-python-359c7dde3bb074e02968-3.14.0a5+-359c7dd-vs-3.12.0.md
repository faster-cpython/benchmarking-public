# Results vs. 3.12.0

- fork: python
- ref: 359c7dde3bb074e02968
- machine: windows-amd64
- commit hash: 359c7dd
- commit date: 2025-02-16
- overall geometric mean: 1.046x faster
- HPT reliability: 81.49%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 224 ms: 1.03x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.71 sec: 1.03x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 388 ms: 1.99x faster                                                        |
| async_tree_io              | 731 ms                                                      | 392 ms: 1.86x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 208 ms: 1.77x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 168 ms: 1.69x faster                                                        |
| async_tree_none            | 291 ms                                                      | 177 ms: 1.65x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 210 ms: 1.62x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 364 ms: 1.38x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 359 ms: 1.36x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.65x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 44.1 ms: 1.29x faster                                                       |
| nbody          | 71.9 ms                                                     | 68.3 ms: 1.05x faster                                                       |
| pidigits       | 152 ms                                                      | 154 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 84.4 ms: 1.04x faster                                                       |
| regex_dna      | 126 ms                                                      | 130 ms: 1.03x slower                                                        |
| regex_v8       | 14.2 ms                                                     | 16.5 ms: 1.16x slower                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.93 ms: 1.19x slower                                                       |
| Geometric mean | (ref)                                                       | 1.08x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_dict          | 18.4 us                                                     | 16.5 us: 1.11x faster                                                       |
| unpickle_list        | 2.75 us                                                     | 2.48 us: 1.11x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.31 sec: 1.05x faster                                                      |
| pickle_list          | 2.83 us                                                     | 2.80 us: 1.01x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 68.1 ms: 1.04x slower                                                       |
| pickle               | 7.43 us                                                     | 7.85 us: 1.06x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 141 us: 1.06x slower                                                        |
| pickle_pure_python   | 195 us                                                      | 209 us: 1.07x slower                                                        |
| xml_etree_parse      | 93.0 ms                                                     | 102 ms: 1.10x slower                                                        |
| xml_etree_generate   | 55.8 ms                                                     | 63.6 ms: 1.14x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 43.7 ms: 1.16x slower                                                       |
| unpickle             | 8.18 us                                                     | 9.53 us: 1.16x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 7.81 ms: 1.37x slower                                                       |
| json_loads           | 13.9 us                                                     | 19.3 us: 1.39x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.08x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.8 ms: 1.22x slower                                                       |
| python_startup         | 19.5 ms                                                     | 25.7 ms: 1.32x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.27x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 24.2 ms: 1.05x slower                                                       |
| mako            | 7.09 ms                                                     | 7.57 ms: 1.07x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.06x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 29.2 ms: 2.76x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 388 ms: 1.99x faster                                                        |
| async_tree_io              | 731 ms                                                      | 392 ms: 1.86x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 208 ms: 1.77x faster                                                        |
| unpack_sequence            | 37.5 ns                                                     | 21.7 ns: 1.72x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 168 ms: 1.69x faster                                                        |
| async_tree_none            | 291 ms                                                      | 177 ms: 1.65x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 210 ms: 1.62x faster                                                        |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.30 sec: 1.61x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 364 ms: 1.38x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 359 ms: 1.36x faster                                                        |
| deepcopy                   | 238 us                                                      | 175 us: 1.36x faster                                                        |
| deepcopy_memo              | 23.7 us                                                     | 17.8 us: 1.33x faster                                                       |
| generators                 | 22.5 ms                                                     | 17.4 ms: 1.29x faster                                                       |
| go                         | 91.6 ms                                                     | 70.8 ms: 1.29x faster                                                       |
| float                      | 56.8 ms                                                     | 44.1 ms: 1.29x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.4 us: 1.24x faster                                                       |
| asyncio_tcp                | 487 ms                                                      | 396 ms: 1.23x faster                                                        |
| spectral_norm              | 66.9 ms                                                     | 55.8 ms: 1.20x faster                                                       |
| deltablue                  | 2.16 ms                                                     | 1.82 ms: 1.19x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 38.9 ms: 1.12x faster                                                       |
| raytrace                   | 192 ms                                                      | 172 ms: 1.12x faster                                                        |
| pickle_dict                | 18.4 us                                                     | 16.5 us: 1.11x faster                                                       |
| unpickle_list              | 2.75 us                                                     | 2.48 us: 1.11x faster                                                       |
| chaos                      | 43.3 ms                                                     | 39.2 ms: 1.11x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.90 us: 1.10x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 71.6 ms: 1.10x faster                                                       |
| async_generators           | 239 ms                                                      | 220 ms: 1.09x faster                                                        |
| sqlite_synth               | 1.76 us                                                     | 1.63 us: 1.08x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 41.7 ms: 1.06x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 57.3 ns: 1.06x faster                                                       |
| nbody                      | 71.9 ms                                                     | 68.3 ms: 1.05x faster                                                       |
| hexiom                     | 4.10 ms                                                     | 3.90 ms: 1.05x faster                                                       |
| pyflate                    | 295 ms                                                      | 281 ms: 1.05x faster                                                        |
| meteor_contest             | 74.6 ms                                                     | 71.2 ms: 1.05x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.31 sec: 1.05x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 13.8 ms: 1.04x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 84.4 ms: 1.04x faster                                                       |
| richards                   | 28.4 ms                                                     | 27.5 ms: 1.03x faster                                                       |
| logging_simple             | 6.28 us                                                     | 6.14 us: 1.02x faster                                                       |
| richards_super             | 32.1 ms                                                     | 31.4 ms: 1.02x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.58 us: 1.02x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.52 ms: 1.02x faster                                                       |
| pickle_list                | 2.83 us                                                     | 2.80 us: 1.01x faster                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.01 ms: 1.01x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 62.4 ms: 1.01x faster                                                       |
| sqlglot_normalize          | 187 ms                                                      | 188 ms: 1.01x slower                                                        |
| sympy_str                  | 175 ms                                                      | 176 ms: 1.01x slower                                                        |
| pidigits                   | 152 ms                                                      | 154 ms: 1.01x slower                                                        |
| pprint_pformat             | 1.05 sec                                                    | 1.06 sec: 1.01x slower                                                      |
| bench_thread_pool          | 857 us                                                      | 873 us: 1.02x slower                                                        |
| sqlglot_optimize           | 34.5 ms                                                     | 35.3 ms: 1.02x slower                                                       |
| regex_dna                  | 126 ms                                                      | 130 ms: 1.03x slower                                                        |
| sympy_integrate            | 13.0 ms                                                     | 13.3 ms: 1.03x slower                                                       |
| 2to3                       | 218 ms                                                      | 224 ms: 1.03x slower                                                        |
| docutils                   | 1.66 sec                                                    | 1.71 sec: 1.03x slower                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 68.1 ms: 1.04x slower                                                       |
| django_template            | 22.9 ms                                                     | 24.2 ms: 1.05x slower                                                       |
| pickle                     | 7.43 us                                                     | 7.85 us: 1.06x slower                                                       |
| sympy_expand               | 284 ms                                                      | 300 ms: 1.06x slower                                                        |
| unpickle_pure_python       | 133 us                                                      | 141 us: 1.06x slower                                                        |
| crypto_pyaes               | 48.5 ms                                                     | 51.5 ms: 1.06x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 62.6 ms: 1.06x slower                                                       |
| mako                       | 7.09 ms                                                     | 7.57 ms: 1.07x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 209 us: 1.07x slower                                                        |
| fannkuch                   | 247 ms                                                      | 267 ms: 1.08x slower                                                        |
| xml_etree_parse            | 93.0 ms                                                     | 102 ms: 1.10x slower                                                        |
| xml_etree_generate         | 55.8 ms                                                     | 63.6 ms: 1.14x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 110 us: 1.15x slower                                                        |
| xml_etree_process          | 37.7 ms                                                     | 43.7 ms: 1.16x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 16.5 ms: 1.16x slower                                                       |
| unpickle                   | 8.18 us                                                     | 9.53 us: 1.16x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.61 sec: 1.18x slower                                                      |
| json                       | 3.05 ms                                                     | 3.60 ms: 1.18x slower                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.93 ms: 1.19x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 19.8 ms: 1.22x slower                                                       |
| telco                      | 4.13 ms                                                     | 5.12 ms: 1.24x slower                                                       |
| coverage                   | 40.8 ms                                                     | 51.9 ms: 1.27x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 88.8 ms: 1.28x slower                                                       |
| python_startup             | 19.5 ms                                                     | 25.7 ms: 1.32x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 7.81 ms: 1.37x slower                                                       |
| json_loads                 | 13.9 us                                                     | 19.3 us: 1.39x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.33 ms: 1.77x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.89 ms: 1.90x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                                |

Benchmark hidden because not significant (5): sympy_sum, scimark_fft, pprint_safe_repr, pycparser, sqlglot_parse
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (13) of results/bm-20250216-3.14.0a5+-359c7dd-CLANG/bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.046x faster

# HPT report

- Reliability score: 81.49% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown