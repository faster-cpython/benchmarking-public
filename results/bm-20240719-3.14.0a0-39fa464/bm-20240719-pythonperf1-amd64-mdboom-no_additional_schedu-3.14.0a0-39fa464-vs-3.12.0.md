# Results vs. 3.12.0

- fork: mdboom
- ref: no_additional_schedu
- machine: windows-amd64
- commit hash: 39fa464
- commit date: 2024-07-19
- overall geometric mean: 1.05x faster
- HPT reliability: 99.81%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-39fa464 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tornado_http   | 89.5 ms                                                     | 91.5 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (2): 2to3, docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-39fa464 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 187 ms: 1.53x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 243 ms: 1.51x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 521 ms: 1.48x faster                                                       |
| async_tree_none            | 291 ms                                                      | 208 ms: 1.40x faster                                                       |
| async_tree_io              | 731 ms                                                      | 527 ms: 1.39x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 252 ms: 1.34x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 381 ms: 1.32x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 380 ms: 1.29x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.40x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-39fa464 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 54.0 ms: 1.05x faster                                                      |
| nbody          | 71.9 ms                                                     | 68.8 ms: 1.04x faster                                                      |
| pidigits       | 152 ms                                                      | 150 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.04x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-39fa464 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 120 ms: 1.06x faster                                                       |
| regex_compile  | 87.5 ms                                                     | 83.8 ms: 1.04x faster                                                      |
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 15.5 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-39fa464 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 63.6 ms: 1.02x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 55.2 ms: 1.01x faster                                                      |
| unpickle_pure_python | 133 us                                                      | 134 us: 1.01x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 38.0 ms: 1.01x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 198 us: 1.01x slower                                                       |
| json_loads           | 13.9 us                                                     | 14.1 us: 1.02x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 5.87 ms: 1.03x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.46 sec: 1.07x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-39fa464 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.0 ms: 1.11x slower                                                      |
| python_startup         | 19.5 ms                                                     | 21.7 ms: 1.12x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-39fa464 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako           | 7.09 ms                                                     | 6.88 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-39fa464 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 187 ms: 1.53x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 243 ms: 1.51x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 521 ms: 1.48x faster                                                       |
| async_tree_none            | 291 ms                                                      | 208 ms: 1.40x faster                                                       |
| async_tree_io              | 731 ms                                                      | 527 ms: 1.39x faster                                                       |
| deepcopy                   | 238 us                                                      | 174 us: 1.37x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 252 ms: 1.34x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 381 ms: 1.32x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 380 ms: 1.29x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.0 us: 1.28x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 18.9 us: 1.26x faster                                                      |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.74 sec: 1.20x faster                                                     |
| deepcopy_reduce            | 2.09 us                                                     | 1.78 us: 1.17x faster                                                      |
| raytrace                   | 192 ms                                                      | 164 ms: 1.17x faster                                                       |
| generators                 | 22.5 ms                                                     | 19.6 ms: 1.15x faster                                                      |
| deltablue                  | 2.16 ms                                                     | 1.95 ms: 1.11x faster                                                      |
| chaos                      | 43.3 ms                                                     | 39.3 ms: 1.10x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 57.4 ms: 1.09x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 13.1 ms: 1.09x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 791 us: 1.08x faster                                                       |
| regex_dna                  | 126 ms                                                      | 120 ms: 1.06x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 45.9 ms: 1.06x faster                                                      |
| logging_simple             | 6.28 us                                                     | 5.95 us: 1.05x faster                                                      |
| float                      | 56.8 ms                                                     | 54.0 ms: 1.05x faster                                                      |
| scimark_lu                 | 58.9 ms                                                     | 56.0 ms: 1.05x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.40 us: 1.05x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 87.5 ms: 1.05x faster                                                      |
| sqlglot_normalize          | 187 ms                                                      | 179 ms: 1.04x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 83.8 ms: 1.04x faster                                                      |
| nbody                      | 71.9 ms                                                     | 68.8 ms: 1.04x faster                                                      |
| hexiom                     | 4.10 ms                                                     | 3.93 ms: 1.04x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 58.2 ns: 1.04x faster                                                      |
| go                         | 91.6 ms                                                     | 88.7 ms: 1.03x faster                                                      |
| mako                       | 7.09 ms                                                     | 6.88 ms: 1.03x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| sympy_str                  | 175 ms                                                      | 171 ms: 1.03x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.6 ms: 1.02x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.6 ms: 1.02x faster                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 33.7 ms: 1.02x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 65.4 ms: 1.02x faster                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 67.8 ms: 1.02x faster                                                      |
| async_generators           | 239 ms                                                      | 235 ms: 1.02x faster                                                       |
| json                       | 3.05 ms                                                     | 3.00 ms: 1.02x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 73.4 ms: 1.02x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.52 ms: 1.02x faster                                                      |
| pidigits                   | 152 ms                                                      | 150 ms: 1.01x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 55.2 ms: 1.01x faster                                                      |
| pyflate                    | 295 ms                                                      | 293 ms: 1.01x faster                                                       |
| unpickle_pure_python       | 133 us                                                      | 134 us: 1.01x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 38.0 ms: 1.01x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.39 sec: 1.01x slower                                                     |
| scimark_monte_carlo        | 43.7 ms                                                     | 44.2 ms: 1.01x slower                                                      |
| scimark_fft                | 184 ms                                                      | 187 ms: 1.01x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 198 us: 1.01x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.04 ms: 1.02x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.1 us: 1.02x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.55 ms: 1.02x slower                                                      |
| tornado_http               | 89.5 ms                                                     | 91.5 ms: 1.02x slower                                                      |
| sympy_expand               | 284 ms                                                      | 292 ms: 1.03x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 5.87 ms: 1.03x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.08 sec: 1.03x slower                                                     |
| sqlglot_parse              | 804 us                                                      | 830 us: 1.03x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 535 ms: 1.04x slower                                                       |
| pycparser                  | 699 ms                                                      | 738 ms: 1.06x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.46 sec: 1.07x slower                                                     |
| asyncio_tcp                | 487 ms                                                      | 525 ms: 1.08x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 15.5 ms: 1.09x slower                                                      |
| fannkuch                   | 247 ms                                                      | 269 ms: 1.09x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 18.0 ms: 1.11x slower                                                      |
| python_startup             | 19.5 ms                                                     | 21.7 ms: 1.12x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 107 us: 1.13x slower                                                       |
| coverage                   | 40.8 ms                                                     | 46.5 ms: 1.14x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.74 ms: 1.15x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 905 us: 1.20x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (8): richards, pathlib, richards_super, django_template, 2to3, xml_etree_parse, scimark_sor, docutils
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240719-3.14.0a0-39fa464/bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-39fa464.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.81% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown