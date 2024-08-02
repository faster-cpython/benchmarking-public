# Results vs. 3.12.0

- fork: python
- ref: 5b941e57c71d7d0ab983
- machine: windows-amd64
- commit hash: 5b941e5
- commit date: 2024-05-11
- overall geometric mean: 1.06x slower
- HPT reliability: 99.91%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 237 ms: 1.09x slower                                                       |
| chameleon      | 4.98 ms                                                     | 5.39 ms: 1.08x slower                                                      |
| docutils       | 1.66 sec                                                    | 1.85 sec: 1.11x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 87.9 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.06x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 279 ms: 1.31x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 221 ms: 1.29x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 390 ms: 1.29x faster                                                       |
| async_tree_none            | 291 ms                                                      | 238 ms: 1.22x faster                                                       |
| async_tree_io              | 731 ms                                                      | 599 ms: 1.22x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 639 ms: 1.21x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 407 ms: 1.20x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 285 ms: 1.19x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.24x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 54.6 ms: 1.04x faster                                                      |
| pidigits       | 152 ms                                                      | 151 ms: 1.01x faster                                                       |
| nbody          | 71.9 ms                                                     | 75.7 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                       | 1.00x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 116 ms: 1.09x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 14.9 ms: 1.05x slower                                                      |
| regex_compile  | 87.5 ms                                                     | 112 ms: 1.27x slower                                                       |
| Geometric mean | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle               | 7.43 us                                                     | 7.13 us: 1.04x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 90.1 ms: 1.03x faster                                                      |
| pickle_dict          | 18.4 us                                                     | 18.3 us: 1.01x faster                                                      |
| json_loads           | 13.9 us                                                     | 14.0 us: 1.01x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 5.76 ms: 1.01x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 2.80 us: 1.02x slower                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 66.4 ms: 1.02x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 57.4 ms: 1.03x slower                                                      |
| unpickle             | 8.18 us                                                     | 8.55 us: 1.05x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 40.3 ms: 1.07x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.11 us: 1.10x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.55 sec: 1.13x slower                                                     |
| pickle_pure_python   | 195 us                                                      | 228 us: 1.17x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 167 us: 1.26x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 16.5 ms: 1.02x slower                                                      |
| python_startup         | 19.5 ms                                                     | 20.3 ms: 1.04x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 25.2 ms: 1.10x slower                                                      |
| mako            | 7.09 ms                                                     | 7.85 ms: 1.11x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.10x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.53 sec: 1.37x faster                                                     |
| async_tree_memoization_tg  | 367 ms                                                      | 279 ms: 1.31x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 221 ms: 1.29x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 390 ms: 1.29x faster                                                       |
| async_tree_none            | 291 ms                                                      | 238 ms: 1.22x faster                                                       |
| async_tree_io              | 731 ms                                                      | 599 ms: 1.22x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 639 ms: 1.21x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 407 ms: 1.20x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 285 ms: 1.19x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 12.9 ms: 1.10x faster                                                      |
| generators                 | 22.5 ms                                                     | 20.7 ms: 1.09x faster                                                      |
| regex_dna                  | 126 ms                                                      | 116 ms: 1.09x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.63 us: 1.08x faster                                                      |
| pickle                     | 7.43 us                                                     | 7.13 us: 1.04x faster                                                      |
| float                      | 56.8 ms                                                     | 54.6 ms: 1.04x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 90.1 ms: 1.03x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| tornado_http               | 89.5 ms                                                     | 87.9 ms: 1.02x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.65 us: 1.01x faster                                                      |
| logging_simple             | 6.28 us                                                     | 6.21 us: 1.01x faster                                                      |
| raytrace                   | 192 ms                                                      | 190 ms: 1.01x faster                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 68.5 ms: 1.01x faster                                                      |
| pickle_dict                | 18.4 us                                                     | 18.3 us: 1.01x faster                                                      |
| pathlib                    | 80.5 ms                                                     | 80.0 ms: 1.01x faster                                                      |
| pidigits                   | 152 ms                                                      | 151 ms: 1.01x faster                                                       |
| json_loads                 | 13.9 us                                                     | 14.0 us: 1.01x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 5.76 ms: 1.01x slower                                                      |
| comprehensions             | 14.1 us                                                     | 14.3 us: 1.01x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 16.5 ms: 1.02x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 2.80 us: 1.02x slower                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 66.4 ms: 1.02x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 57.4 ms: 1.03x slower                                                      |
| async_generators           | 239 ms                                                      | 247 ms: 1.03x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.57 ms: 1.03x slower                                                      |
| python_startup             | 19.5 ms                                                     | 20.3 ms: 1.04x slower                                                      |
| unpickle                   | 8.18 us                                                     | 8.55 us: 1.05x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 78.1 ms: 1.05x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 14.9 ms: 1.05x slower                                                      |
| chaos                      | 43.3 ms                                                     | 45.6 ms: 1.05x slower                                                      |
| nbody                      | 71.9 ms                                                     | 75.7 ms: 1.05x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.47 sec: 1.07x slower                                                     |
| xml_etree_process          | 37.7 ms                                                     | 40.3 ms: 1.07x slower                                                      |
| richards_super             | 32.1 ms                                                     | 34.7 ms: 1.08x slower                                                      |
| chameleon                  | 4.98 ms                                                     | 5.39 ms: 1.08x slower                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 2.27 us: 1.09x slower                                                      |
| 2to3                       | 218 ms                                                      | 237 ms: 1.09x slower                                                       |
| richards                   | 28.4 ms                                                     | 30.9 ms: 1.09x slower                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 53.1 ms: 1.10x slower                                                      |
| django_template            | 22.9 ms                                                     | 25.2 ms: 1.10x slower                                                      |
| pickle_list                | 2.83 us                                                     | 3.11 us: 1.10x slower                                                      |
| sympy_sum                  | 91.5 ms                                                     | 101 ms: 1.10x slower                                                       |
| mako                       | 7.09 ms                                                     | 7.85 ms: 1.11x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 570 ms: 1.11x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.85 sec: 1.11x slower                                                     |
| pprint_pformat             | 1.05 sec                                                    | 1.17 sec: 1.12x slower                                                     |
| deepcopy                   | 238 us                                                      | 266 us: 1.12x slower                                                       |
| scimark_fft                | 184 ms                                                      | 207 ms: 1.12x slower                                                       |
| coverage                   | 40.8 ms                                                     | 46.0 ms: 1.13x slower                                                      |
| sympy_str                  | 175 ms                                                      | 198 ms: 1.13x slower                                                       |
| pycparser                  | 699 ms                                                      | 788 ms: 1.13x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.16 ms: 1.13x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 39.1 ms: 1.13x slower                                                      |
| nqueens                    | 62.8 ms                                                     | 71.2 ms: 1.13x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.55 sec: 1.13x slower                                                     |
| go                         | 91.6 ms                                                     | 104 ms: 1.13x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 919 us: 1.14x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 14.9 ms: 1.15x slower                                                      |
| pyflate                    | 295 ms                                                      | 343 ms: 1.16x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 228 us: 1.17x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.84 ms: 1.17x slower                                                      |
| fannkuch                   | 247 ms                                                      | 289 ms: 1.17x slower                                                       |
| asyncio_tcp                | 487 ms                                                      | 572 ms: 1.17x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 92.5 ms: 1.17x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 896 us: 1.19x slower                                                       |
| sympy_expand               | 284 ms                                                      | 338 ms: 1.19x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 52.7 ms: 1.20x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 116 us: 1.22x slower                                                       |
| spectral_norm              | 66.9 ms                                                     | 81.6 ms: 1.22x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 167 us: 1.26x slower                                                       |
| logging_silent             | 60.5 ns                                                     | 76.5 ns: 1.26x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.75 ms: 1.27x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 112 ms: 1.27x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 3.29 ms: 1.28x slower                                                      |
| deepcopy_memo              | 23.7 us                                                     | 31.2 us: 1.32x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 81.6 ms: 1.39x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 5.76 ms: 1.41x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.06x slower                                                               |

Benchmark hidden because not significant (2): json, bench_thread_pool
Ignored benchmarks (8) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (6) of results/bm-20240511-3.14.0a0-5b941e5-PYTHON_UOPS/bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.91% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown