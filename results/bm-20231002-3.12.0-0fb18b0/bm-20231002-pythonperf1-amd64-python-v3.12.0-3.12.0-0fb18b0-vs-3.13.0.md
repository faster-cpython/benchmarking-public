# Results vs. 3.13.0

- fork: python
- ref: v3.12.0
- machine: windows-amd64
- commit hash: 0fb18b0
- commit date: 2023-10-02
- overall geometric mean: 1.039x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 218 ms: 1.01x faster                                        |
| chameleon      | 4.82 ms                                                     | 4.98 ms: 1.03x slower                                       |
| docutils       | 1.57 sec                                                    | 1.66 sec: 1.06x slower                                      |
| tornado_http   | 93.0 ms                                                     | 89.5 ms: 1.04x faster                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| async_generators           | 223 ms                                                      | 239 ms: 1.07x slower                                        |
| coroutines                 | 12.8 ms                                                     | 14.3 ms: 1.12x slower                                       |
| async_tree_memoization     | 276 ms                                                      | 339 ms: 1.23x slower                                        |
| async_tree_memoization_tg  | 288 ms                                                      | 367 ms: 1.27x slower                                        |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 489 ms: 1.28x slower                                        |
| async_tree_none            | 226 ms                                                      | 291 ms: 1.29x slower                                        |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 502 ms: 1.33x slower                                        |
| async_tree_none_tg         | 209 ms                                                      | 285 ms: 1.37x slower                                        |
| async_tree_io              | 521 ms                                                      | 731 ms: 1.40x slower                                        |
| async_tree_io_tg           | 518 ms                                                      | 771 ms: 1.49x slower                                        |
| Geometric mean             | (ref)                                                       | 1.28x slower                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 152 ms: 1.03x slower                                        |
| nbody          | 68.4 ms                                                     | 71.9 ms: 1.05x slower                                       |
| float          | 49.9 ms                                                     | 56.8 ms: 1.14x slower                                       |
| Geometric mean | (ref)                                                       | 1.07x slower                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 14.2 ms: 1.50x faster                                       |
| regex_effbot   | 1.58 ms                                                     | 1.62 ms: 1.03x slower                                       |
| regex_compile  | 80.5 ms                                                     | 87.5 ms: 1.09x slower                                       |
| regex_dna      | 115 ms                                                      | 126 ms: 1.10x slower                                        |
| Geometric mean | (ref)                                                       | 1.05x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 |
|---------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| json_loads          | 15.1 us                                                     | 13.9 us: 1.09x faster                                       |
| json_dumps          | 5.92 ms                                                     | 5.70 ms: 1.04x faster                                       |
| tomli_loads         | 1.39 sec                                                    | 1.37 sec: 1.02x faster                                      |
| xml_etree_process   | 37.0 ms                                                     | 37.7 ms: 1.02x slower                                       |
| pickle_pure_python  | 190 us                                                      | 195 us: 1.03x slower                                        |
| xml_etree_generate  | 54.0 ms                                                     | 55.8 ms: 1.03x slower                                       |
| xml_etree_iterparse | 61.8 ms                                                     | 65.2 ms: 1.05x slower                                       |
| Geometric mean      | (ref)                                                       | 1.00x faster                                                |

Benchmark hidden because not significant (2): xml_etree_parse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 19.5 ms: 1.31x faster                                       |
| python_startup_no_site | 18.1 ms                                                     | 16.2 ms: 1.12x faster                                       |
| Geometric mean         | (ref)                                                       | 1.21x faster                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| django_template | 22.4 ms                                                     | 22.9 ms: 1.03x slower                                       |
| mako            | 6.35 ms                                                     | 7.09 ms: 1.12x slower                                       |
| Geometric mean  | (ref)                                                       | 1.07x slower                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| create_gc_cycles           | 1.26 ms                                                     | 752 us: 1.67x faster                                        |
| regex_v8                   | 21.4 ms                                                     | 14.2 ms: 1.50x faster                                       |
| mypy2                      | 679 ms                                                      | 509 ms: 1.33x faster                                        |
| python_startup             | 25.4 ms                                                     | 19.5 ms: 1.31x faster                                       |
| gc_traversal               | 1.97 ms                                                     | 1.52 ms: 1.29x faster                                       |
| bench_mp_pool              | 86.4 ms                                                     | 69.2 ms: 1.25x faster                                       |
| telco                      | 4.79 ms                                                     | 4.13 ms: 1.16x faster                                       |
| python_startup_no_site     | 18.1 ms                                                     | 16.2 ms: 1.12x faster                                       |
| coverage                   | 45.6 ms                                                     | 40.8 ms: 1.12x faster                                       |
| typing_runtime_protocols   | 105 us                                                      | 95.1 us: 1.11x faster                                       |
| json_loads                 | 15.1 us                                                     | 13.9 us: 1.09x faster                                       |
| json                       | 3.19 ms                                                     | 3.05 ms: 1.05x faster                                       |
| sqlalchemy_imperative      | 9.69 ms                                                     | 9.29 ms: 1.04x faster                                       |
| tornado_http               | 93.0 ms                                                     | 89.5 ms: 1.04x faster                                       |
| json_dumps                 | 5.92 ms                                                     | 5.70 ms: 1.04x faster                                       |
| fannkuch                   | 253 ms                                                      | 247 ms: 1.03x faster                                        |
| sympy_expand               | 291 ms                                                      | 284 ms: 1.03x faster                                        |
| tomli_loads                | 1.39 sec                                                    | 1.37 sec: 1.02x faster                                      |
| 2to3                       | 221 ms                                                      | 218 ms: 1.01x faster                                        |
| mdp                        | 1.39 sec                                                    | 1.37 sec: 1.01x faster                                      |
| meteor_contest             | 73.5 ms                                                     | 74.6 ms: 1.01x slower                                       |
| deepcopy_reduce            | 2.06 us                                                     | 2.09 us: 1.02x slower                                       |
| deepcopy_memo              | 23.3 us                                                     | 23.7 us: 1.02x slower                                       |
| xml_etree_process          | 37.0 ms                                                     | 37.7 ms: 1.02x slower                                       |
| pycparser                  | 683 ms                                                      | 699 ms: 1.02x slower                                        |
| django_template            | 22.4 ms                                                     | 22.9 ms: 1.03x slower                                       |
| regex_effbot               | 1.58 ms                                                     | 1.62 ms: 1.03x slower                                       |
| pidigits                   | 148 ms                                                      | 152 ms: 1.03x slower                                        |
| pickle_pure_python         | 190 us                                                      | 195 us: 1.03x slower                                        |
| chameleon                  | 4.82 ms                                                     | 4.98 ms: 1.03x slower                                       |
| xml_etree_generate         | 54.0 ms                                                     | 55.8 ms: 1.03x slower                                       |
| scimark_sor                | 76.2 ms                                                     | 78.8 ms: 1.03x slower                                       |
| sympy_integrate            | 12.5 ms                                                     | 13.0 ms: 1.04x slower                                       |
| sympy_str                  | 169 ms                                                      | 175 ms: 1.04x slower                                        |
| richards                   | 27.3 ms                                                     | 28.4 ms: 1.04x slower                                       |
| richards_super             | 30.9 ms                                                     | 32.1 ms: 1.04x slower                                       |
| pprint_safe_repr           | 494 ms                                                      | 513 ms: 1.04x slower                                        |
| pyflate                    | 283 ms                                                      | 295 ms: 1.04x slower                                        |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.56 ms: 1.04x slower                                       |
| sqlglot_parse              | 771 us                                                      | 804 us: 1.04x slower                                        |
| pprint_pformat             | 999 ms                                                      | 1.05 sec: 1.05x slower                                      |
| sqlglot_optimize           | 32.9 ms                                                     | 34.5 ms: 1.05x slower                                       |
| nbody                      | 68.4 ms                                                     | 71.9 ms: 1.05x slower                                       |
| deepcopy                   | 226 us                                                      | 238 us: 1.05x slower                                        |
| go                         | 87.0 ms                                                     | 91.6 ms: 1.05x slower                                       |
| sympy_sum                  | 86.9 ms                                                     | 91.5 ms: 1.05x slower                                       |
| hexiom                     | 3.89 ms                                                     | 4.10 ms: 1.05x slower                                       |
| logging_simple             | 5.96 us                                                     | 6.28 us: 1.05x slower                                       |
| xml_etree_iterparse        | 61.8 ms                                                     | 65.2 ms: 1.05x slower                                       |
| docutils                   | 1.57 sec                                                    | 1.66 sec: 1.06x slower                                      |
| spectral_norm              | 62.8 ms                                                     | 66.9 ms: 1.07x slower                                       |
| crypto_pyaes               | 45.4 ms                                                     | 48.5 ms: 1.07x slower                                       |
| sqlglot_transpile          | 956 us                                                      | 1.02 ms: 1.07x slower                                       |
| sqlglot_normalize          | 175 ms                                                      | 187 ms: 1.07x slower                                        |
| scimark_fft                | 172 ms                                                      | 184 ms: 1.07x slower                                        |
| scimark_monte_carlo        | 40.8 ms                                                     | 43.7 ms: 1.07x slower                                       |
| async_generators           | 223 ms                                                      | 239 ms: 1.07x slower                                        |
| logging_format             | 6.26 us                                                     | 6.72 us: 1.07x slower                                       |
| dulwich_log                | 40.8 ms                                                     | 44.3 ms: 1.08x slower                                       |
| regex_compile              | 80.5 ms                                                     | 87.5 ms: 1.09x slower                                       |
| sqlalchemy_declarative     | 79.2 ms                                                     | 86.4 ms: 1.09x slower                                       |
| regex_dna                  | 115 ms                                                      | 126 ms: 1.10x slower                                        |
| logging_silent             | 54.6 ns                                                     | 60.5 ns: 1.11x slower                                       |
| nqueens                    | 56.7 ms                                                     | 62.8 ms: 1.11x slower                                       |
| scimark_lu                 | 53.0 ms                                                     | 58.9 ms: 1.11x slower                                       |
| mako                       | 6.35 ms                                                     | 7.09 ms: 1.12x slower                                       |
| coroutines                 | 12.8 ms                                                     | 14.3 ms: 1.12x slower                                       |
| chaos                      | 38.5 ms                                                     | 43.3 ms: 1.12x slower                                       |
| deltablue                  | 1.92 ms                                                     | 2.16 ms: 1.13x slower                                       |
| float                      | 49.9 ms                                                     | 56.8 ms: 1.14x slower                                       |
| generators                 | 19.5 ms                                                     | 22.5 ms: 1.16x slower                                       |
| raytrace                   | 160 ms                                                      | 192 ms: 1.20x slower                                        |
| async_tree_memoization     | 276 ms                                                      | 339 ms: 1.23x slower                                        |
| async_tree_memoization_tg  | 288 ms                                                      | 367 ms: 1.27x slower                                        |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 489 ms: 1.28x slower                                        |
| async_tree_none            | 226 ms                                                      | 291 ms: 1.29x slower                                        |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 502 ms: 1.33x slower                                        |
| async_tree_none_tg         | 209 ms                                                      | 285 ms: 1.37x slower                                        |
| comprehensions             | 10.3 us                                                     | 14.1 us: 1.38x slower                                       |
| async_tree_io              | 521 ms                                                      | 731 ms: 1.40x slower                                        |
| async_tree_io_tg           | 518 ms                                                      | 771 ms: 1.49x slower                                        |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                |

Benchmark hidden because not significant (4): xml_etree_parse, pathlib, unpickle_pure_python, bench_thread_pool
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, pylint, shortest_path, sphinx, thrift
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.039x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown