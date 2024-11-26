# Results vs. 3.12.0

- fork: python
- ref: v3.13.0
- machine: windows-amd64
- commit hash: 60403a5
- commit date: 2024-10-07
- overall geometric mean: 1.046x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 221 ms: 1.01x slower                                        |
| chameleon      | 4.98 ms                                                     | 4.82 ms: 1.03x faster                                       |
| docutils       | 1.66 sec                                                    | 1.57 sec: 1.06x faster                                      |
| tornado_http   | 89.5 ms                                                     | 93.0 ms: 1.04x slower                                       |
| Geometric mean | (ref)                                                       | 1.01x faster                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 518 ms: 1.49x faster                                        |
| async_tree_io              | 731 ms                                                      | 521 ms: 1.40x faster                                        |
| async_tree_none_tg         | 285 ms                                                      | 209 ms: 1.37x faster                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 377 ms: 1.33x faster                                        |
| async_tree_none            | 291 ms                                                      | 226 ms: 1.29x faster                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 383 ms: 1.28x faster                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 288 ms: 1.27x faster                                        |
| async_tree_memoization     | 339 ms                                                      | 276 ms: 1.23x faster                                        |
| Geometric mean             | (ref)                                                       | 1.33x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 56.8 ms                                                     | 49.9 ms: 1.14x faster                                       |
| nbody          | 71.9 ms                                                     | 68.4 ms: 1.05x faster                                       |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                        |
| Geometric mean | (ref)                                                       | 1.07x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 115 ms: 1.10x faster                                        |
| regex_compile  | 87.5 ms                                                     | 80.5 ms: 1.09x faster                                       |
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.03x faster                                       |
| regex_v8       | 14.2 ms                                                     | 21.4 ms: 1.50x slower                                       |
| Geometric mean | (ref)                                                       | 1.05x slower                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|---------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| xml_etree_iterparse | 65.2 ms                                                     | 61.8 ms: 1.05x faster                                       |
| xml_etree_generate  | 55.8 ms                                                     | 54.0 ms: 1.03x faster                                       |
| pickle_pure_python  | 195 us                                                      | 190 us: 1.03x faster                                        |
| xml_etree_process   | 37.7 ms                                                     | 37.0 ms: 1.02x faster                                       |
| tomli_loads         | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                      |
| json_dumps          | 5.70 ms                                                     | 5.92 ms: 1.04x slower                                       |
| json_loads          | 13.9 us                                                     | 15.1 us: 1.09x slower                                       |
| Geometric mean      | (ref)                                                       | 1.00x slower                                                |

Benchmark hidden because not significant (2): unpickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.1 ms: 1.12x slower                                       |
| python_startup         | 19.5 ms                                                     | 25.4 ms: 1.31x slower                                       |
| Geometric mean         | (ref)                                                       | 1.21x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.35 ms: 1.12x faster                                       |
| django_template | 22.9 ms                                                     | 22.4 ms: 1.03x faster                                       |
| Geometric mean  | (ref)                                                       | 1.07x faster                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 518 ms: 1.49x faster                                        |
| async_tree_io              | 731 ms                                                      | 521 ms: 1.40x faster                                        |
| comprehensions             | 14.1 us                                                     | 10.3 us: 1.38x faster                                       |
| async_tree_none_tg         | 285 ms                                                      | 209 ms: 1.37x faster                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 377 ms: 1.33x faster                                        |
| async_tree_none            | 291 ms                                                      | 226 ms: 1.29x faster                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 383 ms: 1.28x faster                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 288 ms: 1.27x faster                                        |
| async_tree_memoization     | 339 ms                                                      | 276 ms: 1.23x faster                                        |
| raytrace                   | 192 ms                                                      | 160 ms: 1.20x faster                                        |
| generators                 | 22.5 ms                                                     | 19.5 ms: 1.16x faster                                       |
| float                      | 56.8 ms                                                     | 49.9 ms: 1.14x faster                                       |
| deltablue                  | 2.16 ms                                                     | 1.92 ms: 1.13x faster                                       |
| chaos                      | 43.3 ms                                                     | 38.5 ms: 1.12x faster                                       |
| coroutines                 | 14.3 ms                                                     | 12.8 ms: 1.12x faster                                       |
| mako                       | 7.09 ms                                                     | 6.35 ms: 1.12x faster                                       |
| scimark_lu                 | 58.9 ms                                                     | 53.0 ms: 1.11x faster                                       |
| nqueens                    | 62.8 ms                                                     | 56.7 ms: 1.11x faster                                       |
| logging_silent             | 60.5 ns                                                     | 54.6 ns: 1.11x faster                                       |
| regex_dna                  | 126 ms                                                      | 115 ms: 1.10x faster                                        |
| sqlalchemy_declarative     | 86.4 ms                                                     | 79.2 ms: 1.09x faster                                       |
| regex_compile              | 87.5 ms                                                     | 80.5 ms: 1.09x faster                                       |
| dulwich_log                | 44.3 ms                                                     | 40.8 ms: 1.08x faster                                       |
| logging_format             | 6.72 us                                                     | 6.26 us: 1.07x faster                                       |
| async_generators           | 239 ms                                                      | 223 ms: 1.07x faster                                        |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.8 ms: 1.07x faster                                       |
| scimark_fft                | 184 ms                                                      | 172 ms: 1.07x faster                                        |
| sqlglot_normalize          | 187 ms                                                      | 175 ms: 1.07x faster                                        |
| sqlglot_transpile          | 1.02 ms                                                     | 956 us: 1.07x faster                                        |
| crypto_pyaes               | 48.5 ms                                                     | 45.4 ms: 1.07x faster                                       |
| spectral_norm              | 66.9 ms                                                     | 62.8 ms: 1.07x faster                                       |
| docutils                   | 1.66 sec                                                    | 1.57 sec: 1.06x faster                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.8 ms: 1.05x faster                                       |
| logging_simple             | 6.28 us                                                     | 5.96 us: 1.05x faster                                       |
| hexiom                     | 4.10 ms                                                     | 3.89 ms: 1.05x faster                                       |
| sympy_sum                  | 91.5 ms                                                     | 86.9 ms: 1.05x faster                                       |
| go                         | 91.6 ms                                                     | 87.0 ms: 1.05x faster                                       |
| deepcopy                   | 238 us                                                      | 226 us: 1.05x faster                                        |
| nbody                      | 71.9 ms                                                     | 68.4 ms: 1.05x faster                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 32.9 ms: 1.05x faster                                       |
| pprint_pformat             | 1.05 sec                                                    | 999 ms: 1.05x faster                                        |
| sqlglot_parse              | 804 us                                                      | 771 us: 1.04x faster                                        |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.46 ms: 1.04x faster                                       |
| pyflate                    | 295 ms                                                      | 283 ms: 1.04x faster                                        |
| pprint_safe_repr           | 513 ms                                                      | 494 ms: 1.04x faster                                        |
| richards_super             | 32.1 ms                                                     | 30.9 ms: 1.04x faster                                       |
| richards                   | 28.4 ms                                                     | 27.3 ms: 1.04x faster                                       |
| sympy_str                  | 175 ms                                                      | 169 ms: 1.04x faster                                        |
| sympy_integrate            | 13.0 ms                                                     | 12.5 ms: 1.04x faster                                       |
| scimark_sor                | 78.8 ms                                                     | 76.2 ms: 1.03x faster                                       |
| xml_etree_generate         | 55.8 ms                                                     | 54.0 ms: 1.03x faster                                       |
| chameleon                  | 4.98 ms                                                     | 4.82 ms: 1.03x faster                                       |
| pickle_pure_python         | 195 us                                                      | 190 us: 1.03x faster                                        |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                        |
| regex_effbot               | 1.62 ms                                                     | 1.58 ms: 1.03x faster                                       |
| django_template            | 22.9 ms                                                     | 22.4 ms: 1.03x faster                                       |
| pycparser                  | 699 ms                                                      | 683 ms: 1.02x faster                                        |
| xml_etree_process          | 37.7 ms                                                     | 37.0 ms: 1.02x faster                                       |
| deepcopy_memo              | 23.7 us                                                     | 23.3 us: 1.02x faster                                       |
| deepcopy_reduce            | 2.09 us                                                     | 2.06 us: 1.02x faster                                       |
| meteor_contest             | 74.6 ms                                                     | 73.5 ms: 1.01x faster                                       |
| mdp                        | 1.37 sec                                                    | 1.39 sec: 1.01x slower                                      |
| 2to3                       | 218 ms                                                      | 221 ms: 1.01x slower                                        |
| tomli_loads                | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                      |
| sympy_expand               | 284 ms                                                      | 291 ms: 1.03x slower                                        |
| fannkuch                   | 247 ms                                                      | 253 ms: 1.03x slower                                        |
| json_dumps                 | 5.70 ms                                                     | 5.92 ms: 1.04x slower                                       |
| tornado_http               | 89.5 ms                                                     | 93.0 ms: 1.04x slower                                       |
| sqlalchemy_imperative      | 9.29 ms                                                     | 9.69 ms: 1.04x slower                                       |
| json                       | 3.05 ms                                                     | 3.19 ms: 1.05x slower                                       |
| json_loads                 | 13.9 us                                                     | 15.1 us: 1.09x slower                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 105 us: 1.11x slower                                        |
| coverage                   | 40.8 ms                                                     | 45.6 ms: 1.12x slower                                       |
| python_startup_no_site     | 16.2 ms                                                     | 18.1 ms: 1.12x slower                                       |
| telco                      | 4.13 ms                                                     | 4.79 ms: 1.16x slower                                       |
| bench_mp_pool              | 69.2 ms                                                     | 86.4 ms: 1.25x slower                                       |
| gc_traversal               | 1.52 ms                                                     | 1.97 ms: 1.29x slower                                       |
| python_startup             | 19.5 ms                                                     | 25.4 ms: 1.31x slower                                       |
| mypy2                      | 509 ms                                                      | 679 ms: 1.33x slower                                        |
| regex_v8                   | 14.2 ms                                                     | 21.4 ms: 1.50x slower                                       |
| create_gc_cycles           | 752 us                                                      | 1.26 ms: 1.67x slower                                       |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                |

Benchmark hidden because not significant (4): bench_thread_pool, unpickle_pure_python, pathlib, xml_etree_parse
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.046x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown