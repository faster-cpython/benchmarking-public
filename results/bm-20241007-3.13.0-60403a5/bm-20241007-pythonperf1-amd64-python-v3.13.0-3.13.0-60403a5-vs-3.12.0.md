# Results vs. 3.12.0

- fork: python
- ref: v3.13.0
- machine: windows-amd64
- commit hash: 60403a5
- commit date: 2024-10-07
- overall geometric mean: 1.060x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 215 ms: 1.01x faster                                        |
| chameleon      | 4.98 ms                                                     | 4.74 ms: 1.05x faster                                       |
| docutils       | 1.66 sec                                                    | 1.53 sec: 1.08x faster                                      |
| tornado_http   | 89.5 ms                                                     | 81.2 ms: 1.10x faster                                       |
| Geometric mean | (ref)                                                       | 1.06x faster                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 497 ms: 1.55x faster                                        |
| async_tree_io              | 731 ms                                                      | 513 ms: 1.43x faster                                        |
| async_tree_none_tg         | 285 ms                                                      | 200 ms: 1.42x faster                                        |
| async_tree_none            | 291 ms                                                      | 219 ms: 1.33x faster                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 383 ms: 1.31x faster                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 281 ms: 1.31x faster                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 380 ms: 1.29x faster                                        |
| async_tree_memoization     | 339 ms                                                      | 265 ms: 1.28x faster                                        |
| Geometric mean             | (ref)                                                       | 1.36x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 56.8 ms                                                     | 50.8 ms: 1.12x faster                                       |
| nbody          | 71.9 ms                                                     | 66.3 ms: 1.08x faster                                       |
| pidigits       | 152 ms                                                      | 146 ms: 1.04x faster                                        |
| Geometric mean | (ref)                                                       | 1.08x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 115 ms: 1.10x faster                                        |
| regex_compile  | 87.5 ms                                                     | 80.7 ms: 1.08x faster                                       |
| regex_effbot   | 1.62 ms                                                     | 1.69 ms: 1.05x slower                                       |
| regex_v8       | 14.2 ms                                                     | 23.8 ms: 1.67x slower                                       |
| Geometric mean | (ref)                                                       | 1.10x slower                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 60.5 ms: 1.08x faster                                       |
| pickle_pure_python   | 195 us                                                      | 186 us: 1.05x faster                                        |
| xml_etree_generate   | 55.8 ms                                                     | 53.5 ms: 1.04x faster                                       |
| xml_etree_process    | 37.7 ms                                                     | 36.5 ms: 1.03x faster                                       |
| unpickle_pure_python | 133 us                                                      | 130 us: 1.02x faster                                        |
| xml_etree_parse      | 93.0 ms                                                     | 92.2 ms: 1.01x faster                                       |
| json_loads           | 13.9 us                                                     | 15.1 us: 1.09x slower                                       |
| json_dumps           | 5.70 ms                                                     | 6.19 ms: 1.09x slower                                       |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 16.9 ms: 1.04x slower                                       |
| python_startup         | 19.5 ms                                                     | 24.4 ms: 1.25x slower                                       |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 20.3 ms: 1.13x faster                                       |
| mako            | 7.09 ms                                                     | 6.56 ms: 1.08x faster                                       |
| Geometric mean  | (ref)                                                       | 1.10x faster                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 497 ms: 1.55x faster                                        |
| async_tree_io              | 731 ms                                                      | 513 ms: 1.43x faster                                        |
| async_tree_none_tg         | 285 ms                                                      | 200 ms: 1.42x faster                                        |
| comprehensions             | 14.1 us                                                     | 10.4 us: 1.36x faster                                       |
| async_tree_none            | 291 ms                                                      | 219 ms: 1.33x faster                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 383 ms: 1.31x faster                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 281 ms: 1.31x faster                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 380 ms: 1.29x faster                                        |
| async_tree_memoization     | 339 ms                                                      | 265 ms: 1.28x faster                                        |
| raytrace                   | 192 ms                                                      | 153 ms: 1.25x faster                                        |
| generators                 | 22.5 ms                                                     | 19.0 ms: 1.19x faster                                       |
| chaos                      | 43.3 ms                                                     | 37.9 ms: 1.14x faster                                       |
| deltablue                  | 2.16 ms                                                     | 1.89 ms: 1.14x faster                                       |
| coroutines                 | 14.3 ms                                                     | 12.5 ms: 1.14x faster                                       |
| django_template            | 22.9 ms                                                     | 20.3 ms: 1.13x faster                                       |
| nqueens                    | 62.8 ms                                                     | 56.1 ms: 1.12x faster                                       |
| float                      | 56.8 ms                                                     | 50.8 ms: 1.12x faster                                       |
| sqlalchemy_declarative     | 86.4 ms                                                     | 77.4 ms: 1.12x faster                                       |
| sqlite_synth               | 1.76 us                                                     | 1.59 us: 1.11x faster                                       |
| logging_silent             | 60.5 ns                                                     | 54.6 ns: 1.11x faster                                       |
| dulwich_log                | 44.3 ms                                                     | 40.1 ms: 1.10x faster                                       |
| tornado_http               | 89.5 ms                                                     | 81.2 ms: 1.10x faster                                       |
| regex_dna                  | 126 ms                                                      | 115 ms: 1.10x faster                                        |
| sqlglot_normalize          | 187 ms                                                      | 172 ms: 1.09x faster                                        |
| logging_format             | 6.72 us                                                     | 6.18 us: 1.09x faster                                       |
| logging_simple             | 6.28 us                                                     | 5.77 us: 1.09x faster                                       |
| nbody                      | 71.9 ms                                                     | 66.3 ms: 1.08x faster                                       |
| docutils                   | 1.66 sec                                                    | 1.53 sec: 1.08x faster                                      |
| regex_compile              | 87.5 ms                                                     | 80.7 ms: 1.08x faster                                       |
| go                         | 91.6 ms                                                     | 84.7 ms: 1.08x faster                                       |
| richards                   | 28.4 ms                                                     | 26.3 ms: 1.08x faster                                       |
| mako                       | 7.09 ms                                                     | 6.56 ms: 1.08x faster                                       |
| richards_super             | 32.1 ms                                                     | 29.8 ms: 1.08x faster                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 60.5 ms: 1.08x faster                                       |
| async_generators           | 239 ms                                                      | 223 ms: 1.07x faster                                        |
| sympy_sum                  | 91.5 ms                                                     | 85.2 ms: 1.07x faster                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.7 ms: 1.07x faster                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 953 us: 1.07x faster                                        |
| pprint_pformat             | 1.05 sec                                                    | 977 ms: 1.07x faster                                        |
| pathlib                    | 80.5 ms                                                     | 75.3 ms: 1.07x faster                                       |
| hexiom                     | 4.10 ms                                                     | 3.84 ms: 1.07x faster                                       |
| deepcopy                   | 238 us                                                      | 223 us: 1.07x faster                                        |
| crypto_pyaes               | 48.5 ms                                                     | 45.6 ms: 1.06x faster                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 32.5 ms: 1.06x faster                                       |
| pprint_safe_repr           | 513 ms                                                      | 485 ms: 1.06x faster                                        |
| bench_thread_pool          | 857 us                                                      | 810 us: 1.06x faster                                        |
| spectral_norm              | 66.9 ms                                                     | 63.4 ms: 1.06x faster                                       |
| scimark_fft                | 184 ms                                                      | 175 ms: 1.05x faster                                        |
| sqlglot_parse              | 804 us                                                      | 764 us: 1.05x faster                                        |
| chameleon                  | 4.98 ms                                                     | 4.74 ms: 1.05x faster                                       |
| pickle_pure_python         | 195 us                                                      | 186 us: 1.05x faster                                        |
| sympy_integrate            | 13.0 ms                                                     | 12.3 ms: 1.05x faster                                       |
| sympy_str                  | 175 ms                                                      | 167 ms: 1.05x faster                                        |
| xml_etree_generate         | 55.8 ms                                                     | 53.5 ms: 1.04x faster                                       |
| pyflate                    | 295 ms                                                      | 283 ms: 1.04x faster                                        |
| pidigits                   | 152 ms                                                      | 146 ms: 1.04x faster                                        |
| scimark_lu                 | 58.9 ms                                                     | 56.7 ms: 1.04x faster                                       |
| meteor_contest             | 74.6 ms                                                     | 72.0 ms: 1.04x faster                                       |
| deepcopy_reduce            | 2.09 us                                                     | 2.02 us: 1.03x faster                                       |
| scimark_sor                | 78.8 ms                                                     | 76.2 ms: 1.03x faster                                       |
| xml_etree_process          | 37.7 ms                                                     | 36.5 ms: 1.03x faster                                       |
| deepcopy_memo              | 23.7 us                                                     | 23.1 us: 1.03x faster                                       |
| unpickle_pure_python       | 133 us                                                      | 130 us: 1.02x faster                                        |
| 2to3                       | 218 ms                                                      | 215 ms: 1.01x faster                                        |
| xml_etree_parse            | 93.0 ms                                                     | 92.2 ms: 1.01x faster                                       |
| sympy_expand               | 284 ms                                                      | 286 ms: 1.01x slower                                        |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.60 ms: 1.02x slower                                       |
| fannkuch                   | 247 ms                                                      | 252 ms: 1.02x slower                                        |
| python_startup_no_site     | 16.2 ms                                                     | 16.9 ms: 1.04x slower                                       |
| mdp                        | 1.37 sec                                                    | 1.43 sec: 1.04x slower                                      |
| regex_effbot               | 1.62 ms                                                     | 1.69 ms: 1.05x slower                                       |
| json                       | 3.05 ms                                                     | 3.30 ms: 1.08x slower                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 103 us: 1.08x slower                                        |
| json_loads                 | 13.9 us                                                     | 15.1 us: 1.09x slower                                       |
| json_dumps                 | 5.70 ms                                                     | 6.19 ms: 1.09x slower                                       |
| coverage                   | 40.8 ms                                                     | 45.3 ms: 1.11x slower                                       |
| telco                      | 4.13 ms                                                     | 4.85 ms: 1.17x slower                                       |
| bench_mp_pool              | 69.2 ms                                                     | 84.2 ms: 1.22x slower                                       |
| python_startup             | 19.5 ms                                                     | 24.4 ms: 1.25x slower                                       |
| gc_traversal               | 1.52 ms                                                     | 1.96 ms: 1.29x slower                                       |
| create_gc_cycles           | 752 us                                                      | 1.22 ms: 1.63x slower                                       |
| regex_v8                   | 14.2 ms                                                     | 23.8 ms: 1.67x slower                                       |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                |

Benchmark hidden because not significant (3): pycparser, sqlalchemy_imperative, tomli_loads
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.060x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown