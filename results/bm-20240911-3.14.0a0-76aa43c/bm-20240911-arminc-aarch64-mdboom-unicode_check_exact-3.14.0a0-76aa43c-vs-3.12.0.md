# Results vs. 3.12.0

- fork: mdboom
- ref: unicode_check_exact
- machine: linux-aarch64
- commit hash: 76aa43c
- commit date: 2024-09-11
- overall geometric mean: 1.04x faster
- HPT reliability: 99.88%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 298 ms: 1.03x faster                                                   |
| html5lib       | 65.1 ms                                                               | 64.1 ms: 1.02x faster                                                  |
| tornado_http   | 136 ms                                                                | 127 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                           |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 424 ms: 1.47x faster                                                   |
| async_tree_memoization     | 777 ms                                                                | 555 ms: 1.40x faster                                                   |
| async_tree_none_tg         | 577 ms                                                                | 416 ms: 1.39x faster                                                   |
| async_tree_memoization_tg  | 740 ms                                                                | 548 ms: 1.35x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 727 ms: 1.26x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.15 sec: 1.23x faster                                                 |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 722 ms: 1.22x faster                                                   |
| async_tree_io_tg           | 1.40 sec                                                              | 1.17 sec: 1.20x faster                                                 |
| Geometric mean             | (ref)                                                                 | 1.31x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                   |
| nbody          | 105 ms                                                                | 109 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                           |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 124 ms: 1.11x faster                                                   |
| regex_dna      | 254 ms                                                                | 246 ms: 1.03x faster                                                   |
| regex_effbot   | 4.64 ms                                                               | 4.93 ms: 1.06x slower                                                  |
| regex_v8       | 28.3 ms                                                               | 31.0 ms: 1.09x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 187 ms: 1.04x faster                                                   |
| unpickle_pure_python | 260 us                                                                | 250 us: 1.04x faster                                                   |
| pickle_pure_python   | 365 us                                                                | 358 us: 1.02x faster                                                   |
| xml_etree_generate   | 112 ms                                                                | 111 ms: 1.01x faster                                                   |
| tomli_loads          | 2.59 sec                                                              | 2.61 sec: 1.01x slower                                                 |
| pickle_dict          | 37.3 us                                                               | 37.9 us: 1.02x slower                                                  |
| pickle               | 13.4 us                                                               | 13.7 us: 1.02x slower                                                  |
| json_loads           | 30.7 us                                                               | 31.6 us: 1.03x slower                                                  |
| unpickle_list        | 6.17 us                                                               | 6.39 us: 1.04x slower                                                  |
| unpickle             | 18.5 us                                                               | 19.4 us: 1.05x slower                                                  |
| json_dumps           | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                  |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                           |

Benchmark hidden because not significant (3): xml_etree_iterparse, pickle_list, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.62 ms: 1.03x slower                                                  |
| python_startup         | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                                  |
| Geometric mean         | (ref)                                                                 | 1.09x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 59.4 ms: 1.02x faster                                                  |
| mako            | 12.9 ms                                                               | 13.3 ms: 1.03x slower                                                  |
| django_template | 40.7 ms                                                               | 42.7 ms: 1.05x slower                                                  |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                           |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 424 ms: 1.47x faster                                                   |
| async_tree_memoization     | 777 ms                                                                | 555 ms: 1.40x faster                                                   |
| async_tree_none_tg         | 577 ms                                                                | 416 ms: 1.39x faster                                                   |
| deepcopy                   | 446 us                                                                | 328 us: 1.36x faster                                                   |
| async_tree_memoization_tg  | 740 ms                                                                | 548 ms: 1.35x faster                                                   |
| deepcopy_memo              | 49.6 us                                                               | 37.3 us: 1.33x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 727 ms: 1.26x faster                                                   |
| generators                 | 43.5 ms                                                               | 34.7 ms: 1.25x faster                                                  |
| comprehensions             | 25.4 us                                                               | 20.4 us: 1.24x faster                                                  |
| async_tree_io              | 1.41 sec                                                              | 1.15 sec: 1.23x faster                                                 |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 722 ms: 1.22x faster                                                   |
| async_tree_io_tg           | 1.40 sec                                                              | 1.17 sec: 1.20x faster                                                 |
| deepcopy_reduce            | 4.10 us                                                               | 3.49 us: 1.18x faster                                                  |
| raytrace                   | 353 ms                                                                | 302 ms: 1.17x faster                                                   |
| go                         | 157 ms                                                                | 136 ms: 1.16x faster                                                   |
| pathlib                    | 24.5 ms                                                               | 21.2 ms: 1.16x faster                                                  |
| sympy_sum                  | 154 ms                                                                | 139 ms: 1.11x faster                                                   |
| regex_compile              | 137 ms                                                                | 124 ms: 1.11x faster                                                   |
| logging_simple             | 7.63 us                                                               | 6.92 us: 1.10x faster                                                  |
| logging_format             | 8.34 us                                                               | 7.62 us: 1.10x faster                                                  |
| scimark_lu                 | 146 ms                                                                | 135 ms: 1.07x faster                                                   |
| tornado_http               | 136 ms                                                                | 127 ms: 1.07x faster                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.22 ms: 1.07x faster                                                  |
| dulwich_log                | 62.0 ms                                                               | 57.9 ms: 1.07x faster                                                  |
| sympy_str                  | 280 ms                                                                | 261 ms: 1.07x faster                                                   |
| deltablue                  | 4.12 ms                                                               | 3.89 ms: 1.06x faster                                                  |
| sqlglot_transpile          | 1.83 ms                                                               | 1.73 ms: 1.06x faster                                                  |
| crypto_pyaes               | 86.6 ms                                                               | 81.9 ms: 1.06x faster                                                  |
| sympy_integrate            | 21.6 ms                                                               | 20.6 ms: 1.05x faster                                                  |
| pycparser                  | 1.26 sec                                                              | 1.20 sec: 1.05x faster                                                 |
| xml_etree_parse            | 195 ms                                                                | 187 ms: 1.04x faster                                                   |
| chaos                      | 71.4 ms                                                               | 68.5 ms: 1.04x faster                                                  |
| unpickle_pure_python       | 260 us                                                                | 250 us: 1.04x faster                                                   |
| mdp                        | 3.41 sec                                                              | 3.29 sec: 1.04x faster                                                 |
| sqlglot_parse              | 1.46 ms                                                               | 1.42 ms: 1.03x faster                                                  |
| regex_dna                  | 254 ms                                                                | 246 ms: 1.03x faster                                                   |
| 2to3                       | 308 ms                                                                | 298 ms: 1.03x faster                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 82.4 ms: 1.03x faster                                                  |
| async_generators           | 491 ms                                                                | 476 ms: 1.03x faster                                                   |
| coroutines                 | 29.0 ms                                                               | 28.3 ms: 1.03x faster                                                  |
| nqueens                    | 99.2 ms                                                               | 97.0 ms: 1.02x faster                                                  |
| genshi_xml                 | 60.6 ms                                                               | 59.4 ms: 1.02x faster                                                  |
| pickle_pure_python         | 365 us                                                                | 358 us: 1.02x faster                                                   |
| thrift                     | 937 us                                                                | 921 us: 1.02x faster                                                   |
| html5lib                   | 65.1 ms                                                               | 64.1 ms: 1.02x faster                                                  |
| pprint_safe_repr           | 916 ms                                                                | 904 ms: 1.01x faster                                                   |
| pprint_pformat             | 1.88 sec                                                              | 1.86 sec: 1.01x faster                                                 |
| xml_etree_generate         | 112 ms                                                                | 111 ms: 1.01x faster                                                   |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.61 sec: 1.01x slower                                                 |
| sympy_expand               | 454 ms                                                                | 457 ms: 1.01x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.21 sec: 1.01x slower                                                 |
| richards_super             | 58.5 ms                                                               | 59.4 ms: 1.02x slower                                                  |
| pickle_dict                | 37.3 us                                                               | 37.9 us: 1.02x slower                                                  |
| sqlglot_optimize           | 61.3 ms                                                               | 62.4 ms: 1.02x slower                                                  |
| pickle                     | 13.4 us                                                               | 13.7 us: 1.02x slower                                                  |
| hexiom                     | 6.98 ms                                                               | 7.11 ms: 1.02x slower                                                  |
| sqlite_synth               | 3.77 us                                                               | 3.88 us: 1.03x slower                                                  |
| python_startup_no_site     | 8.37 ms                                                               | 8.62 ms: 1.03x slower                                                  |
| json_loads                 | 30.7 us                                                               | 31.6 us: 1.03x slower                                                  |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.39 ms: 1.03x slower                                                  |
| mako                       | 12.9 ms                                                               | 13.3 ms: 1.03x slower                                                  |
| scimark_sor                | 150 ms                                                                | 155 ms: 1.03x slower                                                   |
| fannkuch                   | 443 ms                                                                | 459 ms: 1.03x slower                                                   |
| unpickle_list              | 6.17 us                                                               | 6.39 us: 1.04x slower                                                  |
| richards                   | 50.9 ms                                                               | 52.8 ms: 1.04x slower                                                  |
| logging_silent             | 127 ns                                                                | 132 ns: 1.04x slower                                                   |
| nbody                      | 105 ms                                                                | 109 ms: 1.04x slower                                                   |
| scimark_fft                | 418 ms                                                                | 439 ms: 1.05x slower                                                   |
| django_template            | 40.7 ms                                                               | 42.7 ms: 1.05x slower                                                  |
| unpickle                   | 18.5 us                                                               | 19.4 us: 1.05x slower                                                  |
| typing_runtime_protocols   | 181 us                                                                | 191 us: 1.06x slower                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.93 ms: 1.06x slower                                                  |
| spectral_norm              | 131 ms                                                                | 142 ms: 1.08x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 31.0 ms: 1.09x slower                                                  |
| json_dumps                 | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                  |
| coverage                   | 87.3 ms                                                               | 97.7 ms: 1.12x slower                                                  |
| gc_traversal               | 4.40 ms                                                               | 5.02 ms: 1.14x slower                                                  |
| python_startup             | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                                  |
| create_gc_cycles           | 1.92 ms                                                               | 2.27 ms: 1.18x slower                                                  |
| telco                      | 8.51 ms                                                               | 10.2 ms: 1.19x slower                                                  |
| Geometric mean             | (ref)                                                                 | 1.04x faster                                                           |

Benchmark hidden because not significant (14): xml_etree_iterparse, genshi_text, pickle_list, asyncio_websockets, meteor_contest, bench_mp_pool, pyflate, float, json, asyncio_tcp, xml_etree_process, docutils, sqlglot_normalize, pylint
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240911-3.14.0a0-76aa43c/bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c.json: bpe_tokeniser, unpack_sequence

# HPT report

- Reliability score: 99.88% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x