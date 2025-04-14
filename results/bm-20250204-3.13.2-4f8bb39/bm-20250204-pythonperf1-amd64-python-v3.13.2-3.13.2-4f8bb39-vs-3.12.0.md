# Results vs. 3.12.0

- fork: python
- ref: v3.13.2
- machine: windows-amd64
- commit hash: 4f8bb39
- commit date: 2025-02-04
- overall geometric mean: 1.066x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-pythonperf1-amd64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| chameleon      | 4.98 ms                                                     | 4.72 ms: 1.06x faster                                       |
| docutils       | 1.66 sec                                                    | 1.54 sec: 1.08x faster                                      |
| tornado_http   | 89.5 ms                                                     | 100 ms: 1.12x slower                                        |
| Geometric mean | (ref)                                                       | 1.01x faster                                                |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-pythonperf1-amd64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 527 ms: 1.46x faster                                        |
| async_tree_io              | 731 ms                                                      | 519 ms: 1.41x faster                                        |
| async_tree_none_tg         | 285 ms                                                      | 203 ms: 1.41x faster                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 277 ms: 1.32x faster                                        |
| async_tree_none            | 291 ms                                                      | 224 ms: 1.30x faster                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 381 ms: 1.28x faster                                        |
| async_tree_memoization     | 339 ms                                                      | 270 ms: 1.26x faster                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 406 ms: 1.24x faster                                        |
| Geometric mean             | (ref)                                                       | 1.33x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-pythonperf1-amd64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 56.8 ms                                                     | 47.7 ms: 1.19x faster                                       |
| nbody          | 71.9 ms                                                     | 65.1 ms: 1.10x faster                                       |
| pidigits       | 152 ms                                                      | 147 ms: 1.03x faster                                        |
| Geometric mean | (ref)                                                       | 1.11x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-pythonperf1-amd64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.41 ms: 1.14x faster                                       |
| regex_dna      | 126 ms                                                      | 113 ms: 1.11x faster                                        |
| regex_compile  | 87.5 ms                                                     | 79.8 ms: 1.10x faster                                       |
| regex_v8       | 14.2 ms                                                     | 15.0 ms: 1.06x slower                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-pythonperf1-amd64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| xml_etree_generate   | 55.8 ms                                                     | 53.8 ms: 1.04x faster                                       |
| xml_etree_process    | 37.7 ms                                                     | 36.4 ms: 1.04x faster                                       |
| pickle_pure_python   | 195 us                                                      | 189 us: 1.03x faster                                        |
| unpickle_pure_python | 133 us                                                      | 130 us: 1.03x faster                                        |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.5 ms: 1.03x faster                                       |
| xml_etree_parse      | 93.0 ms                                                     | 91.4 ms: 1.02x faster                                       |
| json_dumps           | 5.70 ms                                                     | 5.84 ms: 1.02x slower                                       |
| json_loads           | 13.9 us                                                     | 14.5 us: 1.04x slower                                       |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-pythonperf1-amd64-python-v3.13.2-3.13.2-4f8bb39 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.6 ms: 1.14x slower                                       |
| python_startup         | 19.5 ms                                                     | 26.5 ms: 1.36x slower                                       |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-pythonperf1-amd64-python-v3.13.2-3.13.2-4f8bb39 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 19.9 ms: 1.15x faster                                       |
| mako            | 7.09 ms                                                     | 6.35 ms: 1.12x faster                                       |
| Geometric mean  | (ref)                                                       | 1.13x faster                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-pythonperf1-amd64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 527 ms: 1.46x faster                                        |
| async_tree_io              | 731 ms                                                      | 519 ms: 1.41x faster                                        |
| async_tree_none_tg         | 285 ms                                                      | 203 ms: 1.41x faster                                        |
| comprehensions             | 14.1 us                                                     | 10.5 us: 1.35x faster                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 277 ms: 1.32x faster                                        |
| pathlib                    | 80.5 ms                                                     | 61.8 ms: 1.30x faster                                       |
| async_tree_none            | 291 ms                                                      | 224 ms: 1.30x faster                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 381 ms: 1.28x faster                                        |
| async_tree_memoization     | 339 ms                                                      | 270 ms: 1.26x faster                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 406 ms: 1.24x faster                                        |
| raytrace                   | 192 ms                                                      | 156 ms: 1.24x faster                                        |
| generators                 | 22.5 ms                                                     | 18.2 ms: 1.24x faster                                       |
| float                      | 56.8 ms                                                     | 47.7 ms: 1.19x faster                                       |
| chaos                      | 43.3 ms                                                     | 36.8 ms: 1.18x faster                                       |
| django_template            | 22.9 ms                                                     | 19.9 ms: 1.15x faster                                       |
| regex_effbot               | 1.62 ms                                                     | 1.41 ms: 1.14x faster                                       |
| deltablue                  | 2.16 ms                                                     | 1.89 ms: 1.14x faster                                       |
| async_generators           | 239 ms                                                      | 211 ms: 1.13x faster                                        |
| sqlite_synth               | 1.76 us                                                     | 1.55 us: 1.13x faster                                       |
| coroutines                 | 14.3 ms                                                     | 12.7 ms: 1.12x faster                                       |
| mako                       | 7.09 ms                                                     | 6.35 ms: 1.12x faster                                       |
| regex_dna                  | 126 ms                                                      | 113 ms: 1.11x faster                                        |
| spectral_norm              | 66.9 ms                                                     | 60.4 ms: 1.11x faster                                       |
| nbody                      | 71.9 ms                                                     | 65.1 ms: 1.10x faster                                       |
| nqueens                    | 62.8 ms                                                     | 57.1 ms: 1.10x faster                                       |
| logging_silent             | 60.5 ns                                                     | 55.0 ns: 1.10x faster                                       |
| regex_compile              | 87.5 ms                                                     | 79.8 ms: 1.10x faster                                       |
| sqlalchemy_declarative     | 86.4 ms                                                     | 78.8 ms: 1.10x faster                                       |
| sqlglot_normalize          | 187 ms                                                      | 171 ms: 1.09x faster                                        |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.3 ms: 1.08x faster                                       |
| logging_simple             | 6.28 us                                                     | 5.79 us: 1.08x faster                                       |
| crypto_pyaes               | 48.5 ms                                                     | 44.8 ms: 1.08x faster                                       |
| hexiom                     | 4.10 ms                                                     | 3.79 ms: 1.08x faster                                       |
| logging_format             | 6.72 us                                                     | 6.21 us: 1.08x faster                                       |
| docutils                   | 1.66 sec                                                    | 1.54 sec: 1.08x faster                                      |
| dulwich_log                | 44.3 ms                                                     | 41.3 ms: 1.07x faster                                       |
| go                         | 91.6 ms                                                     | 85.4 ms: 1.07x faster                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 955 us: 1.07x faster                                        |
| sympy_sum                  | 91.5 ms                                                     | 86.0 ms: 1.06x faster                                       |
| sqlglot_parse              | 804 us                                                      | 757 us: 1.06x faster                                        |
| sympy_str                  | 175 ms                                                      | 166 ms: 1.06x faster                                        |
| chameleon                  | 4.98 ms                                                     | 4.72 ms: 1.06x faster                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 32.8 ms: 1.05x faster                                       |
| pprint_pformat             | 1.05 sec                                                    | 994 ms: 1.05x faster                                        |
| pprint_safe_repr           | 513 ms                                                      | 488 ms: 1.05x faster                                        |
| richards_super             | 32.1 ms                                                     | 30.5 ms: 1.05x faster                                       |
| richards                   | 28.4 ms                                                     | 27.0 ms: 1.05x faster                                       |
| sympy_integrate            | 13.0 ms                                                     | 12.4 ms: 1.05x faster                                       |
| deepcopy                   | 238 us                                                      | 228 us: 1.05x faster                                        |
| meteor_contest             | 74.6 ms                                                     | 71.7 ms: 1.04x faster                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.46 ms: 1.04x faster                                       |
| xml_etree_generate         | 55.8 ms                                                     | 53.8 ms: 1.04x faster                                       |
| pyflate                    | 295 ms                                                      | 284 ms: 1.04x faster                                        |
| xml_etree_process          | 37.7 ms                                                     | 36.4 ms: 1.04x faster                                       |
| pidigits                   | 152 ms                                                      | 147 ms: 1.03x faster                                        |
| pickle_pure_python         | 195 us                                                      | 189 us: 1.03x faster                                        |
| bench_thread_pool          | 857 us                                                      | 831 us: 1.03x faster                                        |
| unpickle_pure_python       | 133 us                                                      | 130 us: 1.03x faster                                        |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.5 ms: 1.03x faster                                       |
| scimark_sor                | 78.8 ms                                                     | 77.2 ms: 1.02x faster                                       |
| xml_etree_parse            | 93.0 ms                                                     | 91.4 ms: 1.02x faster                                       |
| deepcopy_memo              | 23.7 us                                                     | 23.3 us: 1.02x faster                                       |
| pycparser                  | 699 ms                                                      | 687 ms: 1.02x faster                                        |
| scimark_lu                 | 58.9 ms                                                     | 58.3 ms: 1.01x faster                                       |
| sympy_expand               | 284 ms                                                      | 281 ms: 1.01x faster                                        |
| scimark_fft                | 184 ms                                                      | 183 ms: 1.01x faster                                        |
| fannkuch                   | 247 ms                                                      | 245 ms: 1.01x faster                                        |
| json                       | 3.05 ms                                                     | 3.12 ms: 1.02x slower                                       |
| sqlalchemy_imperative      | 9.29 ms                                                     | 9.52 ms: 1.02x slower                                       |
| json_dumps                 | 5.70 ms                                                     | 5.84 ms: 1.02x slower                                       |
| mdp                        | 1.37 sec                                                    | 1.43 sec: 1.04x slower                                      |
| json_loads                 | 13.9 us                                                     | 14.5 us: 1.04x slower                                       |
| regex_v8                   | 14.2 ms                                                     | 15.0 ms: 1.06x slower                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 104 us: 1.09x slower                                        |
| tornado_http               | 89.5 ms                                                     | 100 ms: 1.12x slower                                        |
| coverage                   | 40.8 ms                                                     | 45.8 ms: 1.12x slower                                       |
| python_startup_no_site     | 16.2 ms                                                     | 18.6 ms: 1.14x slower                                       |
| telco                      | 4.13 ms                                                     | 4.86 ms: 1.18x slower                                       |
| bench_mp_pool              | 69.2 ms                                                     | 86.6 ms: 1.25x slower                                       |
| gc_traversal               | 1.52 ms                                                     | 1.97 ms: 1.30x slower                                       |
| python_startup             | 19.5 ms                                                     | 26.5 ms: 1.36x slower                                       |
| create_gc_cycles           | 752 us                                                      | 1.26 ms: 1.67x slower                                       |
| Geometric mean             | (ref)                                                       | 1.06x faster                                                |

Benchmark hidden because not significant (3): 2to3, deepcopy_reduce, tomli_loads
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250204-3.13.2-4f8bb39/bm-20250204-pythonperf1-amd64-python-v3.13.2-3.13.2-4f8bb39.json: asyncio_websockets, bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.066x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown