# Results vs. 3.12.0

- fork: python
- ref: 6b280a84988ca221b5bd
- machine: windows-amd64
- commit hash: 6b280a8
- commit date: 2024-06-29
- overall geometric mean: 1.01x slower
- HPT reliability: 98.92%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 226 ms: 1.04x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.69 sec: 1.01x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 82.1 ms: 1.09x faster                                                      |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 244 ms: 1.50x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 195 ms: 1.46x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 540 ms: 1.43x faster                                                       |
| async_tree_none            | 291 ms                                                      | 217 ms: 1.34x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 387 ms: 1.30x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 261 ms: 1.30x faster                                                       |
| async_tree_io              | 731 ms                                                      | 569 ms: 1.28x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 387 ms: 1.27x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.36x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 152 ms                                                      | 150 ms: 1.01x faster                                                       |
| float          | 56.8 ms                                                     | 57.4 ms: 1.01x slower                                                      |
| nbody          | 71.9 ms                                                     | 82.2 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 118 ms: 1.07x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 88.1 ms: 1.01x slower                                                      |
| regex_v8       | 14.2 ms                                                     | 16.6 ms: 1.16x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 13.9 us                                                     | 13.8 us: 1.01x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 93.9 ms: 1.01x slower                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 66.6 ms: 1.02x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.00 ms: 1.05x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 59.7 ms: 1.07x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 211 us: 1.08x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 42.0 ms: 1.11x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 156 us: 1.17x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.63 sec: 1.19x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.0 ms: 1.04x slower                                                      |
| python_startup         | 19.5 ms                                                     | 20.6 ms: 1.06x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 24.3 ms: 1.06x slower                                                      |
| mako            | 7.09 ms                                                     | 7.85 ms: 1.11x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.08x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 244 ms: 1.50x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 195 ms: 1.46x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 540 ms: 1.43x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.53 sec: 1.37x faster                                                     |
| async_tree_none            | 291 ms                                                      | 217 ms: 1.34x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 387 ms: 1.30x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 261 ms: 1.30x faster                                                       |
| deepcopy                   | 238 us                                                      | 185 us: 1.29x faster                                                       |
| async_tree_io              | 731 ms                                                      | 569 ms: 1.28x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 387 ms: 1.27x faster                                                       |
| comprehensions             | 14.1 us                                                     | 12.0 us: 1.17x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 768 us: 1.12x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.89 us: 1.11x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 21.6 us: 1.10x faster                                                      |
| tornado_http               | 89.5 ms                                                     | 82.1 ms: 1.09x faster                                                      |
| raytrace                   | 192 ms                                                      | 180 ms: 1.07x faster                                                       |
| regex_dna                  | 126 ms                                                      | 118 ms: 1.07x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 75.7 ms: 1.06x faster                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 65.8 ms: 1.05x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 88.9 ms: 1.03x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                      |
| sympy_str                  | 175 ms                                                      | 172 ms: 1.02x faster                                                       |
| pidigits                   | 152 ms                                                      | 150 ms: 1.01x faster                                                       |
| json_loads                 | 13.9 us                                                     | 13.8 us: 1.01x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 88.1 ms: 1.01x slower                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 93.9 ms: 1.01x slower                                                      |
| float                      | 56.8 ms                                                     | 57.4 ms: 1.01x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.69 sec: 1.01x slower                                                     |
| sympy_integrate            | 13.0 ms                                                     | 13.2 ms: 1.02x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.55 ms: 1.02x slower                                                      |
| sqlglot_normalize          | 187 ms                                                      | 191 ms: 1.02x slower                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 66.6 ms: 1.02x slower                                                      |
| chaos                      | 43.3 ms                                                     | 44.6 ms: 1.03x slower                                                      |
| sympy_expand               | 284 ms                                                      | 292 ms: 1.03x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 35.6 ms: 1.03x slower                                                      |
| coroutines                 | 14.3 ms                                                     | 14.8 ms: 1.04x slower                                                      |
| 2to3                       | 218 ms                                                      | 226 ms: 1.04x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.24 ms: 1.04x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 77.4 ms: 1.04x slower                                                      |
| async_generators           | 239 ms                                                      | 248 ms: 1.04x slower                                                       |
| go                         | 91.6 ms                                                     | 95.1 ms: 1.04x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 17.0 ms: 1.04x slower                                                      |
| generators                 | 22.5 ms                                                     | 23.6 ms: 1.05x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.44 sec: 1.05x slower                                                     |
| json_dumps                 | 5.70 ms                                                     | 6.00 ms: 1.05x slower                                                      |
| python_startup             | 19.5 ms                                                     | 20.6 ms: 1.06x slower                                                      |
| django_template            | 22.9 ms                                                     | 24.3 ms: 1.06x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 64.6 ns: 1.07x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 59.7 ms: 1.07x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 211 us: 1.08x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.13 sec: 1.08x slower                                                     |
| richards_super             | 32.1 ms                                                     | 34.7 ms: 1.08x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 556 ms: 1.08x slower                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 52.6 ms: 1.08x slower                                                      |
| richards                   | 28.4 ms                                                     | 30.9 ms: 1.09x slower                                                      |
| spectral_norm              | 66.9 ms                                                     | 73.2 ms: 1.09x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.50 ms: 1.10x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.12 ms: 1.10x slower                                                      |
| pyflate                    | 295 ms                                                      | 324 ms: 1.10x slower                                                       |
| mako                       | 7.09 ms                                                     | 7.85 ms: 1.11x slower                                                      |
| coverage                   | 40.8 ms                                                     | 45.4 ms: 1.11x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 42.0 ms: 1.11x slower                                                      |
| pycparser                  | 699 ms                                                      | 781 ms: 1.12x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 902 us: 1.12x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 89.4 ms: 1.13x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 67.0 ms: 1.14x slower                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 50.0 ms: 1.14x slower                                                      |
| nbody                      | 71.9 ms                                                     | 82.2 ms: 1.14x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 16.6 ms: 1.16x slower                                                      |
| scimark_fft                | 184 ms                                                      | 215 ms: 1.17x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 156 us: 1.17x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.86 ms: 1.18x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 112 us: 1.18x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 895 us: 1.19x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.63 sec: 1.19x slower                                                     |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 3.07 ms: 1.20x slower                                                      |
| fannkuch                   | 247 ms                                                      | 303 ms: 1.23x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (5): nqueens, logging_simple, logging_format, asyncio_tcp, json
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240629-3.14.0a0-6b280a8/bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 98.92% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown