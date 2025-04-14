# Results vs. 3.12.0

- fork: python
- ref: c9932a9ec8a3077933a8
- machine: windows-amd64
- commit hash: c9932a9
- commit date: 2025-03-01
- overall geometric mean: 1.012x faster
- HPT reliability: 80.53%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 232 ms: 1.07x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.75 sec: 1.06x slower                                                      |
| Geometric mean | (ref)                                                       | 1.06x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 397 ms: 1.94x faster                                                        |
| async_tree_io              | 731 ms                                                      | 406 ms: 1.80x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 208 ms: 1.77x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 172 ms: 1.66x faster                                                        |
| async_tree_none            | 291 ms                                                      | 178 ms: 1.64x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 209 ms: 1.62x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 366 ms: 1.37x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 361 ms: 1.35x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.63x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 46.3 ms: 1.23x faster                                                       |
| nbody          | 71.9 ms                                                     | 67.7 ms: 1.06x faster                                                       |
| pidigits       | 152 ms                                                      | 155 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 86.9 ms: 1.01x faster                                                       |
| regex_dna      | 126 ms                                                      | 129 ms: 1.02x slower                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.87 ms: 1.16x slower                                                       |
| regex_v8       | 14.2 ms                                                     | 17.1 ms: 1.20x slower                                                       |
| Geometric mean | (ref)                                                       | 1.09x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_dict          | 18.4 us                                                     | 17.1 us: 1.08x faster                                                       |
| unpickle_list        | 2.75 us                                                     | 2.60 us: 1.06x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.35 sec: 1.02x faster                                                      |
| pickle               | 7.43 us                                                     | 7.56 us: 1.02x slower                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 70.0 ms: 1.07x slower                                                       |
| pickle_list          | 2.83 us                                                     | 3.14 us: 1.11x slower                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 104 ms: 1.12x slower                                                        |
| pickle_pure_python   | 195 us                                                      | 220 us: 1.12x slower                                                        |
| unpickle_pure_python | 133 us                                                      | 151 us: 1.13x slower                                                        |
| xml_etree_generate   | 55.8 ms                                                     | 65.8 ms: 1.18x slower                                                       |
| unpickle             | 8.18 us                                                     | 9.72 us: 1.19x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 46.1 ms: 1.22x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 7.88 ms: 1.38x slower                                                       |
| json_loads           | 13.9 us                                                     | 20.5 us: 1.47x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.13x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.4 ms: 1.26x slower                                                       |
| python_startup         | 19.5 ms                                                     | 27.4 ms: 1.41x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.33x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 25.1 ms: 1.09x slower                                                       |
| mako            | 7.09 ms                                                     | 8.33 ms: 1.18x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.13x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 31.6 ms: 2.55x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 397 ms: 1.94x faster                                                        |
| async_tree_io              | 731 ms                                                      | 406 ms: 1.80x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 208 ms: 1.77x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 172 ms: 1.66x faster                                                        |
| async_tree_none            | 291 ms                                                      | 178 ms: 1.64x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 209 ms: 1.62x faster                                                        |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.44 sec: 1.45x faster                                                      |
| unpack_sequence            | 37.5 ns                                                     | 26.2 ns: 1.43x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 366 ms: 1.37x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 361 ms: 1.35x faster                                                        |
| deepcopy                   | 238 us                                                      | 182 us: 1.31x faster                                                        |
| generators                 | 22.5 ms                                                     | 17.3 ms: 1.30x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 19.3 us: 1.23x faster                                                       |
| float                      | 56.8 ms                                                     | 46.3 ms: 1.23x faster                                                       |
| go                         | 91.6 ms                                                     | 77.2 ms: 1.19x faster                                                       |
| comprehensions             | 14.1 us                                                     | 12.1 us: 1.17x faster                                                       |
| raytrace                   | 192 ms                                                      | 176 ms: 1.09x faster                                                        |
| deltablue                  | 2.16 ms                                                     | 1.98 ms: 1.09x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.61 us: 1.09x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.1 ms: 1.09x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.93 us: 1.09x faster                                                       |
| pickle_dict                | 18.4 us                                                     | 17.1 us: 1.08x faster                                                       |
| async_generators           | 239 ms                                                      | 225 ms: 1.07x faster                                                        |
| nbody                      | 71.9 ms                                                     | 67.7 ms: 1.06x faster                                                       |
| unpickle_list              | 2.75 us                                                     | 2.60 us: 1.06x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 74.6 ms: 1.06x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 63.4 ms: 1.06x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 42.2 ms: 1.05x faster                                                       |
| chaos                      | 43.3 ms                                                     | 41.3 ms: 1.05x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 42.6 ms: 1.03x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.35 sec: 1.02x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 74.1 ms: 1.01x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 86.9 ms: 1.01x faster                                                       |
| logging_simple             | 6.28 us                                                     | 6.34 us: 1.01x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.15 ms: 1.01x slower                                                       |
| sympy_str                  | 175 ms                                                      | 178 ms: 1.01x slower                                                        |
| pidigits                   | 152 ms                                                      | 155 ms: 1.02x slower                                                        |
| regex_dna                  | 126 ms                                                      | 129 ms: 1.02x slower                                                        |
| pickle                     | 7.43 us                                                     | 7.56 us: 1.02x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 64.0 ms: 1.02x slower                                                       |
| pyflate                    | 295 ms                                                      | 302 ms: 1.02x slower                                                        |
| pycparser                  | 699 ms                                                      | 716 ms: 1.03x slower                                                        |
| sqlglot_transpile          | 1.02 ms                                                     | 1.05 ms: 1.03x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.08 sec: 1.03x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 531 ms: 1.03x slower                                                        |
| sqlglot_parse              | 804 us                                                      | 833 us: 1.04x slower                                                        |
| richards                   | 28.4 ms                                                     | 29.4 ms: 1.04x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.4 ms: 1.04x slower                                                       |
| bench_thread_pool          | 857 us                                                      | 889 us: 1.04x slower                                                        |
| sqlglot_normalize          | 187 ms                                                      | 194 ms: 1.04x slower                                                        |
| richards_super             | 32.1 ms                                                     | 33.6 ms: 1.05x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.75 sec: 1.06x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 63.9 ns: 1.06x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 36.5 ms: 1.06x slower                                                       |
| 2to3                       | 218 ms                                                      | 232 ms: 1.07x slower                                                        |
| scimark_fft                | 184 ms                                                      | 197 ms: 1.07x slower                                                        |
| sympy_expand               | 284 ms                                                      | 304 ms: 1.07x slower                                                        |
| xml_etree_iterparse        | 65.2 ms                                                     | 70.0 ms: 1.07x slower                                                       |
| asyncio_tcp                | 487 ms                                                      | 525 ms: 1.08x slower                                                        |
| crypto_pyaes               | 48.5 ms                                                     | 52.3 ms: 1.08x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.76 ms: 1.08x slower                                                       |
| django_template            | 22.9 ms                                                     | 25.1 ms: 1.09x slower                                                       |
| pickle_list                | 2.83 us                                                     | 3.14 us: 1.11x slower                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 104 ms: 1.12x slower                                                        |
| pickle_pure_python         | 195 us                                                      | 220 us: 1.12x slower                                                        |
| unpickle_pure_python       | 133 us                                                      | 151 us: 1.13x slower                                                        |
| scimark_lu                 | 58.9 ms                                                     | 67.7 ms: 1.15x slower                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.87 ms: 1.16x slower                                                       |
| fannkuch                   | 247 ms                                                      | 287 ms: 1.17x slower                                                        |
| mako                       | 7.09 ms                                                     | 8.33 ms: 1.18x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 112 us: 1.18x slower                                                        |
| xml_etree_generate         | 55.8 ms                                                     | 65.8 ms: 1.18x slower                                                       |
| unpickle                   | 8.18 us                                                     | 9.72 us: 1.19x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 17.1 ms: 1.20x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.66 sec: 1.21x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 46.1 ms: 1.22x slower                                                       |
| json                       | 3.05 ms                                                     | 3.73 ms: 1.22x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 20.4 ms: 1.26x slower                                                       |
| telco                      | 4.13 ms                                                     | 5.23 ms: 1.27x slower                                                       |
| coverage                   | 40.8 ms                                                     | 53.9 ms: 1.32x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 91.5 ms: 1.32x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 7.88 ms: 1.38x slower                                                       |
| python_startup             | 19.5 ms                                                     | 27.4 ms: 1.41x slower                                                       |
| json_loads                 | 13.9 us                                                     | 20.5 us: 1.47x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.65 ms: 1.74x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.33 ms: 1.77x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (2): sympy_sum, logging_format
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (13) of results/bm-20250301-3.14.0a5+-c9932a9-CLANG/bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.012x faster

# HPT report

- Reliability score: 80.53% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown