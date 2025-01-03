# Results vs. 3.12.0

- fork: eendebakpt
- ref: iter_freelists
- machine: windows-amd64
- commit hash: 05f479c
- commit date: 2025-01-02
- overall geometric mean: 1.014x faster
- HPT reliability: 87.96%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-pythonperf1-amd64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 224 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                              |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-pythonperf1-amd64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 398 ms: 1.94x faster                                                      |
| async_tree_io              | 731 ms                                                      | 403 ms: 1.81x faster                                                      |
| async_tree_memoization_tg  | 367 ms                                                      | 209 ms: 1.75x faster                                                      |
| async_tree_none_tg         | 285 ms                                                      | 169 ms: 1.68x faster                                                      |
| async_tree_none            | 291 ms                                                      | 184 ms: 1.58x faster                                                      |
| async_tree_memoization     | 339 ms                                                      | 221 ms: 1.54x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 342 ms: 1.47x faster                                                      |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 347 ms: 1.41x faster                                                      |
| Geometric mean             | (ref)                                                       | 1.64x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-pythonperf1-amd64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 52.7 ms: 1.08x faster                                                     |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                      |
| nbody          | 71.9 ms                                                     | 77.4 ms: 1.08x slower                                                     |
| Geometric mean | (ref)                                                       | 1.01x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-pythonperf1-amd64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.44 ms: 1.12x faster                                                     |
| regex_dna      | 126 ms                                                      | 118 ms: 1.07x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 86.5 ms: 1.01x faster                                                     |
| regex_v8       | 14.2 ms                                                     | 20.8 ms: 1.46x slower                                                     |
| Geometric mean | (ref)                                                       | 1.05x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-pythonperf1-amd64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 88.8 ms: 1.05x faster                                                     |
| xml_etree_iterparse  | 65.2 ms                                                     | 62.6 ms: 1.04x faster                                                     |
| json_loads           | 13.9 us                                                     | 14.0 us: 1.01x slower                                                     |
| xml_etree_generate   | 55.8 ms                                                     | 56.4 ms: 1.01x slower                                                     |
| tomli_loads          | 1.37 sec                                                    | 1.43 sec: 1.05x slower                                                    |
| xml_etree_process    | 37.7 ms                                                     | 40.0 ms: 1.06x slower                                                     |
| pickle_pure_python   | 195 us                                                      | 228 us: 1.16x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 157 us: 1.18x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.73 ms: 1.18x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.06x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-pythonperf1-amd64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.4 ms: 1.07x slower                                                     |
| python_startup         | 19.5 ms                                                     | 23.4 ms: 1.20x slower                                                     |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-pythonperf1-amd64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.94 ms: 1.02x faster                                                     |
| django_template | 22.9 ms                                                     | 24.4 ms: 1.06x slower                                                     |
| Geometric mean  | (ref)                                                       | 1.02x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-pythonperf1-amd64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 398 ms: 1.94x faster                                                      |
| async_tree_io              | 731 ms                                                      | 403 ms: 1.81x faster                                                      |
| async_tree_memoization_tg  | 367 ms                                                      | 209 ms: 1.75x faster                                                      |
| async_tree_none_tg         | 285 ms                                                      | 169 ms: 1.68x faster                                                      |
| async_tree_none            | 291 ms                                                      | 184 ms: 1.58x faster                                                      |
| async_tree_memoization     | 339 ms                                                      | 221 ms: 1.54x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 342 ms: 1.47x faster                                                      |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 347 ms: 1.41x faster                                                      |
| deepcopy                   | 238 us                                                      | 184 us: 1.30x faster                                                      |
| comprehensions             | 14.1 us                                                     | 12.1 us: 1.17x faster                                                     |
| regex_effbot               | 1.62 ms                                                     | 1.44 ms: 1.12x faster                                                     |
| deepcopy_reduce            | 2.09 us                                                     | 1.89 us: 1.11x faster                                                     |
| deepcopy_memo              | 23.7 us                                                     | 21.4 us: 1.11x faster                                                     |
| sqlite_synth               | 1.76 us                                                     | 1.62 us: 1.09x faster                                                     |
| float                      | 56.8 ms                                                     | 52.7 ms: 1.08x faster                                                     |
| regex_dna                  | 126 ms                                                      | 118 ms: 1.07x faster                                                      |
| pathlib                    | 80.5 ms                                                     | 75.4 ms: 1.07x faster                                                     |
| spectral_norm              | 66.9 ms                                                     | 62.8 ms: 1.06x faster                                                     |
| coroutines                 | 14.3 ms                                                     | 13.4 ms: 1.06x faster                                                     |
| bench_thread_pool          | 857 us                                                      | 814 us: 1.05x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 88.8 ms: 1.05x faster                                                     |
| dulwich_log                | 44.3 ms                                                     | 42.3 ms: 1.05x faster                                                     |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.6 ms: 1.04x faster                                                     |
| generators                 | 22.5 ms                                                     | 21.7 ms: 1.04x faster                                                     |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                      |
| go                         | 91.6 ms                                                     | 88.9 ms: 1.03x faster                                                     |
| mako                       | 7.09 ms                                                     | 6.94 ms: 1.02x faster                                                     |
| sympy_sum                  | 91.5 ms                                                     | 89.9 ms: 1.02x faster                                                     |
| regex_compile              | 87.5 ms                                                     | 86.5 ms: 1.01x faster                                                     |
| crypto_pyaes               | 48.5 ms                                                     | 48.8 ms: 1.01x slower                                                     |
| json_loads                 | 13.9 us                                                     | 14.0 us: 1.01x slower                                                     |
| sympy_str                  | 175 ms                                                      | 177 ms: 1.01x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 56.4 ms: 1.01x slower                                                     |
| sqlglot_normalize          | 187 ms                                                      | 190 ms: 1.01x slower                                                      |
| logging_format             | 6.72 us                                                     | 6.83 us: 1.02x slower                                                     |
| sympy_integrate            | 13.0 ms                                                     | 13.2 ms: 1.02x slower                                                     |
| logging_simple             | 6.28 us                                                     | 6.43 us: 1.03x slower                                                     |
| deltablue                  | 2.16 ms                                                     | 2.22 ms: 1.03x slower                                                     |
| 2to3                       | 218 ms                                                      | 224 ms: 1.03x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 77.1 ms: 1.03x slower                                                     |
| scimark_fft                | 184 ms                                                      | 191 ms: 1.04x slower                                                      |
| json                       | 3.05 ms                                                     | 3.18 ms: 1.04x slower                                                     |
| tomli_loads                | 1.37 sec                                                    | 1.43 sec: 1.05x slower                                                    |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.68 ms: 1.05x slower                                                     |
| raytrace                   | 192 ms                                                      | 202 ms: 1.05x slower                                                      |
| pycparser                  | 699 ms                                                      | 738 ms: 1.06x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 40.0 ms: 1.06x slower                                                     |
| sympy_expand               | 284 ms                                                      | 301 ms: 1.06x slower                                                      |
| django_template            | 22.9 ms                                                     | 24.4 ms: 1.06x slower                                                     |
| mdp                        | 1.37 sec                                                    | 1.46 sec: 1.07x slower                                                    |
| python_startup_no_site     | 16.2 ms                                                     | 17.4 ms: 1.07x slower                                                     |
| pprint_safe_repr           | 513 ms                                                      | 550 ms: 1.07x slower                                                      |
| nbody                      | 71.9 ms                                                     | 77.4 ms: 1.08x slower                                                     |
| sqlglot_transpile          | 1.02 ms                                                     | 1.10 ms: 1.08x slower                                                     |
| pyflate                    | 295 ms                                                      | 318 ms: 1.08x slower                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 47.3 ms: 1.08x slower                                                     |
| pprint_pformat             | 1.05 sec                                                    | 1.14 sec: 1.09x slower                                                    |
| logging_silent             | 60.5 ns                                                     | 66.4 ns: 1.10x slower                                                     |
| scimark_lu                 | 58.9 ms                                                     | 65.0 ms: 1.10x slower                                                     |
| hexiom                     | 4.10 ms                                                     | 4.53 ms: 1.10x slower                                                     |
| telco                      | 4.13 ms                                                     | 4.58 ms: 1.11x slower                                                     |
| sqlglot_parse              | 804 us                                                      | 896 us: 1.11x slower                                                      |
| richards_super             | 32.1 ms                                                     | 35.8 ms: 1.11x slower                                                     |
| richards                   | 28.4 ms                                                     | 31.8 ms: 1.12x slower                                                     |
| coverage                   | 40.8 ms                                                     | 46.3 ms: 1.13x slower                                                     |
| fannkuch                   | 247 ms                                                      | 281 ms: 1.14x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 109 us: 1.15x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 90.7 ms: 1.15x slower                                                     |
| pickle_pure_python         | 195 us                                                      | 228 us: 1.16x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 157 us: 1.18x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 6.73 ms: 1.18x slower                                                     |
| bench_mp_pool              | 69.2 ms                                                     | 82.1 ms: 1.19x slower                                                     |
| python_startup             | 19.5 ms                                                     | 23.4 ms: 1.20x slower                                                     |
| mypy2                      | 509 ms                                                      | 634 ms: 1.24x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.96 ms: 1.29x slower                                                     |
| regex_v8                   | 14.2 ms                                                     | 20.8 ms: 1.46x slower                                                     |
| create_gc_cycles           | 752 us                                                      | 1.21 ms: 1.61x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                              |

Benchmark hidden because not significant (5): docutils, chaos, nqueens, sqlglot_optimize, async_generators
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250102-3.14.0a3+-05f479c/bm-20250102-pythonperf1-amd64-eendebakpt-iter_freelists-3.14.0a3+-05f479c.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.014x faster

# HPT report

- Reliability score: 87.96% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown