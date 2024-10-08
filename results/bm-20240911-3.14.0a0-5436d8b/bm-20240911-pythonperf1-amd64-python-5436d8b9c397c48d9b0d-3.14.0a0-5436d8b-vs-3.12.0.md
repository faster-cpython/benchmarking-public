# Results vs. 3.12.0

- fork: python
- ref: 5436d8b9c397c48d9b0d
- machine: windows-amd64
- commit hash: 5436d8b
- commit date: 2024-09-11
- overall geometric mean: 1.01x faster
- HPT reliability: 67.02%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 221 ms: 1.01x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.69 sec: 1.02x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 83.3 ms: 1.07x faster                                                      |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 250 ms: 1.47x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 197 ms: 1.44x faster                                                       |
| async_tree_none            | 291 ms                                                      | 207 ms: 1.41x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 553 ms: 1.39x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 259 ms: 1.31x faster                                                       |
| async_tree_io              | 731 ms                                                      | 564 ms: 1.30x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 390 ms: 1.29x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 388 ms: 1.26x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.36x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 54.4 ms: 1.04x faster                                                      |
| pidigits       | 152 ms                                                      | 151 ms: 1.01x faster                                                       |
| nbody          | 71.9 ms                                                     | 79.8 ms: 1.11x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 114 ms: 1.11x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.55 ms: 1.05x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 14.6 ms: 1.02x slower                                                      |
| regex_compile  | 87.5 ms                                                     | 89.6 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle               | 7.43 us                                                     | 7.28 us: 1.02x faster                                                      |
| unpickle_list        | 2.75 us                                                     | 2.77 us: 1.01x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 57.2 ms: 1.03x slower                                                      |
| pickle_list          | 2.83 us                                                     | 2.94 us: 1.04x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.5 us: 1.05x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 209 us: 1.07x slower                                                       |
| pickle_dict          | 18.4 us                                                     | 19.7 us: 1.07x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 40.4 ms: 1.07x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.18 ms: 1.09x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 145 us: 1.09x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.56 sec: 1.14x slower                                                     |
| unpickle             | 8.18 us                                                     | 9.43 us: 1.15x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.3 ms: 1.07x slower                                                      |
| python_startup         | 19.5 ms                                                     | 21.3 ms: 1.10x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.83 ms: 1.04x faster                                                      |
| django_template | 22.9 ms                                                     | 24.5 ms: 1.07x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.02x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 250 ms: 1.47x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 197 ms: 1.44x faster                                                       |
| async_tree_none            | 291 ms                                                      | 207 ms: 1.41x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.49 sec: 1.40x faster                                                     |
| async_tree_io_tg           | 771 ms                                                      | 553 ms: 1.39x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 259 ms: 1.31x faster                                                       |
| async_tree_io              | 731 ms                                                      | 564 ms: 1.30x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 390 ms: 1.29x faster                                                       |
| deepcopy                   | 238 us                                                      | 188 us: 1.27x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 388 ms: 1.26x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.4 us: 1.24x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 20.0 us: 1.19x faster                                                      |
| regex_dna                  | 126 ms                                                      | 114 ms: 1.11x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 73.9 ms: 1.09x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.92 us: 1.09x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.62 us: 1.09x faster                                                      |
| go                         | 91.6 ms                                                     | 84.6 ms: 1.08x faster                                                      |
| generators                 | 22.5 ms                                                     | 20.9 ms: 1.08x faster                                                      |
| tornado_http               | 89.5 ms                                                     | 83.3 ms: 1.07x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 810 us: 1.06x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 41.9 ms: 1.06x faster                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 65.8 ms: 1.05x faster                                                      |
| asyncio_tcp                | 487 ms                                                      | 464 ms: 1.05x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.55 ms: 1.05x faster                                                      |
| float                      | 56.8 ms                                                     | 54.4 ms: 1.04x faster                                                      |
| mako                       | 7.09 ms                                                     | 6.83 ms: 1.04x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 64.7 ms: 1.03x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 46.9 ms: 1.03x faster                                                      |
| raytrace                   | 192 ms                                                      | 187 ms: 1.03x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 89.2 ms: 1.03x faster                                                      |
| chaos                      | 43.3 ms                                                     | 42.3 ms: 1.02x faster                                                      |
| pickle                     | 7.43 us                                                     | 7.28 us: 1.02x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 14.0 ms: 1.02x faster                                                      |
| pidigits                   | 152 ms                                                      | 151 ms: 1.01x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.66 us: 1.01x faster                                                      |
| async_generators           | 239 ms                                                      | 238 ms: 1.01x faster                                                       |
| unpickle_list              | 2.75 us                                                     | 2.77 us: 1.01x slower                                                      |
| sympy_str                  | 175 ms                                                      | 176 ms: 1.01x slower                                                       |
| 2to3                       | 218 ms                                                      | 221 ms: 1.01x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.69 sec: 1.02x slower                                                     |
| sqlglot_normalize          | 187 ms                                                      | 191 ms: 1.02x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 14.6 ms: 1.02x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 89.6 ms: 1.02x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 61.9 ns: 1.02x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 57.2 ms: 1.03x slower                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.64 ms: 1.03x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.24 ms: 1.04x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 77.6 ms: 1.04x slower                                                      |
| pickle_list                | 2.83 us                                                     | 2.94 us: 1.04x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 36.0 ms: 1.04x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.5 us: 1.05x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.30 ms: 1.05x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 61.8 ms: 1.05x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 541 ms: 1.05x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.11 sec: 1.06x slower                                                     |
| pycparser                  | 699 ms                                                      | 744 ms: 1.07x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 17.3 ms: 1.07x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.09 ms: 1.07x slower                                                      |
| django_template            | 22.9 ms                                                     | 24.5 ms: 1.07x slower                                                      |
| pyflate                    | 295 ms                                                      | 315 ms: 1.07x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 209 us: 1.07x slower                                                       |
| pickle_dict                | 18.4 us                                                     | 19.7 us: 1.07x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 40.4 ms: 1.07x slower                                                      |
| sympy_expand               | 284 ms                                                      | 306 ms: 1.08x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.18 ms: 1.09x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 145 us: 1.09x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 875 us: 1.09x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.50 sec: 1.09x slower                                                     |
| python_startup             | 19.5 ms                                                     | 21.3 ms: 1.10x slower                                                      |
| unpack_sequence            | 37.5 ns                                                     | 41.3 ns: 1.10x slower                                                      |
| scimark_fft                | 184 ms                                                      | 204 ms: 1.10x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 48.5 ms: 1.11x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 87.5 ms: 1.11x slower                                                      |
| nbody                      | 71.9 ms                                                     | 79.8 ms: 1.11x slower                                                      |
| richards_super             | 32.1 ms                                                     | 35.8 ms: 1.12x slower                                                      |
| richards                   | 28.4 ms                                                     | 31.7 ms: 1.12x slower                                                      |
| fannkuch                   | 247 ms                                                      | 280 ms: 1.14x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.56 sec: 1.14x slower                                                     |
| unpickle                   | 8.18 us                                                     | 9.43 us: 1.15x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 111 us: 1.16x slower                                                       |
| coverage                   | 40.8 ms                                                     | 48.1 ms: 1.18x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 887 us: 1.18x slower                                                       |
| telco                      | 4.13 ms                                                     | 5.06 ms: 1.23x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (7): xml_etree_iterparse, logging_simple, gc_traversal, nqueens, sympy_integrate, xml_etree_parse, json
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240911-3.14.0a0-5436d8b/bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 67.02% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown