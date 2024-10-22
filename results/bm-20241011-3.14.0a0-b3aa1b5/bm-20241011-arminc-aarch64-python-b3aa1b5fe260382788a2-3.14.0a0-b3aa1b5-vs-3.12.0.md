# Results vs. 3.12.0

- fork: python
- ref: b3aa1b5fe260382788a2
- machine: linux-aarch64
- commit hash: b3aa1b5
- commit date: 2024-10-11
- overall geometric mean: 1.04x slower
- HPT reliability: 91.83%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 293 ms: 1.05x faster                                                    |
| docutils       | 2.98 sec                                                              | 3.03 sec: 1.02x slower                                                  |
| tornado_http   | 136 ms                                                                | 126 ms: 1.08x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                            |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 428 ms: 1.46x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 550 ms: 1.41x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 420 ms: 1.37x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 545 ms: 1.36x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 722 ms: 1.26x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 708 ms: 1.25x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.15 sec: 1.23x faster                                                  |
| async_tree_io              | 1.41 sec                                                              | 1.16 sec: 1.21x faster                                                  |
| Geometric mean             | (ref)                                                                 | 1.32x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| float          | 92.1 ms                                                               | 94.6 ms: 1.03x slower                                                   |
| nbody          | 105 ms                                                                | 115 ms: 1.10x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 124 ms: 1.11x faster                                                    |
| regex_dna      | 254 ms                                                                | 260 ms: 1.02x slower                                                    |
| regex_effbot   | 4.64 ms                                                               | 5.01 ms: 1.08x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 31.0 ms: 1.09x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 260 us                                                                | 255 us: 1.02x faster                                                    |
| pickle_list          | 5.25 us                                                               | 5.17 us: 1.02x faster                                                   |
| json_loads           | 30.7 us                                                               | 31.3 us: 1.02x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 2.65 sec: 1.02x slower                                                  |
| pickle               | 13.4 us                                                               | 13.9 us: 1.04x slower                                                   |
| unpickle             | 18.5 us                                                               | 19.2 us: 1.04x slower                                                   |
| unpickle_list        | 6.17 us                                                               | 6.53 us: 1.06x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 14.6 ms: 1.19x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                            |

Benchmark hidden because not significant (6): pickle_pure_python, xml_etree_generate, pickle_dict, xml_etree_process, xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.68 ms: 1.04x slower                                                   |
| python_startup         | 11.4 ms                                                               | 13.0 ms: 1.15x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.09x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 59.7 ms: 1.01x faster                                                   |
| genshi_text     | 27.4 ms                                                               | 27.1 ms: 1.01x faster                                                   |
| django_template | 40.7 ms                                                               | 42.4 ms: 1.04x slower                                                   |
| mako            | 12.9 ms                                                               | 13.6 ms: 1.05x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 428 ms: 1.46x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 550 ms: 1.41x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 420 ms: 1.37x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 545 ms: 1.36x faster                                                    |
| deepcopy                   | 446 us                                                                | 332 us: 1.34x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 37.8 us: 1.31x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 722 ms: 1.26x faster                                                    |
| generators                 | 43.5 ms                                                               | 34.7 ms: 1.25x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 708 ms: 1.25x faster                                                    |
| comprehensions             | 25.4 us                                                               | 20.7 us: 1.23x faster                                                   |
| async_tree_io_tg           | 1.40 sec                                                              | 1.15 sec: 1.23x faster                                                  |
| async_tree_io              | 1.41 sec                                                              | 1.16 sec: 1.21x faster                                                  |
| deepcopy_reduce            | 4.10 us                                                               | 3.51 us: 1.17x faster                                                   |
| pathlib                    | 24.5 ms                                                               | 21.2 ms: 1.16x faster                                                   |
| go                         | 157 ms                                                                | 137 ms: 1.15x faster                                                    |
| raytrace                   | 353 ms                                                                | 310 ms: 1.14x faster                                                    |
| regex_compile              | 137 ms                                                                | 124 ms: 1.11x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.55 us: 1.10x faster                                                   |
| logging_simple             | 7.63 us                                                               | 6.96 us: 1.10x faster                                                   |
| sympy_sum                  | 154 ms                                                                | 142 ms: 1.09x faster                                                    |
| scimark_lu                 | 146 ms                                                                | 134 ms: 1.09x faster                                                    |
| tornado_http               | 136 ms                                                                | 126 ms: 1.08x faster                                                    |
| dulwich_log                | 62.0 ms                                                               | 58.0 ms: 1.07x faster                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 81.5 ms: 1.06x faster                                                   |
| sympy_str                  | 280 ms                                                                | 264 ms: 1.06x faster                                                    |
| 2to3                       | 308 ms                                                                | 293 ms: 1.05x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 3.92 ms: 1.05x faster                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 1.74 ms: 1.05x faster                                                   |
| async_generators           | 491 ms                                                                | 475 ms: 1.03x faster                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.42 ms: 1.03x faster                                                   |
| mdp                        | 3.41 sec                                                              | 3.33 sec: 1.03x faster                                                  |
| bench_thread_pool          | 1.31 ms                                                               | 1.28 ms: 1.03x faster                                                   |
| sympy_integrate            | 21.6 ms                                                               | 21.1 ms: 1.02x faster                                                   |
| unpickle_pure_python       | 260 us                                                                | 255 us: 1.02x faster                                                    |
| coroutines                 | 29.0 ms                                                               | 28.5 ms: 1.02x faster                                                   |
| pickle_list                | 5.25 us                                                               | 5.17 us: 1.02x faster                                                   |
| genshi_xml                 | 60.6 ms                                                               | 59.7 ms: 1.01x faster                                                   |
| pycparser                  | 1.26 sec                                                              | 1.24 sec: 1.01x faster                                                  |
| chaos                      | 71.4 ms                                                               | 70.5 ms: 1.01x faster                                                   |
| genshi_text                | 27.4 ms                                                               | 27.1 ms: 1.01x faster                                                   |
| meteor_contest             | 112 ms                                                                | 111 ms: 1.01x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 84.5 ms: 1.01x faster                                                   |
| pprint_safe_repr           | 916 ms                                                                | 911 ms: 1.01x faster                                                    |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.21 sec: 1.01x slower                                                  |
| docutils                   | 2.98 sec                                                              | 3.03 sec: 1.02x slower                                                  |
| sqlglot_optimize           | 61.3 ms                                                               | 62.3 ms: 1.02x slower                                                   |
| json_loads                 | 30.7 us                                                               | 31.3 us: 1.02x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 7.11 ms: 1.02x slower                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.65 sec: 1.02x slower                                                  |
| logging_silent             | 127 ns                                                                | 130 ns: 1.02x slower                                                    |
| regex_dna                  | 254 ms                                                                | 260 ms: 1.02x slower                                                    |
| richards_super             | 58.5 ms                                                               | 59.9 ms: 1.02x slower                                                   |
| float                      | 92.1 ms                                                               | 94.6 ms: 1.03x slower                                                   |
| sqlite_synth               | 3.77 us                                                               | 3.90 us: 1.04x slower                                                   |
| pickle                     | 13.4 us                                                               | 13.9 us: 1.04x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.68 ms: 1.04x slower                                                   |
| richards                   | 50.9 ms                                                               | 52.9 ms: 1.04x slower                                                   |
| unpickle                   | 18.5 us                                                               | 19.2 us: 1.04x slower                                                   |
| pyflate                    | 559 ms                                                                | 582 ms: 1.04x slower                                                    |
| django_template            | 40.7 ms                                                               | 42.4 ms: 1.04x slower                                                   |
| mako                       | 12.9 ms                                                               | 13.6 ms: 1.05x slower                                                   |
| scimark_fft                | 418 ms                                                                | 441 ms: 1.05x slower                                                    |
| unpickle_list              | 6.17 us                                                               | 6.53 us: 1.06x slower                                                   |
| fannkuch                   | 443 ms                                                                | 471 ms: 1.06x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.60 ms: 1.07x slower                                                   |
| spectral_norm              | 131 ms                                                                | 140 ms: 1.07x slower                                                    |
| scimark_sor                | 150 ms                                                                | 161 ms: 1.08x slower                                                    |
| regex_effbot               | 4.64 ms                                                               | 5.01 ms: 1.08x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 196 us: 1.08x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 31.0 ms: 1.09x slower                                                   |
| telco                      | 8.51 ms                                                               | 9.31 ms: 1.09x slower                                                   |
| nbody                      | 105 ms                                                                | 115 ms: 1.10x slower                                                    |
| coverage                   | 87.3 ms                                                               | 97.9 ms: 1.12x slower                                                   |
| python_startup             | 11.4 ms                                                               | 13.0 ms: 1.15x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 5.09 ms: 1.16x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 14.6 ms: 1.19x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.37 ms: 1.24x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 5.11 sec: 724.80x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.04x slower                                                            |

Benchmark hidden because not significant (16): html5lib, thrift, asyncio_tcp, pickle_pure_python, asyncio_websockets, xml_etree_generate, pprint_pformat, pylint, sqlglot_normalize, sympy_expand, json, nqueens, pickle_dict, xml_etree_process, xml_etree_iterparse, xml_etree_parse
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20241011-3.14.0a0-b3aa1b5/bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5.json: bpe_tokeniser, unpack_sequence

# HPT report

- Reliability score: 91.83% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.92x