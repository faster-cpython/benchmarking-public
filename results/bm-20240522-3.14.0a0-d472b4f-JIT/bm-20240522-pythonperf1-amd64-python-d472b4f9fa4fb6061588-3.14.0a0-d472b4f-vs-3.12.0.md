# Results vs. 3.12.0

- fork: python
- ref: d472b4f9fa4fb6061588
- machine: windows-amd64
- commit hash: d472b4f
- commit date: 2024-05-22
- overall geometric mean: 1.05x faster
- HPT reliability: 99.15%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240522-pythonperf1-amd64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 235 ms: 1.08x slower                                                       |
| chameleon      | 4.98 ms                                                     | 5.13 ms: 1.03x slower                                                      |
| docutils       | 1.66 sec                                                    | 1.79 sec: 1.08x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 86.0 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240522-pythonperf1-amd64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 270 ms: 1.36x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 212 ms: 1.34x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 390 ms: 1.29x faster                                                       |
| async_tree_none            | 291 ms                                                      | 232 ms: 1.25x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 623 ms: 1.24x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 403 ms: 1.21x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 281 ms: 1.21x faster                                                       |
| async_tree_io              | 731 ms                                                      | 610 ms: 1.20x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.26x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240522-pythonperf1-amd64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 51.2 ms: 1.40x faster                                                      |
| float          | 56.8 ms                                                     | 45.2 ms: 1.26x faster                                                      |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240522-pythonperf1-amd64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 122 ms: 1.04x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.60 ms: 1.01x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 89.3 ms: 1.02x slower                                                      |
| regex_v8       | 14.2 ms                                                     | 16.2 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240522-pythonperf1-amd64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 172 us: 1.13x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.23 sec: 1.11x faster                                                     |
| xml_etree_iterparse  | 65.2 ms                                                     | 59.8 ms: 1.09x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 51.7 ms: 1.08x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 89.4 ms: 1.04x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 36.5 ms: 1.03x faster                                                      |
| unpickle_pure_python | 133 us                                                      | 129 us: 1.03x faster                                                       |
| pickle_dict          | 18.4 us                                                     | 18.0 us: 1.02x faster                                                      |
| pickle               | 7.43 us                                                     | 7.35 us: 1.01x faster                                                      |
| json_dumps           | 5.70 ms                                                     | 5.66 ms: 1.01x faster                                                      |
| unpickle_list        | 2.75 us                                                     | 2.79 us: 1.01x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.2 us: 1.02x slower                                                      |
| unpickle             | 8.18 us                                                     | 8.57 us: 1.05x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                               |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240522-pythonperf1-amd64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.1 ms: 1.11x slower                                                      |
| python_startup         | 19.5 ms                                                     | 21.9 ms: 1.13x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240522-pythonperf1-amd64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.03 ms: 1.41x faster                                                      |
| django_template | 22.9 ms                                                     | 26.1 ms: 1.14x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.11x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240522-pythonperf1-amd64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| spectral_norm              | 66.9 ms                                                     | 45.4 ms: 1.47x faster                                                      |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.45 sec: 1.45x faster                                                     |
| mako                       | 7.09 ms                                                     | 5.03 ms: 1.41x faster                                                      |
| nbody                      | 71.9 ms                                                     | 51.2 ms: 1.40x faster                                                      |
| comprehensions             | 14.1 us                                                     | 10.2 us: 1.38x faster                                                      |
| async_tree_memoization_tg  | 367 ms                                                      | 270 ms: 1.36x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 212 ms: 1.34x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 390 ms: 1.29x faster                                                       |
| float                      | 56.8 ms                                                     | 45.2 ms: 1.26x faster                                                      |
| scimark_fft                | 184 ms                                                      | 147 ms: 1.26x faster                                                       |
| async_tree_none            | 291 ms                                                      | 232 ms: 1.25x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 623 ms: 1.24x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 403 ms: 1.21x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 281 ms: 1.21x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.13 ms: 1.20x faster                                                      |
| async_tree_io              | 731 ms                                                      | 610 ms: 1.20x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 41.1 ms: 1.18x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 38.1 ms: 1.15x faster                                                      |
| pyflate                    | 295 ms                                                      | 259 ms: 1.14x faster                                                       |
| pickle_pure_python         | 195 us                                                      | 172 us: 1.13x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 20.9 us: 1.13x faster                                                      |
| fannkuch                   | 247 ms                                                      | 218 ms: 1.13x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.57 us: 1.12x faster                                                      |
| pprint_safe_repr           | 513 ms                                                      | 460 ms: 1.12x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 941 ms: 1.11x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.23 sec: 1.11x faster                                                     |
| raytrace                   | 192 ms                                                      | 177 ms: 1.09x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 59.8 ms: 1.09x faster                                                      |
| chaos                      | 43.3 ms                                                     | 39.8 ms: 1.09x faster                                                      |
| logging_simple             | 6.28 us                                                     | 5.80 us: 1.08x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 51.7 ms: 1.08x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.22 us: 1.08x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 56.8 ns: 1.07x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 13.6 ms: 1.05x faster                                                      |
| json                       | 3.05 ms                                                     | 2.91 ms: 1.05x faster                                                      |
| tornado_http               | 89.5 ms                                                     | 86.0 ms: 1.04x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 89.4 ms: 1.04x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 72.0 ms: 1.04x faster                                                      |
| regex_dna                  | 126 ms                                                      | 122 ms: 1.04x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 36.5 ms: 1.03x faster                                                      |
| generators                 | 22.5 ms                                                     | 21.8 ms: 1.03x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 129 us: 1.03x faster                                                       |
| pickle_dict                | 18.4 us                                                     | 18.0 us: 1.02x faster                                                      |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 2.06 us: 1.02x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.60 ms: 1.01x faster                                                      |
| pickle                     | 7.43 us                                                     | 7.35 us: 1.01x faster                                                      |
| pathlib                    | 80.5 ms                                                     | 79.5 ms: 1.01x faster                                                      |
| json_dumps                 | 5.70 ms                                                     | 5.66 ms: 1.01x faster                                                      |
| sqlglot_parse              | 804 us                                                      | 813 us: 1.01x slower                                                       |
| unpickle_list              | 2.75 us                                                     | 2.79 us: 1.01x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 70.4 ms: 1.02x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.55 ms: 1.02x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 89.3 ms: 1.02x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.2 us: 1.02x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.40 sec: 1.02x slower                                                     |
| go                         | 91.6 ms                                                     | 93.6 ms: 1.02x slower                                                      |
| sympy_str                  | 175 ms                                                      | 179 ms: 1.02x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.05 ms: 1.03x slower                                                      |
| chameleon                  | 4.98 ms                                                     | 5.13 ms: 1.03x slower                                                      |
| sympy_sum                  | 91.5 ms                                                     | 94.9 ms: 1.04x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 82.4 ms: 1.05x slower                                                      |
| unpickle                   | 8.18 us                                                     | 8.57 us: 1.05x slower                                                      |
| async_generators           | 239 ms                                                      | 252 ms: 1.05x slower                                                       |
| richards                   | 28.4 ms                                                     | 29.9 ms: 1.05x slower                                                      |
| pycparser                  | 699 ms                                                      | 742 ms: 1.06x slower                                                       |
| richards_super             | 32.1 ms                                                     | 34.1 ms: 1.06x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.79 sec: 1.08x slower                                                     |
| 2to3                       | 218 ms                                                      | 235 ms: 1.08x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 37.3 ms: 1.08x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 14.1 ms: 1.09x slower                                                      |
| coverage                   | 40.8 ms                                                     | 44.4 ms: 1.09x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.38 ms: 1.10x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.56 ms: 1.10x slower                                                      |
| sympy_expand               | 284 ms                                                      | 315 ms: 1.11x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 18.1 ms: 1.11x slower                                                      |
| python_startup             | 19.5 ms                                                     | 21.9 ms: 1.13x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 16.2 ms: 1.14x slower                                                      |
| django_template            | 22.9 ms                                                     | 26.1 ms: 1.14x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.71 ms: 1.15x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 890 us: 1.18x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 114 us: 1.20x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 73.1 ms: 1.24x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (5): asyncio_tcp, pickle_list, bench_thread_pool, deepcopy, nqueens
Ignored benchmarks (8) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (6) of results/bm-20240522-3.14.0a0-d472b4f-JIT/bm-20240522-pythonperf1-amd64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.15% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown