# Results vs. 3.12.0

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: linux-aarch64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.074x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 380 ms: 1.23x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.98 sec: 1.33x slower                                                  |
| html5lib       | 65.1 ms                                                               | 71.3 ms: 1.10x slower                                                   |
| tornado_http   | 136 ms                                                                | 147 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.18x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 444 ms: 1.41x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 426 ms: 1.36x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 588 ms: 1.32x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 564 ms: 1.31x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.14 sec: 1.23x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 757 ms: 1.21x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.17 sec: 1.20x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 742 ms: 1.19x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.28x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 87.5 ms: 1.05x faster                                                   |
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 114 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 242 ms: 1.05x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.88 ms: 1.05x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 31.5 ms: 1.11x slower                                                   |
| regex_compile  | 137 ms                                                                | 190 ms: 1.39x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.11x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 188 ms: 1.04x faster                                                    |
| xml_etree_generate   | 112 ms                                                                | 111 ms: 1.01x faster                                                    |
| xml_etree_iterparse  | 150 ms                                                                | 149 ms: 1.01x faster                                                    |
| xml_etree_process    | 79.0 ms                                                               | 79.9 ms: 1.01x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 2.63 sec: 1.01x slower                                                  |
| pickle_dict          | 37.3 us                                                               | 38.2 us: 1.02x slower                                                   |
| pickle               | 13.4 us                                                               | 13.8 us: 1.03x slower                                                   |
| json_loads           | 30.7 us                                                               | 31.5 us: 1.03x slower                                                   |
| unpickle_pure_python | 260 us                                                                | 267 us: 1.03x slower                                                    |
| unpickle_list        | 6.17 us                                                               | 6.41 us: 1.04x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 380 us: 1.04x slower                                                    |
| unpickle             | 18.5 us                                                               | 19.4 us: 1.05x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.80 ms: 1.05x slower                                                   |
| python_startup         | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.10x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.1 ms: 1.01x slower                                                   |
| django_template | 40.7 ms                                                               | 50.8 ms: 1.25x slower                                                   |
| genshi_text     | 27.4 ms                                                               | 35.7 ms: 1.30x slower                                                   |
| genshi_xml      | 60.6 ms                                                               | 82.2 ms: 1.36x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.22x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 444 ms: 1.41x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 426 ms: 1.36x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 37.2 us: 1.34x faster                                                   |
| async_tree_memoization     | 777 ms                                                                | 588 ms: 1.32x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 564 ms: 1.31x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.14 sec: 1.23x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 757 ms: 1.21x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.17 sec: 1.20x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 742 ms: 1.19x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 21.5 ms: 1.14x faster                                                   |
| deepcopy                   | 446 us                                                                | 394 us: 1.13x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.86 us: 1.06x faster                                                   |
| float                      | 92.1 ms                                                               | 87.5 ms: 1.05x faster                                                   |
| regex_dna                  | 254 ms                                                                | 242 ms: 1.05x faster                                                    |
| comprehensions             | 25.4 us                                                               | 24.5 us: 1.04x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 188 ms: 1.04x faster                                                    |
| logging_format             | 8.34 us                                                               | 8.20 us: 1.02x faster                                                   |
| logging_simple             | 7.63 us                                                               | 7.52 us: 1.02x faster                                                   |
| coroutines                 | 29.0 ms                                                               | 28.6 ms: 1.02x faster                                                   |
| xml_etree_generate         | 112 ms                                                                | 111 ms: 1.01x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 149 ms: 1.01x faster                                                    |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 663 ms: 1.01x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 79.9 ms: 1.01x slower                                                   |
| mako                       | 12.9 ms                                                               | 13.1 ms: 1.01x slower                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.63 sec: 1.01x slower                                                  |
| scimark_sor                | 150 ms                                                                | 152 ms: 1.02x slower                                                    |
| async_generators           | 491 ms                                                                | 501 ms: 1.02x slower                                                    |
| pickle_dict                | 37.3 us                                                               | 38.2 us: 1.02x slower                                                   |
| scimark_lu                 | 146 ms                                                                | 149 ms: 1.02x slower                                                    |
| pickle                     | 13.4 us                                                               | 13.8 us: 1.03x slower                                                   |
| json_loads                 | 30.7 us                                                               | 31.5 us: 1.03x slower                                                   |
| mdp                        | 3.41 sec                                                              | 3.50 sec: 1.03x slower                                                  |
| unpickle_pure_python       | 260 us                                                                | 267 us: 1.03x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.25 sec: 1.03x slower                                                  |
| sqlite_synth               | 3.77 us                                                               | 3.88 us: 1.03x slower                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 89.4 ms: 1.03x slower                                                   |
| json                       | 5.54 ms                                                               | 5.73 ms: 1.03x slower                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.36 ms: 1.04x slower                                                   |
| unpickle_list              | 6.17 us                                                               | 6.41 us: 1.04x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 380 us: 1.04x slower                                                    |
| thrift                     | 937 us                                                                | 981 us: 1.05x slower                                                    |
| unpickle                   | 18.5 us                                                               | 19.4 us: 1.05x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.80 ms: 1.05x slower                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.88 ms: 1.05x slower                                                   |
| deltablue                  | 4.12 ms                                                               | 4.36 ms: 1.06x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 7.57 ms: 1.07x slower                                                   |
| tornado_http               | 136 ms                                                                | 147 ms: 1.09x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 92.5 ms: 1.09x slower                                                   |
| nbody                      | 105 ms                                                                | 114 ms: 1.09x slower                                                    |
| asyncio_tcp                | 566 ms                                                                | 619 ms: 1.09x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 71.3 ms: 1.10x slower                                                   |
| scimark_fft                | 418 ms                                                                | 459 ms: 1.10x slower                                                    |
| logging_silent             | 127 ns                                                                | 140 ns: 1.10x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.82 ms: 1.10x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                   |
| meteor_contest             | 112 ms                                                                | 124 ms: 1.11x slower                                                    |
| spectral_norm              | 131 ms                                                                | 145 ms: 1.11x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 31.5 ms: 1.11x slower                                                   |
| fannkuch                   | 443 ms                                                                | 503 ms: 1.13x slower                                                    |
| python_startup             | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 207 us: 1.15x slower                                                    |
| coverage                   | 87.3 ms                                                               | 101 ms: 1.15x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 5.10 ms: 1.16x slower                                                   |
| pyflate                    | 559 ms                                                                | 654 ms: 1.17x slower                                                    |
| go                         | 157 ms                                                                | 186 ms: 1.18x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 2.29 ms: 1.19x slower                                                   |
| sqlglot_normalize          | 126 ms                                                                | 151 ms: 1.20x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.77 ms: 1.21x slower                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 2.21 ms: 1.21x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.54 sec: 1.23x slower                                                  |
| telco                      | 8.51 ms                                                               | 10.5 ms: 1.23x slower                                                   |
| 2to3                       | 308 ms                                                                | 380 ms: 1.23x slower                                                    |
| django_template            | 40.7 ms                                                               | 50.8 ms: 1.25x slower                                                   |
| sqlglot_optimize           | 61.3 ms                                                               | 78.9 ms: 1.29x slower                                                   |
| richards_super             | 58.5 ms                                                               | 75.3 ms: 1.29x slower                                                   |
| chaos                      | 71.4 ms                                                               | 92.1 ms: 1.29x slower                                                   |
| nqueens                    | 99.2 ms                                                               | 128 ms: 1.29x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 35.7 ms: 1.30x slower                                                   |
| richards                   | 50.9 ms                                                               | 66.3 ms: 1.30x slower                                                   |
| dulwich_log                | 62.0 ms                                                               | 80.8 ms: 1.30x slower                                                   |
| sympy_str                  | 280 ms                                                                | 368 ms: 1.32x slower                                                    |
| generators                 | 43.5 ms                                                               | 57.4 ms: 1.32x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.98 sec: 1.33x slower                                                  |
| pylint                     | 355 ms                                                                | 473 ms: 1.33x slower                                                    |
| sympy_integrate            | 21.6 ms                                                               | 29.0 ms: 1.34x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 82.2 ms: 1.36x slower                                                   |
| sympy_expand               | 454 ms                                                                | 618 ms: 1.36x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.25 sec: 1.37x slower                                                  |
| pprint_pformat             | 1.88 sec                                                              | 2.60 sec: 1.38x slower                                                  |
| regex_compile              | 137 ms                                                                | 190 ms: 1.39x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 216 ms: 1.40x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 10.2 ms: 1.47x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.08x slower                                                            |

Benchmark hidden because not significant (2): raytrace, pickle_list
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: bpe_tokeniser, unpack_sequence

- Geometric mean (including insignificant results): 1.074x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.00x