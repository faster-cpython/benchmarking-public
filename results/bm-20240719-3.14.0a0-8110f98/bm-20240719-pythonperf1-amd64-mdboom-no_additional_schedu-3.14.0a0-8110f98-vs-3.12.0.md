# Results vs. 3.12.0

- fork: mdboom
- ref: no_additional_schedu
- machine: windows-amd64
- commit hash: 8110f98
- commit date: 2024-07-19
- overall geometric mean: 1.02x faster
- HPT reliability: 76.41%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-8110f98 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 222 ms: 1.02x slower                                                       |
| tornado_http   | 89.5 ms                                                     | 91.4 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-8110f98 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 247 ms: 1.49x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 194 ms: 1.47x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 535 ms: 1.44x faster                                                       |
| async_tree_none            | 291 ms                                                      | 213 ms: 1.37x faster                                                       |
| async_tree_io              | 731 ms                                                      | 538 ms: 1.36x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 258 ms: 1.31x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 387 ms: 1.30x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 382 ms: 1.28x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.38x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-8110f98 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 56.0 ms: 1.01x faster                                                      |
| pidigits       | 152 ms                                                      | 150 ms: 1.01x faster                                                       |
| nbody          | 71.9 ms                                                     | 75.5 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-8110f98 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 83.3 ms: 1.05x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 15.4 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-8110f98 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 93.8 ms: 1.01x slower                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 66.2 ms: 1.02x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 199 us: 1.02x slower                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 57.5 ms: 1.03x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.5 us: 1.04x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 5.95 ms: 1.04x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 39.9 ms: 1.06x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 145 us: 1.09x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.58 sec: 1.15x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-8110f98 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.7 ms: 1.09x slower                                                      |
| python_startup         | 19.5 ms                                                     | 21.5 ms: 1.11x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-8110f98 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 24.3 ms: 1.06x slower                                                      |
| mako            | 7.09 ms                                                     | 7.54 ms: 1.06x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.06x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-8110f98 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 247 ms: 1.49x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 194 ms: 1.47x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 535 ms: 1.44x faster                                                       |
| async_tree_none            | 291 ms                                                      | 213 ms: 1.37x faster                                                       |
| async_tree_io              | 731 ms                                                      | 538 ms: 1.36x faster                                                       |
| deepcopy                   | 238 us                                                      | 178 us: 1.34x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 258 ms: 1.31x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.60 sec: 1.31x faster                                                     |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 387 ms: 1.30x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 382 ms: 1.28x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.5 us: 1.22x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 20.3 us: 1.17x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.82 us: 1.15x faster                                                      |
| raytrace                   | 192 ms                                                      | 173 ms: 1.11x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 86.9 ms: 1.05x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 815 us: 1.05x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 83.3 ms: 1.05x faster                                                      |
| generators                 | 22.5 ms                                                     | 21.7 ms: 1.04x faster                                                      |
| deltablue                  | 2.16 ms                                                     | 2.08 ms: 1.04x faster                                                      |
| sympy_str                  | 175 ms                                                      | 169 ms: 1.04x faster                                                       |
| chaos                      | 43.3 ms                                                     | 41.9 ms: 1.03x faster                                                      |
| go                         | 91.6 ms                                                     | 89.2 ms: 1.03x faster                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 67.4 ms: 1.03x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 61.2 ms: 1.03x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 14.0 ms: 1.02x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.8 ms: 1.01x faster                                                      |
| float                      | 56.8 ms                                                     | 56.0 ms: 1.01x faster                                                      |
| pidigits                   | 152 ms                                                      | 150 ms: 1.01x faster                                                       |
| logging_simple             | 6.28 us                                                     | 6.20 us: 1.01x faster                                                      |
| sqlglot_normalize          | 187 ms                                                      | 185 ms: 1.01x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.66 us: 1.01x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 60.6 ns: 1.00x slower                                                      |
| richards                   | 28.4 ms                                                     | 28.5 ms: 1.01x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.13 ms: 1.01x slower                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 93.8 ms: 1.01x slower                                                      |
| sympy_expand               | 284 ms                                                      | 288 ms: 1.01x slower                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 66.2 ms: 1.02x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 199 us: 1.02x slower                                                       |
| async_generators           | 239 ms                                                      | 244 ms: 1.02x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.40 sec: 1.02x slower                                                     |
| 2to3                       | 218 ms                                                      | 222 ms: 1.02x slower                                                       |
| tornado_http               | 89.5 ms                                                     | 91.4 ms: 1.02x slower                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 49.5 ms: 1.02x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.56 ms: 1.02x slower                                                      |
| pyflate                    | 295 ms                                                      | 302 ms: 1.03x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 76.8 ms: 1.03x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 57.5 ms: 1.03x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.5 us: 1.04x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.09 sec: 1.04x slower                                                     |
| pprint_safe_repr           | 513 ms                                                      | 534 ms: 1.04x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 5.95 ms: 1.04x slower                                                      |
| nbody                      | 71.9 ms                                                     | 75.5 ms: 1.05x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.08 ms: 1.05x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 62.2 ms: 1.06x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 39.9 ms: 1.06x slower                                                      |
| django_template            | 22.9 ms                                                     | 24.3 ms: 1.06x slower                                                      |
| mako                       | 7.09 ms                                                     | 7.54 ms: 1.06x slower                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 46.6 ms: 1.07x slower                                                      |
| sqlglot_parse              | 804 us                                                      | 861 us: 1.07x slower                                                       |
| asyncio_tcp                | 487 ms                                                      | 522 ms: 1.07x slower                                                       |
| pycparser                  | 699 ms                                                      | 755 ms: 1.08x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 15.4 ms: 1.08x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 17.7 ms: 1.09x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 145 us: 1.09x slower                                                       |
| scimark_fft                | 184 ms                                                      | 204 ms: 1.11x slower                                                       |
| python_startup             | 19.5 ms                                                     | 21.5 ms: 1.11x slower                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.86 ms: 1.12x slower                                                      |
| coverage                   | 40.8 ms                                                     | 46.4 ms: 1.14x slower                                                      |
| fannkuch                   | 247 ms                                                      | 282 ms: 1.14x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.58 sec: 1.15x slower                                                     |
| telco                      | 4.13 ms                                                     | 4.79 ms: 1.16x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 111 us: 1.16x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 890 us: 1.18x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (9): richards_super, spectral_norm, docutils, json, scimark_sor, pathlib, sqlglot_optimize, regex_effbot, regex_dna
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240719-3.14.0a0-8110f98/bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-8110f98.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 76.41% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown