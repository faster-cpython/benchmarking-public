# Results vs. 3.12.0

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-amd64
- commit hash: 2fa7b0e
- commit date: 2024-09-04
- overall geometric mean: 1.01x slower
- HPT reliability: 99.78%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 228 ms: 1.05x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.70 sec: 1.02x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 93.2 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 255 ms: 1.44x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 206 ms: 1.38x faster                                                       |
| async_tree_none            | 291 ms                                                      | 213 ms: 1.37x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 567 ms: 1.36x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 266 ms: 1.28x faster                                                       |
| async_tree_io              | 731 ms                                                      | 577 ms: 1.27x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 400 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 390 ms: 1.25x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.32x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 152 ms                                                      | 151 ms: 1.01x faster                                                       |
| nbody          | 71.9 ms                                                     | 88.1 ms: 1.23x slower                                                      |
| Geometric mean | (ref)                                                       | 1.07x slower                                                               |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 115 ms: 1.10x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.55 ms: 1.05x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 14.5 ms: 1.02x slower                                                      |
| regex_compile  | 87.5 ms                                                     | 91.6 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 13.9 us                                                     | 14.2 us: 1.02x slower                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 66.6 ms: 1.02x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 57.6 ms: 1.03x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 212 us: 1.09x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 41.3 ms: 1.10x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.27 ms: 1.10x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 155 us: 1.16x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.60 sec: 1.17x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.08x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.1 ms: 1.11x slower                                                      |
| python_startup         | 19.5 ms                                                     | 22.2 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 24.7 ms: 1.08x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 255 ms: 1.44x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 206 ms: 1.38x faster                                                       |
| async_tree_none            | 291 ms                                                      | 213 ms: 1.37x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 567 ms: 1.36x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.62 sec: 1.30x faster                                                     |
| async_tree_memoization     | 339 ms                                                      | 266 ms: 1.28x faster                                                       |
| async_tree_io              | 731 ms                                                      | 577 ms: 1.27x faster                                                       |
| deepcopy                   | 238 us                                                      | 189 us: 1.26x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 400 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 390 ms: 1.25x faster                                                       |
| comprehensions             | 14.1 us                                                     | 12.1 us: 1.16x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 20.7 us: 1.15x faster                                                      |
| regex_dna                  | 126 ms                                                      | 115 ms: 1.10x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.92 us: 1.09x faster                                                      |
| generators                 | 22.5 ms                                                     | 20.7 ms: 1.09x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.55 ms: 1.05x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 42.4 ms: 1.04x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 825 us: 1.04x faster                                                       |
| go                         | 91.6 ms                                                     | 88.6 ms: 1.03x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 90.0 ms: 1.02x faster                                                      |
| pathlib                    | 80.5 ms                                                     | 79.5 ms: 1.01x faster                                                      |
| pidigits                   | 152 ms                                                      | 151 ms: 1.01x faster                                                       |
| sympy_str                  | 175 ms                                                      | 177 ms: 1.01x slower                                                       |
| logging_format             | 6.72 us                                                     | 6.79 us: 1.01x slower                                                      |
| coroutines                 | 14.3 ms                                                     | 14.5 ms: 1.02x slower                                                      |
| logging_simple             | 6.28 us                                                     | 6.37 us: 1.02x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 70.3 ms: 1.02x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 14.5 ms: 1.02x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.2 us: 1.02x slower                                                      |
| chaos                      | 43.3 ms                                                     | 44.2 ms: 1.02x slower                                                      |
| nqueens                    | 62.8 ms                                                     | 64.1 ms: 1.02x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.70 sec: 1.02x slower                                                     |
| xml_etree_iterparse        | 65.2 ms                                                     | 66.6 ms: 1.02x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.56 ms: 1.03x slower                                                      |
| sqlglot_normalize          | 187 ms                                                      | 192 ms: 1.03x slower                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 49.8 ms: 1.03x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 13.3 ms: 1.03x slower                                                      |
| async_generators           | 239 ms                                                      | 247 ms: 1.03x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 57.6 ms: 1.03x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 35.7 ms: 1.03x slower                                                      |
| tornado_http               | 89.5 ms                                                     | 93.2 ms: 1.04x slower                                                      |
| 2to3                       | 218 ms                                                      | 228 ms: 1.05x slower                                                       |
| regex_compile              | 87.5 ms                                                     | 91.6 ms: 1.05x slower                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.69 ms: 1.05x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.28 ms: 1.05x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 78.8 ms: 1.06x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 64.4 ns: 1.06x slower                                                      |
| sympy_expand               | 284 ms                                                      | 303 ms: 1.07x slower                                                       |
| asyncio_tcp                | 487 ms                                                      | 522 ms: 1.07x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 63.1 ms: 1.07x slower                                                      |
| django_template            | 22.9 ms                                                     | 24.7 ms: 1.08x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 212 us: 1.09x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 41.3 ms: 1.10x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 563 ms: 1.10x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.12 ms: 1.10x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 6.27 ms: 1.10x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.15 sec: 1.10x slower                                                     |
| mdp                        | 1.37 sec                                                    | 1.51 sec: 1.10x slower                                                     |
| spectral_norm              | 66.9 ms                                                     | 73.9 ms: 1.10x slower                                                      |
| pyflate                    | 295 ms                                                      | 326 ms: 1.11x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 892 us: 1.11x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 18.1 ms: 1.11x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.56 ms: 1.11x slower                                                      |
| pycparser                  | 699 ms                                                      | 791 ms: 1.13x slower                                                       |
| richards                   | 28.4 ms                                                     | 32.3 ms: 1.14x slower                                                      |
| python_startup             | 19.5 ms                                                     | 22.2 ms: 1.14x slower                                                      |
| richards_super             | 32.1 ms                                                     | 36.7 ms: 1.15x slower                                                      |
| scimark_fft                | 184 ms                                                      | 211 ms: 1.15x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 155 us: 1.16x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 50.9 ms: 1.16x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.60 sec: 1.17x slower                                                     |
| scimark_sor                | 78.8 ms                                                     | 92.7 ms: 1.18x slower                                                      |
| coverage                   | 40.8 ms                                                     | 48.4 ms: 1.19x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 114 us: 1.19x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 917 us: 1.22x slower                                                       |
| nbody                      | 71.9 ms                                                     | 88.1 ms: 1.23x slower                                                      |
| fannkuch                   | 247 ms                                                      | 307 ms: 1.24x slower                                                       |
| telco                      | 4.13 ms                                                     | 5.16 ms: 1.25x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (5): raytrace, mako, float, xml_etree_parse, json
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240904-3.14.0a0-2fa7b0e/bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.78% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown