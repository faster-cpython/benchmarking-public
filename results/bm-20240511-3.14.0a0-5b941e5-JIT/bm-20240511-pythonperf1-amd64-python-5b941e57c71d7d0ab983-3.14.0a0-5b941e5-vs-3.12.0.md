# Results vs. 3.12.0

- fork: python
- ref: 5b941e57c71d7d0ab983
- machine: windows-amd64
- commit hash: 5b941e5
- commit date: 2024-05-11
- overall geometric mean: 1.05x faster
- HPT reliability: 99.34%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 232 ms: 1.06x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.76 sec: 1.06x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 85.4 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 270 ms: 1.36x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 213 ms: 1.34x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 387 ms: 1.30x faster                                                       |
| async_tree_none            | 291 ms                                                      | 226 ms: 1.29x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 619 ms: 1.25x faster                                                       |
| async_tree_io              | 731 ms                                                      | 589 ms: 1.24x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 396 ms: 1.23x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 275 ms: 1.23x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.28x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 49.9 ms: 1.44x faster                                                      |
| float          | 56.8 ms                                                     | 43.4 ms: 1.31x faster                                                      |
| pidigits       | 152 ms                                                      | 150 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.24x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 114 ms: 1.11x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 86.6 ms: 1.01x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 15.3 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 172 us: 1.13x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.23 sec: 1.11x faster                                                     |
| xml_etree_generate   | 55.8 ms                                                     | 51.1 ms: 1.09x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 59.9 ms: 1.09x faster                                                      |
| unpickle_pure_python | 133 us                                                      | 124 us: 1.07x faster                                                       |
| pickle_dict          | 18.4 us                                                     | 17.5 us: 1.05x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 36.1 ms: 1.04x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 91.6 ms: 1.02x faster                                                      |
| pickle               | 7.43 us                                                     | 7.35 us: 1.01x faster                                                      |
| json_dumps           | 5.70 ms                                                     | 5.65 ms: 1.01x faster                                                      |
| json_loads           | 13.9 us                                                     | 14.3 us: 1.03x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 2.88 us: 1.05x slower                                                      |
| unpickle             | 8.18 us                                                     | 8.69 us: 1.06x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                               |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.2 ms: 1.12x slower                                                      |
| python_startup         | 19.5 ms                                                     | 22.0 ms: 1.13x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 4.94 ms: 1.43x faster                                                      |
| django_template | 22.9 ms                                                     | 25.4 ms: 1.11x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.14x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| spectral_norm              | 66.9 ms                                                     | 44.9 ms: 1.49x faster                                                      |
| nbody                      | 71.9 ms                                                     | 49.9 ms: 1.44x faster                                                      |
| mako                       | 7.09 ms                                                     | 4.94 ms: 1.43x faster                                                      |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.52 sec: 1.38x faster                                                     |
| comprehensions             | 14.1 us                                                     | 10.3 us: 1.38x faster                                                      |
| async_tree_memoization_tg  | 367 ms                                                      | 270 ms: 1.36x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 213 ms: 1.34x faster                                                       |
| float                      | 56.8 ms                                                     | 43.4 ms: 1.31x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 387 ms: 1.30x faster                                                       |
| async_tree_none            | 291 ms                                                      | 226 ms: 1.29x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 619 ms: 1.25x faster                                                       |
| async_tree_io              | 731 ms                                                      | 589 ms: 1.24x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 396 ms: 1.23x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 275 ms: 1.23x faster                                                       |
| scimark_fft                | 184 ms                                                      | 150 ms: 1.23x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.14 ms: 1.19x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 40.8 ms: 1.19x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 20.5 us: 1.16x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 37.9 ms: 1.15x faster                                                      |
| pprint_safe_repr           | 513 ms                                                      | 450 ms: 1.14x faster                                                       |
| pickle_pure_python         | 195 us                                                      | 172 us: 1.13x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 924 ms: 1.13x faster                                                       |
| pyflate                    | 295 ms                                                      | 262 ms: 1.12x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.23 sec: 1.11x faster                                                     |
| sqlite_synth               | 1.76 us                                                     | 1.58 us: 1.11x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 54.5 ns: 1.11x faster                                                      |
| fannkuch                   | 247 ms                                                      | 223 ms: 1.11x faster                                                       |
| regex_dna                  | 126 ms                                                      | 114 ms: 1.11x faster                                                       |
| chaos                      | 43.3 ms                                                     | 39.4 ms: 1.10x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 51.1 ms: 1.09x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 59.9 ms: 1.09x faster                                                      |
| raytrace                   | 192 ms                                                      | 179 ms: 1.08x faster                                                       |
| unpickle_pure_python       | 133 us                                                      | 124 us: 1.07x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.3 ms: 1.07x faster                                                      |
| logging_simple             | 6.28 us                                                     | 5.88 us: 1.07x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.31 us: 1.07x faster                                                      |
| pickle_dict                | 18.4 us                                                     | 17.5 us: 1.05x faster                                                      |
| tornado_http               | 89.5 ms                                                     | 85.4 ms: 1.05x faster                                                      |
| xml_etree_process          | 37.7 ms                                                     | 36.1 ms: 1.04x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 832 us: 1.03x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 2.04 us: 1.03x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 61.1 ms: 1.03x faster                                                      |
| generators                 | 22.5 ms                                                     | 22.0 ms: 1.03x faster                                                      |
| deepcopy                   | 238 us                                                      | 233 us: 1.02x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 73.2 ms: 1.02x faster                                                      |
| pidigits                   | 152 ms                                                      | 150 ms: 1.02x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 91.6 ms: 1.02x faster                                                      |
| json                       | 3.05 ms                                                     | 3.01 ms: 1.01x faster                                                      |
| pickle                     | 7.43 us                                                     | 7.35 us: 1.01x faster                                                      |
| pathlib                    | 80.5 ms                                                     | 79.6 ms: 1.01x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 86.6 ms: 1.01x faster                                                      |
| json_dumps                 | 5.70 ms                                                     | 5.65 ms: 1.01x faster                                                      |
| richards_super             | 32.1 ms                                                     | 32.3 ms: 1.01x slower                                                      |
| go                         | 91.6 ms                                                     | 92.6 ms: 1.01x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.04 ms: 1.01x slower                                                      |
| sympy_str                  | 175 ms                                                      | 178 ms: 1.01x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 70.5 ms: 1.02x slower                                                      |
| sympy_sum                  | 91.5 ms                                                     | 93.6 ms: 1.02x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.57 ms: 1.03x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.3 us: 1.03x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 2.88 us: 1.05x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 82.6 ms: 1.05x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.76 sec: 1.06x slower                                                     |
| unpickle                   | 8.18 us                                                     | 8.69 us: 1.06x slower                                                      |
| 2to3                       | 218 ms                                                      | 232 ms: 1.06x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 15.3 ms: 1.07x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.32 ms: 1.07x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.47 sec: 1.07x slower                                                     |
| sqlglot_optimize           | 34.5 ms                                                     | 37.1 ms: 1.07x slower                                                      |
| pycparser                  | 699 ms                                                      | 754 ms: 1.08x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 14.0 ms: 1.08x slower                                                      |
| async_generators           | 239 ms                                                      | 259 ms: 1.08x slower                                                       |
| sympy_expand               | 284 ms                                                      | 309 ms: 1.09x slower                                                       |
| coverage                   | 40.8 ms                                                     | 45.1 ms: 1.10x slower                                                      |
| django_template            | 22.9 ms                                                     | 25.4 ms: 1.11x slower                                                      |
| asyncio_tcp                | 487 ms                                                      | 545 ms: 1.12x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 18.2 ms: 1.12x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.63 ms: 1.12x slower                                                      |
| python_startup             | 19.5 ms                                                     | 22.0 ms: 1.13x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.65 ms: 1.13x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 67.5 ms: 1.15x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 112 us: 1.18x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 906 us: 1.20x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (4): pickle_list, sqlglot_parse, chameleon, richards
Ignored benchmarks (8) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (6) of results/bm-20240511-3.14.0a0-5b941e5-JIT/bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.34% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown