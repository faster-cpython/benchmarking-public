# Results vs. 3.12.0

- fork: python
- ref: c4c7097e64b0c9cb0081
- machine: windows-amd64
- commit hash: c4c7097
- commit date: 2024-07-20
- overall geometric mean: 1.08x faster
- HPT reliability: 96.21%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 235 ms: 1.08x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.79 sec: 1.08x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 93.8 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                       | 1.07x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 186 ms: 1.54x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 244 ms: 1.50x faster                                                       |
| async_tree_none            | 291 ms                                                      | 199 ms: 1.46x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 528 ms: 1.46x faster                                                       |
| async_tree_io              | 731 ms                                                      | 521 ms: 1.40x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 251 ms: 1.35x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 381 ms: 1.32x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 382 ms: 1.28x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.41x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 50.1 ms: 1.43x faster                                                      |
| float          | 56.8 ms                                                     | 44.2 ms: 1.28x faster                                                      |
| pidigits       | 152 ms                                                      | 150 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.23x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 122 ms: 1.04x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.61 ms: 1.01x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 14.8 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 176 us: 1.11x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.23 sec: 1.11x faster                                                     |
| xml_etree_generate   | 55.8 ms                                                     | 51.2 ms: 1.09x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 62.2 ms: 1.05x faster                                                      |
| unpickle_pure_python | 133 us                                                      | 128 us: 1.04x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 36.3 ms: 1.04x faster                                                      |
| json_dumps           | 5.70 ms                                                     | 5.73 ms: 1.01x slower                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 93.8 ms: 1.01x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.3 us: 1.03x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 19.5 ms                                                     | 21.7 ms: 1.11x slower                                                      |
| python_startup_no_site | 16.2 ms                                                     | 18.2 ms: 1.12x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.26 ms: 1.35x faster                                                      |
| django_template | 22.9 ms                                                     | 25.3 ms: 1.10x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.11x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 186 ms: 1.54x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 15.6 us: 1.52x faster                                                      |
| async_tree_memoization_tg  | 367 ms                                                      | 244 ms: 1.50x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.42 sec: 1.47x faster                                                     |
| async_tree_none            | 291 ms                                                      | 199 ms: 1.46x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 528 ms: 1.46x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 46.1 ms: 1.45x faster                                                      |
| nbody                      | 71.9 ms                                                     | 50.1 ms: 1.43x faster                                                      |
| async_tree_io              | 731 ms                                                      | 521 ms: 1.40x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.1 us: 1.39x faster                                                      |
| async_tree_memoization     | 339 ms                                                      | 251 ms: 1.35x faster                                                       |
| mako                       | 7.09 ms                                                     | 5.26 ms: 1.35x faster                                                      |
| deepcopy                   | 238 us                                                      | 179 us: 1.33x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 381 ms: 1.32x faster                                                       |
| float                      | 56.8 ms                                                     | 44.2 ms: 1.28x faster                                                      |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 382 ms: 1.28x faster                                                       |
| scimark_fft                | 184 ms                                                      | 147 ms: 1.25x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.08 ms: 1.23x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 39.8 ms: 1.22x faster                                                      |
| pyflate                    | 295 ms                                                      | 245 ms: 1.20x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.78 us: 1.18x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 37.9 ms: 1.16x faster                                                      |
| fannkuch                   | 247 ms                                                      | 220 ms: 1.12x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 461 ms: 1.11x faster                                                       |
| pickle_pure_python         | 195 us                                                      | 176 us: 1.11x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.23 sec: 1.11x faster                                                     |
| pprint_pformat             | 1.05 sec                                                    | 944 ms: 1.11x faster                                                       |
| chaos                      | 43.3 ms                                                     | 39.2 ms: 1.11x faster                                                      |
| raytrace                   | 192 ms                                                      | 174 ms: 1.10x faster                                                       |
| logging_simple             | 6.28 us                                                     | 5.69 us: 1.10x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 55.0 ns: 1.10x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 51.2 ms: 1.09x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.17 us: 1.09x faster                                                      |
| generators                 | 22.5 ms                                                     | 21.1 ms: 1.07x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 70.2 ms: 1.06x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 807 us: 1.06x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.5 ms: 1.06x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 59.7 ms: 1.05x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.2 ms: 1.05x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 128 us: 1.04x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 36.3 ms: 1.04x faster                                                      |
| regex_dna                  | 126 ms                                                      | 122 ms: 1.04x faster                                                       |
| pidigits                   | 152 ms                                                      | 150 ms: 1.01x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.61 ms: 1.01x faster                                                      |
| sqlglot_parse              | 804 us                                                      | 808 us: 1.01x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 5.73 ms: 1.01x slower                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 93.8 ms: 1.01x slower                                                      |
| richards_super             | 32.1 ms                                                     | 32.4 ms: 1.01x slower                                                      |
| sqlglot_normalize          | 187 ms                                                      | 189 ms: 1.01x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.03 ms: 1.01x slower                                                      |
| richards                   | 28.4 ms                                                     | 28.8 ms: 1.01x slower                                                      |
| go                         | 91.6 ms                                                     | 93.3 ms: 1.02x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.22 ms: 1.03x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 71.1 ms: 1.03x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.56 ms: 1.03x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.3 us: 1.03x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 35.5 ms: 1.03x slower                                                      |
| sympy_sum                  | 91.5 ms                                                     | 94.4 ms: 1.03x slower                                                      |
| sympy_str                  | 175 ms                                                      | 181 ms: 1.03x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 14.8 ms: 1.04x slower                                                      |
| pycparser                  | 699 ms                                                      | 732 ms: 1.05x slower                                                       |
| tornado_http               | 89.5 ms                                                     | 93.8 ms: 1.05x slower                                                      |
| async_generators           | 239 ms                                                      | 253 ms: 1.06x slower                                                       |
| asyncio_tcp                | 487 ms                                                      | 518 ms: 1.06x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.46 sec: 1.06x slower                                                     |
| docutils                   | 1.66 sec                                                    | 1.79 sec: 1.08x slower                                                     |
| telco                      | 4.13 ms                                                     | 4.45 ms: 1.08x slower                                                      |
| 2to3                       | 218 ms                                                      | 235 ms: 1.08x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 14.1 ms: 1.09x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 86.1 ms: 1.09x slower                                                      |
| django_template            | 22.9 ms                                                     | 25.3 ms: 1.10x slower                                                      |
| sympy_expand               | 284 ms                                                      | 316 ms: 1.11x slower                                                       |
| python_startup             | 19.5 ms                                                     | 21.7 ms: 1.11x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 18.2 ms: 1.12x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.60 ms: 1.12x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 67.7 ms: 1.15x slower                                                      |
| coverage                   | 40.8 ms                                                     | 47.2 ms: 1.16x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 113 us: 1.19x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 906 us: 1.20x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.08x faster                                                               |

Benchmark hidden because not significant (3): json, regex_compile, pathlib
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240720-3.14.0a0-c4c7097-JIT/bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 96.21% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown