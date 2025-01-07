# Results vs. 3.12.0

- fork: kumaraditya303
- ref: fast_state
- machine: windows-amd64
- commit hash: 7de6e22
- commit date: 2025-01-07
- overall geometric mean: 1.014x faster
- HPT reliability: 90.36%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1-amd64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 225 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                              |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1-amd64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 393 ms: 1.96x faster                                                      |
| async_tree_io              | 731 ms                                                      | 403 ms: 1.82x faster                                                      |
| async_tree_memoization_tg  | 367 ms                                                      | 209 ms: 1.75x faster                                                      |
| async_tree_none_tg         | 285 ms                                                      | 166 ms: 1.71x faster                                                      |
| async_tree_none            | 291 ms                                                      | 182 ms: 1.60x faster                                                      |
| async_tree_memoization     | 339 ms                                                      | 218 ms: 1.55x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 344 ms: 1.46x faster                                                      |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 347 ms: 1.41x faster                                                      |
| Geometric mean             | (ref)                                                       | 1.65x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1-amd64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 52.6 ms: 1.08x faster                                                     |
| pidigits       | 152 ms                                                      | 146 ms: 1.04x faster                                                      |
| nbody          | 71.9 ms                                                     | 77.8 ms: 1.08x slower                                                     |
| Geometric mean | (ref)                                                       | 1.01x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1-amd64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.42 ms: 1.14x faster                                                     |
| regex_dna      | 126 ms                                                      | 113 ms: 1.11x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 88.0 ms: 1.01x slower                                                     |
| regex_v8       | 14.2 ms                                                     | 20.1 ms: 1.41x slower                                                     |
| Geometric mean | (ref)                                                       | 1.03x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1-amd64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 87.9 ms: 1.06x faster                                                     |
| xml_etree_iterparse  | 65.2 ms                                                     | 62.8 ms: 1.04x faster                                                     |
| xml_etree_generate   | 55.8 ms                                                     | 58.0 ms: 1.04x slower                                                     |
| tomli_loads          | 1.37 sec                                                    | 1.43 sec: 1.05x slower                                                    |
| json_loads           | 13.9 us                                                     | 14.6 us: 1.05x slower                                                     |
| xml_etree_process    | 37.7 ms                                                     | 41.2 ms: 1.09x slower                                                     |
| unpickle_pure_python | 133 us                                                      | 148 us: 1.11x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 225 us: 1.15x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.76 ms: 1.19x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.06x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1-amd64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.0 ms: 1.11x slower                                                     |
| python_startup         | 19.5 ms                                                     | 24.1 ms: 1.24x slower                                                     |
| Geometric mean         | (ref)                                                       | 1.17x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1-amd64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.80 ms: 1.04x faster                                                     |
| django_template | 22.9 ms                                                     | 25.6 ms: 1.11x slower                                                     |
| Geometric mean  | (ref)                                                       | 1.03x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1-amd64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 393 ms: 1.96x faster                                                      |
| async_tree_io              | 731 ms                                                      | 403 ms: 1.82x faster                                                      |
| async_tree_memoization_tg  | 367 ms                                                      | 209 ms: 1.75x faster                                                      |
| async_tree_none_tg         | 285 ms                                                      | 166 ms: 1.71x faster                                                      |
| async_tree_none            | 291 ms                                                      | 182 ms: 1.60x faster                                                      |
| async_tree_memoization     | 339 ms                                                      | 218 ms: 1.55x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 344 ms: 1.46x faster                                                      |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 347 ms: 1.41x faster                                                      |
| deepcopy                   | 238 us                                                      | 187 us: 1.27x faster                                                      |
| comprehensions             | 14.1 us                                                     | 12.3 us: 1.15x faster                                                     |
| regex_effbot               | 1.62 ms                                                     | 1.42 ms: 1.14x faster                                                     |
| deepcopy_memo              | 23.7 us                                                     | 20.9 us: 1.13x faster                                                     |
| regex_dna                  | 126 ms                                                      | 113 ms: 1.11x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.91 us: 1.10x faster                                                     |
| sqlite_synth               | 1.76 us                                                     | 1.61 us: 1.09x faster                                                     |
| float                      | 56.8 ms                                                     | 52.6 ms: 1.08x faster                                                     |
| generators                 | 22.5 ms                                                     | 21.1 ms: 1.07x faster                                                     |
| dulwich_log                | 44.3 ms                                                     | 41.8 ms: 1.06x faster                                                     |
| xml_etree_parse            | 93.0 ms                                                     | 87.9 ms: 1.06x faster                                                     |
| pathlib                    | 80.5 ms                                                     | 76.1 ms: 1.06x faster                                                     |
| coroutines                 | 14.3 ms                                                     | 13.6 ms: 1.05x faster                                                     |
| go                         | 91.6 ms                                                     | 87.2 ms: 1.05x faster                                                     |
| bench_thread_pool          | 857 us                                                      | 820 us: 1.05x faster                                                      |
| mako                       | 7.09 ms                                                     | 6.80 ms: 1.04x faster                                                     |
| pidigits                   | 152 ms                                                      | 146 ms: 1.04x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.8 ms: 1.04x faster                                                     |
| json                       | 3.05 ms                                                     | 2.97 ms: 1.03x faster                                                     |
| raytrace                   | 192 ms                                                      | 188 ms: 1.02x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 90.7 ms: 1.01x faster                                                     |
| spectral_norm              | 66.9 ms                                                     | 66.4 ms: 1.01x faster                                                     |
| regex_compile              | 87.5 ms                                                     | 88.0 ms: 1.01x slower                                                     |
| async_generators           | 239 ms                                                      | 241 ms: 1.01x slower                                                      |
| logging_simple             | 6.28 us                                                     | 6.32 us: 1.01x slower                                                     |
| crypto_pyaes               | 48.5 ms                                                     | 49.1 ms: 1.01x slower                                                     |
| logging_format             | 6.72 us                                                     | 6.84 us: 1.02x slower                                                     |
| sympy_str                  | 175 ms                                                      | 179 ms: 1.02x slower                                                      |
| nqueens                    | 62.8 ms                                                     | 64.4 ms: 1.03x slower                                                     |
| logging_silent             | 60.5 ns                                                     | 62.3 ns: 1.03x slower                                                     |
| 2to3                       | 218 ms                                                      | 225 ms: 1.03x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 60.9 ms: 1.03x slower                                                     |
| xml_etree_generate         | 55.8 ms                                                     | 58.0 ms: 1.04x slower                                                     |
| sympy_integrate            | 13.0 ms                                                     | 13.5 ms: 1.04x slower                                                     |
| meteor_contest             | 74.6 ms                                                     | 77.7 ms: 1.04x slower                                                     |
| deltablue                  | 2.16 ms                                                     | 2.26 ms: 1.04x slower                                                     |
| tomli_loads                | 1.37 sec                                                    | 1.43 sec: 1.05x slower                                                    |
| sqlglot_optimize           | 34.5 ms                                                     | 36.1 ms: 1.05x slower                                                     |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.68 ms: 1.05x slower                                                     |
| json_loads                 | 13.9 us                                                     | 14.6 us: 1.05x slower                                                     |
| sqlglot_normalize          | 187 ms                                                      | 197 ms: 1.05x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 543 ms: 1.06x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.11 sec: 1.06x slower                                                    |
| scimark_fft                | 184 ms                                                      | 196 ms: 1.07x slower                                                      |
| richards                   | 28.4 ms                                                     | 30.5 ms: 1.07x slower                                                     |
| pycparser                  | 699 ms                                                      | 750 ms: 1.07x slower                                                      |
| sympy_expand               | 284 ms                                                      | 306 ms: 1.08x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.11 ms: 1.08x slower                                                     |
| nbody                      | 71.9 ms                                                     | 77.8 ms: 1.08x slower                                                     |
| pyflate                    | 295 ms                                                      | 320 ms: 1.08x slower                                                      |
| richards_super             | 32.1 ms                                                     | 34.8 ms: 1.08x slower                                                     |
| hexiom                     | 4.10 ms                                                     | 4.45 ms: 1.08x slower                                                     |
| xml_etree_process          | 37.7 ms                                                     | 41.2 ms: 1.09x slower                                                     |
| sqlglot_parse              | 804 us                                                      | 887 us: 1.10x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 18.0 ms: 1.11x slower                                                     |
| mdp                        | 1.37 sec                                                    | 1.52 sec: 1.11x slower                                                    |
| unpickle_pure_python       | 133 us                                                      | 148 us: 1.11x slower                                                      |
| django_template            | 22.9 ms                                                     | 25.6 ms: 1.11x slower                                                     |
| scimark_monte_carlo        | 43.7 ms                                                     | 48.8 ms: 1.12x slower                                                     |
| fannkuch                   | 247 ms                                                      | 276 ms: 1.12x slower                                                      |
| coverage                   | 40.8 ms                                                     | 46.7 ms: 1.14x slower                                                     |
| pickle_pure_python         | 195 us                                                      | 225 us: 1.15x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 91.1 ms: 1.16x slower                                                     |
| telco                      | 4.13 ms                                                     | 4.82 ms: 1.17x slower                                                     |
| typing_runtime_protocols   | 95.1 us                                                     | 113 us: 1.18x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 6.76 ms: 1.19x slower                                                     |
| bench_mp_pool              | 69.2 ms                                                     | 82.3 ms: 1.19x slower                                                     |
| python_startup             | 19.5 ms                                                     | 24.1 ms: 1.24x slower                                                     |
| mypy2                      | 509 ms                                                      | 640 ms: 1.26x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.96 ms: 1.29x slower                                                     |
| regex_v8                   | 14.2 ms                                                     | 20.1 ms: 1.41x slower                                                     |
| create_gc_cycles           | 752 us                                                      | 1.21 ms: 1.61x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                              |

Benchmark hidden because not significant (2): docutils, chaos
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250107-3.14.0a3+-7de6e22/bm-20250107-pythonperf1-amd64-kumaraditya303-fast_state-3.14.0a3+-7de6e22.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.014x faster

# HPT report

- Reliability score: 90.36% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown