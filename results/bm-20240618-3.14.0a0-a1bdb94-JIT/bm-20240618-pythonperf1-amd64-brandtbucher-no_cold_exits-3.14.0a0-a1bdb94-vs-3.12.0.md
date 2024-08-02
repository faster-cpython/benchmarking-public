# Results vs. 3.12.0

- fork: brandtbucher
- ref: no_cold_exits
- machine: windows-amd64
- commit hash: a1bdb94
- commit date: 2024-06-18
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 227 ms: 1.04x slower                                                      |
| docutils       | 1.66 sec                                                    | 1.73 sec: 1.04x slower                                                    |
| tornado_http   | 89.5 ms                                                     | 83.1 ms: 1.08x faster                                                     |
| Geometric mean | (ref)                                                       | 1.00x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 253 ms: 1.45x faster                                                      |
| async_tree_none_tg         | 285 ms                                                      | 202 ms: 1.41x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 380 ms: 1.32x faster                                                      |
| async_tree_none            | 291 ms                                                      | 223 ms: 1.31x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 594 ms: 1.30x faster                                                      |
| async_tree_memoization     | 339 ms                                                      | 272 ms: 1.25x faster                                                      |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 396 ms: 1.24x faster                                                      |
| async_tree_io              | 731 ms                                                      | 598 ms: 1.22x faster                                                      |
| Geometric mean             | (ref)                                                       | 1.31x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 51.5 ms: 1.40x faster                                                     |
| float          | 56.8 ms                                                     | 44.4 ms: 1.28x faster                                                     |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.22x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 115 ms: 1.10x faster                                                      |
| regex_effbot   | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                                     |
| regex_compile  | 87.5 ms                                                     | 85.8 ms: 1.02x faster                                                     |
| regex_v8       | 14.2 ms                                                     | 18.9 ms: 1.33x slower                                                     |
| Geometric mean | (ref)                                                       | 1.03x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.18 sec: 1.16x faster                                                    |
| pickle_pure_python   | 195 us                                                      | 168 us: 1.16x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 59.6 ms: 1.09x faster                                                     |
| xml_etree_generate   | 55.8 ms                                                     | 51.7 ms: 1.08x faster                                                     |
| unpickle_pure_python | 133 us                                                      | 125 us: 1.07x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 36.1 ms: 1.04x faster                                                     |
| pickle               | 7.43 us                                                     | 7.20 us: 1.03x faster                                                     |
| pickle_dict          | 18.4 us                                                     | 17.9 us: 1.03x faster                                                     |
| xml_etree_parse      | 93.0 ms                                                     | 91.4 ms: 1.02x faster                                                     |
| json_loads           | 13.9 us                                                     | 14.1 us: 1.01x slower                                                     |
| unpickle_list        | 2.75 us                                                     | 2.88 us: 1.05x slower                                                     |
| unpickle             | 8.18 us                                                     | 8.78 us: 1.07x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                              |

Benchmark hidden because not significant (2): pickle_list, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 16.6 ms: 1.02x slower                                                     |
| python_startup         | 19.5 ms                                                     | 20.4 ms: 1.05x slower                                                     |
| Geometric mean         | (ref)                                                       | 1.03x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.28 ms: 1.34x faster                                                     |
| django_template | 22.9 ms                                                     | 24.0 ms: 1.05x slower                                                     |
| Geometric mean  | (ref)                                                       | 1.13x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 23.7 us                                                     | 15.4 us: 1.54x faster                                                     |
| spectral_norm              | 66.9 ms                                                     | 45.7 ms: 1.47x faster                                                     |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.43 sec: 1.46x faster                                                    |
| async_tree_memoization_tg  | 367 ms                                                      | 253 ms: 1.45x faster                                                      |
| async_tree_none_tg         | 285 ms                                                      | 202 ms: 1.41x faster                                                      |
| deepcopy                   | 238 us                                                      | 169 us: 1.41x faster                                                      |
| nbody                      | 71.9 ms                                                     | 51.5 ms: 1.40x faster                                                     |
| comprehensions             | 14.1 us                                                     | 10.3 us: 1.38x faster                                                     |
| mako                       | 7.09 ms                                                     | 5.28 ms: 1.34x faster                                                     |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 380 ms: 1.32x faster                                                      |
| async_tree_none            | 291 ms                                                      | 223 ms: 1.31x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 594 ms: 1.30x faster                                                      |
| float                      | 56.8 ms                                                     | 44.4 ms: 1.28x faster                                                     |
| async_tree_memoization     | 339 ms                                                      | 272 ms: 1.25x faster                                                      |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 396 ms: 1.24x faster                                                      |
| async_tree_io              | 731 ms                                                      | 598 ms: 1.22x faster                                                      |
| scimark_fft                | 184 ms                                                      | 151 ms: 1.22x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.72 us: 1.22x faster                                                     |
| crypto_pyaes               | 48.5 ms                                                     | 40.8 ms: 1.19x faster                                                     |
| scimark_monte_carlo        | 43.7 ms                                                     | 37.2 ms: 1.18x faster                                                     |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.19 ms: 1.17x faster                                                     |
| tomli_loads                | 1.37 sec                                                    | 1.18 sec: 1.16x faster                                                    |
| pickle_pure_python         | 195 us                                                      | 168 us: 1.16x faster                                                      |
| pyflate                    | 295 ms                                                      | 256 ms: 1.15x faster                                                      |
| logging_simple             | 6.28 us                                                     | 5.46 us: 1.15x faster                                                     |
| logging_silent             | 60.5 ns                                                     | 53.1 ns: 1.14x faster                                                     |
| logging_format             | 6.72 us                                                     | 5.92 us: 1.13x faster                                                     |
| generators                 | 22.5 ms                                                     | 19.9 ms: 1.13x faster                                                     |
| pprint_safe_repr           | 513 ms                                                      | 454 ms: 1.13x faster                                                      |
| raytrace                   | 192 ms                                                      | 170 ms: 1.13x faster                                                      |
| pprint_pformat             | 1.05 sec                                                    | 930 ms: 1.12x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 12.7 ms: 1.12x faster                                                     |
| sqlite_synth               | 1.76 us                                                     | 1.59 us: 1.11x faster                                                     |
| bench_thread_pool          | 857 us                                                      | 773 us: 1.11x faster                                                      |
| chaos                      | 43.3 ms                                                     | 39.1 ms: 1.11x faster                                                     |
| regex_dna                  | 126 ms                                                      | 115 ms: 1.10x faster                                                      |
| fannkuch                   | 247 ms                                                      | 225 ms: 1.10x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 59.6 ms: 1.09x faster                                                     |
| xml_etree_generate         | 55.8 ms                                                     | 51.7 ms: 1.08x faster                                                     |
| tornado_http               | 89.5 ms                                                     | 83.1 ms: 1.08x faster                                                     |
| pathlib                    | 80.5 ms                                                     | 74.9 ms: 1.07x faster                                                     |
| unpickle_pure_python       | 133 us                                                      | 125 us: 1.07x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 60.0 ms: 1.05x faster                                                     |
| asyncio_tcp                | 487 ms                                                      | 466 ms: 1.05x faster                                                      |
| xml_etree_process          | 37.7 ms                                                     | 36.1 ms: 1.04x faster                                                     |
| sqlglot_parse              | 804 us                                                      | 771 us: 1.04x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                                     |
| json                       | 3.05 ms                                                     | 2.94 ms: 1.04x faster                                                     |
| meteor_contest             | 74.6 ms                                                     | 72.1 ms: 1.03x faster                                                     |
| go                         | 91.6 ms                                                     | 88.6 ms: 1.03x faster                                                     |
| pickle                     | 7.43 us                                                     | 7.20 us: 1.03x faster                                                     |
| deltablue                  | 2.16 ms                                                     | 2.10 ms: 1.03x faster                                                     |
| pickle_dict                | 18.4 us                                                     | 17.9 us: 1.03x faster                                                     |
| sqlglot_transpile          | 1.02 ms                                                     | 998 us: 1.02x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 85.8 ms: 1.02x faster                                                     |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 91.4 ms: 1.02x faster                                                     |
| sympy_str                  | 175 ms                                                      | 173 ms: 1.01x faster                                                      |
| richards                   | 28.4 ms                                                     | 28.1 ms: 1.01x faster                                                     |
| bench_mp_pool              | 69.2 ms                                                     | 68.6 ms: 1.01x faster                                                     |
| richards_super             | 32.1 ms                                                     | 31.8 ms: 1.01x faster                                                     |
| sympy_sum                  | 91.5 ms                                                     | 90.8 ms: 1.01x faster                                                     |
| sqlglot_optimize           | 34.5 ms                                                     | 35.0 ms: 1.01x slower                                                     |
| json_loads                 | 13.9 us                                                     | 14.1 us: 1.01x slower                                                     |
| python_startup_no_site     | 16.2 ms                                                     | 16.6 ms: 1.02x slower                                                     |
| gc_traversal               | 1.52 ms                                                     | 1.56 ms: 1.03x slower                                                     |
| async_generators           | 239 ms                                                      | 248 ms: 1.03x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 81.7 ms: 1.04x slower                                                     |
| 2to3                       | 218 ms                                                      | 227 ms: 1.04x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.73 sec: 1.04x slower                                                    |
| django_template            | 22.9 ms                                                     | 24.0 ms: 1.05x slower                                                     |
| sympy_expand               | 284 ms                                                      | 297 ms: 1.05x slower                                                      |
| python_startup             | 19.5 ms                                                     | 20.4 ms: 1.05x slower                                                     |
| unpickle_list              | 2.75 us                                                     | 2.88 us: 1.05x slower                                                     |
| mdp                        | 1.37 sec                                                    | 1.44 sec: 1.05x slower                                                    |
| sympy_integrate            | 13.0 ms                                                     | 13.6 ms: 1.05x slower                                                     |
| unpickle                   | 8.18 us                                                     | 8.78 us: 1.07x slower                                                     |
| telco                      | 4.13 ms                                                     | 4.47 ms: 1.08x slower                                                     |
| coverage                   | 40.8 ms                                                     | 44.5 ms: 1.09x slower                                                     |
| hexiom                     | 4.10 ms                                                     | 4.62 ms: 1.13x slower                                                     |
| typing_runtime_protocols   | 95.1 us                                                     | 108 us: 1.14x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 69.3 ms: 1.18x slower                                                     |
| pycparser                  | 699 ms                                                      | 825 ms: 1.18x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 905 us: 1.20x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 18.9 ms: 1.33x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.08x faster                                                              |

Benchmark hidden because not significant (2): pickle_list, json_dumps
Ignored benchmarks (9) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (5) of results/bm-20240618-3.14.0a0-a1bdb94-JIT/bm-20240618-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown