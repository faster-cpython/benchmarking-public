# Results vs. 3.12.0

- fork: brandtbucher
- ref: nojit
- machine: windows-amd64
- commit hash: f098037
- commit date: 2025-01-07
- overall geometric mean: 1.026x faster
- HPT reliability: 55.64%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 222 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                       | 1.01x slower                                                       |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 402 ms: 1.92x faster                                               |
| async_tree_io              | 731 ms                                                      | 409 ms: 1.79x faster                                               |
| async_tree_memoization_tg  | 367 ms                                                      | 210 ms: 1.75x faster                                               |
| async_tree_none_tg         | 285 ms                                                      | 170 ms: 1.68x faster                                               |
| async_tree_none            | 291 ms                                                      | 185 ms: 1.58x faster                                               |
| async_tree_memoization     | 339 ms                                                      | 226 ms: 1.50x faster                                               |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 347 ms: 1.45x faster                                               |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 349 ms: 1.40x faster                                               |
| Geometric mean             | (ref)                                                       | 1.62x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 51.2 ms: 1.11x faster                                              |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                               |
| nbody          | 71.9 ms                                                     | 73.5 ms: 1.02x slower                                              |
| Geometric mean | (ref)                                                       | 1.04x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.45 ms: 1.11x faster                                              |
| regex_compile  | 87.5 ms                                                     | 82.9 ms: 1.06x faster                                              |
| regex_dna      | 126 ms                                                      | 124 ms: 1.02x faster                                               |
| regex_v8       | 14.2 ms                                                     | 15.6 ms: 1.10x slower                                              |
| Geometric mean | (ref)                                                       | 1.02x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 88.6 ms: 1.05x faster                                              |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.8 ms: 1.02x faster                                              |
| xml_etree_generate   | 55.8 ms                                                     | 57.0 ms: 1.02x slower                                              |
| tomli_loads          | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                             |
| json_loads           | 13.9 us                                                     | 14.5 us: 1.04x slower                                              |
| xml_etree_process    | 37.7 ms                                                     | 40.6 ms: 1.08x slower                                              |
| unpickle_pure_python | 133 us                                                      | 144 us: 1.08x slower                                               |
| pickle_pure_python   | 195 us                                                      | 220 us: 1.13x slower                                               |
| json_dumps           | 5.70 ms                                                     | 6.80 ms: 1.19x slower                                              |
| Geometric mean       | (ref)                                                       | 1.05x slower                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.3 ms: 1.06x slower                                              |
| python_startup         | 19.5 ms                                                     | 23.4 ms: 1.20x slower                                              |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.71 ms: 1.06x faster                                              |
| django_template | 22.9 ms                                                     | 25.5 ms: 1.11x slower                                              |
| Geometric mean  | (ref)                                                       | 1.02x slower                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 402 ms: 1.92x faster                                               |
| async_tree_io              | 731 ms                                                      | 409 ms: 1.79x faster                                               |
| async_tree_memoization_tg  | 367 ms                                                      | 210 ms: 1.75x faster                                               |
| async_tree_none_tg         | 285 ms                                                      | 170 ms: 1.68x faster                                               |
| async_tree_none            | 291 ms                                                      | 185 ms: 1.58x faster                                               |
| async_tree_memoization     | 339 ms                                                      | 226 ms: 1.50x faster                                               |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 347 ms: 1.45x faster                                               |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 349 ms: 1.40x faster                                               |
| deepcopy                   | 238 us                                                      | 187 us: 1.28x faster                                               |
| deepcopy_memo              | 23.7 us                                                     | 20.4 us: 1.16x faster                                              |
| comprehensions             | 14.1 us                                                     | 12.3 us: 1.15x faster                                              |
| dulwich_log                | 44.3 ms                                                     | 39.0 ms: 1.14x faster                                              |
| spectral_norm              | 66.9 ms                                                     | 59.1 ms: 1.13x faster                                              |
| regex_effbot               | 1.62 ms                                                     | 1.45 ms: 1.11x faster                                              |
| float                      | 56.8 ms                                                     | 51.2 ms: 1.11x faster                                              |
| deepcopy_reduce            | 2.09 us                                                     | 1.89 us: 1.11x faster                                              |
| go                         | 91.6 ms                                                     | 85.3 ms: 1.07x faster                                              |
| coroutines                 | 14.3 ms                                                     | 13.3 ms: 1.07x faster                                              |
| pathlib                    | 80.5 ms                                                     | 76.0 ms: 1.06x faster                                              |
| sqlite_synth               | 1.76 us                                                     | 1.66 us: 1.06x faster                                              |
| mako                       | 7.09 ms                                                     | 6.71 ms: 1.06x faster                                              |
| regex_compile              | 87.5 ms                                                     | 82.9 ms: 1.06x faster                                              |
| xml_etree_parse            | 93.0 ms                                                     | 88.6 ms: 1.05x faster                                              |
| sympy_sum                  | 91.5 ms                                                     | 88.4 ms: 1.04x faster                                              |
| bench_thread_pool          | 857 us                                                      | 829 us: 1.03x faster                                               |
| scimark_lu                 | 58.9 ms                                                     | 57.0 ms: 1.03x faster                                              |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                               |
| generators                 | 22.5 ms                                                     | 21.9 ms: 1.03x faster                                              |
| json                       | 3.05 ms                                                     | 2.97 ms: 1.03x faster                                              |
| sympy_str                  | 175 ms                                                      | 171 ms: 1.03x faster                                               |
| regex_dna                  | 126 ms                                                      | 124 ms: 1.02x faster                                               |
| raytrace                   | 192 ms                                                      | 188 ms: 1.02x faster                                               |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.8 ms: 1.02x faster                                              |
| async_generators           | 239 ms                                                      | 236 ms: 1.02x faster                                               |
| chaos                      | 43.3 ms                                                     | 42.8 ms: 1.01x faster                                              |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.54 ms: 1.01x faster                                              |
| crypto_pyaes               | 48.5 ms                                                     | 48.2 ms: 1.01x faster                                              |
| scimark_fft                | 184 ms                                                      | 185 ms: 1.00x slower                                               |
| sympy_expand               | 284 ms                                                      | 288 ms: 1.01x slower                                               |
| logging_simple             | 6.28 us                                                     | 6.37 us: 1.02x slower                                              |
| nqueens                    | 62.8 ms                                                     | 63.8 ms: 1.02x slower                                              |
| logging_format             | 6.72 us                                                     | 6.83 us: 1.02x slower                                              |
| 2to3                       | 218 ms                                                      | 222 ms: 1.02x slower                                               |
| scimark_monte_carlo        | 43.7 ms                                                     | 44.5 ms: 1.02x slower                                              |
| logging_silent             | 60.5 ns                                                     | 61.7 ns: 1.02x slower                                              |
| xml_etree_generate         | 55.8 ms                                                     | 57.0 ms: 1.02x slower                                              |
| nbody                      | 71.9 ms                                                     | 73.5 ms: 1.02x slower                                              |
| sqlglot_optimize           | 34.5 ms                                                     | 35.6 ms: 1.03x slower                                              |
| deltablue                  | 2.16 ms                                                     | 2.23 ms: 1.03x slower                                              |
| tomli_loads                | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                             |
| sympy_integrate            | 13.0 ms                                                     | 13.4 ms: 1.03x slower                                              |
| meteor_contest             | 74.6 ms                                                     | 77.5 ms: 1.04x slower                                              |
| pprint_pformat             | 1.05 sec                                                    | 1.09 sec: 1.04x slower                                             |
| json_loads                 | 13.9 us                                                     | 14.5 us: 1.04x slower                                              |
| sqlglot_normalize          | 187 ms                                                      | 196 ms: 1.05x slower                                               |
| hexiom                     | 4.10 ms                                                     | 4.33 ms: 1.06x slower                                              |
| pprint_safe_repr           | 513 ms                                                      | 542 ms: 1.06x slower                                               |
| python_startup_no_site     | 16.2 ms                                                     | 17.3 ms: 1.06x slower                                              |
| pycparser                  | 699 ms                                                      | 747 ms: 1.07x slower                                               |
| xml_etree_process          | 37.7 ms                                                     | 40.6 ms: 1.08x slower                                              |
| unpickle_pure_python       | 133 us                                                      | 144 us: 1.08x slower                                               |
| sqlglot_transpile          | 1.02 ms                                                     | 1.10 ms: 1.08x slower                                              |
| pyflate                    | 295 ms                                                      | 319 ms: 1.08x slower                                               |
| sqlglot_parse              | 804 us                                                      | 877 us: 1.09x slower                                               |
| mdp                        | 1.37 sec                                                    | 1.50 sec: 1.09x slower                                             |
| richards                   | 28.4 ms                                                     | 31.1 ms: 1.09x slower                                              |
| regex_v8                   | 14.2 ms                                                     | 15.6 ms: 1.10x slower                                              |
| fannkuch                   | 247 ms                                                      | 271 ms: 1.10x slower                                               |
| richards_super             | 32.1 ms                                                     | 35.3 ms: 1.10x slower                                              |
| django_template            | 22.9 ms                                                     | 25.5 ms: 1.11x slower                                              |
| pickle_pure_python         | 195 us                                                      | 220 us: 1.13x slower                                               |
| scimark_sor                | 78.8 ms                                                     | 88.9 ms: 1.13x slower                                              |
| coverage                   | 40.8 ms                                                     | 46.8 ms: 1.15x slower                                              |
| telco                      | 4.13 ms                                                     | 4.78 ms: 1.16x slower                                              |
| typing_runtime_protocols   | 95.1 us                                                     | 113 us: 1.18x slower                                               |
| bench_mp_pool              | 69.2 ms                                                     | 82.1 ms: 1.19x slower                                              |
| json_dumps                 | 5.70 ms                                                     | 6.80 ms: 1.19x slower                                              |
| python_startup             | 19.5 ms                                                     | 23.4 ms: 1.20x slower                                              |
| mypy2                      | 509 ms                                                      | 639 ms: 1.25x slower                                               |
| gc_traversal               | 1.52 ms                                                     | 1.96 ms: 1.29x slower                                              |
| create_gc_cycles           | 752 us                                                      | 1.20 ms: 1.60x slower                                              |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                       |

Benchmark hidden because not significant (1): docutils
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250107-3.14.0a3+-f098037/bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.026x faster

# HPT report

- Reliability score: 55.64% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown