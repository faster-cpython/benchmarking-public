# Results vs. 3.12.0

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: linux-aarch64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.041x faster
- HPT reliability: 97.21%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 295 ms: 1.04x faster                                                    |
| docutils       | 2.98 sec                                                              | 3.01 sec: 1.01x slower                                                  |
| tornado_http   | 136 ms                                                                | 128 ms: 1.06x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                            |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 424 ms: 1.47x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 558 ms: 1.39x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 422 ms: 1.37x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 555 ms: 1.33x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.14 sec: 1.24x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 737 ms: 1.24x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 728 ms: 1.21x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.19 sec: 1.18x faster                                                  |
| Geometric mean             | (ref)                                                                 | 1.30x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 92.7 ms: 1.01x slower                                                   |
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 110 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 126 ms: 1.09x faster                                                    |
| regex_dna      | 254 ms                                                                | 249 ms: 1.02x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.92 ms: 1.06x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.3 ms: 1.07x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 189 ms: 1.03x faster                                                    |
| unpickle_pure_python | 260 us                                                                | 252 us: 1.03x faster                                                    |
| xml_etree_iterparse  | 150 ms                                                                | 149 ms: 1.01x faster                                                    |
| pickle_list          | 5.25 us                                                               | 5.19 us: 1.01x faster                                                   |
| pickle_pure_python   | 365 us                                                                | 362 us: 1.01x faster                                                    |
| pickle_dict          | 37.3 us                                                               | 37.6 us: 1.01x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                                  |
| json_loads           | 30.7 us                                                               | 31.8 us: 1.04x slower                                                   |
| unpickle_list        | 6.17 us                                                               | 6.41 us: 1.04x slower                                                   |
| unpickle             | 18.5 us                                                               | 19.4 us: 1.05x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.2 ms: 1.08x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (3): xml_etree_generate, xml_etree_process, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.62 ms: 1.03x slower                                                   |
| python_startup         | 11.4 ms                                                               | 12.9 ms: 1.14x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.08x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 41.7 ms: 1.03x slower                                                   |
| mako            | 12.9 ms                                                               | 13.5 ms: 1.05x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 424 ms: 1.47x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 558 ms: 1.39x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 422 ms: 1.37x faster                                                    |
| deepcopy                   | 446 us                                                                | 334 us: 1.33x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 555 ms: 1.33x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 37.7 us: 1.32x faster                                                   |
| generators                 | 43.5 ms                                                               | 34.7 ms: 1.25x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.14 sec: 1.24x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 737 ms: 1.24x faster                                                    |
| comprehensions             | 25.4 us                                                               | 20.6 us: 1.23x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 728 ms: 1.21x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 20.7 ms: 1.18x faster                                                   |
| async_tree_io_tg           | 1.40 sec                                                              | 1.19 sec: 1.18x faster                                                  |
| deepcopy_reduce            | 4.10 us                                                               | 3.52 us: 1.17x faster                                                   |
| raytrace                   | 353 ms                                                                | 303 ms: 1.17x faster                                                    |
| go                         | 157 ms                                                                | 139 ms: 1.13x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.63 us: 1.09x faster                                                   |
| sympy_sum                  | 154 ms                                                                | 142 ms: 1.09x faster                                                    |
| logging_simple             | 7.63 us                                                               | 7.01 us: 1.09x faster                                                   |
| regex_compile              | 137 ms                                                                | 126 ms: 1.09x faster                                                    |
| scimark_lu                 | 146 ms                                                                | 135 ms: 1.08x faster                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 81.3 ms: 1.07x faster                                                   |
| dulwich_log                | 62.0 ms                                                               | 58.3 ms: 1.06x faster                                                   |
| tornado_http               | 136 ms                                                                | 128 ms: 1.06x faster                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.23 ms: 1.06x faster                                                   |
| sympy_str                  | 280 ms                                                                | 264 ms: 1.06x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 3.92 ms: 1.05x faster                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 1.74 ms: 1.05x faster                                                   |
| sqlglot_parse              | 1.46 ms                                                               | 1.40 ms: 1.05x faster                                                   |
| 2to3                       | 308 ms                                                                | 295 ms: 1.04x faster                                                    |
| sympy_integrate            | 21.6 ms                                                               | 20.8 ms: 1.04x faster                                                   |
| chaos                      | 71.4 ms                                                               | 69.0 ms: 1.03x faster                                                   |
| pycparser                  | 1.26 sec                                                              | 1.22 sec: 1.03x faster                                                  |
| xml_etree_parse            | 195 ms                                                                | 189 ms: 1.03x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 82.5 ms: 1.03x faster                                                   |
| unpickle_pure_python       | 260 us                                                                | 252 us: 1.03x faster                                                    |
| mdp                        | 3.41 sec                                                              | 3.33 sec: 1.02x faster                                                  |
| regex_dna                  | 254 ms                                                                | 249 ms: 1.02x faster                                                    |
| async_generators           | 491 ms                                                                | 483 ms: 1.02x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 149 ms: 1.01x faster                                                    |
| pickle_list                | 5.25 us                                                               | 5.19 us: 1.01x faster                                                   |
| coroutines                 | 29.0 ms                                                               | 28.7 ms: 1.01x faster                                                   |
| pickle_pure_python         | 365 us                                                                | 362 us: 1.01x faster                                                    |
| thrift                     | 937 us                                                                | 931 us: 1.01x faster                                                    |
| meteor_contest             | 112 ms                                                                | 111 ms: 1.00x faster                                                    |
| pyflate                    | 559 ms                                                                | 562 ms: 1.01x slower                                                    |
| pickle_dict                | 37.3 us                                                               | 37.6 us: 1.01x slower                                                   |
| float                      | 92.1 ms                                                               | 92.7 ms: 1.01x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.01 sec: 1.01x slower                                                  |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 926 ms: 1.01x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 1.91 sec: 1.01x slower                                                  |
| sympy_expand               | 454 ms                                                                | 460 ms: 1.02x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 101 ms: 1.02x slower                                                    |
| richards_super             | 58.5 ms                                                               | 59.4 ms: 1.02x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.22 sec: 1.02x slower                                                  |
| sqlglot_optimize           | 61.3 ms                                                               | 62.3 ms: 1.02x slower                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                                  |
| asyncio_tcp                | 566 ms                                                                | 576 ms: 1.02x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 7.10 ms: 1.02x slower                                                   |
| django_template            | 40.7 ms                                                               | 41.7 ms: 1.03x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.62 ms: 1.03x slower                                                   |
| richards                   | 50.9 ms                                                               | 52.7 ms: 1.03x slower                                                   |
| json_loads                 | 30.7 us                                                               | 31.8 us: 1.04x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.42 ms: 1.04x slower                                                   |
| fannkuch                   | 443 ms                                                                | 460 ms: 1.04x slower                                                    |
| unpickle_list              | 6.17 us                                                               | 6.41 us: 1.04x slower                                                   |
| logging_silent             | 127 ns                                                                | 133 ns: 1.05x slower                                                    |
| unpickle                   | 18.5 us                                                               | 19.4 us: 1.05x slower                                                   |
| mako                       | 12.9 ms                                                               | 13.5 ms: 1.05x slower                                                   |
| scimark_sor                | 150 ms                                                                | 157 ms: 1.05x slower                                                    |
| nbody                      | 105 ms                                                                | 110 ms: 1.05x slower                                                    |
| scimark_fft                | 418 ms                                                                | 442 ms: 1.06x slower                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.92 ms: 1.06x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 193 us: 1.07x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 30.3 ms: 1.07x slower                                                   |
| spectral_norm              | 131 ms                                                                | 140 ms: 1.07x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.2 ms: 1.08x slower                                                   |
| coverage                   | 87.3 ms                                                               | 97.5 ms: 1.12x slower                                                   |
| python_startup             | 11.4 ms                                                               | 12.9 ms: 1.14x slower                                                   |
| telco                      | 8.51 ms                                                               | 9.86 ms: 1.16x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 5.18 ms: 1.18x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.33 ms: 1.21x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.03x faster                                                            |

Benchmark hidden because not significant (12): bench_mp_pool, genshi_xml, xml_etree_generate, genshi_text, json, asyncio_websockets, html5lib, xml_etree_process, pickle, sqlite_synth, sqlglot_normalize, pylint
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240914-3.14.0a0-401fff7/bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: bpe_tokeniser, unpack_sequence

- Geometric mean (including insignificant results): 1.041x faster
# HPT report

- Reliability score: 97.21% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.92x