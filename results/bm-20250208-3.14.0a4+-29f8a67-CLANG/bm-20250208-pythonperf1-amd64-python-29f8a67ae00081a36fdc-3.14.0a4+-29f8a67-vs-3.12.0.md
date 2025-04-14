# Results vs. 3.12.0

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: windows-amd64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.021x faster
- HPT reliability: 53.94%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 232 ms: 1.07x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.74 sec: 1.05x slower                                                      |
| Geometric mean | (ref)                                                       | 1.06x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 397 ms: 1.94x faster                                                        |
| async_tree_io              | 731 ms                                                      | 400 ms: 1.83x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 208 ms: 1.77x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 171 ms: 1.67x faster                                                        |
| async_tree_none            | 291 ms                                                      | 179 ms: 1.62x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 213 ms: 1.59x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 365 ms: 1.38x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 358 ms: 1.37x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.63x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 44.2 ms: 1.28x faster                                                       |
| nbody          | 71.9 ms                                                     | 60.5 ms: 1.19x faster                                                       |
| pidigits       | 152 ms                                                      | 155 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 83.6 ms: 1.05x faster                                                       |
| regex_dna      | 126 ms                                                      | 130 ms: 1.03x slower                                                        |
| regex_v8       | 14.2 ms                                                     | 16.7 ms: 1.17x slower                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.94 ms: 1.20x slower                                                       |
| Geometric mean | (ref)                                                       | 1.08x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.32 sec: 1.03x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 69.4 ms: 1.07x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 211 us: 1.08x slower                                                        |
| unpickle_pure_python | 133 us                                                      | 146 us: 1.09x slower                                                        |
| xml_etree_parse      | 93.0 ms                                                     | 102 ms: 1.09x slower                                                        |
| xml_etree_generate   | 55.8 ms                                                     | 64.3 ms: 1.15x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 44.8 ms: 1.19x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 7.62 ms: 1.34x slower                                                       |
| json_loads           | 13.9 us                                                     | 19.3 us: 1.39x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.14x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.4 ms: 1.25x slower                                                       |
| python_startup         | 19.5 ms                                                     | 27.4 ms: 1.41x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.33x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 24.2 ms: 1.06x slower                                                       |
| mako            | 7.09 ms                                                     | 7.56 ms: 1.07x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.06x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 397 ms: 1.94x faster                                                        |
| async_tree_io              | 731 ms                                                      | 400 ms: 1.83x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 208 ms: 1.77x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 171 ms: 1.67x faster                                                        |
| async_tree_none            | 291 ms                                                      | 179 ms: 1.62x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 213 ms: 1.59x faster                                                        |
| deepcopy                   | 238 us                                                      | 172 us: 1.38x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 365 ms: 1.38x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 358 ms: 1.37x faster                                                        |
| generators                 | 22.5 ms                                                     | 17.0 ms: 1.32x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 62.1 ms: 1.30x faster                                                       |
| float                      | 56.8 ms                                                     | 44.2 ms: 1.28x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 18.9 us: 1.25x faster                                                       |
| go                         | 91.6 ms                                                     | 73.8 ms: 1.24x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.5 us: 1.23x faster                                                       |
| nbody                      | 71.9 ms                                                     | 60.5 ms: 1.19x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 59.7 ms: 1.12x faster                                                       |
| deltablue                  | 2.16 ms                                                     | 1.93 ms: 1.12x faster                                                       |
| raytrace                   | 192 ms                                                      | 173 ms: 1.11x faster                                                        |
| deepcopy_reduce            | 2.09 us                                                     | 1.89 us: 1.11x faster                                                       |
| chaos                      | 43.3 ms                                                     | 39.4 ms: 1.10x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.62 us: 1.09x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.5 ms: 1.08x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 74.0 ms: 1.06x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 42.0 ms: 1.06x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.6 ms: 1.05x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 83.6 ms: 1.05x faster                                                       |
| async_generators           | 239 ms                                                      | 229 ms: 1.04x faster                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.32 sec: 1.03x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 72.5 ms: 1.03x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 62.1 ms: 1.01x faster                                                       |
| logging_simple             | 6.28 us                                                     | 6.22 us: 1.01x faster                                                       |
| hexiom                     | 4.10 ms                                                     | 4.07 ms: 1.01x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.67 us: 1.01x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.05 sec: 1.01x slower                                                      |
| sqlglot_normalize          | 187 ms                                                      | 188 ms: 1.01x slower                                                        |
| pprint_safe_repr           | 513 ms                                                      | 517 ms: 1.01x slower                                                        |
| richards                   | 28.4 ms                                                     | 28.8 ms: 1.02x slower                                                       |
| sympy_str                  | 175 ms                                                      | 178 ms: 1.02x slower                                                        |
| sqlglot_transpile          | 1.02 ms                                                     | 1.04 ms: 1.02x slower                                                       |
| pycparser                  | 699 ms                                                      | 711 ms: 1.02x slower                                                        |
| pidigits                   | 152 ms                                                      | 155 ms: 1.02x slower                                                        |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.60 ms: 1.02x slower                                                       |
| bench_thread_pool          | 857 us                                                      | 874 us: 1.02x slower                                                        |
| scimark_fft                | 184 ms                                                      | 189 ms: 1.02x slower                                                        |
| sqlglot_optimize           | 34.5 ms                                                     | 35.4 ms: 1.03x slower                                                       |
| regex_dna                  | 126 ms                                                      | 130 ms: 1.03x slower                                                        |
| richards_super             | 32.1 ms                                                     | 33.0 ms: 1.03x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.3 ms: 1.03x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 831 us: 1.03x slower                                                        |
| logging_silent             | 60.5 ns                                                     | 62.9 ns: 1.04x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.74 sec: 1.05x slower                                                      |
| django_template            | 22.9 ms                                                     | 24.2 ms: 1.06x slower                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 51.6 ms: 1.06x slower                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 69.4 ms: 1.07x slower                                                       |
| sympy_expand               | 284 ms                                                      | 302 ms: 1.07x slower                                                        |
| 2to3                       | 218 ms                                                      | 232 ms: 1.07x slower                                                        |
| mako                       | 7.09 ms                                                     | 7.56 ms: 1.07x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 211 us: 1.08x slower                                                        |
| unpickle_pure_python       | 133 us                                                      | 146 us: 1.09x slower                                                        |
| xml_etree_parse            | 93.0 ms                                                     | 102 ms: 1.09x slower                                                        |
| fannkuch                   | 247 ms                                                      | 273 ms: 1.11x slower                                                        |
| typing_runtime_protocols   | 95.1 us                                                     | 109 us: 1.15x slower                                                        |
| scimark_lu                 | 58.9 ms                                                     | 67.7 ms: 1.15x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 64.3 ms: 1.15x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 16.7 ms: 1.17x slower                                                       |
| json                       | 3.05 ms                                                     | 3.58 ms: 1.17x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 44.8 ms: 1.19x slower                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.94 ms: 1.20x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.72 sec: 1.25x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 20.4 ms: 1.25x slower                                                       |
| telco                      | 4.13 ms                                                     | 5.22 ms: 1.26x slower                                                       |
| coverage                   | 40.8 ms                                                     | 54.1 ms: 1.33x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 7.62 ms: 1.34x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 95.8 ms: 1.38x slower                                                       |
| json_loads                 | 13.9 us                                                     | 19.3 us: 1.39x slower                                                       |
| python_startup             | 19.5 ms                                                     | 27.4 ms: 1.41x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.36 ms: 1.80x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.82 ms: 1.85x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (2): pyflate, sympy_sum
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250208-3.14.0a4+-29f8a67-CLANG/bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.021x faster

# HPT report

- Reliability score: 53.94% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown