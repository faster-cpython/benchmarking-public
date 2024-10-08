# Results vs. 3.12.0

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-amd64
- commit hash: c9a5962
- commit date: 2024-08-29
- overall geometric mean: 1.02x slower
- HPT reliability: 99.91%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 230 ms: 1.05x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.71 sec: 1.03x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 93.8 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 254 ms: 1.44x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 205 ms: 1.39x faster                                                       |
| async_tree_none            | 291 ms                                                      | 211 ms: 1.38x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 569 ms: 1.36x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 264 ms: 1.28x faster                                                       |
| async_tree_io              | 731 ms                                                      | 582 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 402 ms: 1.25x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 393 ms: 1.25x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.32x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 152 ms                                                      | 151 ms: 1.00x faster                                                       |
| float          | 56.8 ms                                                     | 58.6 ms: 1.03x slower                                                      |
| nbody          | 71.9 ms                                                     | 87.8 ms: 1.22x slower                                                      |
| Geometric mean | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 120 ms: 1.06x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 92.4 ms: 1.06x slower                                                      |
| regex_v8       | 14.2 ms                                                     | 15.9 ms: 1.11x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 66.3 ms: 1.02x slower                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 95.0 ms: 1.02x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.5 us: 1.04x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 59.4 ms: 1.06x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 214 us: 1.10x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.32 ms: 1.11x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 42.3 ms: 1.12x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 155 us: 1.17x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.62 sec: 1.19x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.1 ms: 1.12x slower                                                      |
| python_startup         | 19.5 ms                                                     | 22.4 ms: 1.15x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 25.5 ms: 1.11x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.06x slower                                                               |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 254 ms: 1.44x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 205 ms: 1.39x faster                                                       |
| async_tree_none            | 291 ms                                                      | 211 ms: 1.38x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 569 ms: 1.36x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.60 sec: 1.31x faster                                                     |
| async_tree_memoization     | 339 ms                                                      | 264 ms: 1.28x faster                                                       |
| deepcopy                   | 238 us                                                      | 188 us: 1.27x faster                                                       |
| async_tree_io              | 731 ms                                                      | 582 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 402 ms: 1.25x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 393 ms: 1.25x faster                                                       |
| comprehensions             | 14.1 us                                                     | 12.1 us: 1.17x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 21.2 us: 1.12x faster                                                      |
| generators                 | 22.5 ms                                                     | 20.5 ms: 1.10x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.95 us: 1.07x faster                                                      |
| regex_dna                  | 126 ms                                                      | 120 ms: 1.06x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 818 us: 1.05x faster                                                       |
| go                         | 91.6 ms                                                     | 88.1 ms: 1.04x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 42.9 ms: 1.03x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                      |
| pathlib                    | 80.5 ms                                                     | 79.6 ms: 1.01x faster                                                      |
| pidigits                   | 152 ms                                                      | 151 ms: 1.00x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 49.3 ms: 1.02x slower                                                      |
| sympy_str                  | 175 ms                                                      | 178 ms: 1.02x slower                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 66.3 ms: 1.02x slower                                                      |
| logging_format             | 6.72 us                                                     | 6.85 us: 1.02x slower                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 95.0 ms: 1.02x slower                                                      |
| chaos                      | 43.3 ms                                                     | 44.4 ms: 1.03x slower                                                      |
| coroutines                 | 14.3 ms                                                     | 14.6 ms: 1.03x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.71 sec: 1.03x slower                                                     |
| raytrace                   | 192 ms                                                      | 198 ms: 1.03x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.3 ms: 1.03x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.57 ms: 1.03x slower                                                      |
| nqueens                    | 62.8 ms                                                     | 64.7 ms: 1.03x slower                                                      |
| float                      | 56.8 ms                                                     | 58.6 ms: 1.03x slower                                                      |
| logging_simple             | 6.28 us                                                     | 6.48 us: 1.03x slower                                                      |
| sqlglot_normalize          | 187 ms                                                      | 194 ms: 1.04x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.5 us: 1.04x slower                                                      |
| async_generators           | 239 ms                                                      | 251 ms: 1.05x slower                                                       |
| tornado_http               | 89.5 ms                                                     | 93.8 ms: 1.05x slower                                                      |
| 2to3                       | 218 ms                                                      | 230 ms: 1.05x slower                                                       |
| regex_compile              | 87.5 ms                                                     | 92.4 ms: 1.06x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.28 ms: 1.06x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 36.6 ms: 1.06x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 59.4 ms: 1.06x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 79.5 ms: 1.07x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 64.8 ns: 1.07x slower                                                      |
| sympy_expand               | 284 ms                                                      | 305 ms: 1.08x slower                                                       |
| spectral_norm              | 66.9 ms                                                     | 72.2 ms: 1.08x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.50 sec: 1.10x slower                                                     |
| pickle_pure_python         | 195 us                                                      | 214 us: 1.10x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.15 sec: 1.10x slower                                                     |
| asyncio_tcp                | 487 ms                                                      | 536 ms: 1.10x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.52 ms: 1.10x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 569 ms: 1.11x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 65.3 ms: 1.11x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 6.32 ms: 1.11x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.13 ms: 1.11x slower                                                      |
| pyflate                    | 295 ms                                                      | 327 ms: 1.11x slower                                                       |
| django_template            | 22.9 ms                                                     | 25.5 ms: 1.11x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 15.9 ms: 1.11x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 18.1 ms: 1.12x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 42.3 ms: 1.12x slower                                                      |
| sqlglot_parse              | 804 us                                                      | 910 us: 1.13x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.92 ms: 1.14x slower                                                      |
| richards                   | 28.4 ms                                                     | 32.5 ms: 1.15x slower                                                      |
| python_startup             | 19.5 ms                                                     | 22.4 ms: 1.15x slower                                                      |
| richards_super             | 32.1 ms                                                     | 37.2 ms: 1.16x slower                                                      |
| scimark_fft                | 184 ms                                                      | 214 ms: 1.16x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 155 us: 1.17x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 112 us: 1.18x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 51.6 ms: 1.18x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.62 sec: 1.19x slower                                                     |
| scimark_sor                | 78.8 ms                                                     | 93.8 ms: 1.19x slower                                                      |
| pycparser                  | 699 ms                                                      | 839 ms: 1.20x slower                                                       |
| fannkuch                   | 247 ms                                                      | 300 ms: 1.22x slower                                                       |
| nbody                      | 71.9 ms                                                     | 87.8 ms: 1.22x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 919 us: 1.22x slower                                                       |
| coverage                   | 40.8 ms                                                     | 49.9 ms: 1.22x slower                                                      |
| telco                      | 4.13 ms                                                     | 5.20 ms: 1.26x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (4): json, sympy_sum, bench_mp_pool, mako
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240829-3.14.0a0-c9a5962/bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.91% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown