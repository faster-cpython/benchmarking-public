# Results vs. 3.12.0

- fork: python
- ref: c9932a9ec8a3077933a8
- machine: windows-amd64
- commit hash: c9932a9
- commit date: 2025-03-01
- overall geometric mean: 1.044x faster
- HPT reliability: 62.45%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 223 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 403 ms: 1.91x faster                                                        |
| async_tree_io              | 731 ms                                                      | 416 ms: 1.76x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 212 ms: 1.73x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 177 ms: 1.61x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 217 ms: 1.57x faster                                                        |
| async_tree_none            | 291 ms                                                      | 187 ms: 1.56x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 344 ms: 1.46x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 340 ms: 1.44x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.62x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 44.9 ms: 1.27x faster                                                       |
| nbody          | 71.9 ms                                                     | 68.9 ms: 1.04x faster                                                       |
| pidigits       | 152 ms                                                      | 150 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 115 ms: 1.10x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.47 ms: 1.10x faster                                                       |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 90.2 ms: 1.03x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.8 ms: 1.02x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 56.2 ms: 1.01x slower                                                       |
| unpickle_list        | 2.75 us                                                     | 2.79 us: 1.02x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.47 us: 1.04x slower                                                       |
| pickle               | 7.43 us                                                     | 7.76 us: 1.04x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.43 sec: 1.05x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 40.1 ms: 1.06x slower                                                       |
| json_loads           | 13.9 us                                                     | 14.8 us: 1.07x slower                                                       |
| pickle_dict          | 18.4 us                                                     | 20.4 us: 1.11x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 148 us: 1.11x slower                                                        |
| pickle_pure_python   | 195 us                                                      | 229 us: 1.17x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 6.85 ms: 1.20x slower                                                       |
| pickle_list          | 2.83 us                                                     | 3.50 us: 1.24x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.2 ms: 1.18x slower                                                       |
| python_startup         | 19.5 ms                                                     | 25.0 ms: 1.29x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.23x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.95 ms: 1.02x faster                                                       |
| django_template | 22.9 ms                                                     | 24.8 ms: 1.08x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 34.6 ms: 2.33x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 403 ms: 1.91x faster                                                        |
| async_tree_io              | 731 ms                                                      | 416 ms: 1.76x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 212 ms: 1.73x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 177 ms: 1.61x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 217 ms: 1.57x faster                                                        |
| async_tree_none            | 291 ms                                                      | 187 ms: 1.56x faster                                                        |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.36 sec: 1.54x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 344 ms: 1.46x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 340 ms: 1.44x faster                                                        |
| deepcopy                   | 238 us                                                      | 186 us: 1.28x faster                                                        |
| float                      | 56.8 ms                                                     | 44.9 ms: 1.27x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.2 us: 1.26x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 20.3 us: 1.17x faster                                                       |
| generators                 | 22.5 ms                                                     | 19.5 ms: 1.15x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.55 us: 1.13x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 59.1 ms: 1.13x faster                                                       |
| regex_dna                  | 126 ms                                                      | 115 ms: 1.10x faster                                                        |
| regex_effbot               | 1.62 ms                                                     | 1.47 ms: 1.10x faster                                                       |
| async_generators           | 239 ms                                                      | 220 ms: 1.09x faster                                                        |
| coroutines                 | 14.3 ms                                                     | 13.2 ms: 1.08x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.95 us: 1.07x faster                                                       |
| go                         | 91.6 ms                                                     | 86.1 ms: 1.06x faster                                                       |
| asyncio_tcp                | 487 ms                                                      | 462 ms: 1.06x faster                                                        |
| dulwich_log                | 44.3 ms                                                     | 42.2 ms: 1.05x faster                                                       |
| nbody                      | 71.9 ms                                                     | 68.9 ms: 1.04x faster                                                       |
| chaos                      | 43.3 ms                                                     | 41.8 ms: 1.04x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 90.2 ms: 1.03x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 89.0 ms: 1.03x faster                                                       |
| json                       | 3.05 ms                                                     | 2.97 ms: 1.03x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.8 ms: 1.02x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.95 ms: 1.02x faster                                                       |
| pidigits                   | 152 ms                                                      | 150 ms: 1.02x faster                                                        |
| scimark_fft                | 184 ms                                                      | 182 ms: 1.01x faster                                                        |
| sympy_str                  | 175 ms                                                      | 174 ms: 1.01x faster                                                        |
| logging_silent             | 60.5 ns                                                     | 60.8 ns: 1.01x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 56.2 ms: 1.01x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 63.4 ms: 1.01x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 75.5 ms: 1.01x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 34.9 ms: 1.01x slower                                                       |
| unpickle_list              | 2.75 us                                                     | 2.79 us: 1.02x slower                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 49.5 ms: 1.02x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 44.7 ms: 1.02x slower                                                       |
| 2to3                       | 218 ms                                                      | 223 ms: 1.02x slower                                                        |
| logging_format             | 6.72 us                                                     | 6.89 us: 1.03x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.62 ms: 1.03x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.3 ms: 1.03x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 192 ms: 1.03x slower                                                        |
| logging_simple             | 6.28 us                                                     | 6.45 us: 1.03x slower                                                       |
| pyflate                    | 295 ms                                                      | 304 ms: 1.03x slower                                                        |
| unpickle                   | 8.18 us                                                     | 8.47 us: 1.04x slower                                                       |
| sympy_expand               | 284 ms                                                      | 295 ms: 1.04x slower                                                        |
| pickle                     | 7.43 us                                                     | 7.76 us: 1.04x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.07 ms: 1.05x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.43 sec: 1.05x slower                                                      |
| richards                   | 28.4 ms                                                     | 29.9 ms: 1.05x slower                                                       |
| pycparser                  | 699 ms                                                      | 741 ms: 1.06x slower                                                        |
| hexiom                     | 4.10 ms                                                     | 4.35 ms: 1.06x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 40.1 ms: 1.06x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.11 sec: 1.06x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.8 us: 1.07x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 549 ms: 1.07x slower                                                        |
| richards_super             | 32.1 ms                                                     | 34.4 ms: 1.07x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 862 us: 1.07x slower                                                        |
| scimark_sor                | 78.8 ms                                                     | 84.5 ms: 1.07x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 63.2 ms: 1.07x slower                                                       |
| django_template            | 22.9 ms                                                     | 24.8 ms: 1.08x slower                                                       |
| pickle_dict                | 18.4 us                                                     | 20.4 us: 1.11x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 105 us: 1.11x slower                                                        |
| unpickle_pure_python       | 133 us                                                      | 148 us: 1.11x slower                                                        |
| fannkuch                   | 247 ms                                                      | 277 ms: 1.12x slower                                                        |
| unpack_sequence            | 37.5 ns                                                     | 43.4 ns: 1.16x slower                                                       |
| coverage                   | 40.8 ms                                                     | 47.3 ms: 1.16x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.78 ms: 1.16x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.60 sec: 1.17x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 229 us: 1.17x slower                                                        |
| python_startup_no_site     | 16.2 ms                                                     | 19.2 ms: 1.18x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.85 ms: 1.20x slower                                                       |
| pickle_list                | 2.83 us                                                     | 3.50 us: 1.24x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 86.2 ms: 1.25x slower                                                       |
| python_startup             | 19.5 ms                                                     | 25.0 ms: 1.29x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.02 ms: 1.33x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.21 ms: 1.61x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (6): bench_thread_pool, raytrace, docutils, deltablue, regex_compile, regex_v8
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (13) of results/bm-20250301-3.14.0a5+-c9932a9/bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.044x faster

# HPT report

- Reliability score: 62.45% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown