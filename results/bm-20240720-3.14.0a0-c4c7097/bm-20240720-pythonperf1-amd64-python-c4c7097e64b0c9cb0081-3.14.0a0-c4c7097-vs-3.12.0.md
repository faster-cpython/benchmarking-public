# Results vs. 3.12.0

- fork: python
- ref: c4c7097e64b0c9cb0081
- machine: windows-amd64
- commit hash: c4c7097
- commit date: 2024-07-20
- overall geometric mean: 1.02x faster
- HPT reliability: 63.69%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 223 ms: 1.02x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.68 sec: 1.01x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 91.3 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 245 ms: 1.50x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 196 ms: 1.46x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 541 ms: 1.42x faster                                                       |
| async_tree_none            | 291 ms                                                      | 216 ms: 1.35x faster                                                       |
| async_tree_io              | 731 ms                                                      | 556 ms: 1.31x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 386 ms: 1.30x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 261 ms: 1.30x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 391 ms: 1.25x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.36x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 55.4 ms: 1.03x faster                                                      |
| pidigits       | 152 ms                                                      | 150 ms: 1.02x faster                                                       |
| nbody          | 71.9 ms                                                     | 77.3 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 86.8 ms: 1.01x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 16.4 ms: 1.15x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (2): regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_generate   | 55.8 ms                                                     | 56.5 ms: 1.01x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 199 us: 1.02x slower                                                       |
| json_loads           | 13.9 us                                                     | 14.3 us: 1.03x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 5.92 ms: 1.04x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 39.3 ms: 1.04x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 141 us: 1.06x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.51 sec: 1.10x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.6 ms: 1.08x slower                                                      |
| python_startup         | 19.5 ms                                                     | 21.4 ms: 1.10x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.09x slower                                                               |

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 245 ms: 1.50x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 196 ms: 1.46x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 541 ms: 1.42x faster                                                       |
| deepcopy                   | 238 us                                                      | 175 us: 1.36x faster                                                       |
| async_tree_none            | 291 ms                                                      | 216 ms: 1.35x faster                                                       |
| async_tree_io              | 731 ms                                                      | 556 ms: 1.31x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 386 ms: 1.30x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 261 ms: 1.30x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.1 us: 1.28x faster                                                      |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.64 sec: 1.27x faster                                                     |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 391 ms: 1.25x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 19.6 us: 1.21x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.81 us: 1.16x faster                                                      |
| raytrace                   | 192 ms                                                      | 169 ms: 1.14x faster                                                       |
| generators                 | 22.5 ms                                                     | 20.9 ms: 1.08x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 799 us: 1.07x faster                                                       |
| chaos                      | 43.3 ms                                                     | 41.1 ms: 1.05x faster                                                      |
| logging_simple             | 6.28 us                                                     | 5.99 us: 1.05x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 13.6 ms: 1.05x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 57.9 ns: 1.04x faster                                                      |
| deltablue                  | 2.16 ms                                                     | 2.07 ms: 1.04x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 60.2 ms: 1.04x faster                                                      |
| sqlglot_normalize          | 187 ms                                                      | 180 ms: 1.04x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.48 us: 1.04x faster                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 67.1 ms: 1.03x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 89.0 ms: 1.03x faster                                                      |
| float                      | 56.8 ms                                                     | 55.4 ms: 1.03x faster                                                      |
| sympy_str                  | 175 ms                                                      | 172 ms: 1.02x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 73.3 ms: 1.02x faster                                                      |
| pidigits                   | 152 ms                                                      | 150 ms: 1.02x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 12.8 ms: 1.01x faster                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 34.2 ms: 1.01x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 86.8 ms: 1.01x faster                                                      |
| go                         | 91.6 ms                                                     | 91.0 ms: 1.01x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 48.9 ms: 1.01x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 56.5 ms: 1.01x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.68 sec: 1.01x slower                                                     |
| richards                   | 28.4 ms                                                     | 28.9 ms: 1.02x slower                                                      |
| tornado_http               | 89.5 ms                                                     | 91.3 ms: 1.02x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 199 us: 1.02x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 524 ms: 1.02x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.56 ms: 1.02x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.07 sec: 1.02x slower                                                     |
| 2to3                       | 218 ms                                                      | 223 ms: 1.02x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 60.3 ms: 1.02x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.3 us: 1.03x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.05 ms: 1.03x slower                                                      |
| richards_super             | 32.1 ms                                                     | 33.0 ms: 1.03x slower                                                      |
| pyflate                    | 295 ms                                                      | 304 ms: 1.03x slower                                                       |
| spectral_norm              | 66.9 ms                                                     | 69.5 ms: 1.04x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 5.92 ms: 1.04x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 39.3 ms: 1.04x slower                                                      |
| sympy_expand               | 284 ms                                                      | 298 ms: 1.05x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 847 us: 1.05x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 141 us: 1.06x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.72 ms: 1.06x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.47 sec: 1.07x slower                                                     |
| scimark_fft                | 184 ms                                                      | 198 ms: 1.07x slower                                                       |
| nbody                      | 71.9 ms                                                     | 77.3 ms: 1.07x slower                                                      |
| asyncio_tcp                | 487 ms                                                      | 524 ms: 1.08x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 17.6 ms: 1.08x slower                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 47.9 ms: 1.10x slower                                                      |
| pycparser                  | 699 ms                                                      | 766 ms: 1.10x slower                                                       |
| python_startup             | 19.5 ms                                                     | 21.4 ms: 1.10x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 86.8 ms: 1.10x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.51 sec: 1.10x slower                                                     |
| typing_runtime_protocols   | 95.1 us                                                     | 105 us: 1.10x slower                                                       |
| fannkuch                   | 247 ms                                                      | 280 ms: 1.13x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 16.4 ms: 1.15x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.81 ms: 1.17x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 903 us: 1.20x slower                                                       |
| coverage                   | 40.8 ms                                                     | 79.8 ms: 1.95x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (10): xml_etree_iterparse, xml_etree_parse, pathlib, regex_dna, regex_effbot, async_generators, django_template, mako, json, hexiom
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240720-3.14.0a0-c4c7097/bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 63.69% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown