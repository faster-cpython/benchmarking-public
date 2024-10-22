# Results vs. 3.12.0

- fork: python
- ref: e256a7590a0149feadfe
- machine: windows-amd64
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.00x slower
- HPT reliability: 96.28%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 222 ms: 1.02x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.71 sec: 1.03x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 83.1 ms: 1.08x faster                                                      |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 251 ms: 1.46x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 200 ms: 1.43x faster                                                       |
| async_tree_none            | 291 ms                                                      | 207 ms: 1.41x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 553 ms: 1.39x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 261 ms: 1.30x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 388 ms: 1.29x faster                                                       |
| async_tree_io              | 731 ms                                                      | 566 ms: 1.29x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 386 ms: 1.27x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.35x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 55.2 ms: 1.03x faster                                                      |
| pidigits       | 152 ms                                                      | 150 ms: 1.01x faster                                                       |
| nbody          | 71.9 ms                                                     | 83.2 ms: 1.16x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 118 ms: 1.08x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 14.7 ms: 1.03x slower                                                      |
| regex_compile  | 87.5 ms                                                     | 90.4 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle               | 7.43 us                                                     | 7.04 us: 1.06x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.9 ms: 1.02x faster                                                      |
| pickle_dict          | 18.4 us                                                     | 18.5 us: 1.00x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 2.77 us: 1.01x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 57.7 ms: 1.03x slower                                                      |
| pickle_list          | 2.83 us                                                     | 2.96 us: 1.05x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.8 us: 1.06x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 212 us: 1.08x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 40.9 ms: 1.08x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.35 ms: 1.12x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 149 us: 1.12x slower                                                       |
| unpickle             | 8.18 us                                                     | 9.39 us: 1.15x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.59 sec: 1.17x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.4 ms: 1.13x slower                                                      |
| python_startup         | 19.5 ms                                                     | 22.2 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.81 ms: 1.04x faster                                                      |
| django_template | 22.9 ms                                                     | 24.8 ms: 1.08x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.02x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 251 ms: 1.46x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 200 ms: 1.43x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.48 sec: 1.41x faster                                                     |
| async_tree_none            | 291 ms                                                      | 207 ms: 1.41x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 553 ms: 1.39x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 261 ms: 1.30x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 388 ms: 1.29x faster                                                       |
| async_tree_io              | 731 ms                                                      | 566 ms: 1.29x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 386 ms: 1.27x faster                                                       |
| deepcopy                   | 238 us                                                      | 193 us: 1.24x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.9 us: 1.19x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 20.8 us: 1.14x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.94 us: 1.08x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.63 us: 1.08x faster                                                      |
| tornado_http               | 89.5 ms                                                     | 83.1 ms: 1.08x faster                                                      |
| regex_dna                  | 126 ms                                                      | 118 ms: 1.08x faster                                                       |
| generators                 | 22.5 ms                                                     | 21.0 ms: 1.07x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 802 us: 1.07x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 75.9 ms: 1.06x faster                                                      |
| go                         | 91.6 ms                                                     | 86.6 ms: 1.06x faster                                                      |
| pickle                     | 7.43 us                                                     | 7.04 us: 1.06x faster                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 66.0 ms: 1.05x faster                                                      |
| mako                       | 7.09 ms                                                     | 6.81 ms: 1.04x faster                                                      |
| asyncio_tcp                | 487 ms                                                      | 471 ms: 1.03x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 42.8 ms: 1.03x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| float                      | 56.8 ms                                                     | 55.2 ms: 1.03x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 89.7 ms: 1.02x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.9 ms: 1.02x faster                                                      |
| raytrace                   | 192 ms                                                      | 189 ms: 1.02x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 47.8 ms: 1.02x faster                                                      |
| chaos                      | 43.3 ms                                                     | 42.7 ms: 1.01x faster                                                      |
| pidigits                   | 152 ms                                                      | 150 ms: 1.01x faster                                                       |
| pickle_dict                | 18.4 us                                                     | 18.5 us: 1.00x slower                                                      |
| sympy_str                  | 175 ms                                                      | 176 ms: 1.01x slower                                                       |
| unpickle_list              | 2.75 us                                                     | 2.77 us: 1.01x slower                                                      |
| logging_simple             | 6.28 us                                                     | 6.35 us: 1.01x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 13.1 ms: 1.01x slower                                                      |
| async_generators           | 239 ms                                                      | 243 ms: 1.01x slower                                                       |
| coroutines                 | 14.3 ms                                                     | 14.5 ms: 1.02x slower                                                      |
| 2to3                       | 218 ms                                                      | 222 ms: 1.02x slower                                                       |
| logging_format             | 6.72 us                                                     | 6.85 us: 1.02x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.71 sec: 1.03x slower                                                     |
| regex_v8                   | 14.2 ms                                                     | 14.7 ms: 1.03x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 90.4 ms: 1.03x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 57.7 ms: 1.03x slower                                                      |
| sqlglot_normalize          | 187 ms                                                      | 193 ms: 1.03x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.66 ms: 1.04x slower                                                      |
| spectral_norm              | 66.9 ms                                                     | 69.8 ms: 1.04x slower                                                      |
| nqueens                    | 62.8 ms                                                     | 65.5 ms: 1.04x slower                                                      |
| pickle_list                | 2.83 us                                                     | 2.96 us: 1.05x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 36.3 ms: 1.05x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.44 sec: 1.05x slower                                                     |
| meteor_contest             | 74.6 ms                                                     | 78.6 ms: 1.05x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 63.8 ns: 1.06x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.28 ms: 1.06x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 542 ms: 1.06x slower                                                       |
| pycparser                  | 699 ms                                                      | 740 ms: 1.06x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 62.5 ms: 1.06x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.8 us: 1.06x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.12 sec: 1.07x slower                                                     |
| hexiom                     | 4.10 ms                                                     | 4.39 ms: 1.07x slower                                                      |
| unpack_sequence            | 37.5 ns                                                     | 40.3 ns: 1.08x slower                                                      |
| sympy_expand               | 284 ms                                                      | 306 ms: 1.08x slower                                                       |
| django_template            | 22.9 ms                                                     | 24.8 ms: 1.08x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 212 us: 1.08x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 40.9 ms: 1.08x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.11 ms: 1.08x slower                                                      |
| pyflate                    | 295 ms                                                      | 322 ms: 1.09x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 888 us: 1.10x slower                                                       |
| scimark_fft                | 184 ms                                                      | 204 ms: 1.11x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.35 ms: 1.12x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 149 us: 1.12x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 49.0 ms: 1.12x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 18.4 ms: 1.13x slower                                                      |
| richards_super             | 32.1 ms                                                     | 36.4 ms: 1.14x slower                                                      |
| richards                   | 28.4 ms                                                     | 32.3 ms: 1.14x slower                                                      |
| python_startup             | 19.5 ms                                                     | 22.2 ms: 1.14x slower                                                      |
| unpickle                   | 8.18 us                                                     | 9.39 us: 1.15x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 110 us: 1.15x slower                                                       |
| nbody                      | 71.9 ms                                                     | 83.2 ms: 1.16x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.59 sec: 1.17x slower                                                     |
| create_gc_cycles           | 752 us                                                      | 884 us: 1.18x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 93.1 ms: 1.18x slower                                                      |
| coverage                   | 40.8 ms                                                     | 49.3 ms: 1.21x slower                                                      |
| fannkuch                   | 247 ms                                                      | 299 ms: 1.21x slower                                                       |
| telco                      | 4.13 ms                                                     | 5.09 ms: 1.23x slower                                                      |
| json                       | 3.05 ms                                                     | 4.50 ms: 1.48x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (2): xml_etree_parse, gc_traversal
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240924-3.14.0a0-e256a75/bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 96.28% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown