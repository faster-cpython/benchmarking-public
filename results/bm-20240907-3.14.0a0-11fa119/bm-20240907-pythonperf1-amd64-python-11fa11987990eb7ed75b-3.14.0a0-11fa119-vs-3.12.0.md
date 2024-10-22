# Results vs. 3.12.0

- fork: python
- ref: 11fa11987990eb7ed75b
- machine: windows-amd64
- commit hash: 11fa119
- commit date: 2024-09-07
- overall geometric mean: 1.01x slower
- HPT reliability: 99.39%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 227 ms: 1.04x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.70 sec: 1.02x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 93.8 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 253 ms: 1.45x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 199 ms: 1.43x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 541 ms: 1.42x faster                                                       |
| async_tree_none            | 291 ms                                                      | 217 ms: 1.34x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 260 ms: 1.31x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 390 ms: 1.29x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 383 ms: 1.28x faster                                                       |
| async_tree_io              | 731 ms                                                      | 613 ms: 1.19x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.34x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 84.6 ms: 1.18x slower                                                      |
| Geometric mean | (ref)                                                       | 1.06x slower                                                               |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 120 ms: 1.06x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 90.8 ms: 1.04x slower                                                      |
| regex_v8       | 14.2 ms                                                     | 15.1 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                       | 1.00x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_list        | 2.75 us                                                     | 2.78 us: 1.01x slower                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 94.3 ms: 1.01x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.3 us: 1.03x slower                                                      |
| pickle_dict          | 18.4 us                                                     | 19.0 us: 1.03x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 58.4 ms: 1.05x slower                                                      |
| pickle_list          | 2.83 us                                                     | 2.99 us: 1.06x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 213 us: 1.09x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.21 ms: 1.09x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 41.2 ms: 1.09x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 150 us: 1.13x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.60 sec: 1.17x slower                                                     |
| unpickle             | 8.18 us                                                     | 9.64 us: 1.18x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                               |

Benchmark hidden because not significant (2): pickle, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.1 ms: 1.11x slower                                                      |
| python_startup         | 19.5 ms                                                     | 22.3 ms: 1.15x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.85 ms: 1.03x faster                                                      |
| django_template | 22.9 ms                                                     | 24.9 ms: 1.09x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.02x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 253 ms: 1.45x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 199 ms: 1.43x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 541 ms: 1.42x faster                                                       |
| async_tree_none            | 291 ms                                                      | 217 ms: 1.34x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.59 sec: 1.32x faster                                                     |
| async_tree_memoization     | 339 ms                                                      | 260 ms: 1.31x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 390 ms: 1.29x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 383 ms: 1.28x faster                                                       |
| deepcopy                   | 238 us                                                      | 189 us: 1.26x faster                                                       |
| async_tree_io              | 731 ms                                                      | 613 ms: 1.19x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.9 us: 1.19x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 20.3 us: 1.17x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.89 us: 1.10x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.62 us: 1.08x faster                                                      |
| generators                 | 22.5 ms                                                     | 20.9 ms: 1.08x faster                                                      |
| regex_dna                  | 126 ms                                                      | 120 ms: 1.06x faster                                                       |
| go                         | 91.6 ms                                                     | 86.9 ms: 1.05x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 823 us: 1.04x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.85 ms: 1.03x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 67.8 ms: 1.02x faster                                                      |
| pathlib                    | 80.5 ms                                                     | 79.4 ms: 1.01x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 47.8 ms: 1.01x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.64 us: 1.01x faster                                                      |
| raytrace                   | 192 ms                                                      | 191 ms: 1.01x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 14.1 ms: 1.01x faster                                                      |
| logging_simple             | 6.28 us                                                     | 6.23 us: 1.01x faster                                                      |
| chaos                      | 43.3 ms                                                     | 43.0 ms: 1.01x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 44.1 ms: 1.00x faster                                                      |
| sympy_str                  | 175 ms                                                      | 177 ms: 1.01x slower                                                       |
| unpickle_list              | 2.75 us                                                     | 2.78 us: 1.01x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 13.1 ms: 1.01x slower                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 94.3 ms: 1.01x slower                                                      |
| sqlglot_normalize          | 187 ms                                                      | 190 ms: 1.01x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 63.8 ms: 1.02x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.55 ms: 1.02x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.70 sec: 1.02x slower                                                     |
| json_loads                 | 13.9 us                                                     | 14.3 us: 1.03x slower                                                      |
| spectral_norm              | 66.9 ms                                                     | 69.0 ms: 1.03x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 19.0 us: 1.03x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 62.5 ns: 1.03x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 90.8 ms: 1.04x slower                                                      |
| async_generators           | 239 ms                                                      | 249 ms: 1.04x slower                                                       |
| 2to3                       | 218 ms                                                      | 227 ms: 1.04x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 58.4 ms: 1.05x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.26 ms: 1.05x slower                                                      |
| tornado_http               | 89.5 ms                                                     | 93.8 ms: 1.05x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 36.2 ms: 1.05x slower                                                      |
| pickle_list                | 2.83 us                                                     | 2.99 us: 1.06x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 15.1 ms: 1.06x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 79.0 ms: 1.06x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.12 sec: 1.07x slower                                                     |
| mdp                        | 1.37 sec                                                    | 1.47 sec: 1.07x slower                                                     |
| pprint_safe_repr           | 513 ms                                                      | 549 ms: 1.07x slower                                                       |
| unpack_sequence            | 37.5 ns                                                     | 40.3 ns: 1.08x slower                                                      |
| asyncio_tcp                | 487 ms                                                      | 525 ms: 1.08x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.10 ms: 1.08x slower                                                      |
| sympy_expand               | 284 ms                                                      | 307 ms: 1.08x slower                                                       |
| django_template            | 22.9 ms                                                     | 24.9 ms: 1.09x slower                                                      |
| pyflate                    | 295 ms                                                      | 321 ms: 1.09x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.79 ms: 1.09x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 213 us: 1.09x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.21 ms: 1.09x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 41.2 ms: 1.09x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.50 ms: 1.10x slower                                                      |
| pycparser                  | 699 ms                                                      | 767 ms: 1.10x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 64.7 ms: 1.10x slower                                                      |
| sqlglot_parse              | 804 us                                                      | 892 us: 1.11x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 18.1 ms: 1.11x slower                                                      |
| scimark_fft                | 184 ms                                                      | 205 ms: 1.11x slower                                                       |
| richards_super             | 32.1 ms                                                     | 36.1 ms: 1.12x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 150 us: 1.13x slower                                                       |
| richards                   | 28.4 ms                                                     | 32.1 ms: 1.13x slower                                                      |
| python_startup             | 19.5 ms                                                     | 22.3 ms: 1.15x slower                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 50.4 ms: 1.15x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 91.5 ms: 1.16x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.60 sec: 1.17x slower                                                     |
| nbody                      | 71.9 ms                                                     | 84.6 ms: 1.18x slower                                                      |
| unpickle                   | 8.18 us                                                     | 9.64 us: 1.18x slower                                                      |
| fannkuch                   | 247 ms                                                      | 291 ms: 1.18x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 113 us: 1.19x slower                                                       |
| coverage                   | 40.8 ms                                                     | 48.6 ms: 1.19x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 902 us: 1.20x slower                                                       |
| telco                      | 4.13 ms                                                     | 5.12 ms: 1.24x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (6): sympy_sum, pidigits, pickle, xml_etree_iterparse, float, json
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240907-3.14.0a0-11fa119/bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.39% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown