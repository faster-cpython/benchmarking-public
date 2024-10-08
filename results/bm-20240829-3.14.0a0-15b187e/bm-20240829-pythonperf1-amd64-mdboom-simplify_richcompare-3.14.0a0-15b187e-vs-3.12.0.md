# Results vs. 3.12.0

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-amd64
- commit hash: 15b187e
- commit date: 2024-08-29
- overall geometric mean: 1.01x slower
- HPT reliability: 98.30%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 228 ms: 1.05x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.70 sec: 1.02x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 93.1 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 253 ms: 1.45x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 202 ms: 1.41x faster                                                       |
| async_tree_none            | 291 ms                                                      | 210 ms: 1.39x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 560 ms: 1.38x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 258 ms: 1.31x faster                                                       |
| async_tree_io              | 731 ms                                                      | 579 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 401 ms: 1.25x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 391 ms: 1.25x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.34x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 55.9 ms: 1.02x faster                                                      |
| pidigits       | 152 ms                                                      | 151 ms: 1.01x faster                                                       |
| nbody          | 71.9 ms                                                     | 82.8 ms: 1.15x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 123 ms: 1.03x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.61 ms: 1.01x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 90.9 ms: 1.04x slower                                                      |
| regex_v8       | 14.2 ms                                                     | 15.7 ms: 1.10x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 66.1 ms: 1.01x slower                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 95.0 ms: 1.02x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 57.7 ms: 1.03x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.5 us: 1.05x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 40.5 ms: 1.07x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 210 us: 1.08x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.25 ms: 1.10x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 149 us: 1.12x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.58 sec: 1.16x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.2 ms: 1.12x slower                                                      |
| python_startup         | 19.5 ms                                                     | 22.3 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.90 ms: 1.03x faster                                                      |
| django_template | 22.9 ms                                                     | 24.3 ms: 1.06x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.02x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 253 ms: 1.45x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 202 ms: 1.41x faster                                                       |
| async_tree_none            | 291 ms                                                      | 210 ms: 1.39x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 560 ms: 1.38x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 258 ms: 1.31x faster                                                       |
| deepcopy                   | 238 us                                                      | 186 us: 1.28x faster                                                       |
| async_tree_io              | 731 ms                                                      | 579 ms: 1.26x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.66 sec: 1.26x faster                                                     |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 401 ms: 1.25x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 391 ms: 1.25x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 20.0 us: 1.18x faster                                                      |
| comprehensions             | 14.1 us                                                     | 11.9 us: 1.18x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.92 us: 1.09x faster                                                      |
| go                         | 91.6 ms                                                     | 85.1 ms: 1.08x faster                                                      |
| generators                 | 22.5 ms                                                     | 21.1 ms: 1.07x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 42.5 ms: 1.04x faster                                                      |
| raytrace                   | 192 ms                                                      | 185 ms: 1.04x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 828 us: 1.03x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.90 ms: 1.03x faster                                                      |
| regex_dna                  | 126 ms                                                      | 123 ms: 1.03x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 89.6 ms: 1.02x faster                                                      |
| float                      | 56.8 ms                                                     | 55.9 ms: 1.02x faster                                                      |
| pathlib                    | 80.5 ms                                                     | 79.2 ms: 1.02x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 66.0 ms: 1.01x faster                                                      |
| chaos                      | 43.3 ms                                                     | 42.8 ms: 1.01x faster                                                      |
| pidigits                   | 152 ms                                                      | 151 ms: 1.01x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 14.2 ms: 1.01x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.61 ms: 1.01x faster                                                      |
| sympy_str                  | 175 ms                                                      | 176 ms: 1.01x slower                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 66.1 ms: 1.01x slower                                                      |
| nqueens                    | 62.8 ms                                                     | 63.8 ms: 1.02x slower                                                      |
| async_generators           | 239 ms                                                      | 243 ms: 1.02x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.2 ms: 1.02x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 70.6 ms: 1.02x slower                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 95.0 ms: 1.02x slower                                                      |
| sqlglot_normalize          | 187 ms                                                      | 191 ms: 1.02x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.70 sec: 1.02x slower                                                     |
| gc_traversal               | 1.52 ms                                                     | 1.56 ms: 1.02x slower                                                      |
| logging_simple             | 6.28 us                                                     | 6.45 us: 1.03x slower                                                      |
| logging_format             | 6.72 us                                                     | 6.91 us: 1.03x slower                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.63 ms: 1.03x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 57.7 ms: 1.03x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 35.9 ms: 1.04x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 90.9 ms: 1.04x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 61.2 ms: 1.04x slower                                                      |
| tornado_http               | 89.5 ms                                                     | 93.1 ms: 1.04x slower                                                      |
| 2to3                       | 218 ms                                                      | 228 ms: 1.05x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.5 us: 1.05x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.26 ms: 1.05x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 78.5 ms: 1.05x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 63.7 ns: 1.05x slower                                                      |
| django_template            | 22.9 ms                                                     | 24.3 ms: 1.06x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.37 ms: 1.07x slower                                                      |
| sympy_expand               | 284 ms                                                      | 303 ms: 1.07x slower                                                       |
| scimark_fft                | 184 ms                                                      | 197 ms: 1.07x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 551 ms: 1.07x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 40.5 ms: 1.07x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 210 us: 1.08x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.12 sec: 1.08x slower                                                     |
| sqlglot_transpile          | 1.02 ms                                                     | 1.10 ms: 1.08x slower                                                      |
| asyncio_tcp                | 487 ms                                                      | 529 ms: 1.08x slower                                                       |
| pyflate                    | 295 ms                                                      | 321 ms: 1.09x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.50 sec: 1.10x slower                                                     |
| json_dumps                 | 5.70 ms                                                     | 6.25 ms: 1.10x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 15.7 ms: 1.10x slower                                                      |
| sqlglot_parse              | 804 us                                                      | 886 us: 1.10x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 18.2 ms: 1.12x slower                                                      |
| richards                   | 28.4 ms                                                     | 31.8 ms: 1.12x slower                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 49.0 ms: 1.12x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 149 us: 1.12x slower                                                       |
| richards_super             | 32.1 ms                                                     | 36.0 ms: 1.12x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 89.4 ms: 1.14x slower                                                      |
| python_startup             | 19.5 ms                                                     | 22.3 ms: 1.14x slower                                                      |
| nbody                      | 71.9 ms                                                     | 82.8 ms: 1.15x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.58 sec: 1.16x slower                                                     |
| typing_runtime_protocols   | 95.1 us                                                     | 111 us: 1.16x slower                                                       |
| fannkuch                   | 247 ms                                                      | 288 ms: 1.17x slower                                                       |
| pycparser                  | 699 ms                                                      | 833 ms: 1.19x slower                                                       |
| coverage                   | 40.8 ms                                                     | 48.7 ms: 1.19x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 917 us: 1.22x slower                                                       |
| telco                      | 4.13 ms                                                     | 5.30 ms: 1.28x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (2): crypto_pyaes, json
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240829-3.14.0a0-15b187e/bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 98.30% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown