# Results vs. 3.12.0

- fork: brandtbucher
- ref: nojit
- machine: windows-amd64
- commit hash: f098037
- commit date: 2025-01-07
- overall geometric mean: 1.079x faster
- HPT reliability: 98.68%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 220 ms: 1.01x slower                                               |
| docutils       | 1.66 sec                                                    | 1.72 sec: 1.04x slower                                             |
| Geometric mean | (ref)                                                       | 1.02x slower                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 391 ms: 1.97x faster                                               |
| async_tree_io              | 731 ms                                                      | 399 ms: 1.83x faster                                               |
| async_tree_memoization_tg  | 367 ms                                                      | 212 ms: 1.73x faster                                               |
| async_tree_none_tg         | 285 ms                                                      | 166 ms: 1.72x faster                                               |
| async_tree_none            | 291 ms                                                      | 182 ms: 1.60x faster                                               |
| async_tree_memoization     | 339 ms                                                      | 220 ms: 1.54x faster                                               |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 347 ms: 1.45x faster                                               |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 352 ms: 1.39x faster                                               |
| Geometric mean             | (ref)                                                       | 1.64x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 39.5 ms: 1.44x faster                                              |
| nbody          | 71.9 ms                                                     | 54.2 ms: 1.33x faster                                              |
| pidigits       | 152 ms                                                      | 147 ms: 1.04x faster                                               |
| Geometric mean | (ref)                                                       | 1.26x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.41 ms: 1.15x faster                                              |
| regex_dna      | 126 ms                                                      | 113 ms: 1.11x faster                                               |
| regex_compile  | 87.5 ms                                                     | 80.5 ms: 1.09x faster                                              |
| regex_v8       | 14.2 ms                                                     | 14.6 ms: 1.03x slower                                              |
| Geometric mean | (ref)                                                       | 1.08x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 109 us: 1.22x faster                                               |
| tomli_loads          | 1.37 sec                                                    | 1.19 sec: 1.15x faster                                             |
| xml_etree_generate   | 55.8 ms                                                     | 49.6 ms: 1.12x faster                                              |
| xml_etree_iterparse  | 65.2 ms                                                     | 59.1 ms: 1.10x faster                                              |
| xml_etree_parse      | 93.0 ms                                                     | 87.4 ms: 1.06x faster                                              |
| xml_etree_process    | 37.7 ms                                                     | 35.9 ms: 1.05x faster                                              |
| json_loads           | 13.9 us                                                     | 14.0 us: 1.01x slower                                              |
| pickle_pure_python   | 195 us                                                      | 207 us: 1.06x slower                                               |
| json_dumps           | 5.70 ms                                                     | 6.42 ms: 1.13x slower                                              |
| Geometric mean       | (ref)                                                       | 1.06x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.0 ms: 1.05x slower                                              |
| python_startup         | 19.5 ms                                                     | 23.1 ms: 1.18x slower                                              |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.16 ms: 1.37x faster                                              |
| django_template | 22.9 ms                                                     | 26.0 ms: 1.13x slower                                              |
| Geometric mean  | (ref)                                                       | 1.10x faster                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 391 ms: 1.97x faster                                               |
| async_tree_io              | 731 ms                                                      | 399 ms: 1.83x faster                                               |
| async_tree_memoization_tg  | 367 ms                                                      | 212 ms: 1.73x faster                                               |
| async_tree_none_tg         | 285 ms                                                      | 166 ms: 1.72x faster                                               |
| async_tree_none            | 291 ms                                                      | 182 ms: 1.60x faster                                               |
| async_tree_memoization     | 339 ms                                                      | 220 ms: 1.54x faster                                               |
| deepcopy_memo              | 23.7 us                                                     | 16.0 us: 1.48x faster                                              |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 347 ms: 1.45x faster                                               |
| float                      | 56.8 ms                                                     | 39.5 ms: 1.44x faster                                              |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 352 ms: 1.39x faster                                               |
| mako                       | 7.09 ms                                                     | 5.16 ms: 1.37x faster                                              |
| spectral_norm              | 66.9 ms                                                     | 49.6 ms: 1.35x faster                                              |
| nbody                      | 71.9 ms                                                     | 54.2 ms: 1.33x faster                                              |
| scimark_sor                | 78.8 ms                                                     | 59.7 ms: 1.32x faster                                              |
| scimark_fft                | 184 ms                                                      | 142 ms: 1.30x faster                                               |
| deepcopy                   | 238 us                                                      | 188 us: 1.27x faster                                               |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.08 ms: 1.23x faster                                              |
| scimark_monte_carlo        | 43.7 ms                                                     | 35.7 ms: 1.22x faster                                              |
| unpickle_pure_python       | 133 us                                                      | 109 us: 1.22x faster                                               |
| comprehensions             | 14.1 us                                                     | 11.6 us: 1.22x faster                                              |
| crypto_pyaes               | 48.5 ms                                                     | 40.9 ms: 1.18x faster                                              |
| tomli_loads                | 1.37 sec                                                    | 1.19 sec: 1.15x faster                                             |
| regex_effbot               | 1.62 ms                                                     | 1.41 ms: 1.15x faster                                              |
| xml_etree_generate         | 55.8 ms                                                     | 49.6 ms: 1.12x faster                                              |
| deepcopy_reduce            | 2.09 us                                                     | 1.87 us: 1.12x faster                                              |
| sqlite_synth               | 1.76 us                                                     | 1.57 us: 1.12x faster                                              |
| regex_dna                  | 126 ms                                                      | 113 ms: 1.11x faster                                               |
| dulwich_log                | 44.3 ms                                                     | 39.9 ms: 1.11x faster                                              |
| scimark_lu                 | 58.9 ms                                                     | 53.2 ms: 1.11x faster                                              |
| xml_etree_iterparse        | 65.2 ms                                                     | 59.1 ms: 1.10x faster                                              |
| pprint_pformat             | 1.05 sec                                                    | 955 ms: 1.09x faster                                               |
| regex_compile              | 87.5 ms                                                     | 80.5 ms: 1.09x faster                                              |
| pprint_safe_repr           | 513 ms                                                      | 472 ms: 1.09x faster                                               |
| logging_silent             | 60.5 ns                                                     | 55.7 ns: 1.08x faster                                              |
| xml_etree_parse            | 93.0 ms                                                     | 87.4 ms: 1.06x faster                                              |
| pyflate                    | 295 ms                                                      | 277 ms: 1.06x faster                                               |
| pathlib                    | 80.5 ms                                                     | 75.8 ms: 1.06x faster                                              |
| xml_etree_process          | 37.7 ms                                                     | 35.9 ms: 1.05x faster                                              |
| json                       | 3.05 ms                                                     | 2.90 ms: 1.05x faster                                              |
| coroutines                 | 14.3 ms                                                     | 13.7 ms: 1.04x faster                                              |
| pidigits                   | 152 ms                                                      | 147 ms: 1.04x faster                                               |
| chaos                      | 43.3 ms                                                     | 41.8 ms: 1.04x faster                                              |
| fannkuch                   | 247 ms                                                      | 238 ms: 1.04x faster                                               |
| go                         | 91.6 ms                                                     | 88.6 ms: 1.03x faster                                              |
| meteor_contest             | 74.6 ms                                                     | 72.6 ms: 1.03x faster                                              |
| logging_simple             | 6.28 us                                                     | 6.20 us: 1.01x faster                                              |
| logging_format             | 6.72 us                                                     | 6.68 us: 1.01x faster                                              |
| sympy_str                  | 175 ms                                                      | 176 ms: 1.01x slower                                               |
| json_loads                 | 13.9 us                                                     | 14.0 us: 1.01x slower                                              |
| 2to3                       | 218 ms                                                      | 220 ms: 1.01x slower                                               |
| pycparser                  | 699 ms                                                      | 707 ms: 1.01x slower                                               |
| sqlglot_parse              | 804 us                                                      | 824 us: 1.02x slower                                               |
| generators                 | 22.5 ms                                                     | 23.1 ms: 1.03x slower                                              |
| regex_v8                   | 14.2 ms                                                     | 14.6 ms: 1.03x slower                                              |
| nqueens                    | 62.8 ms                                                     | 65.1 ms: 1.04x slower                                              |
| docutils                   | 1.66 sec                                                    | 1.72 sec: 1.04x slower                                             |
| deltablue                  | 2.16 ms                                                     | 2.25 ms: 1.04x slower                                              |
| sqlglot_transpile          | 1.02 ms                                                     | 1.07 ms: 1.04x slower                                              |
| python_startup_no_site     | 16.2 ms                                                     | 17.0 ms: 1.05x slower                                              |
| sympy_integrate            | 13.0 ms                                                     | 13.6 ms: 1.05x slower                                              |
| telco                      | 4.13 ms                                                     | 4.35 ms: 1.05x slower                                              |
| pickle_pure_python         | 195 us                                                      | 207 us: 1.06x slower                                               |
| sympy_expand               | 284 ms                                                      | 300 ms: 1.06x slower                                               |
| raytrace                   | 192 ms                                                      | 205 ms: 1.07x slower                                               |
| async_generators           | 239 ms                                                      | 259 ms: 1.08x slower                                               |
| sqlglot_normalize          | 187 ms                                                      | 203 ms: 1.09x slower                                               |
| sqlglot_optimize           | 34.5 ms                                                     | 37.6 ms: 1.09x slower                                              |
| mdp                        | 1.37 sec                                                    | 1.52 sec: 1.11x slower                                             |
| json_dumps                 | 5.70 ms                                                     | 6.42 ms: 1.13x slower                                              |
| django_template            | 22.9 ms                                                     | 26.0 ms: 1.13x slower                                              |
| coverage                   | 40.8 ms                                                     | 46.5 ms: 1.14x slower                                              |
| python_startup             | 19.5 ms                                                     | 23.1 ms: 1.18x slower                                              |
| bench_mp_pool              | 69.2 ms                                                     | 82.0 ms: 1.19x slower                                              |
| richards_super             | 32.1 ms                                                     | 38.4 ms: 1.20x slower                                              |
| richards                   | 28.4 ms                                                     | 34.2 ms: 1.21x slower                                              |
| typing_runtime_protocols   | 95.1 us                                                     | 116 us: 1.22x slower                                               |
| hexiom                     | 4.10 ms                                                     | 5.04 ms: 1.23x slower                                              |
| mypy2                      | 509 ms                                                      | 641 ms: 1.26x slower                                               |
| gc_traversal               | 1.52 ms                                                     | 1.96 ms: 1.29x slower                                              |
| create_gc_cycles           | 752 us                                                      | 1.21 ms: 1.61x slower                                              |
| Geometric mean             | (ref)                                                       | 1.07x faster                                                       |

Benchmark hidden because not significant (2): bench_thread_pool, sympy_sum
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250107-3.14.0a3+-f098037-JIT/bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.079x faster

# HPT report

- Reliability score: 98.68% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown