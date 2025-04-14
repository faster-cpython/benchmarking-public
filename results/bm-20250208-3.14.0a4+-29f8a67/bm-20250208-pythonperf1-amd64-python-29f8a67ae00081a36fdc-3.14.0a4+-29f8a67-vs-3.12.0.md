# Results vs. 3.12.0

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: windows-amd64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.041x faster
- HPT reliability: 83.71%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 227 ms: 1.04x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.65 sec: 1.01x faster                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 428 ms: 1.80x faster                                                        |
| async_tree_io              | 731 ms                                                      | 416 ms: 1.76x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 218 ms: 1.68x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 179 ms: 1.59x faster                                                        |
| async_tree_none            | 291 ms                                                      | 190 ms: 1.54x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 224 ms: 1.51x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 345 ms: 1.45x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 339 ms: 1.44x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.59x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 45.1 ms: 1.26x faster                                                       |
| nbody          | 71.9 ms                                                     | 69.1 ms: 1.04x faster                                                       |
| pidigits       | 152 ms                                                      | 151 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.40 ms: 1.15x faster                                                       |
| regex_dna      | 126 ms                                                      | 112 ms: 1.13x faster                                                        |
| regex_compile  | 87.5 ms                                                     | 84.1 ms: 1.04x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 14.3 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 62.9 ms: 1.04x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 90.4 ms: 1.03x faster                                                       |
| pickle_dict          | 18.4 us                                                     | 17.9 us: 1.03x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.35 sec: 1.01x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 56.5 ms: 1.01x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.40 us: 1.03x slower                                                       |
| unpickle_list        | 2.75 us                                                     | 2.84 us: 1.03x slower                                                       |
| pickle_list          | 2.83 us                                                     | 2.96 us: 1.05x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 39.6 ms: 1.05x slower                                                       |
| pickle               | 7.43 us                                                     | 7.87 us: 1.06x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 142 us: 1.07x slower                                                        |
| json_loads           | 13.9 us                                                     | 15.2 us: 1.09x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 217 us: 1.11x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 6.67 ms: 1.17x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.04x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.6 ms: 1.21x slower                                                       |
| python_startup         | 19.5 ms                                                     | 26.2 ms: 1.34x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.27x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.69 ms: 1.06x faster                                                       |
| django_template | 22.9 ms                                                     | 25.9 ms: 1.13x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 428 ms: 1.80x faster                                                        |
| async_tree_io              | 731 ms                                                      | 416 ms: 1.76x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 218 ms: 1.68x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 179 ms: 1.59x faster                                                        |
| async_tree_none            | 291 ms                                                      | 190 ms: 1.54x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 224 ms: 1.51x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 345 ms: 1.45x faster                                                        |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.44 sec: 1.45x faster                                                      |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 339 ms: 1.44x faster                                                        |
| deepcopy                   | 238 us                                                      | 183 us: 1.30x faster                                                        |
| pathlib                    | 80.5 ms                                                     | 62.4 ms: 1.29x faster                                                       |
| float                      | 56.8 ms                                                     | 45.1 ms: 1.26x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 19.4 us: 1.22x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.6 us: 1.22x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.40 ms: 1.15x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 58.2 ms: 1.15x faster                                                       |
| generators                 | 22.5 ms                                                     | 19.8 ms: 1.14x faster                                                       |
| regex_dna                  | 126 ms                                                      | 112 ms: 1.13x faster                                                        |
| deepcopy_reduce            | 2.09 us                                                     | 1.90 us: 1.10x faster                                                       |
| async_generators           | 239 ms                                                      | 222 ms: 1.08x faster                                                        |
| coroutines                 | 14.3 ms                                                     | 13.3 ms: 1.07x faster                                                       |
| go                         | 91.6 ms                                                     | 85.4 ms: 1.07x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.69 ms: 1.06x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 57.2 ns: 1.06x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.67 us: 1.05x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 42.2 ms: 1.05x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 84.1 ms: 1.04x faster                                                       |
| nbody                      | 71.9 ms                                                     | 69.1 ms: 1.04x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.9 ms: 1.04x faster                                                       |
| chaos                      | 43.3 ms                                                     | 41.9 ms: 1.03x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 46.9 ms: 1.03x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 90.4 ms: 1.03x faster                                                       |
| pickle_dict                | 18.4 us                                                     | 17.9 us: 1.03x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 89.4 ms: 1.02x faster                                                       |
| unpack_sequence            | 37.5 ns                                                     | 36.9 ns: 1.02x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.35 sec: 1.01x faster                                                      |
| pidigits                   | 152 ms                                                      | 151 ms: 1.01x faster                                                        |
| docutils                   | 1.66 sec                                                    | 1.65 sec: 1.01x faster                                                      |
| sympy_str                  | 175 ms                                                      | 174 ms: 1.01x faster                                                        |
| scimark_fft                | 184 ms                                                      | 183 ms: 1.01x faster                                                        |
| regex_v8                   | 14.2 ms                                                     | 14.3 ms: 1.01x slower                                                       |
| logging_simple             | 6.28 us                                                     | 6.32 us: 1.01x slower                                                       |
| logging_format             | 6.72 us                                                     | 6.77 us: 1.01x slower                                                       |
| richards                   | 28.4 ms                                                     | 28.7 ms: 1.01x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 44.3 ms: 1.01x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 56.5 ms: 1.01x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 189 ms: 1.01x slower                                                        |
| pprint_pformat             | 1.05 sec                                                    | 1.06 sec: 1.01x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 13.1 ms: 1.02x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 76.0 ms: 1.02x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 35.2 ms: 1.02x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.62 ms: 1.02x slower                                                       |
| richards_super             | 32.1 ms                                                     | 32.9 ms: 1.02x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 527 ms: 1.03x slower                                                        |
| unpickle                   | 8.18 us                                                     | 8.40 us: 1.03x slower                                                       |
| pyflate                    | 295 ms                                                      | 303 ms: 1.03x slower                                                        |
| raytrace                   | 192 ms                                                      | 198 ms: 1.03x slower                                                        |
| scimark_lu                 | 58.9 ms                                                     | 60.7 ms: 1.03x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.23 ms: 1.03x slower                                                       |
| unpickle_list              | 2.75 us                                                     | 2.84 us: 1.03x slower                                                       |
| pycparser                  | 699 ms                                                      | 725 ms: 1.04x slower                                                        |
| 2to3                       | 218 ms                                                      | 227 ms: 1.04x slower                                                        |
| pickle_list                | 2.83 us                                                     | 2.96 us: 1.05x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 39.6 ms: 1.05x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.07 ms: 1.05x slower                                                       |
| sympy_expand               | 284 ms                                                      | 299 ms: 1.05x slower                                                        |
| pickle                     | 7.43 us                                                     | 7.87 us: 1.06x slower                                                       |
| fannkuch                   | 247 ms                                                      | 262 ms: 1.06x slower                                                        |
| unpickle_pure_python       | 133 us                                                      | 142 us: 1.07x slower                                                        |
| mdp                        | 1.37 sec                                                    | 1.46 sec: 1.07x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 85.4 ms: 1.08x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 875 us: 1.09x slower                                                        |
| json_loads                 | 13.9 us                                                     | 15.2 us: 1.09x slower                                                       |
| asyncio_tcp                | 487 ms                                                      | 539 ms: 1.11x slower                                                        |
| pickle_pure_python         | 195 us                                                      | 217 us: 1.11x slower                                                        |
| typing_runtime_protocols   | 95.1 us                                                     | 106 us: 1.11x slower                                                        |
| django_template            | 22.9 ms                                                     | 25.9 ms: 1.13x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.79 ms: 1.16x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.67 ms: 1.17x slower                                                       |
| coverage                   | 40.8 ms                                                     | 48.5 ms: 1.19x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 19.6 ms: 1.21x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 90.8 ms: 1.31x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.04 ms: 1.34x slower                                                       |
| python_startup             | 19.5 ms                                                     | 26.2 ms: 1.34x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.22 ms: 1.62x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (4): json, nqueens, deltablue, bench_thread_pool
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (13) of results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.041x faster

# HPT report

- Reliability score: 83.71% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown