# Results vs. 3.12.0

- fork: brandtbucher
- ref: no_cold_exits
- machine: windows-amd64
- commit hash: f837cc6
- commit date: 2024-06-10
- overall geometric mean: 1.05x faster
- HPT reliability: 99.92%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240610-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 230 ms: 1.06x slower                                                      |
| docutils       | 1.66 sec                                                    | 1.77 sec: 1.07x slower                                                    |
| tornado_http   | 89.5 ms                                                     | 85.5 ms: 1.05x faster                                                     |
| Geometric mean | (ref)                                                       | 1.02x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240610-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 271 ms: 1.35x faster                                                      |
| async_tree_none_tg         | 285 ms                                                      | 213 ms: 1.34x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 386 ms: 1.30x faster                                                      |
| async_tree_none            | 291 ms                                                      | 232 ms: 1.25x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 619 ms: 1.25x faster                                                      |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 402 ms: 1.22x faster                                                      |
| async_tree_memoization     | 339 ms                                                      | 280 ms: 1.21x faster                                                      |
| async_tree_io              | 731 ms                                                      | 610 ms: 1.20x faster                                                      |
| Geometric mean             | (ref)                                                       | 1.26x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240610-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 44.0 ms: 1.29x faster                                                     |
| nbody          | 71.9 ms                                                     | 56.2 ms: 1.28x faster                                                     |
| pidigits       | 152 ms                                                      | 150 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                       | 1.19x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240610-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 116 ms: 1.09x faster                                                      |
| regex_effbot   | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                                     |
| regex_v8       | 14.2 ms                                                     | 14.4 ms: 1.01x slower                                                     |
| regex_compile  | 87.5 ms                                                     | 88.3 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                       | 1.03x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240610-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 172 us: 1.13x faster                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.22 sec: 1.12x faster                                                    |
| xml_etree_generate   | 55.8 ms                                                     | 51.7 ms: 1.08x faster                                                     |
| pickle_dict          | 18.4 us                                                     | 17.6 us: 1.05x faster                                                     |
| unpickle_pure_python | 133 us                                                      | 128 us: 1.04x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 36.4 ms: 1.04x faster                                                     |
| pickle               | 7.43 us                                                     | 7.25 us: 1.03x faster                                                     |
| xml_etree_iterparse  | 65.2 ms                                                     | 64.2 ms: 1.01x faster                                                     |
| json_dumps           | 5.70 ms                                                     | 5.62 ms: 1.01x faster                                                     |
| json_loads           | 13.9 us                                                     | 14.2 us: 1.02x slower                                                     |
| unpickle_list        | 2.75 us                                                     | 2.87 us: 1.04x slower                                                     |
| unpickle             | 8.18 us                                                     | 8.81 us: 1.08x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                              |

Benchmark hidden because not significant (2): xml_etree_parse, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240610-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.0 ms: 1.05x slower                                                     |
| python_startup         | 19.5 ms                                                     | 20.5 ms: 1.05x slower                                                     |
| Geometric mean         | (ref)                                                       | 1.05x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240610-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.25 ms: 1.35x faster                                                     |
| django_template | 22.9 ms                                                     | 26.1 ms: 1.14x slower                                                     |
| Geometric mean  | (ref)                                                       | 1.09x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240610-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.42 sec: 1.48x faster                                                    |
| spectral_norm              | 66.9 ms                                                     | 45.4 ms: 1.47x faster                                                     |
| comprehensions             | 14.1 us                                                     | 10.2 us: 1.39x faster                                                     |
| async_tree_memoization_tg  | 367 ms                                                      | 271 ms: 1.35x faster                                                      |
| mako                       | 7.09 ms                                                     | 5.25 ms: 1.35x faster                                                     |
| async_tree_none_tg         | 285 ms                                                      | 213 ms: 1.34x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 386 ms: 1.30x faster                                                      |
| float                      | 56.8 ms                                                     | 44.0 ms: 1.29x faster                                                     |
| nbody                      | 71.9 ms                                                     | 56.2 ms: 1.28x faster                                                     |
| async_tree_none            | 291 ms                                                      | 232 ms: 1.25x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 619 ms: 1.25x faster                                                      |
| scimark_fft                | 184 ms                                                      | 148 ms: 1.24x faster                                                      |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 402 ms: 1.22x faster                                                      |
| async_tree_memoization     | 339 ms                                                      | 280 ms: 1.21x faster                                                      |
| async_tree_io              | 731 ms                                                      | 610 ms: 1.20x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.14 ms: 1.20x faster                                                     |
| crypto_pyaes               | 48.5 ms                                                     | 41.0 ms: 1.18x faster                                                     |
| deepcopy_memo              | 23.7 us                                                     | 20.7 us: 1.15x faster                                                     |
| scimark_monte_carlo        | 43.7 ms                                                     | 38.2 ms: 1.14x faster                                                     |
| pyflate                    | 295 ms                                                      | 259 ms: 1.14x faster                                                      |
| pickle_pure_python         | 195 us                                                      | 172 us: 1.13x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.22 sec: 1.12x faster                                                    |
| sqlite_synth               | 1.76 us                                                     | 1.59 us: 1.11x faster                                                     |
| fannkuch                   | 247 ms                                                      | 223 ms: 1.11x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 54.8 ns: 1.10x faster                                                     |
| raytrace                   | 192 ms                                                      | 175 ms: 1.10x faster                                                      |
| pprint_safe_repr           | 513 ms                                                      | 467 ms: 1.10x faster                                                      |
| pprint_pformat             | 1.05 sec                                                    | 954 ms: 1.10x faster                                                      |
| chaos                      | 43.3 ms                                                     | 39.7 ms: 1.09x faster                                                     |
| regex_dna                  | 126 ms                                                      | 116 ms: 1.09x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 13.2 ms: 1.08x faster                                                     |
| xml_etree_generate         | 55.8 ms                                                     | 51.7 ms: 1.08x faster                                                     |
| pathlib                    | 80.5 ms                                                     | 75.3 ms: 1.07x faster                                                     |
| generators                 | 22.5 ms                                                     | 21.1 ms: 1.07x faster                                                     |
| logging_simple             | 6.28 us                                                     | 5.92 us: 1.06x faster                                                     |
| logging_format             | 6.72 us                                                     | 6.36 us: 1.06x faster                                                     |
| bench_thread_pool          | 857 us                                                      | 817 us: 1.05x faster                                                      |
| tornado_http               | 89.5 ms                                                     | 85.5 ms: 1.05x faster                                                     |
| pickle_dict                | 18.4 us                                                     | 17.6 us: 1.05x faster                                                     |
| unpickle_pure_python       | 133 us                                                      | 128 us: 1.04x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                                     |
| xml_etree_process          | 37.7 ms                                                     | 36.4 ms: 1.04x faster                                                     |
| asyncio_tcp                | 487 ms                                                      | 471 ms: 1.04x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 60.8 ms: 1.03x faster                                                     |
| meteor_contest             | 74.6 ms                                                     | 72.7 ms: 1.03x faster                                                     |
| pickle                     | 7.43 us                                                     | 7.25 us: 1.03x faster                                                     |
| richards                   | 28.4 ms                                                     | 27.8 ms: 1.02x faster                                                     |
| richards_super             | 32.1 ms                                                     | 31.4 ms: 1.02x faster                                                     |
| xml_etree_iterparse        | 65.2 ms                                                     | 64.2 ms: 1.01x faster                                                     |
| json_dumps                 | 5.70 ms                                                     | 5.62 ms: 1.01x faster                                                     |
| pidigits                   | 152 ms                                                      | 150 ms: 1.01x faster                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 68.4 ms: 1.01x faster                                                     |
| sqlglot_parse              | 804 us                                                      | 799 us: 1.01x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 2.11 us: 1.01x slower                                                     |
| regex_v8                   | 14.2 ms                                                     | 14.4 ms: 1.01x slower                                                     |
| regex_compile              | 87.5 ms                                                     | 88.3 ms: 1.01x slower                                                     |
| go                         | 91.6 ms                                                     | 92.4 ms: 1.01x slower                                                     |
| sqlglot_transpile          | 1.02 ms                                                     | 1.03 ms: 1.01x slower                                                     |
| sympy_str                  | 175 ms                                                      | 178 ms: 1.02x slower                                                      |
| sympy_sum                  | 91.5 ms                                                     | 93.3 ms: 1.02x slower                                                     |
| mdp                        | 1.37 sec                                                    | 1.40 sec: 1.02x slower                                                    |
| json_loads                 | 13.9 us                                                     | 14.2 us: 1.02x slower                                                     |
| gc_traversal               | 1.52 ms                                                     | 1.57 ms: 1.03x slower                                                     |
| unpickle_list              | 2.75 us                                                     | 2.87 us: 1.04x slower                                                     |
| python_startup_no_site     | 16.2 ms                                                     | 17.0 ms: 1.05x slower                                                     |
| python_startup             | 19.5 ms                                                     | 20.5 ms: 1.05x slower                                                     |
| 2to3                       | 218 ms                                                      | 230 ms: 1.06x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 36.6 ms: 1.06x slower                                                     |
| scimark_sor                | 78.8 ms                                                     | 83.8 ms: 1.06x slower                                                     |
| docutils                   | 1.66 sec                                                    | 1.77 sec: 1.07x slower                                                    |
| async_generators           | 239 ms                                                      | 257 ms: 1.07x slower                                                      |
| unpickle                   | 8.18 us                                                     | 8.81 us: 1.08x slower                                                     |
| pycparser                  | 699 ms                                                      | 754 ms: 1.08x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 14.0 ms: 1.08x slower                                                     |
| deltablue                  | 2.16 ms                                                     | 2.34 ms: 1.08x slower                                                     |
| coverage                   | 40.8 ms                                                     | 44.1 ms: 1.08x slower                                                     |
| sympy_expand               | 284 ms                                                      | 309 ms: 1.09x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.60 ms: 1.12x slower                                                     |
| telco                      | 4.13 ms                                                     | 4.68 ms: 1.13x slower                                                     |
| django_template            | 22.9 ms                                                     | 26.1 ms: 1.14x slower                                                     |
| scimark_lu                 | 58.9 ms                                                     | 70.4 ms: 1.20x slower                                                     |
| create_gc_cycles           | 752 us                                                      | 907 us: 1.21x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 115 us: 1.21x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                              |

Benchmark hidden because not significant (4): json, xml_etree_parse, pickle_list, deepcopy
Ignored benchmarks (9) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (5) of results/bm-20240610-3.14.0a0-f837cc6-JIT/bm-20240610-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.92% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown