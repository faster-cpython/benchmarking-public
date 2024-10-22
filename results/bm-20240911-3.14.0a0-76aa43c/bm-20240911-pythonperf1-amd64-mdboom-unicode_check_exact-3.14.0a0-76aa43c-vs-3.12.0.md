# Results vs. 3.12.0

- fork: mdboom
- ref: unicode_check_exact
- machine: windows-amd64
- commit hash: 76aa43c
- commit date: 2024-09-11
- overall geometric mean: 1.01x faster
- HPT reliability: 83.46%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 220 ms: 1.01x slower                                                      |
| docutils       | 1.66 sec                                                    | 1.68 sec: 1.01x slower                                                    |
| tornado_http   | 89.5 ms                                                     | 83.5 ms: 1.07x faster                                                     |
| Geometric mean | (ref)                                                       | 1.02x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 251 ms: 1.46x faster                                                      |
| async_tree_none_tg         | 285 ms                                                      | 199 ms: 1.43x faster                                                      |
| async_tree_none            | 291 ms                                                      | 206 ms: 1.42x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 560 ms: 1.38x faster                                                      |
| async_tree_memoization     | 339 ms                                                      | 261 ms: 1.30x faster                                                      |
| async_tree_io              | 731 ms                                                      | 571 ms: 1.28x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 396 ms: 1.27x faster                                                      |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 390 ms: 1.25x faster                                                      |
| Geometric mean             | (ref)                                                       | 1.35x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 54.2 ms: 1.05x faster                                                     |
| pidigits       | 152 ms                                                      | 150 ms: 1.01x faster                                                      |
| nbody          | 71.9 ms                                                     | 82.1 ms: 1.14x slower                                                     |
| Geometric mean | (ref)                                                       | 1.02x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 114 ms: 1.11x faster                                                      |
| regex_effbot   | 1.62 ms                                                     | 1.54 ms: 1.05x faster                                                     |
| regex_v8       | 14.2 ms                                                     | 14.4 ms: 1.01x slower                                                     |
| regex_compile  | 87.5 ms                                                     | 89.2 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                       | 1.03x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle               | 7.43 us                                                     | 7.15 us: 1.04x faster                                                     |
| xml_etree_iterparse  | 65.2 ms                                                     | 64.5 ms: 1.01x faster                                                     |
| unpickle_list        | 2.75 us                                                     | 2.73 us: 1.01x faster                                                     |
| xml_etree_generate   | 55.8 ms                                                     | 57.2 ms: 1.03x slower                                                     |
| pickle_list          | 2.83 us                                                     | 2.91 us: 1.03x slower                                                     |
| pickle_dict          | 18.4 us                                                     | 19.2 us: 1.04x slower                                                     |
| json_loads           | 13.9 us                                                     | 14.5 us: 1.04x slower                                                     |
| pickle_pure_python   | 195 us                                                      | 207 us: 1.06x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 40.3 ms: 1.07x slower                                                     |
| json_dumps           | 5.70 ms                                                     | 6.14 ms: 1.08x slower                                                     |
| unpickle_pure_python | 133 us                                                      | 147 us: 1.10x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.55 sec: 1.13x slower                                                    |
| unpickle             | 8.18 us                                                     | 9.50 us: 1.16x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.05x slower                                                              |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.3 ms: 1.07x slower                                                     |
| python_startup         | 19.5 ms                                                     | 21.3 ms: 1.09x slower                                                     |
| Geometric mean         | (ref)                                                       | 1.08x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.84 ms: 1.04x faster                                                     |
| django_template | 22.9 ms                                                     | 24.4 ms: 1.06x slower                                                     |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 251 ms: 1.46x faster                                                      |
| async_tree_none_tg         | 285 ms                                                      | 199 ms: 1.43x faster                                                      |
| async_tree_none            | 291 ms                                                      | 206 ms: 1.42x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 560 ms: 1.38x faster                                                      |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.58 sec: 1.33x faster                                                    |
| async_tree_memoization     | 339 ms                                                      | 261 ms: 1.30x faster                                                      |
| async_tree_io              | 731 ms                                                      | 571 ms: 1.28x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 396 ms: 1.27x faster                                                      |
| deepcopy                   | 238 us                                                      | 190 us: 1.26x faster                                                      |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 390 ms: 1.25x faster                                                      |
| comprehensions             | 14.1 us                                                     | 11.5 us: 1.23x faster                                                     |
| deepcopy_memo              | 23.7 us                                                     | 20.2 us: 1.18x faster                                                     |
| regex_dna                  | 126 ms                                                      | 114 ms: 1.11x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.62 us: 1.09x faster                                                     |
| deepcopy_reduce            | 2.09 us                                                     | 1.93 us: 1.09x faster                                                     |
| pathlib                    | 80.5 ms                                                     | 74.2 ms: 1.08x faster                                                     |
| go                         | 91.6 ms                                                     | 84.6 ms: 1.08x faster                                                     |
| tornado_http               | 89.5 ms                                                     | 83.5 ms: 1.07x faster                                                     |
| generators                 | 22.5 ms                                                     | 21.1 ms: 1.07x faster                                                     |
| bench_thread_pool          | 857 us                                                      | 807 us: 1.06x faster                                                      |
| asyncio_tcp                | 487 ms                                                      | 462 ms: 1.06x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 42.1 ms: 1.05x faster                                                     |
| regex_effbot               | 1.62 ms                                                     | 1.54 ms: 1.05x faster                                                     |
| raytrace                   | 192 ms                                                      | 184 ms: 1.05x faster                                                      |
| float                      | 56.8 ms                                                     | 54.2 ms: 1.05x faster                                                     |
| pickle                     | 7.43 us                                                     | 7.15 us: 1.04x faster                                                     |
| mako                       | 7.09 ms                                                     | 6.84 ms: 1.04x faster                                                     |
| sympy_sum                  | 91.5 ms                                                     | 89.1 ms: 1.03x faster                                                     |
| bench_mp_pool              | 69.2 ms                                                     | 67.4 ms: 1.03x faster                                                     |
| crypto_pyaes               | 48.5 ms                                                     | 47.2 ms: 1.03x faster                                                     |
| spectral_norm              | 66.9 ms                                                     | 65.3 ms: 1.03x faster                                                     |
| json                       | 3.05 ms                                                     | 3.00 ms: 1.02x faster                                                     |
| pidigits                   | 152 ms                                                      | 150 ms: 1.01x faster                                                      |
| chaos                      | 43.3 ms                                                     | 42.9 ms: 1.01x faster                                                     |
| xml_etree_iterparse        | 65.2 ms                                                     | 64.5 ms: 1.01x faster                                                     |
| unpickle_list              | 2.75 us                                                     | 2.73 us: 1.01x faster                                                     |
| logging_format             | 6.72 us                                                     | 6.67 us: 1.01x faster                                                     |
| logging_simple             | 6.28 us                                                     | 6.24 us: 1.01x faster                                                     |
| async_generators           | 239 ms                                                      | 241 ms: 1.01x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 13.0 ms: 1.01x slower                                                     |
| 2to3                       | 218 ms                                                      | 220 ms: 1.01x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 14.4 ms: 1.01x slower                                                     |
| docutils                   | 1.66 sec                                                    | 1.68 sec: 1.01x slower                                                    |
| nqueens                    | 62.8 ms                                                     | 63.7 ms: 1.02x slower                                                     |
| scimark_lu                 | 58.9 ms                                                     | 59.9 ms: 1.02x slower                                                     |
| mdp                        | 1.37 sec                                                    | 1.40 sec: 1.02x slower                                                    |
| logging_silent             | 60.5 ns                                                     | 61.7 ns: 1.02x slower                                                     |
| regex_compile              | 87.5 ms                                                     | 89.2 ms: 1.02x slower                                                     |
| sqlglot_normalize          | 187 ms                                                      | 191 ms: 1.02x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 57.2 ms: 1.03x slower                                                     |
| pickle_list                | 2.83 us                                                     | 2.91 us: 1.03x slower                                                     |
| deltablue                  | 2.16 ms                                                     | 2.23 ms: 1.03x slower                                                     |
| pickle_dict                | 18.4 us                                                     | 19.2 us: 1.04x slower                                                     |
| json_loads                 | 13.9 us                                                     | 14.5 us: 1.04x slower                                                     |
| sqlglot_optimize           | 34.5 ms                                                     | 36.1 ms: 1.04x slower                                                     |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.67 ms: 1.05x slower                                                     |
| meteor_contest             | 74.6 ms                                                     | 78.1 ms: 1.05x slower                                                     |
| pprint_safe_repr           | 513 ms                                                      | 541 ms: 1.05x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.33 ms: 1.06x slower                                                     |
| pickle_pure_python         | 195 us                                                      | 207 us: 1.06x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.11 sec: 1.06x slower                                                    |
| django_template            | 22.9 ms                                                     | 24.4 ms: 1.06x slower                                                     |
| sqlglot_transpile          | 1.02 ms                                                     | 1.09 ms: 1.06x slower                                                     |
| python_startup_no_site     | 16.2 ms                                                     | 17.3 ms: 1.07x slower                                                     |
| xml_etree_process          | 37.7 ms                                                     | 40.3 ms: 1.07x slower                                                     |
| sympy_expand               | 284 ms                                                      | 304 ms: 1.07x slower                                                      |
| pyflate                    | 295 ms                                                      | 316 ms: 1.07x slower                                                      |
| pycparser                  | 699 ms                                                      | 751 ms: 1.07x slower                                                      |
| scimark_fft                | 184 ms                                                      | 199 ms: 1.08x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 6.14 ms: 1.08x slower                                                     |
| sqlglot_parse              | 804 us                                                      | 868 us: 1.08x slower                                                      |
| python_startup             | 19.5 ms                                                     | 21.3 ms: 1.09x slower                                                     |
| scimark_sor                | 78.8 ms                                                     | 86.1 ms: 1.09x slower                                                     |
| unpickle_pure_python       | 133 us                                                      | 147 us: 1.10x slower                                                      |
| richards_super             | 32.1 ms                                                     | 35.5 ms: 1.10x slower                                                     |
| richards                   | 28.4 ms                                                     | 31.5 ms: 1.11x slower                                                     |
| scimark_monte_carlo        | 43.7 ms                                                     | 49.1 ms: 1.12x slower                                                     |
| tomli_loads                | 1.37 sec                                                    | 1.55 sec: 1.13x slower                                                    |
| coverage                   | 40.8 ms                                                     | 46.6 ms: 1.14x slower                                                     |
| nbody                      | 71.9 ms                                                     | 82.1 ms: 1.14x slower                                                     |
| unpack_sequence            | 37.5 ns                                                     | 43.2 ns: 1.15x slower                                                     |
| typing_runtime_protocols   | 95.1 us                                                     | 110 us: 1.15x slower                                                      |
| unpickle                   | 8.18 us                                                     | 9.50 us: 1.16x slower                                                     |
| fannkuch                   | 247 ms                                                      | 289 ms: 1.17x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 888 us: 1.18x slower                                                      |
| telco                      | 4.13 ms                                                     | 5.04 ms: 1.22x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                              |

Benchmark hidden because not significant (4): coroutines, xml_etree_parse, sympy_str, gc_traversal
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240911-3.14.0a0-76aa43c/bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 83.46% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown