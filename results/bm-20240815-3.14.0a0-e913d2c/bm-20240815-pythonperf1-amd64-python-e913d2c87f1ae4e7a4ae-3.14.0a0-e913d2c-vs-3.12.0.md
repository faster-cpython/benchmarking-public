# Results vs. 3.12.0

- fork: python
- ref: e913d2c87f1ae4e7a4ae
- machine: windows-amd64
- commit hash: e913d2c
- commit date: 2024-08-15
- overall geometric mean: 1.012x slower
- HPT reliability: 99.83%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 231 ms: 1.06x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.75 sec: 1.05x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 93.2 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 250 ms: 1.47x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 198 ms: 1.44x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 547 ms: 1.41x faster                                                       |
| async_tree_none            | 291 ms                                                      | 219 ms: 1.33x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 266 ms: 1.28x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 395 ms: 1.27x faster                                                       |
| async_tree_io              | 731 ms                                                      | 577 ms: 1.27x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 391 ms: 1.25x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.34x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 152 ms                                                      | 151 ms: 1.01x faster                                                       |
| nbody          | 71.9 ms                                                     | 82.3 ms: 1.15x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 118 ms: 1.07x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 91.7 ms: 1.05x slower                                                      |
| regex_v8       | 14.2 ms                                                     | 16.5 ms: 1.16x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 65.8 ms: 1.01x slower                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 94.6 ms: 1.02x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.2 us: 1.02x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 57.8 ms: 1.04x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 211 us: 1.08x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 41.2 ms: 1.09x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.22 ms: 1.09x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 148 us: 1.11x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.58 sec: 1.16x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.8 ms: 1.10x slower                                                      |
| python_startup         | 19.5 ms                                                     | 22.0 ms: 1.13x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 24.6 ms: 1.07x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 250 ms: 1.47x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 198 ms: 1.44x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 547 ms: 1.41x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.51 sec: 1.38x faster                                                     |
| async_tree_none            | 291 ms                                                      | 219 ms: 1.33x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 266 ms: 1.28x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 395 ms: 1.27x faster                                                       |
| deepcopy                   | 238 us                                                      | 188 us: 1.27x faster                                                       |
| async_tree_io              | 731 ms                                                      | 577 ms: 1.27x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 391 ms: 1.25x faster                                                       |
| comprehensions             | 14.1 us                                                     | 12.0 us: 1.18x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 20.4 us: 1.16x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.89 us: 1.11x faster                                                      |
| regex_dna                  | 126 ms                                                      | 118 ms: 1.07x faster                                                       |
| generators                 | 22.5 ms                                                     | 21.2 ms: 1.06x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 824 us: 1.04x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                                      |
| pathlib                    | 80.5 ms                                                     | 78.3 ms: 1.03x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 43.4 ms: 1.02x faster                                                      |
| json                       | 3.05 ms                                                     | 2.98 ms: 1.02x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 47.8 ms: 1.02x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 14.1 ms: 1.01x faster                                                      |
| pidigits                   | 152 ms                                                      | 151 ms: 1.01x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 62.4 ms: 1.01x faster                                                      |
| chaos                      | 43.3 ms                                                     | 43.7 ms: 1.01x slower                                                      |
| sympy_sum                  | 91.5 ms                                                     | 92.3 ms: 1.01x slower                                                      |
| spectral_norm              | 66.9 ms                                                     | 67.6 ms: 1.01x slower                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 65.8 ms: 1.01x slower                                                      |
| raytrace                   | 192 ms                                                      | 195 ms: 1.02x slower                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 94.6 ms: 1.02x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.2 us: 1.02x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.57 ms: 1.03x slower                                                      |
| sympy_str                  | 175 ms                                                      | 180 ms: 1.03x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.4 ms: 1.03x slower                                                      |
| async_generators           | 239 ms                                                      | 247 ms: 1.03x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 193 ms: 1.03x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 77.2 ms: 1.04x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 57.8 ms: 1.04x slower                                                      |
| tornado_http               | 89.5 ms                                                     | 93.2 ms: 1.04x slower                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.68 ms: 1.05x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 91.7 ms: 1.05x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 36.3 ms: 1.05x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.27 ms: 1.05x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 63.7 ns: 1.05x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.75 sec: 1.05x slower                                                     |
| 2to3                       | 218 ms                                                      | 231 ms: 1.06x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 549 ms: 1.07x slower                                                       |
| django_template            | 22.9 ms                                                     | 24.6 ms: 1.07x slower                                                      |
| go                         | 91.6 ms                                                     | 98.5 ms: 1.08x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 211 us: 1.08x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.49 sec: 1.08x slower                                                     |
| sqlglot_transpile          | 1.02 ms                                                     | 1.11 ms: 1.09x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.46 ms: 1.09x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 41.2 ms: 1.09x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 6.22 ms: 1.09x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.14 sec: 1.09x slower                                                     |
| sympy_expand               | 284 ms                                                      | 312 ms: 1.10x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 17.8 ms: 1.10x slower                                                      |
| pyflate                    | 295 ms                                                      | 324 ms: 1.10x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 888 us: 1.10x slower                                                       |
| asyncio_tcp                | 487 ms                                                      | 539 ms: 1.11x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 65.5 ms: 1.11x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 148 us: 1.11x slower                                                       |
| scimark_fft                | 184 ms                                                      | 205 ms: 1.11x slower                                                       |
| python_startup             | 19.5 ms                                                     | 22.0 ms: 1.13x slower                                                      |
| richards_super             | 32.1 ms                                                     | 36.2 ms: 1.13x slower                                                      |
| richards                   | 28.4 ms                                                     | 32.3 ms: 1.14x slower                                                      |
| nbody                      | 71.9 ms                                                     | 82.3 ms: 1.15x slower                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 50.3 ms: 1.15x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.58 sec: 1.16x slower                                                     |
| regex_v8                   | 14.2 ms                                                     | 16.5 ms: 1.16x slower                                                      |
| coverage                   | 40.8 ms                                                     | 47.4 ms: 1.16x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 92.2 ms: 1.17x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.87 ms: 1.18x slower                                                      |
| fannkuch                   | 247 ms                                                      | 294 ms: 1.19x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 115 us: 1.21x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 909 us: 1.21x slower                                                       |
| pycparser                  | 699 ms                                                      | 888 ms: 1.27x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (5): mako, float, bench_mp_pool, logging_format, logging_simple
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240815-3.14.0a0-e913d2c/bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c.json: genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.012x slower
# HPT report

- Reliability score: 99.83% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown