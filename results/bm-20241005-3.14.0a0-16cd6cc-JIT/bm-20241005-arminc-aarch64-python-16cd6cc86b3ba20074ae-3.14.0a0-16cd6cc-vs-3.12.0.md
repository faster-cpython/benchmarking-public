# Results vs. 3.12.0

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: linux-aarch64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.072x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 383 ms: 1.24x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.71 sec: 1.24x slower                                                  |
| html5lib       | 65.1 ms                                                               | 71.0 ms: 1.09x slower                                                   |
| tornado_http   | 136 ms                                                                | 147 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.16x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 445 ms: 1.40x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 420 ms: 1.37x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 561 ms: 1.32x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 591 ms: 1.31x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.15 sec: 1.23x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 753 ms: 1.21x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 739 ms: 1.20x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.18 sec: 1.19x faster                                                  |
| Geometric mean             | (ref)                                                                 | 1.28x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 90.0 ms: 1.02x faster                                                   |
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 112 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 262 ms: 1.03x slower                                                    |
| regex_effbot   | 4.64 ms                                                               | 5.02 ms: 1.08x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 31.0 ms: 1.09x slower                                                   |
| regex_compile  | 137 ms                                                                | 184 ms: 1.34x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.13x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 188 ms: 1.04x faster                                                    |
| pickle_dict          | 37.3 us                                                               | 37.7 us: 1.01x slower                                                   |
| json_loads           | 30.7 us                                                               | 31.1 us: 1.01x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                                  |
| pickle               | 13.4 us                                                               | 13.8 us: 1.03x slower                                                   |
| unpickle_pure_python | 260 us                                                                | 268 us: 1.03x slower                                                    |
| xml_etree_process    | 79.0 ms                                                               | 81.5 ms: 1.03x slower                                                   |
| unpickle_list        | 6.17 us                                                               | 6.37 us: 1.03x slower                                                   |
| unpickle             | 18.5 us                                                               | 19.2 us: 1.04x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 386 us: 1.06x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 13.1 ms: 1.07x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (3): pickle_list, xml_etree_iterparse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.73 ms: 1.04x slower                                                   |
| python_startup         | 11.4 ms                                                               | 12.9 ms: 1.14x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.09x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.0 ms: 1.01x slower                                                   |
| genshi_text     | 27.4 ms                                                               | 34.4 ms: 1.25x slower                                                   |
| django_template | 40.7 ms                                                               | 51.8 ms: 1.27x slower                                                   |
| genshi_xml      | 60.6 ms                                                               | 83.1 ms: 1.37x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.22x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 445 ms: 1.40x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 420 ms: 1.37x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 561 ms: 1.32x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 591 ms: 1.31x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 37.9 us: 1.31x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.15 sec: 1.23x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 753 ms: 1.21x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 739 ms: 1.20x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.18 sec: 1.19x faster                                                  |
| pathlib                    | 24.5 ms                                                               | 21.8 ms: 1.13x faster                                                   |
| deepcopy                   | 446 us                                                                | 400 us: 1.11x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.93 us: 1.04x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 188 ms: 1.04x faster                                                    |
| logging_format             | 8.34 us                                                               | 8.11 us: 1.03x faster                                                   |
| float                      | 92.1 ms                                                               | 90.0 ms: 1.02x faster                                                   |
| comprehensions             | 25.4 us                                                               | 24.9 us: 1.02x faster                                                   |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 664 ms: 1.01x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.0 ms: 1.01x slower                                                   |
| pickle_dict                | 37.3 us                                                               | 37.7 us: 1.01x slower                                                   |
| json_loads                 | 30.7 us                                                               | 31.1 us: 1.01x slower                                                   |
| scimark_sor                | 150 ms                                                                | 152 ms: 1.02x slower                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                                  |
| mdp                        | 3.41 sec                                                              | 3.48 sec: 1.02x slower                                                  |
| thrift                     | 937 us                                                                | 960 us: 1.03x slower                                                    |
| pickle                     | 13.4 us                                                               | 13.8 us: 1.03x slower                                                   |
| regex_dna                  | 254 ms                                                                | 262 ms: 1.03x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 150 ms: 1.03x slower                                                    |
| unpickle_pure_python       | 260 us                                                                | 268 us: 1.03x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 81.5 ms: 1.03x slower                                                   |
| logging_silent             | 127 ns                                                                | 131 ns: 1.03x slower                                                    |
| unpickle_list              | 6.17 us                                                               | 6.37 us: 1.03x slower                                                   |
| async_generators           | 491 ms                                                                | 508 ms: 1.04x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 3.91 us: 1.04x slower                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 89.9 ms: 1.04x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.27 sec: 1.04x slower                                                  |
| unpickle                   | 18.5 us                                                               | 19.2 us: 1.04x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.73 ms: 1.04x slower                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 89.1 ms: 1.05x slower                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.37 ms: 1.05x slower                                                   |
| deltablue                  | 4.12 ms                                                               | 4.35 ms: 1.06x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 386 us: 1.06x slower                                                    |
| scimark_fft                | 418 ms                                                                | 446 ms: 1.06x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.1 ms: 1.07x slower                                                   |
| nbody                      | 105 ms                                                                | 112 ms: 1.07x slower                                                    |
| asyncio_tcp                | 566 ms                                                                | 611 ms: 1.08x slower                                                    |
| regex_effbot               | 4.64 ms                                                               | 5.02 ms: 1.08x slower                                                   |
| tornado_http               | 136 ms                                                                | 147 ms: 1.09x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 71.0 ms: 1.09x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 31.0 ms: 1.09x slower                                                   |
| meteor_contest             | 112 ms                                                                | 124 ms: 1.11x slower                                                    |
| spectral_norm              | 131 ms                                                                | 145 ms: 1.11x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.87 ms: 1.11x slower                                                   |
| fannkuch                   | 443 ms                                                                | 503 ms: 1.13x slower                                                    |
| python_startup             | 11.4 ms                                                               | 12.9 ms: 1.14x slower                                                   |
| pyflate                    | 559 ms                                                                | 640 ms: 1.14x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.75 ms: 1.15x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 5.05 ms: 1.15x slower                                                   |
| coverage                   | 87.3 ms                                                               | 101 ms: 1.15x slower                                                    |
| go                         | 157 ms                                                                | 185 ms: 1.18x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.48 sec: 1.18x slower                                                  |
| typing_runtime_protocols   | 181 us                                                                | 213 us: 1.18x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.74 ms: 1.19x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.29 ms: 1.19x slower                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 2.21 ms: 1.21x slower                                                   |
| richards_super             | 58.5 ms                                                               | 72.0 ms: 1.23x slower                                                   |
| sqlglot_normalize          | 126 ms                                                                | 156 ms: 1.24x slower                                                    |
| 2to3                       | 308 ms                                                                | 383 ms: 1.24x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.71 sec: 1.24x slower                                                  |
| nqueens                    | 99.2 ms                                                               | 124 ms: 1.25x slower                                                    |
| richards                   | 50.9 ms                                                               | 63.8 ms: 1.25x slower                                                   |
| genshi_text                | 27.4 ms                                                               | 34.4 ms: 1.25x slower                                                   |
| chaos                      | 71.4 ms                                                               | 90.5 ms: 1.27x slower                                                   |
| django_template            | 40.7 ms                                                               | 51.8 ms: 1.27x slower                                                   |
| dulwich_log                | 62.0 ms                                                               | 80.1 ms: 1.29x slower                                                   |
| sympy_str                  | 280 ms                                                                | 366 ms: 1.31x slower                                                    |
| sympy_expand               | 454 ms                                                                | 598 ms: 1.32x slower                                                    |
| regex_compile              | 137 ms                                                                | 184 ms: 1.34x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 82.2 ms: 1.34x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 1.23 sec: 1.34x slower                                                  |
| generators                 | 43.5 ms                                                               | 59.2 ms: 1.36x slower                                                   |
| sympy_integrate            | 21.6 ms                                                               | 29.6 ms: 1.37x slower                                                   |
| pylint                     | 355 ms                                                                | 486 ms: 1.37x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 83.1 ms: 1.37x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.61 sec: 1.39x slower                                                  |
| sympy_sum                  | 154 ms                                                                | 218 ms: 1.41x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 10.1 ms: 1.45x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 2.07 sec: 293.04x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.14x slower                                                            |

Benchmark hidden because not significant (7): logging_simple, raytrace, pickle_list, xml_etree_iterparse, xml_etree_generate, coroutines, json
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20241005-3.14.0a0-16cd6cc-JIT/bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json: bpe_tokeniser, unpack_sequence

- Geometric mean (including insignificant results): 1.072x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 0.97x